# VERIFY-55308f7c b301 T10P193 pins 83901..84248 (1098 tiers): PASS

viewer-r32, first-hand, detached tree NVME tmp/encode-viewer/r32/
tree-55308f7c @55308f7c (base 850d20f4 = b300 tip), seat build
build301/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2562632 B, sha256 rgramc 726c67fa / aae d6e27c97
  (GATE cites aae sha only == match; rgramc sha first-hand).
- RGRAMC-PYID 5685/5685 covered=5685/5685 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11370/11370 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11370/11370 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11370/11370).
- PINS-RGRAM cell set-eq 11370/11370 (cmp-identical; == GATE).
  PINS N-set == for-list 5685/5685 (== GATE).
- PINS 11372 rows = 2 hdr + 11370, +52 vs base (11320).
  For-list +26 exactly: 83901 83902 83903 83910 83918
  83919 83920 83921 83922 83923 83926 83928 83929 83944
  83945 83961 83967 83968 83977 83992 83993 84095 84096
  84223 84224 84248. 0 removed (== GATE).
- Own-loop 83901..84248 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P193 C-vs-py mechanical, ALL 22 EXACT: S0/S1/S2/S3
  168-hex-char singletons 1/1 each; AM 16/16, BM 2/2,
  CM 6/6, M 16/16, QR 4/4, QT 4/4, RM 16/16, RQ 16/16;
  AC 74/74, BC 71/71, CC 70/70, QC 64/64, RC 70/70
  (py-hex vs C-decimal normalized); C _N decls 74/71/70/
  64/70 match actual rows (== GATE). Excl-b5 accounting
  confirmed in-table: no b5 entry in any of the 5 const
  tables (== GATE). Sigs first-hand: S0=20030000 (REPEAT
  P192), S1=47a20700, S2=1b330300 (NEW), S3=47a20700;
  A=47a26700, B=47a20700 (== PB1), C=1b330300 (== 83921),
  Q=b1313300, R=101b3303 (== GATE).
- Dispatch by eye both impls, 9 tiers in order: S0
  n=83901 / S1 n=83902 singletons (offs 0/1); A 83903-
  83918 off=n-83903, mtab 8B b48-51/76-79; B 83919-83920
  off=n-83919, mtab 11B b23/46-51/80-83; S2 n=83921 /
  S3 n=83922 singletons (offs 20/21); C 83923-83928
  off=n-83923, mtab 12B b35/45-51/80-83; Q 83929-83992
  off=n-83929 m=off&15 q=off>>4, M 6B b6,7/76-79, R 8B
  b35/45-51, T 4B b80-83; R 83993-84248 off=n-83993
  TRANSPOSED, b4=(0x33+2off)&FF b5=0x90+(off>=103)+
  (off>=231), M6 b13,14/76-79 by COL off&15, Q6 b6,7/
  72-75 by ROW off>>4; A/B/C/Q raw lencode, all paylen
  84. C blocks carry T53393/398/403/418/434/439/444/460/
  483 py-line mirrors (9/9 == GATE). Insert position exact
  both sides: after T10P192R close (py L53391-53392 / C
  L145569), before dispatch-tail fallthrough (py L53502 /
  C L145829). (== GATE.)
- py diff pure addition: rgram.py +279/+0 (0 del lines),
  test_rgram.sh +1/-1, PINS +52/+0.
- C diff renumber-only + new: numstat 2209 add / 1460 del;
  raw grep 2200 add / 1460 del + 9 blank-only `+` / 0
  blank-only `-` (all == GATE; 2200+9=2209 consistent).
  Coarse-norm ([0-9]+ -> N, cut-c2) del-uniq 937 /
  add-uniq 1108 / 0 missing (== GATE exact). Fine-norm
  (r31 recipe) del-uniq 1457 / add-uniq 1870 / 0 missing.
- Wall on band diff added lines (850d20f4..55308f7c, 2532
  grep-added lines + 9 empty = 2541 == GATE scope):
  vendor/disasm/depload/dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load/libcompression/shebang 0 hits. Files:
  rgramc.c, rgram.py, test_rgram.sh (for-line 1/1),
  PINS (+52/+0). Py side purely additive.
- CONFIRM evidence: A-415-q424-t10p193-geometry verdict
  CONFIRM (47/47 checks, A-263 corroborates; == GATE),
  no DISSENT (CONVERT-01 rule b). Memo incl-counts
  75/72/71/64/70 per A-263 noted in file, consistent
  with GATE's excl/incl accounting note.
- GATE prose CORRECT throughout (build, counts, for-list,
  tables incl BM 2/2 + CM 6/6 widths, _N decls, excl-b5
  note, sigs, mtab byte lists, counters, T-mirrors,
  insert position, blank-line accounting, coarse renumber
  counts, A-415 recon). No slips. (GATE omits rgramc sha;
  recorded first-hand above. Not a slip — no claim made.)

Agrees with GATE-55308f7c (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r32/
(*301* files).

Verdict: PASS. Ready for parent PV + merge.
