# NOTE-w2-hb-s20-214 — r9 R156 CUT-READY (apply slicing lesson)

bump-20

- R156 DERIVED FIRST-HAND: MATCHES A-195 (sig 36a00700, m8B[6-9,76-79], q8B[48-51,72-75] 1st 8B q-tab, b4 0x0b/b5 0x31 steps 123/251, 66 consts) + DERIVE-STAGED-MATCH + Q 16/16 vs P158M (98th) -> r156-patch-r9.txt (12 cells: staged 10 + 71877 q4m0 + 72037 q14m0) -> shadow 256/256 CLOSED. CUT-READY.
- LESSON: 13-line CONSTS (nconst 66) shifts patch layout (te=57/hs=59 vs usual te=58/hs=60) — first apply dropped the `if` guard (sweep 0/256 caught it). Built generic shadow-apply-r9.py (auto-locates bounds). R154/R155 shadows re-verified guards-present (sweeps VALID). WT cuts must verify the `if n <=` guard line explicitly per row.
- RECORD @3104/8462 (37%), 0 FAIL. Runway: R146 WT -> R147..R153 staged -> R154/R155/R156 own-ready.
- Wall intact. No joint DONE.
