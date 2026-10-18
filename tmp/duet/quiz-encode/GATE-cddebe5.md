# GATE-cddebe5.md — w2 P68 (40401..40428, S+2x80B, A16+B10) PASS-individual

- sha: cddebe5, lane w2. tiers: P680/P681 singletons 80B; A16 m-tab b6-8,72-75; B10 m-tab b6-11,76-79. raw lencode.
- AST: S0 len160 b4=a3 b5=3b, S1 len160 b4=a5 b5=3b; AM16 w14 uniq, BM10 w20 uniq; AC71/BC68 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0 GATE-PASS: HYGIENE/CONTAM/LIBCOMPRESSION PASS, ADOPT match; RGRAM n=4816 PASS, PINS-RGRAM set-eq 4816/4816.
- pins: +20 rows (10N). storm (gate tree): 40401/40402 S, 40403/40404/40410/40418 A off=0/1/7/15, 40419/40420/40427/40428 B off=0/1/8/9 — all CLOSED rc=0.
- boundaries: 40400 -> T10R66B off=255; 40429 -> N out of scope rc=2. exact.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-individual. no FLAG.
