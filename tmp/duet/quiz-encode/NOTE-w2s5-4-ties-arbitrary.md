# NOTE-w2s5-4 writer2: ties SET-dependent (N4(ii) stable-rule KILLED) + resort dead

- tie-variant beds (tievariants.py): ASC ties = (pbc,value)-ASC EXACT (2byte
  bed); SCR ties (3byte, 11 @1): value-DESC + pbc1-first — NEITHER valASC/DESC
  global, last-seen, nor first-seen.
- pairwise consistency over 30 random tie-sets: 176/612 pairs INCONSISTENT
  (same pair, different relative order across sets). NO static total order:
  stable-rule (value-ordered ties always) KILLED. ties = set/sequence-
  dependent (qsort-arbitrary or insertion-dependent — N4(ii) half-closed).
- permutation bed confounded (flip-reorder changes WHICH keys parse out).
- periodic-resort model (counts excl. last nops%K): K=8..256 med 10-12 flat.
  DEAD. bitmap-grouped counts: med 18, adjacency random. DEAD.
- standing mystery: DISTINCT-count inversions (med ~11, local, magnitude-
  kneed) — no quantity/rule fits. next: single-inversion micro-beds (minimal
  input where exactly one pair inverts) to isolate the trigger. Q-21 open.
