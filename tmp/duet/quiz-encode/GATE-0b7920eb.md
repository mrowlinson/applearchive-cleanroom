# GATE 0b7920eb b359 T10P251 pins 104085..104432 (348 pins) PASS-functional

Seat sweep-r51, first-hand, WT tmp/wt-encode-sweep @0b7920eb,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r51.
Band = 7226d19c (py merge w2b@a6d4e0a9 partial, +6 tiers
+62 pins) + 0b7920eb (C port). Base 00142e87 (b358 tip,
1488 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build359/{aae,rgramc}, rc=0,
  0 warnings. aae sha1 7d8dd3a2 / sha256 d6e27c97
  (both pinned stable: sha1 r39-r51, sha256 b354-b359),
  rgramc sha1 98a09d55 / sha256 a16d347d.
- RGRAMC-PYID 7339/7339 covered=7339/7339 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 14678/14678 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 14678/14678 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (14678/14678, sorted).
- PINS-RGRAM cells set-eq 7339/7339 (xor 0 all 3 ways:
  for^pass for^pins pass^pins).
  PINS 14680 rows (2 hdr + 14678, +62 vs base 14618).
  For-list union 7308->7339 +31/-0 (2x7339 names,
  fast battery parses sh for-line).
  31 = 2 sing (104085 104086) +
  A 6 (head 104087 + 104088 + 104094 + 104098 + 104101 +
  tail 104102) +
  B 6 (head 104103 + 104104 + 104107 + 104109 + 104111 +
  tail 104112; offs 2,3,5,7 unsampled: 104105, 104106,
  104108, 104110) +
  Q 10 (head 104113 + 104121 + 104129 + 104137 + 104145 +
  104153 + 104161 + 104169 + 104175 + tail 104176; step-8
  coverage, NO carry pair: b5 const) +
  R 7 (head 104177 + edge pair 104191/104192 + mid
  104305 + edge pair 104319/104320 + tail 104432).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 31x2 = 62 = 14678-14616.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P251 C-vs-py, 15-table A-PBA/B10-1SIG/
  QUAD-b42xor+T88 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 90fc0200 ==P250PB0 REPEAT / 5d16fd05 NEW, both NEW
  strings);
  AM 16/16 (7B), BM 10/10 (11B), M 16/16 (7B),
  M42 16/16 (1B), X42 4/4 (1B), QR 4/4 (6B),
  QT 4/4 (4B), RM 16/16 (7B), RQ 16/16 (8B) EXACT;
  AC 75/75, BC 71/71, QC 64/64, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 75/71/64/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit359.py 39 PASS 0 FAIL).
  No CM/CC (B10 replaces C10), no M19/XA19 (no b19 leg),
  no PT/FM (no PAIR/FRAG), table inventory exactly
  the 15.
  Missing-sets first-hand EXACT: AC-9 [4,5,36,37,38,76,
  77,78,79] = b4,b5+M7 (b36-38,76-79);
  BC-13 [4,5,36,37,38,39,40,41,42,80,81,82,83] =
  b4,b5+M11 (b36-42,80-83, b42 IN M-range);
  QC-20 [4,5,34,35,36,37,38,39,40,41,42,43,76,77,78,
  79,80,81,82,83] = b4,b5+QM7 (b34,35,43,76-79)+b42
  xor-leg+R6 (b36-41)+T4 (b80-83);
  RC-17 [4,5,38,39,46,47,52,53,54,76,77,78,79,80,81,
  82,83] = VPOS 17 over 0..87 (b4,b5+TM7 b52-54,80-83
  + TR8 b38,39,46,47,76-79).
  b0-3 first-hand: AC b0-3 00882f46 (NEW, P250Q-adjacent
  26->46); BC b0-3 5d16fd05 (==PB1 sig); QC b0-3
  00882f46 (==PBA sig); RC 05000000 (==P249T sig).
  b42: AC const 0x2f, BC in m-tab, QC xor-leg (42 NOT
  in consts), RC const 0x7e.
  Code AC75/BC71/QC64/RC71; incl = +1/+1/+1/+0
  (A/B/Q b5 const 2d, T counter) = 76/72/65/71;
  lane consts = A-599/A-362 INCL EXACT (writer
  PBA/B10/quad = memo-1, T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/B/Q/R): P2510 n==104085 / P2511 n==104086
  singleton-const (offs 0/1);
  P251A 104087..104102 off=n-104087 PBA16
  (m-tab 7B b36-38,76-79, sig 00882f46 NEW, b5 const
  2d);
  P251B 104103..104112 off=n-104103 B10 single-sig
  (m-tab 11B b36-42,80-83, b42 IN range, sig 5d16fd05
  ==PB1 x10, b5 const 2d);
  P251Q 104113..104176 off=n-104113 m=off&15 q=off>>4
  single-sig quad 00882f46 (M 7B b34,35,43,76-79 +
  b42 row-xor X=[00,06,06,06] XOR-staged ADD-tie +
  R6 6B b36-41 TRIPLE + QT b80-83, b5 const 2d);
  P251R(T88-ring) 104177..104432 off=n-104177
  c=off&15 r=off>>4 STANDARD sig 05000000 (TM 7B
  b52-54,80-83 by COL + TR 8B b38,39,46,47,76-79 by
  ROW SPLIT tails, b84-87 const d3/11/a2/7a);
  A/B/Q paylen 84 + raw lencode l16=((n<<1)|1)&0xFFFF
  pay4=l16&0xFF pay5=l16>>8; R paylen 88 + counter
  b4=(0xe3+2off)&FF b5=0x2d+(off>=15)+(off>=143).
  C blocks carry T68797/68802/68807/68822/68838/68863
  py-line mirrors (exact); guards
  `if ((n) == (104085))` / `if ((n) == (104086))` + 4 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; b42xor via
  snprintf %02lx of pay[42]^hexval(X42[q]) vs M42[m]
  (matches py); counter 227/45 + (off>=15)+(off>=143);
  temps _t5316.._t5335 appended (base max _t5315, no
  reuse); _i max 3246->3257, _b max 3245->3256, no
  reuse; C byte-index lists match py per block (A 7B,
  B 11B, Q 7/1/6/4B, R 7/8B); insert position exact
  (dispatch tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct; BM 10/10
  diverge (single-sig rows, all distinct);
  M 16/16 distinct;
  M42 col-vec 4-valued {d6,96,56,16} counts 6/4/3/3,
  low-nibble const 6; X42 [00,06,06,06] EXACT
  (ADD-tie A=[0,fa,fa,fa] noted in code comment, XOR
  staged per b42-family precedent);
  QR TRIPLE r1==r2==r3 (865bd276b11b x3; r0
  dc5dc1973145 distinct);
  QT 4/4 distinct exact (50155041/7e8da7ed/a88da7ed/
  d28da7ed; r1/r2/r3 share last 3B 8da7ed);
  RQ==M tail-slice 16/16 (b76-79 same-index equal;
  full-string impossible: RQ 8B vs M 7B layouts;
  P243-style shared-slice, NOT P245 string-equal);
  tails SPLIT (RM indexed by COL c=off&15, RQ by ROW
  r=off>>4, RM/RQ 16/16 distinct, 0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P250M-tails (P250M 8B),
  RM 16/16 NEW vs P250RM, QT 4/4 NEW vs P250QT
  (36735045/e43d6c14/0e3e6c14/383e6c14).
  S0 NEW string (sig 90fc0200 ==P250PB0); S1 NEW
  (P250S1 sig 3420f905).
  Counter/lencode edges computed first-hand (never trusted
  from comments): A head 2f/2d (104087) tail 4d/2d
  (104102), b5set {2d}; B head 4f/2d (104103) tail
  61/2d (104112), b5set {2d}; Q head 63/2d (104113)
  tail e1/2d (104176), b5set {2d} NO carry.
  T head e3/2d (104177) + off14/15 (104191->104192)
  ff/2d->01/2e + off142/143 (104319->104320)
  ff/2e->01/2f + mid off128 e3/2e (104305) + tail
  off255 e1/2f (104432). All edge pins in for-list +
  PASS (batteries GREEN); 104432 tail pinned + in
  for-list + PASS. Odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (2b/2d, 2d/2d) match raw lencode.
  Matches A-599/A-362 geometry (mixed-size 92x84B+256x88B,
  PB0 90fc0200 ==P250PB0 + PB1 5d16fd05 NEW, PBA16
  VPOS 8 b5 const 2d 16/16 distinct, B10 single-sig
  VPOS 12 b42-IN b5 const 2d 10/10 diverge, QUAD
  single-sig VPOS 19 QM7 shared + b42 row-XOR tie +
  R6 TRIPLE + tails 4/4 r1/r2/r3-3B + M-tails ALL NEW
  16/16, T88-ring STANDARD sig 05000000 TM7 by COL +
  TR8 by ROW UNPAIRED 16/16 + SPLIT tails + b84-87
  const d311a27a + RM-tails ALL NEW 16/16, ring edges
  + thresholds 15/143, NO D dips).
- C diff pure-add: numstat 640/0 rgramc.c + 260/0 rgram.py
  (+1/-1 for-line, +62/0 PINS); raw C 635 content + 5
  blank-only `+` lines / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip, trailing-';'
  strip, python sets) del-subset-add 0 missing (del-uniq 0,
  add-uniq 168). Band-level sole del = old for-line churn
  (for-line 1/1).
- Wall on band diff added lines (scope 00142e87..0b7920eb,
  963 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 640/0,
  rgram.py 260/0, test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks, tier-comments
  `# T10P` 1394->1400 +6, singletons `if n == ` 534->536
  +2, range-guards `<= n <=` 456->460 +4, CLOSED prints
  1394->1400 +6, seal 1488->1494 +6: all agree (stated
  literal methods, first-hand). C guards: singleton
  `if ((n) == (` 529->531 +2, range 456->460 +4; 5-count
  C-vs-py singleton offset pre-existing (same C-only dip
  guards as b357), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-599-q763
  T10P251 memo CONFIRM 37/37 (shape 12/12 +
  quad+Tring 14/14 + counters 11/11, backfill 4/4,
  writer VERIFY 13312/13312 0 FAIL cited)
  + A-362-q315 viewer corroborates same tier (3/3 legs
  CONFIRM incl tie-stands, consts 76/72/65/71 INCL).
  No DISSENT on P251. Agrees with cport commit msg
  (py/C 14678, PYID 7339).
- Quiz: no conflicting CLAIM/GATE/FLAG on b359/0b7920eb.
  b358/b360 EVEN = sweep2 turf, used b358 tip as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-12
  (w2b Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r51/ (build359.log,
  pyid359.log, rgram359py/c-full.log, pass359py/c.txt,
  pins358base.csv, for359-old/-new.nums, sh358/359.sh,
  smoke359.log, tables359.log, tabaudit359.py,
  edges359.log, numstat359.txt, cdiff359.txt,
  banddiff359.txt, py/c358base, build359/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
