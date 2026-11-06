#!/bin/sh
# tests/test_lzbitmap.sh [workdir] — oracle-vs-impl byte compare, lzbitmap path.
# Covers the LITERAL class (inputs where the oracle finds no long match and
# emits 00+raw per 32KB chunk): our pure-python src/lzbitmap.py must be
# byte-identical at stream level and at .aar level (outer pbzb + store rule).
# MATCH class (runs/periodic/mixed with a repeat >= ~137B) is PARKED below:
# globally-planned grammar (34/44/f3 descriptors, fc epilogue), not replicated.
# Direct stream parity uses a RUNTIME-GENERATED oracle probe (beds-OK class,
# never committed) vs libcompression COMPRESSION_LZBITMAP (0x702), mirroring
# tests/test_rb2.sh bmprobe.
# exit 0 all green / 1 any FAIL / 2 harness error.
# RECORD=1 sh tests/test_lzbitmap.sh [workdir]  (rewrite PINS; REVIEW diff!)
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
W=${1:-$(mktemp -d "${TMPDIR:-/Volumes/NVME/applearchive-cleanroom-ws/tmp}/lzbitmap.XXXXXX")}
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
  $_IMP "$W/in/$1" "$W/$1.bm.got.aar" --alg lzbitmap ${2:+--block "$2"} 2>>"$W/$1.bm.err" || { echo "FAIL $1.bm impl-exit=$?"; fail=1; return; }
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
  python3 -c "import sys;sys.path.insert(0,'$ROOT/src');from lzbitmap import zbm_encode_literal;open('$W/p_$tag.got.zbm','wb').write(zbm_encode_literal(open('$W/p_$tag.bin','rb').read()))"
  if cmp -s "$W/p_$tag.expect.zbm" "$W/p_$tag.got.zbm"; then
    chk "stream-$tag" sha "$(sha "$W/p_$tag.got.zbm")" "$(sz "$W/p_$tag.got.zbm")"
  else
    echo "FAIL stream-$tag expect=$(sz "$W/p_$tag.expect.zbm") got=$(sz "$W/p_$tag.got.zbm")"
    fail=1
  fi
done
# PARKED (match class: globally-planned descriptors, not replicated):
#   zeros100-file (z100: TLV+run compresses 345->235), zeros200 (run match),
#   per8 (offset-8 repeat), per3 (offset-9 long form),
#   mix-zero/rnd/zero (two-match planning). Revisit with match-grammar RE.
[ -n "${RECORD:-}" ] && mv "$PINS.new" "$PINS" && echo "RECORDED $PINS"
echo "== $W =="
[ $fail -eq 0 ] && echo LZBITMAP-GREEN || echo LZBITMAP-RED
exit $fail
