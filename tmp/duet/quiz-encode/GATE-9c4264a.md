# GATE-9c4264a.md — cport band80 T10R69+T10P71 (n<=41472, 588 tiers) PASS-functional

- sha: 9c4264a, lane cport. parent f14da80 = merge (skipped per PARENT-031; R69/P71 py already gated via GATE-29845bb/GATE-7fd15a0). lane-diff = src/c/rgramc.c only.
- code-read FULL: 3 pure insertions (355L R69+P71 tables + 16L tmps + 189L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 11/11 new-tier py-vs-C EQ: R69AM16 R69AQ4 R69BM16 R69AC61 R69BC64 P71S0 P71S1 P71AM16 P71BM10 P71AC72 P71BC68 (+ bonus old-era _T10P71C EQ, inherited).
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=4954, PINS-RGRAM set-eq 4954/4954, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files; LIBCOMP = src/aad.c). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2477/2477 covered GREEN (own run, gate tree, seat-private binary c32d461c).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 4954/4954 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 21/21): R69 41125/41126/41141/41173/41188 A off=0/1/16/48/63, 41189/41190/41290/41443/41444 B off=0/1/101/254/255; P71 41445/41446 S, 41447/41454/41462 A off=0/7/15, 41463/41464/41471/41472 B off=0/1/8/9 — all CLOSED rc=0.
- boundaries: 41124 -> T10P70B off=9; 41473 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
