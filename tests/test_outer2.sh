#!/bin/sh
# test_outer2.sh — writer2 outer/AEA battery (A-7 grant: pins/battery for w2 beds).
# AAR cells: sha-pinned (deterministic oracle). AEA cells: size/prefix/RT/rc
# (archives nondet; .aea bytes NEVER sha-compared). Exit 0 GREEN / 1 RED / 2 error.
# Usage: sh tests/test_outer2.sh [workdir]  (ADAPTER=... default oracle adapter)
# RECORD=1 sh tests/test_outer2.sh [workdir]  (rewrite PINS; REVIEW diff vs beds!)
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
ADAPTER=${ADAPTER:-$HERE/../harness/oracle-adapter.sh}
WORK=${1:-$(mktemp -d "${TMPDIR:-/tmp}/outer2.XXXXXX")}
PINS=$ROOT/vectors/outer2-PINS.csv
FAIL=0
GEN=test_outer2.sh
OS=$(sw_vers -productVersion 2>/dev/null || echo unknown)
BE=$(basename "$ADAPTER")
command -v python3 >/dev/null || { echo "need python3" >&2; exit 2; }
mkdir -p "$WORK" "$ROOT/vectors"
pin_get() { grep "^$1," "$PINS" | head -1 | cut -d, -f3; }
chk() { # name check val [bytes]
  if [ -n "${RECORD:-}" ]; then
    echo "$1,$2,$3,${4:-0},$GEN,$OS,$BE" >> "$PINS.new"
    echo "REC $1=$3"
  else
    [ -f "$PINS" ] || { echo "missing $PINS (RECORD=1 first)" >&2; exit 2; }
    exp=$(pin_get "$1")
    if [ "$3" = "$exp" ]; then echo "PASS $1"; else echo "FAIL $1: got $3 want $exp"; FAIL=1; fi
  fi
}
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
sz() { wc -c < "$1" | tr -d ' '; }
echo "== probe =="
sh "$ADAPTER" probe || exit 2
if [ -n "${RECORD:-}" ]; then
  echo "# outer2 pins: name,check,expect,bytes,generator,os,backend" > "$PINS.new"
  echo "# checks: sha=full-sha | size=byte count | str=opaque compare | rc=exit code" >> "$PINS.new"
  echo "# AAR deterministic (fixed mtimes + python seeds). AEA nondet: size/prefix/RT/rc only." >> "$PINS.new"
fi
IN=$WORK/in; mkdir -p "$IN"
mkempty() { rm -rf "$IN/empty"; mkdir -p "$IN/empty"; touch -t 202001010000 "$IN/empty"; }
mk1file() { # dir nbytes z|seedN
  rm -rf "$IN/$1"; mkdir -p "$IN/$1"
  case "$3" in
    z) head -c "$2" /dev/zero > "$IN/$1/f.bin";;
    seed*) python3 -c "import random; open('$IN/$1/f.bin','wb').write(random.Random(${3#seed}).randbytes($2))";;
  esac
  touch -t 202001010000 "$IN/$1/f.bin" "$IN/$1"
}
mkK() { # dir K (flip input: K zeros + seed42 tail, N=2000)
  rm -rf "$IN/$1"; mkdir -p "$IN/$1"
  python3 -c "import random; s=random.Random(42).randbytes(2000); open('$IN/$1/f.bin','wb').write(bytes($2)+s[$2:])"
  touch -t 202001010000 "$IN/$1/f.bin" "$IN/$1"
}
AAR() { # tag srcdir alg [block] : echoes "rc size sha"
  tag=$1; src=$2; alg=$3; blk=${4:-}
  # shellcheck disable=SC2086
  if sh "$ADAPTER" aar-encode --alg "$alg" --threads 1 ${blk:+--block "$blk"} "$IN/$src" "$WORK/$tag.aar" 2>"$WORK/$tag.err"; then
    echo "0 $(sz "$WORK/$tag.aar") $(sha "$WORK/$tag.aar")"
  else echo "$? 0 -"; fi
}
rule_of() { # tag rawfile : STORED iff size==raw+28 and inner@28==AA01
  if [ "$(sz "$WORK/$1.aar")" -eq $(( $(sz "$2") + 28 )) ] && [ "$(dd if="$WORK/$1.aar" bs=1 skip=28 count=4 2>/dev/null)" = "AA01" ]; then echo STORED; else echo COMPRESSED; fi
}
echo "== AAR =="
mkempty
for a in raw lzfse lzma lz4 zlib lzraven lzbitmap; do
  set -- $(AAR "m-empty-$a" empty "$a"); rc=$1 s=$2 h=$3
  if [ "$rc" != 0 ]; then echo "FAIL m-empty-$a rc=$rc"; FAIL=1; continue; fi
  chk "m-empty-$a" sha "$h" "$s"
