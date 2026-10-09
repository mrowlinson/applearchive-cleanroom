# GATE-f8fc439.md — cport band63 T10P58 (n<=36948, 536 tiers) PASS-functional

- sha: f8fc439, lane cport. lane-diff = src/c/rgramc.c only (846+/568-).
- code-read FULL: 4 new C tiers; hex-singleton + b5=0x20-const mirrors verified via storm.
- table audit 6/6 py-vs-C EQ: P58S0-152 P58S1-160 P58AM16 P58AC71 P58BM10 P58BC62.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4392 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2196/2196 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 36921 P580, 36922 P581, 36930 A off=7, 36939/36948 B off=0/9; 36949 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
