# GATE-5832f8b.md — w2 R51 (34861..35180, A4x16+B16x16 80B) PASS-individual

- sha: 5832f8b, lane w2. A: m b8-10,15,76-79 + q b6,7,12-14,72-75; B: m b20,21,68-71 + qhead b13-15=QH[q] + qtab b76-79=AM[q][8:]. paylen 80 + raw lencode.
- AST: AM16 w16, AQ4 w18, BM16 w12, QH16 w6; AC61/BC65 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4172 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 34861/34900/34924 A off=0/39/63, 34925/35000/35100/35180 B off=0/75/175/255 — all CLOSED rc=0.
- boundaries: 34860 -> T10P52B off=9; 35181 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
