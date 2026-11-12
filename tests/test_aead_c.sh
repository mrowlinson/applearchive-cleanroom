#!/bin/sh
# test_aead_c.sh — committed C-parity gate for aeadc (the C port of proto/aead.py).
# Bed-style like test_lz4_c.sh. ZERO Python on legs 1-6 (sh + `aea` oracle +
# unified-binary `aeadc` passthrough + openssl + dd/xxd/od/awk/cmp only;
# no uv, no python-lz4, no venv).
# Leg 7 runs the full tests/test_aea_enc.sh suite via tests/aeadc-shim.sh; its
# only python usage is struct/sys/base64 byte-slicing of oracle blobs by the
# suite itself (system python3 suffices; no lz4/cryptography modules needed).
#
# UNIFIED MAPPING (cport-unify): every old `"$AEADC" <args>` cell is now
# `"$CLI" aeadc <args>` — same argv into the same aead_main, same bytes,
# same exits, same stderr. The native `aeadc` passthrough is used (NOT
# aea-encrypt/aea-decrypt) because transplant --fixed-* flags, stdio
# positionals, and selftest have no aea-* equivalents; translation would
# change bytes/exits. Cell count and oracle comparisons unchanged.
#
# usage: sh tests/test_aead_c.sh [workdir]
# Env: CLI (default WS unified build), AEA (default /usr/bin/aea).
# Exit 0 ALL-GREEN, 1 RED. Counts 1 battery run.
#
# aea-battery.sh backend mapping (acceptance d): every cell where the battery
# shells to proto aead.py decrypt/id is flipped to aeadc here and MUST agree
# with the oracle. Cells that stay oracle-only (no proto backend involved):
# setups (keygen/sign/append/threaded encrypts), oracmp (oracle-vs-oracle),
# cksum-enforced + lzraven-raw-verbatim (import proto.aead as a module —
# whitebox; covered here by tamper cells + selftest instead), MT stanza
# string cells (oracle stderr text), size cells (byte counts, backend-free).
# Flipped here: all 6 profiles both directions, all codecs both directions
# (lzbitmap/lzraven oracle->C only — v1 has no encoder, same as proto),
# transplant byte-identity (p1/p5), every err/* cell shape, padcorr flips,
# strength flips, range, stdio, pwfile/keyval forms, id (+auth), multi-cluster
# chaining (C->oracle proven; oracle 1M-block 2-cluster blobs decrypt under C
# in the full aea-battery flip, not repeated here).
set -u
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
AEA=${AEA:-/usr/bin/aea}
CLI=${CLI:-/Volumes/NVME/applearchive-cleanroom-ws/build/unified/aae-cli}
HERE=$(dirname "$0")
WORK=${1:-$TMPDIR/aeadc-bed-$$}
mkdir -p "$WORK"
fail=0
npass=0
ok() { npass=$((npass+1)); echo "PASS $1"; }
bad() { fail=1; echo "FAIL $1"; }
[ -x "$CLI" ] || { echo "FAIL missing unified binary: $CLI (CLI=...)"; exit 1; }
[ -x "$AEA" ] || { echo "FAIL missing oracle aea: $AEA"; exit 1; }
command -v openssl >/dev/null || { echo "FAIL missing openssl"; exit 1; }

# fixtures (no python): 80B msg, 3B, empty, ~3MB text, 17MB multi
printf 'The quick brown fox jumps over the lazy dog. 0123456789. ' > "$WORK/msg.txt"
printf 'hi!' > "$WORK/three.bin"
: > "$WORK/empty.bin"
awk 'BEGIN{for(i=0;i<60000;i++)printf "line %05d The quick brown fox jumps over the lazy dog.\n", i}' > "$WORK/big.txt"
head -c 17408000 /dev/urandom > "$WORK/multi.bin"
PW="pw-20-bytes-long-ok!!"
head -c 32 /dev/urandom > "$WORK/key32.bin"
openssl ecparam -name prime256v1 -genkey -noout -out "$WORK/ec-priv.pem" 2>/dev/null
openssl ec -in "$WORK/ec-priv.pem" -pubout -out "$WORK/ec-pub.pem" 2>/dev/null
openssl ecparam -name secp384r1 -genkey -noout -out "$WORK/ec384-priv.pem" 2>/dev/null
openssl ec -in "$WORK/ec384-priv.pem" -pubout -out "$WORK/ec384-pub.pem" 2>/dev/null
SALT32="ab00000000000000000000000000000000000000000000000000000000000000"

