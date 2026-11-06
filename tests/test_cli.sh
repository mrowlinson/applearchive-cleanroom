#!/bin/sh
# test_cli.sh — unified aae-cli battery: every contract command end to end
# vs oracle outputs (byte-compare where parity demanded, exit-code parity
# everywhere, honest-UNSUPPORTED where the subset is parked).
# Usage: tests/test_cli.sh [workdir]; default mktemp under NVME TMPDIR.
# Backend under test: src/aae-cli (impl only). Oracle: harness/oracle-adapter.sh.
# Needs: cc, make, AEAD_PY (venv python w/ cryptography+lz4), LZFSE_DYLIB for
# lzfse-encode cells (OSS dylib). Exit 0 all green / 1 any FAIL / 2 harness error.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
IMPL=$ROOT/src/aae-cli
ORACLE=$ROOT/harness/oracle-adapter.sh
NVME_WS=/Volumes/NVME/applearchive-cleanroom-ws
WORK=${1:-$(mktemp -d "${TMPDIR:-$NVME_WS/tmp}/cli-battery.XXXXXX")}
FAIL=0; PASS=0; TOTAL=0
pass() { PASS=$((PASS+1)); TOTAL=$((TOTAL+1)); echo "PASS $1"; }
fail() { TOTAL=$((TOTAL+1)); FAIL=1; echo "FAIL $1"; }
die() { echo "HARNESS-ERROR $*" >&2; exit 2; }
freeze() { find "$1" -exec touch -h -t 202001020304.05 {} + 2>/dev/null || true; }

command -v cc >/dev/null || die "no cc"
command -v make >/dev/null || die "no make"
[ -x "$IMPL" ] || die "not executable: $IMPL"
AEAD_PY=${AEAD_PY:-$NVME_WS/writer2/.venv/bin/python}
[ -x "$AEAD_PY" ] || die "no AEAD_PY: $AEAD_PY"
export AEAD_PY
if [ -z "${LZFSE_DYLIB:-}" ] && [ -f "$NVME_WS/tools/lzfse/build/bin/liblzfse.dylib" ]; then
  LZFSE_DYLIB=$NVME_WS/tools/lzfse/build/bin/liblzfse.dylib; export LZFSE_DYLIB
fi

mkdir -p "$WORK"
echo "== workdir $WORK =="
echo "== build backends (make OUTDIR/BUILDDIR under workdir; NVME only) =="
make -C "$ROOT" OUTDIR="$WORK/build-aad" >/dev/null 2>&1 || die "aad build failed"
make -C "$ROOT/src/c" BUILDDIR="$WORK/build-aae" >/dev/null 2>&1 || die "aae build failed"
AAD_BIN=$WORK/build-aad/aad; export AAD_BIN
[ -x "$AAD_BIN" ] || die "missing aad binary"
(cd "$ROOT/vectors/selfgen" && shasum -c SHA256SUMS >/dev/null 2>&1) || die "pins drifted"
V=$ROOT/vectors/selfgen

echo "== cell probe =="
if python3 "$IMPL" probe >/dev/null 2>&1; then pass "probe-impl-exit"; else fail "probe-impl-exit"; fi
if sh "$ORACLE" probe >/dev/null 2>&1; then pass "probe-oracle-exit"; else fail "probe-oracle-exit"; fi

echo "== fixture tree (frozen) =="
mkdir -p "$WORK/src/sub"
printf 'hello-aar\n' > "$WORK/src/a.txt"; chmod 640 "$WORK/src/a.txt"
printf 'nested-bytes-0123456789\n' > "$WORK/src/sub/b.txt"
ln -s a.txt "$WORK/src/rel-link" 2>/dev/null || true
xattr -w com.example.tag "TAGBYTES" "$WORK/src/a.txt" 2>/dev/null || die "xattr"
freeze "$WORK/src"

echo "== cells aar-encode 5 algs (byte parity impl vs oracle) =="
for a in raw lzfse zlib lzma lz4; do
  freeze "$WORK/src"
  if python3 "$IMPL" aar-encode --alg "$a" --threads 1 "$WORK/src" "$WORK/impl-$a.aar" 2>"$WORK/enc-$a.stderr"; then
    pass "encode-impl-exit-$a"
  else fail "encode-impl-exit-$a"; continue; fi
  if sh "$ORACLE" aar-encode --alg "$a" --threads 1 "$WORK/src" "$WORK/ora-$a.aar" >/dev/null 2>&1; then
    pass "encode-oracle-exit-$a"
  else fail "encode-oracle-exit-$a"; continue; fi
  if cmp -s "$WORK/impl-$a.aar" "$WORK/ora-$a.aar"; then pass "bytes-$a"; else fail "bytes-$a"; fi
