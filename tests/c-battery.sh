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

echo "== cell special-types =="
mkdir -p "$WORK/ssrc"
python3 -c "import socket; s=socket.socket(socket.AF_UNIX); s.bind('$WORK/ssrc/sock.s'); s.close()" || die "socket mksock"
printf 'keepme\n' > "$WORK/ssrc/keep.txt"
sh "$ADAPTER" aar-encode --alg lzfse --threads 1 "$WORK/ssrc" "$WORK/sk.aar" >/dev/null 2>&1 || die "sk encode"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/sk.aar" "$WORK/o-sk" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/sk.aar" "$WORK/c-sk" 2>/dev/null || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "sk-exit" || fail "sk-exit"
diff -r "$WORK/o-sk" "$WORK/c-sk" >/dev/null 2>&1 && pass "sk-tree" || fail "sk-tree"
python3 - "$ADAPTER" "$V/aar/fifo-mixed.aar" "$WORK/o-ff" <<'EOF' >/dev/null 2>&1 || true
import subprocess, sys
try:
    subprocess.run(["sh", sys.argv[1], "aar-decode", sys.argv[2], sys.argv[3]], capture_output=True, timeout=30)
except subprocess.TimeoutExpired:
    pass
EOF
if "$AAD" "$V/aar/fifo-mixed.aar" "$WORK/c-ff" 2>/dev/null; then pass "ff-exit"; else fail "ff-exit"; fi
python3 - "$WORK/o-ff" "$WORK/c-ff" <<'EOF' >/dev/null 2>&1 && pass "ff-tree" || fail "ff-tree"
import os, stat, sys
def sig(root):
    d = {}
    for dp, dn, fn in os.walk(root):
        for n in sorted(dn + fn):
            p = os.path.join(dp, n); s = os.lstat(p); m = s.st_mode
            ft = "d" if stat.S_ISDIR(m) else "f" if stat.S_ISREG(m) else "l" if stat.S_ISLNK(m) else "p" if stat.S_ISFIFO(m) else "s" if stat.S_ISSOCK(m) else "?"
            body = open(p, "rb").read() if stat.S_ISREG(m) else None
            d[os.path.relpath(p, root)] = (ft, oct(stat.S_IMODE(m)), body)
    assert any(v[0] == "p" for v in sig(sys.argv[1]).values()), "oracle tree lacks fifo"
    sys.exit(0 if sig(sys.argv[1]) == sig(sys.argv[2]) else 1)
EOF
python3 - "$V/aar/hello-raw.aar" "$WORK/craft-Z.aar" <<'EOF' >/dev/null 2>&1 || die "craft-Z"
import sys
d = bytearray(open(sys.argv[1], "rb").read())
i = d.find(b"TYP\x31F")
assert i >= 0
d[i + 4] = ord("Z")
open(sys.argv[2], "wb").write(bytes(d))
EOF
if sh "$ADAPTER" aar-decode "$WORK/craft-Z.aar" "$WORK/o-cz" >/dev/null 2>&1; then pass "cz-orc"; else fail "cz-orc"; fi
if "$AAD" "$WORK/craft-Z.aar" "$WORK/c-cz" 2>/dev/null; then pass "cz-exit"; else fail "cz-exit"; fi
diff -r "$WORK/o-cz" "$WORK/c-cz" >/dev/null 2>&1 && pass "cz-tree" || fail "cz-tree"

echo "== cell hlink-path =="
sh "$ADAPTER" aar-decode "$V/aar/hlink-basic.aar" "$WORK/o-hb" >/dev/null 2>&1 && pass "hb-orc" || fail "hb-orc"
if "$AAD" "$V/aar/hlink-basic.aar" "$WORK/c-hb" 2>/dev/null; then pass "hb-exit"; else fail "hb-exit"; fi
python3 - "$WORK/o-hb" "$WORK/c-hb" <<'EOF' >/dev/null 2>&1 && pass "hb-links" || fail "hb-links"
import os, stat, sys
def sig(root):
  d, ino2p = {}, {}
  for dp, dn, fn in os.walk(root):
    for n in sorted(dn + fn):
      p = os.path.join(dp, n); s = os.lstat(p); m = s.st_mode
      ft = "d" if stat.S_ISDIR(m) else "f" if stat.S_ISREG(m) else "?"
      body = open(p, "rb").read() if stat.S_ISREG(m) else None
      d[os.path.relpath(p, root)] = (ft, oct(stat.S_IMODE(m)), body)
      ino2p.setdefault(s.st_ino, []).append(os.path.relpath(p, root))
  return (d, sorted([tuple(sorted(v)) for v in ino2p.values()]))
sys.exit(0 if sig(sys.argv[1]) == sig(sys.argv[2]) else 1)
EOF
ORC=0; sh "$ADAPTER" aar-decode "$V/aar/hlink-missing.aar" "$WORK/o-hm" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$V/aar/hlink-missing.aar" "$WORK/c-hm" 2>/dev/null || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "hm-exit" || fail "hm-exit"
diff -r "$WORK/o-hm" "$WORK/c-hm" >/dev/null 2>&1 && pass "hm-tree" || fail "hm-tree"
python3 - "$V/aar/hello-raw.aar" "$WORK/evil.aar" <<'EOF' >/dev/null 2>&1 || die "craft-evil"
import sys
d = bytearray(open(sys.argv[1], "rb").read())
old, new = b"hello/greet.txt", b"../evil-1234567"
i = d.find(old)
assert i >= 0
d[i:i + 15] = new
open(sys.argv[2], "wb").write(bytes(d))
EOF
ORC=0; sh "$ADAPTER" aar-decode "$WORK/evil.aar" "$WORK/o-px" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/evil.aar" "$WORK/c-px" 2>/dev/null || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "px-exit" || fail "px-exit"
diff -r "$WORK/o-px" "$WORK/c-px" >/dev/null 2>&1 && pass "px-tree" || fail "px-tree"

