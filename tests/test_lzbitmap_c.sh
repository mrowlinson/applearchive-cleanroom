#!/bin/sh
# tests/test_lzbitmap_c.sh -- C-parity battery (aae --alg lzbitmap + C stream
# harness vs oracle pins + vs py bytes).
# Bed-style like test_lz4_c.sh: every cell encodes byte-identical under py
# (src/lzbitmap.py + src/encode.py) and C, and C verdict matches the
# oracle-bedded pins in vectors/lzbitmap-PINS.csv (C-vs-oracle) with live
# /usr/bin/aa + libcompression-probe byte-compare on top.
# Covers: all 21 .bm .aar corpus cells (1 parity + 20 refusal, refusal
# markers asserted py-vs-C), the 6 pinned stream cells, and
# 4 adversarial refusal stream cells.
# Mapping to tests/test_lzbitmap.sh cells: every X.bm cell here replays the
# identical corpus builder with C backend (also runnable in-place with
# ENC_BIN=$AAE_C in test_lzbitmap.sh); stream-* cells replay the identical
# probe inputs through the C harness.
#
# UNIFIED MAPPING (cport-unify): old `"$AAE_C" <dir> <out> --alg lzbitmap ...`
# .aar corpus cells are now
# `"$CLI" aar-encode --alg lzbitmap ... <dir> <out>` — same ae_main code
# path. Success cells: identical bytes/exits. Refusal cells: the CLI wraps
# the backend's exit-1 + raw marker into exit 2 + "aae-cli: aar-encode
# --alg lzbitmap: <marker>" (same wrap the Python CLI and test_cli.sh
# assert), so py rc=1/C rc=2 with marker grep on both sides replaces the old
# raw-stderr cmp. Cell count and oracle comparisons unchanged.
# Usage: TMPDIR=<nvme-scratch> sh tests/test_lzbitmap_c.sh [workdir]
# Needs: CLI (default WS unified build). Exit 0 GREEN/1 RED/2 setup.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
W=${1:-$(mktemp -d "$TMPDIR/lzbitmapc.XXXXXX")}
ORACLE=${ORACLE:-/usr/bin/aa}
CLI=${CLI:-/Volumes/NVME/applearchive-cleanroom-ws/build/unified/aae-cli}
PINS=$ROOT/vectors/lzbitmap-PINS.csv
fail=0
[ -x "$CLI" ] || { echo "need unified binary: $CLI (CLI=...)" >&2; exit 2; }
[ -x "$ORACLE" ] || { echo "need $ORACLE" >&2; exit 2; }
[ -f "$PINS" ] || { echo "missing $PINS" >&2; exit 2; }
command -v cc >/dev/null || { echo "need cc" >&2; exit 2; }
command -v python3 >/dev/null || { echo "need python3" >&2; exit 2; }
mkdir -p "$W" || exit 2
pin_get() { grep "^$1," "$PINS" | head -1 | cut -d, -f3; }
chk() { # name check val [bytes]
  exp=$(pin_get "$1")
  if [ "$3" = "$exp" ]; then echo "PASS $1"; else echo "FAIL $1: got $3 want $exp"; fail=1; fi
}
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
sz() { wc -c < "$1" | tr -d ' '; }
fix() { find "$1" -exec touch -d '2001-02-03 04:05:06' {} + 2>/dev/null; touch -h -d '2001-02-03 04:05:06' $(find "$1" -type l) 2>/dev/null; return 0; }
echo "== build C stream harness (committed sources only) =="
cat > "$W/zbmmain.c" <<'EOF'
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lzbitmapc.h"
int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "usage: zbm INFILE OUTFILE\n"); return 2;
    }
    FILE *fi = fopen(argv[1], "rb");
    if (!fi) { fprintf(stderr, "zbm: read %s: %s\n", argv[1], strerror(errno)); return 1; }
    fseek(fi, 0, SEEK_END); long z = ftell(fi); fseek(fi, 0, SEEK_SET);
    if (z < 0) { fprintf(stderr, "zbm: read %s: %s\n", argv[1], strerror(errno)); return 1; }
    uint8_t *d = malloc((size_t)z + 1); if (!d) exit(1);
    if (z > 0 && fread(d, 1, (size_t)z, fi) != (size_t)z) return 1;
    fclose(fi);
    char err[256]; size_t on = 0;
    uint8_t *o = zbm_encode_literal(d, (size_t)z, &on, err, sizeof err);
    if (!o) { fprintf(stderr, "LzBitmapMatchFound: %s\n", err); free(d); return 7; }
    FILE *f = fopen(argv[2], "wb");
    if (!f) return 1;
    if (on && fwrite(o, 1, on, f) != on) return 1;
    fclose(f); free(d); free(o); return 0;
}
EOF
cc -O2 -Wall -Wextra -std=c11 -I"$ROOT/src/c" -o "$W/zbmstream" \
  "$W/zbmmain.c" "$ROOT/src/c/lzbitmapc.c" -lm || { echo "harness build failed" >&2; exit 2; }