flipbyte() { # $1=file $2=offset: byte = (byte+1)%256 via dd
  _b=$(od -A n -t u1 -j "$2" -N 1 "$1" | tr -d ' \n')
  _n=$(( (_b + 1) % 256 ))
  _o=$(printf '%03o' "$_n")
  printf "\\$_o" | dd of="$1" bs=1 seek="$2" conv=notrunc 2>/dev/null
}

echo "== leg1 selftest (test_aead_units.py logic as C asserts)"
if "$CLI" aeadc selftest > "$WORK/selftest.log" 2>&1; then ok selftest; else bad selftest; fi
grep -q "SELFTEST 97/97 PASS" "$WORK/selftest.log" 2>/dev/null || bad selftest-count

echo "== leg2 pins (vectors/selfgen/aea decrypt == vectors/selfgen/aar/hello-raw.aar)"
REPO=$(cd "$HERE/.." && pwd)
for v in hello-p1-nopad hello-p5; do
  if [ "$v" = "hello-p1-nopad" ]; then
    "$CLI" aeadc decrypt --key "$REPO/vectors/selfgen/aea/testkey.bin" -i "$REPO/vectors/selfgen/aea/$v.aea" -o "$WORK/$v.out" 2>"$WORK/$v.err"
  else
    "$CLI" aeadc decrypt --password 'test-password-fixture' -i "$REPO/vectors/selfgen/aea/$v.aea" -o "$WORK/$v.out" 2>"$WORK/$v.err"
  fi
  if [ $? -eq 0 ] && cmp -s "$WORK/$v.out" "$REPO/vectors/selfgen/aar/hello-raw.aar"; then ok "pin-$v"; else bad "pin-$v"; fi
done

