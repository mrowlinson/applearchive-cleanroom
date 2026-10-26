# GATE d525fb04 b403 T10P295 pins 119397..119744 (348 pins) PASS-functional

Seat sweep-r62, first-hand, WT tmp/wt-encode-sweep @d525fb04,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r62.
Band = 28d94b61 (py merge w2b@54679d02 partial, +6 tiers
+62 pins) + d525fb04 (C port). Base 84585207 (b402 tip,
1752 tiers sealed).

- Build: make -C src/c BUILDDIR=r62/build403 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build403/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r62, sha256 matches b354-b403
  pinned value; band touches no aae sources), rgramc
  sha1 5dfa3ebc / sha256 63639da3.
- RGRAMC-PYID 8717/8717 covered=8717/8717 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 17434/17434 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 17434/17434 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (17434/17434, sorted).
- PINS-RGRAM cells set-eq 8717/8717 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 17436 rows (2 hdr + 17434, +62 vs base 17374).
  For-list union 8686->8717 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (119397 119398) +
  A 6 (head 119399 + 119400 + 119406 + 119407 +
  119413 + tail 119414; offs 0,1,7,8,14,15) +
  C 6 (head 119415 + 119416 + 119419 + 119420 +
  119423 + tail 119424; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 119417, 119418, 119421,
  119422) +
  Q 10 (head 119425 + off7 119432 + off15/16 pair
  119440/119441 + off24 119449 + off32 119457 +
  off40 119465 + off48 119473 + off55 119480 +
  tail 119488; offs 0,7,15/16,24,32,40,48,55,63;
  b5 const, NO step) +
  R 7 (head 119489 + edge pair 119551/119552 + mid
  119617 + edge pair 119679/119680 + tail 119744;
  offs 0,62/63,128,190/191,255).
  PINS adds = same 31 tier pins (2 rows each; base
  all 2x). Each for-N yields 2 PASS lines; 31x2 = 62
  = 17434-17372.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P295 C-vs-py, 13-table A-PBA88-PLAIN/
  C10-STEP/QUAD88-4R-FRAG+T88-RING layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 63501000 / f2c7a020 NEW, both NEW strings;
  diff vs P294S0/S1 30/84 @ b0,1,4,5,30-32,34-43,
  48,56-59,76-83 + 75/84 @ b0-2,4,5,7-19,21-31,
  34-51,56-83);
  AM 16/16 (7B), CM 10/10 (11B), M 16/16 (8B),
  QR 4/4 (11B), F 16/16 rows (1B, uniq 11),
  RM 16/16 (6B), RQ 16/16 (8B)
  EXACT;
  AC 79/79, CC 71/71, QC 66/66, RC 72/72 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 79/71/66/72 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit403.py 94 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (FRAG is
  single-F coltab+ADD1, not M19), no M42/X42/H42/
  L42 (no b42), no QB/PT/FM, no RT/TT (ring, not
  ROWTAIL), no QT (R11 carries b84-87 inside QR),
  no F0/F1 (single F tab); table inventory exactly
  the 13.
  Missing-sets first-hand EXACT: AC-9 [4,5,13,14,
  15,80,81,82,83] = b4,b5+M7 (b13-15,80-83);
  CC-13 [4,5,13,14,15,16,17,18,19,80,81,82,
  83] = b4,b5+M11 (b13-19,80-83);
  QC-22 [4,5,8,9,10,11,16,17,18,19,20,21,22,
  23,80,81,82,83,84,85,86,87] = b4,b5+QM8
  (b16-19,80-83)+R11 (b8-11,20-22,84-87)+F1
  (b23);
  RC-16 [4,5,20,21,22,23,28,29,76,77,78,79,
  80,81,82,83] = b4,b5+TR8 (b20-23,76-79)+
  TM6 (b28,29,80-83).
  PLAIN first-hand: AC b0..b3 = 02,00,00,00 ->
  sig 02000000 x16; AM 16/16 distinct.
  STEP first-hand: CC b0..b3 = 86,c7,a0,20 const
  -> 86c7a020 x10 SINGLE-sig; CM 10/10 diverge;
  b5 steps o8->9 (edges, below).
  Code AC79/CC71/QC66/RC72; incl = +1/+0/+1/+0
  (A b5 const a4, C b5-step, Q b5 const a5, T
  counter) = 80/71/67/72; lane consts =
  A-748/A-359 INCL EXACT (C-STEP +0 extends the
  A-STEP/Q-step +0 rule).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2950 n==119397 / P2951
  n==119398 singleton-const (offs 0/1);
  P295A 119399..119414 off=n-119399 PBA88-PLAIN
  (m-tab 7B b13-15,80-83, sig 02000000, b0
  const 02, b5 const a4);
  P295C 119415..119424 off=n-119415 C10-STEP
  (m-tab 11B b13-19,80-83, full sig b0-3 in CC,
  b5 0xa4+(o>=9) step o8->9);
  P295Q 119425..119488 off=n-119425 m=off&15
  q=off>>4 QUAD88-4R-FRAG 1-sig 02000000 x64
  (M 8B b16-19,80-83 NO frags + R11 b8-11,20-22,
  84-87 r0 d9183f31 distinct + r123 share 7B
  prefix 99365f3c05131e, tails b84-87 4 distinct
  84414a84/99a274c5/acc979c5/d1c979c5, r2r3 TRUE
  3B c979c5, r1 lcs=1, r0 lcs=0 + FRAG b23 coltab
  F + ADD1 r123==r0+1 mod256, b5 const a5 NO
  step);
  P295R(T88-ring) 119489..119744 off=n-119489
  c=off&15 r=off>>4 STANDARD sig 20000000 (TM 6B
  b28,29,80-83 by COL + TR 8B b20-23,76-79 by
  ROW SPLIT tails UNPAIRED 16/16, b84-87 const
  21/e7/42/40);
  A paylen 88 / C paylen 84 / Q paylen 88 + raw
  lencode l16=((n<<1)|1) &0xFFFF pay4=l16&0xFF
  pay5=l16>>8 (b5-consts/step emerge from raw
  lencode);
  R paylen 88 +
  counter b4=(0x83+2off)&FF b5=0xa5+(off>=63)+
  (off>=191).
  C blocks carry T79951/79956/79961/79976/79992/
  80018 py-line mirrors (exact); guards
  `if ((n) == (119397))` / `if ((n) == (119398))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 131+2*off + 165+(off>=63)+
  (off>=191); ftab if (q)==(0) F else fadd1
  (hexval+1)&255; temps _t6143.._t6160 appended
  (base max _t6142, no reuse); _i max
  3723->3733 (band 3725,3727,3730,3733), _b max
  3722->3732 (band 3724,3726,3728,3729,3731,
  3732), no reuse; C byte-index lists match py
  per block (A 7B, C 11B, Q 8B/11B/1B, R 6/8B);
  insert position exact (dispatch tail, N
  out-of-scope follows; C has 2 scope hits; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0
  d9183f31...84414a84; r123
  99365f3c05131e...99a274c5/
  99365f3c05131e...acc979c5/
  99365f3c05131e...d1c979c5);
  QR all-pairs lcsuf (2,3)=3, (1,2)=(1,3)=1,
  r0-vs-rest 0; r2r3 TRUE 3B c979c5; r1 lcs=1;
  r123 lcpre 7B 99365f3c05131e;
  RQ==M SUFFIX7 (RQ[1:8]==M[1:8] 16/16 on 8B/8B
  widths, byte0 differs 16/16; agree matrix
  diagonal 16/16 x7 bytes 1-7, RQ0 row all 0,
  incidentals (1,0)=(3,5)=(5,3)=(5,7)=(7,5)=1;
  same-pos RM[2:6]==M[4:8] 0/16) -- SUFFIX7
  degree NEW (tab-index 7B-suffix equality);
  19th odd-band RQ==M instance;
  tails STANDARD-SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P294T RQ row-led tails
  (overlap 0); RM-tails (b80-83) ALL NEW vs P294T
  RQ tails (overlap 0); RQ-tails (b76-79) ALL NEW
  vs P294T RM tails (overlap 0); cross overlaps 0;
  F coltab 16 rows uniq 11
  (03,0b,1b,33,4b,73,a3,b3,d3,e3,f3); ftab/fadd1
  both sides (q==0 F[m] else F[m]+1 mod 256);
  S0 NEW string (30/84 differ @ b0,1,4,5,30-32,
  34-43,48,56-59,76-83) + S1 NEW string (75/84
  differ @ b0-2,4,5,7-19,21-31,34-51,56-83);
  P295 actuals (S0 63501000/S1 f2c7a020/PBA88
  02000000/C10-STEP 1-sig + b5 step o8->9) ==
  A-741/A-358 predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head cf/a4 (119399)
  tail ed/a4 (119414), b5set {a4}; C head ef/a4
  (119415) edge o8->9 (119423->119424)
  ff/a4->01/a5;
  Q head 03/a5 (119425) tail 81/a5 (119488),
  b5set {a5} NO step; quad b4=(0x03+2off) 64/64;
  quad formula == raw-lencode 64/64 mismatches 0.
  T head 83/a5 (119489) + off62/63 (119551->
  119552) ff/a5->01/a6 + mid off128 83/a6
  (119617) + off190/191 (119679->119680)
  ff/a6->01/a7 + tail off255 81/a7 (119744).
  All edge pins in for-list + PASS (batteries
  GREEN); 119744 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  8f62b763efd890f1... matches PINS rawlen 104,
  py+C CLOSED T10P295R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (cb/a4, cd/a4) match raw
  lencode.
  Matches A-748/A-359 geometry (12x84B+336x88B,
  PB0 63501000 NEW + PB1 f2c7a020 NEW,
  PBA88-PLAIN VPOS 8 b5 const a4 NO pair,
  C10-STEP VPOS 13 b5-step o8->9 10/10 diverge,
  QUAD88-4R-FRAG VPOS 21 QM8+R11+F1 + R11 4/4
  UNPAIRED + tails b84-87 4 distinct r2r3 3B +
  FRAG coltab+ADD1 + M-tails ALL NEW 16/16,
  T88-RING STANDARD sig 20000000 TM6 by COL +
  TR8 by ROW UNPAIRED 16/16 + SPLIT tails +
  b84-87 const 21e74240, ring edges + thresholds
  63/191, NO D dips).
- C diff pure-add: numstat 634/0 rgramc.c + 253/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 629
  content + 5 blank-only `+` lines / 0 del; raw py
  253 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 183, py del-uniq
  0 add-uniq 201). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 84585207..
  d525fb04, 950 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 634/0, rgram.py 253/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1658->1664 +6, singletons
  `if n == ` 622->624 +2, range-guards `<= n <=`
  632->636 +4, CLOSED T10P prints
  1658->1664 +6, seal 1752->1758
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 617->619 +2,
  range 632->636 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b401 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-748-q887
  memo CONFIRM 40/40 (section heads shape 15/15 +
  quad+T-ring 13/13 + counters 12/12 quoted
  verbatim; tier cut SAFE; w2b-r24 4/8)
  + A-359-q359 viewer corroborates same tier (all
  legs CONFIRM, consts 80/71/67/72 INCL).
  No DISSENT on P295. Agrees with cport commit msg
  (py/C 17434, PYID 8717).
- Quiz: no conflicting CLAIM/GATE/FLAG on b403/
  d525fb04. b402 EVEN = sweep2 turf, used b402 tip
  as diff-base only, NOT gated. Adjacent P294
  PB0/PB1 byte-equality dispute (memo A-741 NOT-byte-
  equal 28/84+56/84 vs viewer A-358 byte-equal) is
  sweep2 turf (b402), out of gate scope; P295-window
  predictions from both agree. Newest PARENT-*
  is QNUM-21 (w2b Q-block refill
  only, read, no gate impact); PROSE-01 re-read
  before filing.
- Logs: NVME ws tmp/encode-sweep/r62/ (build403.log,
  pyid403.log, rgram403py/c.log, pass403py/c.txt,
  seteq403.py/log, smoke403.log, tables403.log,
  tabaudit403.py, edges403.py, edges403.log,
  cdiff403.txt, pydiff403.txt, banddiff403.txt,
  added403.txt, numstat403.txt, diffwall403.py/log,
  build403/ binaries,
  tail-119744.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
