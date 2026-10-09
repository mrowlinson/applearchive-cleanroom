# GATE-ac1ec02.md — cport band50 T10R47+P490..B (n<=33816, 494 tiers) PASS-functional

- sha: ac1ec02, lane cport. lane-diff = src/c/rgramc.c only (1234+/512-).
- code-read FULL: 6 new C tiers; R47B q-reuse (m b41-43,72-75; q b36-38,68-71 = R47AM[q]) mirrors py exactly.
- table audit 11/11 py-vs-C EQ: R47AM16 R47AQ4 R47AC62 R47BM16 R47BC64 P490C74 P491C74 P49A16 P49AC71 P49B10 P49BC63.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4032 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2016/2016 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 33469 R47A off=0, 33533/33650/33788 R47B off=0/117/255, 33789 P490, 33800 P49A off=9, 33816 P49B off=9; 33817 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