echo "== cell device-fail =="
ORC=0; sh "$ADAPTER" aar-decode "$V/aar/bdev-basic.aar" "$WORK/o-bd" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$V/aar/bdev-basic.aar" "$WORK/c-bd" 2>/dev/null || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "bd-exit" || fail "bd-exit"
diff -r "$WORK/o-bd" "$WORK/c-bd" >/dev/null 2>&1 && pass "bd-tree" || fail "bd-tree"
"$AAD" "$V/aar/mix-fail.aar" "$WORK/c-sx" 2>"$WORK/sx.err" || true
grep -q "not implemented yet" "$WORK/sx.err" && grep -q "1 entries failed to extract" "$WORK/sx.err" && pass "sx-tokens" || fail "sx-tokens"

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
  if [ "$RC" -eq 0 ] && [ "$N" -ne "$SZ" ] && [ "$N" -ne 0 ] && [ "$N" -ne 12 ]; then BAD=$((BAD+1)); fi
  if [ "$RC" -gt 1 ]; then BAD=$((BAD+1)); fi
  N=$((N+37))
done
[ "$BAD" -eq 0 ] && pass "trunc-sweep" || fail "trunc-sweep"

echo "== cell no-typ (TYP required on every item incl root) =="
python3 - "$V/aar/hello-raw.aar" "$WORK" <<'EOF' >/dev/null 2>&1 || die "craft-notyp"
import sys
data = open(sys.argv[1], "rb").read()
offs, i = [], 0
while True:
    i = data.find(b"TYP", i)
    if i < 0:
        break
    offs.append(i)
    i += 1
assert len(offs) == 3, offs
for j, o in enumerate(offs):
    b = bytearray(data)
    b[o:o + 3] = b"XXX"
    open("%s/notyp%d.aar" % (sys.argv[2], j), "wb").write(bytes(b))
EOF
for j in 0 1 2; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/notyp$j.aar" "$WORK/o-nt$j" >/dev/null 2>&1 || ORC=$?
  CRC=0; "$AAD" "$WORK/notyp$j.aar" "$WORK/c-nt$j" 2>/dev/null || CRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "nt-exit$j" || fail "nt-exit$j"
  diff -r "$WORK/o-nt$j" "$WORK/c-nt$j" >/dev/null 2>&1 && pass "nt-tree$j" || fail "nt-tree$j"
done
"$AAD" "$WORK/notyp1.aar" "$WORK/c-ntx" 2>"$WORK/ntx.err" || true
grep -q "no TYP field" "$WORK/ntx.err" && pass "nt-stderr" || fail "nt-stderr"

echo "== cell xattr-order (XAT applies before chmod; marker, not ambient) =="
python3 "$HERE/craft.py" setmod "$V/aar/hello-raw.aar" "$WORK/xo1.aar" hello 566 || die "craft-xo"
python3 "$HERE/craft.py" addxat "$WORK/xo1.aar" "$WORK/mod566.aar" hello com.example.mk566 MK566! || die "craft-xo2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/mod566.aar" "$WORK/o-xo" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/mod566.aar" "$WORK/c-xo" 2>/dev/null || CRC=$?
[ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] && pass "xo-exit" || fail "xo-exit"
diff -r "$WORK/o-xo" "$WORK/c-xo" >/dev/null 2>&1 && pass "xo-tree" || fail "xo-tree"
OM=$(stat -f %p "$WORK/o-xo/hello"); CM=$(stat -f %p "$WORK/c-xo/hello")
OX=0; xattr -p com.example.mk566 "$WORK/o-xo/hello" >/dev/null 2>&1 || OX=$?
CX=0; xattr -p com.example.mk566 "$WORK/c-xo/hello" >/dev/null 2>&1 || CX=$?
[ "$OM" = "$CM" ] && [ "$OM" = "40566" ] && [ "$OX" -eq 0 ] && [ "$CX" -eq 0 ] && pass "xo-metax" || fail "xo-metax"

echo "== cell adler (oracle decodes adler-broken zlib) =="
python3 - "$V/aar/hello-zlib.aar" "$WORK/adler.aar" <<'EOF' >/dev/null 2>&1 || die "craft-adler"
import sys
d = bytearray(open(sys.argv[1], "rb").read())
assert d[201] == 0xac  # pinned flip site (mid-stream, stream-valid)
d[201] = 0xf3          # breaks adler only
open(sys.argv[2], "wb").write(bytes(d))
EOF
ORC=0; sh "$ADAPTER" aar-decode "$WORK/adler.aar" "$WORK/o-ad" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/adler.aar" "$WORK/c-ad" 2>/dev/null || CRC=$?
[ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] && pass "ad-exit" || fail "ad-exit"
diff -r "$WORK/o-ad" "$WORK/c-ad" >/dev/null 2>&1 && pass "ad-tree" || fail "ad-tree"

echo "== cell xat-file-order (2 bad files; oracle order racy, SET parity) =="
python3 "$HERE/craft.py" killxat "$V/aar/hello-raw.aar" "$WORK/fsord.aar" 1 2 || die "craft-fsord"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/fsord.aar" "$WORK/o-fo" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/fsord.aar" "$WORK/c-fo" 2>"$WORK/fo.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "fo-exit" || fail "fo-exit"
diff -r "$WORK/o-fo" "$WORK/c-fo" >/dev/null 2>&1 && pass "fo-tree" || fail "fo-tree"
grep -q "2 entries failed to extract" "$WORK/fo.err" && grep -q "greet" "$WORK/fo.err" && grep -q "repeat" "$WORK/fo.err" && pass "fo-tokens" || fail "fo-tokens"

