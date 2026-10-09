# GATE-d952c6f.md — w2 P64 (39009..39036, all-80B) PASS-individual

- sha: d952c6f, lane w2. tiers: P640/P641 full-hex singletons BOTH 80B; A16 80B b21,22,30,31,72-75 b5=0x30; B10 80B b21,22,29-33,76-79 b5=0x30.
- AST: S0 len160, S1 len160, both lencode-consistent; AM16 w16, BM10 w22; AC70/BC67 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4632 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 39009 P640, 39010 P641, 39018/39026 A off=7/15, 39027/39036 B off=0/9 — all CLOSED rc=0.
- boundaries: 39008 -> T10R62B off=255; 39037 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
