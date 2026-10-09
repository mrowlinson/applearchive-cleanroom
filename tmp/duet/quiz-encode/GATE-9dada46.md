# GATE-9dada46.md — w2 R58 (37297..37616, A4x16+B16x16 80B) PASS-individual

- sha: 9dada46, lane w2. A: b5=0x23, m b41-43,72-75 + q b22,23,33-35,40,76-79; B: raw lencode, m b37,38,46,47,72-75 + q=AM[q] full at b40-42,68-71.
- AST: AM16 w14, AQ4 w20, BM16 w16; AC61/BC63 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4452 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 37297/37330/37360 A off=0/33/63, 37361/37450/37550/37616 B off=0/89/189/255 — all CLOSED rc=0.
- boundaries: 37296 -> T10P59B off=9; 37617 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
