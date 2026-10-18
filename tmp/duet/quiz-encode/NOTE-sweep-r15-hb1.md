# NOTE-sweep-r15-hb1

- CLAIM-sweep-3744141 filed; b195 gate
  battery launched (gate-tip + PYID +
  C-batt + own-loop 65201..65456, sequential,
  seat-private logs r15-3744141/ NVME).
- Lane-diff vs 64d03af first-hand: rgramc.c
  only +1239/-1080, wall 0. New pins 12 N
  (24 rows): 65201 65202 65279 65280 65293
  65357 65407 65408 65421 65435 65455 65456.
- Own build rgramc-own rc=0, 0 warnings.
  PYID corpus seeded 4152 .rav (r14-b193) +
  25 fresh-oracle regen in-script (b194 13 +
  b195 12).
- Added tables 4/4 EQ (M 16/16, Q 16/16,
  C 67n, _N=67). Full audits GREEN: 1D
  167/0, 2D 849/0, dicts 11/0, STR 265/0,
  STRARR 1050/0; b193/b194 baselines confirm
  exact +1 2D / +2 STRARR per-R-band delta.
- Inherit 9/9 IDENTICAL b193->b195 (HYG 13,
  AEA 2, CHIT 42, Mach-O 0, depraw 74/74 +
  survivor known-FP, OSS 37/0-new, LIBC 3,
  ADOPT carried c8f52713/c5f921d5).
- Quiz diff 0 (Q361/A361). Next: battery
  results, GATE filing.
