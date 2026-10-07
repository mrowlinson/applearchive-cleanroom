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
LZR_BIN=${LZR_BIN:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/oss/lzraven/build/lzraven_dec}
export LZFSE_BIN ZBM_BIN LZR_BIN
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
EXP=$WORK/bigtext.bin
cell codec-lzraven --password "$PW" -i "$WORK/c-lzraven.aea"
cp "$LZR_BIN" "$WORK/macho.bin"
aea encrypt -profile 5 -password-value "$PW" -a lzraven -padding none -i "$WORK/macho.bin" -o "$WORK/c-lzraven-macho.aea" 2>/dev/null
EXP=$WORK/macho.bin
cell codec-lzraven-macho --password "$PW" -i "$WORK/c-lzraven-macho.aea"
# 4b. mixed-content lzraven (fires in-stream raw bit0 blocks, APROBE-01)
python3 -c "import random;open('$WORK/mixrt.bin','wb').write(random.Random(7).randbytes(524288)+b'Mixed tail text. '*40000)"
aea encrypt -profile 5 -password-value "$PW" -a lzraven -padding none -i "$WORK/mixrt.bin" -o "$WORK/c-lzraven-mixrt.aea" 2>/dev/null
EXP=$WORK/mixrt.bin
cell codec-lzraven-mixrt --password "$PW" -i "$WORK/c-lzraven-mixrt.aea"
python3 -c "import random;open('$WORK/mixtr.bin','wb').write(b'Mixed head text. '*40000+random.Random(9).randbytes(524288))"
aea encrypt -profile 5 -password-value "$PW" -a lzraven -padding none -i "$WORK/mixtr.bin" -o "$WORK/c-lzraven-mixtr.aea" 2>/dev/null
EXP=$WORK/mixtr.bin
cell codec-lzraven-mixtr --password "$PW" -i "$WORK/c-lzraven-mixtr.aea"

# 4c. padding modes (proto strips implicitly via segment structure; sizes APROBE-01)
aea encrypt -profile 5 -password-value "$PW" -a none -i "$WORK/msg.txt" -o "$WORK/pad-def.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell pad-default --password "$PW" -i "$WORK/pad-def.aea"
for p in adaptive 16 4096 65536; do
  aea encrypt -profile 5 -password-value "$PW" -a none -padding $p -i "$WORK/msg.txt" -o "$WORK/pad-$p.aea" 2>/dev/null
  EXP=$WORK/msg.txt
  cell pad-$p --password "$PW" -i "$WORK/pad-$p.aea"
done
aea encrypt -profile 1 -key "$WORK/key32.bin" -a zlib -i "$WORK/bigtext.bin" -o "$WORK/pad-big.aea" 2>/dev/null
EXP=$WORK/bigtext.bin
cell pad-big-def --key "$WORK/key32.bin" -i "$WORK/pad-big.aea"
aea encrypt -profile 1 -key "$WORK/key32.bin" -a zlib -padding 4096 -checksum murmur64 -i "$WORK/bigtext.bin" -o "$WORK/pad-ck.aea" 2>/dev/null
EXP=$WORK/bigtext.bin
cell pad-cksum-combo --key "$WORK/key32.bin" -i "$WORK/pad-ck.aea"

# 5. checksums
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -checksum none -i "$WORK/msg.txt" -o "$WORK/k-none.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell cksum-none --password "$PW" -i "$WORK/k-none.aea"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -checksum murmur64 -i "$WORK/msg.txt" -o "$WORK/k-mur.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell cksum-murmur --password "$PW" -i "$WORK/k-mur.aea"
python3 -c "open('$WORK/bigtext2.bin','wb').write(b'Murmur over many segments: the quick brown fox. '*30000)"
aea encrypt -profile 1 -key "$WORK/key32.bin" -a zlib -padding none -checksum murmur64 -i "$WORK/bigtext2.bin" -o "$WORK/k-mur-big.aea" 2>/dev/null
EXP=$WORK/bigtext2.bin
cell cksum-murmur-big --key "$WORK/key32.bin" -i "$WORK/k-mur-big.aea"

# 5b. auth-data forms
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -auth-data-value hex:deadbeef -auth-data-value hex:0102030405060708 -i "$WORK/msg.txt" -o "$WORK/auth2.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell auth-raw2 --password "$PW" -i "$WORK/auth2.aea"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -auth-data-key mykey -auth-data-value hex:deadbeef -i "$WORK/msg.txt" -o "$WORK/authkv.aea" 2>/dev/null
cell auth-kv --password "$PW" -i "$WORK/authkv.aea"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -auth-data-value hex:aa -auth-data-value hex:bbcc -auth-data-value hex:dd -i "$WORK/msg.txt" -o "$WORK/auth3.aea" 2>/dev/null
cell auth-raw3 --password "$PW" -i "$WORK/auth3.aea"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -auth-data-key k1 -auth-data-value hex:aa -auth-data-key k2 -auth-data-value hex:bb -i "$WORK/msg.txt" -o "$WORK/authkv2.aea" 2>/dev/null
cell auth-kv2 --password "$PW" -i "$WORK/authkv2.aea"

