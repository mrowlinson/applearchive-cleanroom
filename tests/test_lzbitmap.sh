#!/bin/sh
# tests/test_lzbitmap.sh [workdir] — oracle-vs-impl byte compare, lzbitmap path.
# Covers the LITERAL class (inputs where the oracle finds no long match and
# emits 00+raw per 32KB chunk): our pure-python src/lzbitmap.py must be
# byte-identical at stream level and at .aar level (outer pbzb + store rule).
# MATCH class is REFUSED, not replicated: the oracle's match grammar is
# globally planned and multi-modal (match descriptors, dimer codebook,
# sparse order-0 skew mode, 64KB cross-section dictionary), so literal
# bytes would silently diverge there. src/lzbitmap.py raises
# LzBitmapMatchFound (encode.py -> SystemExit) on every input outside the
# proven-parity class (exact guards G1/G2/G3/G4, see src/lzbitmap.py).
# Every cell below is parity-or-refusal: byte-compare on parity, refusal
# verdict (impl exits nonzero with the match-class marker) otherwise.
# Zero silent divergence: any byte mismatch with exit 0 is FAIL.
# Direct stream parity uses a RUNTIME-GENERATED oracle probe (beds-OK class,
# never committed) vs libcompression COMPRESSION_LZBITMAP (0x702), mirroring
# tests/test_rb2.sh bmprobe.
# exit 0 all green / 1 any FAIL / 2 harness error.
# RECORD=1 sh tests/test_lzbitmap.sh [workdir]  (rewrite PINS; REVIEW diff!)
set -u
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
W=${1:-$(mktemp -d "$TMPDIR/lzbitmap.XXXXXX")}
ORACLE=${ORACLE:-/usr/bin/aa}
_IMP=${ENC_BIN:-python3 "$ROOT/src/encode.py"}
PINS=$ROOT/vectors/lzbitmap-PINS.csv
fail=0
mkdir -p "$W" || exit 2
command -v python3 >/dev/null || { echo "need python3" >&2; exit 2; }
[ -x "$ORACLE" ] || { echo "need $ORACLE" >&2; exit 2; }
if [ -n "${RECORD:-}" ]; then
  echo "# lzbitmap pins: name,check,expect,bytes,generator,os,backend" > "$PINS.new"
  echo "# eq = impl-vs-oracle cmp verdict; sha = impl output hash (deterministic inputs)" >> "$PINS.new"
else
  [ -f "$PINS" ] || { echo "missing $PINS (RECORD=1 first)" >&2; exit 2; }
