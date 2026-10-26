# GATE 74f7ebed b351 T10P243 pins 101301..101648 (348 pins) PASS-functional

Seat sweep-r49, first-hand, WT tmp/wt-encode-sweep @74f7ebed,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r49.
Band = 979dc293 (py merge w2b@2ad35b95 partial, +6 tiers
+62 pins) + 74f7ebed (C port). Base 20efeb92 (b350 tip,
1440 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build351/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r49), rgramc 0fdc075e.
- RGRAMC-PYID 7091/7091 covered=7091/7091 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 14182/14182 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py).
- RGRAM C 14182/14182 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (14182/14182, version-sorted).
- PINS-RGRAM names set-eq 14182/14182 (cmp-equal both ways).
  PINS cells 7091 vs for-list 7091: exact match both ways
  (cells-for {} + for-cells {}, tail 101648 pinned AND in
  for-list).
- PINS 14184 rows (2 hdr + 14182, +62 vs base 14122). py diff
  +62/-0 rows = +31/-0 cells (pure P243 addition);
  test_rgram.sh for-line tracked 1/1 (fast battery parses sh
  for-line; 2x7091 names).
  For-list union 7060->7091 +31/-0: 2 sing (101301 101302) +
  A 5 (head 101303 + 101304 + 101310 + 101314 + tail
  101318) +
  B 5 (head 101319 + 101320 + 101323 + 101324 + tail
  101328; off 2,3,6,7,8 unsampled) + Q 13 (head 101329 +
  101336 + 101344/101345 + 101352 + 101360/101361 + 101368
  + carry pair 101375/101376 + 101377 + 101384 + tail
  101392) + R 6 (head 101393 + edge pairs 101503/101504 +
  101631/101632 + tail 101648).
  PINS adds = same 31 tier pins.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P243 C-vs-py, 15-table A/B10/QUADms+T88 layout,
  all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 4b620100 / 3d31c602);
  AM 16/16 (6B), BM 10/10 (11B), M 16/16 (10B),
  M42 16/16 (1B), X42 4/4 (1B), QR 4/4 (6B), QT 4/4 (4B),
  RM 16/16 (8B), RQ 16/16 (11B) EXACT;
  AC 76/76, BC 71/71, QC 61/61, RC 67/67 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/71/61/67 match actual;
  TABAUDIT-GREEN rc=0 (57 PASS 0 FAIL). No CM/CC (B10
  replaces C10), no M19/XA19 (no b19 leg), no PT/FM (no
  PAIR/FRAG), table inventory exactly the 15.
  Missing-sets first-hand EXACT: AC-8 [36,37,76,77,78,79]
  = b4,b5+M6 (b36,37,76-79);
  BC-13 [36,37,38,39,40,41,42,80,81,82,83] = b4,b5+M11
  (b36-42,80-83, b42 IN M-range first);
  QC-23 [14,15,23,34,35,36,37,38,39,40,41,42,43,76,77,
  78,79,80,81,82,83] = b4,b5+M10 (b14,15,23,34,35,43,
  76-79)+b42+R6 (b36-41)+T4 (b80-83);
  RC-21 [18,19,27,38,39,46,47,52,53,54,55,76,77,78,79,
  80,81,82,83] = VPOS 21 over 0..87 (b4,b5+TM8 b52-55,
  80-83 + TR11 b18,19,27,38,39,46,47,76-79).
  b0-3 first-hand: AC 0080773c (PBA ==P242Q sig); BC
  3d31c602 (==PB1 sig); QC 0080773c (==PBA sig); RC
  02000000 (==P242T sig).
  Code AC76/BC71/QC61/RC67; incl = +1/+1/+0/+0
  (A/B b5 const 17, Q b5-carry, T counter) = 77/72/61/67;
  lane consts 77/72/61/67 = A-573/A-313 INCL EXACT
  (writer dual-accounts PBA/B10 = memo-1, quad+T88
  identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/B/Q/R): P2430 n==101301 / P2431 n==101302
  singleton-const (offs 0/1);
  P243A 101303..101318 off=n-101303 PBA16
  (m-tab 6B b36,37,76-79, sig 0080773c ==P242Q,
  b5 const 17);
  P243B 101319..101328 off=n-101319 B10 single-sig
  (m-tab 11B b36-42,80-83 b42-IN, sig 3d31c602 ==PB1,
  b5 const 17);
  P243Q 101329..101392 off=n-101329 m=off&15 q=off>>4
  QUADms single-sig 0080773c (M 10B b14,15,23,34,35,43,
  76-79 + b42 row-xor X=[00,0c,0c,0c] XOR-staged ADD-tie
  + R6 6B b36-41 TRIPLE + QT b80-83, b5-carry 17->18
  @101375->101376 ff->01 edge);
  P243R(T88-ring) 101393..101648 off=n-101393 c=off&15
  r=off>>4 STANDARD sig 02000000 (TM 8B b52-55,80-83
  by COL + TR 11B b18,19,27,38,39,46,47,76-79 by ROW
  SPLIT tails, b84-87 const cd/ea/d4/5d);
  A/B/Q paylen 84 + raw lencode l16=((n<<1)|1)&0xFFFF
  pay4=l16&0xFF pay5=l16>>8; R paylen 88 + counter
  b4=(0x23+2off)&FF b5=0x18+(off>=111)+(off>=239).
  C blocks carry T66711/66716/66721/66736/66752/66778
  py-line mirrors (exact); guards
  `if ((n) == (101301))` / `if ((n) == (101302))` + 4 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; counter
  35/24+(off>=111)+(off>=239); temps _t5162.._t5181
  appended (base max _t5161, no reuse);
  C byte-index lists match py per block (A 6B, B 11B,
  Q 10/6/4B, R 8/11B); insert position exact (dispatch
  tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct; BM 10/10
  diverge; M 16/16 distinct;
  M42 4-valued 06/46/86/c6 = 3/5/5/3 EXACT;
  X42 [00,0c,0c,0c] (b42-family XOR staged, ADD tie
  noted in code comment);
  QR TRIPLE r1==r2==r3 (36db363b3135 x3; r0 ed596928b1d5
  distinct);
  QT 4/4 distinct exact (8469e6f6/5d42faad/928403ae/
  bc8403ae; r2/r3 share last 3B 8403ae TRUE-3B);
  RQ==M shared-slice (b76-79 same-index) 16/16;
  tails SPLIT (RM indexed by COL c=off&15, RQ by ROW
  r=off>>4, RM/RQ 16/16 distinct);
  M-tails 16/16 ALL NEW vs P242T, RM 16/16 NEW vs
  P242RM, QT 4/4 NEW vs P242QT.
  S0 sig 4b620100 ==P242S0 first-hand (REPEAT); S1
  3d31c602 vs P242S1 6197c402 (NEW); PBA/Q sig
  0080773c ==P242QC sig; T sig 02000000 ==P242RC sig.
  Counter/lencode edges computed first-hand (never trusted
  from comments): A head 6f/17 (101303) tail 8d/17
  (101318), b5set {17}; B head 8f/17 (101319) mid 97/17
  (101323) tail a1/17 (101328), b5set {17};
  Q head a3/17 (101329) mid e1/17 (101360) carry
  ff/17->01/18 @101375->101376 tail 21/18 (101392),
  b5set {17,18}.
  T head 23/18 (101393) + off110/111 (101503->101504)
  ff/18->01/19 + off238/239 (101631->101632) ff/19->01/1a
  + tail 21/1a (101648). All edge pins in for-list + PASS
  (batteries GREEN); 101648 tail pinned + in for-list +
  PASS. Odd-lencode 348/348 first-hand.
  Matches A-573/A-313 geometry (mixed-size 92x84B+256x88B,
  PB0 4b620100 ==P242PB0, PB1 3d31c602 NEW, PBA16
  0080773c ==P242Q VPOS 7 b5 const 17, B10 single-sig
  3d31c602 VPOS 12 b42-IN b5 const 17 10/10 diverge,
  QUADms single-sig 0080773c VPOS 23 b5-carry 17->18 +
  QM10 shared + b42 XOR-tie M42 06/46/86/c6 3+5+5+3 +
  R6 TRIPLE + tails 4/4 TRUE-3B + M-tails ALL NEW 16/16,
  T88-ring STANDARD sig 02000000 TM8 by COL + TR11 by ROW
  UNPAIRED 16/16 + SPLIT tails + b84-87 const cdead45d +
  RM-tails ALL NEW 16/16, ring edges + thresholds 111/239,
  NO D dips).
- C diff pure-add: numstat 640/0 rgramc.c + 262/0 rgram.py
  (+1/-1 for-line, +62/0 PINS); raw C 640 add / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip, trailing-';'
  strip, python sets) del-subset-add 0 missing (del-uniq 0,
  add-uniq 182).
