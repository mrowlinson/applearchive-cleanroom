#!/bin/sh
# aea-battery.sh v1 -- writer2 own AEA fixture battery (proto vs oracle).
# Self-generating: encrypts with oracle `aea`, decrypts with proto + oracle, cmp.
# Pins: vectors/selfgen (13/13 shasum required first). Exits 0 ALL-PASS / 1 any FAIL.
# Needs: AEAD_PY (venv python w/ cryptography+lz4), LZFSE_BIN (own-built lzfse CLI).
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
AEAD_PY=${AEAD_PY:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/.venv/bin/python}
LZFSE_BIN=${LZFSE_BIN:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/oss/lzfse/build/bin/lzfse}
ZBM_BIN=${ZBM_BIN:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/oss/zbm/zbmcat}
export LZFSE_BIN ZBM_BIN
WORK=$(mktemp -d "${TMPDIR:-/tmp}/aea-bat.XXXXXX")
trap 'rm -rf "$WORK"' EXIT
PASS=0; FAIL=0
ok() { PASS=$((PASS+1)); echo "PASS $1"; }
bad() { FAIL=$((FAIL+1)); echo "FAIL $1"; }
cell() { # name proto-args... -- input expected
  name=$1; shift
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt "$@" -o "$WORK/out.bin" 2>"$WORK/err.txt" \
     && cmp -s "$WORK/out.bin" "$EXP"; then ok "$name"; else bad "$name"; fi
}

(cd "$REPO/vectors/selfgen" && shasum -c SHA256SUMS >/dev/null 2>&1) || { echo "HARD FAIL pins"; exit 1; }

# 1-2. pinned fixtures
EXP=$REPO/vectors/selfgen/aar/hello-raw.aar
cell pin-p1 --key "$REPO/vectors/selfgen/aea/testkey.bin" -i "$REPO/vectors/selfgen/aea/hello-p1-nopad.aea"
cell pin-p5 --password 'test-password-fixture' -i "$REPO/vectors/selfgen/aea/hello-p5.aea"

# 3. selfgen profiles 0-5 (fixed inputs; oracle encrypt, proto cmp)
printf 'hello aea world\n' > "$WORK/msg.txt"
openssl ecparam -name prime256v1 -genkey -noout -out "$WORK/ec-priv.pem" 2>/dev/null
openssl ec -in "$WORK/ec-priv.pem" -pubout -out "$WORK/ec-pub.pem" 2>/dev/null
head -c 32 /dev/urandom > "$WORK/key32.bin"
PW='testpw32....................................'
aea encrypt -profile 0 -sign-priv "$WORK/ec-priv.pem" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p0.aea" 2>/dev/null
aea encrypt -profile 1 -key "$WORK/key32.bin" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p1.aea" 2>/dev/null
aea encrypt -profile 2 -key "$WORK/key32.bin" -sign-priv "$WORK/ec-priv.pem" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p2.aea" 2>/dev/null
aea encrypt -profile 3 -recipient-pub "$WORK/ec-pub.pem" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p3.aea" 2>/dev/null
aea encrypt -profile 4 -recipient-pub "$WORK/ec-pub.pem" -sign-priv "$WORK/ec-priv.pem" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p4.aea" 2>/dev/null
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p5.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell sg-p0 --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0.aea"
cell sg-p1 --key "$WORK/key32.bin" -i "$WORK/p1.aea"
cell sg-p2 --key "$WORK/key32.bin" --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p2.aea"
cell sg-p3 --recipient-priv "$WORK/ec-priv.pem" -i "$WORK/p3.aea"
cell sg-p4 --recipient-priv "$WORK/ec-priv.pem" --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p4.aea"
cell sg-p5 --password "$PW" -i "$WORK/p5.aea"

# 4. codecs (900KB text, p5)
python3 -c "open('$WORK/bigtext.bin','wb').write(b'The quick brown fox jumps over the lazy dog. '*20000)"
for a in none zlib lzma lz4 lzfse lzbitmap; do
  aea encrypt -profile 5 -password-value "$PW" -a $a -padding none -i "$WORK/bigtext.bin" -o "$WORK/c-$a.aea" 2>/dev/null
  EXP=$WORK/bigtext.bin
  cell codec-$a --password "$PW" -i "$WORK/c-$a.aea"
