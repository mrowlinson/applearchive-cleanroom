# GATE-3184de5.md — cport band81 T10R70 (n<=41792, 592 tiers) PASS-functional

- sha: 3184de5, lane cport. parent 2bdac59 = merge (skipped per PARENT-031; R70 py already gated via GATE-e34f88e). lane-diff = src/c/rgramc.c only.
- code-read FULL: 4 pure insertions (177L R70 tables + 8L tmps + 50L + 47L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 5/5 py-vs-C EQ: R70AM16 R70AQ4 R70BM16 R70AC62 R70BC65.
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=4980, PINS-RGRAM set-eq 4980/4980, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files README/docs/notes/proto/spec; LIBCOMP = src/aad.c). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2490/2490 covered GREEN (own run, gate tree, seat-private binary d86aa2e2).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 4980/4980 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 12/12): 41473/41474/41489/41521/41536 A off=0/1/16/48/63, 41537/41538/41638/41791/41792 B off=0/1/101/254/255 — all CLOSED rc=0.
- boundaries: 41472 -> T10P71B off=9; 41793 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
