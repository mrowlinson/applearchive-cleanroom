#!/bin/sh
# writer2 AEA round 2: diff-offsets, alg x zeros, id stability, -b, big sizes, profile 0.
set -u
OUT=${1:?outdir}
AEA=/usr/bin/aea
R=$OUT/RESULTS-aea.txt
say() { echo "$*" >> "$R"; }
cmp1=$(cmp "$OUT/p1-none-r5000.aea" "$OUT/p1-none-r5000-rep.aea" 2>&1 || true)
cmp5=$(cmp "$OUT/p5-none-r5000.aea" "$OUT/p5-none-r5000-rep.aea" 2>&1 || true)
say "rep-diff-p1: $cmp1"
say "rep-diff-p5: $cmp5"
PW="w2-aea-bed-passphrase-32-chars-ok!"
for a in lzfse zlib lzma lz4 lzraven lzbitmap; do
  "$AEA" encrypt -profile 5 -password-value "$PW" -a "$a" -t 1 -i "$OUT/in-z5000.bin" -o "$OUT/p5-$a-z5000.aea" 2>/dev/null
  say "p5-$a-z5000 size=$(wc -c < "$OUT/p5-$a-z5000.aea" | tr -d ' ')"
done
say "id-p1-rep: $("$AEA" id -i "$OUT/p1-none-r5000-rep.aea" 2>&1) (orig fe64e1b7...)"
say "id-p5-rep: $("$AEA" id -i "$OUT/p5-none-r5000-rep.aea" 2>&1) (orig 1c578e91...)"
say "id-p1z: $("$AEA" id -i "$OUT/p1-none-z5000.aea" 2>&1)"
for b in 4k 64k 1m; do
  "$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -b "$b" -i "$OUT/in-r5000.bin" -o "$OUT/p1-b$b.aea" 2>"$OUT/b$b.err"
  say "p1-b$b rc=$? size=$(wc -c < "$OUT/p1-b$b.aea" 2>/dev/null | tr -d ' ') err=$(head -c 60 "$OUT/b$b.err")"
done
head -c 16384 /dev/urandom > "$OUT/in-r16384.bin"
head -c 100000 /dev/urandom > "$OUT/in-r100000.bin"
for n in 16384 100000; do
  "$AEA" encrypt -profile 1 -key "$OUT/key32.bin" -a none -t 1 -i "$OUT/in-r$n.bin" -o "$OUT/p1-r$n.aea" 2>/dev/null
  say "p1-none-r$n size=$(wc -c < "$OUT/p1-r$n.aea" | tr -d ' ')"
done
"$AEA" encrypt -profile 0 -t 1 -i "$OUT/in-r100.bin" -o "$OUT/p0.aea" 2>"$OUT/p0.err"
say "p0-bare rc=$? err=$(head -c 120 "$OUT/p0.err" | tr '\n' '|')"
echo DONE; tail -25 "$R"
