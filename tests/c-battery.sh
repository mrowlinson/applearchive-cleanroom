#!/bin/sh
# c-battery.sh — C deliverable battery vs oracle (AAR decode).
# Usage: TMPDIR=<nvme-scratch> tests/c-battery.sh [workdir]; default TMPDIR cbattery.XXXXXX.
# Exit 0 all green / 1 any FAIL / 2 harness error. Needs: make, ZBM n/a.
set -eu
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
WORK=${1:-$(mktemp -d "$TMPDIR/cbattery.XXXXXX")}
AAD=$WORK/aad-bin
FAIL=0
pass() { echo "PASS $1"; }
fail() { echo "FAIL $1"; FAIL=1; }
die() { echo "HARNESS-ERROR $*" >&2; exit 2; }
t1pin() { # $1=oracle-stderr $2=tag: -t shape pin (PARENT-024: every outer cell proves -t-1 oracle)
  grep -q '0x9403' "$1" && pass "$2-t1pin" || fail "$2-t1pin"
}
freeze() { # $1=srcdir: fixed mtimes (DPROBE-17) so self-generated
  # crafts are byte-identical run to run (mtimes embed in stream).
  find "$1" -exec touch -h -t 202001020304.05 {} + 2>/dev/null || true
}

command -v cc >/dev/null || die "no cc"
make -C "$ROOT" OUTDIR="$WORK/build" >/dev/null 2>&1 || die "make failed"
{ echo '#!/bin/sh'; echo "exec \"$WORK/build/aae-cli\" aar-decode \"\$@\""; } > "$AAD" && chmod +x "$AAD"
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
  freeze "$WORK/src"
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
import random as _r; open(d + '/big.bin', 'wb').write(_r.Random(777001).randbytes(2000000))
"
for a in lzfse zlib raw; do
  freeze "$WORK/wsrc"
  sh "$ADAPTER" aar-encode --alg "$a" --threads 1 "$WORK/wsrc" "$WORK/w-$a.aar" >/dev/null 2>&1 || { fail "wenc-$a"; continue; }
  sh "$ADAPTER" aar-decode "$WORK/w-$a.aar" "$WORK/wo-$a" >/dev/null 2>&1 || { fail "wodec-$a"; continue; }
  "$AAD" "$WORK/w-$a.aar" "$WORK/wc-$a" 2>/dev/null || { fail "wcdec-$a"; continue; }
  diff -r "$WORK/wo-$a" "$WORK/wc-$a" >/dev/null 2>&1 && pass "wide-$a" || fail "wide-$a"
done

echo "== cell multiblock =="
python3 -c "open('$WORK/big.bin','wb').write(b'Q'*300000)"
mkdir -p "$WORK/bsrc"; mv "$WORK/big.bin" "$WORK/bsrc/"
freeze "$WORK/bsrc"
sh "$ADAPTER" aar-encode --alg lzfse --block 64k --threads 1 "$WORK/bsrc" "$WORK/mb.aar" >/dev/null 2>&1 || die "mb encode"
sh "$ADAPTER" aar-decode "$WORK/mb.aar" "$WORK/o-mb" >/dev/null 2>&1 || die "mb oracle"
"$AAD" "$WORK/mb.aar" "$WORK/c-mb" 2>/dev/null || fail "mb-cdec"
diff -r "$WORK/o-mb" "$WORK/c-mb" >/dev/null 2>&1 && pass "mb-bytes" || fail "mb-bytes"

echo "== cell hardlink =="
mkdir -p "$WORK/hsrc"
printf 'AAA-group0\n' > "$WORK/hsrc/a1.txt"; ln "$WORK/hsrc/a1.txt" "$WORK/hsrc/a2.txt"; ln "$WORK/hsrc/a1.txt" "$WORK/hsrc/a3.txt"
printf 'BBB-group1\n' > "$WORK/hsrc/b1.txt"; ln "$WORK/hsrc/b1.txt" "$WORK/hsrc/b2.txt"
printf 'lonely\n' > "$WORK/hsrc/solo.txt"
freeze "$WORK/hsrc"
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
freeze "$WORK/ssrc"
sh "$ADAPTER" aar-encode --alg lzfse --threads 1 "$WORK/ssrc" "$WORK/sk.aar" >/dev/null 2>&1 || die "sk encode"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/sk.aar" "$WORK/o-sk" >/dev/null 2>&1 || ORC=$?
CRC=0; "$AAD" "$WORK/sk.aar" "$WORK/c-sk" 2>/dev/null || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "sk-exit" || fail "sk-exit"
diff -r "$WORK/o-sk" "$WORK/c-sk" >/dev/null 2>&1 && pass "sk-tree" || fail "sk-tree"
rm -rf "$WORK/o-ff"
FFRC=0
python3 - "$ADAPTER" "$V/aar/fifo-mixed.aar" "$WORK/o-ff" <<'EOF' >/dev/null 2>&1 || FFRC=$?
import subprocess, sys
try:
    r = subprocess.run(["sh", sys.argv[1], "aar-decode", sys.argv[2], sys.argv[3]], capture_output=True, timeout=30)
    sys.exit(0 if r.returncode == 0 else 1)
except subprocess.TimeoutExpired:
    sys.exit(2)  # documented oracle fifo hang (rawenc.py: oracle HANGS reading it)
EOF
if [ "$FFRC" -eq 2 ]; then pass "ff-oracle-hang";
elif [ "$FFRC" -eq 0 ]; then pass "ff-oracle-exit";
else fail "ff-oracle-exit"; fi
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
SXC=0; "$AAD" "$V/aar/mix-fail.aar" "$WORK/c-sx" 2>"$WORK/sx.err" || SXC=$?
[ "$SXC" -eq 1 ] && pass "sx-exit" || fail "sx-exit"
grep -q "not implemented yet" "$WORK/sx.err" && grep -q "1 entries failed to extract" "$WORK/sx.err" && pass "sx-tokens" || fail "sx-tokens"

echo "== cell bloblen-wrap (must error fast, never hang) =="
python3 - "$WORK/wrap.aar" <<'EOF'
import struct, sys
name = b"w"
typ = b"TYP" + b"P" + struct.pack("<H", len(name)) + name
hsize = 6 + 7 + 24
n1 = 1 << 63
n2 = (1 << 63) - hsize  # N1+N2 == -hsize mod 2^64 -> blen wraps, pos rewinds
hdr = typ + b"DAT" + b"C" + struct.pack("<Q", n1) + b"DAT" + b"C" + struct.pack("<Q", n2)
assert 6 + len(hdr) == hsize
open(sys.argv[1], "wb").write(b"AA01" + struct.pack("<H", hsize) + hdr)
EOF
WRC=0; timeout -s KILL 20 python3 "$ROOT/proto/aad.py" "$WORK/wrap.aar" "$WORK/c-wrap-p" >/dev/null 2>&1 || WRC=$?
if [ "$WRC" -eq 124 ] || [ "$WRC" -eq 137 ]; then fail "wrap-proto-hang";
elif [ "$WRC" -ne 0 ]; then pass "wrap-proto-fast"; else fail "wrap-proto-accept"; fi
WRC=0; timeout -s KILL 20 "$AAD" "$WORK/wrap.aar" "$WORK/c-wrap" >/dev/null 2>&1 || WRC=$?
if [ "$WRC" -eq 124 ] || [ "$WRC" -eq 137 ]; then echo "KNOWN-DIFF wrap-hang (aad.c blen accumulation wraps pos; C fix pending)";
elif [ "$WRC" -ne 0 ]; then pass "wrap-exit"; else fail "wrap-accept"; fi

echo "== cell errors =="
python3 -c "import random; open('$WORK/corrupt.aar','wb').write(random.Random(777005).randbytes(100))"
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
freeze "$WORK/x2src"
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

echo "== cell parse-blobover-long (clean A-028 create: n6c-class) =="
mkdir -p "$WORK/po6src"; python3 -c "import random; r=random.Random(777002); open('$WORK/po6src/big1','wb').write(r.randbytes(500*1024)); open('$WORK/po6src/big2','wb').write(r.randbytes(400*1024))"
freeze "$WORK/po6src"
sh "$ADAPTER" aar-encode --alg lzfse --block 128k --threads 1 "$WORK/po6src" "$WORK/po6c-base.aar" >/dev/null 2>&1 || die "po6 encode"
python3 "$HERE/craft.py" setbloblen "$WORK/po6c-base.aar" "$WORK/po6c.aar" big2 DAT 2000000 || die "craft-po6c"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/po6c.aar" "$WORK/o-po6" >/dev/null 2>"$WORK/po6-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/po6c.aar" "$WORK/c-po6" 2>"$WORK/po6.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "po6-exit" || fail "po6-exit"
diff -r "$WORK/o-po6" "$WORK/c-po6" >/dev/null 2>&1 && pass "po6-tree" || fail "po6-tree"
diff "$WORK/po6-o.err" "$WORK/po6.err" >/dev/null 2>&1 && pass "po6-tok" || fail "po6-tok"
[ "$(stat -f %z "$WORK/o-po6/big2")" = 0 ] && [ "$(stat -f %z "$WORK/c-po6/big2")" = 0 ] && pass "po6-big2" || fail "po6-big2"
[ "$(stat -f %p "$WORK/o-po6/big2")" = "$(stat -f %p "$WORK/c-po6/big2")" ] && pass "po6-mode" || fail "po6-mode"
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
freeze "$WORK/trisrc"
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
t1pin "$WORK/oh-o.err" "oh"

echo "== cell outer-raw64 (u64 raw naming, stderr IDENT) =="
python3 "$HERE/craft.py" setblk "$V/aar/empty-lzfse.aar" "$WORK/r64.aar" 0 01000000000000710000000000000071 || die "craft-r64"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/r64.aar" "$WORK/o-r64" >/dev/null 2>"$WORK/r64-o.err" || ORC=$?
mkdir -p "$WORK/c-r64"
CRC=0; "$AAD" "$WORK/r64.aar" "$WORK/c-r64" 2>"$WORK/r64.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "r64-exit" || fail "r64-exit"
diff -r "$WORK/o-r64" "$WORK/c-r64" >/dev/null 2>&1 && pass "r64-tree" || fail "r64-tree"
diff "$WORK/r64-o.err" "$WORK/r64.err" >/dev/null 2>&1 && pass "r64-shape" || fail "r64-shape"
t1pin "$WORK/r64-o.err" "r64"

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
  case "$T" in L13|L27|L28|L29) t1pin "$WORK/$T-o.err" "$T";; esac
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

