# GATE-838cde4.md — w2 R48 (33817..34136, A4x16+B16x16 80B) PASS-individual

- sha: 838cde4, lane w2. A: m b6,7,12,72-75 + q b11,34,35,46,47,76-79; B: m b13,72-75 + b8 rule (0x74 q<11 else 0xd4) + q: b6,7=AM[q][:4], b68-71=AM[q][6:]. paylen 80 + raw lencode.
- AST: AM16 w14, AQ4 w18, BM16 w10; AC62/BC66 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4052 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 33817/33850/33880 A off=0/33/63, 33881/34055/34057/34136 B off=0/174/176/255 — all CLOSED rc=0; b8 flip straddled (q=10/11).
- boundaries: 33816 -> T10P49B off=9; 34137 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
