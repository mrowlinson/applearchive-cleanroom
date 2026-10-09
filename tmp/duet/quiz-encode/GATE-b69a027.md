# GATE-b69a027.md — w2 P65 (39357..39384, all-80B) PASS-individual

- sha: b69a027, lane w2. tiers: P650/P651 full-hex singletons BOTH 80B; A16 80B b37,38,46,47,72-75 b5=0x33; B10 80B b37-39,45-47,76-79 b5=0x33.
- AST: S0 len160, S1 len160, both lencode-consistent; AM16 w16, BM10 w20; AC70/BC68 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4678 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 39357 P650, 39358 P651, 39366/39374 A off=7/15, 39375/39384 B off=0/9 — all CLOSED rc=0.
- boundaries: 39356 -> T10R63B off=255; 39385 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
