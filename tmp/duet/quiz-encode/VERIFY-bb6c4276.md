# VERIFY-bb6c4276 b308 T10P200 pins 86337..86684 (1164 tiers): PASS

viewer-r34, first-hand, detached tree NVME tmp/encode-viewer/r34/
tree-bb6c4276 @bb6c4276 (base 49329853 = b307 tip), seat build
build308/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2664952 B, sha256 rgramc 121de84d / aae d6e27c97
  (BOTH == GATE).
- RGRAMC-PYID 5894/5894 covered=5894/5894 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11788/11788 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11788/11788 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11788/11788).
- PINS-RGRAM cell set-eq 11788/11788 (cmp-identical).
  PINS N-set == for-list 5894/5894 (== GATE "5894/5894";
  standing half-cell phrasing, full cells 2x verified).
- PINS 11790 rows = 2 hdr + 11788 (== GATE). For-list +34
  exactly: 86337 86338 86339 86346 86354 86355 86356
  86357 86358 86359 86360 86361 86362 86363 86364 86365
  86372 86380 86381 86388 86396 86397 86399 86400 86412
  86413 86420 86428 86429 86527 86528 86655 86656 86684.
  0 removed (== GATE). 5894x2 = 11788 PASS lines (== GATE).
  +34 carries flips {86400,86528,86656} + ring edges
  86527/86528 + 86655/86656 (== GATE DET34 note).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 86337..86684 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P200 C-vs-py mechanical, ALL EXACT: S0..S9
  168-hex-char singletons 1/1 each (sigs 74030000 /
  51de0500 / 83260300 / 97bb0300 / 5f950300 / 7f7f0300 /
  832e0300 / 97bb0300 / 7f7f0300 / 832e0300; 8-singles
  order == GATE exact, 5 distinct, ALL NEW vs P199
  72030000/c7e90600); AM 16/16, BM 2/2, M 16/16,
  QR 4/4, QT 4/4, RM 16/16, RQ 16/16; AC 75/75,
  BC 72/72, QC 64/64, RC 69/69 (py-hex vs C-decimal
  normalized); CM/CC absent-both 0/0 (no C tier);
  C _N decls 75/72/64/69 match actual rows (== GATE).
  Sigs first-hand: A=51de6d00, B=51de0500 (==PB1/S1),
  Q=51de3500, R=51de9103 (== GATE, const-table b0-3).
  Code-consts 75/72/64/69 == A-436 (== GATE).
- Dispatch by eye both impls, 14 tiers in order: S0
  n=86337 (PB0 74030000 BREAKS chain) / S1 n=86338
  (fat PB1); A 86339-86354 off=n-86339, mtab 7B
  b32-34/76-79; B 86355-86356 off=n-86355, mtab 10B
  b22,23,30/36-38/80-83; 8 singles 86357-86364
  (all 84B, sigs in GATE order); Q 86365-86428
  off=n-86365 m=off&15 q=off>>4, M 7B b36-38/76-79,
  QR 7B b22,23,30-34, QT b80-83, raw lencode with
  b5-carry @off35 (86399 ff/a2 -> 86400 01/a3
  arith-ok); R 86429-86684 off=n-86429 c=off&15
  r=off>>4 T-ring TRANSPOSED (10th), b4=(0x3b+2off)&FF
  b5=0xa3+(off>=99)+(off>=227) (C: 59/163 literals
  ==), M6 b42,43/76-79 by COL, Q7 b36-38/72-75 by
  ROW; A/B/Q raw lencode, all paylen 84. T-ring edges
  arith-ok: 86527->86528 ff/a3->01/a4 (off 98->99) +
  86655->86656 ff/a4->01/a5 (off 226->227); flips
  {86400,86528,86656} all in for-list (== GATE). C
  blocks carry T55371/376/381/396/412/417/422/427/
  432/437/442/447/452/475 py-line mirrors (14/14
  exact == GATE). Insert position exact both sides:
  after T10P199R close, at dispatch tail ("N out of
  scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +277/-0 in 2 hunks
  (tables after _T10P199RC, dispatch in main()),
  test_rgram.sh +1/-1 (for-line only), PINS +68/+0.
- C diff renumber-only + new: numstat 2233 add / 1522 del;
  raw grep 2219 non-blank add + 14 blank-only `+` /
  1522 del / 0 blank-only `-` (all == GATE; 2219+14 =
  2233 consistent). Fine-norm (calibrated: reproduces
  b304 1481/1976/0 exactly): del-uniq 1518 / add-uniq
  1926 / 0 missing (== GATE exact under blanks-
  pre-filtered/empty-excluding variant; blank-including
  variant is 1927, miss 0 either way — accounting note,
  cf r33 b304/b306 incl convention; sed mapping is the
  b302-validated one either way).
- Wall on band diff added lines (49329853..bb6c4276):
  vendor/disasm/depload/CT-shim//usr/bin/aa 0 hits over
  the FULL 2579-line added scope verified first-hand.
  (GATE scope "2565" = non-blank adds 2219+277+1+68;
  same blank pre-filtering as its raw/fine steps;
  verdict 0-hits holds over both scopes — accounting
  note, not FAIL.) Files: rgramc.c 2233/1522, rgram.py
  +277/+0 purely additive, test_rgram.sh 1/1, PINS
  +68/+0 (== GATE).
- CONFIRM evidence: A-436-q432-t10p200 verdict CONFIRM
  40/40 (18+13+9 sections + 40/40 verdict line; ==
  GATE "file present, counts verified"), A-270
  corroborates incl-consts 76/73/64/69 (== GATE), no
  DISSENT (CONVERT-01 rule b). No CONFIRM-P200.md file
  (== GATE; A-436 suffices per rule). GATE's A-436
  cites (VPOS A b4+M7 / B b4+M10 / Q 20 / R 15, sigs,
  lencode 92/92, M7 row-indep 16/16x4 shared, R7
  bottom-paired r2==r3, tails 4/4 distinct, M-tails ALL
  NEW vs P199T, T-ring edges, flips, DET34 34/34) all
  verbatim in file. Memo code consts 75/72/64/69 ==
  code tables; incl 76/73/64/69 consistent. Agrees
  with cport commit msg (PYID 5894, RGRAM 11788;
  == GATE). No FLAG on b308. GATE's "newest PARENT-*
  QNUM-03" TRUE at filing (GATE 13:59, QNUM-03 13:50,
  QNUM-04/05 14:08/14:14 after; writer Q-blocks, no
  gate impact).
- GATE prose CORRECT throughout (build incl both shas,
  counts, for-list, tables incl CM/CC-absent implication
  via table list + _N decls, sigs incl 8-singles order,
  mtab byte lists, Q-carry + counter formulas, edge
  arithmetic, T-mirrors, insert position, blank-line
  accounting, fine renumber counts, A-436/A-270 recon).
  No slips. Two blank-accounting notes above (add-uniq
  excl-1926 vs incl-1927; wall scope 2565 vs 2579);
  miss 0 / hits 0 either way.

Agrees with GATE-bb6c4276 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r34/
(*308* files).

Verdict: PASS. Ready for parent PV + merge.