cat > "$W/bmprobe.py" <<'EOF'
# runtime-generated oracle probe (beds-OK: never committed).
import ctypes, sys
lib = ctypes.CDLL("libcompression.dylib")
lib.compression_encode_scratch_buffer_size.restype = ctypes.c_size_t
lib.compression_encode_scratch_buffer_size.argtypes = [ctypes.c_int]
lib.compression_encode_buffer.restype = ctypes.c_size_t
lib.compression_encode_buffer.argtypes = [ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_int]
src = open(sys.argv[1], 'rb').read()
n = lib.compression_encode_scratch_buffer_size(0x702)
scratch = ctypes.create_string_buffer(n) if n else None
dst = ctypes.create_string_buffer(len(src) + 65536)
m = lib.compression_encode_buffer(dst, len(dst), src, len(src), scratch, 0x702)
if m == 0: sys.exit(1)
open(sys.argv[2], 'wb').write(dst.raw[:m])
EOF
pyzbm() { # in out err : py stream encode, rc 7 + marker on refusal
  python3 -c "import sys;sys.path.insert(0,'$ROOT/src');from lzbitmap import zbm_encode_literal,LzBitmapMatchFound
try:
  open('$2','wb').write(zbm_encode_literal(open('$1','rb').read()))
except LzBitmapMatchFound as e:
  sys.stderr.write('LzBitmapMatchFound: %s\n' % e); sys.exit(7)" 2>"$3"
}
echo "== stream cells (oracle probe vs py vs C + pins) =="
scell() { # tag size seed
  if [ "$2" = 0 ]; then : > "$W/p_$1.bin"; else python3 -c "import random;random.seed($3);open('$W/p_$1.bin','wb').write(bytes(random.randrange(256) for _ in range($2)))"; fi
  python3 "$W/bmprobe.py" "$W/p_$1.bin" "$W/p_$1.expect.zbm" || { echo "FAIL stream-$1 oracle-probe"; fail=1; return; }
  pyzbm "$W/p_$1.bin" "$W/p_$1.py.zbm" "$W/p_$1.py.err"; prc=$?
  "$W/zbmstream" "$W/p_$1.bin" "$W/p_$1.c.zbm" 2>"$W/p_$1.c.err"; crc=$?
  if [ "$prc" != "$crc" ]; then echo "FAIL stream-$1 rc py=$prc C=$crc"; fail=1; return; fi
  if [ "$prc" = 0 ]; then
    cmp -s "$W/p_$1.expect.zbm" "$W/p_$1.py.zbm" || { echo "FAIL stream-$1 py!=oracle"; fail=1; return; }
    cmp -s "$W/p_$1.py.zbm" "$W/p_$1.c.zbm" || { echo "FAIL stream-$1 C!=py"; fail=1; return; }
    chk "stream-$1" sha "$(sha "$W/p_$1.c.zbm")" "$(sz "$W/p_$1.c.zbm")"
  else
    cmp -s "$W/p_$1.py.err" "$W/p_$1.c.err" || { echo "FAIL stream-$1 reason: [$(cat "$W/p_$1.py.err")] vs [$(cat "$W/p_$1.c.err")]"; fail=1; return; }
    chk "stream-$1" refuse "refused" "$(sz "$W/p_$1.expect.zbm")"
  fi
}
scell empty 0 0
scell one 1 16
scell r100 100 16
scell c32k 32768 16
scell c32k1 32769 16
python3 -c "import random;random.seed(15);open('$W/p_probe70k.bin','wb').write(bytes(random.randrange(256) for _ in range(70000)))"
python3 "$W/bmprobe.py" "$W/p_probe70k.bin" "$W/p_probe70k.expect.zbm" || { echo "FAIL stream-probe70k oracle-probe"; fail=1; }
pyzbm "$W/p_probe70k.bin" "$W/p_probe70k.py.zbm" "$W/p_probe70k.py.err"; prc=$?
"$W/zbmstream" "$W/p_probe70k.bin" "$W/p_probe70k.c.zbm" 2>"$W/p_probe70k.c.err"; crc=$?
if [ "$prc" = 0 ] && [ "$crc" = 0 ] && cmp -s "$W/p_probe70k.py.zbm" "$W/p_probe70k.c.zbm"; then
  chk "stream-probe70k" sha "$(sha "$W/p_probe70k.c.zbm")" "$(sz "$W/p_probe70k.c.zbm")"
