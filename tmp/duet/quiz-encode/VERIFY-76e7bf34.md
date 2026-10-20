# VERIFY-76e7bf34 b310 T10P202 pins 87033..87380 (1182 tiers): PASS

viewer-r34, first-hand, detached tree NVME tmp/encode-viewer/r34/
tree-76e7bf34 @76e7bf34 (base 27d39094 = b309 tip), seat build
build310/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2698792 B, sha256 rgramc 1c798145 / aae d6e27c97
  (BOTH == GATE).
- RGRAMC-PYID 5952/5952 covered=5952/5952 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11904/11904 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11904/11904 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11904/11904).
- PINS-RGRAM cell set-eq 11904/11904 (cmp-identical).
  PINS N-set == for-list 5952/5952 (== GATE "5952/5952";
  standing half-cell phrasing, full cells 2x verified).
- PINS 11906 rows = 2 hdr + 11904 (== GATE). For-list +29
  exactly: 87033 87034 87035 87039 87040 87050 87051
  87052 87053 87056 87060 87061 87068 87076 87077 87084
  87092 87093 87100 87108 87109 87116 87124 87125 87167
  87168 87295 87296 87380. 0 removed (== GATE). 5952x2 =
  11904 PASS lines (== GATE). +29 carries flips
  {87040,87168,87296} + ring edges 87167/87168 +
  87295/87296 (== GATE DET29 note).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 87033..87380 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P202 C-vs-py mechanical, ALL EXACT: S0..S3
  168-hex-char singletons 1/1 each (sigs 9e030000 /
  7c3d0700 / df830600 / 4f4c0600 == GATE); AM 16/16,
  BM 8/8, WM 16/16, RM 16/16, RQ 16/16; AC 75/75,
  BC 71/71, WAC 73/73, WBC 73/73, WC0C 73/73,
  WC1C 73/73, RC 67/67 (py-hex vs C-decimal normalized);
  M/QR/QT/QC/CM/CC absent-both 0/0 (non-Q band, == GATE);
  C _N decls 75/71/73/73/73/73/67 match actual rows
  (== GATE). Sigs first-hand: A=c8d77300, B=be9e0300,
  WA=4f3a3b00, WB=ff683a00, WC0=WC1=37163900,
  R=c7489e03 (== GATE, const-table b0-3). Code-consts
  PBA 75 / PBB8 71 / rows 73x4 / T 67 == A-439 §3-§4
  (PBA 75 per §4 ruling; == GATE).
