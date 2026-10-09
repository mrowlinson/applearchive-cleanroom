# GATE-1582c9c.md — w2 P56 (36225..36252, hex-sing + 80B A/B) PASS-individual

- sha: 1582c9c, lane w2. tiers: P560/P561 full-hex singletons (76B/80B); A16 80B b21,30,31,72-75 b5=0x1B; B10 80B b0,10,11,19,29-35,76-79 b5=0x1B.
- AST: S0 len152, S1 len160, both lencode-consistent; AM16 w14, BM10 w30; AC71/BC63 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4312 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 36225 P560, 36226 P561, 36235/36242 A off=8/15, 36243/36252 B off=0/9 — all CLOSED rc=0.
- boundaries: 36224 -> T10R54B off=255; 36253 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
