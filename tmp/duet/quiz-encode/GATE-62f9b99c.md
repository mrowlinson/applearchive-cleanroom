# GATE 62f9b99c b395 T10P287 pins 116613..116960 (348 pins) PASS-functional

Seat sweep-r60, first-hand, WT tmp/wt-encode-sweep @62f9b99c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r60.
Band = 191490f1 (py merge w2b@05f163cf partial, +6 tiers
+62 pins) + 62f9b99c (C port). Base c28c6aa1 (b394 tip,
1704 tiers sealed).

- Build: make -C src/c BUILDDIR=r60/build395 aae rgramc
  (flags -O2 -Wall -Wextra -std=c11 per Makefile), rc=0,
  0 warnings (log = make/cc command echoes only),
  build395/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r60,
  sha256 matches b354-b395 pinned value; band touches no
  aae sources), rgramc sha1 b3aba7fc / sha256 745936b2.
- RGRAMC-PYID 8468/8468 covered=8468/8468 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 16936/16936 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 16936/16936 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (16936/16936, sorted).
- PINS-RGRAM cells set-eq 8468/8468 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 16938 rows (2 hdr + 16936, +62 vs base 16876).
  For-list union 8437->8468 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (116613 116614) +
  A 6 (head 116615 + 116616 + 116622 + 116623 +
  116629 + tail 116630; offs 0,1,7,8,14,15) +
  C 6 (head 116631 + 116632 + 116635 + 116636 +
  116639 + tail 116640; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 116633, 116634, 116637,
  116638) +
  Q 10 (head 116641 + off7 116648 + off15/16 pair
  116656/116657 + off24 116665 + off32 116673 +
  off40 116681 + off48 116689 + off55 116696 +
  tail 116704; offs 0,7,15/16,24,32,40,48,55,63;
  b5 const, NO step) +
  R 7 (head 116705 + edge pair 116735/116736 + mid
  116833 + edge pair 116863/116864 + tail 116960;
  offs 0,30/31,128,158/159,255).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines; 31x2 = 62 = 16936-16874.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P287 C-vs-py, 12-table A-PBA88-PLAIN/
  C10-1SIG/QUAD88-4R+T88-STANDARD layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 85620b00 / 4c0ac516 NEW, both NEW strings;
  diff vs P286S0/S1 32/84 @ b0-2,4,5,30-43,48,
  56-59,76-83 + 75/84 @ all but b20,21,32,33,
  52-55,63);
  AM 16/16 (10B), CM 10/10 (11B), M 16/16 (9B),
  QR 4/4 (11B), RM 16/16 (8B), RQ 16/16 (8B)
  EXACT;
  AC 76/76, CC 71/71, QC 66/66, RC 70/70 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/71/66/70 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit395.py 98 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42/H42/L42 (no b42), no QB/PT/FM,
  no RT/TT (STANDARD ring, not ROWTAIL), no QT
  (R11 carries b84-87 inside QR); table inventory
  exactly the 12.
  Missing-sets first-hand EXACT: AC-12 [4,5,8,13,
  14,15,16,17,80,81,82,83] = b4,b5+M10 (b8,
  13-17,80-83);
  CC-13 [4,5,13,14,15,16,17,18,19,80,81,82,83]
  = b4,b5+M11 (b13-19,80-83);
  QC-22 [4,5,8,9,10,11,16,17,18,19,20,21,22,23,
  80,81,82,83,84,85,86,87] = b4,b5+QM9 (b16-19,
  23,80-83)+R11 (b8-11,20-22,84-87);
  RC-18 [4,5,20,21,22,23,28,29,30,31,76,77,78,
  79,80,81,82,83] = b4,b5+TR8 (b20-23,76-79)+
  TM8 (b28-31,80-83).
  PLAIN first-hand: AC b0..b3 = 01,00,00,00 ->
  sig 01000000 x16; AM 16/16 distinct.
  1SIG first-hand: CC b0..b3 = 86,14,8a,2d const
  -> 86148a2d x10; CM 10/10 diverge (rows span 3
  distinct 4B heads 01bcf1bb/2c7c107b/d6bc70fb).
  Code AC76/CC71/QC66/RC70; incl = +1/+1/+1/+0
  (A/C/Q b5 const 8f, T counter) = 77/72/67/70;
  lane consts = A-713/A-351 INCL EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2870 n==116613 / P2871
  n==116614 singleton-const (offs 0/1);
  P287A 116615..116630 off=n-116615 PBA88-PLAIN
  (m-tab 10B b8,13-17,80-83, sig 01000000, b0
  const 01, b5 const 8f);
  P287C 116631..116640 off=n-116631 C10-1SIG
  (m-tab 11B b13-19,80-83, full sig b0-3 in
  consts, b5 const 8f);
  P287Q 116641..116704 off=n-116641 m=off&15
  q=off>>4 QUAD88-4R single-sig 02000000 x64 NEW
  (M 9B b16-19,23,80-83 NO frags + R11 b8-11,
  20-22,84-87 r0 19318ff00a8d07849bb33d distinct
  + r123 share 7B prefix d9171fcdeadc53, tails
  b84-87 4 distinct 849bb33d/d4685f45/f9685f45/
  ac8d4aa8, r1r2 TRUE 3B 685f45,
  b5 const 8f NO step NO edge);
  P287R(T88-ring) 116705..116960 off=n-116705
  c=off&15 r=off>>4 STANDARD sig 2d000000 (TM 8B
  b28-31,80-83 by COL + TR 8B b20-23,76-79 by
  ROW SPLIT tails UNPAIRED, b84-87 const
  1a/50/9e/70);
  A paylen 88 / C paylen 84 / Q paylen 88 + raw
  lencode l16=((n<<1)|1) &0xFFFF pay4=l16&0xFF
  pay5=l16>>8 (b5-consts emerge from raw lencode);
  R paylen 88 +
  counter b4=(0xc3+2off)&FF b5=0x8f+(off>=31)+
  (off>=159).
  C blocks carry T78050/78055/78060/78076/78092/
  78113 py-line mirrors (exact); guards
  `if ((n) == (116613))` / `if ((n) == (116614))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 195+2*off + 143+(off>=31)+
  (off>=159); temps _t6012.._t6027 appended (base
  max _t6011, no reuse); _i max 3642->3652 (band
  3644,3646,3649,3652), _b max 3641->3651 (band
  3643,3645,3647,3648,3650,3651), no reuse;
  C byte-index lists match py per block (A 10B,
  C 11B, Q 9B/11B, R 8/8B); insert
  position exact (dispatch tail, N out-of-scope
  follows; C has 2 scope hits, rfind-used; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0
  19318ff00a8d07849bb33d; r123
  d9171fcdeadc53d4685f45/
  d9171fcdeadc53f9685f45/
  d9171fcdeadc53ac8d4aa8);
  QR all-pairs lcsuf (1,2)=3, (1,3)=(2,3)=0,
  r0-vs-rest 0; r1r2 TRUE 3B 685f45;
  RQ==M HEAD3+SHIFT (M 9B vs RQ 8B: RQ[1:4]==
  M[1:4] 16/16 + RQ[4:8]==M[5:9] 16/16, agree
  matrix clean head3+shifted-tail block at
  (1,1),(2,2),(3,3),(4,5),(5,6),(6,7),(7,8),
  RQ0 own (max agree 1/16, 16-distinct);
  incidental off-diag (2,0)=3 (5,4)=2) -- NEW
  degree (P279 HEAD1+SHIFT differs: 1 head byte;
  P283 HEAD0+SHIFT differs: byte0 aligned);
  15th odd-band RQ==M instance;
  tails STANDARD-SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P286T RQ row-led tails
  (overlap 0); RM-tails ALL NEW vs P286T tails
  (overlap 0); RQ-tails ALL NEW vs P286T tails
  (overlap 0);
  S0 NEW string (32/84 differ @ b0-2,4,5,30-43,
  48,56-59,76-83) + S1 NEW string (75/84 differ,
  all but b20,21,32,33,52-55,63);
  P286S0 sig 1df80a00 == A-709/A-349 predicted
  next PB0; P286S1/PBA88/C10 cd23fd15/01000000/
  cd236d10 == predicted EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 0f/8f (116615)
  tail 2d/8f (116630), b5set {8f}; C head 2f/8f
  (116631) tail 41/8f (116640), b5set {8f};
  Q head 43/8f (116641) tail c1/8f (116704),
  b5set {8f} NO step NO edge;
  quad formula == raw-lencode 64/64 mismatches 0.
  T head c3/8f (116705) + off30/31 (116735->
  116736) ff/8f->01/90 + mid off128 c3/90
  (116833) + off158/159 (116863->116864)
  ff/90->01/91 + tail off255 c1/91 (116960).
  All edge pins in for-list + PASS (batteries
  GREEN); 116960 tail pinned + in for-list +
  PASS (direct first-hand: oracle sha
  0ee07be62583cf05... matches PINS, py+C CLOSED
  T10P287R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (0b/8f, 0d/8f) match raw
  lencode.
  Matches A-713/A-351 geometry (12x84B+336x88B,
  PB0 85620b00 NEW + PB1 4c0ac516 NEW, PBA88-PLAIN
  VPOS 11 b5 const 8f NO pair, C10-1SIG VPOS 12
  b5 const 8f 10/10 diverge, QUAD88-4R VPOS 21
  QM9+R11 NO frags + R11 4/4 UNPAIRED + tails
  b84-87 4 distinct r1r2 3B + M-tails ALL NEW
  16/16, T88-ring STANDARD sig 2d000000 TM8 by
  COL + TR8 by ROW UNPAIRED 16/16 + SPLIT tails
  + b84-87 const 1a509e70, quad b5-const NO step
  + ring edges + thresholds 31/159, NO D dips).
- C diff pure-add: numstat 604/0 rgramc.c + 230/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 599
  content + 5 blank-only `+` lines / 0 del; raw py
  230 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 165, py del-uniq
  0 add-uniq 187). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope c28c6aa1..
  62f9b99c, 897 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 604/0, rgram.py 230/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1610->1616 +6, singletons
  `if n == ` 606->608 +2, range-guards `<= n <=`
  600->604 +4, CLOSED T10P prints 1610->1616 +6,
  seal 1704->1710
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 601->603 +2,
  range 600->604 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b393 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-713-q799
  memo CONFIRM 37/37 (section heads shape 14/14 +
  quad+T-ring 12/12 + counters 11/11 quoted
  verbatim; tier cut SAFE; w2b-r23 4/8 LAST-IN-BLOCK)
  + A-351-q351 viewer corroborates same tier (all
  legs CONFIRM, consts 77/72/67/70 INCL).
  No DISSENT on P287. Agrees with cport commit msg
  (py/C 16936, PYID 8468).
- Quiz: no conflicting CLAIM/GATE/FLAG on b395/
  62f9b99c. b394 EVEN = sweep2 turf, used b394 tip
  as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-19 (w2d Q-block
  only, read, no gate impact); PROSE-01 re-read
  before filing.
- Logs: NVME ws tmp/encode-sweep/r60/ (build395.log,
  pyid395.log, rgram395py/c.log, pass395py/c.txt,
  for394-old.nums/for395-new.nums, seteq395.py/log,
  smoke395.log, tables395.log,
  tabaudit395.py, edges395.py, edges395.log,
  cdiff395.txt, pydiff395.txt, banddiff395.txt,
  added395.txt, numstat395.txt, build395/ binaries,
  tail-116960.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
