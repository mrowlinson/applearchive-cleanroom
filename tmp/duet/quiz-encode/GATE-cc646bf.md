# GATE-cc646bf.md — w2 P51 (34485..34512, 4 tiers) PASS-individual

- sha: cc646bf, lane w2. tiers: P510/P511 singletons 76B; A16 80B b36,37,72-75; B10 76B b32-37,72-75. raw lencode all, no Q.
- AST: A16 w12, B10 w20; consts 74/74/72/64 sorted/nodup/disjoint/FULL-cover (76/76/80/76).
- gate-tip.sh RC=0: RGRAM n=4112 PASS, PINS-RGRAM set-eq, 15 PASS legs.
- storm fresh oracle (gate tree): 34485 P510, 34486 P511, 34495/34502 A off=8/15, 34503/34512 B off=0/9 — all CLOSED rc=0.
- boundaries: 34484 -> T10R49B off=255; 34513 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
