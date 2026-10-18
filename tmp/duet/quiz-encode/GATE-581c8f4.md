# GATE-581c8f4.md — cport band72 T10R63 (n<=39356, 562 tiers) PASS-functional

- sha: 581c8f4, lane cport. parent 4b3e3e8 = merge (skipped per PARENT-031; R63 py already gated via GATE-4a3a672). lane-diff = src/c/rgramc.c only.
- code-read FULL: 3 pure insertions (192L _T10R63* tables + 10L tmps + 106L T10R63A/B dispatch); other 612 hunks comment-only T-renumber (verified via comment-stripped diff).
- table audit 6/6 py-vs-C EQ: R63AM16 R63AQ4 R63BM16 R63QH16 R63AC61 R63BC63.
- gate-tip.sh (full log NVME seat ver-581c8f4): C-BUILD PASS 0w; RAWENC/PBZE/LZMA/LZ4/SMOKE/OUTER2/RB2/RAVFRAME/RGRAM/UNITS + all -C legs PASS; RGRAM n=4658 PASS; PINS-RGRAM set-eq 4658/4658; OSS nominated-only; ADOPT WARN (oracle-adapter diff, info only).
- HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b: 13 selfgen .aar identical in parent; CONTAM = docs/notes/README prose + proto/impl-adapter.sh ZBM_DYLIB (sole non-nominated depload, reproduced); LIBCOMPRESSION = src/aad.c; Mach-O scan 0. lane-diff file itself 0 hits all patterns. no FLAG.
- parity: RGRAMC-PYID 2329/2329 covered GREEN (own run x2, gate tree, corpus-reuse).
- C-side RGRAM battery (RGRAM_BIN=C seat-private): RGRAM-GREEN 4658/4658 x2 (orig + PARENT-038 rerun).
- PARENT-038: rebuilt rgramc from at-commit gate tree into seat-private build-038, hash f46c53f5 IDENTICAL to build-storm (deterministic); all C legs rerun with build-038; shared build/aae/* never used by this seat.
- storm fresh oracle (gate tree, py=C byte-identical 12/12): 39037/39038/39053/39085/39100 A off=0/1/16/48/63, 39101/39102/39202/39355/39356 B off=0/1/101/254/255, all CLOSED rc=0 (x2 binaries).
- boundaries: 39036 -> T10P64B off=9; 39357 -> N out of scope rc=2. exact, py=C.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-functional. no FLAG.