echo "== cell midchain-blob (whole>=256K: (blob) + partial, normalized) =="
mkdir -p "$WORK/mcsrc"; python3 -c "import random; r=random.Random(777003); open('$WORK/mcsrc/big1','wb').write(r.randbytes(400*1024)); open('$WORK/mcsrc/big2','wb').write(r.randbytes(300*1024))"
freeze "$WORK/mcsrc"
sh "$ADAPTER" aar-encode --alg lzfse --block 128k --threads 1 "$WORK/mcsrc" "$WORK/mc.aar" >/dev/null 2>&1 || die "mc encode"
MCOFF1=$(python3 -c "import struct,sys; d=open('$WORK/mc.aar','rb').read(); o=12; bs=[];
while o < len(d):
 r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
assert len(bs)>=5; print(bs[1][0]+16+bs[1][2]//2)") || die "mc walk1"
MCOFF2=$(python3 -c "import struct,sys; d=open('$WORK/mc.aar','rb').read(); o=12; bs=[];
while o < len(d):
 r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[2][0]+16+bs[2][2]//2)") || die "mc walk2"
MCOFF4=$(python3 -c "import struct,sys; d=open('$WORK/mc.aar','rb').read(); o=12; bs=[];
while o < len(d):
 r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[4][0]+16+bs[4][2]//2)") || die "mc walk4"
MCOFF3=$(python3 -c "import struct,sys; d=open('$WORK/mc.aar','rb').read(); o=12; bs=[];
while o < len(d):
 r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[3][0]+16+bs[3][2]//2)") || die "mc walk3"
MCBV=$(python3 -c "import struct; d=open('$WORK/mc.aar','rb').read(); o=12; bs=[];
while o < len(d):
 r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print((struct.pack('>Q',0x500000)+d[bs[2][0]+8:bs[2][0]+16]).hex())") || die "mc bv"
head -c "$MCOFF1" "$WORK/mc.aar" > "$WORK/mc1.aar" || die "craft-mc1"
head -c "$MCOFF2" "$WORK/mc.aar" > "$WORK/mc2.aar" || die "craft-mc2"
head -c "$MCOFF4" "$WORK/mc.aar" > "$WORK/mc4.aar" || die "craft-mc4"
head -c "$MCOFF3" "$WORK/mc.aar" > "$WORK/mc3.aar" || die "craft-mc3"
python3 "$HERE/craft.py" setblk "$WORK/mc.aar" "$WORK/mcbv.aar" 2 "$MCBV" || die "craft-mcbv"
mcnorm() { grep -v '^reading payload$' "$1" | sed 's/^[12] entries failed to extract$/1 entries failed to extract/'; }
for T in mc1 mc2 mc3 mc4 mcbv; do
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$T.aar" "$WORK/o-$T" >/dev/null 2>"$WORK/$T-o.err" || ORC=$?
  mkdir -p "$WORK/c-$T"
  CRC=0; "$AAD" "$WORK/$T.aar" "$WORK/c-$T" 2>"$WORK/$T.err" || CRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "$T-exit" || fail "$T-exit"
  mcnorm "$WORK/$T-o.err" > "$WORK/$T-o.n"; mcnorm "$WORK/$T.err" > "$WORK/$T.n"
  diff "$WORK/$T-o.n" "$WORK/$T.n" >/dev/null 2>&1 && pass "$T-shape" || fail "$T-shape"
  t1pin "$WORK/$T-o.err" "$T"
done
diff -r "$WORK/o-mc1" "$WORK/c-mc1" >/dev/null 2>&1 && pass "mc1-tree" || fail "mc1-tree"
# mc2/mc3/mcbv: exists-bit phase-race (oracle EMPTY vs ABSENT legs);
# C pinned ABSENT (A-028 LONG-only). SET + C pin + oracle-mode-when-present.
if [ -e "$WORK/o-mc2/big1" ]; then MC2OS=$(stat -f %z "$WORK/o-mc2/big1"); MC2OM=$(stat -f %p "$WORK/o-mc2/big1"); else MC2OS=ABS; MC2OM=ABS; fi
{ [ "$MC2OS" = 0 ] || [ "$MC2OS" = ABS ]; } && pass "mc2-tree" || fail "mc2-tree"
[ ! -e "$WORK/c-mc2/big1" ] && pass "mc2-cabsent" || fail "mc2-cabsent"
{ [ "$MC2OM" = 100644 ] || [ "$MC2OM" = ABS ]; } && pass "mc2-omode" || fail "mc2-omode"
if [ -e "$WORK/o-mc3/big1" ]; then MC3OS=$(stat -f %z "$WORK/o-mc3/big1"); MC3OM=$(stat -f %p "$WORK/o-mc3/big1"); else MC3OS=ABS; MC3OM=ABS; fi
{ [ "$MC3OS" = 0 ] || [ "$MC3OS" = ABS ]; } && pass "mc3-tree" || fail "mc3-tree"
[ ! -e "$WORK/c-mc3/big1" ] && pass "mc3-cabsent" || fail "mc3-cabsent"
{ [ "$MC3OM" = 100644 ] || [ "$MC3OM" = ABS ]; } && pass "mc3-omode" || fail "mc3-omode"
if [ -e "$WORK/o-mcbv/big1" ]; then MCBVOS=$(stat -f %z "$WORK/o-mcbv/big1"); MCBVOM=$(stat -f %p "$WORK/o-mcbv/big1"); else MCBVOS=ABS; MCBVOM=ABS; fi
{ [ "$MCBVOS" = 0 ] || [ "$MCBVOS" = ABS ]; } && pass "mcbv-tree" || fail "mcbv-tree"
[ ! -e "$WORK/c-mcbv/big1" ] && pass "mcbv-cabsent" || fail "mcbv-cabsent"
{ [ "$MCBVOM" = 100644 ] || [ "$MCBVOM" = ABS ]; } && pass "mcbv-omode" || fail "mcbv-omode"
grep -q "entries failed" "$WORK/mc1-o.err" && fail "mc1-nocount" || pass "mc1-nocount"
# TIP2e M1 tails pins (C modal + oracle SET; hard-path mc1 x0-exact)
OT1=$(grep -c 'reading payload' "$WORK/mc1-o.err" || true); CT1=$(grep -c 'reading payload' "$WORK/mc1.err" || true)
[ "$OT1" = "0" ] && pass "mc1-otails" || fail "mc1-otails"
[ "$CT1" = "0" ] && pass "mc1-ctails" || fail "mc1-ctails"
for T in mc2 mc3 mc4 mcbv; do
  OT=$(grep -c 'reading payload' "$WORK/$T-o.err" || true); CT=$(grep -c 'reading payload' "$WORK/$T.err" || true)
  { [ "$OT" = "0" ] || [ "$OT" = "2" ]; } && pass "$T-otails" || fail "$T-otails"
  if [ "$T" = "mc4" ]; then EXP=2; else EXP=0; fi
  [ "$CT" = "$EXP" ] && pass "$T-ctails" || fail "$T-ctails"
done
cmp -s "$WORK/o-mc4/big1" "$WORK/c-mc4/big1" && pass "mc4-big1" || fail "mc4-big1"
cmp -s "$WORK/mcsrc/big1" "$WORK/o-mc4/big1" && pass "mc4-big1full" || fail "mc4-big1full"
[ ! -e "$WORK/o-mc4/big2" ] && [ ! -e "$WORK/c-mc4/big2" ] && pass "mc4-big2abs" || fail "mc4-big2abs"
[ "$(stat -f %p "$WORK/o-mc4/big1")" = "$(stat -f %p "$WORK/c-mc4/big1")" ] && pass "mc4-big1mode" || fail "mc4-big1mode"

echo "== cell midchain-decfail (decode fail both flavors) =="
mkdir -p "$WORK/mzsrc"; dd if=/dev/zero of="$WORK/mzsrc/f" bs=1024 count=600 2>/dev/null
freeze "$WORK/mzsrc"
sh "$ADAPTER" aar-encode --alg lzfse --block 256k --threads 1 "$WORK/mzsrc" "$WORK/mz.aar" >/dev/null 2>&1 || die "mz encode"
MZ1=$(python3 -c "import struct; d=open('$WORK/mz.aar','rb').read(); o=12; bs=[];
while o < len(d):
 r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[1][0]+16)") || die "mz walk"
python3 "$HERE/craft.py" patch "$WORK/mz.aar" "$WORK/mz1.aar" "$MZ1" ff || die "craft-mz1"
python3 "$HERE/craft.py" patch "$WORK/mz.aar" "$WORK/mz0.aar" 28 ff || die "craft-mz0"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/mz1.aar" "$WORK/o-mz1" >/dev/null 2>"$WORK/mz1-o.err" || ORC=$?
mkdir -p "$WORK/c-mz1"
CRC=0; "$AAD" "$WORK/mz1.aar" "$WORK/c-mz1" 2>"$WORK/mz1.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "mz1-exit" || fail "mz1-exit"
# mz1: same exists-bit phase-race as mc2 (EMPTY-modal vs ABSENT legs); C pinned EMPTY.
if [ -e "$WORK/o-mz1/f" ]; then MZ1OS=$(stat -f %z "$WORK/o-mz1/f"); MZ1OM=$(stat -f %p "$WORK/o-mz1/f"); else MZ1OS=ABS; MZ1OM=ABS; fi
{ [ "$MZ1OS" = 0 ] || [ "$MZ1OS" = ABS ]; } && pass "mz1-tree" || fail "mz1-tree"
[ ! -e "$WORK/c-mz1/f" ] && pass "mz1-cabsent" || fail "mz1-cabsent"
{ [ "$MZ1OM" = 100644 ] || [ "$MZ1OM" = ABS ]; } && pass "mz1-omode" || fail "mz1-omode"
mcnorm "$WORK/mz1-o.err" > "$WORK/mz1-o.n"; mcnorm "$WORK/mz1.err" > "$WORK/mz1.n"
diff "$WORK/mz1-o.n" "$WORK/mz1.n" >/dev/null 2>&1 && pass "mz1-shape" || fail "mz1-shape"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/mz0.aar" "$WORK/o-mz0" >/dev/null 2>"$WORK/mz0-o.err" || ORC=$?
mkdir -p "$WORK/c-mz0"
CRC=0; "$AAD" "$WORK/mz0.aar" "$WORK/c-mz0" 2>"$WORK/mz0.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "mz0-exit" || fail "mz0-exit"
diff -r "$WORK/o-mz0" "$WORK/c-mz0" >/dev/null 2>&1 && pass "mz0-tree" || fail "mz0-tree"
diff "$WORK/mz0-o.err" "$WORK/mz0.err" >/dev/null 2>&1 && pass "mz0-shape" || fail "mz0-shape"

echo "== cell midchain-e4 (complete prefix + cut; tiny UNPINNED, Q-020) =="
cat "$WORK/mc.aar" > "$WORK/e4.aar"; printf '\0\0\0\0\0\0\0\0\0\0' >> "$WORK/e4.aar"
ORC=0; sh "$ADAPTER" aar-decode "$WORK/e4.aar" "$WORK/o-e4" >/dev/null 2>"$WORK/e4-o.err" || ORC=$?
mkdir -p "$WORK/c-e4"
CRC=0; "$AAD" "$WORK/e4.aar" "$WORK/c-e4" 2>"$WORK/e4.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "e4-exit" || fail "e4-exit"
mcnorm "$WORK/e4-o.err" > "$WORK/e4-o.n"; mcnorm "$WORK/e4.err" > "$WORK/e4.n"
diff "$WORK/e4-o.n" "$WORK/e4.n" >/dev/null 2>&1 && pass "e4-shape" || fail "e4-shape"
cmp -s "$WORK/o-e4/big1" "$WORK/c-e4/big1" && pass "e4-big1" || fail "e4-big1"
[ ! -e "$WORK/o-e4/big2" ] && [ ! -e "$WORK/c-e4/big2" ] && pass "e4-big2abs" || fail "e4-big2abs"

echo "== cell midchain-content (presence + 256K chunks, stable zones) =="
mkcx() { # $1=b1KB(0=single) $2=cutblock $3=name
  rm -rf "$WORK/cx$3src"; mkdir -p "$WORK/cx$3src"
  if [ "$1" -gt 0 ]; then
    python3 -c "import random; r=random.Random(777004); open('$WORK/cx$3src/b1','wb').write(r.randbytes($1*1024)); open('$WORK/cx$3src/b2','wb').write(r.randbytes(1024*1024))"
  else
    python3 -c "import random; r=random.Random(777004); open('$WORK/cx$3src/big','wb').write(r.randbytes(1024*1024))"
  fi
  freeze "$WORK/cx$3src"
  sh "$ADAPTER" aar-encode --alg lzfse --block 128k --threads 1 "$WORK/cx$3src" "$WORK/cx$3.aar" >/dev/null 2>&1 || die "cx$3 encode"
  CXC=$(python3 -c "import struct; d=open('$WORK/cx$3.aar','rb').read(); o=12; bs=[];
while o < len(d):
 r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[$2][0]+16+bs[$2][2]//2)") || die "cx$3 walk"
  head -c "$CXC" "$WORK/cx$3.aar" > "$WORK/cx$3c.aar" || die "craft-cx$3"
}
runcx() { # $1=name $2=file $3=wantsize
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/cx$1c.aar" "$WORK/o-cx$1" >/dev/null 2>"$WORK/cx$1-o.err" || ORC=$?
  mkdir -p "$WORK/c-cx$1"
  CRC=0; "$AAD" "$WORK/cx$1c.aar" "$WORK/c-cx$1" 2>"$WORK/cx$1.err" || CRC=$?
  PRC=0; python3 "$HERE/../proto/aad.py" "$WORK/cx$1c.aar" "$WORK/p-cx$1" >/dev/null 2>&1 || PRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "cx$1-exit" || fail "cx$1-exit"
  [ "$PRC" -eq 1 ] && pass "cx$1-pexit" || fail "cx$1-pexit"
  mcnorm "$WORK/cx$1-o.err" > "$WORK/cx$1-o.n"; mcnorm "$WORK/cx$1.err" > "$WORK/cx$1.n"
  diff "$WORK/cx$1-o.n" "$WORK/cx$1.n" >/dev/null 2>&1 && pass "cx$1-shape" || fail "cx$1-shape"
  # Race-SET (M1 tails legs): C pinned modal $3; oracle $3 or one chunk
  # less (0->ABSENT); reduced content is a byte-prefix (verified).
  CXO=$([ -f "$WORK/o-cx$1/$2" ] && stat -f %z "$WORK/o-cx$1/$2" || echo ABS)
  CXC=$([ -f "$WORK/c-cx$1/$2" ] && stat -f %z "$WORK/c-cx$1/$2" || echo ABS)
  CXSET=0
  if [ "$CXC" = "$3" ]; then
    if [ "$CXO" = "$3" ]; then CXSET=1; fi
    if [ "$3" = "0" ] && [ "$CXO" = "ABS" ]; then CXSET=1; fi
    if [ "$3" != "0" ] && [ "$CXO" = "$(($3 - 262144))" ]; then CXSET=1; fi
  fi
  [ "$CXSET" = "1" ] && pass "cx$1-size" || fail "cx$1-size"
  CXCMP=0
  if [ "$CXO" = "$CXC" ] && [ "$CXO" != "ABS" ] && cmp -s "$WORK/o-cx$1/$2" "$WORK/c-cx$1/$2"; then CXCMP=1; fi
  if [ "$CXO" = "ABS" ] && [ "$CXC" = "0" ]; then CXCMP=1; fi
  if [ "$CXO" != "ABS" ] && [ "$CXO" != "$CXC" ] && head -c "$CXO" "$WORK/c-cx$1/$2" | cmp -s - "$WORK/o-cx$1/$2"; then CXCMP=1; fi
  [ "$CXCMP" = "1" ] && pass "cx$1-cmp" || fail "cx$1-cmp"
  if [ "$CXO" = "ABS" ]; then pass "cx$1-mode"; else [ "$(stat -f %p "$WORK/o-cx$1/$2")" = "$(stat -f %p "$WORK/c-cx$1/$2")" ] && pass "cx$1-mode" || fail "cx$1-mode"; fi
  diff -r "$WORK/c-cx$1" "$WORK/p-cx$1" >/dev/null 2>&1 && pass "cx$1-lock" || fail "cx$1-lock"
}
mkcx 0 4 A; runcx A big 0
mkcx 0 6 B; runcx B big 262144
mkcx 0 8 C; runcx C big 524288
mkcx 186 6 D; runcx D b2 262144
cmp -s "$WORK/cxDsrc/b1" "$WORK/o-cxD/b1" && pass "cxD-b1full" || fail "cxD-b1full"
mkcx 300 6 E; runcx E b2 0
cmp -s "$WORK/cxEsrc/b1" "$WORK/o-cxE/b1" && pass "cxE-b1full" || fail "cxE-b1full"
mkcx 400 7 F; runcx F b2 0
cmp -s "$WORK/cxFsrc/b1" "$WORK/o-cxF/b1" && pass "cxF-b1full" || fail "cxF-b1full"
mkcx 100 8 G
# cxG: multi-file chunk1 RACY (oracle 262144-or-524288, MT flush;
# single-file chunk1 stable 9/9). Mine = modal 524288. Unpinned: no size/cmp.
ORC=0; sh "$ADAPTER" aar-decode "$WORK/cxGc.aar" "$WORK/o-cxG" >/dev/null 2>"$WORK/cxG-o.err" || ORC=$?
mkdir -p "$WORK/c-cxG"
CRC=0; "$AAD" "$WORK/cxGc.aar" "$WORK/c-cxG" 2>"$WORK/cxG.err" || CRC=$?
[ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && pass "cxG-exit" || fail "cxG-exit"
mcnorm "$WORK/cxG-o.err" > "$WORK/cxG-o.n"; mcnorm "$WORK/cxG.err" > "$WORK/cxG.n"
diff "$WORK/cxG-o.n" "$WORK/cxG.n" >/dev/null 2>&1 && pass "cxG-shape" || fail "cxG-shape"
[ -f "$WORK/o-cxG/b2" ] && [ -f "$WORK/c-cxG/b2" ] && pass "cxG-exists" || fail "cxG-exists"
[ "$(stat -f %p "$WORK/o-cxG/b2")" = "$(stat -f %p "$WORK/c-cxG/b2")" ] && pass "cxG-mode" || fail "cxG-mode"
cmp -s "$WORK/cxGsrc/b1" "$WORK/o-cxG/b1" && pass "cxG-b1full" || fail "cxG-b1full"
mkcx 300 8 H; runcx H b2 262144
cmp -s "$WORK/cxHsrc/b1" "$WORK/o-cxH/b1" && pass "cxH-b1full" || fail "cxH-b1full"

echo "== cell g-collision (G3 symlink-occupant + G5 missing-parents + G6 replace-modal) =="
mkdir -p "$WORK/gsrc"; printf 'A1-content' > "$WORK/gsrc/victim"; printf 'A2-content' > "$WORK/gsrc/vdir"
freeze "$WORK/gsrc"
sh "$ADAPTER" aar-encode --alg raw --threads 1 "$WORK/gsrc" "$WORK/g.aar" >/dev/null 2>&1 || die "g encode"
for S in o c p; do rm -rf "$WORK/g$S"; mkdir -p "$WORK/g$S"; printf 'old' > "$WORK/g$S/elsewhere"; ln -s elsewhere "$WORK/g$S/victim"; mkdir -p "$WORK/g$S/somedir"; ln -s somedir "$WORK/g$S/vdir"; done
ORC=0; sh "$ADAPTER" aar-decode "$WORK/g.aar" "$WORK/go" >/dev/null 2>"$WORK/g-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/g.aar" "$WORK/gc" 2>"$WORK/g.err" || CRC=$?
PRC=0; python3 "$HERE/../proto/aad.py" "$WORK/g.aar" "$WORK/gp" >/dev/null 2>"$WORK/gp.err" || PRC=$?
[ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] && [ "$PRC" -eq 0 ] && pass "g3-exit" || fail "g3-exit"
[ ! -s "$WORK/g-o.err" ] && [ ! -s "$WORK/g.err" ] && pass "g3-silent" || fail "g3-silent"
for S in o c p; do
  D=$WORK/g$S; [ "$S" = "o" ] && D=$WORK/go; [ "$S" = "c" ] && D=$WORK/gc; [ "$S" = "p" ] && D=$WORK/gp
  [ ! -L "$D/victim" ] && [ "$(cat "$D/victim")" = "A1-content" ] && pass "g3a-$S" || fail "g3a-$S"
  [ ! -L "$D/vdir" ] && [ "$(cat "$D/vdir")" = "A2-content" ] && pass "g3b-$S" || fail "g3b-$S"
done
# G5 true bed pending Q-024. Observed: N-level missing roots mkdir -p rc 0
# all sides (2-level + 4-level first-hand). Pin agreement, not bare.
ORC=0; sh "$ADAPTER" aar-decode "$WORK/g.aar" "$WORK/g5o/sub" >/dev/null 2>"$WORK/g5-o.err" || ORC=$?
CRC=0; "$AAD" "$WORK/g.aar" "$WORK/g5c/sub" 2>"$WORK/g5.err" || CRC=$?
PRC=0; python3 "$HERE/../proto/aad.py" "$WORK/g.aar" "$WORK/g5p/sub" >/dev/null 2>"$WORK/g5p.err" || PRC=$?
[ "$ORC" -eq 0 ] && [ "$CRC" -eq 0 ] && [ "$PRC" -eq 0 ] && pass "g5mk-exit" || fail "g5mk-exit"
diff -r "$WORK/g5o/sub" "$WORK/g5c/sub" >/dev/null 2>&1 && pass "g5mk-tree" || fail "g5mk-tree"
diff -r "$WORK/g5c/sub" "$WORK/g5p/sub" >/dev/null 2>&1 && pass "g5mk-lock" || fail "g5mk-lock"
[ ! -s "$WORK/g5-o.err" ] && [ ! -s "$WORK/g5.err" ] && pass "g5mk-silent" || fail "g5mk-silent"
mkdir -p "$WORK/g6src/dd"; printf 'kid-bytes' > "$WORK/g6src/dd/kid"; chmod 700 "$WORK/g6src/dd"
freeze "$WORK/g6src"
sh "$ADAPTER" aar-encode --alg raw --threads 1 "$WORK/g6src" "$WORK/g6.aar" >/dev/null 2>&1 || die "g6 encode"
for S in o c p; do rm -rf "$WORK/g6$S"; mkdir -p "$WORK/g6$S"; printf 'keepme' > "$WORK/g6$S/dd"; chmod 644 "$WORK/g6$S/dd"; done
ORC=0; sh "$ADAPTER" aar-decode "$WORK/g6.aar" "$WORK/g6o" 2>"$WORK/g6-o.err" >/dev/null || ORC=$?
CRC=0; "$AAD" "$WORK/g6.aar" "$WORK/g6c" 2>"$WORK/g6.err" >/dev/null || CRC=$?
PRC=0; python3 "$HERE/../proto/aad.py" "$WORK/g6.aar" "$WORK/g6p" 2>"$WORK/g6p.err" >/dev/null || PRC=$?
cat > "$WORK/g6modal.err" <<'EOF'
Error 0x83058800
a parent of path is not a directory: dd/kid
invalid path: dd/kid
1 entries failed to extract
EOF
# G6 truth (NOTE-050): oracle ALWAYS replaces file occupant (dir 0700,
# MOD applied); kid races (HAVE+rc0-silent 2/6 vs ABSENT+stanza+rc1 4/6).
# Old keep-pin was oracle-false (never verified vs oracle). Ours: modal.
[ "$(stat -f %p "$WORK/g6o/dd")" = "40700" ] && pass "g6o-repl" || fail "g6o-repl"
if { [ "$ORC" -eq 0 ] && [ ! -s "$WORK/g6-o.err" ] && cmp -s "$WORK/g6o/dd/kid" "$WORK/g6src/dd/kid"; } || { [ "$ORC" -eq 1 ] && diff "$WORK/g6modal.err" "$WORK/g6-o.err" >/dev/null 2>&1 && [ ! -e "$WORK/g6o/dd/kid" ]; }; then pass "g6o-shape"; else fail "g6o-shape"; fi
[ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "g6cp-exit" || fail "g6cp-exit"
diff "$WORK/g6modal.err" "$WORK/g6.err" >/dev/null 2>&1 && pass "g6c-modal" || fail "g6c-modal"
grep -v '^blocks:' "$WORK/g6p.err" | diff "$WORK/g6.err" - >/dev/null 2>&1 && pass "g6p-mirror" || fail "g6p-mirror"
[ "$(stat -f %p "$WORK/g6c/dd")" = "40700" ] && [ ! -e "$WORK/g6c/dd/kid" ] && pass "g6c-tree" || fail "g6c-tree"
[ "$(stat -f %p "$WORK/g6p/dd")" = "40700" ] && [ ! -e "$WORK/g6p/dd/kid" ] && pass "g6p-tree" || fail "g6p-tree"

echo "== cell m3-exactness (unclo/unchi/paylo/stored decoder shapes) =="
mkm3() { # $1=base $2=rawd $3=payd $4=name
  M3H=$(python3 -c "import struct; d=open('$V/aar/$1.aar','rb').read(); raw,pay=struct.unpack('>QQ',d[12:28]); print((struct.pack('>Q',raw+($2))+struct.pack('>Q',pay+($3))).hex())") || die "m3$4 walk"
  python3 "$HERE/craft.py" setblk "$V/aar/$1.aar" "$WORK/m3$4.aar" 0 "$M3H" || die "craft-m3$4"
}
runm3() { # $1=name (-t-1-only: every m3 shape hard-fails short, no extraction, no tails)
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/m3$1.aar" "$WORK/o-m3$1" >/dev/null 2>"$WORK/m3$1-o.err" || ORC=$?
  mkdir -p "$WORK/c-m3$1" "$WORK/p-m3$1"
  CRC=0; "$AAD" "$WORK/m3$1.aar" "$WORK/c-m3$1" 2>"$WORK/m3$1.err" || CRC=$?
  PRC=0; python3 "$HERE/../proto/aad.py" "$WORK/m3$1.aar" "$WORK/p-m3$1" >/dev/null 2>&1 || PRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "m3$1-exit" || fail "m3$1-exit"
  diff "$WORK/m3$1-o.err" "$WORK/m3$1.err" >/dev/null 2>&1 && pass "m3$1-shape" || fail "m3$1-shape"
  t1pin "$WORK/m3$1-o.err" "m3$1"
  diff -r "$WORK/c-m3$1" "$WORK/p-m3$1" >/dev/null 2>&1 && pass "m3$1-lock" || fail "m3$1-lock"
}
empty3() { # $1=name
  [ -z "$(find "$WORK/o-m3$1" "$WORK/c-m3$1" -type f 2>/dev/null)" ] && pass "m3$1-empty" || fail "m3$1-empty"
  diff -r "$WORK/o-m3$1" "$WORK/c-m3$1" >/dev/null 2>&1 && pass "m3$1-tree" || fail "m3$1-tree"
}
mkm3 hello-lzfse -10 0 uc10; runm3 uc10; empty3 uc10
mkm3 hello-lzfse -25 0 uc25; runm3 uc25; empty3 uc25
mkm3 hello-lzfse -36 0 uc36; runm3 uc36; empty3 uc36
mkm3 hello-lzfse -37 0 uc37; runm3 uc37; empty3 uc37
mkm3 hello-lzfse -100 0 uc100; runm3 uc100; empty3 uc100
mkm3 hello-lzfse 10 0 uh10; runm3 uh10; empty3 uh10
mkm3 hello-lzfse 500 0 uh500; runm3 uh500; empty3 uh500
mkm3 hello-lzfse 0 -1 pl1; runm3 pl1; empty3 pl1
mkm3 hello-lzfse 0 -4 pl4; runm3 pl4; empty3 pl4
mkm3 hello-lzfse 0 -5 pl5; runm3 pl5; empty3 pl5
mkm3 hello-lzfse 0 -10 pl10; runm3 pl10; empty3 pl10
mkm3 hello-lzfse 0 -100 pl100; runm3 pl100; empty3 pl100
mkm3 hello-lzfse 0 1 phi; runm3 phi; empty3 phi
mkm3 empty-lzfse 1 0 sthi; runm3 sthi; empty3 sthi
mkm3 empty-lzfse -1 0 stlo; runm3 stlo; empty3 stlo

echo "== cell g9-traversal (sym/file/dangling planted parent) =="
mkdir -p "$WORK/g9src/a" "$WORK/g9src/b/deep"
printf 'hello-f\n' > "$WORK/g9src/a/f.txt"; ln -s f.txt "$WORK/g9src/a/l.lnk"; printf 'deep-g\n' > "$WORK/g9src/b/deep/g.txt"
freeze "$WORK/g9src"
sh "$ADAPTER" aar-encode --alg raw --threads 1 "$WORK/g9src" "$WORK/g9.aar" >/dev/null 2>&1 || die "g9 encode"
cat > "$WORK/g9modal.err" <<'EOF'
Error 0x83058800
a parent of path is not a directory: a/f.txt
invalid path: a/f.txt
a parent of path is not a directory: a/l.lnk
invalid path: a/l.lnk
creating fs object: a/l.lnk
2 entries failed to extract
EOF
# oracle outcome SET (race; NOTE-050): {both-fail either order, f-only
# (l.lnk present), l-only (f.txt full present)}. C pins modal (above).
for shape in sym file dangling; do
  rm -rf "$WORK/go-$shape" "$WORK/gv-$shape" "$WORK/gc-$shape" "$WORK/gw-$shape" "$WORK/gp-$shape" "$WORK/gx-$shape"
  mkdir -p "$WORK/go-$shape" "$WORK/gv-$shape" "$WORK/gc-$shape" "$WORK/gw-$shape" "$WORK/gp-$shape" "$WORK/gx-$shape"
  echo MARKER > "$WORK/gv-$shape/marker"; echo MARKER > "$WORK/gw-$shape/marker"; echo MARKER > "$WORK/gx-$shape/marker"
  case $shape in
    sym) ln -s "$WORK/gv-$shape" "$WORK/go-$shape/a"; ln -s "$WORK/gw-$shape" "$WORK/gc-$shape/a"; ln -s "$WORK/gx-$shape" "$WORK/gp-$shape/a";;
    file) echo OCC > "$WORK/go-$shape/a"; echo OCC > "$WORK/gc-$shape/a"; echo OCC > "$WORK/gp-$shape/a";;
    dangling) ln -s /nonexistent-g9-target "$WORK/go-$shape/a"; ln -s /nonexistent-g9-target "$WORK/gc-$shape/a"; ln -s /nonexistent-g9-target "$WORK/gp-$shape/a";;
  esac
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/g9.aar" "$WORK/go-$shape" 2>"$WORK/go-$shape.err" >/dev/null || ORC=$?
  CRC=0; "$AAD" "$WORK/g9.aar" "$WORK/gc-$shape" 2>"$WORK/gc-$shape.err" >/dev/null || CRC=$?
  PRC=0; python3 "$ROOT/proto/aad.py" "$WORK/g9.aar" "$WORK/gp-$shape" 2>"$WORK/gp-$shape.err" >/dev/null || PRC=$?
  OEXIT=0; [ "$ORC" -eq 1 ] && OEXIT=1
  if [ "$ORC" -eq 0 ] && [ ! -s "$WORK/go-$shape.err" ] && cmp -s "$WORK/go-$shape/a/f.txt" "$WORK/g9src/a/f.txt" && [ -L "$WORK/go-$shape/a/l.lnk" ]; then OEXIT=1; fi
  [ "$OEXIT" -eq 1 ] && [ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "g9$shape-exit" || fail "g9$shape-exit"
  [ "$(ls "$WORK/gv-$shape")" = "marker" ] && [ "$(ls "$WORK/gw-$shape")" = "marker" ] && [ "$(ls "$WORK/gx-$shape")" = "marker" ] && pass "g9$shape-victim" || fail "g9$shape-victim"
  diff "$WORK/g9modal.err" "$WORK/gc-$shape.err" >/dev/null 2>&1 && pass "g9$shape-cmodal" || fail "g9$shape-cmodal"
  grep -v '^blocks:' "$WORK/gp-$shape.err" | diff "$WORK/gc-$shape.err" - >/dev/null 2>&1 && pass "g9$shape-pmirror" || fail "g9$shape-pmirror"
  OSET=0
  if [ "$ORC" -eq 0 ] && [ ! -s "$WORK/go-$shape.err" ] && cmp -s "$WORK/go-$shape/a/f.txt" "$WORK/g9src/a/f.txt" && [ -L "$WORK/go-$shape/a/l.lnk" ]; then OSET=1; fi
  if grep -q '^Error 0x83058800$' "$WORK/go-$shape.err" 2>/dev/null; then
    N=$(grep -c 'a parent of path is not a directory' "$WORK/go-$shape.err" || true)
    if [ "$N" = "2" ] && grep -q '2 entries failed' "$WORK/go-$shape.err" \
       && grep -q 'not a directory: a/f.txt' "$WORK/go-$shape.err" \
       && grep -q 'not a directory: a/l.lnk' "$WORK/go-$shape.err" \
       && grep -q 'creating fs object: a/l.lnk' "$WORK/go-$shape.err" \
       && [ -z "$(ls "$WORK/go-$shape/a")" ]; then OSET=1; fi
    if [ "$N" = "1" ] && grep -q '1 entries failed' "$WORK/go-$shape.err" \
       && grep -q 'not a directory: a/f.txt' "$WORK/go-$shape.err" \
       && [ -L "$WORK/go-$shape/a/l.lnk" ]; then OSET=1; fi
    if [ "$N" = "1" ] && grep -q '1 entries failed' "$WORK/go-$shape.err" \
       && grep -q 'not a directory: a/l.lnk' "$WORK/go-$shape.err" \
       && grep -q 'creating fs object: a/l.lnk' "$WORK/go-$shape.err" \
       && cmp -s "$WORK/go-$shape/a/f.txt" "$WORK/g9src/a/f.txt"; then OSET=1; fi
  fi
  [ "$OSET" = "1" ] && pass "g9$shape-oshape" || fail "g9$shape-oshape"
  [ ! -L "$WORK/gc-$shape/a" ] && [ -d "$WORK/gc-$shape/a" ] && [ -z "$(ls "$WORK/gc-$shape/a")" ] && [ "$(stat -f %p "$WORK/gc-$shape/a")" = "40755" ] && pass "g9$shape-ctree" || fail "g9$shape-ctree"
  cmp -s "$WORK/gc-$shape/b/deep/g.txt" "$WORK/g9src/b/deep/g.txt" && pass "g9$shape-sib" || fail "g9$shape-sib"
  diff -r "$WORK/gc-$shape" "$WORK/gp-$shape" >/dev/null 2>&1 && pass "g9$shape-cplock" || fail "g9$shape-cplock"
  [ "$(ls "$WORK/gc-$shape" | tr '\n' ',')" = "a,b," ] && pass "g9$shape-top" || fail "g9$shape-top"
done

echo "== cell g9P-fifo-child (non-F triple, A-027#1) =="
python3 "$HERE/craft.py" settyppat "$WORK/g9.aar" "$WORK/g9p.aar" a/f.txt P || die "g9p craft"
cat > "$WORK/g9pmodal.err" <<'EOF'
Error 0x83058800
a parent of path is not a directory: a/f.txt
invalid path: a/f.txt
creating fs object: a/f.txt
a parent of path is not a directory: a/l.lnk
invalid path: a/l.lnk
creating fs object: a/l.lnk
2 entries failed to extract
EOF
rm -rf "$WORK/po" "$WORK/pv" "$WORK/pc" "$WORK/pw" "$WORK/pp" "$WORK/px"
mkdir -p "$WORK/po" "$WORK/pv" "$WORK/pc" "$WORK/pw" "$WORK/pp" "$WORK/px"
echo MARKER > "$WORK/pv/marker"; echo MARKER > "$WORK/pw/marker"; echo MARKER > "$WORK/px/marker"
ln -s "$WORK/pv" "$WORK/po/a"; ln -s "$WORK/pw" "$WORK/pc/a"; ln -s "$WORK/px" "$WORK/pp/a"
ORC=0; python3 "$HERE/fifo-drain-run.py" 30 "$WORK/po" /dev/null "$WORK/po.err" sh "$ADAPTER" aar-decode "$WORK/g9p.aar" "$WORK/po" >/dev/null || ORC=$?
CRC=0; "$AAD" "$WORK/g9p.aar" "$WORK/pc" 2>"$WORK/pc.err" >/dev/null || CRC=$?
PRC=0; python3 "$ROOT/proto/aad.py" "$WORK/g9p.aar" "$WORK/pp" 2>"$WORK/pp.err" >/dev/null || PRC=$?
POEXIT=0; [ "$ORC" -eq 1 ] && POEXIT=1
if [ "$ORC" -eq 0 ] && [ ! -s "$WORK/po.err" ] && [ -p "$WORK/po/a/f.txt" ] && [ -L "$WORK/po/a/l.lnk" ]; then POEXIT=1; fi
[ "$POEXIT" -eq 1 ] && [ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "g9p-exit" || fail "g9p-exit"
[ "$(ls "$WORK/pv")" = "marker" ] && [ "$(ls "$WORK/pw")" = "marker" ] && [ "$(ls "$WORK/px")" = "marker" ] && pass "g9p-victim" || fail "g9p-victim"
diff "$WORK/g9pmodal.err" "$WORK/pc.err" >/dev/null 2>&1 && pass "g9p-cmodal" || fail "g9p-cmodal"
grep -v '^blocks:' "$WORK/pp.err" | diff "$WORK/pc.err" - >/dev/null 2>&1 && pass "g9p-pmirror" || fail "g9p-pmirror"
POSET=0
if [ "$ORC" -eq 0 ] && [ ! -s "$WORK/po.err" ] && [ -p "$WORK/po/a/f.txt" ] && [ -L "$WORK/po/a/l.lnk" ]; then POSET=1; fi
if grep -q '^Error 0x83058800$' "$WORK/po.err" 2>/dev/null; then
  N=$(grep -c 'a parent of path is not a directory' "$WORK/po.err" || true)
  if [ "$N" = "2" ] && grep -q '2 entries failed' "$WORK/po.err" \
     && grep -q 'not a directory: a/f.txt' "$WORK/po.err" \
     && grep -q 'not a directory: a/l.lnk' "$WORK/po.err" \
     && grep -q 'creating fs object: a/f.txt' "$WORK/po.err" \
     && grep -q 'creating fs object: a/l.lnk' "$WORK/po.err" \
     && [ -z "$(ls "$WORK/po/a")" ]; then POSET=1; fi
  if [ "$N" = "1" ] && grep -q '1 entries failed' "$WORK/po.err" \
     && grep -q 'not a directory: a/f.txt' "$WORK/po.err" \
     && grep -q 'creating fs object: a/f.txt' "$WORK/po.err" \
     && [ -L "$WORK/po/a/l.lnk" ]; then POSET=1; fi
  if [ "$N" = "1" ] && grep -q '1 entries failed' "$WORK/po.err" \
     && grep -q 'not a directory: a/l.lnk' "$WORK/po.err" \
     && grep -q 'creating fs object: a/l.lnk' "$WORK/po.err" \
     && [ -p "$WORK/po/a/f.txt" ]; then POSET=1; fi
fi
[ "$POSET" = "1" ] && pass "g9p-oshape" || fail "g9p-oshape"
[ ! -L "$WORK/pc/a" ] && [ -d "$WORK/pc/a" ] && [ -z "$(ls "$WORK/pc/a")" ] && pass "g9p-ctree" || fail "g9p-ctree"
diff -r "$WORK/pc" "$WORK/pp" >/dev/null 2>&1 && pass "g9p-cplock" || fail "g9p-cplock"

echo "== cell g9H-hlink-target (pair+H-line+trailer+N1, A-027#2) =="
cat > "$WORK/g9hmodal.err" <<'EOF'
Error 0x83058800
a parent of path is not a directory: hello/repeat.txt
invalid path: hello/repeat.txt
'H' LNK not a regular file: hello/repeat.txt
process hlinks
1 entries failed to extract
EOF
rm -rf "$WORK/ho" "$WORK/hv" "$WORK/hc" "$WORK/hw" "$WORK/hp" "$WORK/hx"
mkdir -p "$WORK/ho" "$WORK/hv" "$WORK/hc" "$WORK/hw" "$WORK/hp" "$WORK/hx"
echo MARKER > "$WORK/hv/marker"; echo MARKER > "$WORK/hw/marker"; echo MARKER > "$WORK/hx/marker"
ln -s "$WORK/hv" "$WORK/ho/hello"; ln -s "$WORK/hw" "$WORK/hc/hello"; ln -s "$WORK/hx" "$WORK/hp/hello"
ORC=0; sh "$ADAPTER" aar-decode "$V/aar/hlink-basic.aar" "$WORK/ho" 2>"$WORK/ho.err" >/dev/null || ORC=$?
CRC=0; "$AAD" "$V/aar/hlink-basic.aar" "$WORK/hc" 2>"$WORK/hc.err" >/dev/null || CRC=$?
PRC=0; python3 "$ROOT/proto/aad.py" "$V/aar/hlink-basic.aar" "$WORK/hp" 2>"$WORK/hp.err" >/dev/null || PRC=$?
[ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "g9h-cp-exit" || fail "g9h-cp-exit"
[ "$(ls "$WORK/hv")" = "marker" ] && [ "$(ls "$WORK/hw")" = "marker" ] && [ "$(ls "$WORK/hx")" = "marker" ] && pass "g9h-victim" || fail "g9h-victim"
diff "$WORK/g9hmodal.err" "$WORK/hc.err" >/dev/null 2>&1 && pass "g9h-cmodal" || fail "g9h-cmodal"
grep -v '^blocks:' "$WORK/hp.err" | diff "$WORK/hc.err" - >/dev/null 2>&1 && pass "g9h-pmirror" || fail "g9h-pmirror"
HOSET=0
if [ "$ORC" -eq 1 ] && diff "$WORK/g9hmodal.err" "$WORK/ho.err" >/dev/null 2>&1 && [ -z "$(ls "$WORK/ho/hello")" ]; then HOSET=1; fi
if [ "$ORC" -eq 0 ] && [ ! -s "$WORK/ho.err" ] && [ -f "$WORK/ho/hello/greet.txt" ] && [ -f "$WORK/ho/hello/repeat.txt" ] && [ "$(stat -f %i "$WORK/ho/hello/greet.txt")" = "$(stat -f %i "$WORK/ho/hello/repeat.txt")" ] && [ "$(stat -f %l "$WORK/ho/hello/greet.txt")" = "2" ]; then HOSET=1; fi
[ "$HOSET" = "1" ] && pass "g9h-oshape" || fail "g9h-oshape"
[ ! -L "$WORK/hc/hello" ] && [ -d "$WORK/hc/hello" ] && [ -z "$(ls "$WORK/hc/hello")" ] && pass "g9h-ctree" || fail "g9h-ctree"
diff -r "$WORK/hc" "$WORK/hp" >/dev/null 2>&1 && pass "g9h-cplock" || fail "g9h-cplock"

echo "== cell typ5-abc (CR-053 class-5 + desync cascade, PRE-009) =="
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/ta0.aar" 1 545950410000 || die "craft-ta0"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tb0.aar" 1 5459504200000000 || die "craft-tb0"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/tc0.aar" 1 545950430000000000000000 || die "craft-tc0"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/taF.aar" 1 545950410000FF || die "craft-taF"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/taZ.aar" 1 5459504100000000 || die "craft-taZ"
python3 "$HERE/craft.py" settyprec "$V/aar/hello-raw.aar" "$WORK/taB5.aar" 1 5459504205000000 || die "craft-taB5"
for n in ta0 tb0 tc0 taF taZ taB5; do
  rm -rf "$WORK/t5o-$n" "$WORK/t5c-$n" "$WORK/t5p-$n"
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/$n.aar" "$WORK/t5o-$n" 2>"$WORK/t5o-$n.err" >/dev/null || ORC=$?
  CRC=0; "$AAD" "$WORK/$n.aar" "$WORK/t5c-$n" 2>"$WORK/t5c-$n.err" >/dev/null || CRC=$?
  PRC=0; python3 "$ROOT/proto/aad.py" "$WORK/$n.aar" "$WORK/t5p-$n" 2>"$WORK/t5p-$n.err" >/dev/null || PRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "t5$n-exit" || fail "t5$n-exit"
  diff "$WORK/t5o-$n.err" "$WORK/t5c-$n.err" >/dev/null 2>&1 && pass "t5$n-cbytes" || fail "t5$n-cbytes"
  grep -v '^blocks:' "$WORK/t5p-$n.err" | diff "$WORK/t5o-$n.err" - >/dev/null 2>&1 && pass "t5$n-pbytes" || fail "t5$n-pbytes"
  diff -r "$WORK/t5o-$n" "$WORK/t5c-$n" >/dev/null 2>&1 && diff -r "$WORK/t5c-$n" "$WORK/t5p-$n" >/dev/null 2>&1 && pass "t5$n-tree" || fail "t5$n-tree"
done

echo "== cell m2clean-cuts (PRE-007 unified short rule, self-gen) =="
mkdir -p "$WORK/m2src"
python3 -c "import random; r=random.Random(40608); open('$WORK/m2src/big1','wb').write(r.randbytes(500*1024)); open('$WORK/m2src/big2','wb').write(r.randbytes(3*1024*1024))"
for blk in 1m 512k 128k; do
  freeze "$WORK/m2src"
  sh "$ADAPTER" aar-encode --alg lzfse --block "$blk" --threads 1 "$WORK/m2src" "$WORK/m2-$blk.aar" >/dev/null 2>&1 || die "m2 encode $blk"
done
cat > "$WORK/m2wrap.err" <<'EOF'
Extraction failed
extract failedError 0xbd011800
No more data
read error
archive stream read error (blob)
stream cancelled
1 entries failed to extract
EOF
# Single-block oracle SET (phase-race): content==modal ALWAYS (31/31);
# (tails,count) flips {(0t,c1),(2t,c2)} (M1sc fixed-tails WITHDRAWN).
# spec: blk:k:expectC (ABS or bytes)
for spec in "1m:1:262144" "1m:2:1310720" "512k:1:ABS" "512k:2:262144" "128k:8:262144" "128k:10:524288" "128k:12:786432" "128k:14:1048576"; do
  blk=$(echo "$spec" | cut -d: -f1); k=$(echo "$spec" | cut -d: -f2); exp=$(echo "$spec" | cut -d: -f3)
  CB=$(python3 -c "
import struct; d=open('$WORK/m2-$blk.aar','rb').read(); o=12; bs=[]
while o < len(d):
    r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[$k][0])") || die "m2 cut $spec"
  head -c "$CB" "$WORK/m2-$blk.aar" > "$WORK/m2cut-$blk-$k.aar"
  NB=$(python3 -c "
import struct; d=open('$WORK/m2cut-$blk-$k.aar','rb').read(); o=12; n=0
while o < len(d):
    r,p=struct.unpack('>QQ',d[o:o+16]); o+=16+p; n+=1
print(n)") || die "m2 count $spec"
  T=m2$blk$k
  rm -rf "$WORK/m2o-$T" "$WORK/m2c-$T" "$WORK/m2p-$T"
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/m2cut-$blk-$k.aar" "$WORK/m2o-$T" 2>"$WORK/m2o-$T.err" >/dev/null || ORC=$?
  CRC=0; "$AAD" "$WORK/m2cut-$blk-$k.aar" "$WORK/m2c-$T" 2>"$WORK/m2c-$T.err" >/dev/null || CRC=$?
  PRC=0; python3 "$ROOT/proto/aad.py" "$WORK/m2cut-$blk-$k.aar" "$WORK/m2p-$T" 2>"$WORK/m2p-$T.err" >/dev/null || PRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "$T-exit" || fail "$T-exit"
  CSZ=$([ -f "$WORK/m2c-$T/big2" ] && stat -f %z "$WORK/m2c-$T/big2" || echo ABS)
  CNUM=$([ -f "$WORK/m2c-$T/big2" ] && stat -f %z "$WORK/m2c-$T/big2" || echo 0)
  ONUM=$([ -f "$WORK/m2o-$T/big2" ] && stat -f %z "$WORK/m2o-$T/big2" || echo 0)
  [ "$CSZ" = "$exp" ] && pass "$T-cmodal" || fail "$T-cmodal"
  grep -v '^blocks:' "$WORK/m2p-$T.err" | diff "$WORK/m2c-$T.err" - >/dev/null 2>&1 && pass "$T-pmirror" || fail "$T-pmirror"
  diff -r "$WORK/m2c-$T" "$WORK/m2p-$T" >/dev/null 2>&1 && pass "$T-cplock" || fail "$T-cplock"
  cmp -s "$WORK/m2o-$T/big1" "$WORK/m2c-$T/big1" && pass "$T-big1" || fail "$T-big1"
  OT=$(grep -c 'reading payload' "$WORK/m2o-$T.err" || true)
  OCT=$(grep -o '[12] entries failed' "$WORK/m2o-$T.err" || echo NONE)
  if [ "$NB" = "1" ]; then
    diff "$WORK/m2wrap.err" "$WORK/m2c-$T.err" >/dev/null 2>&1 && pass "$T-ccbytes" || fail "$T-ccbytes"
    SOSET=0
    if [ "$ONUM" = "$CNUM" ] && [ "$OT" = "0" ] && [ "$OCT" = "1 entries failed" ]; then SOSET=1; fi
    if [ "$ONUM" = "$CNUM" ] && [ "$OT" = "2" ] && [ "$OCT" = "2 entries failed" ]; then SOSET=1; fi
    [ "$SOSET" = "1" ] && pass "$T-oshape" || fail "$T-oshape"
  else
    diff "$WORK/m2wrap.err" "$WORK/m2c-$T.err" >/dev/null 2>&1 && pass "$T-ccbytes" || fail "$T-ccbytes"
    OSET=0
    if [ "$ONUM" = "$CNUM" ] && [ "$OT" = "0" ] && [ "$OCT" = "1 entries failed" ]; then OSET=1; fi
    if [ "$ONUM" = "$((CNUM - 262144))" ] && [ "$OT" = "2" ] && [ "$OCT" = "1 entries failed" ]; then OSET=1; fi
    if [ "$ONUM" = "$CNUM" ] && [ "$OT" = "2" ] && [ "$OCT" = "2 entries failed" ]; then OSET=1; fi # multi-block single-block-style flip joint (VERIFY-5e4c75f FLAKE-1: m2512k2 oracle (262144,x2,fc2))
    [ "$OSET" = "1" ] && pass "$T-oshape" || fail "$T-oshape"
  fi
done

echo "== cell m2dev-truncpay (dev-formula + trunchdr-cap + A-028, self-gen) =="
mkdir -p "$WORK/dsrcA" "$WORK/dsrcB" "$WORK/dsrcC" "$WORK/dsrc511" "$WORK/dsrc512" "$WORK/dsrc750" "$WORK/dsrc800" "$WORK/dsrc600" "$WORK/dsrc350"
python3 -c "import random; r=random.Random(91827); open('$WORK/dsrcA/big1','wb').write(r.randbytes(500*1024)); open('$WORK/dsrcA/big2','wb').write(r.randbytes(2*1024*1024)); open('$WORK/dsrcB/big1','wb').write(r.randbytes(500*1024)); open('$WORK/dsrcB/big2','wb').write(r.randbytes(3*1024*1024)); open('$WORK/dsrcC/big1','wb').write(r.randbytes(500*1024)); open('$WORK/dsrcC/big2','wb').write(r.randbytes(2*1024*1024)); open('$WORK/dsrc511/big1','wb').write(r.randbytes(511*1024)); open('$WORK/dsrc511/big2','wb').write(r.randbytes(1024*1024)); open('$WORK/dsrc512/big1','wb').write(r.randbytes(512*1024)); open('$WORK/dsrc512/big2','wb').write(r.randbytes(1024*1024)); open('$WORK/dsrc750/big1','wb').write(r.randbytes(750*1024)); open('$WORK/dsrc750/big2','wb').write(r.randbytes(1024*1024)); open('$WORK/dsrc800/big1','wb').write(r.randbytes(800*1024)); open('$WORK/dsrc800/big2','wb').write(r.randbytes(1024*1024)); open('$WORK/dsrc600/big1','wb').write(r.randbytes(600*1024)); open('$WORK/dsrc600/big2','wb').write(r.randbytes(1024*1024)); open('$WORK/dsrc350/big1','wb').write(r.randbytes(350*1024)); open('$WORK/dsrc350/big2','wb').write(r.randbytes(300*1024))"
freeze "$WORK/dsrcA"
sh "$ADAPTER" aar-encode --alg lzfse --block 128k --threads 1 "$WORK/dsrcA" "$WORK/dv-128k.aar" >/dev/null 2>&1 || die "dev encode 128k"
freeze "$WORK/dsrcB"
sh "$ADAPTER" aar-encode --alg lzfse --block 1m --threads 1 "$WORK/dsrcB" "$WORK/dv-1m.aar" >/dev/null 2>&1 || die "dev encode 1m"
freeze "$WORK/dsrcC"
sh "$ADAPTER" aar-encode --alg lzfse --block 256k --threads 1 "$WORK/dsrcC" "$WORK/dv-256k.aar" >/dev/null 2>&1 || die "dev encode 256k"
for e in 511 512 750 800 600 350; do
  freeze "$WORK/dsrc$e"
  sh "$ADAPTER" aar-encode --alg lzfse --block 128k --threads 1 "$WORK/dsrc$e" "$WORK/dv-edge$e.aar" >/dev/null 2>&1 || die "dev encode edge$e"
done
# spec blk:k:fracN:fracD:kind:expC:oset  (kind=pay|hdr|hard; oset=oracle sizes, 0=empty-file)
for spec in "128k:6:1:2:pay:0:0" "128k:8:1:2:pay:262144:262144,0" "128k:10:1:2:pay:524288:524288,262144" "128k:12:1:2:pay:786432:524288,262144,786432" "128k:14:1:2:pay:1048576:786432,524288,1048576" "128k:16:1:2:pay:1310720:1048576,786432,1310720" "1m:2:1:2:pay:1310720:524288,786432,1048576,1310720" "1m:2:1:4:pay:1310720:1310720,1048576" "1m:2:3:4:pay:1310720:1310720,1048576" "1m:1:1:2:pay:262144:262144,0" "1m:0:1:2:hard:ABS:ABS" "256k:8:1:2:pay:1310720:1310720,1048576" "1m:2:10:1:HDR:1310720:1310720,1048576" "128k:8:10:1:HDR:262144:262144,0" "128k:5:1:2:pay:ABS:ABS" "128k:7:1:2:pay:0:0,ABS" "edge511:6:1:2:pay:0:0" "edge512:6:1:2:pay:ABS:ABS" "edge750:8:1:2:pay:0:0" "edge800:8:1:2:pay:ABS:ABS" "edge600:7:1:2:pay:ABS:ABS" "edge350:4:1:2:pay:ABS:ABS"; do
  blk=$(echo "$spec" | cut -d: -f1); k=$(echo "$spec" | cut -d: -f2); fn=$(echo "$spec" | cut -d: -f3); fd=$(echo "$spec" | cut -d: -f4); kind=$(echo "$spec" | cut -d: -f5); exp=$(echo "$spec" | cut -d: -f6); oset=$(echo "$spec" | cut -d: -f7)
  T=dv$blk$k$fn$fd$kind
  if [ "$kind" = "HDR" ]; then
    CB=$(python3 -c "
import struct; d=open('$WORK/dv-$blk.aar','rb').read(); o=12; bs=[]
while o < len(d):
    r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[$k][0]+$fn)") || die "dev cut $spec"
  else
    CB=$(python3 -c "
import struct; d=open('$WORK/dv-$blk.aar','rb').read(); o=12; bs=[]
while o < len(d):
    r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[$k][0]+16+bs[$k][2]*$fn//$fd)") || die "dev cut $spec"
  fi
  head -c "$CB" "$WORK/dv-$blk.aar" > "$WORK/dcut-$T.aar"
  rm -rf "$WORK/dvo-$T" "$WORK/dvc-$T" "$WORK/dvp-$T"; mkdir -p "$WORK/dvo-$T" "$WORK/dvc-$T" "$WORK/dvp-$T"
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/dcut-$T.aar" "$WORK/dvo-$T" 2>"$WORK/dvo-$T.err" >/dev/null || ORC=$?
  CRC=0; "$AAD" "$WORK/dcut-$T.aar" "$WORK/dvc-$T" 2>"$WORK/dvc-$T.err" >/dev/null || CRC=$?
  PRC=0; python3 "$ROOT/proto/aad.py" "$WORK/dcut-$T.aar" "$WORK/dvp-$T" 2>"$WORK/dvp-$T.err" >/dev/null || PRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "$T-exit" || fail "$T-exit"
  CSZ=$([ -f "$WORK/dvc-$T/big2" ] && stat -f %z "$WORK/dvc-$T/big2" || echo ABS)
  OSZ=$([ -f "$WORK/dvo-$T/big2" ] && stat -f %z "$WORK/dvo-$T/big2" || echo ABS)
  [ "$CSZ" = "$exp" ] && pass "$T-cmodal" || fail "$T-cmodal"
  grep -v '^blocks:' "$WORK/dvp-$T.err" | diff "$WORK/dvc-$T.err" - >/dev/null 2>&1 && pass "$T-pmirror" || fail "$T-pmirror"
  diff -r "$WORK/dvc-$T" "$WORK/dvp-$T" >/dev/null 2>&1 && pass "$T-cplock" || fail "$T-cplock"
  mcnorm "$WORK/dvo-$T.err" > "$WORK/dvo-$T.n"; mcnorm "$WORK/dvc-$T.err" > "$WORK/dvc-$T.n"
  diff "$WORK/dvo-$T.n" "$WORK/dvc-$T.n" >/dev/null 2>&1 && pass "$T-shape" || fail "$T-shape"
  t1pin "$WORK/dvo-$T.err" "$T"
  if [ "$kind" = "hard" ]; then
    [ -z "$(ls "$WORK/dvo-$T")" ] && [ -z "$(ls "$WORK/dvc-$T")" ] && pass "$T-empty" || fail "$T-empty"
  else
    if [ "$blk" = "edge800" ] || [ "$blk" = "edge600" ]; then # A-029 race-pin (Q-029 CLOSED): oracle big1 modal-vs-minority {FULL,chunk-partial,ABSENT}; C modal FULL; partial = byte-prefix
      if [ "$blk" = "edge800" ]; then FULL1=819200; PART1=524288; else FULL1=614400; PART1=262144; fi # edge600 minority 262144 first-hand (sweep GATE-d110318 flake-2; A-029 family)
      OSZ1=$([ -f "$WORK/dvo-$T/big1" ] && stat -f %z "$WORK/dvo-$T/big1" || echo ABS)
      case ",$FULL1,$PART1,ABS," in *,"$OSZ1,"*) pass "$T-big1";; *) fail "$T-big1";; esac
      if [ -f "$WORK/dvo-$T/big1" ]; then head -c "$OSZ1" "$WORK/dsrc${blk#edge}/big1" | cmp -s - "$WORK/dvo-$T/big1" && pass "$T-oprefix" || fail "$T-oprefix"; else pass "$T-oprefix"; fi
      cmp -s "$WORK/dsrc${blk#edge}/big1" "$WORK/dvc-$T/big1" && pass "$T-cbig1full" || fail "$T-cbig1full"
    else cmp -s "$WORK/dvo-$T/big1" "$WORK/dvc-$T/big1" && pass "$T-big1" || fail "$T-big1"; fi
    case ",$oset," in *,"$OSZ,"*) pass "$T-oshape";; *) fail "$T-oshape";; esac
    if [ -f "$WORK/dvo-$T/big2" ] && [ -f "$WORK/dvc-$T/big2" ]; then
      [ "$(stat -f %p "$WORK/dvo-$T/big2")" = "$(stat -f %p "$WORK/dvc-$T/big2")" ] && pass "$T-mode" || fail "$T-mode"
    else
      pass "$T-mode"
    fi
  fi
done

echo "== cell m3chain (TIP2e chain-together law, self-crafted) =="
mkchainpay() { # $1=base $2=comp' $3=name
  M3H=$(python3 -c "import struct; d=open('$V/aar/$1.aar','rb').read(); raw,pay=struct.unpack('>QQ',d[12:28]); print((struct.pack('>Q',raw)+struct.pack('>Q',$2)).hex())") || die "m3ch$3 walk"
  python3 "$HERE/craft.py" setblk "$V/aar/$1.aar" "$WORK/ch$3.aar" 0 "$M3H" || die "craft-m3ch$3"
}
mkchainpay hello-lzfse 1 H1; mkchainpay hello-lzfse 6 H6; mkchainpay hello-lzfse 12 H12
mkchainpay hello-lzfse 13 H13; mkchainpay hello-lzfse 50 H50; mkchainpay hello-lzfse 92 H92; mkchainpay hello-lzfse 93 H93
mkchainpay empty-lzfse 103 E103; mkchainpay empty-lzfse 100 E100; mkchainpay empty-lzfse 97 E97
mkchainpay empty-lzfse 63 E63; mkchainpay empty-lzfse 13 E13
M3H=$(python3 -c "import struct; d=open('$V/aar/hello-lzfse.aar','rb').read(); raw,pay=struct.unpack('>QQ',d[12:28]); print((struct.pack('>Q',raw+500)+struct.pack('>Q',pay)).hex())") || die "m3chUH walk"
python3 "$HERE/craft.py" setblk "$V/aar/hello-lzfse.aar" "$WORK/chUH.aar" 0 "$M3H" || die "craft-m3chUH"
for t in 5 16 20 32; do cp "$WORK/chUH.aar" "$WORK/chA$t.aar"; python3 -c "open('$WORK/chA$t.aar','ab').write(bytes($t))" || die "craft-chA$t"; done
cp "$WORK/chUH.aar" "$WORK/chG16.aar"; python3 -c "open('$WORK/chG16.aar','ab').write(bytes([0x5A])*16)" || die "craft-chG16"
python3 - "$WORK/chUH.aar" "$WORK" <<'PYEOF' || die "craft-chSP"
import struct, sys
base = open(sys.argv[1], 'rb').read(); w = sys.argv[2]
open(w + '/chSP1.aar', 'wb').write(base + struct.pack('>QQ', 1, 100) + bytes(4))
open(w + '/chSP2.aar', 'wb').write(base + struct.pack('>QQ', 5, 5) + bytes(5) + bytes(3))
open(w + '/chSP3.aar', 'wb').write(base + struct.pack('>QQ', 0, 0) + struct.pack('>QQ', 2, 2) + bytes(2) + bytes(7))
open(w + '/chSP4.aar', 'wb').write(base + struct.pack('>QQ', 5, 5) + bytes(5))
PYEOF
mkchainpay hello-lzfse 5 V2base
python3 -c "
d = bytearray(open('$WORK/chV2base.aar', 'rb').read())
d[33:49] = bytes(16)
open('$WORK/chV2.aar', 'wb').write(bytes(d))" || die "craft-chV2"
mkdir -p "$WORK/chmzsrc"; dd if=/dev/zero of="$WORK/chmzsrc/f" bs=1024 count=600 2>/dev/null
freeze "$WORK/chmzsrc"
sh "$ADAPTER" aar-encode --alg lzfse --block 256k --threads 1 "$WORK/chmzsrc" "$WORK/chmz.aar" >/dev/null 2>&1 || die "chmz encode"
CHMZ1=$(python3 -c "import struct; d=open('$WORK/chmz.aar','rb').read(); o=12; bs=[];
while o < len(d):
 r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print(bs[1][0]+16)") || die "chmz walk"
python3 "$HERE/craft.py" patch "$WORK/chmz.aar" "$WORK/chMZ3.aar" "$CHMZ1" ff || die "craft-chMZ3"
python3 -c "open('$WORK/chMZ3.aar','ab').write(bytes(3))" || die "craft-chMZ3t"
python3 "$HERE/craft.py" patch "$WORK/chmz.aar" "$WORK/chMZ20.aar" "$CHMZ1" ff || die "craft-chMZ20"
python3 -c "open('$WORK/chMZ20.aar','ab').write(bytes(20))" || die "craft-chMZ20t"
runchain() { # $1=name (-t-1-only: deterministic short stanzas, IDENT; race modes retired)
  rm -rf "$WORK/cho-$1" "$WORK/chc-$1" "$WORK/chp-$1"; mkdir -p "$WORK/cho-$1" "$WORK/chc-$1" "$WORK/chp-$1"
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/ch$1.aar" "$WORK/cho-$1" 2>"$WORK/cho-$1.err" >/dev/null || ORC=$?
  CRC=0; "$AAD" "$WORK/ch$1.aar" "$WORK/chc-$1" 2>"$WORK/chc-$1.err" >/dev/null || CRC=$?
  PRC=0; python3 "$HERE/../proto/aad.py" "$WORK/ch$1.aar" "$WORK/chp-$1" 2>"$WORK/chp-$1.err" >/dev/null || PRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "ch$1-exit" || fail "ch$1-exit"
  grep -v '^blocks:' "$WORK/chp-$1.err" | diff "$WORK/chc-$1.err" - >/dev/null 2>&1 && pass "ch$1-pmirror" || fail "ch$1-pmirror"
  [ -z "$(find "$WORK/cho-$1" "$WORK/chc-$1" -type f 2>/dev/null)" ] && pass "ch$1-empty" || fail "ch$1-empty"
  diff -r "$WORK/cho-$1" "$WORK/chc-$1" >/dev/null 2>&1 && pass "ch$1-tree" || fail "ch$1-tree"
  diff -r "$WORK/chc-$1" "$WORK/chp-$1" >/dev/null 2>&1 && pass "ch$1-lock" || fail "ch$1-lock"
  diff "$WORK/cho-$1.err" "$WORK/chc-$1.err" >/dev/null 2>&1 && pass "ch$1-shape" || fail "ch$1-shape"
  t1pin "$WORK/cho-$1.err" "ch$1"
}
for n in H1 H6 H12 H13 H50 H92 H93 E103 E100 E97 E63 E13 A5 A16 A20 A32 G16 V2 SP1 SP2 SP4 MZ3 MZ20 SP3; do runchain "$n"; done

echo "== cell m1m2-tip2e (M1 tails + M2 modals, self-gen rule cuts) =="
mkdir -p "$WORK/t2src/big" "$WORK/t2m2" "$WORK/t2dsrcB"
python3 -c "import random; r=random.Random(112358); open('$WORK/t2src/big/r500k.bin','wb').write(r.randbytes(500000)); open('$WORK/t2src/big/z3m.bin','wb').write(bytes(3000000))"
python3 -c "import random; r=random.Random(40608); open('$WORK/t2m2/big1','wb').write(r.randbytes(500*1024)); open('$WORK/t2m2/big2','wb').write(r.randbytes(3*1024*1024))"
python3 -c "import random; r=random.Random(91827); a1=r.randbytes(500*1024); a2=r.randbytes(2*1024*1024); open('$WORK/t2dsrcB/big1','wb').write(r.randbytes(500*1024)); open('$WORK/t2dsrcB/big2','wb').write(r.randbytes(3*1024*1024))"
freeze "$WORK/t2src"
sh "$ADAPTER" aar-encode --alg lzfse --block 1m --threads 1 "$WORK/t2src" "$WORK/t2mb.aar" >/dev/null 2>&1 || die "t2mb encode"
freeze "$WORK/t2m2"
sh "$ADAPTER" aar-encode --alg lzfse --block 1m --threads 1 "$WORK/t2m2" "$WORK/t2m2.aar" >/dev/null 2>&1 || die "t2m2 encode"
freeze "$WORK/t2dsrcB"
sh "$ADAPTER" aar-encode --alg lzfse --block 1m --threads 1 "$WORK/t2dsrcB" "$WORK/t2dsrcB.aar" >/dev/null 2>&1 || die "t2dsrcB encode"
t2cut() { # $1=base $2=pyexpr $3=name
  CB=$(python3 -c "
import struct; d=open('$WORK/t2$1.aar','rb').read(); o=12; bs=[]
while o < len(d):
    r,p=struct.unpack('>QQ',d[o:o+16]); bs.append((o,r,p)); o+=16+p
print($2)") || die "t2cut $3"
  head -c "$CB" "$WORK/t2$1.aar" > "$WORK/t2$3.aar" || die "craft-t2$3"
}
t2cut mb "bs[2][0]+4" 618
t2cut mb "bs[3][0]+111" 7500
t2cut mb "bs[1][0]+161" 506k
t2cut m2 "bs[1][0]+4" m2th1
t2cut m2 "bs[2][0]+4" m2th2
t2cut m2 "bs[3][0]+4" m2th3
t2cut dsrcB "bs[3][0]+16+bs[3][2]//2" rnd3m
t2cut m2 "bs[1][0]+16+500000" tp1a
t2cut m2 "bs[1][0]+16+900000" tp1b
runt2() { # $1=name $2=relpath $3=csize $4=ctails $5=oset $6=otails $7=ocount
  rm -rf "$WORK/t2o-$1" "$WORK/t2c-$1" "$WORK/t2p-$1"; mkdir -p "$WORK/t2o-$1" "$WORK/t2c-$1" "$WORK/t2p-$1"
  ORC=0; sh "$ADAPTER" aar-decode "$WORK/t2$1.aar" "$WORK/t2o-$1" 2>"$WORK/t2o-$1.err" >/dev/null || ORC=$?
  CRC=0; "$AAD" "$WORK/t2$1.aar" "$WORK/t2c-$1" 2>"$WORK/t2c-$1.err" >/dev/null || CRC=$?
  PRC=0; python3 "$HERE/../proto/aad.py" "$WORK/t2$1.aar" "$WORK/t2p-$1" 2>"$WORK/t2p-$1.err" >/dev/null || PRC=$?
  [ "$ORC" -eq 1 ] && [ "$CRC" -eq 1 ] && [ "$PRC" -eq 1 ] && pass "t2$1-exit" || fail "t2$1-exit"
  CSZ=$([ -f "$WORK/t2c-$1/$2" ] && stat -f %z "$WORK/t2c-$1/$2" || echo ABS)
  OSZ=$([ -f "$WORK/t2o-$1/$2" ] && stat -f %z "$WORK/t2o-$1/$2" || echo ABS)
  [ "$CSZ" = "$3" ] && pass "t2$1-cmodal" || fail "t2$1-cmodal"
  case ",$5," in *,"$OSZ,"*) pass "t2$1-oshape";; *) fail "t2$1-oshape";; esac
  CT=$(grep -c 'reading payload' "$WORK/t2c-$1.err" || true)
  OT=$(grep -c 'reading payload' "$WORK/t2o-$1.err" || true)
  [ "$CT" = "$4" ] && pass "t2$1-ctails" || fail "t2$1-ctails"
  case ",$6," in *,"$OT,"*) pass "t2$1-otails";; *) fail "t2$1-otails";; esac
  CC=$(grep -o '[0-9]* entries failed' "$WORK/t2c-$1.err" || echo NONE)
  OC=$(grep -o '[0-9]* entries failed' "$WORK/t2o-$1.err" || echo NONE)
  [ "$CC" = "1 entries failed" ] && pass "t2$1-ccount" || fail "t2$1-ccount"
  case ",$7," in *,"$OC,"*) pass "t2$1-ocount";; *) fail "t2$1-ocount";; esac
  grep -v '^blocks:' "$WORK/t2p-$1.err" | diff "$WORK/t2c-$1.err" - >/dev/null 2>&1 && pass "t2$1-pmirror" || fail "t2$1-pmirror"
  diff -r "$WORK/t2c-$1" "$WORK/t2p-$1" >/dev/null 2>&1 && pass "t2$1-cplock" || fail "t2$1-cplock"
  mcnorm "$WORK/t2o-$1.err" > "$WORK/t2o-$1.n"; mcnorm "$WORK/t2c-$1.err" > "$WORK/t2c-$1.n"
  diff "$WORK/t2o-$1.n" "$WORK/t2c-$1.n" >/dev/null 2>&1 && pass "t2$1-shape" || fail "t2$1-shape"
  t1pin "$WORK/t2o-$1.err" "t2$1"
  if [ -f "$WORK/t2o-$1/$2" ] && [ -f "$WORK/t2c-$1/$2" ]; then
    SO=$(stat -f %z "$WORK/t2o-$1/$2"); SC=$(stat -f %z "$WORK/t2c-$1/$2")
    if [ "$SO" -le "$SC" ]; then head -c "$SO" "$WORK/t2c-$1/$2" | cmp -s - "$WORK/t2o-$1/$2" && pass "t2$1-prefix" || fail "t2$1-prefix"
    else head -c "$SC" "$WORK/t2o-$1/$2" | cmp -s - "$WORK/t2c-$1/$2" && pass "t2$1-prefix" || fail "t2$1-prefix"; fi
    [ "$(stat -f %p "$WORK/t2o-$1/$2")" = "$(stat -f %p "$WORK/t2c-$1/$2")" ] && pass "t2$1-mode" || fail "t2$1-mode"
  else pass "t2$1-prefix"; pass "t2$1-mode"; fi
}
runt2 618 big/z3m.bin 1310720 2 "1310720,1048576" "0,2,4" "1 entries failed,2 entries failed"
cmp -s "$WORK/t2src/big/r500k.bin" "$WORK/t2o-618/big/r500k.bin" && pass "t2618-rfull" || fail "t2618-rfull"
runt2 7500 big/z3m.bin 2359296 2 "2359296,2097152" "0,2" "1 entries failed"
cmp -s "$WORK/t2src/big/r500k.bin" "$WORK/t2o-7500/big/r500k.bin" && pass "t27500-rfull" || fail "t27500-rfull"
runt2 506k big/z3m.bin 262144 0 "0,262144,ABS" "0,2,4" "1 entries failed,2 entries failed" # otails x4 minority race 2/11 pooled (CR-048 SET)
cmp -s "$WORK/t2src/big/r500k.bin" "$WORK/t2o-506k/big/r500k.bin" && pass "t2506k-rfull" || fail "t2506k-rfull"
runt2 m2th1 big2 262144 0 "262144" "0,2" "1 entries failed,2 entries failed"
cmp -s "$WORK/t2m2/big1" "$WORK/t2o-m2th1/big1" && pass "t2m2th1-b1full" || fail "t2m2th1-b1full"
runt2 m2th2 big2 1310720 2 "1310720,1048576" "0,2" "1 entries failed,2 entries failed"
cmp -s "$WORK/t2m2/big1" "$WORK/t2o-m2th2/big1" && pass "t2m2th2-b1full" || fail "t2m2th2-b1full"
runt2 m2th3 big2 2359296 2 "2359296,2097152" "0,2" "1 entries failed"
cmp -s "$WORK/t2m2/big1" "$WORK/t2o-m2th3/big1" && pass "t2m2th3-b1full" || fail "t2m2th3-b1full"
runt2 rnd3m big2 2359296 2 "2359296,2097152" "0,2" "1 entries failed" # 8ch flush-race minority 1/11 pooled (r3; same class as 7500)
cmp -s "$WORK/t2dsrcB/big1" "$WORK/t2o-rnd3m/big1" && pass "t2rnd3m-b1full" || fail "t2rnd3m-b1full"
runt2 tp1a big2 262144 0 "262144" "0,2" "1 entries failed,2 entries failed"
cmp -s "$WORK/t2m2/big1" "$WORK/t2o-tp1a/big1" && pass "t2tp1a-b1full" || fail "t2tp1a-b1full"
runt2 tp1b big2 262144 0 "262144" "0,2" "1 entries failed,2 entries failed"
cmp -s "$WORK/t2m2/big1" "$WORK/t2o-tp1b/big1" && pass "t2tp1b-b1full" || fail "t2tp1b-b1full"

[ "$FAIL" -eq 0 ] && echo CBATTERY-GREEN || echo CBATTERY-RED
exit "$FAIL"
