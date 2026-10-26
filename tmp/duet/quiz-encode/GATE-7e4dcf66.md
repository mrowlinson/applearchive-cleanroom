# GATE 7e4dcf66 b397 T10P289 pins 117309..117656 (348 pins) PASS-functional

Seat sweep-r61, first-hand, WT tmp/wt-encode-sweep @7e4dcf66,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r61.
Band = 3acd872b (py merge w2b@84f82ebd partial, +6 tiers
+64 pins) + 7e4dcf66 (C port). Base b68cdf88 (b396 tip,
1716 tiers sealed).

- Build: make -C src/c BUILDDIR=r61/build397 aae rgramc
  (flags -O2 -Wall -Wextra -std=c11 per Makefile), rc=0,
  0 warnings (log = make/cc command echoes only),
  build397/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r61,
  sha256 matches b354-b397 pinned value; band touches no
  aae sources), rgramc sha1 90364d74 / sha256 45357ab3.
- RGRAMC-PYID 8531/8531 covered=8531/8531 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 17062/17062 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 17062/17062 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (17062/17062, sorted).
- PINS-RGRAM cells set-eq 8531/8531 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 17064 rows (2 hdr + 17062, +64 vs base 17000).
  For-list union 8499->8531 +32/-0 (python sets,
  trailing-';' stripped, never comm).
  32 = 2 sing (117309 117310) +
  A 6 (head 117311 + 117312 + 117318 + 117319 +
  117325 + tail 117326; offs 0,1,7,8,14,15) +
  C 6 (head 117327 + 117328 + 117333 + 117334 +
  117335 + tail 117336; offs 0,1,6,7,8,9; offs
  2,3,4,5 unsampled: 117329, 117330, 117331,
  117332) +
  Q 10 (head 117337 + off15/16 pair 117352/117353 +
  off24 117361 + off32 117369 + off38/39 pair
  117375/117376 + off48 117385 + off55 117392 +
  tail 117400; offs 0,15/16,24,32,38/39,48,55,63;
  b5 step edge o38->39) +
  R 8 (head 117401 + colsplit pair 117409/117410 +
  edge pair 117503/117504 + edge pair 117631/117632
  + tail 117656; offs 0,8/9,102/103,230/231,255).
  PINS adds = same 32 tier pins. Each for-N yields 2 PASS
  lines; 32x2 = 64 = 17062-16998.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P289 C-vs-py, 12-table A-PBA88-PLAIN/
  C10-2SIG/QUAD88-4R+T88-2SIG layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 0fc51600 / 3bf3f420 NEW, both NEW strings;
  diff vs P288S0/S1 32/84 @ b0,4,5,18-29,32-37,
  52-55,72,74-79 + 50/84 @ b2-5,22-55,72-83);
  AM 16/16 (7B), CM 10/10 (12B), M 16/16 (6B),
  QR 4/4 (10B), RM 16/16 (9B), RQ 16/16 (6B)
  EXACT;
  AC 79/79, CC 70/70, QC 70/70, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 79/70/70/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit397.py 79 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42/H42/L42 (no b42), no QB/PT/FM,
  no RT/TT (ring, not ROWTAIL), no QT
  (R10 carries b84-87 inside QR); table inventory
  exactly the 12.
  Missing-sets first-hand EXACT: AC-9 [4,5,52,53,
  54,80,81,82,83] = b4,b5+M7 (b52-54,80-83);
  CC-14 [3,4,5,35,46,47,48,49,50,51,80,81,82,
  83] = b4,b5+M12 (b3,35,46-51,80-83);
  QC-18 [4,5,6,7,11,50,51,53,54,55,80,81,82,
  83,84,85,86,87] = b4,b5+QM6 (b6,7,80-83)+
  R10 (b11,50,51,53-55,84-87);
  RC-17 [0,4,5,6,7,9,10,11,20,76,77,78,79,
  80,81,82,83] = b4,b5+TR6 (b6,7,76-79)+
  TM9 (b0,9-11,20,80-83).
  PLAIN first-hand: AC b0..b3 = 02,00,00,00 ->
  sig 02000000 x16; AM 16/16 distinct.
  2SIG first-hand: CC b0..b2 = 3b,f3,f4 const +
  CM b3 = 20 rows0-6 / 1a rows7-9 -> 3bf3f420 x7
  + 3bf3f41a x3 ORDERED; CM 10/10 diverge.
  Code AC79/CC70/QC70/RC71; incl = +1/+1/+0/+0
  (A/C b5 const 94, Q b5-step, T counter) =
  80/71/70/71; lane consts = A-728/A-353 INCL
  EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2890 n==117309 / P2891
  n==117310 singleton-const (offs 0/1);
  P289A 117311..117326 off=n-117311 PBA88-PLAIN
  (m-tab 7B b52-54,80-83, sig 02000000, b0
  const 02, b5 const 94);
  P289C 117327..117336 off=n-117327 C10-2SIG
  (m-tab 12B b3,35,46-51,80-83, partial sig b3
  in tab, b5 const 94);
  P289Q 117337..117400 off=n-117337 m=off&15
  q=off>>4 QUAD88-4R single-sig 01000000 x64
  (M 6B b6,7,80-83 NO frags + R10 b11,50,51,
  53-55,84-87 r0 bbb12ce5 distinct + r123 share
  6B prefix c7d82676e7fa, tails b84-87 4 distinct
  05a90c59/42ec79b3/86ec79b3/bbed79b3, r1r2 TRUE
  3B ec79b3, b52-skipped const d1,
  b5 0x94+(o>=39) step edge o38->39);
  P289R(T88-2SIG) 117401..117656 off=n-117401
  c=off&15 r=off>>4 COL-SPLIT b0=1f iff c<9 else
  1d 144+112 (TM 9B b0,9-11,20,80-83 by COL +
  TR 6B b6,7,76-79 by ROW SPLIT tails UNPAIRED,
  b84-87 const 85/36/00/0f);
  A paylen 88 / C paylen 84 / Q paylen 88 + raw
  lencode l16=((n<<1)|1) &0xFFFF pay4=l16&0xFF
  pay5=l16>>8 (b5-consts/step emerge from raw
  lencode);
  R paylen 88 +
  counter b4=(0x33+2off)&FF b5=0x95+(off>=103)+
  (off>=231).
  C blocks carry T78513/78518/78523/78538/78554/
  78575 py-line mirrors (exact); guards
  `if ((n) == (117309))` / `if ((n) == (117310))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 51+2*off + 149+(off>=103)+
  (off>=231); colsplit (c<9)?31:29; temps
  _t6044.._t6059 appended (base max _t6043, no
  reuse); _i max 3662->3672 (band 3664,3666,
  3669,3672), _b max 3661->3671 (band 3663,
  3665,3667,3668,3670,3671), no reuse;
  C byte-index lists match py per block (A 7B,
  C 12B, Q 6B/10B, R 9/6B); insert
  position exact (dispatch tail, N out-of-scope
  follows; C has 2 scope hits; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0
  bbb12ce5...05a90c59; r123
  c7d82676e7fa...42ec79b3/
  c7d82676e7fa...86ec79b3/
  c7d82676e7fa...bbed79b3);
  QR all-pairs lcsuf (1,2)=3, (1,3)=(2,3)=2,
  r0-vs-rest 0; r1r2 TRUE 3B ec79b3; r3 shares
  2B 79b3;
  RQ==M FULL (RQ table == M table byte-identical
  16/16 rows; agree matrix perfect diagonal
  16/16 x6, incidental off-diag (2,5)=(5,2)=1)
  -- NEW degree (all prior odd bands partial:
  TAILS/HEAD3+SHIFT/HEAD1+SHIFT/HEAD0+SHIFT);
  16th odd-band RQ==M instance;
  tails COL-SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P288T RM col-led tails
  (overlap 0); RM-tails ALL NEW vs P288T RM tails
  (overlap 0); RQ-tails ALL NEW vs P288T tails
  (overlap 0 vs RM and RQ);
  S0 NEW string (32/84 differ @ b0,4,5,18-29,
  32-37,52-55,72,74-79) + S1 NEW string (50/84
  differ @ b2-5,22-55,72-83);
  P289 actuals (S0 0fc51600/S1 3bf3f420/PBA88
  02000000/C10-2SIG 7+3 ORDERED) == A-727/A-352
  predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 7f/94 (117311)
  tail 9d/94 (117326), b5set {94}; C head 9f/94
  (117327) tail b1/94 (117336), b5set {94};
  Q head b3/94 (117337) tail 31/95 (117400),
  edge o38->39 (117375->117376) ff/94->01/95;
  quad formula == raw-lencode 64/64 mismatches 0.
  T head 33/95 (117401) + off102/103 (117503->
  117504) ff/95->01/96 + mid off128 33/96
  (117529) + off230/231 (117631->117632)
  ff/96->01/97 + tail off255 31/97 (117656).
  All edge pins in for-list + PASS (batteries
  GREEN); 117656 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  8bcb4fd24d00a120... matches PINS, py+C CLOSED
  T10P289R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand; colsplit
  144+112 first-hand.
  S0/S1 embedded b4/b5 (7b/94, 7d/94) match raw
  lencode.
  Matches A-728/A-353 geometry (12x84B+336x88B,
  PB0 0fc51600 NEW + PB1 3bf3f420 NEW, PBA88-PLAIN
  VPOS 8 b5 const 94 NO pair, C10-2SIG VPOS 13
  b5 const 94 10/10 diverge, QUAD88-4R VPOS 18
  QM6+R10 NO frags + R10 4/4 UNPAIRED + tails
  b84-87 4 distinct r1r2 3B + M-tails ALL NEW
  16/16, T88-2SIG col-split 144+112 TM9 by
  COL + TR6 by ROW UNPAIRED 16/16 + SPLIT tails
  + b84-87 const 8536000f, quad b5-step + edge
  o38->39 + ring edges + thresholds 103/231, NO
  D dips).
- C diff pure-add: numstat 607/0 rgramc.c + 233/0
  rgram.py (+1/-1 for-line, +64/0 PINS); raw C 602
  content + 5 blank-only `+` lines / 0 del; raw py
  233 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 147, py del-uniq
  0 add-uniq 175). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope b68cdf88..
  7e4dcf66, 905 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 607/0, rgram.py 233/0,
  test_rgram.sh 1/1, PINS 64/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1622->1628 +6, singletons
  `if n == ` 610->612 +2, range-guards `<= n <=`
  608->612 +4, CLOSED T10P prints 1622->1628 +6,
  seal 1716->1722
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 605->607 +2,
  range 608->612 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b395 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-728-q881
  memo CONFIRM 37/37 (section heads shape 14/14 +
  quad+T-ring 11/11 + counters 12/12 quoted
  verbatim; tier cut SAFE; w2b-r23 6/8 backfill)
  + A-353-q353 viewer corroborates same tier (all
  legs CONFIRM, consts 80/71/70/71 INCL).
  No DISSENT on P289. Agrees with cport commit msg
  (py/C 17062, PYID 8531).
- Quiz: no conflicting CLAIM/GATE/FLAG on b397/
  7e4dcf66. b396 EVEN = sweep2 turf, used b396 tip
  as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-19 (w2d Q-block
  only, read, no gate impact); PROSE-01 re-read
  before filing.
- Logs: NVME ws tmp/encode-sweep/r61/ (build397.log,
  pyid397.log, rgram397py/c.log, pass397py/c.txt,
  seteq397.py/log, smoke397.log, tables397.log,
  tabaudit397.py, edges397.py, edges397.log,
  cdiff397.txt, pydiff397.txt, banddiff397.txt,
  added397.txt, numstat397.txt, diffwall397.py/log,
  build397/ binaries,
  tail-117656.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