echo "== cell socket-flush (2 sockets: 1 header, forward) =="
python3 "$HERE/craft.py" settyp "$V/aar/hello-raw.aar" "$WORK/sfl1.aar" 1 S || die "craft-sfl"
python3 "$HERE/craft.py" settyp "$WORK/sfl1.aar" "$WORK/sfl.aar" 2 S || die "craft-sfl2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/sfl.aar" "$WORK/o-sf" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/sfl.aar" "$WORK/c-sf" 2>"$WORK/sf.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "sf-exit" || fail "sf-exit"
diff -r "$WORK/o-sf" "$WORK/c-sf" >/dev/null 2>&1 && pass "sf-tree" || fail "sf-tree"
SG=$(grep -n "greet" "$WORK/sf.err" | head -n 1 | cut -d: -f1); SR=$(grep -n "repeat" "$WORK/sf.err" | head -n 1 | cut -d: -f1)
[ "$(grep -c '^Error' "$WORK/sf.err" || true)" -eq 1 ] && [ "$SG" -lt "$SR" ] && grep -q "2 entries failed to extract" "$WORK/sf.err" && pass "sf-shape" || fail "sf-shape"

echo "== cell xat-plus-socket (XAT header wins, S bare, count sums) =="
python3 "$HERE/craft.py" settyp "$V/aar/hello-raw.aar" "$WORK/e4m1.aar" 1 S || die "craft-e4m"
python3 "$HERE/craft.py" killxat "$WORK/e4m1.aar" "$WORK/e4m.aar" 2 || die "craft-e4m2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/e4m.aar" "$WORK/o-em" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/e4m.aar" "$WORK/c-em" 2>"$WORK/em.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "em-exit" || fail "em-exit"
diff -r "$WORK/o-em" "$WORK/c-em" >/dev/null 2>&1 && pass "em-tree" || fail "em-tree"
[ "$(grep -c '^Error' "$WORK/em.err" || true)" -eq 1 ] && grep -q "0xe8012000" "$WORK/em.err" && grep -q "not implemented yet" "$WORK/em.err" && grep -q "2 entries failed to extract" "$WORK/em.err" && pass "em-shape" || fail "em-shape"

echo "== cell xat-dir (trailer, no count) =="
python3 "$HERE/craft.py" killxat "$V/aar/hello-raw.aar" "$WORK/xdir.aar" 0 || die "craft-xdir"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/xdir.aar" "$WORK/o-xd" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/xdir.aar" "$WORK/c-xd" 2>"$WORK/xd.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "xd-exit" || fail "xd-exit"
diff -r "$WORK/o-xd" "$WORK/c-xd" >/dev/null 2>&1 && pass "xd-tree" || fail "xd-tree"
grep -q "process dirs" "$WORK/xd.err" && ! grep -q "entries failed" "$WORK/xd.err" && pass "xd-shape" || fail "xd-shape"

echo "== cell xat-2dirs (continue, one trailer, no count) =="
mkdir -p "$WORK/x2src/a/b"; printf 'x\n' > "$WORK/x2src/a/b/f.txt"; printf 'y\n' > "$WORK/x2src/a/g.txt"
sh "$ADAPTER" aar-encode --alg raw --threads 1 "$WORK/x2src" "$WORK/x2.aar" >/dev/null 2>&1 || die "x2 encode"
python3 "$HERE/craft.py" killxatpat "$WORK/x2.aar" "$WORK/xd2.aar" a a/b || die "craft-xd2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/xd2.aar" "$WORK/o-x2" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/xd2.aar" "$WORK/c-x2" 2>"$WORK/x2.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "x2-exit" || fail "x2-exit"
diff -r "$WORK/o-x2" "$WORK/c-x2" >/dev/null 2>&1 && pass "x2-tree" || fail "x2-tree"
[ "$(grep -c 'process dirs' "$WORK/x2.err" || true)" -eq 1 ] && ! grep -q "entries failed" "$WORK/x2.err" && pass "x2-shape" || fail "x2-shape"

echo "== cell root-meta (outdir gets root MOD/MTM/XAT) =="
python3 "$HERE/craft.py" setmod "$V/aar/empty-lzfse.aar" "$WORK/rm1.aar" "" 700 || die "craft-rm"
python3 "$HERE/craft.py" setmtm "$WORK/rm1.aar" "$WORK/rm2.aar" "" 978307200 || die "craft-rm2"
python3 "$HERE/craft.py" addxat "$WORK/rm2.aar" "$WORK/rm3.aar" "" com.example.rootmark2 MARK2 || die "craft-rm3"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/rm3.aar" "$WORK/o-rm" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/rm3.aar" "$WORK/c-rm" 2>/dev/null || CRC=$?
[ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] && pass "rm-exit" || fail "rm-exit"
python3 - "$WORK/o-rm" "$WORK/c-rm" <<'EOF' >/dev/null 2>&1 && pass "rm-root" || fail "rm-root"
import os, subprocess, sys
o, c = sys.argv[1], sys.argv[2]
so, sc = os.lstat(o), os.lstat(c)
assert oct(so.st_mode) == oct(sc.st_mode) == "0o40700", (oct(so.st_mode), oct(sc.st_mode))
assert so.st_mtime_ns == sc.st_mtime_ns, (so.st_mtime_ns, sc.st_mtime_ns)
for r in (o, c):
    p = subprocess.run(["xattr", "-p", "com.example.rootmark2", r], capture_output=True)
    assert p.returncode == 0 and p.stdout.strip() == b"MARK2", (r, p.returncode, p.stdout)
EOF

