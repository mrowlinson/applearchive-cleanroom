#!/bin/sh
# tests/test_lzraven_c.sh -- C-parity battery (unified aar-encode --alg lzraven
# + C stream harness vs oracle pins + vs py bytes).
# Bed-style like test_lz4_c.sh: every cell encodes byte-identical under
# py (src/lzraven.py + src/encode.py) and C, and C output matches the
# oracle-bedded pins in vectors/lzraven-PINS.csv (C-vs-oracle) with live
# compression_tool / aa byte-compare on top.
# Covers: zeros sweep T0..T3 + stored edges, stored randoms, greet,
# unclosed refusals (exit code + stderr byte-identical), the documented
# STORED-GUESS gap cell (py==C, oracle-divergent, stays loud), and the two
# e2e .aar cells incl. a 1k-block multi-block chain.
# Mapping to tests/test_lzraven.sh cells: ZCELL lz-zN -> stream cells here;
# RCELL lz-rN + lz-greet -> stored cells here; lz-uN -> refusal cells here;
# rep GAP -> gap cell here; lz-e2e-* -> e2e cells here (also runnable with
# ENC_BIN=$AAE_C in test_lzraven.sh).
# UNIFIED MAPPING (cport-unify): old `"$AAE_C" <dir> <out> --alg lzraven ...`
# e2e cells are now `"$CLI" aar-encode --alg lzraven ... <dir> <out>` — same
# ae_main code path, same bytes, same exits (e2e cells are success paths;
# refusal cells use the committed stream harness, untouched). Cell count and
# oracle comparisons unchanged.
# Usage: TMPDIR=<nvme-scratch> sh tests/test_lzraven_c.sh [workdir]
# Needs: CLI (default WS unified build), CT, AA. Exit 0 GREEN/1 RED/2 setup.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
WORK=${1:-$(mktemp -d "$TMPDIR/lzravenc.XXXXXX")}
PINS=$ROOT/vectors/lzraven-PINS.csv
CLI=${CLI:-/Volumes/NVME/applearchive-cleanroom-ws/build/unified/aae-cli}
CT=${CT:-/usr/bin/compression_tool}
AA=${AA:-/usr/bin/aa}
FAIL=0
GAP=0
GEN=test_lzraven_c.sh
[ -x "$CLI" ] || { echo "need unified binary: $CLI (CLI=...)" >&2; exit 2; }
[ -x "$CT" ] || { echo "need $CT" >&2; exit 2; }
[ -x "$AA" ] || { echo "need $AA" >&2; exit 2; }
[ -f "$PINS" ] || { echo "missing $PINS" >&2; exit 2; }
command -v cc >/dev/null || { echo "need cc" >&2; exit 2; }
mkdir -p "$WORK"
pin_get() { grep "^$1," "$PINS" | head -1 | cut -d, -f3; }
chk() { # name check val [bytes]
  exp=$(pin_get "$1")
  if [ "$3" = "$exp" ]; then echo "PASS $1"; else echo "FAIL $1: got $3 want $exp"; FAIL=1; fi
}
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
sz() { wc -c < "$1" | tr -d ' '; }
echo "== build C stream harness (committed sources only) =="
cat > "$WORK/ravmain.c" <<'EOF'
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lzravenc.h"
int main(int argc, char **argv) {
    if (argc != 4 || strcmp(argv[1], "--raw")) {
        fprintf(stderr, "usage: lzraven.py --raw INFILE OUTFILE\n"); return 2;
    }
    FILE *fi = fopen(argv[2], "rb");
    if (!fi) { fprintf(stderr, "lzraven: read %s: %s\n", argv[2], strerror(errno)); return 1; }
    fseek(fi, 0, SEEK_END); long z = ftell(fi); fseek(fi, 0, SEEK_SET);
    if (z < 0) { fprintf(stderr, "lzraven: read %s: %s\n", argv[2], strerror(errno)); return 1; }
    uint8_t *d = malloc((size_t)z + 1); if (!d) exit(1);
    if (z > 0 && fread(d, 1, (size_t)z, fi) != (size_t)z) {
        fprintf(stderr, "lzraven: read %s: %s\n", argv[2], strerror(errno)); return 1;
    }
    fclose(fi);
    char err[256]; size_t on = 0;
    uint8_t *o = lzraven_encode_stream(d, (size_t)z, &on, err, sizeof err);
    if (!o) { fprintf(stderr, "lzraven: unclosed: %s\n", err); free(d); return 1; }
    FILE *f = fopen(argv[3], "wb");
    if (!f) { fprintf(stderr, "lzraven: write %s: %s\n", argv[3], strerror(errno)); free(d); free(o); return 1; }
    if (on && fwrite(o, 1, on, f) != on) {
        fprintf(stderr, "lzraven: write %s: %s\n", argv[3], strerror(errno)); return 1;
    }
    fclose(f); free(d); free(o); return 0;
}
EOF
cc -O2 -Wall -Wextra -std=c11 -I"$ROOT/src/c" -o "$WORK/ravstream" \
  "$WORK/ravmain.c" "$ROOT/src/c/lzravenc.c" || { echo "harness build failed" >&2; exit 2; }
