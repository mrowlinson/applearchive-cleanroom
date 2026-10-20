# VERIFY-850d20f4 b300 T10P192 pins 83553..83900 (1089 tiers): PASS

viewer-r32, first-hand, detached tree NVME tmp/encode-viewer/r32/
tree-850d20f4 @850d20f4 (base 1c414b50 = b299 tip), seat build
build300/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2545672 B, sha256 rgramc 292c8364 / aae d6e27c97
  (== GATE exact).
- RGRAMC-PYID 5659/5659 covered=5659/5659 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary). (One seat-side
  mis-invocation without RGRAMC env went RED on a stale default
  binary first; rerun with seat binary GREEN — procedure
  artifact, not code signal.)
- RGRAM C 11318/11318 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11318/11318 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11318/11318).
- PINS-RGRAM cell set-eq 11318/11318 (cmp-identical).
  (GATE's "5659/5659" is N-set method = half the cells;
  for-list count 5659 confirmed; cell-level set-eq is
  full 11318. Method note, not FAIL.)
- PINS 11320 rows = 2 hdr + 11318, +58 vs base (11262).
  For-list +29 exactly: 83553 83554 83555 83562 83570
  83571 83572 83573 83574 83575 83576 83577 83578 83579
  83580 83581 83583 83584 83596 83597 83613 83629 83644
  83645 83711 83712 83839 83840 83900. 0 removed (== GATE).
  PINS N-set == for-list 5659/5659.
- Own-loop 83553..83900 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P192 C-vs-py mechanical, ALL 21 EXACT: S0/S1/G0-G9
  168-hex-char singletons 1/1 each; AM 16/16, M 16/16,
  QR 4/4, QT 4/4, RM 16/16, RQ 16/16; AC 74/74, QC 65/65,
  RC 70/70 (py-hex vs C-decimal normalized); S2/BM/BC
  absent BOTH sides; C _N decls 74/65/70 match actual rows
  (== GATE). Sigs first-hand: S0=20030000 (NEW), S1=47a20700
  (NEW); G-seq 47a20700/0f010300/b7a00300/9bb60300/47be0300/
  a7030300/338e0300/b7a00300/a7030300/f39d0300 (== GATE);
  A b0-3 AC=47a26700 (NEW).
- Dispatch by eye both impls, 15 tiers in order: S0
  n=83553 / S1 n=83554 singletons; A 83555-83570
  off=n-83555, mtab 8B b32-35/76-79, raw lencode (b5
  emergent-const 8c across range, arith-verified; NOT in
  AC list — comment true, no slip); G0-G9 83571-83580
  singletons (G0 PB1-link 27B-div, G2/G7 6B-div pair,
  G5/G8 3B-div pair, G9 S-last per comments); Q 83581-
  83644 off=n-83581 m=off&15 q=off>>4, M 6B b36,37/76-79,
  R 7B b22,23/30-34, T 4B b80-83, raw lencode; R 83645-
  83900 off=n-83645 TRANSPOSED, b4=(0x7b+2off)&FF
  b5=0x8d+(off>=67)+(off>=195), M6 b42,43/76-79 by COL
  off&15, Q6 b36,37/72-75 by ROW off>>4; all paylen 84.
  C blocks carry T53106/111/116/131/136/141/146/151/156/
  161/166/171/176/181/53204 py-line mirrors (15/15 ==
  GATE). Insert position exact both sides: after T10R189
  close (py L53103-53104 / C L144808-144809), before
  dispatch-tail fallthrough (py L53223 / C L144981-82).
  (== GATE.)
- py diff pure addition: rgram.py +255/+0 (0 del lines),
  test_rgram.sh +1/-1, PINS +58/+0.
- C diff renumber-only + new: numstat 2067 add / 1445 del
  (== GATE); raw grep 2052 add / 1445 del + 15 blank-only
  `+` lines verified (== GATE, r37 accounts empties
  correctly); fine-norm del-uniq 1442 / add-uniq 1817
  (== GATE exact, matches strict empty-excluding recipe),
  del-subset-add 0 missing.
- Wall on band diff added lines (1c414b50..850d20f4, 2366
  grep-added lines + 15 empty == GATE scope): vendor/disasm/
  depload/dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load/
  libcompression/shebang 0 hits. Files: rgramc.c, rgram.py,
  test_rgram.sh (for-line 1/1), PINS (+58/+0). Py side
  purely additive.
- CONFIRM evidence: A-413-q423-t10p192-geometry verdict
  CONFIRM (36/37 + 1 convention finding: pba-consts 74
  excl-b5 vs writer 75 incl-b5, pins unaffected; == GATE),
  no DISSENT (CONVERT-01 rule b).
- GATE prose CORRECT throughout (build+sha, counts,
  for-list, tables, _N decls, absent-tables, sigs, G-div
  pairs, mtab/qtab byte lists, counters, T-mirrors, insert
  position, blank-line accounting, A-413 recon). No slips.

Agrees with GATE-850d20f4 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r32/
(*300* files).

Verdict: PASS. Ready for parent PV + merge.
