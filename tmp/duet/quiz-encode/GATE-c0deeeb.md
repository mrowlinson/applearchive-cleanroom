# GATE-c0deeeb.md — cport band79 T10P70 (n<=41124, 584 tiers) PASS-functional

- sha: c0deeeb, lane cport. parent 54efe06 = merge (skipped per PARENT-031; P70 py already gated via GATE-5776851). lane-diff = src/c/rgramc.c only.
- code-read FULL: 4 pure insertions (178L P70 tables + 8L tmps + 55L + 37L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 6/6 new-tier py-vs-C EQ: P70S0 P70S1 P70AM16 P70BM10 P70AC71 P70BC67 (+ bonus old-era _T10P70C EQ, inherited name collision).
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=4908, PINS-RGRAM set-eq 4908/4908, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files README/docs/notes/proto/spec; LIBCOMP = src/aad.c). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2454/2454 covered GREEN (own run, gate tree, seat-private binary ad25a09b).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 4908/4908 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 12/12): 41097/41098 S, 41099/41100/41106/41114 A off=0/1/7/15, 41115/41116/41123/41124 B off=0/1/8/9 — all CLOSED rc=0.
- boundaries: 41096 -> T10R68B off=255; 41125 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