done
mk1file r1000 1000 seed2000
set -- $(AAR "m-stored-raw" r1000 raw)
set -- $(AAR "m-stored" r1000 lzfse); s=$2 h=$3
chk "m-stored" sha "$h" "$s"
chk "m-stored-rule" str "$(rule_of m-stored "$WORK/m-stored-raw.aar")" "$s"
mkK k95 95; mkK k96 96
set -- $(AAR "m-f95-raw" k95 raw)
set -- $(AAR "m-f95" k95 lzfse); s95=$2 h95=$3
chk "m-flip95-rule" str "$(rule_of m-f95 "$WORK/m-f95-raw.aar")" "$s95"
chk "m-flip95" sha "$h95" "$s95"
set -- $(AAR "m-f96-raw" k96 raw)
set -- $(AAR "m-f96" k96 lzfse); s96=$2 h96=$3
chk "m-flip96-rule" str "$(rule_of m-f96 "$WORK/m-f96-raw.aar")" "$s96"
chk "m-flip96-comp" str "$((s96 - 28))" "$s96"
chk "m-flip96" sha "$h96" "$s96"
mk1file z200k 200000 z
set -- $(AAR "m-b16" z200k lzfse 16); chk "m-b16" sha "$3" "$2"
set -- $(AAR "m-b20" z200k lzfse 20); chk "m-b20" sha "$3" "$2"
mk1file bigR 5000000 seed7; mk1file bigZ 5000000 z
for k in R Z; do
  sh "$ADAPTER" aar-encode --alg lzfse --threads 1 "$IN/big$k" "$WORK/m-t$k-1.aar" 2>/dev/null
  sh "$ADAPTER" aar-encode --alg lzfse --threads 18 "$IN/big$k" "$WORK/m-t$k-18.aar" 2>/dev/null
  cmp -s "$WORK/m-t$k-1.aar" "$WORK/m-t$k-18.aar" && v=EQ || v=DIFF
  chk "m-t$k-cmp" str "$v" "$(sz "$WORK/m-t$k-1.aar")"
  chk "m-t$k" sha "$(sha "$WORK/m-t$k-1.aar")" "$(sz "$WORK/m-t$k-1.aar")"
done
mk1file rb-z1000 1000 z
mk1file rb-r1000 1000 seed6000
mk1file rb-z100k 100000 z
set -- $(AAR "m-rb-r1k-raw" rb-r1000 raw)
for a in lzraven lzbitmap; do
  set -- $(AAR "m-rb-$a-z1k" rb-z1000 "$a"); chk "m-rb-$a-z1k" sha "$3" "$2"
  set -- $(AAR "m-rb-$a-r1k" rb-r1000 "$a"); s=$2 h=$3
  chk "m-rb-$a-r1k-rule" str "$(rule_of "m-rb-$a-r1k" "$WORK/m-rb-r1k-raw.aar")" "$s"
  chk "m-rb-$a-r1k" sha "$h" "$s"
  set -- $(AAR "m-rb-$a-z100k" rb-z100k "$a"); chk "m-rb-$a-z100k" sha "$3" "$2"
