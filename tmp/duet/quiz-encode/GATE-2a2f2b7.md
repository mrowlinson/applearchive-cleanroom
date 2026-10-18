# GATE-2a2f2b7.md — cport band74 T10P66 (n<=39732, 568 tiers) PASS-functional

- sha: 2a2f2b7, lane cport. parent bee28c5 = merge (skipped per PARENT-031; P66 py already gated via GATE-3682200). lane-diff = src/c/rgramc.c only.
- code-read FULL: 4 pure insertions (178L P66 tables + 8L tmps + 55L + 37L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 6/6 py-vs-C EQ: P66S0 P66S1 P66AM16 P66BM10 P66AC71 P66BC67.
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=4724, PINS-RGRAM set-eq 4724/4724, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files README/docs/notes/proto/spec; LIBCOMP = src/aad.c). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2362/2362 covered GREEN (own run, gate tree, seat-private binary d01814ce).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 4724/4724 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 12/12): 39705/39706 S, 39707/39708/39714/39722 A off=0/1/7/15, 39723/39724/39731/39732 B off=0/1/8/9 — all CLOSED rc=0.
- boundaries: 39704 -> T10R64B off=255; 39733 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