done

echo "== cells roundtrip (impl-dec impl.aar vs oracle-dec oracle.aar) =="
for a in raw lzfse zlib lzma lz4; do
  [ -f "$WORK/impl-$a.aar" ] || { fail "skip-rt-$a"; continue; }
  python3 "$IMPL" aar-decode "$WORK/impl-$a.aar" "$WORK/i-$a" 2>/dev/null || { fail "rt-impldec-$a"; continue; }
  sh "$ORACLE" aar-decode "$WORK/ora-$a.aar" "$WORK/o-$a" >/dev/null 2>&1 || { fail "rt-oradec-$a"; continue; }
  if diff -r "$WORK/o-$a" "$WORK/i-$a" >/dev/null 2>&1; then pass "roundtrip-$a"; else fail "roundtrip-$a"; fi
done

echo "== cells cross-decode (impl-dec oracle.aar, all 7 pinned fixtures) =="
for f in hello-lzfse hello-lzma hello-lzraven hello-zlib hello-lz4 hello-lzbitmap hello-raw empty-lzfse; do
  python3 "$IMPL" aar-decode "$V/aar/$f.aar" "$WORK/x-$f" 2>/dev/null || { fail "xdec-$f"; continue; }
  sh "$ORACLE" aar-decode "$V/aar/$f.aar" "$WORK/xo-$f" >/dev/null 2>&1 || { fail "xdec-ora-$f"; continue; }
  if diff -r "$WORK/xo-$f" "$WORK/x-$f" >/dev/null 2>&1; then pass "xbytes-$f"; else fail "xbytes-$f"; fi
done

echo "== cells aar-list (normalized compare + exit parity) =="
for f in hello-lzfse empty-lzfse; do
  python3 "$IMPL" aar-list "$V/aar/$f.aar" >"$WORK/il-$f.txt" 2>/dev/null; ie=$?
  sh "$ORACLE" aar-list "$V/aar/$f.aar" >"$WORK/ol-$f.txt" 2>/dev/null; oe=$?
  [ "$ie" -eq "$oe" ] && pass "list-exit-$f" || fail "list-exit-$f"
  grep -v '^$' "$WORK/il-$f.txt" | sort >"$WORK/il-$f.n"; grep -v '^$' "$WORK/ol-$f.txt" | sort >"$WORK/ol-$f.n"
  if cmp -s "$WORK/il-$f.n" "$WORK/ol-$f.n"; then pass "list-bytes-$f"; else fail "list-bytes-$f"; fi
done

echo "== cells aea-id (byte parity) =="
for f in hello-p1-nopad hello-p5; do
  python3 "$IMPL" aea-id "$V/aea/$f.aea" >"$WORK/ii-$f.txt" 2>/dev/null || { fail "id-impl-exit-$f"; continue; }
  /usr/bin/aea id -i "$V/aea/$f.aea" >"$WORK/oi-$f.txt" 2>/dev/null || { fail "id-oracle-exit-$f"; continue; }
  pass "id-impl-exit-$f"
  if cmp -s "$WORK/ii-$f.txt" "$WORK/oi-$f.txt"; then pass "id-bytes-$f"; else fail "id-bytes-$f"; fi
done

