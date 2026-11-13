#!/bin/sh
# test_aea_enc.sh v1 -- writer3 own AEA-encrypt battery (proto vs oracle).
# Self-generating: encrypts with proto `aead.py encrypt`, cross-checks with
# oracle `aea` both directions, cmp. Exits 0 ALL-PASS / 1 any FAIL.
# VERB=0|1|2 (default 1): 0 counts only, 1 cell lines, 2 + failing commands.
# Needs: AEAD_PY (venv python w/ cryptography+lz4), LZFSE_BIN (own-built CLI).
set -u
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
REPO=$(cd "$(dirname "$0")/.." && pwd)
AEAD_PY=${AEAD_PY:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/.venv/bin/python}
LZFSE_BIN=${LZFSE_BIN:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/oss/lzfse/build/bin/lzfse}
export LZFSE_BIN
SCRATCH=$TMPDIR
WORK=$(mktemp -d "$SCRATCH/aea-enc.XXXXXX")
trap 'rm -rf "$WORK"' EXIT
VERB=${VERB:-1}
PASS=0; FAIL=0
EPASS=0; EFAIL=0; OPASS=0; OFAIL=0
note() { [ "$VERB" -ge "$1" ] && shift && echo "$@" || true; }
ok() { PASS=$((PASS+1)); note 1 "PASS $1"; }
bad() { FAIL=$((FAIL+1)); echo "FAIL $1"; [ "$VERB" -ge 2 ] && echo "  $2" || true; }
eok() { EPASS=$((EPASS+1)); ok "enc-$1"; }
ebad() { EFAIL=$((EFAIL+1)); bad "enc-$1" "$2"; }
ook() { OPASS=$((OPASS+1)); ok "dec-$1"; }
obad() { OFAIL=$((OFAIL+1)); bad "dec-$1" "$2"; }

PW='testpw32....................................'
printf 'hello aea world\n' > "$WORK/msg.txt"
python3 -c "open('$WORK/big.bin','wb').write(b'The quick brown fox jumps over the lazy dog. '*20000)"
: > "$WORK/empty.bin"
openssl ecparam -name prime256v1 -genkey -noout -out "$WORK/ec-priv.pem" 2>/dev/null
openssl ec -in "$WORK/ec-priv.pem" -pubout -out "$WORK/ec-pub.pem" 2>/dev/null
head -c 32 /dev/urandom > "$WORK/key32.bin"
K=$WORK/key32.bin; ECP=$WORK/ec-pub.pem; ECS=$WORK/ec-priv.pem

# ours encrypt -> oracle decrypt -> cmp
ours_ora() { # tag profile me-creds... -- input expected
  tag=$1; shift
  if "$AEAD_PY" "$REPO/proto/aead.py" encrypt "$@" -o "$WORK/m.aea" 2>"$WORK/e.txt" \
     && aea decrypt $ODEC -i "$WORK/m.aea" -o "$WORK/m.out" 2>/dev/null \
     && cmp -s "$WORK/m.out" "$EXP"; then eok "$tag"; else ebad "$tag" "$(cat "$WORK/e.txt")"; fi
}
# oracle encrypt -> ours decrypt -> cmp
ora_ours() { # tag profile ora-creds... -- input expected
  tag=$1; shift
  if aea encrypt "$@" -o "$WORK/g.aea" 2>/dev/null \
     && "$AEAD_PY" "$REPO/proto/aead.py" decrypt $PDEC -i "$WORK/g.aea" -o "$WORK/g.out" 2>"$WORK/e.txt" \
     && cmp -s "$WORK/g.out" "$EXP"; then ook "$tag"; else obad "$tag" "$(cat "$WORK/e.txt")"; fi
}

