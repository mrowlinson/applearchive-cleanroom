# VERIFY-bf0ee03b b311 T10P203 pins 87381..87728 (1188 tiers): PASS

viewer-r35, first-hand, detached tree NVME tmp/encode-viewer/r35/
tree-bf0ee03b @bf0ee03b (base 76e7bf34 = b310 tip), seat build
build311/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2699176 B, sha256 rgramc dd70009a (first-hand;
  GATE cites aae only, same standing sweep pattern as
  b307/b309) / aae d6e27c97 (== GATE).
- RGRAMC-PYID 5978/5978 covered=5978/5978 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11956/11956 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11956/11956 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11956/11956).
- PINS-RGRAM cell set-eq 11956/11956 (cmp-identical).
  PINS N-set == for-list 5978/5978 (== GATE "5978/5978").
- PINS 11958 rows = 2 hdr + 11956 (== GATE; +52 vs base
  11906). For-list +26 exactly: 87381 87382 87383 87390
  87398 87399 87403 87408 87409 87423 87424 87425 87432
  87440 87441 87448 87456 87457 87464 87472 87473 87551
  87552 87679 87680 87728. 0 removed (== GATE). 5978x2 =
  11956 PASS lines (== GATE). +26 carries Q-carry pair
  87423/87424 + ring edges 87551/87552 + 87679/87680.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 87381..87728 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P203 C-vs-py mechanical, ALL EXACT: S0/S1
  168-hex-char singletons 1/1 each (sigs 9e030000 /
  95020500 == GATE); AM 16/16, BM 10/10, M 16/16,
  QR 4/4, QT 4/4, RM 16/16, RQ 16/16; AC 76/76,
  BC 70/70, QC 63/63, RC 65/65 (py-hex vs C-decimal
  normalized); B42 16/16 (py-hex-tuple vs C-long-array
  as ints); T/TC/CM/CC absent-both (== GATE); C _N
  decls 76/70/63/65 match actual rows (== GATE). No
  b4/b5 entry in any of the 4 const tables (excl
  accounting == GATE). Sigs first-hand: A=95027100,
  B=95020500, Q=95026d00, R=95022d07 (== GATE,
  const-table b0-3). Code-consts 76/70/63/65 == A-441
  §3 (incl 77/71/63/65 reconciled, == GATE).
- Dispatch by eye both impls, 6 blocks in order: S0
  n=87381 (PB0 9e030000 REPEAT P202) / S1 n=87382 (fat
  PB1 95020500) singleton-const offs 0/1; A 87383-87398
  off=n-87383, mtab 6B b36,37/76-79, b5 const aa,
  raw lencode; B 87399-87408 off=n-87399, mtab 12B
  b32,33/37-42/80-83, b5 const aa, raw lencode; Q
  87409-87472 off=n-87409 m=off&15 q=off>>4, M8
  b23,34,35,43,76-79 + b42 rule (b42b=B42[m],
  b42e=q<2?b42b:b42b-1, C ternary ==) + QR sigr6
  b36-41 + QT tails b80-83, raw lencode; R 87473-87728
  off=n-87473 c=off&15 r=off>>4 T-ring TRANSPOSED
  (13th) + TAILS-SWAPPED (4th), b4=(0x63+2off)&FF
  (C: 99 literal ==) b5=0xab+(off>=79)+(off>=207)
  (C: 171 literal ==), M8 b48-51,72-75 by COL,
  Q9 b23,34,35,42,43,76-79 by ROW; A/B/Q raw
  lencode l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF
  pay5=l16>>8, all paylen 84. Counter edges
  arith-verified first-hand: A/B b5 const aa over
  full tier ranges; Q 87423->87424 ff/aa->01/ab
  (@off15); R off78->79 (87551->87552) ff/ab->
  01/ac + off206->207 (87679->87680) ff/ac->01/ad;
  all edge/flip Ns in for-list (== GATE). C blocks
  carry T56228/233/238/253/269/296 py-line mirrors
  (6/6 exact == GATE). Insert position exact both
  sides: after T10P202R close, at dispatch tail ("N
  out of scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +244/-0 (0 deletions,
  2 hunks: tables after _T10P202RC + dispatch in main()),
  test_rgram.sh +1/-1 (for-line only), PINS +52/+0
  (== GATE "py diff +52/-0" = PINS leg).
- C diff renumber-only + new: numstat 2167/1555; raw
  grep 2161 non-blank add / 1555 del / 6 blank-only `+`
  / 0 blank-only `-` (2161+6=2167 consistent; GATE
  "(incl 6 blank-plus)" = same sweep convention as
  b307/b309 GATEs, ruled CORRECT r34 — not a slip).
  Coarse-norm (b304-calibrated [0-9]+->N + cut-c2):
  del-uniq 1010 / add-uniq 1185 / 0 missing (all ==
  GATE exact).
- Wall on band diff added lines (76e7bf34..bf0ee03b):
  vendor/disasm 0, depload 0, CT-shim/shebang +
  /usr/bin/aa 0, over 2458 added lines (== GATE).
  Files: rgramc.c, rgram.py, test_rgram.sh (for-line),
  PINS (== GATE).
- Band composition: bf0ee03b^ = 664b1070 single parent;
  664b1070 = merge 76e7bf34 + 6e356170 (== GATE;
  cport msg PYID 5978 / RGRAM 11956 agrees).
- CONFIRM evidence: A-441-q435-t10p203 verdict CONFIRM
  all, 70/70 = 14+12+9+35 (file present, counts
  verified: shape 14/14 + quad/ring 12/12 + counters
  9/9 + verdict 35/35; == GATE), A-273 corroborates
  all 3 legs incl consts 77/71/63/65 + NO D dips
  (== GATE), no DISSENT (CONVERT-01 rule b). GATE's
  A-441 cites (PBA VPOS b4+M6, PBB10 10-diverge 10/10,
  QUAD VPOS 21, b42 rule 64/64, R6 double-pair 2/4
  distinct, tails 4/4 13/16B, M-tails ALL NEW 0/16,
  TRANSPOSED 13th + TAILS-SWAPPED 4th, ring-Q ==
  quad-M row0 16/16, lencode 92/92, edges, flips
  {87424,87552,87680} all in for-list, DET26 26/26)
  all verbatim in file. No FLAG/CLAIM/GATE conflict
  on b311 (FLAG-* are unrelated holds). QNUM-06
  (16:02) postdates GATE (14:53); w2b Q-block only,
  no gate impact (read at verify time).
- GATE prose CORRECT throughout (build, counts,
  for-list, tables incl B42 + absent + _N, sigs,
  edges, T-mirrors, insert, blank accounting,
  coarse renumber counts, A-441/A-273 recon). No slips.

Agrees with GATE-bf0ee03b (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r35/
(*311* files).

Verdict: PASS. Ready for parent PV + merge.
