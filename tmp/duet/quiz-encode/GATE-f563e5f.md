# GATE-f563e5f.md — cport band75 T10R65+T10P67 (n<=40080, 572 tiers) PASS-functional

- sha: f563e5f, lane cport. parent 97e5ee8 = merge (skipped per PARENT-031; R65/P67 py already gated via GATE-4b20deb/GATE-1030015). lane-diff = src/c/rgramc.c only.
- code-read FULL: 3 pure insertions (354L R65+P67 tables + 16L tmps + 190L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 11/11 py-vs-C EQ: R65AM16 R65AQ4 R65BM16 R65AC62 R65BC65 P67S0 P67S1 P67AM16 P67BM10 P67AC70 P67BC67.
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=4770, PINS-RGRAM set-eq 4770/4770, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files README/docs/notes/proto/spec; LIBCOMP = src/aad.c). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2385/2385 covered GREEN (own run, gate tree, seat-private binary f8d49045).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 4770/4770 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 21/21): R65 39733/39734/39749/39781/39796 A off=0/1/16/48/63, 39797/39798/39898/40051/40052 B off=0/1/101/254/255; P67 40053/40054 S, 40055/40062/40070 A off=0/7/15, 40071/40072/40079/40080 B off=0/1/8/9 — all CLOSED rc=0.
- boundaries: 39732 -> T10P66B off=9; 40081 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
