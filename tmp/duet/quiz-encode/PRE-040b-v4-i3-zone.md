# PRE-040b I3 zone 3257..3400: minimal 9-field + tabs (w2 next commit)

## only 9 var (43 const; v5q 144 rows) — CORRECTS PRE-039b b14 note
- b14 "chatter" = STRICT 16-tab: 7c x5 3c x2 7c 3c x5 7c x3 (duty
  5/2/1/5/3, verifies all 9 cycles). not chatter.
- b13: a4x3 c0x2 c4x2 dc e0x2 fcx3 18x2 34 (8 values, plateau-duty).
- b15: d1 d2 d3 f0 f1 07 08 10 26 27 44 45 46 63 64 81 (16 unique).
- b16: 75x5 95x11.
- b5/b6/b7: 16-plateaus (b5 10 runs: split 3321-3327:69 / 3328-3336:6a
  7+9 off-phase; b6/b7 9 runs clean 16s).
- b8: ONE flip @3353 (37->57). b4: L10-lo +2/row (73@3257 exact).
