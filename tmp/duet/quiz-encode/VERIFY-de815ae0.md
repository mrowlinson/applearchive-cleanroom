# VERIFY-de815ae0 b302 T10P194 pins 84249..84596 (1105 tiers): PASS

viewer-r32, first-hand, detached tree NVME tmp/encode-viewer/r32/
tree-de815ae0 @de815ae0 (base 55308f7c = b301 tip), seat build
build302/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2563032 B, sha256 rgramc 99d0585b / aae d6e27c97
  (== GATE exact).
- RGRAMC-PYID 5712/5712 covered=5712/5712 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11424/11424 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11424/11424 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11424/11424).
- PINS-RGRAM cell set-eq 11424/11424 (cmp-identical).
  (GATE's "5712/5712" is N-set method = half the cells;
  for-list count 5712 confirmed; cell-level set-eq is
  full 11424. Method note, not FAIL.)
- PINS 11426 rows = 2 hdr + 11424, +54 vs base (11372).
  For-list +27 exactly: 84249 84250 84251 84258 84266
  84267 84268 84272 84276 84277 84284 84292 84293 84300
  84308 84309 84316 84324 84325 84332 84340 84341 84351
  84352 84479 84480 84596. 0 removed (== GATE).
  PINS N-set == for-list 5712/5712.
- Own-loop 84249..84596 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P194 C-vs-py mechanical, ALL 22 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, BM 9/9,
  OM 16/16, OR 4/4, OT 4/4, RM 16/16, RQ 16/16; AC 74/74,
  BC 71/71, OC 61/61, RC 65/65 (py-hex vs C-decimal
  normalized); M/QR/QT/QC absent BOTH sides (grep 0 hits
  both files); C _N decls 74/71/61/65 match actual rows
  (== GATE). Sigs first-hand: S0=48030000, S1=20900600,
  S2=6fcd0700 (all NEW, == GATE).
- Dispatch by eye both impls, 7 tiers in order: S0
  n=84249 / S1 n=84250 singletons; A 84251-84266
  off=n-84251, mtab 8B b20-23/76-79, raw lencode (b5
  emergent-const 92 across range, arith-verified);
  S2 n=84267 SING; B 84268-84276 off=n-84268, mtab 11B
  b20-26/80-83, raw lencode (b5 emergent-const 92,
  arith-verified); O 84277-84340 off=n-84277 m=off&15
  q=off>>4, SHARED mtab 10B b20-22/26-28/76-79, row-tuple
  r7 b0-2/18/19/24/25, tails b80-83, raw lencode; R
  84341-84596 off=n-84341 TRANSPOSED, b4=(0xeb+2off)&FF
  b5=0x92+(off>=11)+(off>=139), M8 b32-35/76-79 by COL
  off&15, Q9 b24-28/72-75 by ROW off>>4; all paylen 84.
  C blocks carry T53655/660/665/680/685/701/725 py-line
  mirrors (7/7 == GATE). Insert position exact both sides:
  after T10P193R close (py L53653-53654 / C L146230-31),
  before dispatch-tail fallthrough (py L53744 / C L146449).
  (== GATE. No Q tier anywhere — matches A-416.)
- py diff pure addition: rgram.py +242/+0 (0 del lines),
  test_rgram.sh +1/-1, PINS +54/+0.
- C diff renumber-only + new: numstat 2089 add / 1469 del
  (== GATE); raw grep 2082 add / 1469 del + 7 blank-only
  `+` lines verified (== GATE); fine-norm del-uniq 1466 /
  add-uniq 1848 (== GATE exact), del-subset-add 0 missing.
- Wall on band diff added lines (55308f7c..de815ae0, 2379
  grep-added lines + 7 empty == GATE scope): vendor/disasm/
  depload/dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load/
  libcompression/shebang 0 hits. Files: rgramc.c, rgram.py,
  test_rgram.sh (for-line 1/1), PINS (+54/+0). Py side
  purely additive.
- CONFIRM evidence: A-416-q425-t10p194-geometry verdict
  CONFIRM (58/58 checks, A-264 corroborates; == GATE),
  no DISSENT (CONVERT-01 rule b).
- GATE prose CORRECT throughout (build+sha, counts,
  for-list, tables, _N decls, absent-tables, sigs, mtab/
  byte lists, counters, T-mirrors, insert position,
  blank-line accounting, A-416 recon). No slips.

Agrees with GATE-de815ae0 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r32/
(*302* files).

Verdict: PASS. Ready for parent PV + merge.