echo "== leg3 profiles 0-5 (C->C, C->oracle, oracle->C on msg)"
for p in 0 1 2 3 4 5; do
  extra=""; dextra=""
  case $p in
    0) extra="--sign-priv $WORK/ec-priv.pem"; dextra="--sign-pub $WORK/ec-pub.pem" ;;
    1) extra="--key $WORK/key32.bin"; dextra="--key $WORK/key32.bin" ;;
    2) extra="--key $WORK/key32.bin --sign-priv $WORK/ec-priv.pem"; dextra="--key $WORK/key32.bin --sign-pub $WORK/ec-pub.pem" ;;
    3) extra="--recipient-pub $WORK/ec-pub.pem"; dextra="--recipient-priv $WORK/ec-priv.pem" ;;
    4) extra="--recipient-pub $WORK/ec-pub.pem --sign-priv $WORK/ec-priv.pem"; dextra="--recipient-priv $WORK/ec-priv.pem --sign-pub $WORK/ec-pub.pem" ;;
    5) extra="--password $PW"; dextra="--password $PW" ;;
  esac
  "$CLI" aeadc encrypt --profile $p $extra -a none --checksum sha256 --padding none -i "$WORK/msg.txt" -o "$WORK/p$p-c.aea" 2>/dev/null || { bad "enc-p$p"; continue; }
  "$CLI" aeadc decrypt $dextra -i "$WORK/p$p-c.aea" -o "$WORK/p$p-cc.out" 2>/dev/null && cmp -s "$WORK/p$p-cc.out" "$WORK/msg.txt" && ok "p$p-rt" || bad "p$p-rt"
  # oracle cross: profile flags are oracle-style (-profile/-password-value/-key)
  oextra=""
  case $p in
    0) oextra="-sign-pub $WORK/ec-pub.pem" ;;
    1) oextra="-key $WORK/key32.bin" ;;
    2) oextra="-key $WORK/key32.bin -sign-pub $WORK/ec-pub.pem" ;;
    3) oextra="-recipient-priv $WORK/ec-priv.pem" ;;
    4) oextra="-recipient-priv $WORK/ec-priv.pem -sign-pub $WORK/ec-pub.pem" ;;
    5) oextra="-password-value $PW" ;;
  esac
  "$AEA" decrypt $oextra -i "$WORK/p$p-c.aea" -o "$WORK/p$p-co.out" 2>/dev/null && cmp -s "$WORK/p$p-co.out" "$WORK/msg.txt" && ok "p$p-c2ora" || bad "p$p-c2ora"
  case $p in
    0) "$AEA" encrypt -profile $p -sign-priv "$WORK/ec-priv.pem" -a none -i "$WORK/msg.txt" -o "$WORK/p$p-o.aea" 2>/dev/null ;;
    1) "$AEA" encrypt -profile $p -key "$WORK/key32.bin" -a none -i "$WORK/msg.txt" -o "$WORK/p$p-o.aea" 2>/dev/null ;;
    2) "$AEA" encrypt -profile $p -key "$WORK/key32.bin" -sign-priv "$WORK/ec-priv.pem" -a none -i "$WORK/msg.txt" -o "$WORK/p$p-o.aea" 2>/dev/null ;;
    3) "$AEA" encrypt -profile $p -recipient-pub "$WORK/ec-pub.pem" -a none -i "$WORK/msg.txt" -o "$WORK/p$p-o.aea" 2>/dev/null ;;
    4) "$AEA" encrypt -profile $p -recipient-pub "$WORK/ec-pub.pem" -sign-priv "$WORK/ec-priv.pem" -a none -i "$WORK/msg.txt" -o "$WORK/p$p-o.aea" 2>/dev/null ;;
    5) "$AEA" encrypt -profile $p -password-value "$PW" -a none -i "$WORK/msg.txt" -o "$WORK/p$p-o.aea" 2>/dev/null ;;
  esac
  "$CLI" aeadc decrypt $dextra -i "$WORK/p$p-o.aea" -o "$WORK/p$p-oc.out" 2>/dev/null && cmp -s "$WORK/p$p-oc.out" "$WORK/msg.txt" && ok "p$p-ora2c" || bad "p$p-ora2c"
done

echo "== leg4b lz4 tail literals (tail>=15 roundtrip; fuzzer regression: tail literals >=15 were silently truncated) =="
for _tsz in 15 16 31 9000; do
  head -c "$_tsz" /dev/urandom > "$WORK/tail-$_tsz.bin" 2>/dev/null || { bad "tail-$_tsz-gen"; continue; }
  if "$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" -a lz4 -i "$WORK/tail-$_tsz.bin" -o "$WORK/tail-$_tsz.aea" 2>/dev/null \
     && "$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/tail-$_tsz.aea" -o "$WORK/tail-$_tsz.out" 2>/dev/null \
     && cmp -s "$WORK/tail-$_tsz.out" "$WORK/tail-$_tsz.bin"; then ok "tail-$_tsz";
  else bad "tail-$_tsz"; fi
done

echo "== leg4 codecs (C->oracle + oracle->C on big.txt; lzbitmap/lzraven ora->C)"
for alg in none zlib lzma lz4 lzfse; do
  "$CLI" aeadc encrypt --profile 5 --password "$PW" -a $alg --checksum sha256 --padding none -i "$WORK/big.txt" -o "$WORK/c-$alg.aea" 2>/dev/null || { bad "cenc-$alg"; continue; }
  "$AEA" decrypt -password-value "$PW" -i "$WORK/c-$alg.aea" -o "$WORK/c-$alg-co.out" 2>/dev/null && cmp -s "$WORK/c-$alg-co.out" "$WORK/big.txt" && ok "c2ora-$alg" || bad "c2ora-$alg"
  "$AEA" encrypt -profile 5 -password-value "$PW" -a $alg -i "$WORK/big.txt" -o "$WORK/o-$alg.aea" 2>/dev/null || { bad "oenc-$alg"; continue; }
  "$CLI" aeadc decrypt --password "$PW" -i "$WORK/o-$alg.aea" -o "$WORK/o-$alg-oc.out" 2>/dev/null && cmp -s "$WORK/o-$alg-oc.out" "$WORK/big.txt" && ok "ora2c-$alg" || bad "ora2c-$alg"
