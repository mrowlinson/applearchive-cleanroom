#!/bin/sh
# writer2 flip-bisect: pin STORE-vs-COMPRESS rule independently.
# content = K zero bytes + (N-K) fixed-random bytes; ladder K, find flip.
set -u
OUT=${1:?outdir}; N=${2:-2000}; STEP=${3:-100}; KSTART=${4:-0}; KEND=${5:-$N}
AA=/usr/bin/aa
mkdir -p "$OUT"
[ -f "$OUT/seed.bin" ] || head -c "$N" /dev/urandom > "$OUT/seed.bin"
> "$OUT/FLIP.txt"
K=$KSTART
while [ "$K" -le "$KEND" ]; do
  d="$OUT/w"; rm -rf "$d"; mkdir -p "$d"
  { head -c "$K" /dev/zero; dd if="$OUT/seed.bin" bs=1 skip="$K" 2>/dev/null; } > "$d/f.bin"
  touch -t 202001010000 "$d/f.bin" "$d"
  "$AA" archive -d "$d" -a raw -t 1 -o "$OUT/k$K.raw" 2>/dev/null
  "$AA" archive -d "$d" -a lzfse -t 1 -o "$OUT/k$K.aar" 2>/dev/null
  raw=$(wc -c < "$OUT/k$K.raw" | tr -d ' ')
  osz=$(wc -c < "$OUT/k$K.aar" | tr -d ' ')
  head4=$(head -c 4 "$OUT/k$K.aar")
  inner=$(dd if="$OUT/k$K.aar" bs=1 skip=28 count=4 2>/dev/null)
  if [ "$inner" = "AA01" ] && [ "$osz" -eq $((raw + 28)) ]; then
    echo "K=$K unc=$raw STORED" >> "$OUT/FLIP.txt"
  else
    comp=$((osz - 28))
    echo "K=$K unc=$raw COMPRESSED comp=$comp ratio_x10000=$((comp * 10000 / raw))" >> "$OUT/FLIP.txt"
  fi
  K=$((K + STEP))
done
echo DONE; cat "$OUT/FLIP.txt"
