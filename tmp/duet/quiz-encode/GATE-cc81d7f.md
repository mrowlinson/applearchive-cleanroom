# GATE-cc81d7f.md — cport band77 T10R67 (n<=40748, 578 tiers) PASS-functional

- sha: cc81d7f, lane cport. parent 7d2affe = merge (skipped per PARENT-031; R67 py already gated via GATE-c55aa3c). lane-diff = src/c/rgramc.c only.
- code-read FULL: 4 pure insertions (177L R67 tables + 8L tmps + 49L + 48L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 5/5 py-vs-C EQ: R67AM16 R67AQ4 R67BM16 R67AC63 R67BC64.
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=4842, PINS-RGRAM set-eq 4842/4842, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files README/docs/notes/proto/spec; LIBCOMP = src/aad.c). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2421/2421 covered GREEN (own run, gate tree, seat-private binary f72f8edd).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 4842/4842 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 12/12): 40429/40430/40445/40477/40492 A off=0/1/16/48/63, 40493/40494/40594/40747/40748 B off=0/1/101/254/255 — all CLOSED rc=0.
- boundaries: 40428 -> T10P68B off=9; 40749 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