echo "== cell no-dat (F without DAT skipped, no count) =="
python3 "$HERE/craft.py" blankdat "$V/aar/hello-raw.aar" "$WORK/nodat.aar" hello/greet.txt || die "craft-nd"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/nodat.aar" "$WORK/o-nd" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/nodat.aar" "$WORK/c-nd" 2>"$WORK/nd.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "nd-exit" || fail "nd-exit"
diff -r "$WORK/o-nd" "$WORK/c-nd" >/dev/null 2>&1 && pass "nd-tree" || fail "nd-tree"
grep -q "invalid entry final state 0" "$WORK/nd.err" && pass "nd-tok" || fail "nd-tok"

echo "== cell empty-pat-file (EISDIR counted) =="
python3 "$HERE/craft.py" zeropat "$V/aar/hello-raw.aar" "$WORK/epf.aar" hello/greet.txt || die "craft-epf"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/epf.aar" "$WORK/o-ef" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/epf.aar" "$WORK/c-ef" 2>"$WORK/ef.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "ef-exit" || fail "ef-exit"
diff -r "$WORK/o-ef" "$WORK/c-ef" >/dev/null 2>&1 && pass "ef-tree" || fail "ef-tree"
grep -q "Is a directory" "$WORK/ef.err" && grep -q "1 entries failed to extract" "$WORK/ef.err" && pass "ef-tok" || fail "ef-tok"

echo "== cell hlink-trailer (process hlinks iff H-fail) =="
"$AAD" "$V/aar/hlink-missing.aar" "$WORK/c-hm2" 2>"$WORK/hm.err" || true
grep -q "process hlinks" "$WORK/hm.err" && pass "hm-tokens" || fail "hm-tokens"

echo "== cell socket-plus-abort (S flushes after abort, counted) =="
python3 "$HERE/craft.py" settyp "$V/aar/hello-raw.aar" "$WORK/sab1.aar" 1 S || die "craft-sab"
python3 "$HERE/craft.py" blanktyp "$WORK/sab1.aar" "$WORK/sab.aar" 2 || die "craft-sab2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/sab.aar" "$WORK/o-sa" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/sab.aar" "$WORK/c-sa" 2>"$WORK/sa.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "sa-exit" || fail "sa-exit"
diff -r "$WORK/o-sa" "$WORK/c-sa" >/dev/null 2>&1 && pass "sa-tree" || fail "sa-tree"
grep -q "not implemented yet" "$WORK/sa.err" && grep -q "1 entries failed to extract" "$WORK/sa.err" && pass "sa-tok" || fail "sa-tok"

echo "== cell xat-fail-skips-rest (mode stays default) =="
python3 "$HERE/craft.py" setmod "$V/aar/hello-raw.aar" "$WORK/mx1.aar" hello/greet.txt 600 || die "craft-mx"
python3 "$HERE/craft.py" killxat "$WORK/mx1.aar" "$WORK/mx.aar" 1 || die "craft-mx2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/mx.aar" "$WORK/o-mr" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/mx.aar" "$WORK/c-mr" 2>/dev/null || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "mr-exit" || fail "mr-exit"
diff -r "$WORK/o-mr" "$WORK/c-mr" >/dev/null 2>&1 && pass "mr-tree" || fail "mr-tree"
[ "$(stat -f %p "$WORK/o-mr/hello/greet.txt")" = "$(stat -f %p "$WORK/c-mr/hello/greet.txt")" ] && [ "$(stat -f %p "$WORK/c-mr/hello/greet.txt")" = "100644" ] && pass "mr-mode" || fail "mr-mode"

echo "== cell parse-badmagic (prefix + wrapper) =="
python3 "$HERE/craft.py" setmagic "$V/aar/hello-raw.aar" "$WORK/f1.aar" 1 5A5A5A5A || die "craft-f1"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/f1.aar" "$WORK/o-pm" >/dev/null 2>"$WORK/pm-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/f1.aar" "$WORK/c-pm" 2>"$WORK/pm.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "pm-exit" || fail "pm-exit"
diff -r "$WORK/o-pm" "$WORK/c-pm" >/dev/null 2>&1 && pass "pm-tree" || fail "pm-tree"
diff "$WORK/pm-o.err" "$WORK/pm.err" >/dev/null 2>&1 && pass "pm-tok" || fail "pm-tok"

echo "== cell parse-hdrend (trailing byte: 2800) =="
python3 "$HERE/craft.py" hsdelta "$V/aar/hello-raw.aar" "$WORK/f2.aar" 1 1 || die "craft-f2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/f2.aar" "$WORK/o-ph" >/dev/null 2>"$WORK/ph-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/f2.aar" "$WORK/c-ph" 2>"$WORK/ph.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "ph-exit" || fail "ph-exit"
diff -r "$WORK/o-ph" "$WORK/c-ph" >/dev/null 2>&1 && pass "ph-tree" || fail "ph-tree"
diff "$WORK/ph-o.err" "$WORK/ph.err" >/dev/null 2>&1 && pass "ph-tok" || fail "ph-tok"

echo "== cell parse-valover (cut value: a400) =="
python3 "$HERE/craft.py" hsdelta "$V/aar/hello-raw.aar" "$WORK/hs1.aar" 1 -1 || die "craft-hs1"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/hs1.aar" "$WORK/o-pv" >/dev/null 2>"$WORK/pv-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/hs1.aar" "$WORK/c-pv" 2>"$WORK/pv.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "pv-exit" || fail "pv-exit"
diff -r "$WORK/o-pv" "$WORK/c-pv" >/dev/null 2>&1 && pass "pv-tree" || fail "pv-tree"
diff "$WORK/pv-o.err" "$WORK/pv.err" >/dev/null 2>&1 && pass "pv-tok" || fail "pv-tok"

