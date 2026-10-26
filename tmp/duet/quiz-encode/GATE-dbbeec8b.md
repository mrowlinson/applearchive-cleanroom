# GATE dbbeec8b b353 T10P245 pins 101997..102344 (348 pins) PASS-functional

Seat sweep-r49, first-hand, WT tmp/wt-encode-sweep @dbbeec8b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r49.
Band = db592df5 (py merge w2b@35028def partial, +6 tiers
+62 pins) + dbbeec8b (C port). Base 1ff87cd1 (b352 tip,
1452 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build353/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r49), rgramc 974d4072.
- RGRAMC-PYID 7153/7153 covered=7153/7153 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 14306/14306 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py).
- RGRAM C 14306/14306 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (14306/14306, version-sorted).
- PINS-RGRAM names set-eq 14306/14306 (cmp-equal both ways).
  PINS cells 7153 vs for-list 7153: exact match both ways
  (cells-for {} + for-cells {}, tail 102344 pinned AND in
  for-list).
- PINS 14308 rows (2 hdr + 14306, +62 vs base 14246). py diff
  +62/-0 rows = +31/-0 cells (pure P245 addition);
  test_rgram.sh for-line tracked 1/1 (fast battery parses sh
  for-line; 2x7153 names).
  For-list union 7122->7153 +31/-0: 2 sing (101997 101998) +
  A 6 (head 101999 + 102000 + 102006 + 102010 + 102013 +
  tail 102014) +
  C 6 (head 102015 carry-edge + 102016 + 102017 + 102018 +
  102021 + tail 102024; off 4,5,7,8 unsampled) + Q 10 (head
  102025 + 102033 + 102041 + 102049 + 102057 + 102065 +
  102073 + 102081 + 102087 + tail 102088) + R 7 (head
  102089 + edge pairs 102143/102144 + 102271/102272 + mid
  102217 + tail 102344).
  PINS adds = same 31 tier pins.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P245 C-vs-py, 13-table A/C10/QUADms+T88 layout,
  all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs d46f0100 / b553d702, both NEW);
  AM 16/16 (6B), CM 10/10 (17B), M 16/16 (8B),
  QR 4/4 (7B), QT 4/4 (4B), RM 16/16 (7B), RQ 16/16 (8B)
  EXACT;
  AC 76/76, CC 65/65, QC 63/63, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/65/63/71 match actual;
  TABAUDIT-GREEN rc=0 (53 PASS 0 FAIL). No BM/BC (C10
  replaces B10), no M42/X42 (b42 const 0x95 via consts,
  NO b42 leg), no M19/XA19 (no b19 leg), no PT/FM (no
  PAIR/FRAG), table inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-8 [24,25,76,77,78,79]
  = b4,b5+M6 (b24,25,76-79);
  CC-19 [2,3,21,22,23,24,25,26,27,28,29,30,31,80,81,82,
  83] = b4,b5+M17 (b2,3,21-31,80-83, sig bytes in tab);
  QC-21 [21,22,23,24,25,26,27,28,29,30,31,76,77,78,79,
  80,81,82,83] = b4,b5+M8 (b21,22,23,31,76-79)+R7
  (b24-30)+T4 (b80-83);
  RC-17 [25,26,27,35,40,41,42,76,77,78,79,80,81,82,83]
  = VPOS 17 over 0..87 (b4,b5+TM7 b40-42,76-79 +
  TR8 b25-27,35,80-83).
  b0-3 first-hand: AC 2085c72e (PBA NEW); CC
  0:7d 1:38 2:TAB 3:TAB (2-sig 7d38+tab); QC 2085c72e
  (==PBA sig); RC 02000000 (==P244T sig).
  Code AC76/CC65/QC63/RC71; incl = +1/+0/+1/+0
  (A/Q b5 const 1c/1d, C b5-carry, T counter) =
  77/65/64/71; lane consts 77/65/64/71 = A-580/A-315
  INCL EXACT (writer dual-accounts PBA/quad = memo-1,
  C10+T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2450 n==101997 / P2451 n==101998
  singleton-const (offs 0/1);
  P245A 101999..102014 off=n-101999 PBA16
  (m-tab 6B b24,25,76-79, sig 2085c72e NEW,
  b5 const 1c);
  P245C 102015..102024 off=n-102015 C10 2-sig 3+7
  (m-tab 17B b2,3,21-31,80-83, sig bytes in tab,
  sigs 7d38be05 x3 + 7d38de02 x7,
  b5-carry 1c->1d @102015->102016 INSIDE block);
  P245Q 102025..102088 off=n-102025 m=off&15 q=off>>4
  QUADms single-sig 2085c72e (M 8B b21,22,23,31,76-79
  + R7 7B b24-30 TRIPLE + QT b80-83 + b42 const 0x95,
  b5 const 1d);
  P245R(T88-ring) 102089..102344 off=n-102089 c=off&15
  r=off>>4 STANDARD sig 02000000 (TM 7B b40-42,76-79
  by COL + TR 8B b25-27,35,80-83 by ROW SPLIT tails,
  b84-87 const b1/96/ff/e1);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)&0xFFFF
  pay4=l16&0xFF pay5=l16>>8; R paylen 88 + counter
  b4=(0x93+2off)&FF b5=0x1d+(off>=55)+(off>=183).
  C blocks carry T67356/67361/67366/67381/67398/67421
  py-line mirrors (exact); guards
  `if ((n) == (101997))` / `if ((n) == (101998))` + 4 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; counter
  147/29+(off>=55)+(off>=183); temps _t5210.._t5227
  appended (base max _t5209, no reuse);
  C byte-index lists match py per block (A 6B, C 17B,
  Q 8/7/4B, R 7/8B); insert position exact (dispatch
  tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct; CM 10/10
  diverge, 2-sig map order EXACT (7d38be05 x3 @102015-17
  + 7d38de02 x7 @102018-24, b2b3 be05x3 + de02x7);
  M 16/16 distinct;
  QR TRIPLE r1==r2==r3 (ba7c80a31478a7 x3; r0
  933cc422d4f27c distinct);
  QT 4/4 distinct exact (c26f98d7/78214c1b/a2214c1b/
  cc214c1b; r1/r2/r3 share last 3B 214c1b);
  RQ==M string-equal 16/16 (same staged values;
  positions differ: QM8 b21,22,23,31,76-79 vs TR8
  b25-27,35,80-83, no shared bytes);
  tails SPLIT (RM indexed by COL c=off&15, RQ by ROW
  r=off>>4, RM/RQ 16/16 distinct);
  M-tails 16/16 ALL NEW vs P244T, RM 16/16 NEW vs
  P244RM, QT 4/4 NEW vs P244QT.
  S0/S1 NEW (P244 S0/S1 44620100/3d319602); PBA/Q sig
  2085c72e NEW; T sig 02000000 ==P244RC sig.
  Counter/lencode edges computed first-hand (never trusted
  from comments): A head df/1c (101999) tail fd/1c
  (102014), b5set {1c}; C head ff/1c (102015) carry
  ff/1c->01/1d @102015->102016 INSIDE tail 11/1d (102024),
  b5set {1c,1d};
  Q head 13/1d (102025) mid 53/1d (102057) tail 91/1d
  (102088), b5set {1d}.
  T head 93/1d (102089) + off54/55 (102143->102144)
  ff/1d->01/1e + off182/183 (102271->102272) ff/1e->01/1f
  + tail 91/1f (102344). All edge pins in for-list + PASS
  (batteries GREEN); 102344 tail pinned + in for-list +
  PASS. Odd-lencode 348/348 first-hand.
  Matches A-580/A-315 geometry (mixed-size 92x84B+256x88B,
  PB0 d46f0100 NEW + PB1 b553d702 NEW, PBA16 2085c72e
  NEW VPOS 7 b5 const 1c, C10-2SIG be05x3/de02x7 VPOS 19
  b5-carry INSIDE 10/10 diverge, QUADms single-sig
  2085c72e VPOS 20 b5 const 1d + QM8 shared + b42 const
  0x95 + R7 TRIPLE + tails 4/4 r1/r2/r3-3B + M-tails ALL
  NEW 16/16, T88-ring STANDARD sig 02000000 TM7 by COL
  (b42 in T-M) + TR8 by ROW UNPAIRED 16/16 + SPLIT tails
  + b84-87 const b196ffe1 + RM-tails ALL NEW 16/16, ring
  edges + thresholds 55/183, NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 237/0 rgram.py
  (+1/-1 for-line, +62/0 PINS); raw C 610 add / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip, trailing-';'
  strip, python sets) del-subset-add 0 missing (del-uniq 0,
  add-uniq 158).
- Wall on band diff added lines (scope 1ff87cd1..dbbeec8b,
  910 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 610/0,
  rgram.py 237/0, test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks, tier-comments
  `# T10P` 1358->1364 +6, singletons `if n == ` 522->524
  +2, range-guards `<= n <=` 432->436 +4, CLOSED prints
  1358->1364 +6: all agree (stated literal methods,
  first-hand). py lines del 0 add 237.
- CONFIRM evidence (CONVERT-01 rule b): A-580-q637
  T10P245 predictive reproduces 34/34 (shape 12/12 +
  quad+Tring 13/13 + counters 9/9 CONFIRM, cut SAFE)
  + A-315-q309 corroborates same tier (3/3 legs CONFIRM,
  consts 77/65/64/71 INCL). No DISSENT on P245. Agrees
  with cport commit msg (py/C 14306, PYID 7153).
- Quiz: no conflicting CLAIM/GATE/FLAG on b353/dbbeec8b.
  b352/b354 EVEN = sweep2 turf, used b352 tip as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-11
  (w2f Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r49/ (*353* files:
  build353.log, pyid353.log, rgram353py/c-full.log,
  pass353py/c.txt, pins352base.csv, for353-old/-new.nums,
  pins353.py, sh352.sh, smoke353.log, tables353.log,
  tabaudit353.py, edges353.py, cdiff353.txt/-add-norm/
  -del-norm, banddiff353.txt, added353.txt, numstat353.txt,
  rgram352.py, rgramc352.c).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