ZCELL() { # n : zeros-N triple compare (oracle vs py vs C) + pins
  n=$1
  if [ "$n" -eq 0 ]; then : > "$WORK/z$n.bin"; else head -c "$n" /dev/zero > "$WORK/z$n.bin" 2>/dev/null || { echo "FAIL z$n input"; FAIL=1; return; }; fi
  [ "$(sz "$WORK/z$n.bin")" -eq "$n" ] || { echo "FAIL z$n input-size"; FAIL=1; return; }
  "$CT" -encode -a lzraven -i "$WORK/z$n.bin" -o "$WORK/z$n.ora.rav" 2>/dev/null || { echo "FAIL z$n oracle rc"; FAIL=1; return; }
  python3 "$ROOT/src/lzraven.py" --raw "$WORK/z$n.bin" "$WORK/z$n.py.rav" 2>"$WORK/z$n.py.err" || { echo "FAIL z$n py rc"; FAIL=1; return; }
  "$WORK/ravstream" --raw "$WORK/z$n.bin" "$WORK/z$n.c.rav" 2>"$WORK/z$n.c.err" || { echo "FAIL z$n C rc"; FAIL=1; return; }
  if ! cmp -s "$WORK/z$n.py.rav" "$WORK/z$n.c.rav"; then echo "FAIL z$n py!=C bytes"; FAIL=1; return; fi
  if ! cmp -s "$WORK/z$n.ora.rav" "$WORK/z$n.c.rav"; then echo "FAIL z$n C!=oracle bytes"; FAIL=1; return; fi
  chk "lz-z$n" sha "$(sha "$WORK/z$n.c.rav")" "$(sz "$WORK/z$n.c.rav")"
}
echo "== zeros-N sweep (T0..T3 + stored edges) =="
for s in 0 1 2 16 62 63 64 65 100 124 125 126 127 128 129 200 255 256 257 300 380 381 382 383 398 399 400 408 409 440 472 473 474 488 505 511 512 600 728 729 730 731 746 747 756 757 788 804 805 820; do
  ZCELL "$s"
done
echo "== unclosed-N (both must refuse, stderr byte-identical) =="
for s in 821 1077 1500 524288; do
  head -c "$s" /dev/zero > "$WORK/u$s.bin" 2>/dev/null || { echo "FAIL u$s input"; FAIL=1; continue; }
  [ "$(sz "$WORK/u$s.bin")" -eq "$s" ] || { echo "FAIL u$s input-size"; FAIL=1; continue; }
  python3 "$ROOT/src/lzraven.py" --raw "$WORK/u$s.bin" "$WORK/u$s.py.rav" 2>"$WORK/u$s.py.err"; prc=$?
  "$WORK/ravstream" --raw "$WORK/u$s.bin" "$WORK/u$s.c.rav" 2>"$WORK/u$s.c.err"; crc=$?
  if [ "$prc" = "$crc" ] && [ "$crc" != 0 ] && cmp -s "$WORK/u$s.py.err" "$WORK/u$s.c.err"; then
    chk "lz-u$s" str "ERROR" "0"
  else
    echo "FAIL u$s: py rc=$prc C rc=$crc"; FAIL=1
  fi
done
echo "== stored cells (random + greet, py==C + pins) =="
RCELL() { # tag size seed
  python3 -c "import random; open('$WORK/$1.bin','wb').write(random.Random($3).randbytes($2))"
  "$CT" -encode -a lzraven -i "$WORK/$1.bin" -o "$WORK/$1.ora.rav" 2>/dev/null || { echo "FAIL $1 oracle rc"; FAIL=1; return; }
  python3 "$ROOT/src/lzraven.py" --raw "$WORK/$1.bin" "$WORK/$1.py.rav" 2>/dev/null || { echo "FAIL $1 py rc"; FAIL=1; return; }
  "$WORK/ravstream" --raw "$WORK/$1.bin" "$WORK/$1.c.rav" 2>/dev/null || { echo "FAIL $1 C rc"; FAIL=1; return; }
  if ! cmp -s "$WORK/$1.py.rav" "$WORK/$1.c.rav"; then echo "FAIL $1 py!=C"; FAIL=1; return; fi
  if ! cmp -s "$WORK/$1.ora.rav" "$WORK/$1.c.rav"; then echo "FAIL $1 C!=oracle"; FAIL=1; return; fi
  chk "lz-$1" sha "$(sha "$WORK/$1.c.rav")" "$(sz "$WORK/$1.c.rav")"
}
for s in 1 16 63; do RCELL "r$s" "$s" "$s"; done
for s in 64 65 256 1000; do RCELL "r$s" "$s" "$s"; done
cp "$ROOT/vectors/selfgen/input/hello/greet.txt" "$WORK/greet.bin"
"$CT" -encode -a lzraven -i "$WORK/greet.bin" -o "$WORK/greet.ora.rav" 2>/dev/null || { echo "FAIL greet oracle rc"; FAIL=1; }
python3 "$ROOT/src/lzraven.py" --raw "$WORK/greet.bin" "$WORK/greet.py.rav" 2>/dev/null || { echo "FAIL greet py rc"; FAIL=1; }
"$WORK/ravstream" --raw "$WORK/greet.bin" "$WORK/greet.c.rav" 2>/dev/null || { echo "FAIL greet C rc"; FAIL=1; }
if cmp -s "$WORK/greet.py.rav" "$WORK/greet.c.rav" && cmp -s "$WORK/greet.ora.rav" "$WORK/greet.c.rav"; then
  chk "lz-greet" sha "$(sha "$WORK/greet.c.rav")" "$(sz "$WORK/greet.c.rav")"
