#!/bin/sh
# writer2 AEA-encrypt beds: black-box `aea` behavior. execute + observe I/O only.
set -u
OUT=${1:?outdir}
AEA=/usr/bin/aea
mkdir -p "$OUT"
> "$OUT/RESULTS-aea.txt"
say() { echo "$*" >> "$OUT/RESULTS-aea.txt"; }
"$AEA" -h > "$OUT/aea-h.txt" 2>&1; "$AEA" encrypt -h > "$OUT/aea-encrypt-h.txt" 2>&1
say "help_bytes: $(wc -c < "$OUT/aea-h.txt" | tr -d ' ') $(wc -c < "$OUT/aea-encrypt-h.txt" | tr -d ' ')"
head -c 5000 /dev/urandom > "$OUT/seed5k.bin"
: > "$OUT/empty.bin"
for n in 1 100 1000 5000; do
  head -c "$n" "$OUT/seed5k.bin" > "$OUT/in-r$n.bin"
  head -c "$n" /dev/zero > "$OUT/in-z$n.bin"
done
head -c 32 /dev/urandom > "$OUT/key32.bin"
KEYSHA=$(shasum -a 256 "$OUT/key32.bin" | cut -c1-16)
PW="w2-aea-bed-passphrase-32-chars-ok!"
say "key32sha16=$KEYSHA pwlen=${#PW}"
enc() { # $1=tag $2=profile $3=keymode $4=alg $5=in [$6... extra flags]
  tag=$1; prof=$2; km=$3; alg=$4; in=$5; shift 5
  case $km in
    key) KO="-key $OUT/key32.bin";;
    pw) KO="-password-value $PW";;
  esac
  # shellcheck disable=SC2086
  "$AEA" encrypt -profile "$prof" $KO -a "$alg" -t 1 "$@" -i "$in" -o "$OUT/$tag.aea" 2>"$OUT/$tag.err"
  rc=$?
  if [ $rc -ne 0 ]; then say "$tag RC=$rc ERR=$(head -c 100 "$OUT/$tag.err" | tr '\n' '|')"; return; fi
  sz=$(wc -c < "$OUT/$tag.aea" | tr -d ' ')
  hd=$(head -c 16 "$OUT/$tag.aea" | xxd -p | tr -d '\n')
  say "$tag size=$sz head16=$hd"
}
for n in 1 100 1000 5000; do
  enc "p1-none-z$n" 1 key none "$OUT/in-z$n.bin"
  enc "p1-none-r$n" 1 key none "$OUT/in-r$n.bin"
  enc "p5-none-z$n" 5 pw none "$OUT/in-z$n.bin"
  enc "p5-none-r$n" 5 pw none "$OUT/in-r$n.bin"
done
enc "p1-none-empty" 1 key none "$OUT/empty.bin"
enc "p5-none-empty" 5 pw none "$OUT/empty.bin"
for a in lzfse zlib lzma lz4 lzraven lzbitmap; do enc "p5-$a-r5000" 5 pw "$a" "$OUT/in-r5000.bin"; done
enc "p1-lzfse-r5000" 1 key lzfse "$OUT/in-r5000.bin"
for p in none adaptive; do enc "p1-pad$p-r5000" 1 key none "$OUT/in-r5000.bin" -padding "$p"; done
for c in none sha256; do enc "p1-cks$c-r5000" 1 key none "$OUT/in-r5000.bin" -checksum "$c"; done
enc "p1-none-r5000-rep" 1 key none "$OUT/in-r5000.bin"
enc "p5-none-r5000-rep" 5 pw none "$OUT/in-r5000.bin"
dec() { # $1=tag $2=src $3=keymode $4=expect
  tag=$1
  case $3 in
    key) KO="-key $OUT/key32.bin";;
    pw) KO="-password-value $PW";;
  esac
  # shellcheck disable=SC2086
  "$AEA" decrypt $KO -i "$2" -o "$OUT/$tag.back" 2>"$OUT/$tag.derr"; rc=$?
  if [ $rc -ne 0 ]; then say "$tag-dec RC=$rc"; return; fi
  cmp -s "$OUT/$tag.back" "$4" && say "$tag-dec RT-OK" || say "$tag-dec RT-DIFF"
}
dec "p1-none-r5000" "$OUT/p1-none-r5000.aea" key "$OUT/in-r5000.bin"
dec "p5-none-r5000" "$OUT/p5-none-r5000.aea" pw "$OUT/in-r5000.bin"
dec "p5-lzfse-r5000" "$OUT/p5-lzfse-r5000.aea" pw "$OUT/in-r5000.bin"
"$AEA" id -i "$OUT/p1-none-r5000.aea" > "$OUT/id-p1.txt" 2>&1; say "id-p1 rc=$? out=$(cat "$OUT/id-p1.txt")"
"$AEA" id -i "$OUT/p5-none-r5000.aea" > "$OUT/id-p5.txt" 2>&1; say "id-p5 rc=$? out=$(cat "$OUT/id-p5.txt")"
echo DONE; cat "$OUT/RESULTS-aea.txt"
