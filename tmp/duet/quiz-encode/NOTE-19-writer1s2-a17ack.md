# NOTE-19-writer1s2-a17ack (heartbeat8)

A-17 ACKED (Q-13 skipclasses). lzma framing fitted in parallel (self-serve oracle).

## a17-takeaways
- EVICTION class: hash table confirmed, 50% ~8.5K inserts, hard-0 ~11.5K, last-pos 2x, ext-precise.
- TAIL-ZONE ~128 confirmed. (b) hash-from-metadata NONE-FOUND, table ~8-16K behavioral.
- (c) one-pass plain dups; HOLE1: kill chunk-verdict-flip alternative first (bv41 vs bv4-).
- DEBTS (mine): X=0 minimal-pair bytes + HOLE1/k600 bytes (P2+walls) + HOLE1 chunk verdicts. Extracting from beds next.

## lzma-framing (fitted, oracle-first-hand)
- Streams: inner split 4MB (f2=4194304 confirms); each indep XZ; gap [u64 unc][u64 clen]; hdr=(s1 unc,c).
- Chunks: fill <=2MB snap packet-end (chunk0=md+2096877 const 7/7 fine sweep; m3s1 j=7681x273 exact).
- XZ: flags 0000, block 0xc0, dict 0x16, props 0x5d, rs3-first/rs0-rest; b0: fields11->+4 overpad.
- Store path: rnd100 c==unc, raw inner, NO flag diff (store-decision rule OPEN).
- Next: store-threshold sweep + mixed-region stream-independence + liblzma preset compare.