done
for alg in lzbitmap lzraven; do
  "$AEA" encrypt -profile 5 -password-value "$PW" -a $alg -i "$WORK/big.txt" -o "$WORK/o-$alg.aea" 2>/dev/null || { bad "oenc-$alg"; continue; }
  "$CLI" aeadc decrypt --password "$PW" -i "$WORK/o-$alg.aea" -o "$WORK/o-$alg-oc.out" 2>/dev/null && cmp -s "$WORK/o-$alg-oc.out" "$WORK/big.txt" && ok "ora2c-$alg" || bad "ora2c-$alg"
  out=$("$CLI" aeadc encrypt --profile 5 --password "$PW" -a $alg -i "$WORK/msg.txt" -o "$WORK/x.aea" 2>&1); rc=$?
  if [ $rc -ne 0 ]; then ok "noenc-$alg"; else bad "noenc-$alg"; fi
done
# all codecs on empty + tiny (decoder edge shapes)
for alg in none zlib lzma lz4 lzfse; do
  "$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" -a $alg -i "$WORK/empty.bin" -o "$WORK/e-$alg.aea" 2>/dev/null &&
  "$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/e-$alg.aea" -o "$WORK/e-$alg.out" 2>/dev/null &&
  cmp -s "$WORK/e-$alg.out" "$WORK/empty.bin" && ok "empty-$alg" || bad "empty-$alg"
done

echo "== leg5 deterministic transplant (C bytes == oracle bytes, fixed salt/nmac/smacs)"
# offsets: pe=12+auth+144; salt=pe-144(32); sh=pe(shsz); nmac=pe+shsz*256; smacs=+32(8192)
transplant() { # $1=profile $2=key-or-pw-flag $3=ckname $4=cksize $5=in $6=tag
  _p=$1; _cred=$2; _ckn=$3; _cks=$4; _in=$5; _tag=$6
  _sl=128; _pl=0; case $_p in 0)_sl=128;_pl=32;; 1)_sl=0;_pl=0;; 2)_sl=160;_pl=0;; 3)_sl=0;_pl=65;; 4)_sl=160;_pl=65;; 5)_sl=0;_pl=0;; esac
  _shsz=$((8 + _cks))
  "$AEA" encrypt -profile $_p $_cred -a none -b 64k -checksum "$_ckn" -padding none -i "$_in" -o "$WORK/t-$_tag-o.aea" 2>/dev/null || { bad "tenc-$_tag"; return; }
  _asz=$(od -A n -t u4 -j8 -N4 "$WORK/t-$_tag-o.aea" | tr -d ' ')
  _pe=$((12 + _asz + _sl + _pl + 144))
  _so=$((_pe - 144)); _no=$((_pe + _shsz * 256)); _mo=$((_no + 32))
  _salt=$(dd bs=1 skip=$_so count=32 if="$WORK/t-$_tag-o.aea" 2>/dev/null | xxd -p -c 32)
  _nmac=$(dd bs=1 skip=$_no count=$((32 * 256)) if="$WORK/t-$_tag-o.aea" 2>/dev/null | xxd -p -c 8192)
  _smac=$(dd bs=1 skip=$_mo count=$((32 * 256)) if="$WORK/t-$_tag-o.aea" 2>/dev/null | xxd -p -c 8192)
  _ccred=$_cred
  case "$_cred" in -key\ *) _ccred="--key ${_cred#-key }";; -password-value\ *) _ccred="--password ${_cred#-password-value }";; esac
  "$CLI" aeadc encrypt --profile $_p $_ccred -a none -b 64k --checksum "$_ckn" --padding none --fixed-salt "hex:$_salt" --fixed-nmac "hex:$_nmac" --fixed-smacs "hex:$_smac" -i "$_in" -o "$WORK/t-$_tag-c.aea" 2>/dev/null || { bad "tcenc-$_tag"; return; }
  cmp -s "$WORK/t-$_tag-o.aea" "$WORK/t-$_tag-c.aea" && ok "transplant-$_tag" || bad "transplant-$_tag"
}
transplant 1 "-key $WORK/key32.bin" murmur64 8 "$WORK/msg.txt" p1-msg
transplant 5 "-password-value $PW" sha256 32 "$WORK/msg.txt" p5-msg
transplant 1 "-key $WORK/key32.bin" sha256 32 "$WORK/big.txt" p1-big

