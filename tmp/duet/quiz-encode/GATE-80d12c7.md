# GATE-80d12c7.md — cport band70 T10P63 (n<=38688, 556 tiers) PASS-functional

- sha: 80d12c7, lane cport. parent 2a7fa9a single. lane-diff = src/c/rgramc.c only.
- code-read FULL: 4 new C tiers; all-80B singletons + b5=0x2E-const mirrors verified via storm.
- table audit 6/6 py-vs-C EQ: P63S0-160 P63S1-160 P63AM16 P63AC71 P63BM10 P63BC68.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4592 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2296/2296 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 38661 P630, 38662 P631, 38670 A off=7, 38679/38688 B off=0/9; 38689 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
