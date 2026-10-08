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
oracmp() { # name oracle-decrypt-args... (uses $EXP)
  name=$1; shift
  if aea decrypt "$@" -o "$WORK/out-ora.bin" 2>/dev/null \
     && cmp -s "$WORK/out-ora.bin" "$EXP"; then ok "ora-$name"; else bad "ora-$name"; fi
}

(cd "$REPO/vectors/selfgen" && shasum -c SHA256SUMS >/dev/null 2>&1) || { echo "HARD FAIL pins"; exit 1; }

# 1-2. pinned fixtures
EXP=$REPO/vectors/selfgen/aar/hello-raw.aar
cell pin-p1 --key "$REPO/vectors/selfgen/aea/testkey.bin" -i "$REPO/vectors/selfgen/aea/hello-p1-nopad.aea"
cell pin-p5 --password 'test-password-fixture' -i "$REPO/vectors/selfgen/aea/hello-p5.aea"
oracmp pin-p1 -key "$REPO/vectors/selfgen/aea/testkey.bin" -i "$REPO/vectors/selfgen/aea/hello-p1-nopad.aea"
oracmp pin-p5 -password-value 'test-password-fixture' -i "$REPO/vectors/selfgen/aea/hello-p5.aea"

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
# 4b2. A-014 AEA-transfer: raw bit0 blocks present + verbatim in AEA segs;
# mixtr tail stored at seg level (decomp uncalled -> 1 captured stream)
if "$AEAD_PY" - "$REPO/proto" "$WORK/c-lzraven-mixrt.aea" "$WORK/mixrt.bin" "$WORK/c-lzraven-mixtr.aea" "$WORK/mixtr.bin" "$PW" <<'EOF' 2>/dev/null; then ok "lzraven-raw-verbatim"; else bad "lzraven-raw-verbatim"; fi
import struct, sys
sys.path.insert(0, sys.argv[1])
import aead
cap = []
orig = aead.decomp
def spy(alg, data, size):
    if alg == "m":
        cap.append(bytes(data))
    return orig(alg, data, size)
aead.decomp = spy
def walk(s):
    assert s[:4] == b"\x2b\x00\xca\xec"
    off, out = 8, []
    while True:
        (bh,) = struct.unpack_from("<I", s, off)
        if bh == 0:
            assert off + 4 == len(s)
            return out
        out.append((bh & 0xFFF, s[off+4:off+4+(bh >> 12)]))
        off += 4 + (bh >> 12)
def check(aea_p, plain_p):
    blob = open(plain_p, "rb").read()
    del cap[:]
    assert aead.decrypt_aea(open(aea_p, "rb").read(), password=sys.argv[6]) == blob
    raw = 0
    for d in cap:
        assert d[:4] == b"\x2b\x00\xca\xec"
        for flags, payload in walk(d):
            if flags & 1:
                assert payload in blob
                raw += 1
    return len(cap), raw
