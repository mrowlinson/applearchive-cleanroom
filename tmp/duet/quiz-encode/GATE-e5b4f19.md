# GATE-e5b4f19.md — cport band49 T10P480..B (n<=33468, 488 tiers) PASS-functional

- sha: e5b4f19, lane cport. lane-diff = src/c/rgramc.c only (948+/508-).
- code-read FULL: 4 new C tiers; B-tier 14 bytes (b2,3,15,25-31,72-75) mirror py exactly.
- table audit 6/6 py-vs-C EQ: P480C74 P481C74 P48A16 P48AC71 P48B10 P48BC60.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=3992 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 1996/1996 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 33441 P480, 33442 P481, 33450 A off=7, 33459/33468 B off=0/9; 33469 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
