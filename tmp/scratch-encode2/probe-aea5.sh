#!/bin/sh
# writer2 AEA round 5: pw 18/19, auth-data, append (p1 + p3-mainkey).
set -u
OUT=${1:?outdir}
AEA=/usr/bin/aea
R=$OUT/RESULTS-aea.txt
say() { echo "$*" >> "$R"; }
for L in 18 19; do
  P=$(head -c "$L" /dev/zero | tr '\0' 'p')
  "$AEA" encrypt -profile 5 -password-value "$P" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/pw$L.aea" 2>"$OUT/pw$L.err"
  say "pwlen$L rc=$? err=$(head -c 50 "$OUT/pw$L.err" | tr '\n' '|')"
done
"$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -auth-data-value deadbeef -i "$OUT/in-r100.bin" -o "$OUT/ad-v.aea" 2>"$OUT/ad-v.err"
say "ad-value rc=$? size=$(wc -c < "$OUT/ad-v.aea" 2>/dev/null | tr -d ' ') (baseline 19456) err=$(head -c 60 "$OUT/ad-v.err" | tr '\n' '|')"
"$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -auth-data-key mykey -auth-data-value deadbeef -i "$OUT/in-r100.bin" -o "$OUT/ad-kv.aea" 2>"$OUT/ad-kv.err"
say "ad-keyvalue rc=$? size=$(wc -c < "$OUT/ad-kv.aea" 2>/dev/null | tr -d ' ') err=$(head -c 60 "$OUT/ad-kv.err" | tr '\n' '|')"
"$AEA" decrypt -key "$OUT/key32.bin" -i "$OUT/ad-kv.aea" -o "$OUT/ad-kv.back" 2>/dev/null
cmp -s "$OUT/ad-kv.back" "$OUT/in-r100.bin" && say "ad-kv RT-OK" || say "ad-kv RT-DIFF"
head -c 100 /dev/urandom > "$OUT/in-r100b.bin"
cp "$OUT/p1-none-r100.aea" "$OUT/app1.aea"
"$AEA" append -key "$OUT/key32.bin" -i "$OUT/in-r100b.bin" -o "$OUT/app1.aea" 2>"$OUT/app1.err"
say "app-p1 rc=$? size=$(wc -c < "$OUT/app1.aea" 2>/dev/null | tr -d ' ') err=$(head -c 60 "$OUT/app1.err" | tr '\n' '|')"
"$AEA" decrypt -key "$OUT/key32.bin" -i "$OUT/app1.aea" -o "$OUT/app1.back" 2>/dev/null
cat "$OUT/in-r100.bin" "$OUT/in-r100b.bin" > "$OUT/app1.expect"
cmp -s "$OUT/app1.back" "$OUT/app1.expect" && say "app-p1 RT-CONCAT-OK" || say "app-p1 RT-DIFF size=$(wc -c < "$OUT/app1.back" 2>/dev/null | tr -d ' ')"
"$AEA" encrypt -profile 3 -recipient-pub "$OUT/ec-pub.pem" -main-key "$OUT/p3.mainkey" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/app3.aea" 2>"$OUT/app3e.err"
say "p3-mainkey-enc rc=$? err=$(head -c 60 "$OUT/app3e.err" | tr '\n' '|')"
"$AEA" append -main-key "$OUT/p3.mainkey" -i "$OUT/in-r100b.bin" -o "$OUT/app3.aea" 2>"$OUT/app3.err"
say "app-p3 rc=$? size=$(wc -c < "$OUT/app3.aea" 2>/dev/null | tr -d ' ') err=$(head -c 60 "$OUT/app3.err" | tr '\n' '|')"
"$AEA" decrypt -recipient-priv "$OUT/ec-priv.pem" -i "$OUT/app3.aea" -o "$OUT/app3.back" 2>/dev/null
cmp -s "$OUT/app3.back" "$OUT/app1.expect" && say "app-p3 RT-CONCAT-OK" || say "app-p3 RT-DIFF"
echo DONE; tail -14 "$R"