n_rt, raw_rt = check(sys.argv[2], sys.argv[3])
n_tr, raw_tr = check(sys.argv[4], sys.argv[5])
assert (n_rt, raw_rt) == (2, 1), (n_rt, raw_rt)
assert (n_tr, raw_tr) == (1, 0), (n_tr, raw_tr)
EOF

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
if aea id -i "$WORK/id-tr100.aea" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/id-tr100.aea" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-id-trunc100"; else bad "err-id-trunc100"; fi
head -c 155 "$WORK/p5.aea" > "$WORK/id-tr155.aea"
if aea id -i "$WORK/id-tr155.aea" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/id-tr155.aea" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-id-trunc155"; else bad "err-id-trunc155"; fi
head -c 156 "$WORK/p5.aea" > "$WORK/id-tr156.aea"
OIDT=$(aea id -i "$WORK/id-tr156.aea" 2>/dev/null)
PIDT=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/id-tr156.aea" 2>/dev/null)
if [ "$OIDT" = "$PIDT" ] && [ "$PIDT" = "$OID" ] && [ -n "$OIDT" ]; then ok "id-trunc156"; else bad "id-trunc156"; fi
OIDA=$(aea id -i "$WORK/auth2.aea" 2>/dev/null)
PIDA=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/auth2.aea" 2>/dev/null)
if [ "$OIDA" = "$PIDA" ] && [ -n "$OIDA" ]; then ok "id-auth"; else bad "id-auth"; fi
if (cd "$WORK" && rm -f ./- && aea decrypt -password-value "$PW" -i - -o iminus-ora.out < "$WORK/p5.aea" 2>/dev/null); then ora=0; else ora=1; fi
if (cd "$WORK" && rm -f ./- && "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i - -o iminus.out < "$WORK/p5.aea" 2>/dev/null); then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-iminus"; else bad "err-iminus"; fi

# 8b. thread-count indifference (oracle -t 1 vs default; proto single-threaded)
aea encrypt -profile 5 -password-value "$PW" -a lzma -t 1 -padding none -i "$WORK/bigtext.bin" -o "$WORK/thr1.aea" 2>/dev/null
EXP=$WORK/bigtext.bin
cell threads-t1 --password "$PW" -i "$WORK/thr1.aea"
oracmp threads-t1 -password-value "$PW" -i "$WORK/thr1.aea"

# 9. error-class parity (exit codes; both sides must reject)
if aea decrypt -password-value WRONG -i "$WORK/p5.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password WRONG -i "$WORK/p5.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-wrongpw"; else bad "err-wrongpw"; fi
head -c 8 "$WORK/p5.aea" > "$WORK/tr8.aea"
if aea decrypt -password-value "$PW" -i "$WORK/tr8.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/tr8.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-trunc8"; else bad "err-trunc8"; fi
cp "$WORK/p5.aea" "$WORK/mg.aea" && printf 'Q' | dd of="$WORK/mg.aea" bs=1 seek=0 conv=notrunc 2>/dev/null
if aea decrypt -password-value "$PW" -i "$WORK/mg.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/mg.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-magic"; else bad "err-magic"; fi
# 9a. profile-byte @4 parity (oracle: 7->`Invalid profile: 7`, 1->`-key required`; APROBE-01)
cp "$WORK/p5.aea" "$WORK/pf7.aea" && printf '\007' | dd of="$WORK/pf7.aea" bs=1 seek=4 conv=notrunc 2>/dev/null
if aea decrypt -password-value "$PW" -i "$WORK/pf7.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/pf7.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-profile7"; else bad "err-profile7"; fi
cp "$WORK/p5.aea" "$WORK/pf1.aea" && printf '\001' | dd of="$WORK/pf1.aea" bs=1 seek=4 conv=notrunc 2>/dev/null
if aea decrypt -password-value "$PW" -i "$WORK/pf1.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/pf1.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-profile1"; else bad "err-profile1"; fi
openssl ecparam -name prime256v1 -genkey -noout -out "$WORK/ec2-priv.pem" 2>/dev/null
openssl ec -in "$WORK/ec2-priv.pem" -pubout -out "$WORK/ec2-pub.pem" 2>/dev/null
if aea decrypt -key "$WORK/key32.bin" -sign-pub "$WORK/ec2-pub.pem" -i "$WORK/p2.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key32.bin" --sign-pub "$WORK/ec2-pub.pem" -i "$WORK/p2.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-wrongsign"; else bad "err-wrongsign"; fi
if aea decrypt -recipient-priv "$WORK/ec-priv.pem" -sign-pub "$WORK/ec2-pub.pem" -i "$WORK/p4.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --recipient-priv "$WORK/ec-priv.pem" --sign-pub "$WORK/ec2-pub.pem" -i "$WORK/p4.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-p4wrongsign"; else bad "err-p4wrongsign"; fi
# 9b. EC-curve parity: oracle P-256-only (encrypt rejects 384/521 pubs,
# decrypt exits 1 on 384/521 creds); proto exits 1 too. APROBE-01.
for spec in 384:secp384r1 521:secp521r1; do
  tag=${spec%%:*}; curve=${spec##*:}
  openssl ecparam -name $curve -genkey -noout -out "$WORK/ec-$tag-priv.pem" 2>/dev/null
  openssl ec -in "$WORK/ec-$tag-priv.pem" -pubout -out "$WORK/ec-$tag-pub.pem" 2>/dev/null
  if aea decrypt -recipient-priv "$WORK/ec-$tag-priv.pem" -i "$WORK/p3.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --recipient-priv "$WORK/ec-$tag-priv.pem" -i "$WORK/p3.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
  if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-rec-$tag"; else bad "err-rec-$tag"; fi
  if aea decrypt -sign-pub "$WORK/ec-$tag-pub.pem" -i "$WORK/p0.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --sign-pub "$WORK/ec-$tag-pub.pem" -i "$WORK/p0.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
  if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-sign-$tag"; else bad "err-sign-$tag"; fi
done
aea encrypt -profile 0 -sign-pub "$WORK/ec-pub.pem" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/p0u.aea" 2>/dev/null
if aea decrypt -sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0u.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0u.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-unsigned"; else bad "err-unsigned"; fi
OIDU=$(aea id -i "$WORK/p0u.aea" 2>/dev/null)
PIDU=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/p0u.aea" 2>/dev/null)
if [ "$OIDU" = "$PIDU" ] && [ -n "$OIDU" ]; then ok "id-unsigned"; else bad "id-unsigned"; fi
aea decrypt -password-value "$PW" -range-offset 0 -range-size 5 -i "$WORK/auth2.aea" -o "$WORK/rg-auth.bin" 2>/dev/null
EXP=$WORK/rg-auth.bin
cell range-auth --password "$PW" --range-offset 0 --range-size 5 -i "$WORK/auth2.aea"
cp "$WORK/p0u.aea" "$WORK/p0s.aea" && aea sign -sign-priv "$WORK/ec-priv.pem" -o "$WORK/p0s.aea" 2>/dev/null
EXP=$WORK/msg.txt
cell sign-later --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0s.aea"
oracmp sign-later -sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0s.aea"
head -c 31 /dev/urandom > "$WORK/key31.bin"; head -c 33 /dev/urandom > "$WORK/key33.bin"
if aea decrypt -key "$WORK/key31.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key31.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-key31"; else bad "err-key31"; fi
EXP=$WORK/msg.txt
cell mixed-p1-pwextra --key "$WORK/key32.bin" --password "$PW" -i "$WORK/p1.aea"
cell mixed-p5-keyextra --password "$PW" --key "$WORK/key32.bin" -i "$WORK/p5.aea"
if aea decrypt -i "$WORK/p5.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt -i "$WORK/p5.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-no-creds"; else bad "err-no-creds"; fi
if aea decrypt -password-value "$PW" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-wrong-credtype"; else bad "err-wrong-credtype"; fi
if aea decrypt -key "$WORK/key33.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key33.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-key33"; else bad "err-key33"; fi
# NOTE: seek=7 is the profile-u32 HIGH byte, not a strength field (APROBE-01
# byte map); err-strength* names kept for history. Oracle: exit 1 unlock-class.
cp "$WORK/p5.aea" "$WORK/ss3.aea" && printf '\003' | dd of="$WORK/ss3.aea" bs=1 seek=7 conv=notrunc 2>/dev/null
if aea decrypt -password-value "$PW" -i "$WORK/ss3.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/ss3.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-strength3"; else bad "err-strength3"; fi
cp "$WORK/p5.aea" "$WORK/ss9.aea" && printf '\011' | dd of="$WORK/ss9.aea" bs=1 seek=7 conv=notrunc 2>/dev/null
if aea decrypt -password-value "$PW" -i "$WORK/ss9.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/ss9.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-strength9"; else bad "err-strength9"; fi
printf '%s' "$PW" > "$WORK/pw-exact.txt"; printf '%s\n' "$PW" > "$WORK/pw-nl.txt"
EXP=$WORK/msg.txt
cell pwfile-exact --password-file "$WORK/pw-exact.txt" -i "$WORK/p5.aea"
cell pwfile-nl --password-file "$WORK/pw-nl.txt" -i "$WORK/p5.aea"
printf '%s\r\n' "$PW" > "$WORK/pw-crlf.txt"
cell pwfile-crlf --password-file "$WORK/pw-crlf.txt" -i "$WORK/p5.aea"
printf '%s\n\n' "$PW" > "$WORK/pw-2nl.txt"
cell pwfile-2nl --password-file "$WORK/pw-2nl.txt" -i "$WORK/p5.aea"
# oracle -password <file> is the file form (proto --password-file); both must MATCH
oracmp pwfile-exact -password "$WORK/pw-exact.txt" -i "$WORK/p5.aea"
oracmp pwfile-nl -password "$WORK/pw-nl.txt" -i "$WORK/p5.aea"
oracmp pwfile-crlf -password "$WORK/pw-crlf.txt" -i "$WORK/p5.aea"
oracmp pwfile-2nl -password "$WORK/pw-2nl.txt" -i "$WORK/p5.aea"
for coff in 50 200 1000; do
  cp "$WORK/pad-def.aea" "$WORK/padc-$coff.aea"
  python3 -c "import sys;p=sys.argv[1];o=int(sys.argv[2]);b=bytearray(open(p,'rb').read());b[o]^=0xFF;open(p,'wb').write(bytes(b))" "$WORK/padc-$coff.aea" "$coff"
  if aea decrypt -password-value "$PW" -i "$WORK/padc-$coff.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/padc-$coff.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
  if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-padcorr-$coff"; else bad "err-padcorr-$coff"; fi
done
# 9c. pad edges: verified range [padstart,arc); trailing bytes ignored; short pad rejected
cp "$WORK/pad-def.aea" "$WORK/pad-plus1.aea" && printf 'Z' >> "$WORK/pad-plus1.aea"
EXP=$WORK/msg.txt
cell pad-plus1 --password "$PW" -i "$WORK/pad-plus1.aea"
oracmp pad-plus1 -password-value "$PW" -i "$WORK/pad-plus1.aea"
head -c $(($(wc -c < "$WORK/pad-def.aea")-100)) "$WORK/pad-def.aea" > "$WORK/pad-short.aea"
if aea decrypt -password-value "$PW" -i "$WORK/pad-short.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/pad-short.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-pad-short"; else bad "err-pad-short"; fi
: > "$WORK/empty.bin"
aea encrypt -profile 5 -password-value "$PW" -a none -i "$WORK/empty.bin" -o "$WORK/e-pad.aea" 2>/dev/null
head -c $(($(wc -c < "$WORK/e-pad.aea")-2)) "$WORK/e-pad.aea" > "$WORK/e-short2.aea"
if aea decrypt -password-value "$PW" -i "$WORK/e-short2.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/e-short2.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-pad-short-empty"; else bad "err-pad-short-empty"; fi
# 9e. pad-CONTENT flips (A-016B verify-or-reject; both must reject, fail-closed)
PSTART=$(($(wc -c < "$WORK/msg.txt")+18620))
cp "$WORK/pad-def.aea" "$WORK/pad-flip.aea"
python3 -c "import sys;p=sys.argv[1];o=int(sys.argv[2]);b=bytearray(open(p,'rb').read());b[o]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/pad-flip.aea" "$PSTART"
if aea decrypt -password-value "$PW" -i "$WORK/pad-flip.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/pad-flip.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-pad-flip"; else bad "err-pad-flip"; fi
cp "$WORK/e-pad.aea" "$WORK/e-flip.aea"
python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[158]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/e-flip.aea"
if aea decrypt -password-value "$PW" -i "$WORK/e-flip.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/e-flip.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-pad-flipe"; else bad "err-pad-flipe"; fi
# 9f. pad-verify across profiles (p0 default emits padlen 0 -> vacuous skip; explicit pad works)
aea encrypt -profile 0 -sign-priv "$WORK/ec-priv.pem" -a none -padding 4096 -i "$WORK/msg.txt" -o "$WORK/pp0.aea" 2>/dev/null
cp "$WORK/pp0.aea" "$WORK/ppf0.aea"
python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[-1]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/ppf0.aea"
if aea decrypt -sign-pub "$WORK/ec-pub.pem" -i "$WORK/ppf0.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --sign-pub "$WORK/ec-pub.pem" -i "$WORK/ppf0.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-padflip-p0"; else bad "err-padflip-p0"; fi
aea encrypt -profile 1 -key "$WORK/key32.bin" -a none -i "$WORK/msg.txt" -o "$WORK/pp1.aea" 2>/dev/null
aea encrypt -profile 2 -key "$WORK/key32.bin" -sign-priv "$WORK/ec-priv.pem" -a none -i "$WORK/msg.txt" -o "$WORK/pp2.aea" 2>/dev/null
aea encrypt -profile 3 -recipient-pub "$WORK/ec-pub.pem" -a none -i "$WORK/msg.txt" -o "$WORK/pp3.aea" 2>/dev/null
aea encrypt -profile 4 -recipient-pub "$WORK/ec-pub.pem" -sign-priv "$WORK/ec-priv.pem" -a none -i "$WORK/msg.txt" -o "$WORK/pp4.aea" 2>/dev/null
for p in 1 2 3 4; do
  case $p in
    1) OC="-key $WORK/key32.bin"; PC="--key $WORK/key32.bin";;
    2) OC="-key $WORK/key32.bin -sign-pub $WORK/ec-pub.pem"; PC="--key $WORK/key32.bin --sign-pub $WORK/ec-pub.pem";;
    3) OC="-recipient-priv $WORK/ec-priv.pem"; PC="--recipient-priv $WORK/ec-priv.pem";;
    4) OC="-recipient-priv $WORK/ec-priv.pem -sign-pub $WORK/ec-pub.pem"; PC="--recipient-priv $WORK/ec-priv.pem --sign-pub $WORK/ec-pub.pem";;
  esac
  cp "$WORK/pp$p.aea" "$WORK/ppf$p.aea"
  python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[-1]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/ppf$p.aea"
  # shellcheck disable=SC2086
  if aea decrypt $OC -i "$WORK/ppf$p.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
  # shellcheck disable=SC2086
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt $PC -i "$WORK/ppf$p.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
  if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-padflip-p$p"; else bad "err-padflip-p$p"; fi
