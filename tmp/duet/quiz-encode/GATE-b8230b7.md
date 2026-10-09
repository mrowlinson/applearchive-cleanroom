# GATE-b8230b7.md — w2 R50 (34513..34832, A4x16+B16x16 80B) PASS-individual

- sha: b8230b7, lane w2. A: b40=QB40[q]|0x80 iff m in {1,2,6,10,12}, m b41,42,76-79 + q b0,10,11,33-35,72-75; B: m b37,38,46,47,68-71 + qhead b40,41=QH[q] + qtab b76-79=AM[q][4:]. paylen 80 + raw lencode.
- AST: AM16 w12, QB40-4, AQ4 w20, BM16 w16, QH16 w4; AC61/BC64 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4132 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 34513/34514/34515/34519/34576 A off=0/1/2/6/63 (b40 set hit m=1,2,6 + miss m=0), 34577/34700/34832 B off=0/123/255 — all CLOSED rc=0.
- boundaries: 34512 -> T10P51B off=9; 34833 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