echo "== cell parse-badsubtype (DAT/K: 75) =="
python3 "$HERE/craft.py" setsub "$V/aar/hello-raw.aar" "$WORK/f4.aar" hello/greet.txt DAT K || die "craft-f4"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/f4.aar" "$WORK/o-pb" >/dev/null 2>"$WORK/pb-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/f4.aar" "$WORK/c-pb" 2>"$WORK/pb.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "pb-exit" || fail "pb-exit"
diff -r "$WORK/o-pb" "$WORK/c-pb" >/dev/null 2>&1 && pass "pb-tree" || fail "pb-tree"
diff "$WORK/pb-o.err" "$WORK/pb.err" >/dev/null 2>&1 && pass "pb-tok" || fail "pb-tok"

echo "== cell parse-blobover (DAT huge: counted) =="
python3 "$HERE/craft.py" setbloblen "$V/aar/hello-raw.aar" "$WORK/f3.aar" hello/greet.txt DAT 32767 || die "craft-f3"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/f3.aar" "$WORK/o-po" >/dev/null 2>"$WORK/po-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/f3.aar" "$WORK/c-po" 2>"$WORK/po.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "po-exit" || fail "po-exit"
diff -r "$WORK/o-po" "$WORK/c-po" >/dev/null 2>&1 && pass "po-tree" || fail "po-tree"
diff "$WORK/po-o.err" "$WORK/po.err" >/dev/null 2>&1 && pass "po-tok" || fail "po-tok"

echo "== cell parse-tail (trailing garbage: full prefix) =="
python3 "$HERE/craft.py" append "$V/aar/hello-raw.aar" "$WORK/tail1.aar" 5A || die "craft-tail"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/tail1.aar" "$WORK/o-pt" >/dev/null 2>"$WORK/pt-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/tail1.aar" "$WORK/c-pt" 2>"$WORK/pt.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "pt-exit" || fail "pt-exit"
diff -r "$WORK/o-pt" "$WORK/c-pt" >/dev/null 2>&1 && pass "pt-tree" || fail "pt-tree"
diff "$WORK/pt-o.err" "$WORK/pt.err" >/dev/null 2>&1 && pass "pt-tok" || fail "pt-tok"

echo "== cell parse-hsbig (hsize overrun: a400) =="
python3 "$HERE/craft.py" hsdelta "$V/aar/hello-raw.aar" "$WORK/hsbig.aar" 2 1000 || die "craft-hsbig"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/hsbig.aar" "$WORK/o-pg" >/dev/null 2>"$WORK/pg-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/hsbig.aar" "$WORK/c-pg" 2>"$WORK/pg.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "pg-exit" || fail "pg-exit"
diff -r "$WORK/o-pg" "$WORK/c-pg" >/dev/null 2>&1 && pass "pg-tree" || fail "pg-tree"
diff "$WORK/pg-o.err" "$WORK/pg.err" >/dev/null 2>&1 && pass "pg-tok" || fail "pg-tok"

echo "== cell typ-uint248 (wider uint TYP accepted) =="
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/t2.aar" 1 545950324600 || die "craft-t2"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/t4.aar" 1 5459503446000000 || die "craft-t4"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/t8.aar" 1 545950384600000000000000 || die "craft-t8"
TUOK=1
for v in t2 t4 t8; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$v.aar" "$WORK/o-$v" >/dev/null 2>&1 || ORC=$?
  CRC=0; "$AAD" "$WORK/$v.aar" "$WORK/c-$v" 2>/dev/null || CRC=$?
  [ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] || TUOK=0
  diff -r "$WORK/o-$v" "$WORK/c-$v" >/dev/null 2>&1 || TUOK=0
done
[ "$TUOK" -eq 1 ] && pass "tu-exit" || fail "tu-exit"
[ "$TUOK" -eq 1 ] && pass "tu-tree" || fail "tu-tree"

echo "== cell typ-enum (non-uint TYP: type-N abort) =="
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tP.aar" 1 54595050010046 || die "craft-tP"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tS.aar" 1 545950534600000000000000 || die "craft-tS"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tT.aar" 1 54595054460000000000000000000000 || die "craft-tT"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tE.aar" 1 5459502a || die "craft-tE"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tH.aar" 1 545950484600000000000000000000000000000000000000000000000000000000000000 || die "craft-tH"
GHEX=54595047$(python3 -c 'print("00"*20)')
IHEX=54595049$(python3 -c 'print("00"*48)')
JHEX=5459504a$(python3 -c 'print("00"*64)')
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tG.aar" 1 "$GHEX" || die "craft-tG"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tI.aar" 1 "$IHEX" || die "craft-tI"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tJ.aar" 1 "$JHEX" || die "craft-tJ"
TEOK=1
for v in tP tS tT tE tH tG tI tJ; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$v.aar" "$WORK/o-$v" >/dev/null 2>"$WORK/$v-o.err" || ORC=$?
  CRC=0; "$AAD" "$WORK/$v.aar" "$WORK/c-$v" 2>"$WORK/$v.err" || CRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] || TEOK=0
  diff -r "$WORK/o-$v" "$WORK/c-$v" >/dev/null 2>&1 || TEOK=0
  diff "$WORK/$v-o.err" "$WORK/$v.err" >/dev/null 2>&1 || TEOK=0
done
[ "$TEOK" -eq 1 ] && pass "te-exit" || fail "te-exit"
[ "$TEOK" -eq 1 ] && pass "te-tree" || fail "te-tree"
[ "$TEOK" -eq 1 ] && pass "te-tok" || fail "te-tok"

