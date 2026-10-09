# GATE-bac386a.md — cport band58 T10P54+R53 (n<=35876, 522 tiers) PASS-functional

- sha: bac386a, lane cport. lane-diff = src/c/rgramc.c only (1104+/544-).
- code-read FULL: 6 new C tiers; hex-singleton + b5-const + AM-full-suffix mirrors verified via storm.
- table audit 11/11 py-vs-C EQ: P54S0-152 P54S1-160 P54AM16 P54AC72 P54BM10 P54BC66 R53AM16 R53AQ4 R53AC60 R53BM16 R53BC66.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4252 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2126/2126 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 35529 P540, 35540 P54A off=9, 35556 P54B off=9, 35557 R53A off=0, 35621/35800/35876 R53B off=0/179/255; 35877 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
