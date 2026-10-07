#!/bin/sh
# writer2 AEA round 3: id-flip, size sweep, EC profiles, key forms, murmur64, big -b, pw floor.
set -u
OUT=${1:?outdir}
AEA=/usr/bin/aea
R=$OUT/RESULTS-aea.txt
say() { echo "$*" >> "$R"; }
# 1. id semantics: copy + 1-byte flip @1000
cp "$OUT/p1-none-r5000.aea" "$OUT/id-copy.aea"
say "id-copy: $("$AEA" id -i "$OUT/id-copy.aea" 2>&1)"
cp "$OUT/p1-none-r5000.aea" "$OUT/id-flip.aea"
printf '\xff' | dd of="$OUT/id-flip.aea" bs=1 seek=1000 conv=notrunc 2>/dev/null
say "id-flip: $("$AEA" id -i "$OUT/id-flip.aea" 2>&1)"
"$AEA" decrypt -key "$OUT/key32.bin" -i "$OUT/id-flip.aea" -o "$OUT/id-flip.back" 2>"$OUT/id-flip.derr"
say "flip-dec rc=$? err=$(head -c 80 "$OUT/id-flip.derr" | tr '\n' '|')"
# 2. size sweep p1 none
for n in 200 400 600 900 1100 1500 2000 3000 4000 6000 8000 12000; do
  head -c "$n" /dev/urandom > "$OUT/sw$n.bin"
  "$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -i "$OUT/sw$n.bin" -o "$OUT/sw$n.aea" 2>/dev/null
  say "sw-n$n size=$(wc -c < "$OUT/sw$n.aea" | tr -d ' ')"
done
# 3. EC profiles (openssl P-256)
openssl ecparam -name prime256v1 -genkey -noout -out "$OUT/ec-priv.pem" 2>/dev/null
openssl ec -in "$OUT/ec-priv.pem" -pubout -out "$OUT/ec-pub.pem" 2>/dev/null
say "ec-keygen rc=$?"
"$AEA" encrypt -profile 0 -sign-priv "$OUT/ec-priv.pem" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/p0.aea" 2>"$OUT/p0b.err"
say "p0-signpriv rc=$? size=$(wc -c < "$OUT/p0.aea" 2>/dev/null | tr -d ' ') err=$(head -c 80 "$OUT/p0b.err" | tr '\n' '|')"
"$AEA" encrypt -profile 2 -key "$OUT/key32.bin" -sign-priv "$OUT/ec-priv.pem" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/p2.aea" 2>"$OUT/p2.err"
say "p2 rc=$? size=$(wc -c < "$OUT/p2.aea" 2>/dev/null | tr -d ' ') err=$(head -c 80 "$OUT/p2.err" | tr '\n' '|')"
"$AEA" encrypt -profile 3 -recipient-pub "$OUT/ec-pub.pem" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/p3.aea" 2>"$OUT/p3.err"
say "p3 rc=$? size=$(wc -c < "$OUT/p3.aea" 2>/dev/null | tr -d ' ') err=$(head -c 80 "$OUT/p3.err" | tr '\n' '|')"
"$AEA" encrypt -profile 4 -recipient-pub "$OUT/ec-pub.pem" -sign-priv "$OUT/ec-priv.pem" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/p4.aea" 2>"$OUT/p4.err"
say "p4 rc=$? size=$(wc -c < "$OUT/p4.aea" 2>/dev/null | tr -d ' ') err=$(head -c 80 "$OUT/p4.err" | tr '\n' '|')"
# 4. key-value forms (p1)
HEX=$(xxd -p "$OUT/key32.bin" | tr -d '\n')
"$AEA" encrypt -profile 1 -key-value "$HEX" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/kv-bare.aea" 2>"$OUT/kv-bare.err"
say "kv-barehex rc=$? err=$(head -c 80 "$OUT/kv-bare.err" | tr '\n' '|')"
"$AEA" encrypt -profile 1 -key-value "hex:$HEX" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/kv-hex.aea" 2>"$OUT/kv-hex.err"
say "kv-hexpfx rc=$? size=$(wc -c < "$OUT/kv-hex.aea" 2>/dev/null | tr -d ' ') err=$(head -c 80 "$OUT/kv-hex.err" | tr '\n' '|')"
# 5. murmur64
"$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -checksum murmur64 -i "$OUT/in-r5000.bin" -o "$OUT/p1-murmur.aea" 2>/dev/null
say "p1-murmur size=$(wc -c < "$OUT/p1-murmur.aea" | tr -d ' ')"
# 6. big -b (1MB input)
head -c 1000000 /dev/urandom > "$OUT/in-r1m.bin"
for b in 4k 64k 1m; do
  "$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -b "$b" -i "$OUT/in-r1m.bin" -o "$OUT/p1-1m-b$b.aea" 2>/dev/null
  say "p1-1m-b$b size=$(wc -c < "$OUT/p1-1m-b$b.aea" | tr -d ' ')"
done
# 7. password floor (profile 5)
for L in 1 8 16 31 32; do
  P=$(head -c "$L" /dev/zero | tr '\0' 'p')
  "$AEA" encrypt -profile 5 -password-value "$P" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/pw$L.aea" 2>"$OUT/pw$L.err"
  say "pwlen$L rc=$? err=$(head -c 80 "$OUT/pw$L.err" | tr '\n' '|')"
done
echo DONE; tail -40 "$R"