echo "== cell eisdir-order (S < EISDIR < nodat) =="
python3 "$HERE/craft.py" zeropat "$V/aar/hello-raw.aar" "$WORK/es1a.aar" hello/greet.txt || die "craft-es1"
python3 "$HERE/craft.py" settyp "$WORK/es1a.aar" "$WORK/es1.aar" 2 S || die "craft-es1b"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/es1.aar" "$WORK/o-eo" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/es1.aar" "$WORK/c-eo" 2>"$WORK/eo.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "eo-exit" || fail "eo-exit"
diff -r "$WORK/o-eo" "$WORK/c-eo" >/dev/null 2>&1 && pass "eo-tree" || fail "eo-tree"
ES=$(grep -n "not implemented yet" "$WORK/eo.err" | head -n 1 | cut -d: -f1); EE=$(grep -n "Is a directory" "$WORK/eo.err" | head -n 1 | cut -d: -f1)
[ "$ES" -lt "$EE" ] && grep -q "2 entries failed to extract" "$WORK/eo.err" && pass "eo-shape" || fail "eo-shape"

echo "== cell wrapper-eisdir (wrapper first, EISDIR bare) =="
python3 "$HERE/craft.py" zeropat "$V/aar/hello-raw.aar" "$WORK/ef1a.aar" hello/greet.txt || die "craft-ef1"
python3 "$HERE/craft.py" setmagic "$WORK/ef1a.aar" "$WORK/ef1.aar" 2 5A5A5A5A || die "craft-ef1b"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/ef1.aar" "$WORK/o-ew" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/ef1.aar" "$WORK/c-ew" 2>"$WORK/ew.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "ew-exit" || fail "ew-exit"
diff -r "$WORK/o-ew" "$WORK/c-ew" >/dev/null 2>&1 && pass "ew-tree" || fail "ew-tree"
EW=$(grep -n "invalid header magic" "$WORK/ew.err" | head -n 1 | cut -d: -f1); EE=$(grep -n "Is a directory" "$WORK/ew.err" | head -n 1 | cut -d: -f1)
[ "$EW" -lt "$EE" ] && grep -q "1 entries failed to extract" "$WORK/ew.err" && pass "ew-shape" || fail "ew-shape"

echo "== cell eisdir-nodat (EISDIR < nodat) =="
python3 "$HERE/craft.py" blankdat "$V/aar/hello-raw.aar" "$WORK/ne1.aar" hello/greet.txt || die "craft-ne"
python3 "$HERE/craft.py" zeropat "$WORK/ne1.aar" "$WORK/ne.aar" hello/repeat.txt || die "craft-ne2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/ne.aar" "$WORK/o-ne" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/ne.aar" "$WORK/c-ne" 2>"$WORK/ne.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "ne-exit" || fail "ne-exit"
diff -r "$WORK/o-ne" "$WORK/c-ne" >/dev/null 2>&1 && pass "ne-tree" || fail "ne-tree"
EE=$(grep -n "Is a directory" "$WORK/ne.err" | head -n 1 | cut -d: -f1); NF=$(grep -n "final state" "$WORK/ne.err" | head -n 1 | cut -d: -f1)
[ "$EE" -lt "$NF" ] && grep -q "1 entries failed to extract" "$WORK/ne.err" && pass "ne-shape" || fail "ne-shape"

echo "== cell notyp-nodat (dd: no-TYP + bare no-DAT, stderr IDENT) =="
python3 "$HERE/craft.py" blankdat "$V/aar/hello-raw.aar" "$WORK/dd1.aar" hello/greet.txt || die "craft-dd"
python3 "$HERE/craft.py" blanktyp "$WORK/dd1.aar" "$WORK/dd.aar" 2 || die "craft-dd2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/dd.aar" "$WORK/o-dd" >/dev/null 2>"$WORK/dd-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/dd.aar" "$WORK/c-dd" 2>"$WORK/dd.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "dd-exit" || fail "dd-exit"
diff -r "$WORK/o-dd" "$WORK/c-dd" >/dev/null 2>&1 && pass "dd-tree" || fail "dd-tree"
diff "$WORK/dd-o.err" "$WORK/dd.err" >/dev/null 2>&1 && pass "dd-shape" || fail "dd-shape"

echo "== cell tri-class (S + nodat + dirXAT) =="
mkdir -p "$WORK/trisrc/a/b"; printf 'x\n' > "$WORK/trisrc/a/b/f.txt"; printf 'y\n' > "$WORK/trisrc/a/g.txt"
sh "$ADAPTER" aar-encode --alg raw --threads 1 "$WORK/trisrc" "$WORK/tri0.aar" >/dev/null 2>&1 || die "tri encode"
python3 "$HERE/craft.py" blankdat "$WORK/tri0.aar" "$WORK/tri1.aar" a/b/f.txt || die "craft-tri"
python3 "$HERE/craft.py" settyppat "$WORK/tri1.aar" "$WORK/tri2.aar" a/g.txt S || die "craft-tri2"
python3 "$HERE/craft.py" killxatpat "$WORK/tri2.aar" "$WORK/tri.aar" a/b || die "craft-tri3"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/tri.aar" "$WORK/o-tr" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/tri.aar" "$WORK/c-tr" 2>"$WORK/tr.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "tr-exit" || fail "tr-exit"
diff -r "$WORK/o-tr" "$WORK/c-tr" >/dev/null 2>&1 && pass "tr-tree" || fail "tr-tree"
grep -q "not implemented yet" "$WORK/tr.err" && grep -q "final state" "$WORK/tr.err" && grep -q "process dirs" "$WORK/tr.err" && grep -q "1 entries failed to extract" "$WORK/tr.err" && pass "tr-shape" || fail "tr-shape"

echo "== cell nodat-hlink (nodat + H-fail, no count) =="
python3 "$HERE/craft.py" blankdat "$V/aar/hlink-missing.aar" "$WORK/nh2.aar" hello/repeat.txt || die "craft-nh2"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/nh2.aar" "$WORK/o-nh" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/nh2.aar" "$WORK/c-nh" 2>"$WORK/nh.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "nh-exit" || fail "nh-exit"
diff -r "$WORK/o-nh" "$WORK/c-nh" >/dev/null 2>&1 && pass "nh-tree" || fail "nh-tree"
grep -q "final state" "$WORK/nh.err" && grep -q "process hlinks" "$WORK/nh.err" && ! grep -q "entries failed" "$WORK/nh.err" && pass "nh-shape" || fail "nh-shape"