echo "== cells aea-decrypt (byte parity impl vs oracle) =="
KEYHEX=$(xxd -p "$V/aea/testkey.bin" | tr -d '\n')
python3 "$IMPL" aea-decrypt --key "$KEYHEX" "$V/aea/hello-p1-nopad.aea" "$WORK/d-p1.bin" 2>/dev/null || fail "dec-impl-exit-p1"
aea decrypt -key "$V/aea/testkey.bin" -i "$V/aea/hello-p1-nopad.aea" -o "$WORK/do-p1.bin" 2>/dev/null || fail "dec-oracle-exit-p1"
if cmp -s "$WORK/d-p1.bin" "$WORK/do-p1.bin"; then pass "dec-bytes-p1"; else fail "dec-bytes-p1"; fi
PW='test-password-fixture'
python3 "$IMPL" aea-decrypt --password "$PW" "$V/aea/hello-p5.aea" "$WORK/d-p5.bin" 2>/dev/null || fail "dec-impl-exit-p5"
aea decrypt -password-value "$PW" -i "$V/aea/hello-p5.aea" -o "$WORK/do-p5.bin" 2>/dev/null || fail "dec-oracle-exit-p5"
if cmp -s "$WORK/d-p5.bin" "$WORK/do-p5.bin"; then pass "dec-bytes-p5"; else fail "dec-bytes-p5"; fi
# stdio shape: IN=- OUT=- pipe parity
if aea encrypt -profile 1 -key "$V/aea/testkey.bin" -a none -padding none -i "$V/aar/hello-raw.aar" -o "$WORK/p1-none.aea" 2>/dev/null; then
  pass "stdio-fixture-exit"
  if "$AEAD_PY" -c "import sys" </dev/null 2>/dev/null; then
    if python3 "$IMPL" aea-decrypt --key "$KEYHEX" - - <"$WORK/p1-none.aea" >"$WORK/d-stdio.bin" 2>/dev/null \
       && aea decrypt -key "$V/aea/testkey.bin" -i "$WORK/p1-none.aea" -o "$WORK/do-stdio.bin" 2>/dev/null \
       && cmp -s "$WORK/d-stdio.bin" "$WORK/do-stdio.bin"; then pass "dec-stdio-bytes"; else fail "dec-stdio-bytes"; fi
  fi
else fail "stdio-fixture-exit"; fi

echo "== cells aar-encode lzraven (parity, wired via src/encode.py) =="
mkdir -p "$WORK/ravdir"
python3 -c "import random;random.seed(7);open('$WORK/ravdir/p','wb').write(bytes(random.randrange(256) for _ in range(3000)))"
python3 -c "import random;random.seed(8);open('$WORK/ravdir/q','wb').write(bytes(random.randrange(256) for _ in range(100000)))"
freeze "$WORK/ravdir"
if python3 "$IMPL" aar-encode --alg lzraven --threads 1 "$WORK/ravdir" "$WORK/impl-rav.aar" 2>"$WORK/enc-rav.stderr"; then
  pass "encode-impl-exit-lzraven"
else fail "encode-impl-exit-lzraven"; fi
if sh "$ORACLE" aar-encode --alg lzraven --threads 1 "$WORK/ravdir" "$WORK/ora-rav.aar" >/dev/null 2>&1; then
  pass "encode-oracle-exit-lzraven"
else fail "encode-oracle-exit-lzraven"; fi
if cmp -s "$WORK/impl-rav.aar" "$WORK/ora-rav.aar"; then pass "bytes-lzraven"; else fail "bytes-lzraven"; fi
# non-default block size parity (mirrors sibling E2E e2e1k)
if python3 "$IMPL" aar-encode --alg lzraven --block 1k --threads 1 "$WORK/ravdir" "$WORK/impl-rav1k.aar" 2>/dev/null \
   && sh "$ORACLE" aar-encode --alg lzraven --block 1k --threads 1 "$WORK/ravdir" "$WORK/ora-rav1k.aar" >/dev/null 2>&1 \
   && cmp -s "$WORK/impl-rav1k.aar" "$WORK/ora-rav1k.aar"; then pass "bytes-lzraven-1k"; else fail "bytes-lzraven-1k"; fi

echo "== cells aar-encode lzbitmap (parity on proven-parity input) =="
# Only parity input at .aar level: the AAR inner TLV structure itself trips
# the literal-class guards on every non-trivial dir (sibling pins: all .aar
# cells refuse except empty1). Empty dir is byte-identical vs oracle.
mkdir -p "$WORK/emptybm"
freeze "$WORK/emptybm"
if python3 "$IMPL" aar-encode --alg lzbitmap --threads 1 "$WORK/emptybm" "$WORK/impl-lzbm.aar" 2>"$WORK/enc-lzbm.stderr"; then
  pass "encode-impl-exit-lzbitmap"
