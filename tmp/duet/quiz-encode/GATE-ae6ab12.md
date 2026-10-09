# GATE-ae6ab12.md — cport band64 T10R57+P59 (n<=37296, 540 tiers) PASS-functional

- sha: ae6ab12, lane cport. parent d228eb4 = merge (skipped per PARENT-032.14; R57/P59 py already gated via GATE-0a850b0/GATE-36d0b16). lane-diff = src/c/rgramc.c only (1158+/572-).
- code-read FULL: 6 new C tiers; hex-singleton + b5=0x23-const + AM-suf+QH1B mirrors verified via storm.
- table audit 12/12 py-vs-C EQ: R57AM16 R57AQ4 R57AC63 R57BM16 R57QH16 R57BC66 P59S0-152 P59S1-160 P59AM16 P59AC72 P59BM10 P59BC68.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4432 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2216/2216 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 36949 R57A off=0, 37013/37268 R57B off=0/255, 37269 P590, 37270 P591, 37280 P59A off=9, 37296 P59B off=9; 37297 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
