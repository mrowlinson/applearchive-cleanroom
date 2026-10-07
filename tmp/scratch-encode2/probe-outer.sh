#!/bin/sh
# writer2 outer-wrapper probes: black-box `aa archive` outer framing.
# execute + observe I/O only. fixed mtimes (nsec=0) for determinism.
set -u
OUT=${1:?outdir}
AA=/usr/bin/aa
mkdir -p "$OUT"
> "$OUT/RESULTS.txt"

mkinput() { # $1=dir $2=sizebytes : one file f.bin of zeros, fixed mtime
  d=$1; n=$2; rm -rf "$d"; mkdir -p "$d"
  if [ "$n" -gt 0 ]; then head -c "$n" /dev/zero > "$d/f.bin"; else : > "$d/f.bin"; fi
  touch -t 202001010000 "$d/f.bin" "$d"
}

one() { # $1=tag $2=srcdir $3=alg $4=extra-args
  tag=$1; src=$2; alg=$3; extra=$4; f="$OUT/$tag.aar"
  # shellcheck disable=SC2086
  "$AA" archive -d "$src" -a "$alg" -t 1 $extra -o "$f" 2>"$OUT/$tag.err"
  rc=$?
  if [ $rc -ne 0 ]; then echo "$tag RC=$rc ERR=$(cat "$OUT/$tag.err")" >> "$OUT/RESULTS.txt"; return; fi
  sz=$(wc -c < "$f" | tr -d ' ')
  magic=$(head -c 16 "$f" | xxd -p | tr -d '\n')
  sha=$(shasum -a 256 "$f" | cut -c1-16)
  echo "$tag size=$sz magic16=$magic sha16=$sha" >> "$OUT/RESULTS.txt"
}

BASE="$OUT/inputs"; mkdir -p "$BASE"
# size sweep, zeros (highly compressible)
for n in 0 1 16 1000 65535 65536 70000 200000; do mkinput "$BASE/z$n" "$n"; done
# size sweep, random (incompressible) — fixed seed via openssl
for n in 1000 70000; do
  rm -rf "$BASE/r$n"; mkdir -p "$BASE/r$n"
  openssl rand -out "$BASE/r$n/f.bin" "$n" 2>/dev/null || head -c "$n" /dev/urandom > "$BASE/r$n/f.bin"
  touch -t 202001010000 "$BASE/r$n/f.bin" "$BASE/r$n"
done
# empty dir input
rm -rf "$BASE/empty"; mkdir -p "$BASE/empty"; touch -t 202001010000 "$BASE/empty"

for alg in raw lzfse lzma lz4 zlib lzraven lzbitmap; do
  one "empty-$alg" "$BASE/empty" "$alg" ""
  one "z0-$alg" "$BASE/z0" "$alg" ""
  one "z1-$alg" "$BASE/z1" "$alg" ""
  one "z16-$alg" "$BASE/z16" "$alg" ""
  one "z1000-$alg" "$BASE/z1000" "$alg" ""
  one "z65535-$alg" "$BASE/z65535" "$alg" ""
  one "z65536-$alg" "$BASE/z65536" "$alg" ""
  one "z70000-$alg" "$BASE/z70000" "$alg" ""
  one "z200000-$alg" "$BASE/z200000" "$alg" ""
  one "r1000-$alg" "$BASE/r1000" "$alg" ""
  one "r70000-$alg" "$BASE/r70000" "$alg" ""
done
# determinism: repeat 2 cells
one "z1000-lzfse-rep" "$BASE/z1000" lzfse ""
one "r70000-lzma-rep" "$BASE/r70000" lzma ""
# blocksize + threads effects on outer bytes
one "z200000-lzfse-b16" "$BASE/z200000" lzfse "-b 16"
one "z200000-lzfse-b20" "$BASE/z200000" lzfse "-b 20"
one "z200000-lzfse-t4" "$BASE/z200000" lzfse "-t 4"
echo DONE; cat "$OUT/RESULTS.txt"
