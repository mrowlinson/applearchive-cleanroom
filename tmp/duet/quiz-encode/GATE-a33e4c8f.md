# GATE a33e4c8f b385 T10P277 pins 113133..113480 (348 pins) PASS-functional

Seat sweep-r58, first-hand, WT tmp/wt-encode-sweep @a33e4c8f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r58.
Band = 9f1aa46d (py merge w2b@e2008f5b partial, +6 tiers
+60 pins) + a33e4c8f (C port). Base db0378aa (b384 tip,
1644 tiers sealed).

- Build: make -C src/c BUILDDIR=r58/build385 aae rgramc
  (flags -O2 -Wall -Wextra -std=c11 per Makefile), rc=0,
  0 warnings (log = make/cc command echoes only),
  build385/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r58,
  sha256 matches b354-b385 pinned value; band touches no
  aae sources), rgramc sha1 3befc1e6 / sha256 3552fba3.
- RGRAMC-PYID 8153/8153 covered=8153/8153 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 16306/16306 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 16306/16306 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (16306/16306, sorted).
- PINS-RGRAM cells set-eq 8153/8153 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 16308 rows (2 hdr + 16306, +60 vs base 16248).
  For-list union 8123->8153 +30/-0 (python sets,
  trailing-';' stripped, never comm).
  30 = 2 sing (113133 113134) +
  A 6 (head 113135 + 113136 + 113140 + 113145 +
  113149 + tail 113150; offs 0,1,5,10,14,15) +
  C 6 (head 113151 + 113152 + 113154 + 113156 +
  113158 + tail 113160; offs 0,1,3,5,7,9; offs
  2,4,6,8 unsampled: 113153, 113155, 113157,
  113159) +
  Q 8 (head 113161 + mid pair 113176/113177 +
  mid pair 113192/113193 + mid pair 113208/113209
  + tail 113224; offs 0,15/16,31/32,47/48,63;
  b5 const, no step) +
  R 8 (head 113225 + edge pair 113279/113280 +
  mid 113327 + edge pair 113407/113408 + off230
  113455 + tail 113480; offs 0,54/55,102,
  182/183,230,255).
  PINS adds = same 30 tier pins. Each for-N yields 2 PASS
  lines; 30x2 = 60 = 16306-16246.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P277 C-vs-py, 14-table A-PBA-PLAIN/
  C10-CARRY/QUAD1s+T88-ROWTAIL layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs b6aa0700 / d505540f NEW, both NEW strings;
  diff vs P276S0/S1 30/84 @ b1,4-11,42-48,50,51,
  56-67 + 59/84);
  AM 16/16 (8B), CM 10/10 (12B), M 16/16 (8B),
  QR 4/4 (7B), QT 4/4 (4B), RM 16/16 (8B),
  RQ 16/16 (3B), RT 16/16 (4B)
  EXACT;
  AC 74/74, CC 70/70, QC 63/63, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 74/70/63/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit385.py 96 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42 (no b42 staging), no QB/PT/FM;
  table inventory exactly the 14. RT present =
  ROWTAIL TT tab (code names memo-TT "RT").
  Missing-sets first-hand EXACT: AC-10 [4,5,24,
  25,26,27,76,77,78,79] = b4,b5+M8 (b24-27,
  76-79);
  CC-14 [4,5,24,25,26,27,28,29,30,31,80,81,
  82,83] = b4,b5+M12 (b24-31,80-83);
  QC-21 [4,5,21,22,23,24,25,26,27,28,29,30,
  31,76,77,78,79,80,81,82,83] = b4,b5+QM8
  (b21-23,31,76-79)+R7 (b24-30)+T4
  (b80-83);
  RC-17 [4,5,29,34,35,40,41,42,43,76,77,
  78,79,80,81,82,83] = b4,b5+TR3 (b29,34,
  35)+TM8 (b40-43,76-79)+TT4 (b80-83).
  PLAIN first-hand: AC b0 const e0 -> sig
  e09a1ffa; AM 16/16 distinct.
  CARRY first-hand: CM rows 0-5 share 8B head
  3fbcb44875f06ba6 + distinct 4B tails
  (45f14707/65f14707/05004807/25004807/
  a5516907/c5516907), rows 6-9 all-distinct;
  CC b0..b3 = f5,f4,57,0f -> sig f5f4570f;
  CM 10/10 diverge; first-cell carry o=0->1
  (edge 113151->113152 ff/73->01/74).
  Code AC74/CC70/QC63/RC71; incl = +1/+0/+1/+0
  (A b5 const 73, C b5-step, Q b5 const 74,
  T counter) = 75/70/64/71;
  lane consts = A-682/A-341 INCL EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2770 n==113133 / P2771
  n==113134 singleton-const (offs 0/1);
  P277A 113135..113150 off=n-113135 PBA-PLAIN
  (m-tab 8B b24-27,76-79, sig e09a1ffa, b0
  const e0, b5 const 73);
  P277C 113151..113160 off=n-113151 C10-CARRY
  (m-tab 12B b24-31,80-83, b5 73+step1);
  P277Q 113161..113224 off=n-113161 m=off&15
  q=off>>4 QUAD1s single-sig e09a1ffa (M 8B
  b21-23,31,76-79 NO frags + R7 b24-30
  r1==r2==r3 LAST3-PAIRED cb3c329115c98d x3
  + QT b80-83 0b6db88f/b3dff5e9/246311ea/
  8a1ff0ea no shared suffix >=2B, b5 const
  74);
  P277R(T88-ROWTAIL) 113225..113480 off=n-113225
  c=off&15 r=off>>4 sig 08000000 (TM 8B
  b40-43,76-79 by COL + TR 3B b29,34,35 by
  ROW PAIRED 14/16 r6==r7 fe4de6 + r14==r15
  ff6d87 tails disambiguate + TT 4B b80-83
  ROW-led by r, b84-87 const 27/83/81/1e);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (b5-consts
  + carry edge emerge from raw lencode);
  R paylen 88 + counter b4=(0x93+2off)&FF
  b5=0x74+(off>=55)+(off>=183).
  C blocks carry T75656/75661/75666/75681/
  75697/75720 py-line mirrors (exact); guards
  `if ((n) == (113133))` / `if ((n) == (113134))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 147+2*off + 116+(off>=55)+
  (off>=183);
  temps _t5830.._t5849 appended (base max _t5829,
  no reuse); _i max 3533->3545 (band 3535,3537,
  3541,3545), _b max 3532->3544 (band 3534,3536,
  3538,3539,3540,3542,3543,3544), no reuse;
  C byte-index lists match py per block (A 8B,
  C 12B, Q 8/7/4B, R 8/3/4B); insert position exact
  (dispatch tail, N out-of-scope follows; C has 2
  scope hits, rfind-used).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (CARRY rows, all distinct);
  M 16/16 distinct; QR r1==r2==r3 LAST3-PAIRED
  exact (cb3c329115c98d x3; r0 acbca4ea955e68
  distinct); 2 distinct;
  QT 4/4 distinct exact (0b6db88f/b3dff5e9/
  246311ea/8a1ff0ea); all-pairs shared suffix
  max 1B, only r2/r3 (last-2B b88f/f5e9/11ea/
  f0ea all distinct);
  RQ 14/16 PAIRED exact (r6==r7 fe4de6 +
  r14==r15 ff6d87, tails disambiguate);
  RM 16/16 distinct; RT 16/16 distinct;
  RT==M-tails 16/16 + set-eq (ROWTAIL degree:
  RT[r] == M[m] bytes 4-7 same-index; RQ 3B
  has no M containment) -- third rowtail T88
  instance (P269 family note carried);
  tails ROW-led by r 16/16 (staged _T10P277TT
  by r; code names the tab RT);
  M-tails 16/16 ALL NEW vs P276T row-0
  reference (overlap 0); M-full also ALL NEW
  vs P276RQ; QT 4/4 ALL NEW vs P276QT
  (overlap 0); RM ALL NEW vs P276RM.
  S0/S1 both NEW strings (30/84 + 59/84 differ
  vs P276; P276S0 sig b6690700 == A-671/A-339
  predicted next PB0; P276S1/PBA/C10
  0d2b660e/ddb062e6/386c550f == predicted
  EXACT; P277 S0/S1/PBA/C10 b6aa0700/
  d505540f/e09a1ffa/f5f4570f == A-676
  predicted EXACT).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head df/73 (113135)
  tail fd/73 (113150), b5set {73}; C head ff/73
  (113151) tail 11/74 (113160), b5set {73,74}
  first-cell carry; Q head 13/74 (113161) tail
  91/74 (113224), b5set {74} NO step, NO ff
  edge (b4 range 0x13..0x91).
  T head 93/74 (113225) + off54/55
  (113279->113280) ff/74->01/75 + off182/183
  (113407->113408) ff/75->01/76 + mid off102
  5f/75 (113327) + off230 5f/76 (113455) +
  tail off255 91/76 (113480).
  All edge pins in for-list + PASS (batteries
  GREEN); 113480 tail pinned + in for-list +
  PASS (direct first-hand: oracle sha
  fdaa0c42882cb62c... matches PINS, py+C CLOSED
  T10P277R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (db/73, dd/73) match raw
  lencode.
  Matches A-682/A-341 geometry (mixed-size 92x84B+
  256x88B, PB0 b6aa0700 NEW + PB1 d505540f NEW,
  PBA16-PLAIN VPOS 9 b5 const 73 NO pair,
  C10-CARRY VPOS 14 b5 73+step1 first-cell carry
  10/10 diverge, QUAD1s VPOS 20 QM8+R7+T4 NO
  frags + R7 r1==r2==r3 LAST3-PAIRED + tails no
  shared suffix >=2B + M-tails ALL NEW 16/16,
  T88-ROWTAIL sig 08000000 TM8 by COL + TR3 by
  ROW PAIRED 14/16 + TT4 ROW-led + b84-87 const
  2783811e, quad const + ring edges + thresholds
  55/183, NO D dips).
- C diff pure-add: numstat 636/0 rgramc.c + 257/0
  rgram.py (+1/-1 for-line, +60/0 PINS); raw C 631
  content + 5 blank-only `+` lines / 0 del; raw py
  257 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 184, py del-uniq
  0 add-uniq 208). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope db0378aa..
  a33e4c8f, 954 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 636/0, rgram.py 257/0,
  test_rgram.sh 1/1 (for-line), PINS 60/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1550->1556 +6, singletons
  `if n == ` 586->588 +2, range-guards `<= n <=`
  560->564 +4, CLOSED T10P prints 1550->1556 +6,
  seal 1644->1650
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 581->583 +2,
  range 560->564 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b383 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-682-q789
  memo CONFIRM 39/39 (section heads shape 13/13 +
  quad+T-ring 14/14 + counters 12/12 quoted
  verbatim; tier cut SAFE)
  + A-341-q341 viewer corroborates same tier (all 3
  legs CONFIRM, consts 75/70/64/71 INCL).
  No DISSENT on P277. Agrees with cport commit msg
  (py/C 16306, PYID 8153).
- Quiz: no conflicting CLAIM/GATE/FLAG on b385/
  a33e4c8f. b384 EVEN = sweep2 turf (all evens are),
  used b384 tip as diff-base only, NOT gated. Newest
  PARENT-* is QNUM-18 (w2e/w2f Q-blocks only, read, no
  gate impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r58/ (build385.log,
  pyid385.log, rgram385py/c.log, pass385py/c.txt,
  for384-old.nums/for385-new.nums, seteq385.py/log,
  smoke385.log, tables385.log, tables385-CM.log, tabaudit385.py,
  edges385.log, edges385.py, cdiff385.txt,
  pydiff385.txt, banddiff385.txt, added385.txt,
  build385/ binaries, tail-113480.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