else echo "FAIL greet bytes differ"; FAIL=1; fi
echo "== stored-guess gap (py==C, oracle-divergent stays loud) =="
cp "$ROOT/vectors/selfgen/input/hello/repeat.txt" "$WORK/rep.bin"
"$CT" -encode -a lzraven -i "$WORK/rep.bin" -o "$WORK/rep.ora.rav" 2>/dev/null || { echo "FAIL rep oracle rc"; FAIL=1; }
python3 "$ROOT/src/lzraven.py" --raw "$WORK/rep.bin" "$WORK/rep.py.rav" 2>/dev/null || { echo "FAIL rep py rc"; FAIL=1; }
"$WORK/ravstream" --raw "$WORK/rep.bin" "$WORK/rep.c.rav" 2>/dev/null || { echo "FAIL rep C rc"; FAIL=1; }
if cmp -s "$WORK/rep.py.rav" "$WORK/rep.c.rav"; then
  if cmp -s "$WORK/rep.ora.rav" "$WORK/rep.c.rav"; then
    echo "FAIL rep: unexpectedly oracle-identical (gap closed? update battery)"; FAIL=1
  else
    if python3 "$ROOT/src/ravframe.py" "$WORK/rep.c.rav" 2000 >/dev/null 2>&1; then
      echo "GAP-DOCUMENTED rep: C valid-stored, oracle-divergent (gap stays loud)"; GAP=$((GAP+1))
    else echo "FAIL rep: C output not even frame-valid"; FAIL=1; fi
  fi
else echo "FAIL rep: py!=C (stored-guess diverged)"; FAIL=1; fi
echo "== e2e .aar cells (oracle vs py vs C, incl. 1k multi-block) =="
fix() { find "$1" -exec touch -d '2001-02-03 04:05:06' {} + 2>/dev/null; links=$(find "$1" -type l); if [ -n "$links" ]; then touch -h -d '2001-02-03 04:05:06' $links 2>/dev/null; fi; return 0; }
E2E() { # tag [block]
  tag=$1; blk=${2:-}
  mkdir -p "$WORK/in-$tag"
  python3 -c "import random;random.seed(7);open('$WORK/in-$tag/p','wb').write(bytes(random.randrange(256) for _ in range(3000)))"
  python3 -c "import random;random.seed(8);open('$WORK/in-$tag/q','wb').write(bytes(random.randrange(256) for _ in range(100000)))"
  fix "$WORK/in-$tag"
  "$AA" archive -a lzraven -t 1 ${blk:+-b "$blk"} -d "$WORK/in-$tag" -o "$WORK/$tag.expect.aar" 2>"$WORK/$tag.err" || { echo "FAIL $tag oracle rc"; FAIL=1; return; }
  python3 "$ROOT/src/encode.py" "$WORK/in-$tag" "$WORK/$tag.py.aar" --alg lzraven ${blk:+--block "$blk"} 2>>"$WORK/$tag.err" || { echo "FAIL $tag py rc"; FAIL=1; return; }
  "$CLI" aar-encode --alg lzraven ${blk:+--block "$blk"} "$WORK/in-$tag" "$WORK/$tag.c.aar" 2>>"$WORK/$tag.err" || { echo "FAIL $tag C rc"; FAIL=1; return; }
  if ! cmp -s "$WORK/$tag.py.aar" "$WORK/$tag.c.aar"; then echo "FAIL $tag py!=C"; FAIL=1; return; fi
  if ! cmp -s "$WORK/$tag.expect.aar" "$WORK/$tag.c.aar"; then echo "FAIL $tag C!=oracle"; FAIL=1; return; fi
  chk "lz-e2e-$tag" sha "$(sha "$WORK/$tag.c.aar")" "$(sz "$WORK/$tag.c.aar")"
  rm -rf "$WORK/rt-$tag"; mkdir -p "$WORK/rt-$tag"
  "$AA" extract -i "$WORK/$tag.c.aar" -d "$WORK/rt-$tag" 2>>"$WORK/$tag.err" || { echo "FAIL $tag roundtrip rc"; FAIL=1; }
}
E2E e2e4m
E2E e2e1k 1k
echo "== $WORK (gaps-documented=$GAP) =="
[ "$FAIL" -eq 0 ] && echo LZRAVEN-C-GREEN || echo LZRAVEN-C-RED
exit "$FAIL"
