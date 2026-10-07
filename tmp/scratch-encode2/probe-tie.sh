#!/bin/sh
# writer2 tie-hunt: exact 16*comp == 15*unc -> COMPRESS (<=) or STORE (<)?
# unc=2224 (name len 8), target comp=2085. same seed as out-flip.
set -u
OUT=${1:?outdir}; KSTART=${2:-88}; KEND=${3:-98}; NAME=${4:-abcd.bin}
AA=/usr/bin/aa
mkdir -p "$OUT"
> "$OUT/TIE.txt"
K=$KSTART
while [ "$K" -le "$KEND" ]; do
  d="$OUT/w"; rm -rf "$d"; mkdir -p "$d"
  { head -c "$K" /dev/zero 2>/dev/null; dd if="$OUT/seed.bin" bs=1 skip="$K" 2>/dev/null; } > "$d/$NAME"
  touch -t 202001010000 "$d/$NAME" "$d"
  "$AA" archive -d "$d" -a raw -t 1 -o "$OUT/k$K.raw" 2>/dev/null
  "$AA" archive -d "$d" -a lzfse -t 1 -o "$OUT/k$K.aar" 2>/dev/null
  raw=$(wc -c < "$OUT/k$K.raw" | tr -d ' ')
  osz=$(wc -c < "$OUT/k$K.aar" | tr -d ' ')
  inner=$(dd if="$OUT/k$K.aar" bs=1 skip=28 count=4 2>/dev/null)
  if [ "$inner" = "AA01" ] && [ "$osz" -eq $((raw + 28)) ]; then
    echo "K=$K unc=$raw STORED" >> "$OUT/TIE.txt"
  else
    comp=$((osz - 28))
    tie=""; [ $((16 * comp)) -eq $((15 * raw)) ] && tie=" TIE-EXACT"
    echo "K=$K unc=$raw COMPRESSED comp=$comp 16c=$((16*comp)) 15u=$((15*raw))$tie" >> "$OUT/TIE.txt"
  fi
  K=$((K + 1))
done
echo DONE; cat "$OUT/TIE.txt"