done
FLIP() { # tag nbytes alg : rule + sha pins (random seed42 input, NOTE-w2s2-3/4 beds)
  tag=$1; n=$2; alg=$3
  mk1file "fl$n" "$n" seed42
  set -- $(AAR "m-$tag-raw" "fl$n" raw)
  set -- $(AAR "m-$tag" "fl$n" "$alg"); s=$2 h=$3
  chk "m-$tag-rule" str "$(rule_of "m-$tag" "$WORK/m-$tag-raw.aar")" "$s"
  chk "m-$tag" sha "$h" "$s"
}
FLIP fl-lzma170 170 lzma;  FLIP fl-lzma171 171 lzma
FLIP fl-lz4-62 62 lz4;     FLIP fl-lz4-63 63 lz4
FLIP fl-lz4-274 274 lz4;   FLIP fl-lz4-275 275 lz4
FLIP fl-zlib610 610 zlib;  FLIP fl-zlib611 611 zlib
FLIP fl-lzfse658 658 lzfse; FLIP fl-lzfse659 659 lzfse
FLIP fl-rav287 287 lzraven; FLIP fl-rav288 288 lzraven
FLIP fl-bm50 50 lzbitmap;  FLIP fl-bm51 51 lzbitmap
FLIP fl-bm70 70 lzbitmap;  FLIP fl-bm71 71 lzbitmap
FRAMES() { # tag nbytes alg magichex block : frame-lens csv + sha (NOTE-w2s2-5 beds)
  tag=$1; n=$2; alg=$3; mg=$4; blk=$5
  mk1file "fr$n" "$n" z
  set -- $(AAR "m-$tag" "fr$n" "$alg" "$blk"); s=$2 h=$3
  lens=$(python3 -c "
import sys
b=open('$WORK/m-$tag.aar','rb').read(); mg=bytes.fromhex('$mg')
o=[]; i=28
while True:
  j=b.find(mg,i)
  if j<0: break
  o.append(j); i=j+1
e=o[1:]+[len(b)]
print(':'.join(str(t-s) for s,t in zip(o,e)))")
  chk "m-$tag-lens" str "$lens" "$s"
  chk "m-$tag" sha "$h" "$s"
}
FRAMES fr-rav100k 100000 lzraven 2b00caec 10000
FRAMES fr-bm100k 100000 lzbitmap 5a424d 10000
UNC() { # tag nbytes alg block : unc-sum/chain verdict + sha (NOTE-w2s2-6 layout)
  tag=$1; n=$2; alg=$3; blk=$4
  mk1file "un$n$blk" "$n" z
  set -- $(AAR "m-$tag-raw" "un$n$blk" raw)
  set -- $(AAR "m-$tag" "un$n$blk" "$alg" "$blk"); s=$2 h=$3
  v=$(python3 -c "
import struct
b = open('$WORK/m-$tag.aar','rb').read()
r = open('$WORK/m-$tag-raw.aar','rb').read()
inner = len(r) - 28
p = 12; su = 0; nb = 0
while p < len(b):
  z1, u, z2, c = struct.unpack('>IIII', b[p:p+16])
  assert z1 == 0 and z2 == 0, (nb, z1, z2)
  su += u; nb += 1; p += 16 + c
iv = 'INNER-EQ' if su - 28 == inner else f'INNER-DIFF-{su}-{inner}'
cv = 'CHAIN-EQ' if p == len(b) else f'CHAIN-DIFF-{p}-{len(b)}'
print(f'{iv}-{cv}-NB{nb}')")
  chk "m-$tag-unc" str "$v" "$s"
  chk "m-$tag" sha "$h" "$s"
}
UNC un-rav100k-b10k 100000 lzraven 10000
UNC un-bm100k-b10k 100000 lzbitmap 10000
UNC un-rav200k-1 200000 lzraven ""
UNC un-bm200k-1 200000 lzbitmap ""
MIX() { # tag alg : per-block S/C pattern + sha (50k zeros + 50k seed11 random, -b 10000)
  tag=$1; alg=$2
  rm -rf "$IN/mix"; mkdir -p "$IN/mix"
  python3 -c "import random; open('$IN/mix/f.bin','wb').write(bytes(50000)+random.Random(11).randbytes(50000))"
  touch -t 202001010000 "$IN/mix/f.bin" "$IN/mix"
  set -- $(AAR "m-$tag" mix "$alg" 10000); s=$2 h=$3
  pat=$(python3 -c "
import struct
b = open('$WORK/m-$tag.aar','rb').read()
p = 12; o = ''
while p < len(b):
  z1, u, z2, c = struct.unpack('>IIII', b[p:p+16])
  assert z1 == 0 and z2 == 0
  o += 'S' if u == c else 'C'
  p += 16 + c
assert p == len(b)
print(o)")
  chk "m-$tag-pat" str "$pat" "$s"
  chk "m-$tag" sha "$h" "$s"
}
MIX mix-rav lzraven; MIX mix-bm lzbitmap; MIX mix-lz lzfse
echo "== AEA =="
AEA=${AEA:-/usr/bin/aea}
PW="0123456789abcdef0123456789abcdef"
python3 -c "import random; open('$WORK/key32.bin','wb').write(random.Random(4242).randbytes(32))"
HEX=$(xxd -p "$WORK/key32.bin" | tr -d '\n')
openssl ecparam -name prime256v1 -genkey -noout -out "$WORK/ec-priv.pem" 2>/dev/null
openssl ec -in "$WORK/ec-priv.pem" -pubout -out "$WORK/ec-pub.pem" 2>/dev/null
for n in 0 1 100 1000 5000; do
  if [ "$n" = 0 ]; then : > "$IN/a$n.bin"; else head -c "$n" /dev/zero > "$IN/a$n.bin"; fi
done
AEAa() { # tag profile pw|hex alg infile : adapter encrypt; echoes "rc size"
  case $3 in pw) K="--password $PW";; hex) K="--key hex:$HEX";; esac
  # shellcheck disable=SC2086
  if sh "$ADAPTER" aea-encrypt --profile "$2" $K --alg "$4" --threads 1 "$IN/$5" "$WORK/$1.aea" 2>"$WORK/$1.err"; then
    echo "0 $(sz "$WORK/$1.aea")"
  else echo "$? 0"; fi
}
RTa() { # tag aeafile expectfile pw|hex : adapter decrypt+cmp; echoes RT-OK/RT-DIFF/RC-n
  case $4 in pw) K="--password $PW";; hex) K="--key hex:$HEX";; esac
  # shellcheck disable=SC2086
  if sh "$ADAPTER" aea-decrypt $K "$WORK/$2" "$WORK/$1.back" 2>/dev/null; then
    cmp -s "$WORK/$1.back" "$IN/$3" && echo RT-OK || echo RT-DIFF
  else echo "RC-$?"; fi
}
for n in 0 1 100 1000 5000; do
  set -- $(AEAa "a-p1-$n" 1 hex none "a$n.bin")
  if [ "$1" != 0 ]; then echo "FAIL a-p1-$n rc=$1"; FAIL=1; else chk "a-size-p1-$n" size "$2" "$2"; fi
  set -- $(AEAa "a-p5-$n" 5 pw none "a$n.bin")
  if [ "$1" != 0 ]; then echo "FAIL a-p5-$n rc=$1"; FAIL=1; else chk "a-size-p5-$n" size "$2" "$2"; fi