done
# 9d. A-017 R1/R2 regression bed (8 tag/data flips; both sides reject via real HMAC checks)
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -checksum sha256 -i "$WORK/msg.txt" -o "$WORK/a17.aea" 2>/dev/null
for off in 50 80 130 200 10396 10428 10460 18620; do
  cp "$WORK/a17.aea" "$WORK/a17f.aea"
  python3 -c "import sys;p=sys.argv[1];o=int(sys.argv[2]);b=bytearray(open(p,'rb').read());b[o]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/a17f.aea" "$off"
  if aea decrypt -password-value "$PW" -i "$WORK/a17f.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/a17f.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
  if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-a17-$off"; else bad "err-a17-$off"; fi
done
KHEX=$(python3 -c "import sys;print(sys.stdin.buffer.read().hex())" < "$WORK/key32.bin")
KB64=$(python3 -c "import sys,base64;print(base64.b64encode(sys.stdin.buffer.read()).decode())" < "$WORK/key32.bin")
EXP=$WORK/msg.txt
cell keyval-hex --key-value "hex:$KHEX" -i "$WORK/p1.aea"
cell keyval-b64 --key-value "base64:$KB64" -i "$WORK/p1.aea"
oracmp keyval-hex -key-value "hex:$KHEX" -i "$WORK/p1.aea"
oracmp keyval-b64 -key-value "base64:$KB64" -i "$WORK/p1.aea"
if aea decrypt -key-value "$KHEX" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key-value "$KHEX" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-kv-bare"; else bad "err-kv-bare"; fi
if aea decrypt -key-value "0x$KHEX" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key-value "0x$KHEX" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-kv-0x"; else bad "err-kv-0x"; fi
SPW='  spaced-battery-password-32ch-abcd  '
aea encrypt -profile 5 -password-value "$SPW" -a none -padding none -i "$WORK/msg.txt" -o "$WORK/sp.aea" 2>/dev/null
printf '%s' "$SPW" > "$WORK/sp-exact.txt"; printf '%s\n' "$SPW" > "$WORK/sp-nl.txt"; printf 'spaced-battery-password-32ch-abcd' > "$WORK/sp-strip.txt"
cell pwspace-value --password "$SPW" -i "$WORK/sp.aea"
cell pwspace-file --password-file "$WORK/sp-exact.txt" -i "$WORK/sp.aea"
cell pwspace-nl --password-file "$WORK/sp-nl.txt" -i "$WORK/sp.aea"
oracmp pwspace-value -password-value "$SPW" -i "$WORK/sp.aea"
oracmp pwspace-file -password "$WORK/sp-exact.txt" -i "$WORK/sp.aea"
oracmp pwspace-nl -password "$WORK/sp-nl.txt" -i "$WORK/sp.aea"
if aea decrypt -password "$WORK/sp-strip.txt" -i "$WORK/sp.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password-file "$WORK/sp-strip.txt" -i "$WORK/sp.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-pwspace-strip"; else bad "err-pwspace-strip"; fi
cp "$WORK/key32.bin" "$WORK/key32nl.bin" && printf '\n' >> "$WORK/key32nl.bin"
if aea decrypt -key "$WORK/key32nl.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$WORK/key32nl.bin" -i "$WORK/p1.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-key32nl"; else bad "err-key32nl"; fi
aea encrypt -profile 1 -key "$WORK/genkey.txt" -key-gen -a none -padding none -i "$WORK/msg.txt" -o "$WORK/gen.aea" 2>/dev/null
cell keygen-file --key "$WORK/genkey.txt" -i "$WORK/gen.aea"
if [ "$(wc -c < "$WORK/genkey.txt")" -eq 69 ] && head -c 4 "$WORK/genkey.txt" | grep -q "hex:"; then ok "keygen-format"; else bad "keygen-format"; fi
if aea decrypt -key "$WORK/genkey.txt" -i "$WORK/gen.aea" -o "$WORK/out.bin" 2>/dev/null && cmp -s "$WORK/out.bin" "$WORK/msg.txt"; then ok "keygen-oracle"; else bad "keygen-oracle"; fi

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
oracmp append -password-value "$PW" -i "$WORK/app.aea"