- Dispatch by eye both impls, 11 tiers in order: S0
  n=87033 (PB0 9e030000 NEW chain) / S1 n=87034 (fat
  PB1); A 87035-87050 off=n-87035, mtab 7B b20-22/
  76-79, b5 CARRY @87040 (87039 ff/a7 -> 87040 01/a8
  arith-ok); S2 n=87051 / S3 n=87052 singles; B
  87053-87060 PBB8 off=n-87053, mtab 11B b20-26/80-83,
  b5 const; WA 87061-87076 / WB 87077-87092 / WC0
  87093-87108 / WC1 87109-87124, all shared WM[off]
  9B b20,21,22,26,27/76-79 + own consts WAC/WBC/WC0C/
  WC1C (verified per-row); R 87125-87380 off=n-87125
  c=off&15 r=off>>4 T-ring TRANSPOSED (12th),
  b4=(0xab+2off)&FF b5=0xa8+(off>=43)+(off>=171)
  (C: 171/168 literals ==), M7 b32-34/76-79 by COL,
  Q8 b24-27/72-75 by ROW; A/B/W raw lencode, all
  paylen 84. T-ring edges arith-ok: 87167->87168
  ff/a8->01/a9 (off 42->43) + 87295->87296 ff/a9->
  01/aa (off 170->171); flips {87040,87168,87296}
  all in for-list (== GATE). Row-const diffs
  first-hand: a-b 10B [0,1,2,19,24,25,80-83] /
  a-c0 12B +[11,18] (== GATE == A-439/A-272 sets);
  WC0-vs-WC1 differ b80 only (9c/d0 half-flags ==
  memo), b4 via lencode (== GATE "halves identical
  ex-b4+b80"). C blocks carry T55941/946/951/966/
  971/976/992/007/022/037/052 py-line mirrors (11/11
  exact == GATE; T55941=S0 ... T56052=R). Insert
  position exact both sides: after T10P201R close, at
  dispatch tail ("N out of scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +319/-0 in 2 hunks
  (tables after _T10P201RC, dispatch in main()),
  test_rgram.sh +1/-1 (for-line only), PINS +58/+0.
- C diff renumber-only + new: numstat 2489 add / 1544 del;
  raw grep 2478 non-blank add + 11 blank-only `+` /
  1544 del / 0 blank-only `-` (all == GATE; 2478+11 =
  2489 consistent). Fine-norm (b304-calibrated):
  del-uniq 1540 / add-uniq 1973 / 0 missing (== GATE
  exact under blanks-pre-filtered/empty-excluding
  variant; blank-including variant is 1974, miss 0
  either way — same accounting note as b308; sed
  mapping is the b302-validated one).
- Wall on band diff added lines (27d39094..76e7bf34):
  vendor/disasm/depload/CT-shim//usr/bin/aa 0 hits over
  the FULL 2867-line added scope verified first-hand.
  (GATE scope "2856" = non-blank adds 2478+319+1+58;
  same blank pre-filtering as its raw/fine steps;
  verdict 0-hits holds over both scopes — accounting
  note, not FAIL.) Files: rgramc.c 2489/1544, rgram.py
  +319/+0 purely additive, test_rgram.sh 1/1, PINS
  +58/+0 (== GATE).
- CONFIRM evidence: A-439-q434-t10p202 verdict CONFIRM
  (36/37 + bookkeeping FINDING on PBA code-consts
  74-vs-75, ruled code uses 75 per §4; file present,
  counts verified: 17+11+8+finding; == GATE), A-272
  corroborates incl-consts 75/72/74-74-73/67 + VPOS +
  rowdiffs + halves (== GATE), no DISSENT
  (CONVERT-01 rule b; A-439 §4 cites A-413 precedent:
  CONFIRM-with-finding). No CONFIRM-P202.md file
  (== GATE; A-439 suffices per rule). GATE's A-439
  cites (VPOS A 9 / B 12 / rows 10/10/11 / R 17, sigs,
  lencode 92/92, M9 shared 16/16 all 3 groups, ROW32
  halves identical ex-b4+b80, constdiffs a-b 10B /
  a-c0 12B, M-tails ALL NEW vs P201T, T-ring edges,
  flips, DET29 29/29) all verbatim in file (rowdiff
  sets + b80 9c/d0 re-verified first-hand in code).
  Memo code consts 75/71/73x4/67 == code tables; incl
  reconciles (rows 74/74/73 = WA/WB/WC32-group =
  84-VPOS). Agrees with cport commit msg (PYID 5952,
  RGRAM 11904; == GATE). No FLAG on b310. GATE's
  "newest PARENT-* QNUM-03" TRUE at filing (GATE 14:03,
  QNUM-03 13:50, QNUM-04/05 14:08/14:14 after; writer
  Q-blocks, no gate impact).
- GATE prose CORRECT throughout (build incl both shas,
  counts, for-list, tables incl 4-row consts + _N decls
  + M/QR/QT/QC-absent, sigs, A-carry + counter formulas,
  edge arithmetic, rowdiff sets, T-mirrors, insert
  position, blank-line accounting, fine renumber counts,
  A-439/A-272 recon incl §4 ruling). No slips. Two
  blank-accounting notes above (add-uniq excl-1973 vs
  incl-1974; wall scope 2856 vs 2867); miss 0 / hits 0
  either way.

Agrees with GATE-76e7bf34 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r34/
(*310* files).

Verdict: PASS. Ready for parent PV + merge.
