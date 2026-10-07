#!/bin/sh
# c-battery.sh — C deliverable battery vs oracle (AAR decode).
# Usage: tests/c-battery.sh [workdir]; default WS cbattery.XXXXXX.
# Exit 0 all green / 1 any FAIL / 2 harness error. Needs: make, ZBM n/a.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
WORK=${1:-$(mktemp -d /Volumes/NVME/applearchive-cleanroom-ws/cbattery.XXXXXX)}
AAD=$WORK/aad-bin
FAIL=0
pass() { echo "PASS $1"; }
fail() { echo "FAIL $1"; FAIL=1; }
die() { echo "HARNESS-ERROR $*" >&2; exit 2; }

command -v cc >/dev/null || die "no cc"
make -C "$ROOT" OUTDIR="$WORK/build" >/dev/null 2>&1 || die "make failed"
cp "$WORK/build/aad" "$AAD"
ADAPTER=$ROOT/harness/oracle-adapter.sh
V=$ROOT/vectors/selfgen
(cd "$V" && shasum -c SHA256SUMS >/dev/null 2>&1) || die "pins drifted"

echo "== cell fixtures-bytes (8) =="
for f in hello-lzfse hello-lzma hello-lzraven hello-zlib hello-lz4 hello-lzbitmap hello-raw empty-lzfse; do
  "$AAD" "$V/aar/$f.aar" "$WORK/c-$f" 2>/dev/null || { fail "c-$f"; continue; }
  sh "$ADAPTER" aar-decode "$V/aar/$f.aar" "$WORK/o-$f" >/dev/null 2>&1 || { fail "o-$f"; continue; }
  diff -r "$WORK/o-$f" "$WORK/c-$f" >/dev/null 2>&1 && pass "bytes-$f" || fail "bytes-$f"
done

echo "== cell attrtree-full (7 algs) =="
mkdir -p "$WORK/src/sub"
printf 'data\n' > "$WORK/src/f.txt"; chmod 640 "$WORK/src/f.txt"
ln -s f.txt "$WORK/src/rel-link"; ln -s /tmp/abs-target "$WORK/src/abs-link"
printf 'sub\n' > "$WORK/src/sub/g.txt"
xattr -w com.example.tag "TAGBYTES" "$WORK/src/f.txt" 2>/dev/null || die "xattr"
touch -t 202001020304.05 "$WORK/src/f.txt" "$WORK/src/sub/g.txt"
for a in lzfse lzma lzraven zlib lz4 lzbitmap raw; do
  sh "$ADAPTER" aar-encode --alg "$a" --threads 1 "$WORK/src" "$WORK/$a.aar" >/dev/null 2>&1 || { fail "enc-$a"; continue; }
  sh "$ADAPTER" aar-decode "$WORK/$a.aar" "$WORK/o-$a" >/dev/null 2>&1 || { fail "odec-$a"; continue; }
  "$AAD" "$WORK/$a.aar" "$WORK/c-$a" 2>/dev/null || { fail "cdec-$a"; continue; }
  python3 - "$WORK/o-$a" "$WORK/c-$a" <<'EOF' >/dev/null 2>&1 && pass "full-$a" || fail "full-$a"
import os, sys
def sig(root):
  d = {}
  for dp, dn, fn in os.walk(root):
    for n in sorted(dn + fn):
      p = os.path.join(dp, n); s = os.lstat(p)
      d[os.path.relpath(p, root)] = (oct(s.st_mode), s.st_uid, s.st_gid,
        s.st_mtime_ns, s.st_birthtime,
        os.readlink(p) if os.path.islink(p) else open(p, 'rb').read() if os.path.isfile(p) else None)
  return d
sys.exit(0 if sig(sys.argv[1]) == sig(sys.argv[2]) else 1)
EOF
done

echo "== cell wide-names (3 algs) =="
mkdir -p "$WORK/wsrc"
python3 -c "
import os
d = '$WORK/wsrc'
open(d + '/empty.bin', 'wb').close()
open(d + '/uni-h\xe9llo-\U0001f5dc.txt', 'w').write('unicode\n')
p = d
for i in range(20):
  p += '/nest%d' % i; os.makedirs(p, exist_ok=True)
open(p + '/deep.txt', 'w').write('deep\n')
open(d + '/odd name;with&chars().txt', 'w').write('odd\n')
open(d + '/big.bin', 'wb').write(os.urandom(2000000))
"
for a in lzfse zlib raw; do
  sh "$ADAPTER" aar-encode --alg "$a" --threads 1 "$WORK/wsrc" "$WORK/w-$a.aar" >/dev/null 2>&1 || { fail "wenc-$a"; continue; }
  sh "$ADAPTER" aar-decode "$WORK/w-$a.aar" "$WORK/wo-$a" >/dev/null 2>&1 || { fail "wodec-$a"; continue; }
  "$AAD" "$WORK/w-$a.aar" "$WORK/wc-$a" 2>/dev/null || { fail "wcdec-$a"; continue; }
  diff -r "$WORK/wo-$a" "$WORK/wc-$a" >/dev/null 2>&1 && pass "wide-$a" || fail "wide-$a"