else echo "FAIL stream-probe70k py=$prc C=$crc"; fail=1; fi
scell bigrnd 100000 60
echo "== adversarial stream cells (refusal parity) =="
acell() { # tag builder(python -c body writing $W/sc_TAG.bin)
  python3 -c "$2" || { echo "FAIL scell-$1 builder"; fail=1; return; }
  python3 "$W/bmprobe.py" "$W/sc_$1.bin" "$W/sc_$1.expect.zbm" || { echo "FAIL scell-$1 oracle-probe"; fail=1; return; }
  pyzbm "$W/sc_$1.bin" "$W/sc_$1.py.zbm" "$W/sc_$1.py.err"; prc=$?
  "$W/zbmstream" "$W/sc_$1.bin" "$W/sc_$1.c.zbm" 2>"$W/sc_$1.c.err"; crc=$?
  if [ "$prc" != "$crc" ]; then echo "FAIL scell-$1 rc py=$prc C=$crc"; fail=1; return; fi
  if [ "$prc" = 0 ]; then
    cmp -s "$W/sc_$1.expect.zbm" "$W/sc_$1.c.zbm" || { echo "FAIL scell-$1 C!=oracle"; fail=1; return; }
    chk "stream-$1" sha "$(sha "$W/sc_$1.c.zbm")" "$(sz "$W/sc_$1.c.zbm")"
  else
    cmp -s "$W/sc_$1.py.err" "$W/sc_$1.c.err" || { echo "FAIL scell-$1 reason: [$(cat "$W/sc_$1.py.err")] vs [$(cat "$W/sc_$1.c.err")]"; fail=1; return; }
    chk "stream-$1" refuse "refused" "$(sz "$W/sc_$1.expect.zbm")"
  fi
}
acell zeros145 "open('$W/sc_zeros145.bin','wb').write(b'\x00'*145)"
acell denseL2 "import random
random.seed(1002);R=bytes(random.randrange(256) for _ in range(2))
random.seed(3002);open('$W/sc_denseL2.bin','wb').write(b''.join(R+bytes(random.randrange(256) for _ in range(8)) for _ in range(300)))"
acell tileL3 "import random
random.seed(1003);R=bytes(random.randrange(256) for _ in range(3))
random.seed(2003);open('$W/sc_tileL3.bin','wb').write(b''.join(R+bytes(random.randrange(256) for _ in range(32)) for _ in range(60)))"
acell skewmulti "pool=[b for b in range(256) if b not in (65,66,67,68)];open('$W/sc_skewmulti.bin','wb').write(b'A'*20+b'B'*20+b'C'*20+b'D'*20+b''.join(bytes([x]) for x in pool[:300]))"
echo "== .aar corpus cells (oracle vs py vs C + pins) =="
mkdir -p "$W/in/empty1"; fix "$W/in/empty1"
mkdir -p "$W/in/efile"; : > "$W/in/efile/f.bin"; fix "$W/in/efile"
mkdir -p "$W/in/tiny"; printf 'hi\n' > "$W/in/tiny/f.bin"; fix "$W/in/tiny"
mkdir -p "$W/in/r1"; python3 -c "import random;random.seed(11);open('$W/in/r1/p','wb').write(bytes(random.randrange(256) for _ in range(3000)))"; fix "$W/in/r1"
mkdir -p "$W/in/r40k"; python3 -c "import random;random.seed(12);open('$W/in/r40k/p','wb').write(bytes(random.randrange(256) for _ in range(40000)))"; fix "$W/in/r40k"
mkdir -p "$W/in/multi"; python3 -c "import random;random.seed(13);open('$W/in/multi/a','wb').write(bytes(random.randrange(256) for _ in range(5000)))"; python3 -c "import random;random.seed(14);open('$W/in/multi/b','wb').write(bytes(random.randrange(256) for _ in range(9000)))"; fix "$W/in/multi"
mkdir -p "$W/in/z144"; python3 -c "open('$W/in/z144/f','wb').write(b'\x00'*144)"; fix "$W/in/z144"
mkdir -p "$W/in/z200"; python3 -c "open('$W/in/z200/f','wb').write(b'\x00'*200)"; fix "$W/in/z200"
mkdir -p "$W/in/per8"; python3 -c "open('$W/in/per8/f','wb').write((bytes(range(8))*38)[:300])"; fix "$W/in/per8"
mkdir -p "$W/in/mix"; python3 -c "import random;random.seed(7);open('$W/in/mix/f','wb').write(bytes(random.randrange(256) for _ in range(300))+b'\x00'*40)"; fix "$W/in/mix"
mkdir -p "$W/in/runfirst"; python3 -c "import random;random.seed(7);open('$W/in/runfirst/f','wb').write(b'\x00'*40+bytes(random.randrange(256) for _ in range(300)))"; fix "$W/in/runfirst"
mkdir -p "$W/in/tileL4"; python3 -c "import random;random.seed(1004);R=bytes(random.randrange(256) for _ in range(4));random.seed(2004);open('$W/in/tileL4/f','wb').write(b''.join(R+bytes(random.randrange(256) for _ in range(32)) for _ in range(60)))"; fix "$W/in/tileL4"
mkdir -p "$W/in/skew400"; python3 -c "xs=bytes(b for b in range(1,256) if b!=0x41)[:200];open('$W/in/skew400/f','wb').write(b''.join(b'A'+bytes([x]) for x in xs)[:400])"; fix "$W/in/skew400"
mkdir -p "$W/in/skewmulti"; python3 -c "pool=[b for b in range(256) if b not in (65,66,67)];open('$W/in/skewmulti/f','wb').write(b'A'*30+b'B'*30+b'C'*30+b''.join(bytes([x]) for x in pool[:300]))"; fix "$W/in/skewmulti"
mkdir -p "$W/in/spread8"; python3 -c "
import random
random.seed(777);grams=set()
while len(grams)<200: grams.add(bytes([random.randrange(256),random.randrange(256)]))
grams=list(grams);sepset=set();seps=[]
while len(seps)<1600:
  s=bytes(random.randrange(256) for _ in range(8))
  if s[:2] not in sepset and not any(s[:2]==g for g in grams): sepset.add(s[:2]);seps.append(s)