else fail "encode-impl-exit-lzbitmap"; fi
if sh "$ORACLE" aar-encode --alg lzbitmap --threads 1 "$WORK/emptybm" "$WORK/ora-lzbm.aar" >/dev/null 2>&1; then
  pass "encode-oracle-exit-lzbitmap"
else fail "encode-oracle-exit-lzbitmap"; fi
if cmp -s "$WORK/impl-lzbm.aar" "$WORK/ora-lzbm.aar"; then pass "bytes-lzbitmap"; else fail "bytes-lzbitmap"; fi

echo "== cells refusal propagation (honest backend errors -> CLI exit 2 + marker) =="
mkdir -p "$WORK/zerosdir"
head -c 2000 /dev/zero > "$WORK/zerosdir/z.bin"
freeze "$WORK/zerosdir"
# lzraven: zeros run + small block -> an all-zeros block N=1024 > scope 820 -> LzRavenUnclosed
python3 "$IMPL" aar-encode --alg lzraven --block 1k --threads 1 "$WORK/zerosdir" "$WORK/x-rav.aar" 2>"$WORK/ref-rav.stderr"; rc=$?
[ "$rc" -eq 2 ] && pass "refuse-rav-exit" || fail "refuse-rav-exit"
grep -q "lzraven unclosed" "$WORK/ref-rav.stderr" && pass "refuse-rav-marker" || fail "refuse-rav-marker"
# lzbitmap: zeros file trips the order0-hot1 guard -> LzBitmapMatchFound
python3 "$IMPL" aar-encode --alg lzbitmap --threads 1 "$WORK/zerosdir" "$WORK/x-lzbm.aar" 2>"$WORK/ref-lzbm.stderr"; rc=$?
[ "$rc" -eq 2 ] && pass "refuse-lzbm-exit" || fail "refuse-lzbm-exit"
grep -q "lzbitmap match-class" "$WORK/ref-lzbm.stderr" && pass "refuse-lzbm-marker" || fail "refuse-lzbm-marker"
# oracle sanity: these ARE supported by vendor (proves gap is impl-subset, not fixture)
sh "$ORACLE" aar-encode --alg lzraven --threads 1 "$WORK/src" "$WORK/o-rav.aar" >/dev/null 2>&1 && pass "oracle-has-lzraven" || fail "oracle-has-lzraven"
sh "$ORACLE" aar-encode --alg lzbitmap --threads 1 "$WORK/src" "$WORK/o-lzbm.aar" >/dev/null 2>&1 && pass "oracle-has-lzbitmap" || fail "oracle-has-lzbitmap"

echo "== cells aea-encrypt (all 6 profiles, CLI-encrypt -> oracle-decrypt roundtrip) =="
# Encrypt output is nondeterministic (random salts/MACs), so parity here is
# interop roundtrip, not byte-compare: oracle must decrypt CLI output to the
# input bytes. (Deterministic transplant byte-compare lives in test_aea_enc.sh.)
printf 'hello aea world\n' > "$WORK/msg-aea.txt"
openssl ecparam -name prime256v1 -genkey -noout -out "$WORK/ec-priv.pem" 2>/dev/null || die "openssl ec"
openssl ec -in "$WORK/ec-priv.pem" -pubout -out "$WORK/ec-pub.pem" 2>/dev/null || die "openssl ec pub"
head -c 32 /dev/urandom > "$WORK/key32.bin"
EKEYHEX=$(xxd -p "$WORK/key32.bin" | tr -d '\n')
EPW='test-password-fixture-32................'
for p in 0 1 2 3 4 5; do
  case $p in
    0) EC="--sign-priv $WORK/ec-priv.pem"; EOD="-sign-pub $WORK/ec-pub.pem";;
    1) EC="--key $EKEYHEX"; EOD="-key $WORK/key32.bin";;
    2) EC="--key $EKEYHEX --sign-priv $WORK/ec-priv.pem"; EOD="-key $WORK/key32.bin -sign-pub $WORK/ec-pub.pem";;
    3) EC="--recipient-pub $WORK/ec-pub.pem"; EOD="-recipient-priv $WORK/ec-priv.pem";;
    4) EC="--recipient-pub $WORK/ec-pub.pem --sign-priv $WORK/ec-priv.pem"; EOD="-recipient-priv $WORK/ec-priv.pem -sign-pub $WORK/ec-pub.pem";;
    5) EC="--password $EPW"; EOD="-password-value $EPW";;
  esac
  # shellcheck disable=SC2086
  if python3 "$IMPL" aea-encrypt --profile "$p" $EC --threads 1 "$WORK/msg-aea.txt" "$WORK/e-p$p.aea" 2>"$WORK/e-p$p.stderr"; then
    pass "enc-impl-exit-p$p"
  else fail "enc-impl-exit-p$p"; continue; fi
  # shellcheck disable=SC2086
  if aea decrypt $EOD -i "$WORK/e-p$p.aea" -o "$WORK/e-p$p.out" 2>/dev/null \
     && cmp -s "$WORK/e-p$p.out" "$WORK/msg-aea.txt"; then pass "enc-roundtrip-p$p"; else fail "enc-roundtrip-p$p"; fi