done
for P in 1 5; do chk "a-hdr12-p$P" str "$(head -c 12 "$WORK/a-p$P-100.aea" | xxd -p | tr -d '\n')" 0; done
for a in lzfse zlib lzma lz4 lzraven lzbitmap; do
  set -- $(AEAa "a-z-$a" 5 pw "$a" "a5000.bin"); chk "a-alg-z-$a" size "$2" "$2"
done
chk "a-rt-p1" str "$(RTa rt-p1 a-p1-5000.aea a5000.bin hex)" 0
chk "a-rt-p5" str "$(RTa rt-p5 a-p5-5000.aea a5000.bin pw)" 0
chk "a-rt-lzfse" str "$(RTa rt-lz a-z-lzfse.aea a5000.bin pw)" 0
# extended cells: direct `aea` (contract-v1 gap: adapter has no padding/checksum/key-file/EC/auth/append)
if "$AEA" encrypt -profile 1 -key "$WORK/key32.bin" -a none -t 1 -padding none -i "$IN/a5000.bin" -o "$WORK/a-pad-none.aea" 2>/dev/null; then
  chk "a-pad-none" size "$(sz "$WORK/a-pad-none.aea")" "$(sz "$WORK/a-pad-none.aea")"
else echo "FAIL a-pad-none rc"; FAIL=1; fi
if "$AEA" encrypt -profile 1 -key "$WORK/key32.bin" -a none -t 1 -checksum none -i "$IN/a5000.bin" -o "$WORK/a-cks-none.aea" 2>/dev/null; then
  chk "a-cks-none" size "$(sz "$WORK/a-cks-none.aea")" "$(sz "$WORK/a-cks-none.aea")"
else echo "FAIL a-cks-none rc"; FAIL=1; fi
if "$AEA" encrypt -profile 1 -key "$WORK/key32.bin" -a none -t 1 -checksum murmur64 -i "$IN/a5000.bin" -o "$WORK/a-cks-murmur.aea" 2>/dev/null; then
  chk "a-cks-murmur" size "$(sz "$WORK/a-cks-murmur.aea")" "$(sz "$WORK/a-cks-murmur.aea")"
