#!/bin/sh
# test_ravframe.sh -- raven frame-layer battery (NOTE-w2s4-9).
# ravframe.py verifies oracle bytes structurally (magic/F2/frames/
# trailer); output must CLOSE on every cell (proves framing rules;
# codec payload bytes stay opaque, bed-war replaces oracles later).
# Oracle = TEST-TIME EXEC ONLY, never shipped: compression_tool
# -encode -a lzraven (A-13, POC IDENTICAL). Exit 0 GREEN/1 RED/2 err.
# Usage: sh tests/test_ravframe.sh [workdir]
# RECORD=1 sh tests/test_ravframe.sh [workdir]  (rewrite PINS; REVIEW diff!)
set -eu
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
WORK=${1:-$(mktemp -d "$TMPDIR/ravframe.XXXXXX")}
PINS=$ROOT/vectors/ravframe-PINS.csv
FAIL=0
GEN=test_ravframe.sh
OS=$(sw_vers -productVersion 2>/dev/null || echo unknown)
CT=${CT:-/usr/bin/compression_tool}
RAV=$ROOT/src/ravframe.py
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
"$CT" -encode -a lzraven -i /dev/null -o "$WORK/probe.bin" 2>/dev/null || { echo "ct raven failed" >&2; exit 2; }
if [ -n "${RECORD:-}" ]; then
  echo "# ravframe pins: name,check,expect,bytes,generator,os,backend" > "$PINS.new"
  echo "# closed = ravframe structural verdict; f2 = F2 field hex; sha = output hash (deterministic inputs)" >> "$PINS.new"
fi
mk() { # tag nbytes z|seedN|pat
  case "$3" in
    z) head -c "$2" /dev/zero > "$WORK/$1.bin";;
    seed*) python3 -c "import random; open('$WORK/$1.bin','wb').write(random.Random(${3#seed}).randbytes($2))";;
    pat) python3 -c "open('$WORK/$1.bin','wb').write((b'ABCDEFGH'*(($2+7)//8))[:$2])";;
  esac
}
CELL() { # tag nbytes kind : closed + f2 + sha pins (+ store pin)
  tag=$1; n=$2; kind=$3
  mk "$tag" "$n" "$kind"
  "$CT" -encode -a lzraven -i "$WORK/$tag.bin" -o "$WORK/$tag.rav" 2>/dev/null || { echo "FAIL $tag ct rc"; FAIL=1; return; }
  if v=$(python3 "$RAV" "$WORK/$tag.rav" "$n" 2>"$WORK/$tag.ravf"); then
    case "$v" in
      *CLOSED*) c=CLOSED;; *) c=BAD;;
    esac
    chk "f-$tag-closed" str "$c" "$(sz "$WORK/$tag.rav")"
    f2=$(python3 -c "import struct;print('%08x' % struct.unpack('<I', open('$WORK/$tag.rav','rb').read()[4:8])[0])" 2>/dev/null || echo none)
    if [ "$n" -eq 0 ]; then f2=00000000; fi
    chk "f-$tag-f2" str "$f2" "$(sz "$WORK/$tag.rav")"
    chk "f-$tag" sha "$(sha "$WORK/$tag.rav")" "$(sz "$WORK/$tag.rav")"
  else echo "FAIL $tag ravframe: $(head -1 "$WORK/$tag.ravf")"; FAIL=1; fi
}
echo "== ravframe empty (oracle 12B form, no rawlen) =="
if v=$(python3 "$RAV" "$WORK/probe.bin" 2>"$WORK/empty12.err"); then
  case "$v" in *CLOSED*) echo "PASS e12-closed";; *) echo "FAIL e12-closed: $v"; FAIL=1;; esac
else echo "FAIL e12 rc: $(head -1 "$WORK/empty12.err")"; FAIL=1; fi
python3 -c "open('$WORK/bad12.rav','wb').write(bytes.fromhex('2b00caec00000000ffffffff'))"
if python3 "$RAV" "$WORK/bad12.rav" 2>/dev/null; then echo "FAIL e12bad: accepted bad 12B"; FAIL=1;
else echo "PASS e12bad"; fi
echo "== ravframe random (F2 steps + frames) =="
for s in 0 1 8 63 64 65 1000 65536 65537 81920 81921 98304 98305 114688 114689 131072 131073 196608 196609 229376 229377 262144 262145 327680 327681 393216 393217 458752 458753 524287 524288 524289 532480 532481 600000 655360 655361 786432 786433 917504 917505 1000000 1048576 1048577 1100000; do
  CELL "r$s" "$s" "seed$s"
done
echo "== ravframe zeros (store rule + min-64 + multi-frame) =="
for s in 63 64 65 1000 100000 524289 600000 1000000; do
  CELL "z$s" "$s" z
done
echo "== ravframe pattern =="
for s in 64 1000; do
  CELL "p$s" "$s" pat
done
SCELL() { # tag nbytes kind : CELL + --raw verbatim pin (all-stored only)
  tag=$1; n=$2; kind=$3
  mk "$tag" "$n" "$kind"
  "$CT" -encode -a lzraven -i "$WORK/$tag.bin" -o "$WORK/$tag.rav" 2>/dev/null || { echo "FAIL $tag ct rc"; FAIL=1; return; }
  if v=$(python3 "$RAV" "$WORK/$tag.rav" "$n" --raw "$WORK/$tag.bin" 2>"$WORK/$tag.ravf"); then
    case "$v" in
      *CLOSED*) c=CLOSED;; *) c=BAD;;
    esac
    case "$v" in
      *rawmatch*) m=MATCH;; *) m=SKIP;;
    esac
    chk "f-$tag-closed" str "$c" "$(sz "$WORK/$tag.rav")"
    f2=$(python3 -c "import struct;print('%08x' % struct.unpack('<I', open('$WORK/$tag.rav','rb').read()[4:8])[0])" 2>/dev/null || echo none)
    chk "f-$tag-f2" str "$f2" "$(sz "$WORK/$tag.rav")"
    chk "f-$tag" sha "$(sha "$WORK/$tag.rav")" "$(sz "$WORK/$tag.rav")"
    chk "f-$tag-rawmatch" str "$m" "$(sz "$WORK/$tag.rav")"
  else echo "FAIL $tag ravframe: $(head -1 "$WORK/$tag.ravf")"; FAIL=1; fi
}
echo "== ravframe stored verbatim =="
for s in 1 16 256 4096; do
  SCELL "st$s" "$s" "seed$s"
done
[ -n "${RECORD:-}" ] && mv "$PINS.new" "$PINS" && echo "RECORDED $PINS"
echo "== $WORK =="
[ "$FAIL" -eq 0 ] && echo RAVFRAME-GREEN || echo RAVFRAME-RED
exit "$FAIL"
