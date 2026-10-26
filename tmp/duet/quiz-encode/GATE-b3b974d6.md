# GATE b3b974d6 b349 T10P241 pins 100605..100952 (348 pins) PASS-functional

Seat sweep-r48, first-hand, WT tmp/wt-encode-sweep @b3b974d6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r48.
Band = a84ebe31 (py merge w2b@b13d5cc0 partial, +6 tiers
+62 pins) + b3b974d6 (C port). Base e97ace92 (b348 tip,
1428 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build349/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r48), rgramc 1025c9de.
- RGRAMC-PYID 7029/7029 covered=7029/7029 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 14058/14058 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 14058/14058 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (14058/14058, version-sorted).
- PINS-RGRAM names set-eq 14058/14058 (cmp-equal both ways).
  PINS cells 7029 vs for-list 7029: exact match both ways
  (cells-for {} + for-cells {}, tail 100952 pinned AND in
  for-list).
- PINS 14060 rows (2 hdr + 14058, +62 vs base 13998). py diff
  +62/-0 rows = +31/-0 cells (pure P241 addition);
  test_rgram.sh for-line tracked 1/1 (fast battery parses sh
  for-line; 2x7029 names).
  For-list union 6998->7029 +31/-0: 2 sing (100605 100606) +
  A 4 (head 100607 + carry edge 100608 + off7 100614 + tail
  100622) +
  C 7 (off 0,1,2,3,4,6,9: 100623 100624 100625 100626
  100627 100629 100632; off 5,7,8 unsampled) + Q 12 (row
  starts off 0/16/32/48 + row ends off 15/31/47/63 + off
  7/23/39/55: 100633 100640 100648 100649 100656 100664
  100665 100672 100680 100681 100688 100696) + R 6 (head
  100697 + edge pairs 100735/100736 + 100863/100864 + tail
  100952).
  PINS adds = same 31 tier pins.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P241 C-vs-py, 13-table A/C10/QUADms+T88 layout,
  all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 3f550100 / 4dc2a402, both ==P240 sig REPEAT with NEW
  bodies first-hand);
  AM 16/16 (9B), CM 10/10 (20B), M 16/16 (6B),
  QR 4/4 (13B), QT 4/4 (4B), RM 16/16 (7B), RQ 16/16 (6B)
  EXACT;
  AC 73/73, CC 62/62, QC 59/59, RC 73/73 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 73/62/59/73 match actual;
  TABAUDIT-GREEN rc=0 (47 PASS 0 FAIL). No BM/BC (C10
  replaces B), no M19/XA19/M42/X42 (no b19/b42 leg), no
  PT/FM (no PAIR/FRAG), table inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-11 [4,5,47,48,49,50,
  51,76,77,78,79] = b4,b5+M9 (b47-51,76-79);
  CC-22 [2,3,4,5,20,21,23,24,25,26,27,35,46,47,48,49,50,
  51,80,81,82,83] = b4,b5+M20 (b2,3,20,21,23-27,35,46-51,
  80-83, b22 skipped);
  QC-25 [3,4,5,6,7,20,21,24,25,26,27,35,46,47,49,50,51,
  76,77,78,79,80,81,82,83] = b4,b5+M6 (b6,7,76-79)+R13
  (b3,20,21,24-27,35,46,47,49-51, b48 skipped)+T4
  (b80-83);
  RC-15 [4,5,6,7,9,10,11,76,77,78,79,80,81,82,83] = VPOS
  15 over 0..87 (b4,b5+M7 b9-11,80-83 + R6 b6,7,76-79).
  b0-3 first-hand: AC a0/95/57/36 (PBA sig a0955736); CC
  0:4d 1:c2 2:TAB 3:TAB (sigs 4dc2+tab); QC 0:de 1:24
  2:4c 3:TAB (row-led de244c + b3 row-sig); RC 03000000
  (NEW sig).
  Code AC73/CC62/QC59/RC73; incl = +0/+1/+1/+0
  (A b5 carry, C/Q b5 const 12, T counter) = 73/63/60/73;
  lane consts 73/63/60/73 = A-562/A-311 INCL EXACT
  (writer dual-accounts C10/quad = memo-1, PBA+T88
  identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2410 n==100605 / P2411 n==100606
  singleton-const (offs 0/1);
  P241A 100607..100622 off=n-100607 PBA16
  (m-tab 9B b47-51,76-79, sig a0955736 ==P240PBA,
  FIRST PBA b5-carry 11->12 @100607->100608);
  P241C 100623..100632 off=n-100623 C10-MS 6-sig
  (m-tab 20B b2,3,20,21,23-27,35,46-51,80-83 b22-skipped,
  sig bytes in tab);
  P241Q 100633..100696 off=n-100633 m=off&15 q=off>>4
  QUADms row-led de244c1f/de244c20 (M 6B b6,7,76-79 +
  R13 13B b3,20,21,24-27,35,46,47,49-51 b48-skipped +
  QT b80-83, b5 const 12);
  P241R(T88-ring) 100697..100952 off=n-100697 c=off&15
  r=off>>4 STANDARD sig 03000000 NEW (RM 7B b9-11,80-83
  by COL + RQ 6B b6,7,76-79 by ROW SPLIT tails,
  b84-87 const 6b/af/ef/49);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)&0xFFFF
  pay4=l16&0xFF pay5=l16>>8; R paylen 88 + counter
  b4=(0xb3+2off)&FF b5=0x12+(off>=39)+(off>=167).
  C blocks carry T66213/66218/66223/66238/66256/66280
  py-line mirrors (exact); guards
  `if ((n) == (100605))` / `if ((n) == (100606))` + 4 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; counter
  179/18+(off>=39)+(off>=167); temps _t5126.._t5143
  appended (base max _t5125, no reuse);
  C byte-index lists match py per block; insert position
  exact (dispatch tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct; CM 10/10
  diverge, 6-sig map order EXACT (4dc2a402 x3 @100623-25
  + 4dc2f401/4dc2d401/4dc2f401/4dc20402/4dc21402/
  4dc22402/4dc2f401 @100626-32, b2b3 a402x3 +
  f401/d401/f401/0402/1402/2402/f401);
  M 16/16 distinct;
  QR TRIPLE-PAIRED r1==r2==r3 2/4 (2089f9b03c37ecc1fbfb
  745f57 x3; r0 1f09fbcc61796e01b02aca478b distinct;
  row-sigs b3 1f/20/20/20);
  QT 4/4 distinct exact (a46dc517/a6780a47/d0780a47/
  fa780a47; r1/r2/r3 share last 2B 0a47; r0 ends c517);
  RQ==M FULL 16/16 element-wise (QM==TR staged to full
  equality this band);
  tails SPLIT (RM b80-83 part 16 distinct col-shared +
  RQ b76-79 part 16 distinct row-shared);
  M-tails 16/16 ALL NEW vs P240T, RM 16/16 NEW vs
  P240RM, QT 4/4 NEW vs P240QT.
  Counter/lencode edges computed first-hand (never trusted
  from comments): A head ff/11 (100607) edge+ 01/12
  (100608) tail 1d/12 (100622), b5set {11,12}; C head
  1f/12 (100623) mid 27/12 (100627) tail 31/12 (100632);
  Q head 33/12 (100633) mid 71/12 (100664) tail b1/12
  (100696); b5 const 12 full range C/Q (sets {12}).
  T off38/39 (100735->100736) ff/12->01/13
  + off166/167 (100863->100864) ff/13->01/14. All edge
  pins in for-list + PASS (batteries GREEN); 100952 tail
  pinned + in for-list + PASS. Odd-lencode 348/348
  first-hand.
  Matches A-562/A-311 geometry (mixed-size 92x84B+256x88B,
  PB0 3f550100 ==P240PB0, PB1 4dc2a402 ==P240PB1, PBA16
  a0955736 NEW geometry VPOS 11 FIRST PBA carry 11->12,
  C10-MS 6-sig map VPOS 21 b22-skipped b5 const 12 10/10
  diverge, QUADms row-led de244c1f/20 VPOS 24 b5 const
  12 + M6 shared + R13 TRIPLE b48-skipped + tails 4/4
  TRUE-2B + M-tails ALL NEW 16/16, T88-ring STANDARD NEW
  sig 03000000 M7 by COL + R6 by ROW UNPAIRED 16/16 +
  SPLIT tails + b84-87 const 6bafef49 + M-tails ALL NEW
  16/16, ring edges + thresholds 39/167, NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 239/0 rgram.py
  (+1/-1 for-line, +62/0 PINS); raw C 610 add / 0 del
  (611 incl +++ header); normalized ([0-9]+ -> N,
  diff-sign strip, trailing-';' strip, python sets)
  del-subset-add 0 missing (del-uniq 0, add-uniq 154).
- Wall on band diff added lines (scope e97ace92..b3b974d6,
  912 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 610/0,
  rgram.py 239/0, test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks, tier-comments
  1593->1599 +6, singletons `if n == ` 514->516 +2,
  range-guards `<= n <=` 416->420 +4, CLOSED prints
  1851->1857 +6: all agree (stated literal methods,
  first-hand). py lines del 0 add 239.
- CONFIRM evidence (CONVERT-01 rule b): A-562-q633
  T10P241 predictive reproduces 33/33 (shape 15/15 +
  quad+Tring 10/10 + counters 8/8 CONFIRM, cut SAFE)
  + A-311-q305 corroborates same tier (3/3 legs CONFIRM,
  consts 73/63/60/73 INCL). No DISSENT on P241. Agrees
  with cport commit msg (py/C 14058, PYID 7029).
- Quiz: no conflicting CLAIM/GATE/FLAG on b349/b3b974d6.
  b348/b350 EVEN = sweep2 turf, used b348 tip as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-11
  (w2f Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r48/ (*349* files:
  build349.log, pyid349.log, rgram349py/c-full.log,
  pass349py/c.txt, pins348base.csv, pins348/349-cells.nums,
  for349-old/-new.nums, pins349.py, sh348.sh, smoke349.log,
  tables349.log, tabaudit349.py, cdiff349.txt/-add-norm/
  -del-norm, banddiff349.txt, added349.txt, numstat349.txt,
  rgram348.py, rgramc348.c).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
