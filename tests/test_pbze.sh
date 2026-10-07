#!/bin/sh
# tests/test_pbze.sh [workdir] — oracle-vs-impl byte compare, lzfse path.
# exit 0 all green / 1 any FAIL.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
W=${1:-$(mktemp -d "${TMPDIR:-/tmp}/pbze.XXXXXX")}
ORACLE=${ORACLE:-/usr/bin/aa}
fail=0
cell() { # $1=name $2=block $3=alg(lzfse|zlib)
  _alg=${3:-lzfse}
  "$ORACLE" archive -a $_alg -t 1 ${2:+-b "$2"} -d "$W/in/$1" -o "$W/$1.$_alg.expect.aar" 2>"$W/$1.$_alg.err" || { echo "FAIL $1.$_alg oracle-exit=$?"; fail=1; return; }
  python3 "$ROOT/src/encode.py" "$W/in/$1" "$W/$1.$_alg.got.aar" --alg $_alg ${2:+--block "$2"} 2>>"$W/$1.$_alg.err" || { echo "FAIL $1.$_alg impl-exit=$?"; fail=1; return; }
  if cmp -s "$W/$1.$_alg.expect.aar" "$W/$1.$_alg.got.aar"; then
    echo "PASS $1.$_alg bytes=$(stat -f %z "$W/$1.$_alg.got.aar") sha=$(shasum -a 256 "$W/$1.$_alg.got.aar" | cut -c1-16)"
  else
    echo "FAIL $1.$_alg expect=$(stat -f %z "$W/$1.$_alg.expect.aar") got=$(stat -f %z "$W/$1.$_alg.got.aar")"
    cmp "$W/$1.$_alg.expect.aar" "$W/$1.$_alg.got.aar" | head -n 3
    fail=1
  fi
  # roundtrip: oracle must decode impl output
  rm -rf "$W/rt/$1.$_alg"; mkdir -p "$W/rt/$1.$_alg"
  "$ORACLE" extract -i "$W/$1.$_alg.got.aar" -d "$W/rt/$1.$_alg" 2>>"$W/$1.$_alg.err" || { echo "FAIL $1.$_alg roundtrip-exit=$?"; fail=1; }
}
fix() { find "$1" -exec touch -d '2001-02-03 04:05:06' {} + 2>/dev/null; touch -h -d '2001-02-03 04:05:06' $(find "$1" -type l) 2>/dev/null; return 0; }
mkdir -p "$W/in/z1"; python3 -c "open('$W/in/z1/p','wb').write(b'ABCD'*3000)"; fix "$W/in/z1"
mkdir -p "$W/in/r1"; python3 -c "import random;random.seed(9);open('$W/in/r1/p','wb').write(bytes(random.randrange(256) for _ in range(3000)))"; fix "$W/in/r1"
mkdir -p "$W/in/mb"; python3 -c "open('$W/in/mb/p','wb').write(b'\xAB'*5000000)"; fix "$W/in/mb"
mkdir -p "$W/in/mix"; python3 -c "import random;random.seed(3);open('$W/in/mix/p','wb').write(bytes(random.randrange(256) for _ in range(1048576))+b'\x00'*600000)"; fix "$W/in/mix"
cell z1 ""
cell r1 ""
cell mb 1m
cell mix 1m
cell z1 "" zlib
cell r1 "" zlib
cell mb 1m zlib
cell mix 1m zlib
[ $fail -eq 0 ] && echo PBZE-GREEN || echo PBZE-RED
exit $fail
