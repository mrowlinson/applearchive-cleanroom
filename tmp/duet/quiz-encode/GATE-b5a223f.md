# GATE-b5a223f.md — w2 R52 (35209..35528, A4x16+B16x16 80B) PASS-individual

- sha: b5a223f, lane w2. A: b5 CONST 0x13, m b19,30,31,72-75 + q b18,25-29,76-79; B: raw lencode, m b36-38,72-75 + q=AM[q] full at b21,30,31,68-71.
- AST: AM16 w14, AQ4 w20, BM16 w14; AC61/BC64 sorted/nodup/disjoint/FULL-cover80 (A b5 rule-excluded).
- gate-tip.sh RC=0: RGRAM n=4212 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 35209/35240/35272 A off=0/31/63, 35273/35350/35500/35528 B off=0/77/227/255 — all CLOSED rc=0.
- boundaries: 35208 -> T10P53B off=9; 35529 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
