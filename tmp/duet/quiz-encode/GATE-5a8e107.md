# GATE-5a8e107.md — w2 P61 (37965..37992, hex-sing + 80B A/B) PASS-individual

- sha: 5a8e107, lane w2. tiers: P610/P611 full-hex singletons (76B/80B); A16 80B b25,26,72-75 b5=0x28; B10 80B b18,19,25-30,76-79 b5=0x28.
- AST: S0 len152, S1 len160, both lencode-consistent; AM16 w12, BM10 w24; AC72/BC66 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4512 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 37965 P610, 37966 P611, 37975/37982 A off=8/15, 37983/37992 B off=0/9 — all CLOSED rc=0.
- boundaries: 37964 -> T10R59B off=255; 37993 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
