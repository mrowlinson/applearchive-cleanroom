# GATE-42b1e16.md — cport band61 T10R55 (n<=36572, 530 tiers) PASS-functional

- sha: 42b1e16, lane cport. lane-diff = src/c/rgramc.c only (868+/560-).
- code-read FULL: R55A b5=0x1B-const + R55B qhead=QH[q]/qtab=AM[q]+6 mirror py exactly.
- table audit 6/6 py-vs-C EQ: R55AM16 R55AQ4 R55AC60 R55BM16 R55QH16 R55BC64.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4332 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2166/2166 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 36253/36316 A off=0/63, 36317/36450/36572 B off=0/133/255; 36573 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
