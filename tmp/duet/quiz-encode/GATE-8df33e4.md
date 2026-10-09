# GATE-8df33e4.md — cport band55 T10P52 (n<=34860, 512 tiers) PASS-functional

- sha: 8df33e4, lane cport. lane-diff = src/c/rgramc.c only (976+/532-).
- code-read FULL: 4 new C tiers incl mixed-regime singletons (520 76B / 521 80B).
- table audit 6/6 py-vs-C EQ: P520C74 P521C78 P52A16 P52AC72 P52B10 P52BC64.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4152 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2076/2076 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 34833 P520, 34834 P521, 34840 A off=5, 34851/34860 B off=0/9; 34861 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
