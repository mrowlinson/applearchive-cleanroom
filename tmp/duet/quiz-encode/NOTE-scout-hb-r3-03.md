# NOTE-scout-hb-r3-03: T2 GREEN seed 7, seed-8 proving T3 hook

- Calls ~35. t2-seeded.sh: T2-SEED7 GREEN, all 27 cells first full
  run (q0 quota; q1 12-arch -b sweep + framing walk + 2 corner
  round-trips; q2 -t pairs; q3 sparse dense/explode/holes; q4
  clone no-SLC; q5 HLC+ignore-flag; q6 omanifest-IDX chain;
  q7 seed guard). One syntax fix (stray fi) before green.
- Adapter extended: frame-archive --block/--omanifest +
  frame-cpio-convert (all oracle-verified; caught+fixed own
  positional-clobber bug pre-test).
- Quiz re-polled: newest Q-361, zero scout-directed; DONE
  unchanged. No joint DONE.
- Next: seed-8 (T3-shape) run, T2=1 wiring + README + FIXTURES
  §9, T0+T1 regression, commit LOCAL ONLY.
