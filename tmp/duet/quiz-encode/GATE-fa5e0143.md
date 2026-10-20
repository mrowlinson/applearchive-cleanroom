# GATE fa5e0143 b345 T10P237 pins 99213..99560 (348 pins) PASS-functional

Seat sweep-r47, first-hand, WT tmp/wt-encode-sweep @fa5e0143,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r47.
Band = b1b96b2b (py merge w2b@ea63fbd4 partial, +6 tiers
+62 pins) + fa5e0143 (C port). Base 5d63fca7 (b344 tip,
1404 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build345/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r47), rgramc a14c9ab2.
- RGRAMC-PYID 6905/6905 covered=6905/6905 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 13810/13810 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 13810/13810 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (13810/13810, version-sorted).
- PINS-RGRAM names set-eq 13810/13810 (cmp-equal both ways).
  PINS cells 6905 vs for-list 6905: exact match both ways
  (cells-for {} + for-cells {}, tail 99560 pinned AND in
  for-list).
- PINS 13812 rows (2 hdr + 13810, +62 vs base 13750). py diff
  +62/-0 rows = +31/-0 cells (pure P237 addition);
  test_rgram.sh for-line tracked 1/1 (fast battery parses sh
  for-line; 2x6905 names).
  For-list union 6874->6905 +31/-0: 2 sing (99213 99214) +
  A 4 (head 99215 + off1 99216 + mid 99222 + tail 99230) +
  C 7 (off 0,1,2,3,4,6,9: 99231 99232 99233 99234 99235
  99237 99240; off 5,7,8 unsampled) + Q 12 (row starts off
  0/16/32/48 + row ends off 15/31/47/63 + off 7/23/39/55:
  99241 99248 99256 99257 99264 99272 99273 99280 99288
  99289 99296 99304) + R 6 (head 99305 + edge pairs
  99327/99328 + 99455/99456 + tail 99560).
  PINS adds = same 31 tier pins.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P237 C-vs-py, 13-table A/C10/QUAD layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 93540100 / b590ac02);
  AM 16/16, CM 10/10, M 16/16,
  QR 4/4, QT 4/4, RM 16/16, RQ 16/16 EXACT;
  AC 76/76, CC 64/64, QC 63/63, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/64/63/71 match actual;
  TABAUDIT-GREEN rc=0. No BM/BC (C10 replaces B),
  no M42/X42 (NO b42 leg), no PT/FM (no PAIR/FRAG),
  table inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-8 [4,5,24,25,76,77,78,
  79] = b4,b5+M6 (b24,25,76-79) = VPOS 7;
  CC-20 [2,3,4,5,20,21,22,23,24,25,26,27,28,29,30,31,80,
  81,82,83] = b4,b5+M18 (b2,3,20-31,80-83) = VPOS 19;
  QC-21 [4,5,21,22,23,24,25,26,27,28,29,30,31,76,77,78,
  79,80,81,82,83] = b4,b5+M8 (b21-23,31,76-79)+R7
  (b24-30)+T4 (b80-83) = VPOS 20;
  RC-17 [4,5,25,26,27,35,40,41,42,76,77,78,79,80,81,82,
  83] = VPOS 17 over 0..87 (b4,b5+M7 b40-42,76-79 + R8
  b25-27,35,80-83). QC b42 const 0x14 first-hand (in
  consts, outside VPOS).
  b0-3 first-hand: AC 609bd720; CC (0,ad),(1,52) const +
  b2,3 in tab (2-sig map); QC ad520714; RC 01000000.
  Code AC76/CC64/QC63/RC71; incl = +1/+1/+1/+0
  (A/C/Q b5 const 07, T counter) = 77/65/64/71; lane
  consts 77/65/64/71 = A-553/A-307 INCL EXACT (writer
  dual-accounts PBA/C10/quad = memo-1, T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2370 n==99213 / P2371 n==99214
  singleton-const (offs 0/1);
  P237A 99215..99230 off=n-99215 sig 609bd720
  (m-tab 6B b24,25,76-79);
  P237C 99231..99240 off=n-99231 C10 2-sig
  (m-tab 18B b2,3,20-31,80-83, sig bytes in tab);
  P237Q 99241..99304 off=n-99241 m=off&15 q=off>>4
  QUAD single-sig (M 8B b21-23,31,76-79 + R7 7B b24-30
  + QT b80-83, b42 const via consts, NO b42 leg);
  P237R(T88-ring) 99305..99560 off=n-99305 c=off&15
  r=off>>4 STANDARD sig 01000000 (RM 7B b40-42,76-79
  by COL + RQ 8B b25-27,35,80-83 by ROW INVERTED tails,
  b84-87 const 7a/cd/c1/0e);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)&0xFFFF
  pay4=l16&0xFF pay5=l16>>8; R paylen 88 + counter
  b4=(0xd3+2off)&FF b5=0x07+(off>=23)+(off>=151).
  C blocks carry T65240/65245/65250/65265/65282/65305
  py-line mirrors (exact); guards
  `if ((n) == (99213))` / `if ((n) == (99214))` + 4 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; counter
  211/7+(off>=23)+(off>=151); temps _t5052.._t5069
  appended (base max _t5051, no reuse);
  C byte-index lists match py per block; insert position
  exact (dispatch tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 + M 16/16 + RM 16/16
  + RQ 16/16 distinct; CM 10/10 diverge, 2-sig map order
  EXACT (a702 x3 @99231-33 + 5701 x7 @99234-40);
  QR TRIPLE-PAIRED r1==r2==r3 2/4 (e63c528914eb60 x3;
  r0 aefc0117f49a39 distinct);
  QT 4/4 distinct exact (4d4c1e83/0e319725/a0160327/
  ca160327; r2/r3 share last 3B 160327; r1 0e319725 no
  triple share);
  RQ==M FULL 16/16 element-wise (QM==TR staged to full
  equality);
  tails INVERTED (RM b76-79 part 16 distinct col-shared +
  RQ b80-83 part 16 distinct row-shared);
  M-tails 16/16 ALL NEW vs P236T, RM 16/16 NEW vs
  P236RM, QT 4/4 NEW vs P236QT.
  Counter/lencode edges computed first-hand (never trusted
  from comments): A head 1f/07 (99215) mid 2d/07 tail
  3d/07 (99230); C head 3f/07 (99231) mid 47/07 tail
  51/07 (99240); Q head 53/07 (99241) mid 91/07 tail
  d1/07 (99304); b5 const 07 full range A/C/Q (sets
  {07}), no carry. T off22/23 (99327->99328) ff/07->01/08
  + off150/151 (99455->99456) ff/08->01/09. All edge pins
  in for-list + PASS (batteries GREEN); 99560 tail pinned
  + in for-list + PASS. Odd-lencode 348/348 first-hand.
  Matches A-553/A-307 geometry (mixed-size 92x84B+256x88B,
  PB0 93540100 NEW, PB1 b590ac02 NEW, PBA 609bd720 VPOS 7
  b5 const 07, C10-2SIG map VPOS 19 b5 const 07 10/10
  diverge, QUAD single-sig ad520714 NEW VPOS 20 b5 const
  07 no carry + M8 shared + NO b42 + R7 TRIPLE-PAIRED +
  tails 4/4 + M-tails ALL NEW 16/16, T88-ring STANDARD M7
  by COL + R8 by ROW UNPAIRED 16/16 + INVERTED tails +
  b84-87 const 7acdc10e + M-tails ALL NEW 16/16, ring
  edges + thresholds 23/151, NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 237/0 rgram.py
  (+1/-1 for-line, +62/0 PINS); raw C 610 add / 0 del
  (611 incl +++ header); normalized ([0-9]+ -> N,
  diff-sign strip, trailing-';' strip, python sets)
  del-subset-add 0 missing (del-uniq 0, add-uniq 158).
- Wall on band diff added lines (scope 5d63fca7..fa5e0143,
  910 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 610/0,
  rgram.py 237/0, test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks, tier-comments
  1310->1316 +6, singletons `if n == ` 506->508 +2,
  range-guards `<= n <=` 400->404 +4, CLOSED prints
  1827->1833 +6: all agree (stated literal methods,
  first-hand). py lines del 0 add 237.
- CONFIRM evidence (CONVERT-01 rule b): A-553-q629
  T10P237 predictive reproduces 33/33 (shape 15/15 +
  quad+Tring 10/10 + counters 8/8 CONFIRM, cut SAFE,
  states no DISSENT) + A-307-q301 corroborates same tier
  (3/3 legs CONFIRM, consts 77/65/64/71 INCL). No DISSENT
  on P237. Agrees with cport commit msg (py/C 13810,
  PYID 6905).
- Quiz: no conflicting CLAIM/GATE/FLAG on b345/fa5e0143.
  b344/b346 EVEN = sweep2 turf, used b344 tip as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-09
  (w2e Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r47/ (*345* files:
  build345.log, pyid345.log, rgram345py/c-full.log,
  pass345py/c.txt, pins344base.csv, pins344/345-cells.nums,
  for345-old/-new.nums, pins345.py, sh344.sh, smoke345.log,
  tables345.log, tabaudit345.py, cdiff345.txt/-add-norm/
  -del-norm, banddiff345.txt, added345.txt, rgram344.py).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
