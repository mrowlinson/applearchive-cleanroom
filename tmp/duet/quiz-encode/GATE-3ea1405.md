# GATE-3ea1405.md — w2 R55 (36253..36572, A4x16+B16x16 80B) PASS-individual

- sha: 3ea1405, lane w2. A: b5=0x1B, m b36-38,72-75 + q b21,22,29-33,76-79; B: raw lencode, m b40-42,72-75 + qhead b22,34,35=QH[q] + qtab b68-71=AM[q][6:].
- AST: AM16 w14, AQ4 w22, BM16 w14, QH16 w6; AC60/BC64 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4332 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 36253/36290/36316 A off=0/37/63, 36317/36400/36500/36572 B off=0/83/183/255 — all CLOSED rc=0.
- boundaries: 36252 -> T10P56B off=9; 36573 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
