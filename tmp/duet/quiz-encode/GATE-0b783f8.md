# GATE-0b783f8.md — w2 P54 (35529..35556, hex-sing + 80B A/B) PASS-individual

- sha: 0b783f8, lane w2. tiers: P540/P541 full-hex singletons (76B/80B); A16 80B b41,42,72-75 b5=0x15; B10 80B b33,34,40-45,76-79 b5=0x15.
- AST: S0 len152, S1 len160, both lencode-consistent; AM16 w12, BM10 w24; AC72/BC66 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4232 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 35529 P540, 35530 P541, 35540/35546 A off=9/15, 35547/35556 B off=0/9 — all CLOSED rc=0.
- boundaries: 35528 -> T10R52B off=255; 35557 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