done
aea encrypt -profile 5 -password-value "$PW" -a lzraven -padding none -i "$WORK/bigtext.bin" -o "$WORK/c-lzraven.aea" 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/c-lzraven.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "codec-lzraven-failclosed"; else ok "codec-lzraven-failclosed"; fi

# 5. checksums
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -checksum none -i "$WORK/msg.txt" -o "$WORK/k-none.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell cksum-none --password "$PW" -i "$WORK/k-none.aea"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -checksum murmur64 -i "$WORK/msg.txt" -o "$WORK/k-mur.aea" 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/k-mur.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "cksum-murmur-failclosed"; else ok "cksum-murmur-failclosed"; fi

# 5b. auth-data forms
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -auth-data-value hex:deadbeef -auth-data-value hex:0102030405060708 -i "$WORK/msg.txt" -o "$WORK/auth2.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell auth-raw2 --password "$PW" -i "$WORK/auth2.aea"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -auth-data-key mykey -auth-data-value hex:deadbeef -i "$WORK/msg.txt" -o "$WORK/authkv.aea" 2>/dev/null
cell auth-kv --password "$PW" -i "$WORK/authkv.aea"

# 6. empty
: > "$WORK/empty.bin"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -i "$WORK/empty.bin" -o "$WORK/empty.aea" 2>/dev/null
EXP=$WORK/empty.bin
cell empty --password "$PW" -i "$WORK/empty.aea"

# 7. range + 8. id
aea decrypt -password-value "$PW" -range-offset 0 -range-size 5 -i "$WORK/p5.aea" -o "$WORK/rg-ora.bin" 2>/dev/null
EXP=$WORK/rg-ora.bin
cell range-0-5 --password "$PW" --range-offset 0 --range-size 5 -i "$WORK/p5.aea"
OID=$(aea id -i "$WORK/p5.aea" 2>/dev/null)
PID=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/p5.aea" 2>/dev/null)
if [ "$OID" = "$PID" ] && [ -n "$OID" ]; then ok "id"; else bad "id"; fi

# 9. error-class parity (exit codes)
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password WRONG -i "$WORK/p5.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-wrongpw"; else ok "err-wrongpw"; fi
head -c 8 "$WORK/p5.aea" > "$WORK/tr8.aea"
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/tr8.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-trunc8"; else ok "err-trunc8"; fi
cp "$WORK/p5.aea" "$WORK/mg.aea" && printf 'Q' | dd of="$WORK/mg.aea" bs=1 seek=0 conv=notrunc 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/mg.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-magic"; else ok "err-magic"; fi
openssl ecparam -name prime256v1 -genkey -noout -out "$WORK/ec2-priv.pem" 2>/dev/null
openssl ec -in "$WORK/ec2-priv.pem" -pubout -out "$WORK/ec2-pub.pem" 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key32.bin" --sign-pub "$WORK/ec2-pub.pem" -i "$WORK/p2.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-wrongsign"; else ok "err-wrongsign"; fi
aea encrypt -profile 0 -sign-pub "$WORK/ec-pub.pem" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p0u.aea" 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0u.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-unsigned"; else ok "err-unsigned"; fi
cp "$WORK/p0u.aea" "$WORK/p0s.aea" && aea sign -sign-priv "$WORK/ec-priv.pem" -o "$WORK/p0s.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell sign-later --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0s.aea"

# 10. append
printf 'APPENDED-DATA-BLOCK' > "$WORK/app-in.bin"
cp "$WORK/p5.aea" "$WORK/app.aea"
aea append -password-value "$PW" -i "$WORK/app-in.bin" -o "$WORK/app.aea" 2>/dev/null
cat "$WORK/msg.txt" "$WORK/app-in.bin" > "$WORK/app-exp.bin"
EXP=$WORK/app-exp.bin
cell append --password "$PW" -i "$WORK/app.aea"

echo "PASS=$PASS FAIL=$FAIL"
[ "$FAIL" -eq 0 ]
