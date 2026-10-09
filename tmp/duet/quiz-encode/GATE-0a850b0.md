# GATE-0a850b0.md — w2 R57 (36949..37268, A4x16+B16x16 80B) PASS-individual

- sha: 0a850b0, lane w2. A: m b25,72-75 + q b0,10,11,18,19,24,76-79 (raw lencode); B: m b29-31,72-75 + qhead b24=QH[q] (1B) + qtab b68-71=AM[q][2:].
- AST: AM16 w10, AQ4 w20, BM16 w14, QH16 w2; AC63/BC66 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4412 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 36949/36990/37012 A off=0/41/63, 37013/37100/37200/37268 B off=0/87/187/255 — all CLOSED rc=0.
- boundaries: 36948 -> T10P58B off=9; 37269 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
