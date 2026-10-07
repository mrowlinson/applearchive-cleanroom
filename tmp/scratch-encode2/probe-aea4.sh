#!/bin/sh
# writer2 AEA round 4: EC headers+roundtrips, kv cross-forms, -b x lzfse, pw floor, murmur RT.
set -u
OUT=${1:?outdir}
AEA=/usr/bin/aea
R=$OUT/RESULTS-aea.txt
say() { echo "$*" >> "$R"; }
for p in p0 p2 p3 p4; do say "hdr-$p: $(head -c 16 "$OUT/$p.aea" | xxd -p | tr -d '\n')"; done
D() { # $1=tag $2=src $3=expect $@=keyflags
  tag=$1; src=$2; exp=$3; shift 3
  "$AEA" decrypt "$@" -i "$src" -o "$OUT/$tag.back" 2>"$OUT/$tag.derr"; rc=$?
  if [ $rc -ne 0 ]; then say "$tag rc=$rc err=$(head -c 70 "$OUT/$tag.derr" | tr '\n' '|')"; return; fi
  cmp -s "$OUT/$tag.back" "$exp" && say "$tag RT-OK" || say "$tag RT-DIFF"
}
D "p0-dec-pub" "$OUT/p0.aea" "$OUT/in-r100.bin" -sign-pub "$OUT/ec-pub.pem"
D "p2-dec-key" "$OUT/p2.aea" "$OUT/in-r100.bin" -key "$OUT/key32.bin"
D "p2-dec-keypub" "$OUT/p2.aea" "$OUT/in-r100.bin" -key "$OUT/key32.bin" -sign-pub "$OUT/ec-pub.pem"
D "p3-dec-rpriv" "$OUT/p3.aea" "$OUT/in-r100.bin" -recipient-priv "$OUT/ec-priv.pem"
D "p4-dec-rpriv" "$OUT/p4.aea" "$OUT/in-r100.bin" -recipient-priv "$OUT/ec-priv.pem"
D "p4-dec-both" "$OUT/p4.aea" "$OUT/in-r100.bin" -recipient-priv "$OUT/ec-priv.pem" -sign-pub "$OUT/ec-pub.pem"
D "kv-hex-filedec" "$OUT/kv-hex.aea" "$OUT/in-r100.bin" -key "$OUT/key32.bin"
HEX=$(xxd -p "$OUT/key32.bin" | tr -d '\n')
D "fileenc-hexdec" "$OUT/p1-none-r100.aea" "$OUT/in-r100.bin" -key-value "hex:$HEX"
B64=$(base64 < "$OUT/key32.bin")
"$AEA" encrypt -profile 1 -key-value "base64:$B64" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/kv-b64.aea" 2>"$OUT/kv-b64.err"
say "kv-b64pfx rc=$? size=$(wc -c < "$OUT/kv-b64.aea" 2>/dev/null | tr -d ' ')"
"$AEA" encrypt -profile 1 -key-value "$B64" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/kv-b64bare.aea" 2>"$OUT/kv-b64bare.err"
say "kv-b64bare rc=$? err=$(head -c 60 "$OUT/kv-b64bare.err" | tr '\n' '|')"
head -c 1000000 /dev/zero > "$OUT/in-z1m.bin"
for b in 4k 64k 1m; do
  "$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a lzfse -t 1 -b "$b" -i "$OUT/in-z1m.bin" -o "$OUT/p1z1m-b$b.aea" 2>/dev/null
  say "p1z1m-b$b size=$(wc -c < "$OUT/p1z1m-b$b.aea" | tr -d ' ')"
  "$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a lzfse -t 1 -b "$b" -i "$OUT/in-r1m.bin" -o "$OUT/p1r1m-b$b.aea" 2>/dev/null
  say "p1r1m-b$b size=$(wc -c < "$OUT/p1r1m-b$b.aea" | tr -d ' ')"
done
D "p1-murmur-rt" "$OUT/p1-murmur.aea" "$OUT/in-r5000.bin" -key "$OUT/key32.bin"
for L in 17 20 23 26 29; do
  P=$(head -c "$L" /dev/zero | tr '\0' 'p')
  "$AEA" encrypt -profile 5 -password-value "$P" -a none -t 1 -i "$OUT/in-r100.bin" -o "$OUT/pw$L.aea" 2>"$OUT/pw$L.err"
  say "pwlen$L rc=$? err=$(head -c 50 "$OUT/pw$L.err" | tr '\n' '|')"
done
echo DONE; tail -30 "$R"
