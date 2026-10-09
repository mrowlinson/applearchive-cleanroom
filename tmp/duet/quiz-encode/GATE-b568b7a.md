# GATE-b568b7a.md — w2 R49 (34165..34484, A4x16+B16x16 80B) PASS-individual

- sha: b568b7a, lane w2. A: m b18,25-27,72-75 + q b20-24,76-79; B: m b21,22,29-31,72-75 + qhead b25-27=QH[q] + qtab b68-71=AM[q][8:]. paylen 80 + raw lencode.
- AST: AM16 w16, AQ4 w18, BM16 w18, QH16 w6; AC61/BC62 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4092 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 34165/34200/34228 A off=0/35/63, 34229/34300/34400/34484 B off=0/71/171/255 — all CLOSED rc=0.
- boundaries: 34164 -> T10P50B off=9; 34485 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