parts=[];k=0
for g in grams:
  for _ in range(8): parts.append(g+seps[k]);k+=1
open('$W/in/spread8/f','wb').write(b''.join(parts))"; fix "$W/in/spread8"
mkdir -p "$W/in/bigrnd"; python3 -c "import random;random.seed(55);open('$W/in/bigrnd/f','wb').write(bytes(random.randrange(256) for _ in range(200000)))"; fix "$W/in/bigrnd"
mkdir -p "$W/in/bigmix"; python3 -c "import random;random.seed(56);a=bytes(random.randrange(256) for _ in range(100000));random.seed(57);b=bytes(random.randrange(256) for _ in range(100000));open('$W/in/bigmix/f','wb').write(a+b'\x00'*1000+b)"; fix "$W/in/bigmix"
mkdir -p "$W/in/dup40k"; python3 -c "import random;random.seed(58);d=bytes(random.randrange(256) for _ in range(40000));open('$W/in/dup40k/a','wb').write(d);open('$W/in/dup40k/b','wb').write(d)"; fix "$W/in/dup40k"
mkdir -p "$W/in/taillast"; python3 -c "import random;random.seed(59);d=bytes(random.randrange(256) for _ in range(32768));open('$W/in/taillast/f','wb').write(d+d[:100])"; fix "$W/in/taillast"
mkdir -p "$W/in/multi20"; python3 -c "import random
for i in range(20):
  random.seed(100+i);open('$W/in/multi20/f%02d'%i,'wb').write(bytes(random.randrange(256) for _ in range(2000)))"; fix "$W/in/multi20"
