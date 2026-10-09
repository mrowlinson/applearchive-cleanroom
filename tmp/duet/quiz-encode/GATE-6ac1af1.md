# GATE-6ac1af1.md — cport band47 T10P470..Q (n<=33184, 483 tiers) PASS-functional

- sha: 6ac1af1, lane cport. lane-diff = src/c/rgramc.c only (1082+/502-).
- code-read FULL: 5 new C tiers; Q-tier bytes (m b16,17,68-71; q b0,1,2,11,12,13,72-75) mirror py exactly.
- table audit 9/9 py-vs-C EQ: P470C74 P471C74 P47A16 P47AC70 P47B10 P47BC63 P47M16 P47Q4 P47QC58.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=3952 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 1976/1976 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 33093 P470, 33094 P471, 33100 A off=5, 33115 B off=4, 33121/33150/33184 Q off=0/29/63, 33185 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