echo "== $WORK =="
echo "== cell outer-bsize (u64 bsize rule, stderr IDENT) =="
python3 "$HERE/craft.py" setbsize "$V/aar/empty-lzfse.aar" "$WORK/bs0.aar" 0000000000000000 || die "craft-bs0"
python3 "$HERE/craft.py" setbsize "$V/aar/empty-lzfse.aar" "$WORK/bsm.aar" 0000000008000001 || die "craft-bsm"
python3 "$HERE/craft.py" setbsize "$V/aar/empty-lzfse.aar" "$WORK/bshi.aar" ff00000000400000 || die "craft-bshi"
for T in bs0 bsm bshi; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$T.aar" "$WORK/o-$T" >/dev/null 2>"$WORK/$T-o.err" || ORC=$?
  mkdir -p "$WORK/c-$T"
  CRC=0; "$AAD" "$WORK/$T.aar" "$WORK/c-$T" 2>"$WORK/$T.err" || CRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "$T-exit" || fail "$T-exit"
  diff -r "$WORK/o-$T" "$WORK/c-$T" >/dev/null 2>&1 && pass "$T-tree" || fail "$T-tree"
  diff "$WORK/$T-o.err" "$WORK/$T.err" >/dev/null 2>&1 && pass "$T-shape" || fail "$T-shape"
done

echo "== cell outer-blkhdr (unc>bsize cascade, stderr IDENT) =="
python3 "$HERE/craft.py" setbsize "$V/aar/hello-lzfse.aar" "$WORK/oh.aar" 00000000000003e8 || die "craft-oh"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/oh.aar" "$WORK/o-oh" >/dev/null 2>"$WORK/oh-o.err" || ORC=$?
mkdir -p "$WORK/c-oh"
CRC=0; "$AAD" "$WORK/oh.aar" "$WORK/c-oh" 2>"$WORK/oh.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "oh-exit" || fail "oh-exit"
diff -r "$WORK/o-oh" "$WORK/c-oh" >/dev/null 2>&1 && pass "oh-tree" || fail "oh-tree"
diff "$WORK/oh-o.err" "$WORK/oh.err" >/dev/null 2>&1 && pass "oh-shape" || fail "oh-shape"

echo "== cell outer-raw64 (u64 raw naming, stderr IDENT) =="
python3 "$HERE/craft.py" setblk "$V/aar/empty-lzfse.aar" "$WORK/r64.aar" 0 01000000000000710000000000000071 || die "craft-r64"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/r64.aar" "$WORK/o-r64" >/dev/null 2>"$WORK/r64-o.err" || ORC=$?
mkdir -p "$WORK/c-r64"
CRC=0; "$AAD" "$WORK/r64.aar" "$WORK/c-r64" 2>"$WORK/r64.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "r64-exit" || fail "r64-exit"
diff -r "$WORK/o-r64" "$WORK/c-r64" >/dev/null 2>&1 && pass "r64-tree" || fail "r64-tree"
diff "$WORK/r64-o.err" "$WORK/r64.err" >/dev/null 2>&1 && pass "r64-shape" || fail "r64-shape"

echo "== cell outer-multiblock (2-block chains) =="
python3 "$HERE/craft.py" mbcat "$V/aar/hello-lzfse.aar" "$WORK/mb12.aar" "$V/aar/empty-lzfse.aar" || die "craft-mb12"
python3 "$HERE/craft.py" mbcat "$V/aar/empty-lzfse.aar" "$WORK/mb21.aar" "$V/aar/hello-lzfse.aar" || die "craft-mb21"
for T in mb12 mb21; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$T.aar" "$WORK/o-$T" >/dev/null 2>&1 || ORC=$?
  CRC=0; "$AAD" "$WORK/$T.aar" "$WORK/c-$T" 2>/dev/null || CRC=$?
  [ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] && pass "$T-exit" || fail "$T-exit"
  diff -r "$WORK/o-$T" "$WORK/c-$T" >/dev/null 2>&1 && pass "$T-tree" || fail "$T-tree"
done

echo "== cell mode-suid (chown-before-chmod keeps setgid) =="
python3 "$HERE/craft.py" setmod "$V/aar/hello-raw.aar" "$WORK/suid.aar" hello/greet.txt 3244 || die "craft-suid"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/suid.aar" "$WORK/o-suid" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/suid.aar" "$WORK/c-suid" 2>/dev/null || CRC=$?
[ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] && pass "suid-exit" || fail "suid-exit"
[ "$(stat -f %p "$WORK/o-suid/hello/greet.txt")" = "$(stat -f %p "$WORK/c-suid/hello/greet.txt")" ] && [ "$(stat -f %p "$WORK/c-suid/hello/greet.txt")" = "103244" ] && pass "suid-mode" || fail "suid-mode"
chmod u+r "$WORK/o-suid/hello/greet.txt" "$WORK/c-suid/hello/greet.txt"
diff -r "$WORK/o-suid" "$WORK/c-suid" >/dev/null 2>&1 && pass "suid-tree" || fail "suid-tree"

