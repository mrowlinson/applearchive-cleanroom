# GATE-5e0909c.md — w2 P63 (38661..38688, all-80B) PASS-individual

- sha: 5e0909c, lane w2. tiers: P630/P631 full-hex singletons BOTH 80B; A16 80B b13,14,15,72-75 b5=0x2E; B10 80B b13-18,76-79 b5=0x2E.
- AST: S0 len160, S1 len160, both lencode-consistent; AM16 w14, BM10 w20; AC71/BC68 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4592 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 38661 P630, 38662 P631, 38670/38678 A off=7/15, 38679/38688 B off=0/9 — all CLOSED rc=0.
- boundaries: 38660 -> T10R61B off=255; 38689 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