# 10b. raw concat: oracle decrypts FIRST archive only (unlike append); proto agrees
printf 'second message\n' > "$WORK/msg2.txt"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -i "$WORK/msg2.txt" -o "$WORK/b.aea" 2>/dev/null
cat "$WORK/p5.aea" "$WORK/b.aea" > "$WORK/cat.aea"
EXP=$WORK/msg.txt
cell concat-first-only --password "$PW" -i "$WORK/cat.aea"
oracmp concat-first-only -password-value "$PW" -i "$WORK/cat.aea"

# 10c. stdio paths (oracle: omit -i = stdin, omit -o = stdout, -o - = literal file `-`; APROBE-01/A-001)
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -o "$WORK/stdin.out" < "$WORK/p5.aea" 2>/dev/null \
   && cmp -s "$WORK/stdin.out" "$WORK/msg.txt"; then ok "stdin"; else bad "stdin"; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/p5.aea" > "$WORK/stdout.out" 2>/dev/null \
   && cmp -s "$WORK/stdout.out" "$WORK/msg.txt"; then ok "stdout"; else bad "stdout"; fi
if (cd "$WORK" && "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/p5.aea" -o - 2>/dev/null) \
   && cmp -s "$WORK/-" "$WORK/msg.txt"; then ok "dash-o-literal"; else bad "dash-o-literal"; fi
