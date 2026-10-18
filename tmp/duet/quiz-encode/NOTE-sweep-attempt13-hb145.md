# NOTE sweep attempt13 hb145

- band72 gate-tip RGRAM ~49% (2300/4658 PASS, 0 FAIL so far); C-side battery running parallel.
- prep done: P66 AST-GREEN (S0/S1 len160+lencode, AM16/BM10 uniq, AC71/BC67 cover80) wall 0; R65 AST-GREEN (AM16 w10/AQ4 w22/BM16 w16, AC62/BC65 cover80) wall 0; band73 tables 11/11 EQ (P65 6 + R64 5), C diff 4 pure insertions, wall 0.
- audit tooling: audit-P.py + audit-R.py validated vs gated R64 (exact match to GATE-012efda numbers); audit-band.py extended with singleton EQ; storm.sh py=C identical harness.
- queue unchanged, 33 jobs. quiz: Q-40 viewer-owned; no new PARENT.