# 1. per-profile cells (msg, -a none, sha256, no pad)
for p in 0 1 2 3 4 5; do
  case $p in
    0) ME="--profile 0 --sign-priv $ECS"; MO="-profile 0 -sign-priv $ECS"; OD="-sign-pub $ECP"; PD="--sign-pub $ECP";;
    1) ME="--profile 1 --key $K"; MO="-profile 1 -key $K"; OD="-key $K"; PD="--key $K";;
    2) ME="--profile 2 --key $K --sign-priv $ECS"; MO="-profile 2 -key $K -sign-priv $ECS"; OD="-key $K -sign-pub $ECP"; PD="--key $K --sign-pub $ECP";;
    3) ME="--profile 3 --recipient-pub $ECP"; MO="-profile 3 -recipient-pub $ECP"; OD="-recipient-priv $ECS"; PD="--recipient-priv $ECS";;
    4) ME="--profile 4 --recipient-pub $ECP --sign-priv $ECS"; MO="-profile 4 -recipient-pub $ECP -sign-priv $ECS"; OD="-recipient-priv $ECS -sign-pub $ECP"; PD="--recipient-priv $ECS --sign-pub $ECP";;
    5) ME="--profile 5 --password $PW"; MO="-profile 5 -password-value $PW"; OD="-password-value $PW"; PD="--password $PW";;
  esac
  EXP=$WORK/msg.txt; ODEC=$OD; PDEC=$PD
  # shellcheck disable=SC2086
  ours_ora "p$p" $ME -a none --checksum sha256 --padding none -i "$WORK/msg.txt"
  # shellcheck disable=SC2086
  ora_ours "p$p" $MO -a none -checksum sha256 -padding none -i "$WORK/msg.txt"
done

# 2. codecs both directions (big text; p5 ours->ora, p1 ora->ours)
for alg in none zlib lzma lz4 lzfse; do
  EXP=$WORK/big.bin; ODEC="-password-value $PW"; PDEC="--password $PW"
  ours_ora "p5-$alg" --profile 5 --password "$PW" -a "$alg" --checksum sha256 --padding none -i "$WORK/big.bin"
  ODEC="-key $K"; PDEC="--key $K"
  ora_ours "p1-$alg" -profile 1 -key "$K" -a "$alg" -checksum sha256 -padding none -i "$WORK/big.bin"
done

# 3. byte-identical deterministic cells (p1/p5, transplant salt+nmac+smacs)
 transplant() { # tag profile extra-creds...
  tag=$1; shift
  eval "$(python3 - "$WORK/g.aea" <<'EOF'
import struct, sys
ob = open(sys.argv[1], "rb").read()
asz = struct.unpack("<I", ob[8:12])[0]
pe = 12 + asz + 144
salt = ob[pe - 144:pe - 112]
shsz = 8 + 32
nmac = ob[pe + shsz * 256:pe + shsz * 256 + 32]
smacs = ob[pe + shsz * 256 + 32:pe + shsz * 256 + 32 + 32 * 256]
print("SALT=hex:%s;NMAC=hex:%s;SMACS=hex:%s" % (salt.hex(), nmac.hex(), smacs.hex()))
EOF
)"
  if "$AEAD_PY" "$REPO/proto/aead.py" encrypt "$@" --fixed-salt "$SALT" --fixed-nmac "$NMAC" --fixed-smacs "$SMACS" \
       -o "$WORK/d.aea" 2>"$WORK/e.txt" \
     && cmp -s "$WORK/d.aea" "$WORK/g.aea"; then ok "det-$tag"; else bad "det-$tag" "$(cat "$WORK/e.txt")"; fi
}
EXP=$WORK/msg.txt
if aea encrypt -profile 1 -key "$K" -a none -checksum sha256 -padding none -i "$WORK/msg.txt" -o "$WORK/g.aea" 2>/dev/null; then
  transplant "p1-msg" --profile 1 --key "$K" -a none --checksum sha256 --padding none -i "$WORK/msg.txt"
else bad "ora-setup-p1-msg" "oracle encrypt failed (no stale reuse)"; fi
if aea encrypt -profile 5 -password-value "$PW" -a none -checksum sha256 -padding none -i "$WORK/msg.txt" -o "$WORK/g.aea" 2>/dev/null; then
  transplant "p5-msg" --profile 5 --password "$PW" -a none --checksum sha256 --padding none -i "$WORK/msg.txt"
else bad "ora-setup-p5-msg" "oracle encrypt failed (no stale reuse)"; fi
EXP=$WORK/big.bin
if aea encrypt -profile 1 -key "$K" -a none -checksum sha256 -padding none -i "$WORK/big.bin" -o "$WORK/g.aea" 2>/dev/null; then
  transplant "p1-big" --profile 1 --key "$K" -a none --checksum sha256 --padding none -i "$WORK/big.bin"