else echo "FAIL a-cks-murmur rc"; FAIL=1; fi
if "$AEA" decrypt -key "$WORK/key32.bin" -i "$WORK/a-cks-murmur.aea" -o "$WORK/a-murmur.back" 2>/dev/null && cmp -s "$WORK/a-murmur.back" "$IN/a5000.bin"; then v=RT-OK; else v=RT-DIFF; fi
chk "a-rt-murmur" str "$v" 0
if "$AEA" encrypt -profile 1 -key "$WORK/key32.bin" -a none -t 1 -auth-data-key mykey -auth-data-value hex:deadbeef -i "$IN/a100.bin" -o "$WORK/a-auth.aea" 2>/dev/null; then
  chk "a-auth-size" size "$(sz "$WORK/a-auth.aea")" "$(sz "$WORK/a-auth.aea")"
  if "$AEA" decrypt -key "$WORK/key32.bin" -i "$WORK/a-auth.aea" -o "$WORK/a-auth.back" 2>/dev/null && cmp -s "$WORK/a-auth.back" "$IN/a100.bin"; then v=RT-OK; else v=RT-DIFF; fi
  chk "a-rt-auth" str "$v" 0
else echo "FAIL a-auth rc"; FAIL=1; fi
if "$AEA" encrypt -profile 0 -sign-priv "$WORK/ec-priv.pem" -a none -t 1 -i "$IN/a100.bin" -o "$WORK/a-p0.aea" 2>/dev/null; then
  chk "a-hdr12-p0" str "$(head -c 12 "$WORK/a-p0.aea" | xxd -p | tr -d '\n')" 0
  chk "a-size-p0" size "$(sz "$WORK/a-p0.aea")" "$(sz "$WORK/a-p0.aea")"
  if "$AEA" decrypt -sign-pub "$WORK/ec-pub.pem" -i "$WORK/a-p0.aea" -o "$WORK/a-p0.back" 2>/dev/null && cmp -s "$WORK/a-p0.back" "$IN/a100.bin"; then v=RT-OK; else v=RT-DIFF; fi
  chk "a-rt-p0" str "$v" 0
else echo "FAIL a-p0 rc"; FAIL=1; fi
if "$AEA" encrypt -profile 2 -key "$WORK/key32.bin" -sign-priv "$WORK/ec-priv.pem" -a none -t 1 -i "$IN/a100.bin" -o "$WORK/a-p2.aea" 2>/dev/null; then
  chk "a-hdr12-p2" str "$(head -c 12 "$WORK/a-p2.aea" | xxd -p | tr -d '\n')" 0
  if "$AEA" decrypt -key "$WORK/key32.bin" -sign-pub "$WORK/ec-pub.pem" -i "$WORK/a-p2.aea" -o "$WORK/a-p2.back" 2>/dev/null && cmp -s "$WORK/a-p2.back" "$IN/a100.bin"; then v=RT-OK; else v=RT-DIFF; fi
  chk "a-rt-p2" str "$v" 0
else echo "FAIL a-p2 rc"; FAIL=1; fi
if "$AEA" encrypt -profile 3 -recipient-pub "$WORK/ec-pub.pem" -a none -t 1 -i "$IN/a100.bin" -o "$WORK/a-p3.aea" 2>/dev/null; then
  chk "a-hdr12-p3" str "$(head -c 12 "$WORK/a-p3.aea" | xxd -p | tr -d '\n')" 0
  if "$AEA" decrypt -recipient-priv "$WORK/ec-priv.pem" -i "$WORK/a-p3.aea" -o "$WORK/a-p3.back" 2>/dev/null && cmp -s "$WORK/a-p3.back" "$IN/a100.bin"; then v=RT-OK; else v=RT-DIFF; fi
  chk "a-rt-p3" str "$v" 0
else echo "FAIL a-p3 rc"; FAIL=1; fi
if "$AEA" encrypt -profile 4 -recipient-pub "$WORK/ec-pub.pem" -sign-priv "$WORK/ec-priv.pem" -a none -t 1 -i "$IN/a100.bin" -o "$WORK/a-p4.aea" 2>/dev/null; then
  chk "a-hdr12-p4" str "$(head -c 12 "$WORK/a-p4.aea" | xxd -p | tr -d '\n')" 0
  if "$AEA" decrypt -recipient-priv "$WORK/ec-priv.pem" -sign-pub "$WORK/ec-pub.pem" -i "$WORK/a-p4.aea" -o "$WORK/a-p4.back" 2>/dev/null && cmp -s "$WORK/a-p4.back" "$IN/a100.bin"; then v=RT-OK; else v=RT-DIFF; fi
  chk "a-rt-p4" str "$v" 0