- Wall on band diff added lines (scope 20efeb92..74f7ebed,
  965 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 640/0,
  rgram.py 262/0, test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks, tier-comments
  `# T10P` 1346->1352 +6, singletons `if n == ` 518->520
  +2, range-guards `<= n <=` 424->428 +4, CLOSED prints
  1863->1869 +6: all agree (stated literal methods,
  first-hand). py lines del 0 add 262.
- CONFIRM evidence (CONVERT-01 rule b): A-573-q635
  T10P243 predictive reproduces 34/34 (shape 15/15 +
  quad+Tring 11/11 + counters 8/8 CONFIRM, cut SAFE)
  + A-313-q307 corroborates same tier (3/3 legs CONFIRM,
  consts 77/72/61/67 INCL). No DISSENT on P243. Agrees
  with cport commit msg (py/C 14182, PYID 7091).
- Quiz: no conflicting CLAIM/GATE/FLAG on b351/74f7ebed.
  b350/b352 EVEN = sweep2 turf, used b350 tip as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-11
  (w2f Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r49/ (*351* files:
  build351.log, pyid351.log, rgram351py/c-full.log,
  pass351py/c.txt, pins350base.csv, for351-old/-new.nums,
  pins351.py, sh350.sh, smoke351.log, tables351.log,
  tabaudit351.py, edges351.py, cdiff351.txt/-add-norm/
  -del-norm, banddiff351.txt, added351.txt, numstat351.txt,
  rgram350.py, rgramc350.c).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
