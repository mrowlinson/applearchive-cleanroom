# GATE-a07ce91.md — cport band66 T10P60+R59 (n<=37964, 546 tiers) PASS-functional

- sha: a07ce91, lane cport. parent d22cdc1 = merge (skipped per PARENT-032.14; P60/R59 py already gated via GATE-43e6d43/GATE-599f93c). lane-diff = src/c/rgramc.c only (1140+/580-).
- code-read FULL: 6 new C tiers; hex-singleton + A-raw/B-b5=0x26 + A-b5=0x26/B-raw + AM-full mirrors verified via storm.
- table audit 11/11 py-vs-C EQ: P60S0-152 P60S1-160 P60AM16 P60AC72 P60BM10 P60BC68 R59AM16 R59AQ4 R59AC63 R59BM16 R59BC65.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4492 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2246/2246 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 37617 P600, 37625 P60A off=6, 37644 P60B off=9, 37645 R59A off=0, 37709/37850/37964 R59B off=0/141/255; 37965 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
