# VERIFY-c8b4a6a6 b313 T10P205 pins 88077..88424 (1204 tiers): PASS

viewer-r35, first-hand, detached tree NVME tmp/encode-viewer/r35/
tree-c8b4a6a6 @c8b4a6a6 (base 13c46dc8 = b312 tip), seat build
build313/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2733192 B, sha256 rgramc bfcb862a (first-hand;
  GATE cites aae only, same standing sweep pattern as
  b307/b309/b311) / aae d6e27c97 (== GATE).
- RGRAMC-PYID 6030/6030 covered=6030/6030 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 12060/12060 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 12060/12060 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (12060/12060).
- PINS-RGRAM cell set-eq 12060/12060 (cmp-identical).
  PINS N-set == for-list 6030/6030 (== GATE "6030/6030").
- PINS 12062 rows = 2 hdr + 12060 (== GATE; +52 vs base
  12010). For-list +26 exactly: 88077 88078 88079 88086
  88094 88095 88097 88098 88101 88104 88105 88120 88121
  88136 88137 88152 88153 88168 88169 88191 88192 88319
  88320 88408 88409 88424. 0 removed (== GATE). 6030x2 =
  12060 PASS lines. +26 carries ring edges 88191/88192 +
  88319/88320 + R-end/T-start/T-end 88408/88409/88424.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 88077..88424 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P205 C-vs-py mechanical, 21-table ALL EXACT:
  S0/S1 168-hex-char singletons 1/1 each (sigs 94070000
  / 6b850e00 == GATE); AM 16/16, FM0 6/6, FM1 4/4, M
  16/16, QR1 2/2, QT1 2/2, QR2 2/2, QT2 2/2, RM 16/16,
  RQ 15/15; AC 75/75, FC0 69/69, FC1 70/70, QC1 63/63,
  QC2 69/69, RC 68/68, TC 76/76 (py-hex vs C-decimal
  normalized); FS 10/10 + FO 10/10 (py-hex-tuple vs
  C-long-array as ints); FS order 0d,0d,05,0d,0d,05,
  05,0d,0d,05 == memo interleave (== GATE); B/BC/BM/
  Q/QC/QR/QT/CM/CC absent-both via definition-site
  inventory (== GATE; substring-safe vs QR1/QT1/QC1);
  C _N decls 75/69/70/63/69/68/76 match actual rows
  (== GATE). No b4/b5 entry in any of the 7 const
  tables (excl accounting == GATE). Sigs first-hand:
  A=6b85f200, F0=1d6a0d00, F1=1d6a0500, H1=1d6af100,
  H2=1d6a7900, R=1d6add0e, T=1d6ae50e (== GATE,
  const-table b0-3). Code-consts 75/69/70/63/69/68/
  76 vs memo incl 76/70/71/64/70/68/77: +1 = b5-const
  (A/F/H1/H2 b0 computed first-hand, T b2 continued),
  R +0 counter (== GATE).
