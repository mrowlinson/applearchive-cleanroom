# GATE-d840c7b.md — cport band52 T10P500..B (n<=34164, 500 tiers) PASS-functional

- sha: d840c7b, lane cport. lane-diff = src/c/rgramc.c only (960+/520-).
- code-read FULL: 4 new C tiers; B-tier 16 byte-refs (b2,3,14-23,72-75) mirror py exactly.
- table audit 6/6 py-vs-C EQ: P500C74 P501C74 P50A16 P50AC72 P50B10 P50BC58.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4072 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2036/2036 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 34137 P500, 34138 P501, 34145 A off=6, 34155/34164 B off=0/9; 34165 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
