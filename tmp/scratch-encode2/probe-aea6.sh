#!/bin/sh
# writer2 AEA round 6: auth hex: prefix, append p3+pub, append p5.
set -u
OUT=${1:?outdir}
AEA=/usr/bin/aea
R=$OUT/RESULTS-aea.txt
say() { echo "$*" >> "$R"; }
"$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -auth-data-value hex:deadbeef -i "$OUT/in-r100.bin" -o "$OUT/ad-v2.aea" 2>"$OUT/ad-v2.err"
say "ad-value-hex rc=$? size=$(wc -c < "$OUT/ad-v2.aea" 2>/dev/null | tr -d ' ') (baseline 19456) err=$(head -c 60 "$OUT/ad-v2.err" | tr '\n' '|')"
"$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -auth-data-key mykey -auth-data-value hex:deadbeef -i "$OUT/in-r100.bin" -o "$OUT/ad-kv2.aea" 2>"$OUT/ad-kv2.err"
say "ad-keyvalue-hex rc=$? size=$(wc -c < "$OUT/ad-kv2.aea" 2>/dev/null | tr -d ' ') err=$(head -c 60 "$OUT/ad-kv2.err" | tr '\n' '|')"
"$AEA" decrypt -key "$OUT/key32.bin" -i "$OUT/ad-kv2.aea" -o "$OUT/ad-kv2.back" 2>/dev/null
cmp -s "$OUT/ad-kv2.back" "$OUT/in-r100.bin" && say "ad-kv2 RT-OK" || say "ad-kv2 RT-DIFF"
"$AEA" append -main-key "$OUT/p3.mainkey" -recipient-pub "$OUT/ec-pub.pem" -i "$OUT/in-r100b.bin" -o "$OUT/app3.aea" 2>"$OUT/app3b.err"
say "app-p3b rc=$? size=$(wc -c < "$OUT/app3.aea" 2>/dev/null | tr -d ' ') err=$(head -c 60 "$OUT/app3b.err" | tr '\n' '|')"
"$AEA" decrypt -recipient-priv "$OUT/ec-priv.pem" -i "$OUT/app3.aea" -o "$OUT/app3.back" 2>/dev/null
cmp -s "$OUT/app3.back" "$OUT/app1.expect" && say "app-p3 RT-CONCAT-OK" || say "app-p3 RT-DIFF"
PW="w2-aea-bed-passphrase-32-chars-ok!"
cp "$OUT/p5-none-r100.aea" "$OUT/app5.aea"
"$AEA" append -password-value "$PW" -i "$OUT/in-r100b.bin" -o "$OUT/app5.aea" 2>"$OUT/app5.err"
say "app-p5 rc=$? size=$(wc -c < "$OUT/app5.aea" 2>/dev/null | tr -d ' ') err=$(head -c 60 "$OUT/app5.err" | tr '\n' '|')"
"$AEA" decrypt -password-value "$PW" -i "$OUT/app5.aea" -o "$OUT/app5.back" 2>/dev/null
cmp -s "$OUT/app5.back" "$OUT/app1.expect" && say "app-p5 RT-CONCAT-OK" || say "app-p5 RT-DIFF"
echo DONE; tail -10 "$R"
