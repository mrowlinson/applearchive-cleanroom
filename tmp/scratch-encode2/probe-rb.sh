#!/bin/sh
# writer2 raven/bitmap byte beds (aa-only black-box): ladders + payload capture + chain walk.
set -u
OUT=${1:?outdir}
AA=/usr/bin/aa
mkdir -p "$OUT"
> "$OUT/RESULTS-rb.txt"
say() { echo "$*" >> "$R"; }; R=$OUT/RESULTS-rb.txt
BASE=$OUT/inputs; mkdir -p "$BASE"
rm -rf "$BASE/empty"; mkdir -p "$BASE/empty"; touch -t 202001010000 "$BASE/empty"
for n in 100 1000 10000 100000; do
  rm -rf "$BASE/z$n"; mkdir -p "$BASE/z$n"; head -c "$n" /dev/zero > "$BASE/z$n/f.bin"
  touch -t 202001010000 "$BASE/z$n/f.bin" "$BASE/z$n"
  rm -rf "$BASE/r$n"; mkdir -p "$BASE/r$n"
  python3 -c "import random; open('$BASE/r$n/f.bin','wb').write(random.Random(5000 + $n).randbytes($n))"
  touch -t 202001010000 "$BASE/r$n/f.bin" "$BASE/r$n"
done
cell() { # tag input alg [block]
  tag=$1; src=$2; alg=$3; blk=${4:-}
  if [ -n "$blk" ]; then BO="-b $blk"; else BO=""; fi
  # shellcheck disable=SC2086
  "$AA" archive -d "$BASE/$src" -a "$alg" -t 1 $BO -o "$OUT/$tag.aar" 2>"$OUT/$tag.err"
  rc=$?
  if [ $rc -ne 0 ]; then say "$tag RC=$rc"; return; fi
  f=$OUT/$tag.aar
  sz=$(wc -c < "$f" | tr -d ' ')
  magic=$(head -c 16 "$f" | xxd -p | tr -d '\n')
  bh=$(xxd -s 12 -l 16 -p "$f" | tr -d '\n')
  pay=$(dd if="$f" bs=1 skip=28 count=32 2>/dev/null | xxd -p | tr -d '\n')
  say "$tag size=$sz magic16=$magic blkhdr16=$bh pay32=$pay"
}
for a in lzraven lzbitmap; do
  cell "empty-$a" empty "$a"
  for n in 100 1000 10000 100000; do
    cell "z$n-$a" "z$n" "$a"
    cell "r$n-$a" "r$n" "$a"
  done
  cell "z100000-$a-b10k" z100000 "$a" 10000
  cell "r100000-$a-b10k" r100000 "$a" 10000
done
cell "z100000-raw" z100000 raw
cell "r100000-raw" r100000 raw
echo DONE; cat "$OUT/RESULTS-rb.txt"
