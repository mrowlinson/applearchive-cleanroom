# GATE-4a3a672.md — w2 R63 (39037..39356, A4x16+B16x16 80B) PASS-individual

- sha: 4a3a672, lane w2. A: m b36,37,72-75 + q b21,22,29-33,76-79 (raw lencode); B: m b40-43,72-75 + qhead b22,34,35=QH[q] + qtab b68-71=AM[q][4:].
- AST: AM16 w12, AQ4 w22, BM16 w16, QH16 w6; AC61/BC63 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4658 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 39037/39070/39100 A off=0/33/63, 39101/39200/39300/39356 B off=0/99/199/255 — all CLOSED rc=0.
- boundaries: 39036 -> T10P64B off=9; 39357 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