echo "== cell hsize-floor (u16<6: f000 + echo, stderr IDENT) =="
for NV in 0 2 5; do
  python3 "$HERE/craft.py" sethsize "$V/aar/hello-raw.aar" "$WORK/hf$NV.aar" 0 "$NV" || die "craft-hf$NV"
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/hf$NV.aar" "$WORK/o-hf$NV" >/dev/null 2>"$WORK/hf$NV-o.err" || ORC=$?
  mkdir -p "$WORK/c-hf$NV"
  CRC=0; "$AAD" "$WORK/hf$NV.aar" "$WORK/c-hf$NV" 2>"$WORK/hf$NV.err" || CRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "hf$NV-exit" || fail "hf$NV-exit"
  diff -r "$WORK/o-hf$NV" "$WORK/c-hf$NV" >/dev/null 2>&1 && pass "hf$NV-tree" || fail "hf$NV-tree"
  diff "$WORK/hf$NV-o.err" "$WORK/hf$NV.err" >/dev/null 2>&1 && pass "hf$NV-shape" || fail "hf$NV-shape"
done

echo "== cell hsize-end (u16 end>n: bd011800, stderr IDENT) =="
python3 "$HERE/craft.py" sethsize "$V/aar/hello-raw.aar" "$WORK/he1.aar" 0 2446 || die "craft-he1"
python3 "$HERE/craft.py" sethsize "$V/aar/hello-raw.aar" "$WORK/he2.aar" 0 65535 || die "craft-he2"
for T in he1 he2; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$T.aar" "$WORK/o-$T" >/dev/null 2>"$WORK/$T-o.err" || ORC=$?
  mkdir -p "$WORK/c-$T"
  CRC=0; "$AAD" "$WORK/$T.aar" "$WORK/c-$T" 2>"$WORK/$T.err" || CRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "$T-exit" || fail "$T-exit"
  diff -r "$WORK/o-$T" "$WORK/c-$T" >/dev/null 2>&1 && pass "$T-tree" || fail "$T-tree"
  diff "$WORK/$T-o.err" "$WORK/$T.err" >/dev/null 2>&1 && pass "$T-shape" || fail "$T-shape"
done

echo "== cell outer-ladder (truncation table, stderr IDENT) =="
: > "$WORK/L0.aar"
for L in 1 5 6 11 12 13 27 28 29; do head -c "$L" "$V/aar/hello-lzfse.aar" > "$WORK/L$L.aar" || die "craft-L$L"; done
printf 'XXXXXXXXXXXX' > "$WORK/LX.aar"
python3 "$HERE/craft.py" setbsize "$V/aar/hello-lzfse.aar" "$WORK/LBs0f.aar" 0000000000000000 || die "craft-LBs0"
head -c 12 "$WORK/LBs0f.aar" > "$WORK/LBs0.aar" || die "craft-LBs0t"
python3 "$HERE/craft.py" patch "$V/aar/hello-lzfse.aar" "$WORK/PQ.aar" 3 51 || die "craft-PQ"
python3 "$HERE/craft.py" patch "$V/aar/empty-lzfse.aar" "$WORK/Q2.aar" 28 5A5A5A5A || die "craft-Q2"
python3 "$HERE/craft.py" setblk "$V/aar/empty-lzfse.aar" "$WORK/Q3f.aar" 0 00000000000000030000000000000003 || die "craft-Q3"
head -c 31 "$WORK/Q3f.aar" > "$WORK/Q3.aar" || die "craft-Q3t"
python3 "$HERE/craft.py" setblk "$V/aar/empty-lzfse.aar" "$WORK/Q4f.aar" 0 00000000000000000000000000000000 || die "craft-Q4"
head -c 28 "$WORK/Q4f.aar" > "$WORK/Q4.aar" || die "craft-Q4t"
for T in L0 L1 L5 L6 L11 L12 L13 L27 L28 L29 LX LBs0 PQ Q2 Q3 Q4; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$T.aar" "$WORK/o-$T" >/dev/null 2>"$WORK/$T-o.err" || ORC=$?
  mkdir -p "$WORK/c-$T"
  CRC=0; "$AAD" "$WORK/$T.aar" "$WORK/c-$T" 2>"$WORK/$T.err" || CRC=$?
  [ "$ORC" -eq "$CRC" ] && pass "$T-exit" || fail "$T-exit"
  diff -r "$WORK/o-$T" "$WORK/c-$T" >/dev/null 2>&1 && pass "$T-tree" || fail "$T-tree"
  diff "$WORK/$T-o.err" "$WORK/$T.err" >/dev/null 2>&1 && pass "$T-shape" || fail "$T-shape"
done

echo "== cell typ-multibyte (full-uint dispatch, oracle-compared) =="
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/mFA.aar" 1 545950324641 || die "craft-mFA"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/m44.aar" 1 545950324400 || die "craft-m44"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/m4F.aar" 1 5459503446000000 || die "craft-m4F"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/m1f.aar" 1 5459503166 || die "craft-m1f"
for T in mFA m44 m4F m1f; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$T.aar" "$WORK/o-$T" >/dev/null 2>&1 || ORC=$?
  CRC=0; "$AAD" "$WORK/$T.aar" "$WORK/c-$T" 2>/dev/null || CRC=$?
  [ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] && pass "$T-exit" || fail "$T-exit"
  diff -r "$WORK/o-$T" "$WORK/c-$T" >/dev/null 2>&1 && pass "$T-tree" || fail "$T-tree"
done
[ ! -e "$WORK/c-mFA/hello/greet.txt" ] && pass "mFA-skip" || fail "mFA-skip"
[ -d "$WORK/c-m44/hello/greet.txt" ] && [ -d "$WORK/o-m44/hello/greet.txt" ] && pass "m44-dir" || fail "m44-dir"
[ -f "$WORK/c-m4F/hello/greet.txt" ] && [ -f "$WORK/o-m4F/hello/greet.txt" ] && pass "m4F-file" || fail "m4F-file"
[ ! -e "$WORK/c-m1f/hello/greet.txt" ] && pass "m1f-skip" || fail "m1f-skip"

[ "$FAIL" -eq 0 ] && echo CBATTERY-GREEN || echo CBATTERY-RED
exit "$FAIL"
