# GATE-648ac73.md — w2 P57 (36573..36600, hex-sing + 80B A/B) PASS-individual

- sha: 648ac73, lane w2. tiers: P570/P571 full-hex singletons (76B/80B); A16 80B b37,38,46,47,68-71 b5=0x1D; B10 80B b36-39,45-47,76-79 b5=0x1D.
- AST: S0 len152, S1 len160, both lencode-consistent; AM16 w16, BM10 w22; AC70/BC67 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4352 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 36573 P570, 36574 P571, 36585/36590 A off=10/15, 36591/36600 B off=0/9 — all CLOSED rc=0.
- boundaries: 36572 -> T10R55B off=255; 36601 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