else bad "ora-setup-p1-big" "oracle encrypt failed (no stale reuse)"; fi

# 4. shape/edge cells
EXP=$WORK/empty.bin; ODEC="-key $K"; PDEC="--key $K"
ours_ora "empty" --profile 1 --key "$K" -a none --checksum none --padding none -i "$WORK/empty.bin"
EXP=$WORK/msg.txt
ours_ora "pad16-p1" --profile 1 --key "$K" -a none --checksum sha256 --padding 16 -i "$WORK/msg.txt"
EXP=$WORK/big.bin; ODEC="-password-value $PW"; PDEC="--password $PW"
ours_ora "pad16-p5" --profile 5 --password "$PW" -a none --checksum sha256 --padding 16 -i "$WORK/big.bin"
EXP=$WORK/big.bin; ODEC="-key $K"
if aea encrypt -profile 1 -key "$K" -a none -i "$WORK/msg.txt" -o "$WORK/g.aea" 2>/dev/null; then
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$K" -i "$WORK/g.aea" -o "$WORK/g.out" 2>/dev/null \
     && cmp -s "$WORK/g.out" "$WORK/msg.txt"; then ok "orapad"; else bad "orapad" ""; fi
else bad "ora-setup-orapad" "oracle encrypt failed (no stale reuse)"; fi
ours_ora "b64k" --profile 1 --key "$K" -a none --checksum sha256 --padding none -b 64k -i "$WORK/big.bin"
ours_ora "murmur" --profile 1 --key "$K" -a zlib --checksum murmur64 --padding none -i "$WORK/big.bin"
printf 'hello-auth' > "$WORK/auth.txt"
EXP=$WORK/msg.txt
ours_ora "auth" --profile 1 --key "$K" -a none --checksum sha256 --padding none --auth-data "$WORK/auth.txt" \
  --auth-data-key mykey --auth-data-value hex:deadbeef -i "$WORK/msg.txt"
EXP=$WORK/msg.txt
if aea encrypt -profile 1 -key "$K" -a none -checksum sha256 -padding none -auth-data-key mykey \
  -auth-data-value hex:deadbeef -i "$WORK/msg.txt" -o "$WORK/g.aea" 2>/dev/null; then
  ORA_AUTH_OK=1
else bad "ora-setup-auth-ora" "oracle encrypt failed (no stale reuse)"; ORA_AUTH_OK=0; fi
if [ "$ORA_AUTH_OK" -eq 1 ] && "$AEAD_PY" "$REPO/proto/aead.py" decrypt --key "$K" -i "$WORK/g.aea" -o "$WORK/g.out" 2>/dev/null \
   && cmp -s "$WORK/g.out" "$WORK/msg.txt"; then ok "auth-ora"; else bad "auth-ora" ""; fi
python3 -c "open('$WORK/three.bin','wb').write(bytes((i*7919)%256 for i in range(3*1024*1024)))"
EXP=$WORK/three.bin; ODEC="-password-value $PW"
ours_ora "3MB" --profile 5 --password "$PW" -a none --checksum sha256 --padding none -i "$WORK/three.bin"
EXP=$WORK/msg.txt; ODEC="-key $K"
printf 'hello aea world\n' | "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 1 --key "$K" -a none \
  --checksum none --padding none -o "$WORK/s.aea" 2>/dev/null \
&& aea decrypt -key "$K" -i "$WORK/s.aea" -o "$WORK/s.out" 2>/dev/null \
&& cmp -s "$WORK/s.out" "$WORK/msg.txt" && ok "stdio" || bad "stdio" ""
oid=$(aea id -i "$WORK/m.aea" 2>/dev/null); pid=$("$AEAD_PY" "$REPO/proto/aead.py" id -i "$WORK/m.aea" 2>/dev/null)
if [ -n "$oid" ] && [ -n "$pid" ] && [ "$oid" = "$pid" ]; then
  ok "id"; else bad "id" "oracle='$oid' proto='$pid' (both nonempty required)"; fi