echo "== leg6 errors/messages/id/range/stdio/pwfile/keyval/multi/padcorr/strength/auth"
ex() { # $1=tag $2=want-exit $3=want-msg-or-empty rest=args($CLI aeadc ...)
  # refusal cells assert rc AND stderr-nonempty (byte-identity only where pinned)
  _tag=$1; _want=$2; _msg=$3; shift 3
  _out=$("$CLI" aeadc "$@" 2>&1); _rc=$?
  if [ $_rc -eq "$_want" ] && [ -n "$_out" ] && { [ -z "$_msg" ] || echo "$_out" | grep -qF "$_msg"; }; then ok "$_tag"; else bad "$_tag(rc=$_rc out=$_out)"; fi
}
ex err-bad-profile 1 "bad profile" encrypt --profile 9 --key "$WORK/key32.bin" -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-nokey 1 "symmetric key required (32B)" encrypt --profile 1 -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-badalg 1 "bad algorithm" encrypt --profile 1 --key "$WORK/key32.bin" -a bogus -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-badck 1 "bad checksum" encrypt --profile 1 --key "$WORK/key32.bin" --checksum bogus -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-adapad 1 "bad padding (adaptive unsupported in v1)" encrypt --profile 1 --key "$WORK/key32.bin" --padding adaptive -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-smallpad 1 "bad padding (must be 0/none or >= 16)" encrypt --profile 1 --key "$WORK/key32.bin" --padding 5 -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-nosign 1 "sign_priv required" encrypt --profile 2 --key "$WORK/key32.bin" -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-pw-short 1 "Password is too short" encrypt --profile 5 --password 'short-pw' -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-pw-19 1 "Password is too short" encrypt --profile 5 --password '1234567890123456789' -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-pw-empty 1 "password required" encrypt --profile 5 --password '' -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-pw-none 1 "password required" encrypt --profile 5 -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-key31 1 "symmetric key required (32B)" encrypt --profile 1 --key-value hex:abcd -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-kv-bare 1 "key-value must be hex:... or base64:... (oracle rejects bare)" encrypt --profile 1 --key-value abcd -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-rec384 1 "recipient_pub invalid" encrypt --profile 3 --recipient-pub "$WORK/ec384-pub.pem" -i "$WORK/msg.txt" -o "$WORK/x.aea"
ex err-sign384 1 "sign_priv invalid" encrypt --profile 2 --key "$WORK/key32.bin" --sign-priv "$WORK/ec384-priv.pem" -i "$WORK/msg.txt" -o "$WORK/x.aea"
# decrypt-side rejects on C blobs
"$CLI" aeadc encrypt --profile 5 --password "$PW" -a none -i "$WORK/msg.txt" -o "$WORK/e5.aea" 2>/dev/null
ex err-wrongpw 1 "HMAC mismatch" decrypt --password 'wrong-password-000000' -i "$WORK/e5.aea" -o "$WORK/x.out"
head -c 8 "$WORK/e5.aea" > "$WORK/trunc8.aea"
ex err-trunc8 1 "bad magic" decrypt --password "$PW" -i "$WORK/trunc8.aea" -o "$WORK/x.out"
cp "$WORK/e5.aea" "$WORK/prof7.aea"; flipbyte "$WORK/prof7.aea" 4
ex err-profile7 1 "bad profile" decrypt --password "$PW" -i "$WORK/prof7.aea" -o "$WORK/x.out"
cp "$WORK/e5.aea" "$WORK/mag.aea"; flipbyte "$WORK/mag.aea" 0
ex err-badmagic 1 "bad magic" decrypt --password "$PW" -i "$WORK/mag.aea" -o "$WORK/x.out"
ex err-no-creds 1 "password required" decrypt -i "$WORK/e5.aea" -o "$WORK/x.out"
ex err-wrong-credtype 1 "symmetric key required (32B)" decrypt --password "$PW" -i "$WORK/p1-c.aea" -o "$WORK/x.out"
ex err-p5-keyextra 1 "password required" decrypt --key "$WORK/key32.bin" -i "$WORK/e5.aea" -o "$WORK/x.out"
cp "$WORK/e5.aea" "$WORK/sstr4.aea"; flipbyte "$WORK/sstr4.aea" 7; flipbyte "$WORK/sstr4.aea" 7; flipbyte "$WORK/sstr4.aea" 7; flipbyte "$WORK/sstr4.aea" 7
ex err-sstr4 1 "bad scrypt strength" decrypt --password "$PW" -i "$WORK/sstr4.aea" -o "$WORK/x.out"
# strength-ok: no-op copy decrypts fine
cp "$WORK/e5.aea" "$WORK/sstrok.aea"
"$CLI" aeadc decrypt --password "$PW" -i "$WORK/sstrok.aea" -o "$WORK/sstrok.out" 2>/dev/null && cmp -s "$WORK/sstrok.out" "$WORK/msg.txt" && ok str-ok || bad str-ok
# unsigned p0 (oracle makes it with -sign-pub encrypt): both must reject
"$AEA" encrypt -profile 0 -sign-pub "$WORK/ec-pub.pem" -a none -i "$WORK/msg.txt" -o "$WORK/p0u.aea" 2>/dev/null || bad unsigned-setup
"$AEA" decrypt -sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0u.aea" -o "$WORK/x.out" 2>/dev/null && bad unsigned-ora || ok unsigned-ora
ex err-unsigned 1 "" decrypt --sign-pub "$WORK/ec-pub.pem" -i "$WORK/p0u.aea" -o "$WORK/x.out"
# id + id-auth
"$CLI" aeadc id -i "$WORK/p1-c.aea" > "$WORK/id1.out" 2>/dev/null && grep -qE '^[0-9a-f]{64}$' "$WORK/id1.out" && ok id || bad id
"$AEA" id -i "$WORK/p1-c.aea" > "$WORK/id1o.out" 2>/dev/null && cmp -s "$WORK/id1.out" "$WORK/id1o.out" && ok id-ora || bad id-ora
head -c 100 "$WORK/p1-c.aea" > "$WORK/idt.aea"
ex err-id-trunc 1 "truncated prologue" id -i "$WORK/idt.aea"
printf 'auth-bytes' > "$WORK/auth.bin"
"$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" --auth-data "$WORK/auth.bin" --auth-data-key mykey --auth-data-value hex:010203 --auth-data-value hex:0405 -i "$WORK/msg.txt" -o "$WORK/auth.aea" 2>/dev/null || bad auth-enc
"$CLI" aeadc id -i "$WORK/auth.aea" > "$WORK/idauth.out" 2>/dev/null && grep -qE '^[0-9a-f]{64}$' "$WORK/idauth.out" && ok id-auth || bad id-auth
"$AEA" decrypt -key "$WORK/key32.bin" -i "$WORK/auth.aea" -o "$WORK/auth-ora.out" 2>/dev/null && cmp -s "$WORK/auth-ora.out" "$WORK/msg.txt" && ok auth-c2ora || bad auth-c2ora
ex err-authkey-noval 1 "auth-data-key without following value" encrypt --profile 1 --key "$WORK/key32.bin" --auth-data-key k1 -i "$WORK/msg.txt" -o "$WORK/x.aea"
# range (expected from oracle range decrypt)
"$AEA" encrypt -profile 1 -key "$WORK/key32.bin" -a none -i "$WORK/big.txt" -o "$WORK/rng.aea" 2>/dev/null
for rs in "10 20" "0 100" "100000 5000"; do
  set -- $rs
  "$AEA" decrypt -key "$WORK/key32.bin" -range-offset "$1" -range-size "$2" -i "$WORK/rng.aea" -o "$WORK/rng-exp.out" 2>/dev/null
  "$CLI" aeadc decrypt --key "$WORK/key32.bin" --range-offset "$1" --range-size "$2" -i "$WORK/rng.aea" -o "$WORK/rng-c.out" 2>/dev/null &&
  cmp -s "$WORK/rng-c.out" "$WORK/rng-exp.out" && ok "range-$1-$2" || bad "range-$1-$2"
