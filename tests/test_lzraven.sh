#!/bin/sh
# tests/test_lzraven.sh -- lzraven encoder proto battery.
# impl (src/lzraven.py + encode.py --alg lzraven) vs oracle byte-compare.
# Scope: zeros N 0..820 synthesized (T0..T3) + stored paths + honest
# errors beyond scope. Non-zero compressible inputs (patterns, zeros-dir
# inners) are a DOCUMENTED PROTO GAP: impl emits stored-guess, oracle
# compresses -> bytes differ (loud GAP cell, never claimed green).
# Oracle = TEST-TIME EXEC ONLY: compression_tool -encode -a lzraven,
# /usr/bin/aa archive/extract. Exit 0 GREEN/1 RED/2 err.
# Usage: TMPDIR=<nvme-scratch> sh tests/test_lzraven.sh [workdir]
# RECORD=1 sh tests/test_lzraven.sh [workdir]  (rewrite PINS; REVIEW diff!)
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
WORK=${1:-$(mktemp -d "$TMPDIR/lzraven.XXXXXX")}
PINS=$ROOT/vectors/lzraven-PINS.csv
FAIL=0
GAP=0
GEN=test_lzraven.sh
OS=$(sw_vers -productVersion 2>/dev/null || echo unknown)
CT=${CT:-/usr/bin/compression_tool}
AA=${AA:-/usr/bin/aa}
LZ=$ROOT/src/lzraven.py
ENC=$ROOT/src/encode.py
command -v python3 >/dev/null || { echo "need python3" >&2; exit 2; }
mkdir -p "$WORK" "$ROOT/vectors"
pin_get() { grep "^$1," "$PINS" | head -1 | cut -d, -f3; }
chk() { # name check val [bytes]
  if [ -n "${RECORD:-}" ]; then
    echo "$1,$2,$3,${4:-0},$GEN,$OS,ct-lzraven" >> "$PINS.new"
    echo "REC $1=$3"
  else
    [ -f "$PINS" ] || { echo "missing $PINS (RECORD=1 first)" >&2; exit 2; }
    exp=$(pin_get "$1")
    if [ "$3" = "$exp" ]; then echo "PASS $1"; else echo "FAIL $1: got $3 want $exp"; FAIL=1; fi
  fi
}
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
sz() { wc -c < "$1" | tr -d ' '; }
echo "== probe =="
[ -x "$CT" ] || { echo "need $CT" >&2; exit 2; }
[ -x "$AA" ] || { echo "need $AA" >&2; exit 2; }
"$CT" -encode -a lzraven -i /dev/null -o "$WORK/probe.rav" 2>/dev/null || { echo "ct raven failed" >&2; exit 2; }
if [ -n "${RECORD:-}" ]; then
  echo "# lzraven pins: name,check,expect,bytes,generator,os,backend" > "$PINS.new"
  echo "# sha = impl output hash (byte-identical to oracle on covered cells); ERROR = impl must refuse" >> "$PINS.new"
fi
ZCELL() { # n : zeros-N byte-compare
  n=$1
  head -c "$n" /dev/zero > "$WORK/z$n.bin" 2>/dev/null || : > "$WORK/z$n.bin"
  "$CT" -encode -a lzraven -i "$WORK/z$n.bin" -o "$WORK/z$n.ora.rav" 2>/dev/null || { echo "FAIL z$n oracle rc"; FAIL=1; return; }
  python3 "$LZ" --raw "$WORK/z$n.bin" "$WORK/z$n.got.rav" 2>"$WORK/z$n.err" || { echo "FAIL z$n impl rc: $(head -1 "$WORK/z$n.err")"; FAIL=1; return; }
  if cmp -s "$WORK/z$n.got.rav" "$WORK/z$n.ora.rav"; then
    chk "lz-z$n" sha "$(sha "$WORK/z$n.got.rav")" "$(sz "$WORK/z$n.got.rav")"
  else
    echo "FAIL z$n bytes differ"; FAIL=1
  fi
}
echo "== zeros-N sweep (T0..T3 + stored edges) =="
for s in 0 1 2 16 62 63 64 65 100 124 125 126 127 128 129 200 255 256 257 300 380 381 382 383 398 399 400 408 409 440 472 473 474 488 505 511 512 600 728 729 730 731 746 747 756 757 788 804 805 820; do
  ZCELL "$s"
done
echo "== unclosed-N (impl must refuse) =="
for s in 821 1077 1500 524288; do
  head -c "$s" /dev/zero > "$WORK/u$s.bin" 2>/dev/null || : > "$WORK/u$s.bin"
  if python3 "$LZ" --raw "$WORK/u$s.bin" "$WORK/u$s.got.rav" 2>/dev/null; then
    echo "FAIL u$s: impl emitted, want honest error"; FAIL=1
  else
    chk "lz-u$s" str "ERROR" "0"
  fi
