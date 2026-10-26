# GATE 2d5cbe97 b391 T10P283 pins 115221..115568 (348 pins) PASS-functional

Seat sweep-r59, first-hand, WT tmp/wt-encode-sweep @2d5cbe97,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r59.
Band = b67f7800 (py merge w2b@cfefa1d0 partial, +6 tiers
+66 pins) + 2d5cbe97 (C port). Base 256db28a (b390 tip,
1680 tiers sealed).

- Build: make -C src/c BUILDDIR=r59/build391 aae rgramc
  (flags -O2 -Wall -Wextra -std=c11 per Makefile), rc=0,
  0 warnings (log = make/cc command echoes only),
  build391/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r59,
  sha256 matches b354-b391 pinned value; band touches no
  aae sources), rgramc sha1 d7c5de50 / sha256 09d8ce9d.
- RGRAMC-PYID 8344/8344 covered=8344/8344 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 16688/16688 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 16688/16688 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (16688/16688, sorted).
- PINS-RGRAM cells set-eq 8344/8344 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 16690 rows (2 hdr + 16688, +66 vs base 16624).
  For-list union 8311->8344 +33/-0 (python sets,
  trailing-';' stripped, never comm).
  33 = 2 sing (115221 115222) +
  A 6 (head 115223 + 115224 + 115228 + 115233 +
  115237 + tail 115238; offs 0,1,5,10,14,15) +
  C 8 (head 115239 + 115240 + 115243 + 115244 +
  115245 + 115246 + 115247 + tail 115248; offs
  0,1,4,5,6,7,8,9; offs 2,3 unsampled: 115241,
  115242; sig-boundary dense: sig1 head pair +
  sig1 tail pair + full sig2) +
  Q 10 (head 115249 + off7 115256 + edge pair
  115264/115265 + mid pair 115280/115281 + off39
  115288 + mid pair 115296/115297 + tail 115312;
  offs 0,7,15/16,31/32,39,47/48,63; b5 const,
  NO step) +
  R 7 (head 115313 + edge pair 115327/115328 + mid
  115392 + edge pair 115455/115456 + tail 115568;
  offs 0,14/15,79,142/143,255).
  PINS adds = same 33 tier pins. Each for-N yields 2 PASS
  lines; 33x2 = 66 = 16688-16622.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P283 C-vs-py, 15-table A-PBA-PLAIN/
  C10-2SIG/QUAD1s+b42+T88-STANDARD layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 9ef00700 / 4513e30f NEW, both NEW strings;
  diff vs P282S0/S1 30/84 @ b4-7,9-11,13-18,20,
  22-25,64-75 + 48/84 @ b0-2,4,5,11,13,15-39,
  52-55,68-75,80-83);
  AM 16/16 (7B), CM 10/10 (16B), M 16/16 (6B),
  H42 16/16 (nib), L42 4/4 (nib), QR 4/4 (6B),
  QT 4/4 (4B), RM 16/16 (6B), RQ 16/16 (7B)
  EXACT;
  AC 75/75, CC 66/66, QC 65/65, RC 73/73 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 75/66/65/73 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit391.py 106 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42 (b42 staging is H42/L42 nib-tabs),
  no QB/PT/FM, no RT/TT (STANDARD ring, not
  ROWTAIL); table inventory exactly the 15.
  Missing-sets first-hand EXACT: AC-9 [4,5,36,37,
  38,76,77,78,79] = b4,b5+M7 (b36-38,76-79);
  CC-18 [2,3,4,5,34,35,36,37,38,39,40,41,42,
  43,80,81,82,83] = b4,b5+M16 (b2,3,34-43,
  80-83);
  QC-19 [4,5,34,36,37,38,39,40,41,42,43,76,
  77,78,79,80,81,82,83] = b4,b5+QM6 (b34,43,
  76-79)+b42+R6 (b36-41)+T4 (b80-83);
  RC-15 [4,5,38,46,47,52,53,76,77,78,79,80,
  81,82,83] = b4,b5+TR7 (b38,46,47,76-79)+
  TM6 (b52,53,80-83).
  PLAIN first-hand: AC b0..b3 = c0,9b,7f,e2 ->
  sig c09b7fe2 x16; AM 16/16 distinct.
  2SIG first-hand: CC b0,b1 = 45,13 + CM b2,b3
  map ORDERED e30f x6 @115239-44 + f307 x4
  @115245-48 -> 4513e30f x6 + 4513f307 x4;
  CM 10/10 diverge.
  Code AC75/CC66/QC65/RC73; incl = +1/+1/+1/+0
  (A/C/Q b5 const 84, T counter) = 76/67/66/73;
  lane consts = A-699/A-347 INCL EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2830 n==115221 / P2831
  n==115222 singleton-const (offs 0/1);
  P283A 115223..115238 off=n-115223 PBA-PLAIN
  (m-tab 7B b36-38,76-79, sig c09b7fe2, b0 const
  c0, b5 const 84);
  P283C 115239..115248 off=n-115239 C10-2SIG
  (m-tab 16B b2,3,34-43,80-83, partial sig b2,3
  in tab, b5 const 84);
  P283Q 115249..115312 off=n-115249 m=off&15
  q=off>>4 QUAD1s single-sig c09b7f62 x64 (M 6B
  b34,43,76-79 NO frags + b42 NIBSPLIT hi==H42
  [m] coltab / lo==L42[q] rowtab + R6 b36-41
  r1==r2==r3 LAST3-PAIRED 9d592674f113 x3 +
  QT b80-83 1ebc3c63/9a7d1825/bf7d1825/e47d1825
  r123 TRUE 3B 7d1825, b5 const 84 NO step);
  P283R(T88-ring) 115313..115568 off=n-115313
  c=off&15 r=off>>4 STANDARD sig 07000000 (TM 6B
  b52,53,80-83 by COL + TR 7B b38,46,47,76-79
  by ROW SPLIT tails UNPAIRED, b84-87 const
  a8/fd/2c/45);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (b5-consts
  emerge from raw lencode); R paylen 88 +
  counter b4=(0xe3+2off)&FF b5=0x84+(off>=15)+
  (off>=143).
  C blocks carry T77124/77129/77134/77149/
  77166/77193 py-line mirrors (exact); guards
  `if ((n) == (115221))` / `if ((n) == (115222))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 227+2*off + 132+(off>=15)+
  (off>=143); nibble checks via snprintf %lx
  of pay[42]>>4 / pay[42]&15 vs H42[m]/L42[q];
  temps _t5942.._t5963 appended (base max _t5941,
  no reuse); _i max 3601->3612 (band 3603,3605,
  3609,3612), _b max 3600->3611 (band 3602,3604,
  3606,3607,3608,3610,3611), no reuse;
  C byte-index lists match py per block (A 7B,
  C 16B, Q 6B+2nib/6B/4B, R 6/7B); insert
  position exact (dispatch tail, N out-of-scope
  follows; C has 2 scope hits, rfind-used; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (2SIG rows, all distinct);
  M 16/16 distinct; H42 coltab 733f373777bff773
  exact; L42 rowtab [5,9,9,9] exact (r0->5,
  r123->9); QR r1==r2==r3 LAST3-PAIRED exact
  (9d592674f113 x3; r0 285f5f3c51e4 distinct);
  2 distinct;
  QT 4/4 distinct exact (1ebc3c63/9a7d1825/
  bf7d1825/e47d1825); r1/r2/r3 share last 3B
  7d1825; full all-pairs LCS (1,2)=(1,3)=(2,3)
  =3, r0-vs-rest 0;
  b42 3-way tie per A-699 (row-XOR X=[00,0c,0c,
  0c] + row-ADD A=[0,4,4,4] ALSO fit 64/64,
  10th b42-tie family member; memo first-hand
  beds, code implements NIBSPLIT);
  RQ==M HEAD0+SHIFT FIRST (M 6B vs RQ 7B:
  RQ[0]==M[0] 16/16 + RQ[2:7]==M[1:6] 16/16,
  agree matrix clean shift (7x6 diagonal at
  (0,0),(2,1),(3,2),(4,3),(5,4),(6,5)),
  RQ[1] own (max agree 1/16, 4-distinct 3c/7c/
  bc/fc, lo-6 bits const 3c)) -- NEW degree
  (P279 HEAD1+SHIFT differs: byte1 + RQ[2:6]==
  M[3:7] on 6B/7B widths); 13th odd-band RQ==M
  instance;
  tails SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P282T reference
  (overlap 0);
  QT 4/4 ALL NEW vs P282QT (overlap 0);
  RM ALL NEW vs P282RM.
  S0 NEW string (30/84 differ @ b4-7,9-11,13-18,
  20,22-25,64-75) + S1 NEW string (48/84 differ
  @ b0-2,4,5,11,13,15-39,52-55,68-75,80-83);
  P282S0 sig 9ef00700 == A-692/A-345 predicted
  next PB0; P282S1/PBA/C10 cb3de10f/e0857ffe/
  3582e40f-x6+4dffe70f+8d59ea0f+ad85e10f-x2 ==
  predicted EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 2f/84 (115223)
  tail 4d/84 (115238), b5set {84}; C head 4f/84
  (115239) tail 61/84 (115248), b5set {84};
  Q head 63/84 (115249) tail e1/84 (115312),
  b5set {84} NO step NO edge; quad formula ==
  raw-lencode 64/64 mismatches 0.
  T head e3/84 (115313) + off14/15 (115327->
  115328) ff/84->01/85 + mid off79 81/85
  (115392) + off142/143 (115455->115456)
  ff/85->01/86 + tail off255 e1/86 (115568).
  All edge pins in for-list + PASS (batteries
  GREEN); 115568 tail pinned + in for-list +
  PASS (direct first-hand: oracle sha
  996f684d281c44ad... matches PINS, py+C CLOSED
  T10P283R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (2b/84, 2d/84) match raw
  lencode.
  Matches A-699/A-347 geometry (mixed-size 92x84B+
  256x88B, PB0 9ef00700 sigeq-P282PB0 30/84 diff
  + PB1 4513e30f NEW, PBA16-PLAIN VPOS 8 b5 const
  84 NO pair, C10-2SIG VPOS 17 b5 const 84 10/10
  diverge 6+4 map, QUAD1s VPOS 18 QM6+R6+T4 NO
  frags + b42 NIBSPLIT FIRST-in-quad + R6
  r1==r2==r3 LAST3-PAIRED + tails r123 3B 7d1825
  + M-tails ALL NEW 16/16, T88-ring STANDARD sig
  07000000 TM6 by COL + TR7 by ROW UNPAIRED 16/16
  + SPLIT tails + b84-87 const a8fd2c45, quad
  b5-const NO step + ring edges + thresholds
  15/143, NO D dips).
- C diff pure-add: numstat 647/0 rgramc.c + 266/0
  rgram.py (+1/-1 for-line, +66/0 PINS); raw C 642
  content + 5 blank-only `+` lines / 0 del; raw py
  266 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 180, py del-uniq
  0 add-uniq 199). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 256db28a..
  2d5cbe97, 980 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 647/0, rgram.py 266/0,
  test_rgram.sh 1/1, PINS 66/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1586->1592 +6, singletons
  `if n == ` 598->600 +2, range-guards `<= n <=`
  584->588 +4, CLOSED T10P prints 1586->1592 +6,
  seal 1680->1686
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 593->595 +2,
  range 584->588 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b389 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-699-q795
  memo CONFIRM 39/39 (section heads shape 13/13 +
  quad+T-ring 14/14 + counters 12/12 quoted
  verbatim; tier cut SAFE; w2b-r22 8/8 CAP COMPLETE)
  + A-347-q347 viewer corroborates same tier (all
  legs CONFIRM, consts 76/67/66/73 INCL).
  No DISSENT on P283. Agrees with cport commit msg
  (py/C 16688, PYID 8344).
- Quiz: no conflicting CLAIM/GATE/FLAG on b391/
  2d5cbe97. b390 EVEN = sweep2 turf (sweep2-r60 live
  b388+b390), used b390 tip as diff-base only, NOT
  gated. Newest PARENT-* is QNUM-19 (w2d Q-block
  only, read, no gate impact); PROSE-01 re-read
  before filing.
- Logs: NVME ws tmp/encode-sweep/r59/ (build391.log,
  pyid391.log, rgram391py/c.log, pass391py/c.txt,
  for390-old.nums/for391-new.nums, seteq391.py/log,
  smoke391.log, tables391.log,
  tabaudit391.py, edges391.py, edges391.log,
  cdiff391.txt, pydiff391.txt, banddiff391.txt,
  added391.txt, numstat391.txt, build391/ binaries,
  tail-115568.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
