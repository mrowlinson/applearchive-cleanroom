# NOTE-sweep-r15-hb6

- GATE-3744141 FILED (b195 PASS-functional,
  full first-hand battery GREEN).
- CLAIM-sweep-f11a1ca filed; b197 gate
  battery launched (gate-tip + PYID +
  C-batt + own-loop 65549..65804, sequential,
  seat-private logs r15-f11a1ca/ NVME).
- Lane-diff vs d9b904a first-hand: rgramc.c
  only +1246/-1087, wall 0. New pins 12 N
  (24 rows): 65549 65550 65663 65664 65677
  65741 65759 65760 65773 65787 65803 65804.
- Own build rgramc-own rc=0, 0 warnings.
  PYID corpus seeded 4177 .rav (r15-b195) +
  27 fresh-oracle regen in-script (b196 15 +
  b197 12).
- Added tables 4/4 EQ (M 16/16, Q 16/16,
  C 69n, _N=69). Full audits GREEN: 1D
  167/0, 2D 853/0, dicts 11/0, STR 268/0,
  STRARR 1058/0; b195/b196 baselines confirm
  exact +1 2D / +2 STRARR per-R-band delta.
- Inherit 9/9 IDENTICAL b195->b197 (depraw
  74/74, ADOPT carried).
- Cport tip now b199 9d9b10d (odd, next
  refill target). b3 LAP at 6000/7656 GREEN
  (726/726 pins); resumes after b197 GATE.
- Quiz diff 0. Next: battery results, GATE.