mkdir -p "$W/in/hmedge"; python3 -c "pool=[b for b in range(256) if b not in (65,66,67,68)];open('$W/in/hmedge/f','wb').write(b'A'*15+b'B'*15+b'C'*15+b'D'*15+b''.join(bytes([x]) for x in pool[:300]))"; fix "$W/in/hmedge"
cell() { # $1=name $2=block
  "$ORACLE" archive -a lzbitmap -t 1 ${2:+-b "$2"} -d "$W/in/$1" -o "$W/$1.expect.aar" 2>"$W/$1.ora.err" || { echo "FAIL $1 oracle-exit=$?"; fail=1; return; }
  python3 "$ROOT/src/encode.py" "$W/in/$1" "$W/$1.py.aar" --alg lzbitmap ${2:+--block "$2"} 2>"$W/$1.py.err"; prc=$?
  "$CLI" aar-encode --alg lzbitmap ${2:+--block "$2"} "$W/in/$1" "$W/$1.c.aar" 2>"$W/$1.c.err"; crc=$?
  if [ "$prc" = 0 ] && [ "$crc" = 0 ]; then
    cmp -s "$W/$1.expect.aar" "$W/$1.py.aar" || { echo "FAIL $1 py!=oracle"; fail=1; return; }
    cmp -s "$W/$1.py.aar" "$W/$1.c.aar" || { echo "FAIL $1 C!=py"; fail=1; return; }
    chk "$1.bm" sha "$(sha "$W/$1.c.aar")" "$(sz "$W/$1.c.aar")"
    rm -rf "$W/rt/$1"; mkdir -p "$W/rt/$1"
    "$ORACLE" extract -i "$W/$1.c.aar" -d "$W/rt/$1" 2>>"$W/$1.ora.err" || { echo "FAIL $1 roundtrip-exit=$?"; fail=1; }
  elif [ "$prc" = 1 ] && [ "$crc" = 2 ]; then
    # Unified CLI wrap: exit 2 + "aae-cli: aar-encode --alg lzbitmap: <marker>".
    if ! grep -q "lzbitmap match-class" "$W/$1.py.err"; then
      echo "FAIL $1 py refusal without marker"; fail=1; return
    fi
    if ! grep -q "^aae-cli: aar-encode --alg lzbitmap: .*lzbitmap match-class" "$W/$1.c.err"; then
      echo "FAIL $1 C refusal without wrapped marker: [$(cat "$W/$1.c.err")]"; fail=1; return
    fi
    chk "$1.bm" refuse "refused" "$(sz "$W/$1.expect.aar")"
  else
    echo "FAIL $1 rc py=$prc C=$crc"; fail=1; return
  fi
}
cell empty1 ""
cell efile ""
cell tiny ""
cell r1 ""
cell r40k ""
cell multi 10000
cell z144 ""
cell z200 ""
cell per8 ""
cell mix ""
cell runfirst ""
cell tileL4 ""
cell skew400 ""
cell skewmulti ""
cell spread8 ""
cell bigrnd ""
cell bigmix ""
cell dup40k ""
cell taillast ""
cell multi20 ""
cell hmedge ""
echo "== $W =="
[ $fail -eq 0 ] && echo LZBITMAP-C-GREEN || echo LZBITMAP-C-RED
exit $fail
