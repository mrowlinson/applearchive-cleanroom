# GATE-0fb3ec8.md — w2 P47 (33093..33184, 5 tiers) PASS-individual

- sha: 0fb3ec8, lane w2. tiers: P470/P471 singletons 76B; A16 80B b8,9,10,15,72-75; B10 76B b0,1,2,11-14,72-75; Q4x16 76B m b16,17,68-71 + q b0,1,2,11,12,13,72-75. raw lencode all.
- AST: A16 w16, B10 w22, M16 w12, Q4 w20; consts 74/74/70/63/58 sorted/nodup/disjoint/FULL-cover (76/76/80/76/76).
- gate-tip.sh RC=0: RGRAM n=3952 PASS, PINS-RGRAM set-eq, 15 PASS legs (HYGIENE/CONTAM/LIBCOMPRESSION PASS at w2 tip).
- storm fresh oracle (gate tree): 33093 P470, 33094 P471, 33100/33110 A off=5/15, 33115/33120 B off=4/9, 33121/33150/33184 Q off=0/29/63 — all CLOSED rc=0.
- boundaries: 33092 -> T10R45 off=255; 33185 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
