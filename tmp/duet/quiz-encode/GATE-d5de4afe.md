# GATE d5de4afe b399 T10P291 pins 118005..118352 (348 pins) PASS-functional

Seat sweep-r61, first-hand, WT tmp/wt-encode-sweep @d5de4afe,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r61.
Band = 7c7363ba (py merge w2b@8b76d52e partial, +6 tiers
+62 pins) + d5de4afe (C port). Base b5516b9b (b398 tip,
1728 tiers sealed).

- Build: make -C src/c BUILDDIR=r61/build399 aae rgramc
  (flags -O2 -Wall -Wextra -std=c11 per Makefile), rc=0,
  0 warnings (log = make/cc command echoes only),
  build399/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r61,
  sha256 matches b354-b399 pinned value; band touches no
  aae sources), rgramc sha1 4a8f214c / sha256 e020d475.
- RGRAMC-PYID 8593/8593 covered=8593/8593 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 17186/17186 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 17186/17186 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (17186/17186, sorted).
- PINS-RGRAM cells set-eq 8593/8593 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 17188 rows (2 hdr + 17186, +62 vs base 17126).
  For-list union 8562->8593 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (118005 118006) +
  A 6 (head 118007 + 118008 + 118015 + 118016 +
  118021 + tail 118022; offs 0,1,8,9,14,15; step
  edge o8->9) +
  C 6 (head 118023 + 118024 + 118027 + 118030 +
  118031 + tail 118032; offs 0,1,4,7,8,9; offs
  2,3,5,6 unsampled: 118025, 118026, 118028,
  118029) +
  Q 10 (head 118033 + off8 118041 + off15/16 pair
  118048/118049 + off24 118057 + off32 118065 +
  off40 118073 + off48 118081 + off56 118089 +
  tail 118096; offs 0,8,15/16,24,32,40,48,56,63;
  b5 const, NO step) +
  R 7 (head 118097 + edge pair 118143/118144 + mid
  118225 + edge pair 118271/118272 + tail 118352;
  offs 0,46/47,128,174/175,255).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines; 31x2 = 62 = 17186-17124.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P291 C-vs-py, 14-table A-PBA88-STEP/
  C10-2SIG/QUAD88-2SIG-FRAG+T88-RING layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 5f6f1300 / 2b81c726; S0 sig-eq P290PB0sig
  with 30/84 payload diff NOT byte-equal, S1 NEW
  string 48/84 @ b0-2,4,5,13-39,52-55,68-75,
  80-83);
  AM 16/16 (8B), CM 10/10 (16B), M 16/16 (4B),
  QR 4/4 (12B), F0 16/16 (4B), F1 16/16 (4B),
  RM 16/16 (9B), RQ 16/16 (8B)
  EXACT;
  AC 78/78, CC 66/66, QC 66/66, RC 69/69 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 78/66/66/69 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit399.py 89 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (FRAG is
  F0/F1 rowpair-tabs, not M19), no M42/X42/H42/L42
  (no b42), no QB/PT/FM, no RT/TT (ring, not
  ROWTAIL), no QT (R12 carries b84-87 inside QR);
  table inventory exactly the 14.
  Missing-sets first-hand EXACT: AC-10 [4,5,40,41,
  42,43,80,81,82,83] = b4,b5+M8 (b40-43,80-83);
  CC-18 [2,3,4,5,34,35,36,37,38,39,40,41,42,43,
  80,81,82,83] = b4,b5+M16 (b2,3,34-43,80-83);
  QC-22 [0,4,5,19,38,39,40,41,42,43,44,45,46,
  47,80,81,82,83,84,85,86,87] = b4,b5+QM4
  (b80-83)+R12 (b0,19,40-45,84-87)+FRAG
  (b38,39,46,47);
  RC-19 [4,5,38,39,46,47,50,52,53,54,55,76,77,
  78,79,80,81,82,83] = b4,b5+TR8 (b38,39,46,
  47,76-79)+TM9 (b50,52-55,80-83).
  STEP first-hand: AC b0..b3 = 02,00,00,00 ->
  sig 02000000 x16; AM 16/16 distinct; b5 steps
  o8->9 (edges, below).
  2SIG first-hand: CC b0,b1 = 2b,81 const +
  CM b2,b3 = c7,26 rows0-7 / 67,13 rows8-9 ->
  2b81c726 x8 + 2b816713 x2 ORDERED; CM 10/10
  diverge.
  Code AC78/CC66/QC66/RC69; incl = +0/+1/+1/+0
  (A b5-step, C b5 const 9a, Q b5 const 9a, T
  counter) = 78/67/67/69; lane consts =
  A-730/A-355 INCL EXACT (A-STEP +0 mirrors the
  Q-step +0 rule; Q b5-CONST +1 per rule).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2910 n==118005 / P2911
  n==118006 singleton-const (offs 0/1);
  P291A 118007..118022 off=n-118007 PBA88-STEP
  (m-tab 8B b40-43,80-83, sig 02000000, b0
  const 02, b5 0x99+(o>=9) step o8->9);
  P291C 118023..118032 off=n-118023 C10-2SIG
  (m-tab 16B b2,3,34-43,80-83, partial sig b2,3
  in tab, b5 const 9a);
  P291Q 118033..118096 off=n-118033 m=off&15
  q=off>>4 QUAD88-2SIG-FRAG row-split r0-01/
  r123-02 (M 4B b80-83 NO frags + R12 b0,19,
  40-45,84-87 r0 01175bdd distinct + r1/r2 share
  8B prefix 022f0cdf49ad1296 + r3 022f0ddf,
  tails b84-87 4 distinct 322dd5e9/553f379a/
  7a3f379a/12f6cff1, r1r2 TRUE 3B 3f379a +
  FRAG b38,39,46,47 rowpair-tabs F0(r0)/F1(r123)
  differ 16/16 rows + per-pos 16/16 x4,
  b5 const 9a NO step);
  P291R(T88-ring) 118097..118352 off=n-118097
  c=off&15 r=off>>4 STANDARD sig 23000000 (TM 9B
  b50,52-55,80-83 b51-skipped const dc by COL +
  TR 8B b38,39,46,47,76-79 by ROW SPLIT tails
  UNPAIRED, b84-87 const 15/37/fc/9a);
  A paylen 88 / C paylen 84 / Q paylen 88 + raw
  lencode l16=((n<<1)|1) &0xFFFF pay4=l16&0xFF
  pay5=l16>>8 (b5-step/consts emerge from raw
  lencode);
  R paylen 88 +
  counter b4=(0xa3+2off)&FF b5=0x9a+(off>=47)+
  (off>=175).
  C blocks carry T79009/79014/79019/79034/79051/
  79076 py-line mirrors (exact); guards
  `if ((n) == (118005))` / `if ((n) == (118006))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 163+2*off + 154+(off>=47)+
  (off>=175); ftab if (q)==(0) F0 else F1;
  temps _t6076.._t6094 appended (base max _t6075,
  no reuse); _i max 3682->3693 (band 3684,3686,
  3690,3693), _b max 3681->3692 (band 3683,
  3685,3687,3688,3689,3691,3692), no reuse;
  C byte-index lists match py per block (A 8B,
  C 16B, Q 4B/12B/4B, R 9/8B); insert
  position exact (dispatch tail, N out-of-scope
  follows; C has 2 scope hits; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0
  01175bdd...322dd5e9; r123
  022f0cdf49ad1296...553f379a/
  022f0cdf49ad1296...7a3f379a/
  022f0ddf...12f6cff1);
  QR all-pairs lcsuf (1,2)=3, all other pairs 0
  (r0+r3 lcs=0); r1r2 TRUE 3B 3f379a; r1r2
  lcpre 8B 022f0cdf49ad1296 (memo A-730/A-355
  quote 6B 022f0cdf49ad; first-hand 8B is the
  fuller value);
  RQ==M TAILS (M 4B b80-83 vs RQ 8B: RQ[4:8]==
  M[0:4] 16/16, head 4x4 agree noise <=1 with
  incidental (3,3)=1) -- TAILS degree (joins
  P255/P263/P267/P285 group);
  17th odd-band RQ==M instance;
  tails STANDARD-SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P290T RM col-led tails
  (overlap 0); RM-tails ALL NEW vs P290T RM tails
  (overlap 0); RQ-tails ALL NEW vs P290T tails
  (overlap 0 vs RM and RQ);
  S0 sig-eq string (30/84 differ @ b4-10,13-15,
  17,18,20-25,64-75: memo A-730's figure EXACT,
  viewer A-355's byte-equal claim REFUTED) + S1
  NEW string (48/84 differ @ b0-2,4,5,13-39,
  52-55,68-75,80-83);
  P291 actuals (S0 5f6f1300 30-diff/S1 2b81c726/
  PBA88-STEP 02000000/C10-2SIG 8+2 ORDERED) ==
  A-729 predicted next EXACT (incl its NOT-
  byte-equal call); A-354 window resolved
  except its PB0 byte-equal line, refuted
  first-hand 30/84.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head ef/99 (118007)
  edge o8->9 (118015->118016) ff/99->01/9a tail
  0d/9a (118022); C head 0f/9a (118023) tail
  21/9a (118032), b5set {9a};
  Q head 23/9a (118033) tail a1/9a (118096),
  b5set {9a} NO step; quad b4=(0x23+2off) 64/64.
  T head a3/9a (118097) + off46/47 (118143->
  118144) ff/9a->01/9b + mid off128 a3/9b
  (118225) + off174/175 (118271->118272)
  ff/9b->01/9c + tail off255 a1/9c (118352).
  All edge pins in for-list + PASS (batteries
  GREEN); 118352 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  5d5480eb5ca05125... matches PINS, py+C CLOSED
  T10P291R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (eb/99, ed/99) match raw
  lencode.
  Matches A-730/A-355 geometry (12x84B+336x88B,
  PB0 5f6f1300 sig-eq + PB1 2b81c726 NEW,
  PBA88-STEP VPOS 10 b5-step o8->9, C10-2SIG
  VPOS 17 b5 const 9a 10/10 diverge,
  QUAD88-2SIG-FRAG VPOS 21 QM4+R12+F4 +
  R12 4/4 UNPAIRED + tails b84-87 4 distinct
  r1r2 3B + FRAG split 16/16 + M-tails ALL NEW
  16/16, T88-RING STANDARD sig 23000000 TM9 by
  COL + TR8 by ROW UNPAIRED 16/16 + SPLIT tails
  + b84-87 const 1537fc9a + b51-skipped dc,
  ring edges + thresholds 47/175, NO D dips).
- C diff pure-add: numstat 656/0 rgramc.c + 269/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 651
  content + 5 blank-only `+` lines / 0 del; raw py
  269 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 185, py del-uniq
  0 add-uniq 200). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope b5516b9b..
  d5de4afe, 988 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 656/0, rgram.py 269/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1634->1640 +6, singletons
  `if n == ` 614->616 +2, range-guards `<= n <=`
  616->620 +4, CLOSED T10P prints 1634->1640 +6,
  seal 1728->1734
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 609->611 +2,
  range 616->620 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b397 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-730-q883
  memo CONFIRM 44/44 (section heads shape 15/15 +
  quad+T-ring 15/15 + counters 14/14 quoted
  verbatim; tier cut SAFE; w2b-r23 8/8 CAP,
  backfill 4/4 COMPLETE)
  + A-355-q355 viewer corroborates same tier (all
  legs CONFIRM, consts 78/67/67/69 INCL) with ONE
  resolved dispute: viewer PB0 byte-equal line
  REFUTED first-hand (30/84 diff; memo A-730's
  figure + NOT-byte-equal call vindicated).
  No DISSENT on tier cut. Agrees with cport commit
  msg (py/C 17186, PYID 8593).
- Quiz: no conflicting CLAIM/GATE/FLAG on b399/
  d5de4afe. b398 EVEN = sweep2 turf, used b398 tip
  as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-20 (w2f Q-block
  only, read, no gate impact); PROSE-01 re-read
  before filing.
- Logs: NVME ws tmp/encode-sweep/r61/ (build399.log,
  pyid399.log, rgram399py/c.log, pass399py/c.txt,
  seteq399.py/log, smoke399.log, tables399.log,
  tabaudit399.py, edges399.py, edges399.log,
  cdiff399.txt, pydiff399.txt, banddiff399.txt,
  added399.txt, numstat399.txt, diffwall399.py/log,
  build399/ binaries,
  tail-118352.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
