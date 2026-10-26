# GATE 26effd6a b363 T10P255 pins 105477..105824 (348 pins) PASS-functional

Seat sweep-r52, first-hand, WT tmp/wt-encode-sweep @26effd6a,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r52.
Band = 2013543b (py merge w2b@a13b79a9 partial, +6 tiers
+62 pins) + 26effd6a (C port). Base ade4c863 (b362 tip,
1512 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build363/{aae,rgramc}, rc=0,
  0 warnings. aae sha1 7d8dd3a2 / sha256 d6e27c97
  (both pinned stable: sha1 r39-r52, sha256 b354-b363),
  rgramc sha1 f97a6560 / sha256 0ebbf0b2.
- RGRAMC-PYID 7463/7463 covered=7463/7463 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 14926/14926 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 14926/14926 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (14926/14926, sorted).
- PINS-RGRAM cells set-eq 7463/7463 (xor 0 all 3 ways:
  for^pass for^pins pass^pins).
  PINS 14928 rows (2 hdr + 14926, +62 vs base 14866).
  For-list union 7432->7463 +31/-0 (python sets, never
  comm).
  31 = 2 sing (105477 105478) +
  A 6 (head 105479 + 105480 + 105485 + 105489 + 105493 +
  tail 105494) +
  C 6 (head 105495 + 105498 + 105499 + 105502 + 105503 +
  tail 105504; offs 1,2,5,6 unsampled: 105496, 105497,
  105500, 105501) +
  Q 10 (head 105505 + 105520 + 105521 + 105536 + 105537 +
  mid 105545 + 105552 + 105553 + 105561 + tail 105568;
  NO carry pair: b5 const) +
  R 7 (head 105569 + edge pair 105599/105600 + mid
  105697 + edge pair 105727/105728 + tail 105824).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 31x2 = 62 = 14926-14864.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P255 C-vs-py, 17-table A-PBA/C10-2SIG/
  QUADms-3sig+T88 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs e4180300 ==P254PB0 REPEAT / 0dc83406 NEW, both
  NEW strings);
  AM 16/16 (7B), CM 10/10 (16B), M 16/16 (4B),
  QB12/QB13/QB14/QB15/QB19 32/32 (1B), QR 4/4 (7B),
  QT 4/4 (4B), RM 16/16 (7B), RQ 16/16 (9B) EXACT;
  AC 75/75, CC 66/66, QC 62/62, RC 70/70 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 75/66/62/70 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit363.py 55 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M42/X42 (no b42 leg),
  no PT/FM (no PAIR/FRAG), table inventory exactly
  the 17.
  Missing-sets first-hand EXACT: AC-9 [4,5,9,10,11,
  76,77,78,79] = b4,b5+M7 (b9-11,76-79);
  CC-18 [0,1,2,3,4,5,11,13,14,15,16,17,18,19,80,
  81,82,83] = b4,b5+M16 (b0-3,11,13-19,80-83;
  b12 const 00 SKIPPED, sig bytes in tab);
  QC-22 [0,1,2,3,4,5,12,13,14,15,16,17,18,19,76,
  77,78,79,80,81,82,83] = b4,b5+QM4 (b76-79)+
  5pair (b12-15,19)+R7 (b0-3,16-18)+T4 (b80-83);
  RC-18 [4,5,16,17,18,19,23,28,29,30,76,77,78,79,
  80,81,82,83] = VPOS 18 over 0..87 (b4,b5+TM7
  b28-30,80-83 + TR9 b16-19,23,76-79).
  b0-3 first-hand: AC b0-3 79824c63 (NEW);
  CM sig heads 26c83406 x4 @rows0-3 + 13641a03 x4
  @rows4-7 + 26c83406 x2 @rows8-9 (full-sig in
  tab);
  QR full-sig rows 009e1f76-r0 / 608fcf66-r1 /
  4089bf36-r2,r3 (3-sig, r2==r3);
  RC 03000000 (==P241T sig, re-read first-hand).
  Code AC75/CC66/QC62/RC70; incl = +1/+1/+1/+0
  (A/C/Q b5 const 38, T counter) = 76/67/63/70;
  lane consts = A-609/A-366 INCL EXACT (writer
  PBA/C10/quad = memo-1, T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2550 n==105477 / P2551
  n==105478 singleton-const (offs 0/1);
  P255A 105479..105494 off=n-105479 PBA16
  (m-tab 7B b9-11,76-79, sig 79824c63 NEW, b5
  const 38);
  P255C 105495..105504 off=n-105495 C10-2SIG
  sandwich (m-tab 16B b0-3,11,13-19,80-83, b12
  skipped, b5 const 38);
  P255Q 105505..105568 off=n-105505 m=off&15
  q=off>>4 3-sig quad (M 4B tails-only b76-79 +
  g=0/16 pair-coltabs QB12/13/14/15/19[g+m] +
  R7 7B full-sig b0-3,16-18 + QT b80-83, b5
  const 38 NO carry);
  P255R(T88-ring) 105569..105824 off=n-105569
  c=off&15 r=off>>4 STANDARD sig 03000000 (TM 7B
  b28-30,80-83 by COL + TR 9B b16-19,23,76-79 by
  ROW SPLIT tails, b84-87 const a3/6f/d7/65);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8; R paylen 88
  + counter b4=(0xc3+2off)&FF b5=0x38+(off>=31)+
  (off>=159).
  C blocks carry T70102/70107/70112/70127/70144/
  70178 py-line mirrors (exact); guards
  `if ((n) == (105477))` / `if ((n) == (105478))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; pair-coltab via snprintf %02lx of pay[12/
  13/14/15/19] vs QB[g+m] (matches py); counter
  195/56 + (off>=31)+(off>=159); temps _t5400..
  _t5427 appended (base max _t5399, no reuse);
  _i max 3290->3301, _b max 3289->3300, no
  reuse; C byte-index lists match py per block
  (A 7B, C 16B, Q 4/1x5/7/4B, R 7/9B); insert
  position exact (dispatch tail, N out-of-scope
  follows).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (sandwich rows, all distinct);
  M 16/16 distinct;
  QB12 16 / QB13 10 / QB14 8 / QB15 6 / QB19 26
  distinct (memo counts EXACT); all 5 group tabs
  differ (r01 vs r23);
  QR r2==r3 PAIRED (4089bf36856b85 x2; r0
  009e1f769e1850 + r1 608fcf66d88719 distinct);
  QT 4/4 distinct exact (b3f8e313/492cce3a/
  feb89ebb/28b99ebb); r2/r3 share last 2B ONLY
  (9ebb; 2nd bytes b8/b9 1B-off) per A-609 SecR
  (writer-staged TBD, ruled 2B);
  RQ==M b76-79 same-index 16/16 (shared-slice,
  P249-style; full-string impossible: RQ 9B vs M
  4B);
  tails SPLIT (RM b80-83 by COL c=off&15, RQ
  b76-79 by ROW r=off>>4, RM/RQ 16/16 distinct,
  0 overlap UNPAIRED; RM-tails + RQ-tails 16/16
  distinct);
  M-tails 16/16 ALL NEW vs P254T
  (P254RQ 9B tails, row-led via TR9);
  QT 4/4 NEW vs P254QT
  (b6a8543e/e95abd76/ef6138db/196238db).
  S0 NEW string (sig e4180300 ==P254PB0 REPEAT);
  S1 NEW (sig 0dc83406 NEW; P254S1 sig 6d4b3306).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 0f/38 (105479)
  tail 2d/38 (105494), b5set {38}; C head 2f/38
  (105495) tail 41/38 (105504), b5set {38}; Q
  head 43/38 (105505) tail c1/38 (105568),
  b5set {38} NO carry.
  T head c3/38 (105569) + off30/31 (105599->
  105600) ff/38->01/39 + off158/159 (105727->
  105728) ff/39->01/3a + mid off128 c3/39
  (105697) + tail off255 c1/3a (105824). All
  edge pins in for-list + PASS (batteries GREEN);
  105824 tail pinned + in for-list + PASS.
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (0b/38, 0d/38) match raw
  lencode.
  Matches A-609/A-366 geometry (mixed-size 92x84B+
  256x88B, PB0 e4180300 ==P254PB0 + PB1 0dc83406
  NEW, PBA16 VPOS 8 b5 const 38 16/16 distinct NO
  pair, C10-2SIG sandwich 4/4/2 VPOS 17 b12
  SKIPPED b5 const 38 10/10 diverge, QUAD 3-sig
  VPOS 21 QM4 tails-only + 5 pair-coltabs + R7
  r2==r3 + tails 4/4 (2B-share per SecR) +
  M-tails ALL NEW 16/16, T88-ring STANDARD sig
  03000000 TM7 by COL + TR9 by ROW UNPAIRED 16/16
  + SPLIT tails + b84-87 const a36fd765, ring
  edges + thresholds 31/159, NO D dips).
- C diff pure-add: numstat 811/0 rgramc.c + 419/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 806
  content + 5 blank-only `+` lines / 0 del; raw py
  419 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 202, py del-uniq
  0 add-uniq 219). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope ade4c863..
  26effd6a, 1293 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 811/0, rgram.py 419/0,
  test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1418->1424 +6, singletons
  `if n == ` 542->544 +2, range-guards `<= n <=`
  472->476 +4, CLOSED prints 1418->1424 +6, seal
  1512->1518 +6: all agree (stated literal methods,
  first-hand). C guards: singleton `if ((n) == (`
  537->539 +2, range 472->476 +4; 5-count C-vs-py
  singleton offset pre-existing (same C-only dip
  guards as b357/b359/b361), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-609-q767
  T10P255 memo CONFIRM 39/39 + SecR (shape 12/12 +
  quad+Tring 13/13 + counters 11/11; SecR rules
  writer-TBD tails 2B-share 9ebb + 1B-off b8/b9,
  tier cut SAFE)
  + A-366-q319 viewer corroborates same tier (3/3
  legs CONFIRM, consts 76/67/63/70 INCL).
  No DISSENT on P255. Agrees with cport commit msg
  (py/C 14926, PYID 7463).
- Quiz: no conflicting CLAIM/GATE/FLAG on b363/
  26effd6a. b362/b364 EVEN = sweep2 turf, used b362
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-12 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r52/ (build363.log,
  pyid363.log, rgram363py/c-full.log, pass363py/c.
  txt, pins362base.csv, for363-old/-new.nums,
  sh362/363.sh, smoke363.log, tables363.log,
  tabaudit363.py, edges363.log, numstat363.txt,
  cdiff363.txt, pydiff363.txt, banddiff363.txt,
  build363/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
