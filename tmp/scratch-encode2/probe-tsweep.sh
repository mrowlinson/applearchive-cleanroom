#!/bin/sh
# writer2 thread-sweep: outer byte-determinism over -t (single/multi-block, stored/compressed).
# 5MB inputs (2 blocks @4m) x -t {1,2,4,18} + -b1m 5-block t1/t18 + default-t. execute+observe only.
set -u
OUT=${1:?outdir}
AA=/usr/bin/aa
mkdir -p "$OUT"
> "$OUT/TSWEEP.txt"
say() { echo "$*" >> "$OUT/TSWEEP.txt"; }
python3 -c "import random; open('$OUT/big-r.bin','wb').write(random.Random(7).randbytes(5000000))"
head -c 5000000 /dev/zero > "$OUT/big-z.bin"
for k in r z; do
  rm -rf "$OUT/w$k"; mkdir -p "$OUT/w$k"
  cp "$OUT/big-$k.bin" "$OUT/w$k/f.bin"
  touch -t 202001010000 "$OUT/w$k/f.bin" "$OUT/w$k"
done
for k in r z; do
  for t in 1 2 4 18; do
    "$AA" archive -d "$OUT/w$k" -a lzfse -t "$t" -o "$OUT/$k-t$t.aar" 2>/dev/null
    say "$k-t$t size=$(wc -c < "$OUT/$k-t$t.aar" | tr -d ' ') sha=$(shasum -a 256 "$OUT/$k-t$t.aar" | cut -c1-16)"
  done
done
for k in r z; do
  for t in 2 4 18; do
    cmp -s "$OUT/$k-t1.aar" "$OUT/$k-t$t.aar" && say "$k-t1==t$t EQ" || say "$k-t1==t$t DIFF"
  done
done
"$AA" archive -d "$OUT/wr" -a lzfse -t 1 -b 1m -o "$OUT/r-b1m-t1.aar" 2>/dev/null
"$AA" archive -d "$OUT/wr" -a lzfse -t 18 -b 1m -o "$OUT/r-b1m-t18.aar" 2>/dev/null
cmp -s "$OUT/r-b1m-t1.aar" "$OUT/r-b1m-t18.aar" && say "B1M-T1-T18-EQ" || say "B1M-T1-T18-DIFF"
"$AA" archive -d "$OUT/wr" -a lzfse -o "$OUT/r-default-t.aar" 2>/dev/null
cmp -s "$OUT/r-t18.aar" "$OUT/r-default-t.aar" && say "DEFAULT-T-EQ-T18" || say "DEFAULT-T-DIFF"
echo DONE; cat "$OUT/TSWEEP.txt"
