# GATE-599f93c.md — w2 R59 (37645..37964, A4x16+B16x16 80B) PASS-individual

- sha: 599f93c, lane w2. A: b5=0x26, m b13,14,76-79 + q b6-10,72-75; B: raw lencode, m b20-22,68-71 + q=AM[q] full at b13,14,76-79.
- AST: AM16 w12, AQ4 w18, BM16 w14; AC63/BC65 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4492 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 37645/37680/37708 A off=0/35/63, 37709/37800/37900/37964 B off=0/91/191/255 — all CLOSED rc=0.
- boundaries: 37644 -> T10P60B off=9; 37965 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