rm -f "$WORK/-"
if aea decrypt -password-value "$PW" -o "$WORK/ostdin.out" < "$WORK/p5.aea" 2>/dev/null \
   && cmp -s "$WORK/ostdin.out" "$WORK/msg.txt"; then ok "ora-stdin"; else bad "ora-stdin"; fi
if aea decrypt -password-value "$PW" -i "$WORK/p5.aea" > "$WORK/ostdout.out" 2>/dev/null \
   && cmp -s "$WORK/ostdout.out" "$WORK/msg.txt"; then ok "ora-stdout"; else bad "ora-stdout"; fi
if (cd "$WORK" && aea decrypt -password-value "$PW" -i "$WORK/p5.aea" -o - 2>/dev/null) \
   && cmp -s "$WORK/-" "$WORK/msg.txt"; then ok "ora-dash-o-literal"; else bad "ora-dash-o-literal"; fi
rm -f "$WORK/-"

# 11. A-019 G1: multi-cluster cells (p5/-a none/sha256/pad-none; own APROBE-103 walk)
head -c 268435457 /dev/zero > "$WORK/z2.bin"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -checksum sha256 -i "$WORK/z2.bin" -o "$WORK/mc2.aea" 2>/dev/null
if [ "$(wc -c < "$WORK/mc2.aea" | tr -d ' ')" -eq 268472541 ]; then ok "mc2-size"; else bad "mc2-size"; fi
EXP=$WORK/z2.bin
cell mc2-happy --password "$PW" -i "$WORK/mc2.aea"
oracmp mc2-happy -password-value "$PW" -i "$WORK/mc2.aea"
# C1 = [0,268454076): prologue 156 + table 18464 + 256MiB payload; C2 hdr follows
cp "$WORK/mc2.aea" "$WORK/mc2f-hdr.aea"
python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[5000]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/mc2f-hdr.aea"
if aea decrypt -password-value "$PW" -i "$WORK/mc2f-hdr.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/mc2f-hdr.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-mc2-c1hdr"; else bad "err-mc2-c1hdr"; fi
cp "$WORK/mc2.aea" "$WORK/mc2f-seg.aea"
python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[1067195]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/mc2f-seg.aea"
if aea decrypt -password-value "$PW" -i "$WORK/mc2f-seg.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/mc2f-seg.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-mc2-c1seg"; else bad "err-mc2-c1seg"; fi
cp "$WORK/mc2.aea" "$WORK/mc2f-end.aea"
python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[268454075]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/mc2f-end.aea"
if aea decrypt -password-value "$PW" -i "$WORK/mc2f-end.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/mc2f-end.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-mc2-c1end"; else bad "err-mc2-c1end"; fi
# MT thread-shape: default-threads MT stanza (0x9e05cc00) vs -t1 single-thread (0xde108400); exits agree
aea decrypt -password-value "$PW" -i "$WORK/mc2f-hdr.aea" -o "$WORK/out.bin" 2>"$WORK/mt-def.err"; edef=$?
aea decrypt -t 1 -password-value "$PW" -i "$WORK/mc2f-hdr.aea" -o "$WORK/out.bin" 2>"$WORK/mt-t1.err"; et1=$?
if [ $edef -eq 1 ] && [ $et1 -eq 1 ] \
   && grep -q '0x9e05cc00' "$WORK/mt-def.err" && grep -q '0xde108400' "$WORK/mt-t1.err" \
   && ! cmp -s "$WORK/mt-def.err" "$WORK/mt-t1.err"; then ok "ora-mt-threadshape"; else bad "ora-mt-threadshape"; fi
