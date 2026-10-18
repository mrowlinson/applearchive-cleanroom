# GATE-5ab465c.md — cport band78 T10P69+T10R68 (n<=41096, 582 tiers) PASS-functional

- sha: 5ab465c, lane cport. parent 40c2817 = merge (skipped per PARENT-031; P69/R68 py already gated via GATE-a6bf95f/GATE-911b25f). lane-diff = src/c/rgramc.c only.
- code-read FULL: 4 pure insertions (370L P69+R68 tables + 18L tmps + 54L + 144L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 12/12 py-vs-C EQ: P69S0 P69S1 P69AM16 P69BM10 P69AC72 P69BC65 R68AM16 R68AQ4 R68BM16 R68QH16 R68AC61 R68BC64.
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=4888, PINS-RGRAM set-eq 4888/4888, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files README/docs/notes/proto/spec; LIBCOMP = src/aad.c). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2444/2444 covered GREEN (own run, gate tree, seat-private binary d8b08d12).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 4888/4888 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 21/21): P69 40749/40750 S, 40751/40758/40766 A off=0/7/15, 40767/40768/40775/40776 B off=0/1/8/9; R68 40777/40778/40793/40825/40840 A off=0/1/16/48/63, 40841/40842/40942/41095/41096 B off=0/1/101/254/255 — all CLOSED rc=0.
- boundaries: 40748 -> T10R67B off=255; 41097 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
