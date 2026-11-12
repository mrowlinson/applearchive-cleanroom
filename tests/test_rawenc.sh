#!/bin/sh
# tests/test_rawenc.sh [workdir] — oracle-vs-impl byte compare, raw AAR.
# exit 0 all green / 1 any FAIL. Fixed mtimes (S-times) => deterministic.
set -u
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
W=${1:-$(mktemp -d "$TMPDIR/rawenc.XXXXXX")}
ORACLE=${ORACLE:-/usr/bin/aa}
_IMP=${ENC_BIN:-python3 "$ROOT/src/rawenc.py"}
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
  $_IMP "$W/in/$1" "$W/$1.got.aar" --alg raw 2>>"$W/$1.err" || { echo "FAIL $1 impl-exit=$?"; fail=1; return; }
  if cmp -s "$W/$1.expect.aar" "$W/$1.got.aar"; then
    echo "PASS $1 bytes=$(stat -f %z "$W/$1.got.aar") sha=$(shasum -a 256 "$W/$1.got.aar" | cut -d' ' -f1)"
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
# c9 odd modes + flags: 0600, setuid 4755, sticky subdir, UF_HIDDEN
# (MOD'1' unreachable: any readable file/listable dir has bits >0xFF;
#  width-1 covered by GID/FLG cells. unreadable input -> oracle exit 1
#  "Archive encoding failed", observed, not a cell.)
mk c9; printf 'm' > "$W/in/c9/tiny"; chmod 0600 "$W/in/c9/tiny"
printf 's' > "$W/in/c9/suid"; chmod 4755 "$W/in/c9/suid"
mkdir -p "$W/in/c9/stick"; chmod 1755 "$W/in/c9/stick"
printf 'h' > "$W/in/c9/hid"; chflags hidden "$W/in/c9/hid"
fix "$W/in/c9"
# c10 non-ASCII symlink + xattr order (created zzz first, aaa second)
mk c10; printf 'U' > "$W/in/c10/réal.txt"; ln -s "réal.txt" "$W/in/c10/liën.txt"
printf 'X' > "$W/in/c10/f"; xattr -w user.zzz FIRST "$W/in/c10/f"; xattr -w user.aaa SECOND "$W/in/c10/f"
fix "$W/in/c10"
for c in c1 c2 c3 c4 c5 c6 c7 c8 c9 c10; do cell $c; done
# c12 hardlink pair + solo control (HLC'1' on nlink>1 regular files only)
mk c12; printf 'LINKME' > "$W/in/c12/orig"; ln "$W/in/c12/orig" "$W/in/c12/hard"; printf 'SOLO' > "$W/in/c12/solo"; fix "$W/in/c12"
for c in c12; do cell $c; done
# c13 4.5GB sparse (DAT'C', RUN_BIG-gated: ~10GB transient on NVME, ~15s)
if [ "${RUN_BIG:-0}" = "1" ]; then
  BW=${BIGCELL_WS:-/Volumes/NVME/applearchive-cleanroom-ws/tmp/bigcell.$$}; rm -rf "$BW"; mkdir -p "$BW/in"
  truncate -s 4831838208 "$BW/in/big"; touch -d '2001-02-03 04:05:06' "$BW/in/big" "$BW/in"
  "$ORACLE" archive -a raw -t 1 -d "$BW/in" -o "$BW/c13.expect.aar" 2>"$W/c13.err" || { echo "FAIL c13 oracle-exit=$?"; fail=1; }
  $_IMP "$BW/in" "$BW/c13.got.aar" --alg raw 2>>"$W/c13.err" || { echo "FAIL c13 impl-exit=$?"; fail=1; }
  if cmp -s "$BW/c13.expect.aar" "$BW/c13.got.aar"; then echo "PASS c13 bytes=$(stat -f %z "$BW/c13.got.aar") sha=$(shasum -a 256 "$BW/c13.got.aar" | cut -d' ' -f1)"; else echo "FAIL c13"; fail=1; fi
  rm -rf "$BW"
else
  echo "SKIP c13 (RUN_BIG=1 to run)"
fi
# c11 live unix socket (compare-only; short path for AF_UNIX limit)
C11_IMP="$_IMP" python3 - "$W" "$ROOT" "$ORACLE" <<'EOF'
import os, shlex, socket, subprocess, sys
W, ROOT, ORACLE = sys.argv[1], sys.argv[2], sys.argv[3]
d = os.path.join(W, "sockcell.%d" % os.getpid())
os.makedirs(d, exist_ok=True)
p = os.path.join(d, "sk")
try: os.unlink(p)
except OSError: pass
s = socket.socket(socket.AF_UNIX); s.bind(p)
r1 = subprocess.run([ORACLE, "archive", "-a", "raw", "-t", "1", "-d", d, "-o", W + "/c11.expect.aar"], capture_output=True)
r2 = subprocess.run(shlex.split(os.environ["C11_IMP"]) + [d, W + "/c11.got.aar", "--alg", "raw"], capture_output=True)
s.close()
e = open(W + "/c11.expect.aar", "rb").read(); g = open(W + "/c11.got.aar", "rb").read()
print(("PASS" if (r1.returncode == 0 and e == g) else "FAIL") + " c11 bytes=%d" % len(g))
sys.exit(0 if (r1.returncode == 0 and e == g) else 1)
EOF
[ $? -ne 0 ] && fail=1; [ $fail -eq 0 ] && echo RAWENC-GREEN || echo RAWENC-RED
exit $fail
