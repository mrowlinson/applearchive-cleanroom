# GATE-43e6d43.md — w2 P60 (37617..37644, hex-sing + 80B A/B) PASS-individual

- sha: 43e6d43, lane w2. tiers: P600/P601 full-hex singletons (76B/80B); A16 80B b6,7,72-75 RAW lencode; B10 80B b6-11,76-79 b5=0x26.
- AST: S0 len152, S1 len160, both lencode-consistent; AM16 w12, BM10 w20; AC72/BC68 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4472 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 37617 P600, 37618 P601, 37625/37634 A off=6/15, 37635/37644 B off=0/9 — all CLOSED rc=0.
- boundaries: 37616 -> T10R58B off=255; 37645 -> N out of scope rc=2 (R59 not yet committed at this tip). exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