# 5. error cells (must all exit != 0)
errcell() { # tag args...
  tag=$1; shift
  if "$AEAD_PY" "$REPO/proto/aead.py" encrypt "$@" -i "$WORK/msg.txt" -o "$WORK/x.aea" 2>/dev/null; then
    bad "err-$tag" "exit 0"; else ok "err-$tag"; fi
}
errcell "badprof" --profile 9 --key "$K"
errcell "nokey" --profile 1
errcell "badalg" --profile 1 --key "$K" -a bogus
errcell "badck" --profile 1 --key "$K" --checksum bogus
errcell "adapad" --profile 1 --key "$K" --padding adaptive
errcell "smallpad" --profile 1 --key "$K" --padding 5
errcell "nosign" --profile 2 --key "$K"

# 6. p5 short-password gate (oracle: >= 20 UTF-8 bytes, else "Password is too short")
pwcell() { # tag password -- proto must reject with oracle text
  tag=$1; pw=$2
  if "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 5 --password "$pw" -a none \
       --checksum sha256 --padding none -i "$WORK/msg.txt" -o "$WORK/x.aea" 2>"$WORK/e.txt"; then
    bad "err-pwenc-$tag" "exit 0"
  elif grep -q "Password is too short" "$WORK/e.txt"; then
    ok "err-pwenc-$tag"
  else
    bad "err-pwenc-$tag" "$(cat "$WORK/e.txt")"
  fi
}
# empty CLI arg is falsy -> "password required"; oracle also rejects (rc 1)
if "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 5 --password "" -a none \
     --checksum sha256 --padding none -i "$WORK/msg.txt" -o "$WORK/x.aea" 2>/dev/null; then
  bad "err-pwenc-empty" "exit 0"; else ok "err-pwenc-empty"; fi
pwcell "short" "short"
pwcell "19" "xxxxxxxxxxxxxxxxxxx"
pwcell "19B" "$(python3 -c "print('é'*9+'x',end='')")"
EXP=$WORK/msg.txt; ODEC="-password-value xxxxxxxxxxxxxxxxxxxx"
ours_ora "pw20" --profile 5 --password "xxxxxxxxxxxxxxxxxxxx" -a none --checksum sha256 --padding none -i "$WORK/msg.txt"
EXP=$WORK/msg.txt; ODEC="-password-value $(python3 -c "print('x'*18+'é',end='')")"
ours_ora "pw20B" --profile 5 --password "$(python3 -c "print('x'*18+'é',end='')")" -a none --checksum sha256 --padding none -i "$WORK/msg.txt"

# 7. fixed-input determinism (profiles 3/4 eph + pad): same fixed
# inputs twice -> byte-identical outputs (P7/P17 gate)
# (proto-only: the C aeadc has no --fixed-* flags yet; under the
# aeadc-shim these cells SKIP instead of failing on unrecognized args)
case "$AEAD_PY" in
*aeadc-shim*) echo "SKIP det-p3-* (C aeadc lacks --fixed-eph/--fixed-pad)";;
*)
FIXSALT=ab00000000000000000000000000000000000000000000000000000000000000
FIXNMAC=cd00000000000000000000000000000000000000000000000000000000000000
FIXEPH=$(xxd -p "$ECS" | tr -d '\n')
# seed run: fixed salt/eph, everything else random -> a VALID blob.
# Transplant its nmac/smacs/pad back in: re-encrypting with all fixed
# inputs must reproduce the seed blob byte-for-byte (P7/P17 gate).
if "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 3 --recipient-pub "$ECP" \
     -a none --checksum sha256 --padding 16 --fixed-salt "hex:$FIXSALT" \
     --fixed-eph "hex:$FIXEPH" \
     -i "$WORK/msg.txt" -o "$WORK/d3seed.aea" 2>"$WORK/e.txt" \
   && "$AEAD_PY" "$REPO/proto/aead.py" decrypt --recipient-priv "$ECS" -i "$WORK/d3seed.aea" -o "$WORK/d3s.out" 2>/dev/null \
   && cmp -s "$WORK/d3s.out" "$WORK/msg.txt" \
   && aea decrypt -recipient-priv "$ECS" -i "$WORK/d3seed.aea" -o "$WORK/d3so.out" 2>/dev/null \
   && cmp -s "$WORK/d3so.out" "$WORK/msg.txt"; then
  ok "det-p3-seedvalid"
  eval "$(python3 - "$WORK/d3seed.aea" <<'EOF'
