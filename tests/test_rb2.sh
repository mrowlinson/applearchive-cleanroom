#!/bin/sh
# test_rb2.sh -- rb2 frame-layer battery (PARENT-007(3) IMPL, NOTE-w2s3-8).
# rb2.py frames raw.aar with injected payloads; output must be byte-identical
# to aa -a (proves framing; codec bed-war replaces oracles later).
# Payload oracles = TEST-TIME EXEC ONLY, never shipped: raven via
# compression_tool (A-13, POC IDENTICAL); bitmap via a ctypes probe vs
# libcompression 0x702 written to WORK at runtime (A-13/A-12(a) beds-OK
# class: runtime-generated, NEVER committed). Exit 0 GREEN / 1 RED / 2 error.
# Usage: sh tests/test_rb2.sh [workdir]
# RECORD=1 sh tests/test_rb2.sh [workdir]  (rewrite PINS; REVIEW diff!)
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
ADAPTER=${ADAPTER:-$HERE/../harness/oracle-adapter.sh}
WORK=${1:-$(mktemp -d "${TMPDIR:-/tmp}/rb2.XXXXXX")}
PINS=$ROOT/vectors/rb2-PINS.csv
FAIL=0
GEN=test_rb2.sh
OS=$(sw_vers -productVersion 2>/dev/null || echo unknown)
BE=$(basename "$ADAPTER")
CT=${CT:-/usr/bin/compression_tool}
RB2=$ROOT/src/rb2.py
command -v python3 >/dev/null || { echo "need python3" >&2; exit 2; }
mkdir -p "$WORK" "$ROOT/vectors"
pin_get() { grep "^$1," "$PINS" | head -1 | cut -d, -f3; }
chk() { # name check val [bytes]
  if [ -n "${RECORD:-}" ]; then
    echo "$1,$2,$3,${4:-0},$GEN,$OS,$BE" >> "$PINS.new"
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
sh "$ADAPTER" probe || exit 2
[ -x "$CT" ] || { echo "need $CT" >&2; exit 2; }
if [ -n "${RECORD:-}" ]; then
  echo "# rb2 pins: name,check,expect,bytes,generator,os,backend" > "$PINS.new"
  echo "# eq = rb2-vs-oracle cmp verdict; sha = rb2 output hash (deterministic inputs)" >> "$PINS.new"
fi
cat > "$WORK/bmprobe.py" <<'EOF'
# runtime-generated bitmap payload probe (beds-OK: never committed).
# libcompression COMPRESSION_LZBITMAP (0x702) one-shot, public buffer API.
import ctypes, sys
lib = ctypes.CDLL("libcompression.dylib")
lib.compression_encode_scratch_buffer_size.restype = ctypes.c_size_t
lib.compression_encode_scratch_buffer_size.argtypes = [ctypes.c_int]
lib.compression_encode_buffer.restype = ctypes.c_size_t
lib.compression_encode_buffer.argtypes = [ctypes.c_char_p, ctypes.c_size_t,
    ctypes.c_char_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_int]
ALG = 0x702
src = open(sys.argv[1], 'rb').read()
n = lib.compression_encode_scratch_buffer_size(ALG)
scratch = ctypes.create_string_buffer(n) if n else None
dst = ctypes.create_string_buffer(len(src) + 65536)
m = lib.compression_encode_buffer(dst, len(dst), src, len(src), scratch, ALG)
if m == 0:
    sys.exit(1)
open(sys.argv[2], 'wb').write(dst.raw[:m])
EOF
IN=$WORK/in; mkdir -p "$IN"
mkempty() { rm -rf "$IN/empty"; mkdir -p "$IN/empty"; touch -t 202001010000 "$IN/empty"; }
mkefile() { rm -rf "$IN/efile"; mkdir -p "$IN/efile"; : > "$IN/efile/f.bin"; touch -t 202001010000 "$IN/efile/f.bin" "$IN/efile"; }
mk1file() { # dir nbytes z|seedN
  rm -rf "$IN/$1"; mkdir -p "$IN/$1"
  case "$3" in
    z) head -c "$2" /dev/zero > "$IN/$1/f.bin";;
    seed*) python3 -c "import random; open('$IN/$1/f.bin','wb').write(random.Random(${3#seed}).randbytes($2))";;
  esac
  touch -t 202001010000 "$IN/$1/f.bin" "$IN/$1"
}
mkmix() { # dir (50k zeros + 50k seed11 random)
  rm -rf "$IN/$1"; mkdir -p "$IN/$1"
  python3 -c "import random; open('$IN/$1/f.bin','wb').write(bytes(50000)+random.Random(11).randbytes(50000))"
  touch -t 202001010000 "$IN/$1/f.bin" "$IN/$1"
}
RB() { # tag srcdir alg block : rb2-vs-oracle EQ + sha pins
  tag=$1; src=$2; alg=$3; blk=$4
  rm -rf "$WORK/$tag"; mkdir -p "$WORK/$tag/raw" "$WORK/$tag/pay"
  sh "$ADAPTER" aar-encode --alg raw --threads 1 "$IN/$src" "$WORK/$tag/raw.aar" 2>/dev/null
  # shellcheck disable=SC2086
  sh "$ADAPTER" aar-encode --alg "$alg" --threads 1 ${blk:+--block "$blk"} "$IN/$src" "$WORK/$tag/o.aar" 2>/dev/null
  python3 -c "
import sys
raw = open('$WORK/$tag/raw.aar','rb').read()
bs = 0
s = '$blk'.strip().lower()
if s == '': bs = 4*1024*1024
else:
    m = 1
    if s[-1] in 'bkmg': m = {'b':1,'k':1024,'m':1024**2,'g':1024**3}[s[-1]]; s = s[:-1]
    bs = int(s)*m
n = (len(raw)+bs-1)//bs
for i in range(n):
    open('$WORK/$tag/raw/blk%04d.bin' % i,'wb').write(raw[i*bs:(i+1)*bs])
print(n)"
  n=$(python3 -c "
raw = open('$WORK/$tag/raw.aar','rb').read()
s = '$blk'.strip().lower()
bs = 4*1024*1024
if s != '':
    m = 1
    if s[-1] in 'bkmg': m = {'b':1,'k':1024,'m':1024**2,'g':1024**3}[s[-1]]; s = s[:-1]
    bs = int(s)*m
print((len(raw)+bs-1)//bs)")
  i=0
  while [ "$i" -lt "$n" ]; do
    b=$(printf "$WORK/$tag/raw/blk%04d.bin" "$i")
    p=$(printf "$WORK/$tag/pay/blk%04d.bin" "$i")
    if [ "$alg" = lzraven ]; then
      "$CT" -encode -a lzraven -i "$b" -o "$p" 2>/dev/null || { echo "FAIL $tag payload $i"; FAIL=1; return; }
    else
      python3 "$WORK/bmprobe.py" "$b" "$p" 2>/dev/null || { echo "FAIL $tag payload $i"; FAIL=1; return; }
    fi
    i=$((i + 1))
  done
  # shellcheck disable=SC2086
  if python3 "$RB2" --alg "$alg" ${blk:+--block "$blk"} --payload-dir "$WORK/$tag/pay" "$WORK/$tag/raw.aar" "$WORK/$tag/r.aar" 2>"$WORK/$tag.rb2err"; then
    cmp -s "$WORK/$tag/r.aar" "$WORK/$tag/o.aar" && v=EQ || v=DIFF
    chk "r-$tag-eq" str "$v" "$(sz "$WORK/$tag/r.aar")"
    chk "r-$tag" sha "$(sha "$WORK/$tag/r.aar")" "$(sz "$WORK/$tag/r.aar")"
  else echo "FAIL $tag rb2 rc: $(head -1 "$WORK/$tag.rb2err")"; FAIL=1; fi
}
echo "== rb2 =="
mkempty; mkefile; mk1file z100k 100000 z; mk1file r1k 1000 seed6000; mkmix mix100k
for s in empty efile z100k r1k mix100k; do
  for a in lzraven lzbitmap; do
    RB "$s-$a-d" "$s" "$a" ""
    RB "$s-$a-b10k" "$s" "$a" 10000
  done
done
RB r1k-rav-b16 r1k lzraven 16
RB r1k-bm-b16 r1k lzbitmap 16
if python3 "$RB2" --alg bogus --payload-dir "$WORK/x" "$WORK/x" "$WORK/x" 2>/dev/null; then rc=0; else rc=$?; fi
chk "r-err-alg" rc "$rc" 0
if python3 "$RB2" --alg lzraven --block 0 --payload-dir "$WORK/x" "$WORK/x" "$WORK/x" 2>/dev/null; then rc=0; else rc=$?; fi
chk "r-err-block" rc "$rc" 0
rm -rf "$WORK/mpay"; mkdir -p "$WORK/mpay"
if python3 "$RB2" --alg lzraven --payload-dir "$WORK/mpay" "$WORK/r1k-lzraven-d/raw.aar" "$WORK/mpay.out" 2>/dev/null; then rc=0; else rc=$?; fi
chk "r-err-pay" rc "$rc" 0
[ -n "${RECORD:-}" ] && mv "$PINS.new" "$PINS" && echo "RECORDED $PINS"
echo "== $WORK =="
[ "$FAIL" -eq 0 ] && echo RB2-GREEN || echo RB2-RED
exit "$FAIL"
