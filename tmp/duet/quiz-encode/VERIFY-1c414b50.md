# VERIFY-1c414b50 b299 T10P191 pins 83205..83296 (1074 tiers): PASS

viewer-r32, first-hand, detached tree NVME tmp/encode-viewer/r32/
tree-1c414b50 @1c414b50 (base cf3d8483 = b298 tip), seat build
build299/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2528600 B, sha256 rgramc 464efd20 / aae d6e27c97
  (GATE cites aae sha only == match; rgramc sha first-hand).
- RGRAMC-PYID 5630/5630 covered=5630/5630 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11260/11260 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11260/11260 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11260/11260).
- PINS-RGRAM cell set-eq 11260/11260 (cmp-identical; == GATE).
  PINS N-set == for-list 5630/5630 (== GATE).
- PINS 11262 rows = 2 hdr + 11260, +32 vs base (11230).
  For-list +16 exactly: 83205 83206 83207 83214 83222
  83223 83224 83228 83232 83233 83248 83249 83265 83281
  83295 83296. 0 removed (== GATE).
- Own-loop 83205..83296 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P191 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, BM 9/9,
  M 16/16, QR 4/4, QT 4/4; AC 75/75, BC 71/71, QC 64/64
  (py-hex vs C-decimal normalized); C _N decls 75/71/64
  match actual rows (== GATE). Sigs first-hand:
  S0=1e030000 (REPEAT x3 per comment), S1=6a410600 (NEW),
  S2=6d410600 (NEW); A b0-3 AC=d2166400 (NEW);
  B b0-3 BC=b6200300 (NEW); Q b0-3 QC=6e0b3200.
- Dispatch by eye both impls, 6 tiers in order: S0
  n=83205 / S1 n=83206 singletons (offs 0/1); A 83207-
  83222 off=n-83207, mtab 7B b9-11/76-79; S2 n=83223
  singleton (off 18); B 83224-83232 off=n-83224, mtab
  11B b13-19/80-83; Q 83233-83296 off=n-83233 m=off&15
  q=off>>4, M 7B b20-22/76-79, R 7B b13-19, T 4B
  b80-83; all paylen 84, raw lencode b4/b5 (b5=0x8a
  whole tier emergent, arith-verified all 3 ranges).
  C blocks carry T52879/884/889/904/909/925 py-line
  mirrors (6/6 == GATE). Insert position exact both
  sides: after T10R188 close (py L52876-52877 / C
  L144245), before T10R189 (n<=83552, base 83297;
  py L52948 / C L144454). (== GATE.)
- py diff pure addition: rgram.py +173/+0 (0 del lines),
  test_rgram.sh +1/-1, PINS +32/+0.
- C diff renumber-only + new: numstat 1925 add / 1464 del;
  raw grep 1919 add / 1464 del + 6 blank-only `+` / 0
  blank-only `-` (all == GATE; 1919+6=1925 consistent).
  Coarse-norm ([0-9]+ -> N, cut-c2) del-uniq 928 /
  add-uniq 1048 / 0 missing (== GATE exact). Fine-norm
  (r31 recipe) del-uniq 1460 / add-uniq 1768 / 0 missing.
- Wall on band diff added lines (cf3d8483..1c414b50, 2125
  grep-added lines + 6 empty = 2131 == GATE scope):
  vendor/disasm/depload/dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load/libcompression/shebang 0 hits. Files:
  rgramc.c, rgram.py, test_rgram.sh (for-line 1/1),
  PINS (+32/+0). Py side purely additive.
- CONFIRM evidence: A-410-q422p191-t10p191-geometry verdict
  CONFIRM (34/34 checks; == GATE), no DISSENT
  (CONVERT-01 rule b).
- GATE prose CORRECT throughout (build, counts, for-list,
  tables, _N decls, sigs, mtab byte lists, T-mirrors,
  insert position, blank-line accounting, coarse renumber
  counts, A-410 recon). No slips. (GATE omits rgramc sha;
  recorded first-hand above. Not a slip — no claim made.)

Agrees with GATE-1c414b50 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r32/
(*299* files).

Verdict: PASS. Ready for parent PV + merge.
