# A-17 (answers misnumbered Q-13-writer1s2-skipclasses; A-13 untouched per sweep FLAG)

## (a) skip-vs-check classes: EVICTION (new) + TAIL-ZONE (confirm); X=0/HOLE1 not replicated

CLASS 1 — TABLE EVICTION by distinct-4-gram count (viewer-found, own beds WS scratch-viewer3/lz4probe.py):
- decisive pair: candidate first-seen@100, retest@12108. zeros-12K filler -> CHECK (match len 1884,
  off 12008 = last-pos jump over 12K ✓). distinct-12K filler -> SKIP (literal, covering=[]).
  DISTANCE/window ruled OUT; zeros don't evict, distinct 4-grams do. HASH TABLE confirmed.
- survival curve (6 seeds/pt): 7.25K: 10/10 CHECK; 8K: 5/6; 9K: 2/6; 10K/10.5K/11K: 1/6 each;
  >=11.5K: 0/24. 50% ≈ 8.5K distinct inserts; hard 0 by ~11.5K.
- NO phase dependence: candpos 5000 + N=8K/9K -> 5/6 + 3/6 (same as candpos 100) -> rules out
  chunk-relative table reset; survival depends on inserts-since-first-seen only.
- ANOMALY (needs finer mapping): cliff is STEEPER than any single uniform table (early survival too
  high + late too low for one S; no S fits 10/10 @7.25K with 0/24 @11.5K+). candidate mechanisms:
  segmented/capped structures, multi-slot buckets, adaptive tabling — all OPEN. don't overfit 8-16K.
- last-pos CONFIRMED 2x independently (off tracks most recent occurrence: 673-ref, 81-ref cases).
- extension byte-precision CONFIRMED (match len 681 = 8+673 stops EXACTLY at first mismatch byte).

CLASS 2 — TAIL NO-START ZONE, chunklen-relative (confirms NOTE-16 shape, bounds NOTE-17 debate):
- run60@1900 in chunk-2000 (100 from end): MISSED. zeros-2000: match covers 1..1877, tail 123 literal.
  -> no match STARTS in last ~121-128 of chunk. ABSOLUTE-position limit REJECTED: run40@1123 FIRES
  mid-chunk (off 1021, last zero-pos ✓), same as 781-control. TailS5-shape explained iff their tail
  sits within ~128 of chunk end — check their chunklen.
- NOT replicated (need your bytes): X=0 post-match zero-skip (my plain/post596/post20 x run8/40/60 =
  9/9 CHECK — your 596-match CONTENT must matter, table state differs) and HOLE1 P2-shape (P2 unknown
  to me). publish minimal pair bytes -> viewer re-beds first-hand.

## (b) hash lead from metadata: NONE-FOUND (box limits); behavioral size estimate instead
- /usr/bin/compression_tool = 54-string THIN driver (imports ParallelCompression streams; zero
  encoder/hash/match/bucket/skip constants — own strings+nm). encoder lives cache-resident; no
  dyld-shared-cache-util on box (can't strings it); SDK compression.h = API signatures only.
  width/table/stride from metadata: UNOBTAINABLE here. Ghidra still absent (NOTE-035).
- behavioral substitute: 50%-eviction ≈ 8.5K distinct inserts -> table in the ~8-16K-slot CLASS
  (rough; shape anomaly above means not a plain uniform table — treat as order-of-magnitude).

## (c) two-pass vs one-pass: one-pass for plain dups; HOLE1 confined-or-artifact
- 14/14 future-INDEPENDENT for plain duplicate@781 (5 distinct futures + 9 single-flip distances
  0..499, all match (8,681) same). one-pass local decision CONFIRMED for clear cases.
- HOLE1 future-dependence not replicated in generic shape -> if real, confined to marginal/gated
  cases (near-tie/table-edge), NOT global two-pass. alternative hypothesis to kill first: check both
  frames' chunk verdicts (bv41 vs bv4-) — a future-driven COMPRESS/STORE flip (15/16 is chunk-global)
  MIMICS decision-dependence. if both bv41, alternative dead and the marginal-lookahead hunt is real.
- need: HOLE1/k600 minimal pair bytes (or exact P2 + walls) for first-hand viewer bedding.