import struct, sys
ob = open(sys.argv[1], "rb").read()
asz = struct.unpack("<I", ob[8:12])[0]
pe = 12 + asz + 0 + 65 + 144  # profile 3: sig 0, pub 65
shsz = 8 + 32
hdrlen = shsz * 256 + 32 + 32 * 256
padstart = pe + hdrlen + 16  # 16B msg, one segment, none codec
print("FIXNMAC=hex:%s" % ob[pe + shsz * 256:pe + shsz * 256 + 32].hex())
print("FIXSMAC=hex:%s" % ob[pe + shsz * 256 + 32:pe + shsz * 256 + 32 + 32 * 256].hex())
print("FIXPAD=hex:%s" % ob[padstart:].hex())
EOF
)"
  FIXARGS="--fixed-salt hex:$FIXSALT --fixed-nmac $FIXNMAC --fixed-smacs $FIXSMAC --fixed-eph hex:$FIXEPH --fixed-pad $FIXPAD"
  # shellcheck disable=SC2086
  if "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 3 --recipient-pub "$ECP" \
       -a none --checksum sha256 --padding 16 $FIXARGS \
       -i "$WORK/msg.txt" -o "$WORK/d3a.aea" 2>"$WORK/e.txt" \
     && "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 3 --recipient-pub "$ECP" \
       -a none --checksum sha256 --padding 16 $FIXARGS \
       -i "$WORK/msg.txt" -o "$WORK/d3b.aea" 2>>"$WORK/e.txt" \
     && cmp -s "$WORK/d3a.aea" "$WORK/d3b.aea" \
     && cmp -s "$WORK/d3a.aea" "$WORK/d3seed.aea"; then ok "det-p3-eph-pad"; else bad "det-p3-eph-pad" "$(cat "$WORK/e.txt")"; fi
  # the deterministic blob self-decrypts AND oracle-decrypts (valid, not just stable)
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --recipient-priv "$ECS" -i "$WORK/d3a.aea" -o "$WORK/d3a.out" 2>/dev/null \
     && cmp -s "$WORK/d3a.out" "$WORK/msg.txt" \
     && aea decrypt -recipient-priv "$ECS" -i "$WORK/d3a.aea" -o "$WORK/d3o.out" 2>/dev/null \
     && cmp -s "$WORK/d3o.out" "$WORK/msg.txt"; then ok "det-p3-oracle"; else bad "det-p3-oracle" ""; fi
else bad "det-p3-seed" "seed encrypt failed"; fi
# without --fixed-eph the same run must NOT be byte-identical (random eph proves the flag matters)
if "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 3 --recipient-pub "$ECP" \
     -a none --checksum sha256 --padding none --fixed-salt "hex:$FIXSALT" \
     --fixed-nmac "hex:$FIXNMAC" -i "$WORK/msg.txt" -o "$WORK/d3c.aea" 2>/dev/null \
   && "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 3 --recipient-pub "$ECP" \
     -a none --checksum sha256 --padding none --fixed-salt "hex:$FIXSALT" \
     --fixed-nmac "hex:$FIXNMAC" -i "$WORK/msg.txt" -o "$WORK/d3d.aea" 2>/dev/null \
   && cmp -s "$WORK/d3c.aea" "$WORK/d3d.aea"; then bad "det-p3-noeph" "identical without fixed-eph"; else ok "det-p3-noeph"; fi
# --fixed-pad wrong length fails closed
if "$AEAD_PY" "$REPO/proto/aead.py" encrypt --profile 3 --recipient-pub "$ECP" \
     -a none --checksum sha256 --padding 16 --fixed-pad hex:deadbeef -i "$WORK/msg.txt" -o "$WORK/x.aea" 2>/dev/null; then
  bad "err-fixedpad-len" "exit 0"; else ok "err-fixedpad-len"; fi
esac

echo "ENC ours->ora: PASS=$EPASS FAIL=$EFAIL"
echo "DEC ora->ours: PASS=$OPASS FAIL=$OFAIL"
echo "TOTAL PASS=$PASS FAIL=$FAIL"
[ "$FAIL" -eq 0 ] && echo ENC-GREEN
exit "$FAIL"
