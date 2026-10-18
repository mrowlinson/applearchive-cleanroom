# GATE-7c309fc.md — cport band82 T10P72+T10R71 (n<=42140, 596 tiers) PASS-functional

- sha: 7c309fc, lane cport. parent 91f70b6 = merge (skipped per PARENT-031; P72/R71 py already gated via GATE-df54d7e/GATE-60aa85b). lane-diff = src/c/rgramc.c only.
- code-read FULL: 4 pure insertions (376L P72+R71 tables + 18L tmps + 55L + 137L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 12/12 py-vs-C EQ: P72S0 P72S1 P72AM16 P72BM10 P72AC71 P72BC66 R71AM16 R71AQ4 R71BM16 R71QH16 R71AC67 R71BC64.
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=5026, PINS-RGRAM set-eq 5026/5026, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files README/docs/notes/proto/spec; LIBCOMP = src/aad.c). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2513/2513 covered GREEN (own run, gate tree, seat-private binary f114b2df).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 5026/5026 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 21/21): P72 41793/41794 S, 41795/41802/41810 A off=0/7/15, 41811/41812/41819/41820 B off=0/1/8/9; R71 41821/41822/41837/41869/41884 A off=0/1/16/48/63, 41885/41886/41986/42139/42140 B off=0/1/101/254/255 — all CLOSED rc=0.
- boundaries: 41792 -> T10R70B off=255; 42141 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
