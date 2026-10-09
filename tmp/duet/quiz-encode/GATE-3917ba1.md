# GATE-3917ba1.md — w2 P62 (38313..38340, all-80B) PASS-individual

- sha: 3917ba1, lane w2. tiers: P620/P621 full-hex singletons BOTH 80B (first all-80B P-band); A16 80B b40,41,42,72-75 b5=0x2B; B10 80B b36,40-45,76-79 b5=0x2B.
- AST: S0 len160, S1 len160, both lencode-consistent; AM16 w14, BM10 w22; AC71/BC67 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=4552 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 38313 P620, 38314 P621, 38322/38330 A off=7/15, 38331/38340 B off=0/9 — all CLOSED rc=0.
- boundaries: 38312 -> T10R60B off=255; 38341 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
