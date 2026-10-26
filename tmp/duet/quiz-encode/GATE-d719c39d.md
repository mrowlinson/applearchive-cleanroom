# GATE d719c39d b357 T10P249 pins 103389..103736 (348 pins) PASS-functional

Seat sweep-r51, first-hand, WT tmp/wt-encode-sweep @d719c39d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r51.
Band = 1352f58d (py merge w2b@9c144a8e partial, +6 tiers
+62 pins) + d719c39d (C port). Base f9bb207b (b356 tip,
1476 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build357/{aae,rgramc}, rc=0,
  0 warnings. aae sha1 7d8dd3a2 / sha256 d6e27c97
  (both pinned stable: sha1 r39-r51, sha256 b354-b357),
  rgramc sha1 00ea4b5e / sha256 51554ddc.
- RGRAMC-PYID 7277/7277 covered=7277/7277 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 14554/14554 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 14554/14554 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (14554/14554, sorted).
- PINS-RGRAM cells set-eq 7277/7277 (xor 0 all 3 ways:
  for^pass for^pins pass^pins).
  PINS 14556 rows (2 hdr + 14554, +62 vs base 14494).
  For-list union 7246->7277 +31/-0 (2x7277 names,
  fast battery parses sh for-line).
  31 = 2 sing (103389 103390) +
  A 6 (head 103391 + 103392 + 103398 + 103402 + 103405 +
  tail 103406) +
  C 8 (head 103407 + 103409 + 103410 + 103411 + 103412 +
  103413 + 103414 + 103415; offs 1,9 unsampled: 103408,
  103416) +
  Q 8 (head 103417 + EARLY-carry pair 103423/103424 +
  103433 + 103449 + 103465 + 103479 + tail 103480) +
  R 7 (head 103481 + edge pair 103551/103552 + mid
  103609 + edge pair 103679/103680 + tail 103736).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 31x2 = 62 = 14554-14492.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P249 C-vs-py, 13-table A-PBA/C10-7SIG/
  QUADms-1Boff+T88 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 18e10200 NEW / c503ce05 ==P248PB1, S1 NEW string);
  AM 16/16 (8B), CM 10/10 (13B), M 16/16 (8B),
  QR 4/4 (8B), QT 4/4 (4B), RM 16/16 (7B), RQ 16/16 (7B)
  EXACT;
  AC 74/74, CC 69/69, QC 62/62, RC 72/72 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 74/69/62/72 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit357.py 34 PASS 0 FAIL).
  No BM/BC (C10 replaces B10), no M42/X42 (b42 const
  0x9d/0x8a/0x8a/0x79 via consts, NO b42 leg), no
  M19/XA19 (no b19 leg), no PT/FM (no PAIR/FRAG), table
  inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-10 [4,5,48,49,50,
  51,76,77,78,79] = b4,b5+M8 (b48-51,76-79);
  CC-15 [2,3,4,5,35,46,47,48,49,50,51,80,81,82,83] =
  b4,b5+M13 (b2,3,35,46-51,80-83, sig bytes in tab);
  QC-22 [3,4,5,6,7,8,9,35,46,47,48,49,50,51,76,77,
  78,79,80,81,82,83] = b4,b5+QM8 (b6-9,76-79)+R8
  (b3,35,46-51)+T4 (b80-83);
  RC-16 [4,5,6,7,9,10,11,12,76,77,78,79,80,81,82,
  83] = VPOS 16 over 0..87 (b4,b5+TM7 b9-11,80-83 +
  TR7 b6,7,12,76-79).
  b0-3 first-hand: AC b0-3 809a1f4a (==P248PBA sig);
  CC b0,1 c5,03 const (b2,3 TAB sig-in-tab); QC b0-2
  5c,3c,e0 const (b3 TAB row-sig 47/46); RC 05000000
  (NEW, breaks 02000000 run).
  Code AC74/CC69/QC62/RC72; incl = +1/+1/+0/+0
  (A/C b5 const 27, Q b5-carry, T counter) =
  75/70/62/72; lane consts = A-597/A-319 INCL EXACT
  (writer PBA/C10 = memo-1, quad/T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2490 n==103389 / P2491 n==103390
  singleton-const (offs 0/1);
  P249A 103391..103406 off=n-103391 PBA16
  (m-tab 8B b48-51,76-79, sig 809a1f4a ==P248PBA NEW
  geometry, b5 const 27);
  P249C 103407..103416 off=n-103407 C10-MS 7-sig
  (m-tab 13B b2,3,35,46-51,80-83, sig bytes in tab,
  sigs c503ce05 x3 + c5034e05/c5030e04/c5034e04/
  c5036e04/c5037e04 x1 + c503be04 x2, b5 const 27);
  P249Q 103417..103480 off=n-103417 m=off&15 q=off>>4
  QUADms 1B-off row-led 5c3ce047 + 5c3ce046 (M 8B
  b6-9,76-79 + R8 8B b3,35,46-51 TRIPLE + QT b80-83,
  b5-carry 27->28 @103423->103424 EARLY-INTERNAL
  off6->7);
  P249R(T88-ring) 103481..103736 off=n-103481
  c=off&15 r=off>>4 STANDARD sig 05000000 (TM 7B
  b9-11,80-83 by COL + TR 7B b6,7,12,76-79 by ROW
  SPLIT tails, b84-87 const 79/ad/62/84);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)&0xFFFF
  pay4=l16&0xFF pay5=l16>>8; R paylen 88 + counter
  b4=(0x73+2off)&FF b5=0x28+(off>=71)+(off>=199).
  C blocks carry T68300/68305/68310/68325/68341/68364
  py-line mirrors (exact); guards
  `if ((n) == (103389))` / `if ((n) == (103390))` + 4 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; counter
  115/40 + (off>=71)+(off>=199); temps _t5280.._t5297
  appended (base max _t5279, no reuse);
  _i max 3224->3235, _b max 3223->3234, no reuse;
  C byte-index lists match py per block (A 8B, C 13B,
  Q 8/8/4B, R 7/7B); insert position exact (dispatch
  tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge, 7-sig map order EXACT (c503ce05 x3
  @103407-09 + c5034e05 @103410 + c5030e04 @103411 +
  c5034e04 @103412 + c5036e04 @103413 + c5037e04
  @103414 + c503be04 x2 @103415-16);
  M 16/16 distinct;
  QR TRIPLE r1==r2==r3 (460a99cc5196b776 x3; r0
  47cad1a5d1b2a75c distinct; b3 row-sigs 47/46/46/46);
  QT 4/4 distinct exact (6d6d4ae9/706b3942/9a6b3942/
  c46b3942; r1/r2/r3 share last 3B 6b3942);
  RQ==M shared-slice 16/16 (b6,7,76-79 same-index equal;
  full-string 0/16: layouts diverge at byte2, RQ b12 vs
  M b8; P243-style, NOT P245 string-equal);
  tails SPLIT (RM indexed by COL c=off&15, RQ by ROW
  r=off>>4, RM/RQ 16/16 distinct, 0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P248M-tails, RM 16/16 NEW vs
  P248RM, QT 4/4 NEW vs P248QT (2B tails 6936/9336/
  30ea/5aea, width differs, zero overlap).
  S0 NEW (P248S0 sig 1ce10200); S1 NEW string (sig
  c503ce05 ==P248PB1).
  Counter/lencode edges computed first-hand (never trusted
  from comments): A head bf/27 (103391) tail dd/27
  (103406), b5set {27}; C head df/27 (103407) tail
  f1/27 (103416), b5set {27};
  Q head f3/27 (103417) carry ff/27->01/28
  @103423->103424 EARLY-INTERNAL, b5set {27,28}.
  T head 73/28 (103481) + off70/71 (103551->103552)
  ff/28->01/29 + off198/199 (103679->103680)
  ff/29->01/2a + tail off255 71/2a (103736). All edge
  pins in for-list + PASS (batteries GREEN); 103736
  tail pinned + in for-list + PASS. Odd-lencode 348/348
  first-hand. S0/S1 embedded b4/b5 (bb/27, bd/27) match
  raw lencode.
  Matches A-597/A-319 geometry (mixed-size 92x84B+256x88B,
  PB0 18e10200 NEW + PB1 c503ce05 ==P248PB1, PBA16
  VPOS 9 b5 const 27, C10-MS 7-sig VPOS 14 b5 const
  27 10/10 diverge, QUADms 1B-off row-led VPOS 22 b3
  47/46 + QM8 shared + R8 TRIPLE + tails 4/4
  r1/r2/r3-3B + M-tails ALL NEW 16/16, T88-ring STANDARD
  sig 05000000 TM7 by COL + TR7 by ROW UNPAIRED 16/16 +
  SPLIT tails + b84-87 const 79ad6284 + RM-tails ALL NEW
  16/16, ring edges + thresholds 71/199, NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 237/0 rgram.py
  (+1/-1 for-line, +62/0 PINS); raw C 605 content + 5
  blank-only `+` lines / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip, trailing-';'
  strip, python sets) del-subset-add 0 missing (del-uniq 0,
  add-uniq 174). Band-level sole del = old for-line churn
  (for-line 1/1).
- Wall on band diff added lines (scope f9bb207b..d719c39d,
  910 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 610/0,
  rgram.py 237/0, test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks, tier-comments
  `# T10P` 1382->1388 +6, singletons `if n == ` 530->532
  +2, range-guards `<= n <=` 448->452 +4, CLOSED prints
  1382->1388 +6, seal 1476->1482 +6: all agree (stated
  literal methods, first-hand). C guards: singleton
  `if ((n) == (` 525->527 +2, range 448->452 +4; 5-count
  C-vs-py singleton offset pre-existing (C-only dip
  guards 11609/12909/13257/13605/14045), unchanged by
  band; every py guard has its C guard (set-diff empty).
- CONFIRM evidence (CONVERT-01 rule b): A-597-q761
  T10P249 memo CONFIRM 33/33 (shape 11/11 +
  quad+Tring 12/12 + counters 10/10, backfill 2/4,
  writer VERIFY 13188/13188 0 FAIL cited)
  + A-319-q313 viewer corroborates same tier (3/3 legs
  CONFIRM, consts 75/70/62/72 INCL). No DISSENT on P249.
  Agrees with cport commit msg (py/C 14554, PYID 7277).
- Quiz: no conflicting CLAIM/GATE/FLAG on b357/d719c39d.
  b356/b358 EVEN = sweep2 turf, used b356 tip as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-12
  (w2b Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r51/ (build357.log,
  pyid357.log, rgram357py/c-full.log, pass357py/c.txt,
  pins356base.csv, for357-old/-new.nums, sh356/357.sh,
  smoke357.log, tables357.log, tabaudit357.py,
  edges357.log, numstat357.txt, cdiff357.txt,
  banddiff357.txt, py/c356base, build357/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