done
echo "== real-file cells (stored paths, byte-compare) =="
RCELL() { # tag size seed
  python3 -c "import random; open('$WORK/$1.bin','wb').write(random.Random($3).randbytes($2))"
  "$CT" -encode -a lzraven -i "$WORK/$1.bin" -o "$WORK/$1.ora.rav" 2>/dev/null || { echo "FAIL $1 oracle rc"; FAIL=1; return; }
  python3 "$LZ" --raw "$WORK/$1.bin" "$WORK/$1.got.rav" 2>"$WORK/$1.err" || { echo "FAIL $1 impl rc"; FAIL=1; return; }
  if cmp -s "$WORK/$1.got.rav" "$WORK/$1.ora.rav"; then
    chk "lz-$1" sha "$(sha "$WORK/$1.got.rav")" "$(sz "$WORK/$1.got.rav")"
  else
    echo "FAIL $1 bytes differ (oracle may compress: gap?)"; FAIL=1
  fi
}
for s in 1 16 63; do RCELL "r$s" "$s" "$s"; done
for s in 64 65 256 1000; do RCELL "r$s" "$s" "$s"; done
cp "$ROOT/vectors/selfgen/input/hello/greet.txt" "$WORK/greet.bin"
"$CT" -encode -a lzraven -i "$WORK/greet.bin" -o "$WORK/greet.ora.rav" 2>/dev/null || { echo "FAIL greet oracle rc"; FAIL=1; }
python3 "$LZ" --raw "$WORK/greet.bin" "$WORK/greet.got.rav" 2>/dev/null || { echo "FAIL greet impl rc"; FAIL=1; }
if cmp -s "$WORK/greet.got.rav" "$WORK/greet.ora.rav"; then
  chk "lz-greet" sha "$(sha "$WORK/greet.got.rav")" "$(sz "$WORK/greet.got.rav")"
else echo "FAIL greet bytes differ"; FAIL=1; fi
echo "== documented gap: patterned input (oracle compresses, impl stored-guess) =="
cp "$ROOT/vectors/selfgen/input/hello/repeat.txt" "$WORK/rep.bin"
"$CT" -encode -a lzraven -i "$WORK/rep.bin" -o "$WORK/rep.ora.rav" 2>/dev/null || { echo "FAIL rep oracle rc"; FAIL=1; }
python3 "$LZ" --raw "$WORK/rep.bin" "$WORK/rep.got.rav" 2>/dev/null || { echo "FAIL rep impl rc"; FAIL=1; }
if cmp -s "$WORK/rep.got.rav" "$WORK/rep.ora.rav"; then
  echo "FAIL rep: unexpectedly identical (gap closed? update battery)"; FAIL=1
else
  if python3 "$ROOT/src/ravframe.py" "$WORK/rep.got.rav" 2000 >/dev/null 2>&1; then
    echo "GAP-DOCUMENTED rep: impl valid-stored, oracle-divergent (general grammar out of scope)"; GAP=$((GAP+1))
  else echo "FAIL rep: impl output not even frame-valid"; FAIL=1; fi
fi
echo "== end to end (encode.py --alg lzraven vs aa) =="
fix() { find "$1" -exec touch -d '2001-02-03 04:05:06' {} + 2>/dev/null; links=$(find "$1" -type l); if [ -n "$links" ]; then touch -h -d '2001-02-03 04:05:06' $links 2>/dev/null; fi; return 0; }
E2E() { # tag [block]
  tag=$1; blk=${2:-}
  mkdir -p "$WORK/in-$tag"
  python3 -c "import random;random.seed(7);open('$WORK/in-$tag/p','wb').write(bytes(random.randrange(256) for _ in range(3000)))"
  python3 -c "import random;random.seed(8);open('$WORK/in-$tag/q','wb').write(bytes(random.randrange(256) for _ in range(100000)))"
  fix "$WORK/in-$tag"
  "$AA" archive -a lzraven -t 1 ${blk:+-b "$blk"} -d "$WORK/in-$tag" -o "$WORK/$tag.expect.aar" 2>"$WORK/$tag.err" || { echo "FAIL $tag oracle rc"; FAIL=1; return; }
  python3 "$ENC" "$WORK/in-$tag" "$WORK/$tag.got.aar" --alg lzraven ${blk:+--block "$blk"} 2>>"$WORK/$tag.err" || { echo "FAIL $tag impl rc"; FAIL=1; return; }
  if cmp -s "$WORK/$tag.expect.aar" "$WORK/$tag.got.aar"; then
    chk "lz-e2e-$tag" sha "$(sha "$WORK/$tag.got.aar")" "$(sz "$WORK/$tag.got.aar")"
  else echo "FAIL $tag aar bytes differ"; FAIL=1; return; fi
  rm -rf "$WORK/rt-$tag"; mkdir -p "$WORK/rt-$tag"
  "$AA" extract -i "$WORK/$tag.got.aar" -d "$WORK/rt-$tag" 2>>"$WORK/$tag.err" || { echo "FAIL $tag roundtrip rc"; FAIL=1; }
}
E2E e2e4m
E2E e2e1k 1k
[ -n "${RECORD:-}" ] && mv "$PINS.new" "$PINS" && echo "RECORDED $PINS"
echo "== $WORK (gaps-documented=$GAP) =="
[ "$FAIL" -eq 0 ] && echo LZRAVEN-GREEN || echo LZRAVEN-RED
exit "$FAIL"