# 6. empty
: > "$WORK/empty.bin"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -i "$WORK/empty.bin" -o "$WORK/empty.aea" 2>/dev/null
EXP=$WORK/empty.bin
cell empty --password "$PW" -i "$WORK/empty.aea"

# 7. range + 8. id
aea decrypt -password-value "$PW" -range-offset 0 -range-size 5 -i "$WORK/p5.aea" -o "$WORK/rg-ora.bin" 2>/dev/null
EXP=$WORK/rg-ora.bin
cell range-0-5 --password "$PW" --range-offset 0 --range-size 5 -i "$WORK/p5.aea"
aea decrypt -password-value "$PW" -range-offset 6 -i "$WORK/p5.aea" -o "$WORK/rg-ora2.bin" 2>/dev/null
EXP=$WORK/rg-ora2.bin
cell range-off-only --password "$PW" --range-offset 6 -i "$WORK/p5.aea"
aea decrypt -password-value "$PW" -range-offset 6 -range-size 0 -i "$WORK/p5.aea" -o "$WORK/rg-ora0.bin" 2>/dev/null
EXP=$WORK/rg-ora0.bin
cell range-size0 --password "$PW" --range-offset 6 --range-size 0 -i "$WORK/p5.aea"
aea decrypt -password-value "$PW" -range-offset 6 -range-size 5 -i "$WORK/pad-def.aea" -o "$WORK/rg-padora.bin" 2>/dev/null
EXP=$WORK/rg-padora.bin
cell range-pad --password "$PW" --range-offset 6 --range-size 5 -i "$WORK/pad-def.aea"
OID=$(aea id -i "$WORK/p5.aea" 2>/dev/null)
PID=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/p5.aea" 2>/dev/null)
if [ "$OID" = "$PID" ] && [ -n "$OID" ]; then ok "id"; else bad "id"; fi
OIDP=$(aea id -i "$WORK/pad-def.aea" 2>/dev/null)
PIDP=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/pad-def.aea" 2>/dev/null)
if [ "$OIDP" = "$PIDP" ] && [ -n "$OIDP" ]; then ok "id-pad"; else bad "id-pad"; fi
head -c 100 "$WORK/p5.aea" > "$WORK/id-tr100.aea"
if "$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/id-tr100.aea" 2>/dev/null; then bad "err-id-trunc100"; else ok "err-id-trunc100"; fi
head -c 155 "$WORK/p5.aea" > "$WORK/id-tr155.aea"
if "$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/id-tr155.aea" 2>/dev/null; then bad "err-id-trunc155"; else ok "err-id-trunc155"; fi
head -c 156 "$WORK/p5.aea" > "$WORK/id-tr156.aea"
OIDT=$(aea id -i "$WORK/id-tr156.aea" 2>/dev/null)
PIDT=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/id-tr156.aea" 2>/dev/null)
if [ "$OIDT" = "$PIDT" ] && [ "$PIDT" = "$OID" ] && [ -n "$OIDT" ]; then ok "id-trunc156"; else bad "id-trunc156"; fi
OIDA=$(aea id -i "$WORK/auth2.aea" 2>/dev/null)
PIDA=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/auth2.aea" 2>/dev/null)
if [ "$OIDA" = "$PIDA" ] && [ -n "$OIDA" ]; then ok "id-auth"; else bad "id-auth"; fi
if (cd "$WORK" && rm -f ./- && "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i - -o iminus.out < "$WORK/p5.aea" 2>/dev/null); then bad "err-iminus"; else ok "err-iminus"; fi

# 8b. thread-count indifference (oracle -t 1 vs default; proto single-threaded)
aea encrypt -profile 5 -password-value "$PW" -a lzma -t 1 -padding none -i "$WORK/bigtext.bin" -o "$WORK/thr1.aea" 2>/dev/null
EXP=$WORK/bigtext.bin
cell threads-t1 --password "$PW" -i "$WORK/thr1.aea"

# 9. error-class parity (exit codes)
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password WRONG -i "$WORK/p5.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-wrongpw"; else ok "err-wrongpw"; fi
head -c 8 "$WORK/p5.aea" > "$WORK/tr8.aea"
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/tr8.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-trunc8"; else ok "err-trunc8"; fi
cp "$WORK/p5.aea" "$WORK/mg.aea" && printf 'Q' | dd of="$WORK/mg.aea" bs=1 seek=0 conv=notrunc 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/mg.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-magic"; else ok "err-magic"; fi
openssl ecparam -name prime256v1 -genkey -noout -out "$WORK/ec2-priv.pem" 2>/dev/null
openssl ec -in "$WORK/ec2-priv.pem" -pubout -out "$WORK/ec2-pub.pem" 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key32.bin" --sign-pub "$WORK/ec2-pub.pem" -i "$WORK/p2.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-wrongsign"; else ok "err-wrongsign"; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --recipient-priv "$WORK/ec-priv.pem" --sign-pub "$WORK/ec2-pub.pem" -i "$WORK/p4.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-p4wrongsign"; else ok "err-p4wrongsign"; fi
aea encrypt -profile 0 -sign-pub "$WORK/ec-pub.pem" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p0u.aea" 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0u.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-unsigned"; else ok "err-unsigned"; fi
cp "$WORK/p0u.aea" "$WORK/p0s.aea" && aea sign -sign-priv "$WORK/ec-priv.pem" -o "$WORK/p0s.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell sign-later --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0s.aea"
head -c 31 /dev/urandom > "$WORK/key31.bin"; head -c 33 /dev/urandom > "$WORK/key33.bin"
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key31.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-key31"; else ok "err-key31"; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key33.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-key33"; else ok "err-key33"; fi
cp "$WORK/p5.aea" "$WORK/ss3.aea" && printf '\003' | dd of="$WORK/ss3.aea" bs=1 seek=7 conv=notrunc 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/ss3.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-strength3"; else ok "err-strength3"; fi
cp "$WORK/p5.aea" "$WORK/ss9.aea" && printf '\011' | dd of="$WORK/ss9.aea" bs=1 seek=7 conv=notrunc 2>/dev/null
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/ss9.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-strength9"; else ok "err-strength9"; fi
printf '%s' "$PW" > "$WORK/pw-exact.txt"; printf '%s\n' "$PW" > "$WORK/pw-nl.txt"
EXP=$WORK/msg.txt
cell pwfile-exact --password-file "$WORK/pw-exact.txt" -i "$WORK/p5.aea"
cell pwfile-nl --password-file "$WORK/pw-nl.txt" -i "$WORK/p5.aea"
SPW='  spaced-battery-password-32ch-abcd  '
aea encrypt -profile 5 -password-value "$SPW" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/sp.aea" 2>/dev/null
printf '%s' "$SPW" > "$WORK/sp-exact.txt"; printf '%s\n' "$SPW" > "$WORK/sp-nl.txt"; printf 'spaced-battery-password-32ch-abcd' > "$WORK/sp-strip.txt"
cell pwspace-value --password "$SPW" -i "$WORK/sp.aea"
cell pwspace-file --password-file "$WORK/sp-exact.txt" -i "$WORK/sp.aea"
cell pwspace-nl --password-file "$WORK/sp-nl.txt" -i "$WORK/sp.aea"
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password-file "$WORK/sp-strip.txt" -i "$WORK/sp.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-pwspace-strip"; else ok "err-pwspace-strip"; fi
cp "$WORK/key32.bin" "$WORK/key32nl.bin" && printf '\n' >> "$WORK/key32nl.bin"
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key32nl.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then bad "err-key32nl"; else ok "err-key32nl"; fi
aea encrypt -profile 1 -key "$WORK/genkey.txt" -key-gen -a none -padding none -i "$WORK/msg.txt" -o "$WORK/gen.aea" 2>/dev/null
cell keygen-file --key "$WORK/genkey.txt" -i "$WORK/gen.aea"

# 9b. block-size flag indifference (same bytes as default @small input)
for b in 64k 1m; do
  aea encrypt -profile 5 -password-value "$PW" -a zlib -b $b -padding none -i "$WORK/msg.txt" -o "$WORK/blk-$b.aea" 2>/dev/null
  EXP=$WORK/msg.txt
  cell block-$b --password "$PW" -i "$WORK/blk-$b.aea"
done

# 10. append
printf 'APPENDED-DATA-BLOCK' > "$WORK/app-in.bin"
cp "$WORK/p5.aea" "$WORK/app.aea"
aea append -password-value "$PW" -i "$WORK/app-in.bin" -o "$WORK/app.aea" 2>/dev/null
cat "$WORK/msg.txt" "$WORK/app-in.bin" > "$WORK/app-exp.bin"
EXP=$WORK/app-exp.bin
cell append --password "$PW" -i "$WORK/app.aea"

# 10b. raw concat: oracle decrypts FIRST archive only (unlike append); proto agrees
printf 'second message\n' > "$WORK/msg2.txt"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -i "$WORK/msg2.txt" -o "$WORK/b.aea" 2>/dev/null
cat "$WORK/p5.aea" "$WORK/b.aea" > "$WORK/cat.aea"
EXP=$WORK/msg.txt
cell concat-first-only --password "$PW" -i "$WORK/cat.aea"

# 10c. stdio paths (oracle: omit -i = stdin, omit -o = stdout, -o - = literal file `-`; APROBE-01/A-001)
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -o "$WORK/stdin.out" < "$WORK/p5.aea" 2>/dev/null \
   && cmp -s "$WORK/stdin.out" "$WORK/msg.txt"; then ok "stdin"; else bad "stdin"; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/p5.aea" > "$WORK/stdout.out" 2>/dev/null \
   && cmp -s "$WORK/stdout.out" "$WORK/msg.txt"; then ok "stdout"; else bad "stdout"; fi
if (cd "$WORK" && "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/p5.aea" -o - 2>/dev/null) \
   && cmp -s "$WORK/-" "$WORK/msg.txt"; then ok "dash-o-literal"; else bad "dash-o-literal"; fi
rm -f "$WORK/-"

echo "PASS=$PASS FAIL=$FAIL"
[ "$FAIL" -eq 0 ]
