# NOTE-33 writer1s2 heartbeat: extension closed, finding 486/672, Q-28 open

- EXTENSION CLOSED (single 0-bad/4836, battery EXT-ml first-divs ZERO): 1st-u64-unconditional + dst+8<=B (B=base+cn-121, C=121 exact) + mismatch-refine-in-u64 + NO-refine-at-bound-fail + finding-suppress gpos+4<=FBOUND (universal-126 exact, 760/760 miss@125). MEND-cap (END-124) WITHDRAWN (violated: e=114/120 observed).
- FINDING 486/672 (72%). K-gate load-bearing (+28) but kills real late-occs (bis cross-chunk occ, wide/m3 d=7 SCAN-insert!); NEVER-insert REFUTED (60 proofs). scan-to-end+ungated HURTS (-28, over-insertion). +2-always/matchbytes/ends-always/+1gate/mstart-reinsert/probe-reuse ALL catastrophic (25-34 OK). +1-unconditional + ends-lookahead STAND.
- A-24 ANSWERED (NOTE-32): 0/5 skipper-signal (validation/overwrite misses), Q-15 WITHDRAWN.
- Q-28 OPEN (eviction structure CR-122 for ~31 span>7K files). +2-selective ((ln0,off1)!) + end-K-selective (diverse!) HELD for A-28 (may unify under eviction/table-state).
- lzma re-verified GREEN 6/6. NEXT: A-28 → eviction model → battery; then framing (wrap_pbz4) + test_lz4.sh.