head -c 536870913 /dev/zero > "$WORK/z3.bin"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -checksum sha256 -i "$WORK/z3.bin" -o "$WORK/mc3.aea" 2>/dev/null
if [ "$(wc -c < "$WORK/mc3.aea" | tr -d ' ')" -eq 536926461 ]; then ok "mc3-size"; else bad "mc3-size"; fi
EXP=$WORK/z3.bin
cell mc3-happy --password "$PW" -i "$WORK/mc3.aea"
oracmp mc3-happy -password-value "$PW" -i "$WORK/mc3.aea"

# 12. A-019 G2: conforming-but-unpinned shapes
cp "$WORK/p5.aea" "$WORK/pf6.aea" && printf '\006' | dd of="$WORK/pf6.aea" bs=1 seek=4 conv=notrunc 2>/dev/null
if aea decrypt -password-value "$PW" -i "$WORK/pf6.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/pf6.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-profile6"; else bad "err-profile6"; fi
cp "$WORK/p5.aea" "$WORK/pad-plus1u.aea" && printf 'Z' >> "$WORK/pad-plus1u.aea"
EXP=$WORK/msg.txt
cell pad-plus1-unpadded --password "$PW" -i "$WORK/pad-plus1u.aea"
oracmp pad-plus1-unpadded -password-value "$PW" -i "$WORK/pad-plus1u.aea"
EXP=$WORK/empty.bin
cell range-past-eof --password "$PW" --range-offset 999999999 -i "$WORK/p5.aea"
oracmp range-past-eof -password-value "$PW" -range-offset 999999999 -i "$WORK/p5.aea"
EXP=$WORK/msg.txt
cell range-huge --password "$PW" --range-offset 0 --range-size 999999 -i "$WORK/p5.aea"
oracmp range-huge -password-value "$PW" -range-offset 0 -range-size 999999 -i "$WORK/p5.aea"
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/p5.aea" -o /dev/null 2>/dev/null; then ok "devnull"; else bad "devnull"; fi
if aea decrypt -password-value "$PW" -i "$WORK/p5.aea" -o /dev/null 2>/dev/null; then ok "ora-devnull"; else bad "ora-devnull"; fi
cp "$WORK/p5.aea" "$WORK/segf-null.aea"
python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[200]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/segf-null.aea"
if aea decrypt -password-value "$PW" -i "$WORK/segf-null.aea" -o /dev/null 2>/dev/null; then ora=0; else ora=1; fi
if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/segf-null.aea" -o /dev/null 2>/dev/null; then pro=0; else pro=1; fi
if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-devnull-segf"; else bad "err-devnull-segf"; fi
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -auth-data-value hex:deadbeef -i "$WORK/empty.bin" -o "$WORK/eauth.aea" 2>/dev/null
EXP=$WORK/empty.bin
cell empty-auth --password "$PW" -i "$WORK/eauth.aea"
oracmp empty-auth -password-value "$PW" -i "$WORK/eauth.aea"
for aoff in 20 100 150; do
  cp "$WORK/auth2.aea" "$WORK/authf.aea"
  python3 -c "import sys;p=sys.argv[1];o=int(sys.argv[2]);b=bytearray(open(p,'rb').read());b[o]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/authf.aea" "$aoff"
  if aea decrypt -password-value "$PW" -i "$WORK/authf.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$WORK/authf.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
  if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-authflip-$aoff"; else bad "err-authflip-$aoff"; fi