done
# stdio: stdin->stdout roundtrip, literal '-' file
"$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" -a none -i "$WORK/msg.txt" -o "$WORK/std.aea" 2>/dev/null
"$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/std.aea" > "$WORK/std.out" 2>/dev/null && cmp -s "$WORK/std.out" "$WORK/msg.txt" && ok stdio-out || bad stdio-out
cat "$WORK/msg.txt" | "$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" -a none -o "$WORK/std2.aea" 2>/dev/null &&
"$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/std2.aea" -o "$WORK/std2.out" 2>/dev/null &&
cmp -s "$WORK/std2.out" "$WORK/msg.txt" && ok stdio-in || bad stdio-in
mkdir -p "$WORK/dash" && printf 'dash-data' > "$WORK/dash/-"
(cd "$WORK/dash" && "$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" -a none -i - -o dash.aea) 2>/dev/null &&
(cd "$WORK/dash" && "$CLI" aeadc decrypt --key "$WORK/key32.bin" -i dash.aea -o dash.out) 2>/dev/null &&
cmp -s "$WORK/dash/dash.out" "$WORK/dash/-" && ok dash-in || bad dash-in
# pwfile forms + keyval forms
printf '%s' "$PW" > "$WORK/pwfile.txt"
printf '%s\n' "$PW" > "$WORK/pwfile-nl.txt"
"$CLI" aeadc encrypt --profile 5 --password-file "$WORK/pwfile-nl.txt" -a none -i "$WORK/msg.txt" -o "$WORK/pwf.aea" 2>/dev/null &&
"$CLI" aeadc decrypt --password-file "$WORK/pwfile.txt" -i "$WORK/pwf.aea" -o "$WORK/pwf.out" 2>/dev/null &&
cmp -s "$WORK/pwf.out" "$WORK/msg.txt" && ok pwfile || bad pwfile
printf '\377\376' > "$WORK/pwfile-bad.bin"
ex err-pwfile-text 1 "password file not text" encrypt --profile 5 --password-file "$WORK/pwfile-bad.bin" -i "$WORK/msg.txt" -o "$WORK/x.aea"
K64=$(od -A n -t x1 "$WORK/key32.bin" | tr -d ' \n')
B64=$(openssl base64 -A -in "$WORK/key32.bin")
"$CLI" aeadc encrypt --profile 1 --key-value "hex:$K64" -i "$WORK/msg.txt" -o "$WORK/kvh.aea" 2>/dev/null &&
"$CLI" aeadc decrypt --key-value "base64:$B64" -i "$WORK/kvh.aea" -o "$WORK/kvh.out" 2>/dev/null &&
cmp -s "$WORK/kvh.out" "$WORK/msg.txt" && ok keyval || bad keyval
# multi-cluster chaining (C->C, C->oracle, oracle->C)
"$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" -a none --checksum sha256 --padding none -b 64k -i "$WORK/multi.bin" -o "$WORK/mc-c.aea" 2>/dev/null || bad mc-enc
"$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/mc-c.aea" -o "$WORK/mc-cc.out" 2>/dev/null && cmp -s "$WORK/mc-cc.out" "$WORK/multi.bin" && ok mc-rt || bad mc-rt
"$AEA" decrypt -key "$WORK/key32.bin" -i "$WORK/mc-c.aea" -o "$WORK/mc-co.out" 2>/dev/null && cmp -s "$WORK/mc-co.out" "$WORK/multi.bin" && ok mc-c2ora || bad mc-c2ora
head -c 263000000 /dev/zero > "$WORK/mcz.bin"
"$AEA" encrypt -profile 5 -password-value "$PW" -a none -padding none -i "$WORK/mcz.bin" -o "$WORK/mcz-o.aea" 2>/dev/null || bad mc-oenc
"$CLI" aeadc decrypt --password "$PW" -i "$WORK/mcz-o.aea" -o "$WORK/mcz-oc.out" 2>/dev/null && cmp -s "$WORK/mcz-oc.out" "$WORK/mcz.bin" && ok mc-ora2c || bad mc-ora2c
# padcorr flips (single-cluster p1 + padding 16): every flip must fail
"$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" -a none --checksum sha256 --padding 16 -i "$WORK/msg.txt" -o "$WORK/pad.aea" 2>/dev/null || bad pad-enc
"$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/pad.aea" -o "$WORK/pad.out" 2>/dev/null && cmp -s "$WORK/pad.out" "$WORK/msg.txt" && ok pad-rt || bad pad-rt
LAST=$(( $(wc -c < "$WORK/pad.aea" | tr -d ' ') - 1 ))
for off in 50 200 1000 5000 10000 $LAST; do
  cp "$WORK/pad.aea" "$WORK/padf.aea"; flipbyte "$WORK/padf.aea" $off
  if "$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/padf.aea" -o "$WORK/x.out" 2>/dev/null; then bad "padcorr-$off"; else ok "padcorr-$off"; fi