done

echo "== cell multiblock =="
python3 -c "open('$WORK/big.bin','wb').write(b'Q'*300000)"
mkdir -p "$WORK/bsrc"; mv "$WORK/big.bin" "$WORK/bsrc/"
sh "$ADAPTER" aar-encode --alg lzfse --block 64k --threads 1 "$WORK/bsrc" "$WORK/mb.aar" >/dev/null 2>&1 || die "mb encode"
sh "$ADAPTER" aar-decode "$WORK/mb.aar" "$WORK/o-mb" >/dev/null 2>&1 || die "mb oracle"
"$AAD" "$WORK/mb.aar" "$WORK/c-mb" 2>/dev/null || fail "mb-cdec"
diff -r "$WORK/o-mb" "$WORK/c-mb" >/dev/null 2>&1 && pass "mb-bytes" || fail "mb-bytes"

echo "== cell hardlink =="
mkdir -p "$WORK/hsrc"
printf 'AAA-group0\n' > "$WORK/hsrc/a1.txt"; ln "$WORK/hsrc/a1.txt" "$WORK/hsrc/a2.txt"; ln "$WORK/hsrc/a1.txt" "$WORK/hsrc/a3.txt"
printf 'BBB-group1\n' > "$WORK/hsrc/b1.txt"; ln "$WORK/hsrc/b1.txt" "$WORK/hsrc/b2.txt"
printf 'lonely\n' > "$WORK/hsrc/solo.txt"
sh "$ADAPTER" aar-encode --alg lzfse --threads 1 "$WORK/hsrc" "$WORK/hl.aar" >/dev/null 2>&1 || die "hl encode"
sh "$ADAPTER" aar-decode "$WORK/hl.aar" "$WORK/o-hl" >/dev/null 2>&1 || die "hl oracle"
"$AAD" "$WORK/hl.aar" "$WORK/c-hl" 2>/dev/null || fail "hl-cdec"
diff -r "$WORK/o-hl" "$WORK/c-hl" >/dev/null 2>&1 && pass "hl-bytes" || fail "hl-bytes"
python3 - "$WORK/o-hl" "$WORK/c-hl" <<'EOF' >/dev/null 2>&1 && pass "hl-links" || fail "hl-links"
import os, sys
def part(root):
  ino2paths, nl = {}, {}
  for dp, dn, fn in os.walk(root):
    for n in sorted(fn):
      p = os.path.join(dp, n); s = os.lstat(p)
      ino2paths.setdefault(s.st_ino, []).append(os.path.relpath(p, root))
      nl[os.path.relpath(p, root)] = s.st_nlink
  return (sorted([tuple(sorted(v)) for v in ino2paths.values()]), nl)
sys.exit(0 if part(sys.argv[1]) == part(sys.argv[2]) else 1)
EOF

echo "== cell errors =="
head -c 100 /dev/urandom > "$WORK/corrupt.aar"
"$AAD" "$WORK/corrupt.aar" "$WORK/c-cor" 2>/dev/null && fail "corrupt-exit" || pass "corrupt-exit"
head -c 20 "$V/aar/hello-lzfse.aar" > "$WORK/trunc.aar"
"$AAD" "$WORK/trunc.aar" "$WORK/c-tru" 2>/dev/null && fail "trunc-exit" || pass "trunc-exit"

echo "== cell trunc-sweep (exit-1-or-clean, no crash) =="
SZ=$(wc -c < "$V/aar/hello-lzfse.aar" | tr -d ' ')
N=0; BAD=0
while [ "$N" -le "$SZ" ]; do
  if [ "$N" -eq 0 ]; then : > "$WORK/sw.aar"; else head -c "$N" "$V/aar/hello-lzfse.aar" > "$WORK/sw.aar"; fi
  if "$AAD" "$WORK/sw.aar" "$WORK/sw-o" 2>/dev/null; then RC=0; else RC=$?; fi
  if [ "$RC" -eq 0 ] && [ "$N" -ne "$SZ" ]; then BAD=$((BAD+1)); fi
  if [ "$RC" -gt 1 ]; then BAD=$((BAD+1)); fi
  N=$((N+37))
done
[ "$BAD" -eq 0 ] && pass "trunc-sweep" || fail "trunc-sweep"

echo "== $WORK =="
[ "$FAIL" -eq 0 ] && echo CBATTERY-GREEN || echo CBATTERY-RED
exit "$FAIL"