done
for soff in 1000 5000; do
  cp "$WORK/p0.aea" "$WORK/p0f.aea"
  python3 -c "import sys;p=sys.argv[1];o=int(sys.argv[2]);b=bytearray(open(p,'rb').read());b[o]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/p0f.aea" "$soff"
  if aea decrypt -sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0f.aea" -o "$WORK/out.bin" 2>/dev/null; then ora=0; else ora=1; fi
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0f.aea" -o "$WORK/out.bin" 2>/dev/null; then pro=0; else pro=1; fi
  if [ $ora -eq 1 ] && [ $pro -eq 1 ]; then ok "err-p0sig-$soff"; else bad "err-p0sig-$soff"; fi
done
cp "$WORK/p0.aea" "$WORK/p0sp.aea"
python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[100]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/p0sp.aea"
EXP=$WORK/msg.txt
cell p0-spare-100 --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0sp.aea"
oracmp p0-spare-100 -sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0sp.aea"
# -t1 decrypt invariance (single-cluster): exits + stderr + bytes identical, 5 shapes
cp "$WORK/p5.aea" "$WORK/t1-segf.aea"
python3 -c "import sys;p=sys.argv[1];b=bytearray(open(p,'rb').read());b[200]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/t1-segf.aea"
cp "$WORK/pad-def.aea" "$WORK/t1-padf.aea"
python3 -c "import sys;p=sys.argv[1];o=int(sys.argv[2]);b=bytearray(open(p,'rb').read());b[o]^=0x01;open(p,'wb').write(bytes(b))" "$WORK/t1-padf.aea" "$PSTART"
for shape in happy:p5.aea:good wrongpw:p5.aea:bad trunc8:tr8.aea:good segflip:t1-segf.aea:good padflip:t1-padf.aea:good; do
  nm=${shape%%:*}; rest=${shape#*:}; fn=${rest%%:*}; pwk=${rest##*:}
  if [ "$pwk" = bad ]; then PWA=WRONG; else PWA=$PW; fi
  aea decrypt -password-value "$PWA" -i "$WORK/$fn" -o "$WORK/t1-o1.bin" 2>"$WORK/t1-s1"; e1=$?
  aea decrypt -t 1 -password-value "$PWA" -i "$WORK/$fn" -o "$WORK/t1-o2.bin" 2>"$WORK/t1-s2"; e2=$?
  if [ $e1 -eq $e2 ] && cmp -s "$WORK/t1-s1" "$WORK/t1-s2" && cmp -s "$WORK/t1-o1.bin" "$WORK/t1-o2.bin" 2>/dev/null; then ok "ora-t1-ident-$nm"; else bad "ora-t1-ident-$nm"; fi
done

echo "PASS=$PASS FAIL=$FAIL"
[ "$FAIL" -eq 0 ]
