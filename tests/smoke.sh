#!/bin/sh
# smoke.sh — T0 smoke tier skeleton (see harness/BATTERY.md).
# 2 cells: AAR roundtrip + AEA roundtrip. No pins. Exit 0 green / 1 FAIL / 2 harness error.
# Usage: tests/smoke.sh [workdir]; workdir defaults to mktemp under $TMPDIR.
# Backend override: BACKEND=/path/to/impl-adapter (same CLI contract). Default: harness oracle adapter.
set -eu

HERE=$(cd "$(dirname "$0")" && pwd)
ADAPTER=${BACKEND:-$HERE/../harness/oracle-adapter.sh}
WORK=${1:-$(mktemp -d "${TMPDIR:-/tmp}/aax-smoke.XXXXXX")}
FAIL=0

cell() { # name -- cmd...
  name=$1; shift
  if "$@" >/dev/null 2>"$WORK/$name.stderr"; then
    echo "PASS $name"
  else
    echo "FAIL $name (see $WORK/$name.stderr)"
    FAIL=1
  fi
}

mkdir -p "$WORK"
echo "== probe =="
sh "$ADAPTER" probe || exit 2

echo "== cell aar-roundtrip =="
mkdir -p "$WORK/src/sub"
printf 'hello-aar\n' > "$WORK/src/a.txt"
printf 'nested-bytes-0123456789\n' > "$WORK/src/sub/b.txt"
cell aar-encode sh "$ADAPTER" aar-encode --alg lzfse --threads 1 "$WORK/src" "$WORK/t.aar"
cell aar-decode sh "$ADAPTER" aar-decode "$WORK/t.aar" "$WORK/out"
if [ -f "$WORK/out/a.txt" ] && cmp -s "$WORK/src/a.txt" "$WORK/out/a.txt" \
   && cmp -s "$WORK/src/sub/b.txt" "$WORK/out/sub/b.txt"; then
  echo "PASS aar-bytes"
else
  echo "FAIL aar-bytes"; FAIL=1
fi

echo "== cell aea-roundtrip =="
printf 'hello-aea-secret-bytes\n' > "$WORK/plain.bin"
# NOTE: profile 5 (scrypt) rejects passwords < 20 UTF-8 bytes
# ("Password is too short", error 0xb9076000, encrypt + decrypt).
# Pin: smoke pw fixed below (>= 20 bytes).
PW="smoke-test-passphrase-32-chars-ok12"
cell aea-encrypt sh "$ADAPTER" aea-encrypt --profile 5 --password "$PW" \
  --alg none --threads 1 "$WORK/plain.bin" "$WORK/t.aea"
cell aea-decrypt sh "$ADAPTER" aea-decrypt --password "$PW" "$WORK/t.aea" "$WORK/back.bin"
if [ -f "$WORK/back.bin" ] && cmp -s "$WORK/plain.bin" "$WORK/back.bin"; then
  echo "PASS aea-bytes"
else
  echo "FAIL aea-bytes"; FAIL=1
fi

echo "== $WORK =="
[ "$FAIL" -eq 0 ] && echo SMOKE-GREEN || echo SMOKE-RED
exit "$FAIL"
