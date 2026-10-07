#!/bin/sh
# tests/test_rawenc.sh [workdir] — oracle-vs-impl byte compare, raw AAR.
# exit 0 all green / 1 any FAIL. Fixed mtimes (S-times) => deterministic.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
W=${1:-$(mktemp -d "${TMPDIR:-/tmp}/rawenc.XXXXXX")}
ORACLE=${ORACLE:-/usr/bin/aa}
fail=0
mk() { # $1=name -> builds $W/in/$1, caller fills, then fix()
  mkdir -p "$W/in/$1"
}
fix() { # pin all mtimes under dir ($1) to fixed stamp
  find "$1" -exec touch -d '2001-02-03 04:05:06' {} + 2>/dev/null
  touch -h -d '2001-02-03 04:05:06' $(find "$1" -type l) 2>/dev/null
  return 0
}
cell() { # $1=name
  "$ORACLE" archive -a raw -t 1 -d "$W/in/$1" -o "$W/$1.expect.aar" 2>"$W/$1.err" || { echo "FAIL $1 oracle-exit=$?"; fail=1; return; }
  python3 "$ROOT/src/rawenc.py" "$W/in/$1" "$W/$1.got.aar" 2>>"$W/$1.err" || { echo "FAIL $1 impl-exit=$?"; fail=1; return; }
  if cmp -s "$W/$1.expect.aar" "$W/$1.got.aar"; then
    echo "PASS $1 bytes=$(stat -f %z "$W/$1.got.aar") sha=$(shasum -a 256 "$W/$1.got.aar" | cut -c1-16)"
  else
    echo "FAIL $1 expect=$(stat -f %z "$W/$1.expect.aar") got=$(stat -f %z "$W/$1.got.aar")"
    cmp "$W/$1.expect.aar" "$W/$1.got.aar" | head -n 3
    fail=1
  fi
}
# c1 empty
mk c1; fix "$W/in/c1"
# c2 one empty file
mk c2; : > "$W/in/c2/e.txt"; fix "$W/in/c2"
# c3 one 9B file
mk c3; printf '123456789' > "$W/in/c3/nine.bin"; fix "$W/in/c3"
# c4 kitchen sink: nested, symlink, xattr, unicode, mode
mk c4; mkdir -p "$W/in/c4/sub/deep"
printf 'DEEP' > "$W/in/c4/sub/deep/f.txt"; printf 'TOP' > "$W/in/c4/top.txt"
ln -s top.txt "$W/in/c4/link.txt"; printf 'X' > "$W/in/c4/run.sh"; chmod 755 "$W/in/c4/run.sh"
printf 'U' > "$W/in/c4/café.txt"; xattr -w user.k v123 "$W/in/c4/top.txt"
fix "$W/in/c4"
# c5 70KB (DAT'B')
mk c5; python3 -c "import sys; sys.stdout.buffer.write(bytes((i*13+1)&0xFF for i in range(70000)))" > "$W/in/c5/big.bin"; fix "$W/in/c5"
# c6 65535B + 65536B boundary pair
mk c6; python3 -c "import sys; sys.stdout.buffer.write(bytes((i*7)&0xFF for i in range(65535)))" > "$W/in/c6/a65k"
python3 -c "import sys; sys.stdout.buffer.write(bytes((i*7)&0xFF for i in range(65536)))" > "$W/in/c6/b65k"; fix "$W/in/c6"
# c7 live mtimes (T-path, compare-only: oracle+impl same tree, no writes between)
mk c7; mkdir -p "$W/in/c7/sub"
printf 'live1' > "$W/in/c7/b.txt"; printf 'live2' > "$W/in/c7/sub/a.txt"; ln -s b.txt "$W/in/c7/z"
# c8 adversarial order: created z,m,a (reverse); oracle must emit sorted
mk c8; printf '1' > "$W/in/c8/zebra"; printf '2' > "$W/in/c8/mike"; printf '3' > "$W/in/c8/apple"; fix "$W/in/c8"
for c in c1 c2 c3 c4 c5 c6 c7 c8; do cell $c; done
[ $fail -eq 0 ] && echo RAWENC-GREEN || echo RAWENC-RED
exit $fail