else echo "FAIL a-p4 rc"; FAIL=1; fi
cp "$WORK/a-p1-100.aea" "$WORK/a-app.aea"
head -c 100 /dev/zero > "$IN/a100b.bin"
cat "$IN/a100.bin" "$IN/a100b.bin" > "$WORK/a-app.expect"
if "$AEA" append -key "$WORK/key32.bin" -i "$IN/a100b.bin" -o "$WORK/a-app.aea" 2>/dev/null; then
  chk "a-app-size" size "$(sz "$WORK/a-app.aea")" "$(sz "$WORK/a-app.aea")"
  if "$AEA" decrypt -key "$WORK/key32.bin" -i "$WORK/a-app.aea" -o "$WORK/a-app.back" 2>/dev/null && cmp -s "$WORK/a-app.back" "$WORK/a-app.expect"; then v=RT-OK; else v=RT-DIFF; fi
  chk "a-rt-append" str "$v" 0
else echo "FAIL a-append rc"; FAIL=1; fi
if sh "$ADAPTER" aea-id "$WORK/a-p1-100.aea" 2>/dev/null | grep -q '^[0-9a-f]\{64\}$'; then v=IDHEX; else v=OTHER; fi
chk "a-id-fmt" str "$v" 0
set -- $(AEAa "a-nd1" 1 hex none "a5000.bin"); set -- $(AEAa "a-nd2" 1 hex none "a5000.bin")
if cmp -s "$WORK/a-nd1.aea" "$WORK/a-nd2.aea"; then v=SAME; else v=$(cmp "$WORK/a-nd1.aea" "$WORK/a-nd2.aea" 2>&1 | grep -o 'char [0-9]*' || echo DIFF); fi
chk "a-nondet" str "$v" 0
for P in 1 5; do
  for A in none lzfse; do
    case $P in 1) K="-key $WORK/key32.bin";; 5) K="-password-value $PW";; esac
    # shellcheck disable=SC2086
    if "$AEA" encrypt -profile $P $K -a $A -t 1 -i "$IN/a5000.bin" -o "$WORK/a-t$P$A-1.aea" 2>/dev/null && \
       "$AEA" encrypt -profile $P $K -a $A -t 18 -i "$IN/a5000.bin" -o "$WORK/a-t$P$A-18.aea" 2>/dev/null; then
      [ "$(sz "$WORK/a-t$P$A-1.aea")" = "$(sz "$WORK/a-t$P$A-18.aea")" ] && v=SIZE-EQ || v=SIZE-DIFF
      chk "a-t-$P-$A" str "$v" "$(sz "$WORK/a-t$P$A-1.aea")"
    else echo "FAIL a-t-$P-$A rc"; FAIL=1; fi
  done
done
head -c 200000 /dev/zero > "$IN/a200k.bin"
for F in a5000 a200k; do
  for A in none lzfse; do
    for B in 16b 64k; do
      if "$AEA" encrypt -profile 1 -key "$WORK/key32.bin" -a "$A" -t 1 -b "$B" -i "$IN/$F.bin" -o "$WORK/a-b$F$A$B.aea" 2>/dev/null; then
        chk "a-b-$F-$A-$B" size "$(sz "$WORK/a-b$F$A$B.aea")" "$(sz "$WORK/a-b$F$A$B.aea")"
      else echo "FAIL a-b-$F-$A-$B rc"; FAIL=1; fi
    done
  done
done
for L in 19 20; do
  P=$(head -c "$L" /dev/zero | tr '\0' p)
  if sh "$ADAPTER" aea-encrypt --profile 5 --password "$P" --alg none --threads 1 "$IN/a100.bin" "$WORK/a-pw$L.aea" 2>/dev/null; then rc=0; else rc=$?; fi
  chk "a-pw$L" rc "$rc" 0
done
if sh "$ADAPTER" aea-encrypt --profile 1 --key "$HEX" --alg none --threads 1 "$IN/a100.bin" "$WORK/a-kv-bare.aea" 2>/dev/null; then rc=0; else rc=$?; fi
chk "a-kv-bare" rc "$rc" 0
[ -n "${RECORD:-}" ] && mv "$PINS.new" "$PINS" && echo "RECORDED $PINS"
echo "== $WORK =="
[ "$FAIL" -eq 0 ] && echo OUTER2-GREEN || echo OUTER2-RED
exit "$FAIL"