done
# --alg forwarding (real compression path, not stored): repeated text + zlib
python3 -c "open('$WORK/big-aea.txt','w').write('The quick brown fox jumps over the lazy dog. '*2000)"
if python3 "$IMPL" aea-encrypt --profile 1 --key "$EKEYHEX" --alg zlib --threads 1 "$WORK/big-aea.txt" "$WORK/e-zlib.aea" 2>/dev/null; then
  pass "enc-impl-exit-zlib"
else fail "enc-impl-exit-zlib"; fi
if aea decrypt -key "$WORK/key32.bin" -i "$WORK/e-zlib.aea" -o "$WORK/e-zlib.out" 2>/dev/null \
   && cmp -s "$WORK/e-zlib.out" "$WORK/big-aea.txt"; then pass "enc-roundtrip-zlib"; else fail "enc-roundtrip-zlib"; fi
# stdio shape: IN=- OUT=- pipe roundtrip
if python3 "$IMPL" aea-encrypt --profile 1 --key "$EKEYHEX" --threads 1 - - <"$WORK/msg-aea.txt" >"$WORK/e-stdio.aea" 2>/dev/null \
   && aea decrypt -key "$WORK/key32.bin" -i "$WORK/e-stdio.aea" -o "$WORK/e-stdio.out" 2>/dev/null \
   && cmp -s "$WORK/e-stdio.out" "$WORK/msg-aea.txt"; then pass "enc-stdio-roundtrip"; else fail "enc-stdio-roundtrip"; fi
# usage: missing --profile is exit 2
python3 "$IMPL" aea-encrypt "$WORK/msg-aea.txt" "$WORK/x-nousage.aea" 2>/dev/null; rc=$?
[ "$rc" -eq 2 ] && pass "enc-usage-exit2" || fail "enc-usage-exit2"

echo "== cells exit-code parity on corrupt input =="
printf 'not-an-archive-at-all' > "$WORK/garbage.aar"
python3 "$IMPL" aar-decode "$WORK/garbage.aar" "$WORK/g1" 2>/dev/null; ie=$?
sh "$ORACLE" aar-decode "$WORK/garbage.aar" "$WORK/g2" >/dev/null 2>&1; oe=$?
if [ "$ie" -ne 0 ] && [ "$oe" -ne 0 ]; then pass "exitparity-garbage"; else fail "exitparity-garbage"; fi
python3 "$IMPL" aea-id "$WORK/garbage.aar" >/dev/null 2>&1; ie=$?
/usr/bin/aea id -i "$WORK/garbage.aar" >/dev/null 2>&1; oe=$?
if [ "$ie" -ne 0 ] && [ "$oe" -ne 0 ]; then pass "exitparity-badid"; else fail "exitparity-badid"; fi
head -c 100 "$V/aar/hello-lzfse.aar" > "$WORK/trunc.aar"
python3 "$IMPL" aar-decode "$WORK/trunc.aar" "$WORK/t1" 2>/dev/null; ie=$?
sh "$ORACLE" aar-decode "$WORK/trunc.aar" "$WORK/t2" >/dev/null 2>&1; oe=$?
if [ "$ie" -ne 0 ] && [ "$oe" -ne 0 ]; then pass "exitparity-trunc"; else fail "exitparity-trunc"; fi

echo "== cells=$PASS/$TOTAL fail=$FAIL =="
[ "$FAIL" -eq 0 ] && echo CLI-BATTERY-GREEN || echo CLI-BATTERY-RED
exit "$FAIL"
