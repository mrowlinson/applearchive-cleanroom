# GATE-36d0b16.md — w2 P59 (37269..37296, hex-sing + 80B A/B) PASS-individual

- sha: 36d0b16, lane w2. tiers: P590/P591 full-hex singletons (76B/80B); A16 80B b36,37,72-75 b5=0x23; B10 80B b0,11,33-35,40,76-79 b5=0x23.
- AST: S0 len152, S1 len160, both lencode-consistent; AM16 w12, BM10 w20; AC72/BC68 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4432 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 37269 P590, 37270 P591, 37280/37286 A off=9/15, 37287/37296 B off=0/9 — all CLOSED rc=0.
- boundaries: 37268 -> T10R57B off=255; 37297 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