fi
OS=$(sw_vers -productVersion 2>/dev/null || echo unknown)
pin_get() { grep "^$1," "$PINS" | head -1 | cut -d, -f3; }
chk() { # name check val [bytes]
  if [ -n "${RECORD:-}" ]; then
    echo "$1,$2,$3,${4:-0},test_lzbitmap.sh,$OS,oracle" >> "$PINS.new"
    echo "REC $1=$3"
  else
    exp=$(pin_get "$1")
    if [ "$3" = "$exp" ]; then echo "PASS $1"; else echo "FAIL $1: got $3 want $exp"; fail=1; fi
  fi
}
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
sz() { wc -c < "$1" | tr -d ' '; }
fix() { find "$1" -exec touch -d '2001-02-03 04:05:06' {} + 2>/dev/null; touch -h -d '2001-02-03 04:05:06' $(find "$1" -type l) 2>/dev/null; return 0; }
cell() { # $1=name $2=block
  "$ORACLE" archive -a lzbitmap -t 1 ${2:+-b "$2"} -d "$W/in/$1" -o "$W/$1.bm.expect.aar" 2>"$W/$1.bm.err" || { echo "FAIL $1.bm oracle-exit=$?"; fail=1; return; }
  if ! $_IMP "$W/in/$1" "$W/$1.bm.got.aar" --alg lzbitmap ${2:+--block "$2"} 2>>"$W/$1.bm.err"; then
    if grep -q "lzbitmap match-class" "$W/$1.bm.err" 2>/dev/null; then
      chk "$1.bm" refuse "refused" "$(sz "$W/$1.bm.expect.aar")"
    else
      echo "FAIL $1.bm impl-exit(non-refusal, see $W/$1.bm.err)"; fail=1
    fi
    return
  fi
  if cmp -s "$W/$1.bm.expect.aar" "$W/$1.bm.got.aar"; then
    chk "$1.bm" sha "$(sha "$W/$1.bm.got.aar")" "$(sz "$W/$1.bm.got.aar")"
  else
    echo "FAIL $1.bm expect=$(stat -f %z "$W/$1.bm.expect.aar") got=$(stat -f %z "$W/$1.bm.got.aar")"
    cmp "$W/$1.bm.expect.aar" "$W/$1.bm.got.aar" | head -n 3
    fail=1
  fi
  rm -rf "$W/rt/$1.bm"; mkdir -p "$W/rt/$1.bm"
  "$ORACLE" extract -i "$W/$1.bm.got.aar" -d "$W/rt/$1.bm" 2>>"$W/$1.bm.err" || { echo "FAIL $1.bm roundtrip-exit=$?"; fail=1; }
}
# corpus: match-free by construction (seeded random) + sub-threshold runs
mkdir -p "$W/in/empty1"; fix "$W/in/empty1"
mkdir -p "$W/in/efile"; : > "$W/in/efile/f.bin"; fix "$W/in/efile"
mkdir -p "$W/in/tiny"; printf 'hi\n' > "$W/in/tiny/f.bin"; fix "$W/in/tiny"
mkdir -p "$W/in/r1"; python3 -c "import random;random.seed(11);open('$W/in/r1/p','wb').write(bytes(random.randrange(256) for _ in range(3000)))"; fix "$W/in/r1"
mkdir -p "$W/in/r40k"; python3 -c "import random;random.seed(12);open('$W/in/r40k/p','wb').write(bytes(random.randrange(256) for _ in range(40000)))"; fix "$W/in/r40k"
mkdir -p "$W/in/multi"; python3 -c "import random;random.seed(13);open('$W/in/multi/a','wb').write(bytes(random.randrange(256) for _ in range(5000)))"; python3 -c "import random;random.seed(14);open('$W/in/multi/b','wb').write(bytes(random.randrange(256) for _ in range(9000)))"; fix "$W/in/multi"
cell empty1 ""
cell efile ""
cell tiny ""
cell r1 ""
cell r40k ""
cell multi 10000
# adversarial match-class cells (each must be parity-or-refusal, never silent divergence)
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
# direct stream parity: runtime-generated oracle probe vs src/lzbitmap.py
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
python3 -c "import random;random.seed(15);open('$W/probe70k.bin','wb').write(bytes(random.randrange(256) for _ in range(70000)))"
for spec in "0:empty" "1:one" "100:r100" "32768:c32k" "32769:c32k1" "70000:probe70k"; do
  n=${spec%%:*}; tag=${spec##*:}
  if [ "$n" = 0 ]; then : > "$W/p_$tag.bin";
  elif [ "$tag" = "probe70k" ]; then cp "$W/probe70k.bin" "$W/p_$tag.bin";
  else python3 -c "import random;random.seed(16);open('$W/p_$tag.bin','wb').write(bytes(random.randrange(256) for _ in range($n)))"; fi
  python3 "$W/bmprobe.py" "$W/p_$tag.bin" "$W/p_$tag.expect.zbm" || { echo "FAIL stream-$tag oracle-probe"; fail=1; continue; }
  if python3 -c "import sys;sys.path.insert(0,'$ROOT/src');from lzbitmap import zbm_encode_literal,LzBitmapMatchFound
try:
  open('$W/p_$tag.got.zbm','wb').write(zbm_encode_literal(open('$W/p_$tag.bin','rb').read()))
except LzBitmapMatchFound as e:
  sys.stderr.write('LzBitmapMatchFound: %s\n' % e); sys.exit(7)" 2>"$W/p_$tag.impl.err"; then
    if cmp -s "$W/p_$tag.expect.zbm" "$W/p_$tag.got.zbm"; then
      chk "stream-$tag" sha "$(sha "$W/p_$tag.got.zbm")" "$(sz "$W/p_$tag.got.zbm")"
    else
      echo "FAIL stream-$tag expect=$(sz "$W/p_$tag.expect.zbm") got=$(sz "$W/p_$tag.got.zbm")"
      fail=1
    fi
  else
    if [ $? -eq 7 ] && grep -q "LzBitmapMatchFound" "$W/p_$tag.impl.err" 2>/dev/null; then
      chk "stream-$tag" refuse "refused" "$(sz "$W/p_$tag.expect.zbm")"
    else
      echo "FAIL stream-$tag impl-exit(non-refusal)"; fail=1
    fi
  fi
done
# adversarial stream cells: custom builders (refusal expected unless noted)
scell() { # $1=tag $2=builder(python -c body writing $W/sc_$1.bin)
  python3 -c "$2" || { echo "FAIL scell-$1 builder"; fail=1; return; }
  python3 "$W/bmprobe.py" "$W/sc_$1.bin" "$W/sc_$1.expect.zbm" || { echo "FAIL scell-$1 oracle-probe"; fail=1; return; }
  if python3 -c "import sys;sys.path.insert(0,'$ROOT/src');from lzbitmap import zbm_encode_literal,LzBitmapMatchFound
try:
  open('$W/sc_$1.got.zbm','wb').write(zbm_encode_literal(open('$W/sc_$1.bin','rb').read()))
except LzBitmapMatchFound as e:
  sys.stderr.write('LzBitmapMatchFound: %s\n' % e); sys.exit(7)" 2>"$W/sc_$1.impl.err"; then
    if cmp -s "$W/sc_$1.expect.zbm" "$W/sc_$1.got.zbm"; then
      chk "stream-$1" sha "$(sha "$W/sc_$1.got.zbm")" "$(sz "$W/sc_$1.got.zbm")"
    else
      echo "FAIL scell-$1 expect=$(sz "$W/sc_$1.expect.zbm") got=$(sz "$W/sc_$1.got.zbm")"
      fail=1
    fi
  else
    if [ $? -eq 7 ] && grep -q "LzBitmapMatchFound" "$W/sc_$1.impl.err" 2>/dev/null; then
      chk "stream-$1" refuse "refused" "$(sz "$W/sc_$1.expect.zbm")"
    else
      echo "FAIL scell-$1 impl-exit(non-refusal)"; fail=1
    fi
  fi
}
scell zeros145 "open('$W/sc_zeros145.bin','wb').write(b'\x00'*145)"
scell denseL2 "import random
random.seed(1002);R=bytes(random.randrange(256) for _ in range(2))
random.seed(3002);open('$W/sc_denseL2.bin','wb').write(b''.join(R+bytes(random.randrange(256) for _ in range(8)) for _ in range(300)))"
scell tileL3 "import random
random.seed(1003);R=bytes(random.randrange(256) for _ in range(3))
random.seed(2003);open('$W/sc_tileL3.bin','wb').write(b''.join(R+bytes(random.randrange(256) for _ in range(32)) for _ in range(60)))"
scell skewmulti "pool=[b for b in range(256) if b not in (65,66,67,68)];open('$W/sc_skewmulti.bin','wb').write(b'A'*20+b'B'*20+b'C'*20+b'D'*20+b''.join(bytes([x]) for x in pool[:300]))"
scell bigrnd "import random;random.seed(60);open('$W/sc_bigrnd.bin','wb').write(bytes(random.randrange(256) for _ in range(100000)))"
[ -n "${RECORD:-}" ] && mv "$PINS.new" "$PINS" && echo "RECORDED $PINS"
echo "== $W =="
[ $fail -eq 0 ] && echo LZBITMAP-GREEN || echo LZBITMAP-RED
exit $fail
