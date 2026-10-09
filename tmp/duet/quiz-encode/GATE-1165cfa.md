# GATE-1165cfa.md — w2 P58 (36921..36948, hex-sing + 80B A/B) PASS-individual

- sha: 1165cfa, lane w2. tiers: P580/P581 full-hex singletons (76B/80B); A16 80B b20,21,22,72-75 b5=0x20; B10 80B b0,11,18-27,76-79 b5=0x20.
- AST: S0 len152, S1 len160, both lencode-consistent; AM16 w14, BM10 w32; AC71/BC62 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4392 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 36921 P580, 36922 P581, 36930/36938 A off=7/15, 36939/36948 B off=0/9 — all CLOSED rc=0.
- boundaries: 36920 -> T10R56B off=255; 36949 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
