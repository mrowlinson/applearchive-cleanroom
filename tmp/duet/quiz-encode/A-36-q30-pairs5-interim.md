# A-36 Q-30 INTERIM (attempt#5): single-gram kills are cover-artifacts; pairs impossible under S=5

## artifact (v5q30 first-hand, T=94dd1fa95673375c PH1-shape)
- 12/3161 single-gram fillers "kill" T — ALL end in 0x96 = PRE[99].
  mechanism: filler-tail + T == PRE[99:108] (9B match @p-1 off 16)
  COVERS p. parse overlap, not eviction. mutants confirm: pos0-6
  mutants (still ..96) kill; pos7 (..97) fires.
- clean-miss single-gram kill rate: 0/3161 (pending retest with
  no-cover criterion — running).

## model verdict (derived, constrains their fit)
- under S=5 distinct-LRU (CR-129, this same T), a PAIR cannot evict at
  low N: minimum killing set = 5 co-bucket distinct grams (~10K hunt
  to find, then minimize). "mutual pair-ejection" needs S=1 — REFUTED
  for this table. the atom is a 5-SET, not a pair.
- their B=2048/S=5 implementation choice is consistent with this; hashmode fit
  must use SETS (below), not pairs.

## final coming (ETA ~15min): 3-5 minimized killing SETS (drop-one from
  12K-killer via neutral-gram substitution, layout-fixed) with hex per
  gram + N (distinct count) + load-bearing proof per gram + 1-byte
  mutant panel on one set + symmetry (singles-never-evict) confirm.
- dual-seat: attempt#6 may file own A-36 — different slug, both stand;
  compare values, mine are the -attempt5- files.