done
# murmur + empty + block-size indifference (decrypt side)
"$CLI" aeadc encrypt --profile 2 --key "$WORK/key32.bin" --sign-priv "$WORK/ec-priv.pem" -a none --checksum murmur64 -i "$WORK/msg.txt" -o "$WORK/mur.aea" 2>/dev/null &&
"$CLI" aeadc decrypt --key "$WORK/key32.bin" --sign-pub "$WORK/ec-pub.pem" -i "$WORK/mur.aea" -o "$WORK/mur.out" 2>/dev/null &&
cmp -s "$WORK/mur.out" "$WORK/msg.txt" && ok murmur || bad murmur
"$CLI" aeadc encrypt --profile 5 --password "$PW" -a none -i "$WORK/empty.bin" -o "$WORK/mt.aea" 2>/dev/null &&
"$CLI" aeadc decrypt --password "$PW" -i "$WORK/mt.aea" -o "$WORK/mt.out" 2>/dev/null &&
cmp -s "$WORK/mt.out" "$WORK/empty.bin" && ok empty || bad empty
for bs in 64k 16k 4k 1k; do
  "$CLI" aeadc encrypt --profile 1 --key "$WORK/key32.bin" -a none -b $bs -i "$WORK/msg.txt" -o "$WORK/bs.aea" 2>/dev/null &&
  "$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/bs.aea" -o "$WORK/bs.out" 2>/dev/null &&
  cmp -s "$WORK/bs.out" "$WORK/msg.txt" && ok "bs-$bs" || bad "bs-$bs"
done
# concat: decrypt uses first blob only
cat "$WORK/p1-c.aea" "$WORK/e5.aea" > "$WORK/concat.aea"
"$CLI" aeadc decrypt --key "$WORK/key32.bin" -i "$WORK/concat.aea" -o "$WORK/concat.out" 2>/dev/null &&
cmp -s "$WORK/concat.out" "$WORK/msg.txt" && ok concat || bad concat

echo "== leg7 full tests/test_aea_enc.sh via aeadc-shim (system python3 only)"
SHIM=$(cd "$HERE" && pwd)/aeadc-shim.sh
if AEAD_PY="$SHIM" CLI="$CLI" sh "$HERE/test_aea_enc.sh" > "$WORK/aea-enc.log" 2>&1; then ok aea-enc-suite; else bad aea-enc-suite; fi
tail -3 "$WORK/aea-enc.log"

echo "== $npass passed, fail=$fail"
rm -rf "$WORK"
[ $fail -eq 0 ] && echo "AEADC-GREEN" || echo "AEADC-RED"
exit $fail
