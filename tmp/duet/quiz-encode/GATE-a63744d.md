# GATE-a63744d.md — cport band69 T10R61 (n<=38660, 554 tiers) PASS-functional

- sha: a63744d, lane cport. parent dc6552e = merge (skipped per PARENT-032.14; R61 py already gated via GATE-e2f8de7). lane-diff = src/c/rgramc.c only.
- code-read FULL: R61A/B AM-full mirrors verified via storm.
- table audit 5/5 py-vs-C EQ: R61AM16 R61AQ4 R61AC61 R61BM16 R61BC64.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4572 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2286/2286 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 38341/38404 A off=0/63, 38405/38550/38660 B off=0/145/255; 38661 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
