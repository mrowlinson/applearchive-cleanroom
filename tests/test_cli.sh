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

echo "== cells honest-UNSUPPORTED (no stub, sibling lanes own them) =="
if python3 "$IMPL" aea-encrypt --profile 5 --password x "$WORK/src/a.txt" "$WORK/x.aea" 2>"$WORK/u-enc.stderr"; then
  fail "unsup-aea-encrypt-exit"
else grep -q "UNSUPPORTED" "$WORK/u-enc.stderr" && pass "unsup-aea-encrypt" || fail "unsup-aea-encrypt"; fi
for a in lzraven lzbitmap; do
  if python3 "$IMPL" aar-encode --alg "$a" --threads 1 "$WORK/src" "$WORK/x-$a.aar" 2>"$WORK/u-$a.stderr"; then
    fail "unsup-encode-exit-$a"
  else grep -q "UNSUPPORTED" "$WORK/u-$a.stderr" && pass "unsup-encode-$a" || fail "unsup-encode-$a"; fi
done
# oracle sanity: these ARE supported by vendor (proves gap is impl-subset, not fixture)
sh "$ORACLE" aar-encode --alg lzraven --threads 1 "$WORK/src" "$WORK/o-rav.aar" >/dev/null 2>&1 && pass "oracle-has-lzraven" || fail "oracle-has-lzraven"
sh "$ORACLE" aar-encode --alg lzbitmap --threads 1 "$WORK/src" "$WORK/o-lzbm.aar" >/dev/null 2>&1 && pass "oracle-has-lzbitmap" || fail "oracle-has-lzbitmap"

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
