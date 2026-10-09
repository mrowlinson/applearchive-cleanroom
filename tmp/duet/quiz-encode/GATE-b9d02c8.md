# GATE-b9d02c8.md — cport band46 T10P460..Q+T10R45 (n<=33092, 478 tiers) PASS-functional

- sha: b9d02c8, lane cport. lane-diff = src/c/rgramc.c only (1346+/495-).
- code-read FULL: 7 new C tiers; Q-tier b32 rule pay[32]==M32[m]^(q>=2?32:0) mirrors py 0x20-bit.
- table audit 15/15 py-vs-C EQ: P460C74 P461C74 P46A16 P46AC68 P46B1-5 P46B1C63 P46B2-5 P46B2C63 P46M16 P46M32-16 P46Q4 P46QC56 R45M16 R45QH16 R45C64.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=3932 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 1966/1966 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 32745 P460, 32755 A off=8, 32765 B1 off=2, 32770 B2 off=2, 32800 Q off=27, 32900/33092 R45 off=63/255, 33093 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
