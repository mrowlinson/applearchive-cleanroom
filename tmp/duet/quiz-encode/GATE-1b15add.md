# GATE-1b15add.md — cport band71 T10R62+P64 (n<=39036, 560 tiers) PASS-functional

- sha: 1b15add, lane cport. parent c19269e = merge (skipped per PARENT-032.14; R62/P64 py already gated via GATE-c236297/GATE-d952c6f). lane-diff = src/c/rgramc.c only.
- code-read FULL: 6 new C tiers; AM-suf+QH + all-80B singleton mirrors verified via storm.
- table audit 12/12 py-vs-C EQ: R62AM16 R62AQ4 R62AC62 R62BM16 R62QH16 R62BC64 P64S0-160 P64S1-160 P64AM16 P64AC70 P64BM10 P64BC67.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4632 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2316/2316 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 38689 R62A off=0, 38753/39008 R62B off=0/255, 39009 P640, 39010 P641, 39018 P64A off=7, 39036 P64B off=9; 39037 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
