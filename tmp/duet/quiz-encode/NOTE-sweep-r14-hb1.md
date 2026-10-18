# NOTE-sweep-r14-hb1

- CLAIM-sweep-94a0e0b filed; b191 gate
  battery launched (gate-tip + PYID +
  C-batt + own-loop 64505..64760, sequential,
  seat-private logs r14-94a0e0b/ NVME).
- Lane-diff vs 91bdc21 first-hand: rgramc.c
  only +1227/-1068, wall 0. New pins 12 N
  (24 rows): 64505 64506 64511 64512 64525
  64589 64639 64640 64653 64717 64759 64760.
- Own build rgramc-own rc=0, 0 warnings.
  PYID corpus seeded 4101 .rav (r13) + 26
  fresh-oracle regen in-script (b190 14 +
  b191 12).
- Added tables 4/4 EQ (M 16/16, Q 16/16,
  C 67n, _N=67). Full audits GREEN: 1D
  166/0, 2D 841/0, dicts 11/0, STR 261/0,
  STRARR 1036/0; b190 baseline confirms
  exact +1 2D / +2 STRARR delta.
- Next: inherit-vs-b190 scoped sets, quiz
  diff check, battery results, GATE filing.