- Dispatch by eye both impls, 8 blocks in order: S0
  n=88077 (PB0 94070000 NEW) / S1 n=88078 (fat PB1
  6b850e00); A 88079-88094 off=n-88079, mtab 7B
  b24-26,76-79, b5 const b0, raw lencode; F 88095-
  88104 off=n-88095, sigtag pay[2]==FS[off], k=FO[off],
  0x0D->FM0[k]/FC0 (mtab F0 13B b20,21,25-31,80-83)
  else 0x05->FM1[k]/FC1 (F1 12B b20,21,25-30,80-83),
  C: ==13/==5 literals ==, b5 const b0, raw lencode;
  H1 88105-88136 off=n-88105 m=off&15 h=off>>4, M8
  b32-35,76-79 + QR1 R7 b24-30 + QT1 b80-83, b5
  const b0, raw lencode; H2 88137-88168 same M8 +
  QR2 R1 b25 + QT2 b80-83, b5 const b0, raw lencode;
  R 88169-88408 off=n-88169 c=off&15 r=off>>4 T240
  TRANSPOSED (15th, "NO swap" comment ==), b4=
  (0xd3+2off)&FF (C: 211 literal ==) b5=0xb0+
  (off>=23)+(off>=151) (C: 176 literal ==), RM
  b37,38,76-79 by COL, RQ b21-23,31,72-75 by ROW;
  T 88409-88424 off=n-88169 (continued ring counter,
  same formulas both sides) k=n-88409, RM[k]
  positional, TC consts; all paylen 84. Counter
  edges arith-verified first-hand: A/F/H1/H2 b5
  const b0 over full tier ranges; R off22->23
  (88191->88192) ff/b0->01/b1 + off150->151
  (88319->88320) ff/b1->01/b2; T b5 const b2 over
  off240-255 (continued); all edge/flip Ns in
  for-list (== GATE). C blocks carry T56783/788/
  793/808/838/861/883/902 py-line mirrors (8/8
  exact == GATE). Insert position exact both sides:
  after T10P204R close, at dispatch tail ("N out of
  scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +344/-0 (0 deletions,
  2 hunks: tables after _T10P204RC + dispatch in main()),
  test_rgram.sh +1/-1 (for-line only), PINS +52/+0
  (== GATE "py diff +52/-0" = PINS leg).
- C diff renumber-only + new: numstat 2541/1569; raw
  grep 2533 non-blank add / 1569 del / 8 bare `+` /
  0 blank `-` (2533+8=2541 consistent; GATE "(incl 8
  blank-plus)" = same sweep convention as b307/b309/
  b311, ruled CORRECT — not a slip). Coarse-norm
  ([0-9]+->N + cut-c2): del-uniq 1022 / add-uniq 1236
  / 0 missing (all == GATE exact).
- Wall on band diff added lines (13c46dc8..c8b4a6a6):
  vendor/disasm 0, depload 0, CT-shim/shebang +
  /usr/bin/aa 0, over 2930 added lines (== GATE;
  8 bare blanks definitionally clean). Files:
  rgramc.c, rgram.py, test_rgram.sh (for-line), PINS
  (== GATE).
- Band composition: c8b4a6a6^ = 2dd2e15e single parent;
  2dd2e15e = merge 13c46dc8 + c2b4ec3a (== GATE;
  cport msg PYID 6030 / RGRAM 12060 agrees).
- CONFIRM evidence: A-456-q437-t10p205 predictions
  reproduce 31/31 (file present; lencode 92/92, T240
  240/240, shape/mid/ring/counters CONFIRM) + 2
  FINDINGS adopted (ring CLASSIC transposed NOT
  tails-swapped == impl "NO swap" comment; no
  ring-Q/quad-M swap relation; == GATE), A-275
  corroborates same tier incl consts 76/70/71/64/
  70/68/77 + CORRECTION re-tagging H1/H2/tail b5
  const (counts stand as filed) + NO D dips (==
  GATE), no DISSENT (CONVERT-01 rule b re memo-A
  CONFIRM; A-456 "CONFIRM with FINDINGS" + A-275
  "CONFIRM + CORRECTION" both adoptable per A-413/
  A-439 precedent class). GATE's geometry cites
  (PBA VPOS b4+M7, FRAG10 interleave == FS — also
  position-verified per-N vs A-275's 0dx6/05x4
  lists, VPOS 14/13, H1/H2 shared M8 16/16 x4,
  H1 R7 2/2 + H2 R1 0x70/0x72, tails 4/4, T240
  TRANSPOSED 15th CLASSIC, TAIL16 == ring row-15
  M positional 16/16 + Q15 novel, RQ 15 rows ==
  T240 15/15, M-tails ALL NEW 0/16, NO D dips)
  all verbatim in files. No FLAG/CLAIM/GATE
  conflict on b313 (GATE-c81821f confirmed unrelated
  writer2 gate == GATE parenthetical). No newest-
  PARENT claim in GATE (turf note only); QNUM-06/07
  postdate, writer Q-blocks, no gate impact.
- GATE prose CORRECT throughout (build, counts,
  for-list, 21 tables incl FS/FO + absent inventory
  + _N, F-split, sigs, b5-consts, edge arithmetic,
  T-mirrors, insert, blank accounting, coarse
  renumber counts, A-456/A-275 recon). No slips.

Agrees with GATE-c8b4a6a6 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r35/
(*313* files).

Verdict: PASS. Ready for parent PV + merge.
