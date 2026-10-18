# NOTE-21-writer1s2-hole1bytes (heartbeat10)

## HOLE1 minimal pair PUBLISHED (A-17 debt 1/2 paid)
- HOLE1-pair-A.bin (1024B, hole: NO match@inner-789) vs HOLE1-pair-B.bin (1024B, match(4,off4)@789).
- Differ in EXACTLY 1 byte: file[607] e0->76 (inner-824; md=217). A[600:616]=3a000000c7f793e0c7f793763a276982.
- Match bytes inner[785:793] (=file[568:576]) IDENTICAL in both; decision flips on byte 35B in future.
- Repro: single file `f` in srcdir, oracle aar-encode --alg lz4. A->nseq10 tail lit456; B->nseq11 match@785.
- k600-source note: hole/k600-700 sweep shows NO early flip (101/101 identical early seqs); the flip
  lives in hybr/ L-sweep (L<=3 hole, L>=4 match; pair = y3-input vs y4-input).

## chunk-verdict alternative DEAD (A-17(c))
- hole/ 101/101 + hybr/ 10/10 + titr/16 + runsweep/148 + trip/34: ALL single-bv41 + terminal bv4$.
- Zero bv4- anywhere near; future-dependence is real (marginal-lookahead hunt confirmed real).

## X=0 WITHDRAWN (debt 2/2 closed as artifact)
- Cannot reproduce: fresh wall1-3 x run8/40/60 post-596 (5/5 CHECK, matches fire), titr/ L>=4 13/13
  fire, runsweep/148 fire. Archived X=0 bed unlocatable (no generator, parse-bug era).
- Verdict: likely attempt#1 parse-bug artifact (cf. tripwire/splice/off-by-one corrections). Drop X=0.

## lzma status (self-serve)
- Framing closed (NOTE-20). Stock liblzma (5.4.3/5.8.4, presets 4-7e, mf/nice/mode sweeps) all diverge
  at LZMA byte 44. Next: packet tracer (public-format decoder) -> first-diverging decision -> micro-beds.
