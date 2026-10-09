# GATE-f15455c.md — cport band53 T10R49+P510..B (n<=34512, 506 tiers) PASS-functional

- sha: f15455c, lane cport. lane-diff = src/c/rgramc.c only (1272+/524-).
- code-read FULL: 6 new C tiers; R49B qhead b25-27=QH[q] + qtab b68-71=AM[q]+8 mirror py exactly.
- table audit 12/12 py-vs-C EQ: R49AM16 R49AQ4 R49AC61 R49BM16 R49QH16 R49BC62 P510C74 P511C74 P51A16 P51AC72 P51B10 P51BC64.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4112 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2056/2056 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 34165 R49A off=0, 34229/34400/34484 R49B off=0/171/255, 34485 P510, 34502 P51A off=15, 34512 P51B off=9; 34513 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
