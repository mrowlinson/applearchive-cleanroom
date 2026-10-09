# GATE-cac2fafe.md — cport band68 T10R60+P62 (n<=38340, 552 tiers) PASS-functional

- sha: cac2fafe, lane cport. parent 57108c8 = merge (skipped per PARENT-032.14; R60/P62 py already gated via GATE-fb598fd/GATE-3917ba1). lane-diff = src/c/rgramc.c only.
- code-read FULL: 6 new C tiers; all-80B singletons + AM-full mirrors verified via storm.
- table audit 11/11 py-vs-C EQ: R60AM16 R60AQ4 R60AC61 R60BM16 R60BC66 P62S0-160 P62S1-160 P62AM16 P62AC71 P62BM10 P62BC67.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=4552 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 2276/2276 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 8/8): 37993 R60A off=0, 38057/38312 R60B off=0/255, 38313 P620, 38314 P621, 38322 P62A off=7, 38340 P62B off=9; 38341 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
