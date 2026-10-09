# GATE-c10b738.md — cport band59 T10P55 (n<=35904, 524 tiers) PASS-functional

- sha: c10b738, lane cport. lane-diff = src/c/rgramc.c only (828+/550-).
- code-read FULL: 4 new C tiers; hex-singleton + b5=0x18-const mirrors verified via storm.
- table audit 6/6 py-vs-C EQ: P55S0-152 P55S1-160 P55AM16 P55AC72 P55BM10 P55BC67.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4272 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2136/2136 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 35877 P550, 35878 P551, 35885 A off=6, 35895/35904 B off=0/9; 35905 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
