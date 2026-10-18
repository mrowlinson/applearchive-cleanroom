# GATE-d0484b7.md — cport band73 T10P65+T10R64 (n<=39704, 566 tiers) PASS-functional

- sha: d0484b7, lane cport. parent b4de394 = merge (skipped per PARENT-031; P65/R64 py already gated via GATE-b69a027/GATE-012efda). lane-diff = src/c/rgramc.c only.
- code-read FULL: 4 pure insertions (356L P65+R64 tables + 16L tmps + 11L + 177L dispatch); rest comment-only T-renumber (comment-stripped diff).
- table audit 11/11 py-vs-C EQ: P65S0 P65S1 P65AM16 P65BM10 P65AC70 P65BC68 R64AM16 R64AQ4 R64BM16 R64AC62 R64BC66.
- gate-tip.sh: C-BUILD PASS 0w, all batteries PASS (RGRAM n=4704, PINS-RGRAM set-eq 4704/4704, all -C legs, LZ4C, UNITS); HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 (13 selfgen .aar; CONTAM 10 files README/docs/notes/proto/spec; depload sole = proto/impl-adapter.sh; LIBCOMP = src/aad.c; Mach-O 0). lane-diff 0 hits. ADOPT WARN diff (info). no FLAG.
- parity: RGRAMC-PYID 2352/2352 covered GREEN (own run, gate tree, seat-private binary 2c1fb5f5).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN 4704/4704 exit 0.
- storm fresh oracle (gate tree, py=C byte-identical 19/19): P65 39357/39358 S, 39359/39366/39374 A off=0/7/15, 39375/39384 B off=0/9; R64 39385/39386/39401/39433/39448 A off=0/1/16/48/63, 39449/39450/39550/39703/39704 B off=0/1/101/254/255 — all CLOSED rc=0.
- boundaries: 39356 -> T10R63B off=255; 39705 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
