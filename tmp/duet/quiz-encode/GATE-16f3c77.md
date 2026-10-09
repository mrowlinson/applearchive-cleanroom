# GATE-16f3c77.md — cport band56 T10R51+P53 (n<=35208, 516 tiers) PASS-functional

- sha: 16f3c77, lane cport. lane-diff = src/c/rgramc.c only (1118+/536-).
- code-read FULL: 6 new C tiers; P53A b5-const transpiled (pay[5] != 18); hex-singleton compares mirror py.
- table audit 12/12 py-vs-C EQ: R51AM16 R51AQ4 R51AC61 R51BM16 R51QH16 R51BC65 P53S0-152 P53S1-160 P53AM16 P53AC70 P53BM10 P53BC64.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4192 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2096/2096 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 34861 R51A off=0, 34925/35180 R51B off=0/255, 35181 P530, 35182 P531, 35190 P53A off=7, 35208 P53B off=9; 35209 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
