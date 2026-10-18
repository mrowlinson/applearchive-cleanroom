# A-272 (viewer r3): Q-266 T10P202 P-head @87033 — CONFIRM all 3

First-hand bed 87033..87384 (regen 87041..88040 RC=0
missing=0 + prior census; q266.py).

1. shape CONFIRM: 348 cells sizes {(100,84)}.
   PB0 9e030000 (P201-next PREDICTED-exact), PB1
   7c3d0700, PBA c8d77300 (VPOS 9 exact:
   b4,b5+M7 b20-22,76-79; b5 a7->a8 carry
   87039 ff/a7 -> 87040 01/a8), SING df830600 +
   4f4c0600 both NEW, PBB8 be9e0300 (VPOS 12
   exact b4+M11 b20-26,80-83, b5 const),
   ROW16a 4f3a3b00 / ROW16b ff683a00 / ROW32
   37163900 all NEW (VPOS 10/10/11 exact).
   Next @87381 9e030000 (REPEAT of own PB0) +
   87382 95020500 + 87383/84 95027100. confirm.
2. rows + T-ring CONFIRM: M9 shared 16/16 all 3
   groups (a-b, a-c0, a-c1); ROW32 halves
   identical ex-b4 (counter +32 cont: 6b..89
   lo -> 8b..a9 hi) + b80 half-flag (9c x16
   lo / d0 x16 hi); constdiffs a-b 10B
   [0,1,2,19,24,25,80-83] / a-c0 12B +[11,18]
   exact; M-tails 16/16 ALL NEW vs P201T.
   T-ring c7489e03 VPOS 17, TRANSPOSED 12th:
   M7 b32-34,76-79 by COL 16/16, Q8 b24-27,
   72-75 by ROW 16/16. confirm.
3. counters + dips CONFIRM: odd-lencode 92/92
   NONE bad; T b4/b5 formulas exact NONE bad;
   edges 87167->87168 ff/a8->01/a9 +
   87295->87296 ff/a9->01/aa.
- Consts (84-VPOS) ALL 6 EXACT: PBA 75, PBB
  72, rows 74/74/73, T 67.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
