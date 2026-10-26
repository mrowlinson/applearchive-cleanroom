# VERIFY-7d7d1ea8 b438 T10P330 pins 131577..131924 (348 pins) PASS

Seat viewer-r67, first-hand, tree @7d7d1ea8,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r67.
Base 3c686253 (b437 tip, 1962 tiers sealed; this
seat's VERIFY-3c686253 PASS-filed same round,
base-use only, respected). Band = 8c1a747b (py
merge w2b@0682e6ac partial, +6 tiers, +62 pins;
commit msg verified via git log) + 7d7d1ea8 (C
port; parent == 8c1a747b verified). Trees
manifest-identical to tips (git ls-tree vs git
ls-files cmp clean, 117/117 both; WT detached
at band, will return to lanes/encode-viewer at
round end).

Banked Next-P330 shape (r67 FWD-bank from A-870
Next-P330 forward note) CONSUMED FIRST and
corroborated EXACT: PB0 eed6f805 SAME-sig-as-
P329PB0 33/84 @131577 + PB1 0b000000 sig-eq-
P329PB1 59/88 @131578 + PBA88 be000000 x16
@131579-594 + C10-region 0b000000 x10 @131595-
604 SAME-as-PB1-sig -- all exact.

- Build: make -C WT/src/c BUILDDIR=$R/build438
  aae rgramc (absolute NVME path, flags -O2 -Wall
  -Wextra -std=c11 per Makefile), rc=0, 0
  warnings (log = 2 mkdir/cc command echoes
  only), build438/{aae,rgramc}. aae sha1
  7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues; band touches no aae sources),
  rgramc sha256 c88f00de (== GATE; sha1
  88cb47a9 recorded, GATE states sha256 only).
- RGRAMC-PYID 9814/9814 covered=9814/9814 GREEN
  rc=0 (tests/test_rgramc_fast.py, RGRAMC=seat
  binary, CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19628/19628 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 19628/19628 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 19628/19628; cmp438.py; GATE claims
  ordered + raw identical too, both corroborated).
- PINS 19630 rows (2 hdr + 19628, +62 vs base
  19568; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq438.py). For-list
  union delta vs base +31/-0 (9783->9814):
  131577 131578 131579 131580 131583 131584
  131587 131594 131595 131596 131599 131600
  131603 131604 131605 131613 131620 131621
  131636 131637 131652 131653 131661 131668
  131669 131711 131712 131797 131839 131840
  131924 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (131577/78) + A head pair 579/580 off0/1
  + STEP edge pair 583/584 pinned off4/5 + mid
  587 off8 + tail 594 off15 (6: offs 0,1,4,5,8,
  15) + C head pair 595/596 + mid pair 599/600
  + tail pair 603/604 (6) + Q head 605 off0 +
  off8 613 + row-boundary pairs 620/621 off15/
  16 + 636/637 off31/32 + 652/653 off47/48 SIG-
  boundary + off56 661 + tail 668 (10: offs 0,8,
  15,16,31,32,47,48,56,63) + R head 669 off0 +
  edge pair 711/712 off42/43 + mid 797 off128 +
  edge pair 839/840 off170/171 + tail 924 (7:
  offs 0,42/43,128,170/171,255; both counter
  edges pair-covered first-hand). 31x2=62
  rows, range 131577..131924 exact. PINS-new-N
  == for-added 31/31, PINS removed 0. PINS
  numstat 62/0 clean append (all in py-merge leg;
  C-port leg touched zero PINS rows); cols1-4
  purity +62/-0, cols5-7 unchanged (test_rgram_
  fast.py/27.0.1/ct-lzraven uniform both --
  filename/tooling cited as GATE states).
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit438.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 170 PASS 0 FAIL first run (no seat-script
  fixes, no GATE prose slips). Inventory exactly
  the 12 both sides, C==py (S0/S1/AM/AC/CM/CC/
  M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1, no BM/BC,
  no M19/X19, no QB/PT/FM, no M42/X42/H42/L42,
  no RT/TT, no QT). S0 168ch sig eed6f805
  sig-eq-P329PB0 (33/84 payload diff vs P329S0
  @ 4,5,32-35,37-55,72-79 first-hand, NOT byte-
  equal; differs vs P329 C10 heads) / S1 176ch
  sig 0b000000 sig-eq-P329PB1 (59/88 payload
  diff vs P329S1 @ 4-7,9-14,16-25,28-31,36-43,
  45-59,76-87 first-hand, NOT byte-equal; 30/88
  diff vs own C10[0] staged cell0; sig SAME-as-
  own-C10; differs vs own PB0), staged as full-
  payload singletons. AM 16/16 12ch distinct,
  CM 10/10 8ch diverge (first bytes 10/10
  distinct, b84-87 tails-only M4), M 16/16 16ch
  distinct, QR 4/4 30ch distinct (R15) UNPAIRED,
  RM 16/16 20ch distinct (TM10), RQ 16/16 16ch
  distinct (TR8) UNPAIRED, no QT (quad tails in
  QR rows R15) + no RT (COLSIG tails) + no F (no
  frags). AC 80, b0-3 be000000 (b0 const be),
  no b4/b5. C10-1SIG-88-TAIL sig 0b000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM
  10/10 diverge 8ch b84-87; CC has no b4/b5, b5
  const 04 full block via raw lencode). S1-vs-
  own-C10 staged per-cell (M4 b84-87 + b0-3 CC
  sig + b4/b5 lencode, each cell own assembly)
  [30]x10 TRUE UNIFORM, cells0-9 positions
  identical (cell0 @ 4,5,8-11,16-31,60-63,84-87
  first-hand; oracle secf438c same vector),
  sig 0b000000 both, NOT byte-equal -- new TRUE-
  uniform case (GATE checks cell0 only; viewer
  record 22->23, 22 excl P299; SAMESIG).
  QUAD88-2SIG-4R-NOFRAG be000000 x48 (rows0-2)
  SAME-sig-as-PBA + 5f000000 x16 (row3): 2-sig
  rows (b0 row-led in tab: be/be/be/5f, QC has
  no b0, b0 in R lanes both sides); QM8 b28-31,
  80-83 M 16/16 shared NO frags + R15 b0,11,19,
  20-27,84-87 rows 4/4 NO pairing pairwise-
  unequal (r0 beb483b9dd9c18343c06decebdaa11 /
  r1 beb483b9dd9c18343c06deeebdaa11 share 11B
  prefix beb483b9dd9c18343c06de, differ at b84
  (ce/ee/46 all distinct, 3 distinct tail
  tuples); r2 beb483b9dd9c18343c06de466ee62c
  same 11B prefix; code comments py + C still
  say "12B prefix" -- seat confirms first-hand
  the shared prefix is exactly 11B (12th byte
  ce/ee/46 all distinct), comment-gloss only
  both sides asserted present, bytes unaffected
  (matches A-871 §F + GATE Matches note); r3
  5f34c1885b5b5a1388f6efd2f15f5b fully
  distinct; tails b84-87 4 distinct cebdaa11/
  eebdaa11/466ee62c/d2f15f5b, r01 TRUE-3B
  bdaa11 suffix, r2/r3 tail-LCS 0 vs all
  (suffix+subseq+substr all 0); full-row
  longest-common-substring 01=11 02=11 03=1
  12=11 13=1 23=1 (substring convention
  verified: prefix gives 11/11/0/11/0/0, the r3x
  1s are single-shared-byte; GATE "full-LCS"
  == substring, consistent with b437 FULL-
  substr usage); b87 [11,11,2c,5b] NOT const,
  set {11,2c,5b}).
  R legs M[m] + QR[q] both sides, NO F-row leg,
  NO F-scalar leg; Q region m=off&15/q=off>>4.
  P330R(T88-ring COLSIG) 131669..131924 off=
  n-131669 c=off&15 r=off>>4, sigs 88040000
  c0-6 + 8e040000 c7-15 EVERY row (b0 col-led:
  RM b0 = 88 x7 cols0-6 / 8e x9 cols7-15
  first-hand); TM10 b0,11,19,27,34,35,80-83 by
  COL (b0 in TM10, col-led) + TR8 b28-31,76-79
  by ROW UNPAIRED SPLIT tails (b80-83 col /
  b76-79 row, 16/16 distinct each, 0 overlap
  UNPAIRED); b1 const 04 ring-wide; b84-87
  const 8fed394b ring-wide NEW; counter b4=
  (0xab+2off)&FF b5=0x04+(off>=43)+(off>=171)
  (py hex 0xab/0x04; C staged literals 171/4,
  re-derived: 171==0xab; edges off42/43 +
  off170/171 first-hand). R legs RM[c] + RQ[r]
  both sides, NO F anywhere in R. RM 16/16
  distinct + RQ 16/16 distinct.
  M==RQ FULL 16/16 string-identical INTRA-tier:
  set-eq True AND ordered-eq True (matrices:
  diag-16 all 8 lanes; off-diag (6,7)=(7,6)=1
  = intra-row byte coincidence only); payload
  positions DIFFER (QM8 b28-31,80-83 vs TR8
  b28-31,76-79 slots, verified in region code
  both sides) -- 37th even-band RQ==M instance,
  class string-eq-positions-differ (viewer chain
  b434 FULL-eq-positions-identical / b436
  string-eq-positions-differ / b438 string-eq-
  positions-differ sequential; sweep GATE
  running pattern lists b438 the same;
  reconciled first-hand: tables ordered-
  identical, payload slots split). Tails SPLIT
  (RM b80-83 by COL c=off&15, RQ b76-79 by ROW
  r=off>>4, 16/16 distinct each, 0 overlap
  UNPAIRED); M-tails 16/16 ALL NEW vs P329
  (vs P329M/RM/RQ tails 0 overlap); RM-tails
  ALL NEW vs P329RM; RQ-tails NEW vs P329RQ;
  cross overlaps 0 (P329T STANDARD-split frame,
  position-aware).
  S0 string 33/84 differ vs P329S0 (sig-eq
  P329PB0) + S1 string 59/88 differ vs P329S1
  (sig-eq P329PB1; [30x10] vs own C10 TRUE
  UNIFORM -- new uniform case). P330 actuals
  (S0 eed6f805/S1 0b000000/PBA88 be000000/C10
  0b000000 x10 SAME-as-PB1-sig + PB0-vs-P329PB0
  33/84 + PB1-vs-P329PB1 59/88) == A-870
  predicted shape EXACT (A-871 + A-1042 agree;
  bank-consumption clean).
  Missing-sets first-hand EXACT: AC-8
  [4,5,20,21,80-83] = b4,b5+M6 (b20,21,80-83;
  b5 STEP 03->04 @off5 in VPOS via raw
  lencode) / CC-6 [4,5,84-87] = b4,b5+M4
  (b84-87 tails-only, full sig b0-3 in CC =
  0b,00,00,00 -> 0b000000 x10 SAME-as-PB1-sig)
  / QC-25 [0,4,5,11,19,20,21,22,23,24,25,26,
  27,28,29,30,31,80,81,82,83,84,85,86,87] =
  b4,b5+QM8
  (b28-31,80-83)+R15 (b0,11,19,20-27,84-87;
  b0 in R15, counted once; b5 const 04
  deducted from QC) / RC-20 [0,4,5,11,19,27,
  28-31,34,35,76-83] = b0,b4,b5+TM10 (b0,11,
  19,27,34,35,80-83)+TR8 (b28-31,76-79).
  PLAIN first-hand: AC b0-3 = be,00,00,00 ->
  sig be000000 x16, b0 const be; AM 16/16
  distinct; b5 STEP. COLSIG first-hand: TM10
  b0-led 88x7/8ex9; b1 const 04 ring-wide;
  b84-87 8fed394b. AC-QC both=63 sameval=49
  (63 common bytes / 49 same value, NOT set-
  intersection -- computed first-hand, ==
  GATE; prose-level corroboration).
  Code AC80/CC82/QC63/RC68; incl = +0/+1/+1/+0
  (A b5 STEP-varies in VPOS memo-exact, C b5
  const 04, Q b5 const 04, T counter) =
  80/83/64/68; lane consts = A-871 INCL EXACT
  (deduct-b5-only-when-b5vary rule holds;
  C10/quad lag this tier: 32nd consecutive S-F
  tables-lag + 14th even-band C10/quad-lag per
  GATE running counts; memo-exact on PBA (b5
  STEP-varies, in VPOS) and T88 (b5 counter-
  varies, no deduction); geometry exact, PORT
  verdict stands). Sorted-unique + _N decls
  80/82/63/68 match actual. Coverage unions
  exact every block (const U tab U lencode/b0
  == 88 x4, 0 overlap; each missing == region
  pay-index set minus lencode/b0 EXACT all 4
  (A/C/Q/R region text re-derived; Q b0 via R
  lanes both sides)). Base temp maxes _t6732/
  _b4074/_i4075 (no reuse: band adds
  _t6733-6748 continuous-16 + _i4077/79/82/85
  + _b4076/78/80/81/83/84, whole-file max
  _t6748, all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 131577 / S1 131578 / A 131579-594 /
  C 131595-604 / Q 131605-668 / R 131669-924):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A b5 STEP 03->04 @off5
  emerges from raw lencode, C b5 const 04, Q b5
  const 04; A/C/Q use raw lencode, no counter
  literals anywhere A/C/Q) + R explicit counter
  (b4=(0xab+2off)&FF b5=0x04+(off>=43)+
  (off>=171); py hex 0xab/0x04; C staged
  literals 171/4, re-derived: 171==0xab) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A M6
  b20,21,80-83 12ch; C M4 b84-87 8ch; Q QM8
  b28-31,80-83 + R15 b0,11,19,20-27,84-87
  16/30ch; R TM10 b0,11,19,27,34,35,80-83 20ch
  by COL (code-RM10) + TR8 b28-31,76-79 16ch
  by ROW (code-RQ8), tails SPLIT). C blocks
  carry T88408/88413/88418/88433/88448/88470
  py-line mirrors (all 6 re-read verbatim
  against the py guard lines above); bounds +
  byte positions exact. Insert exact both
  sides: after T10P329R close (py CLOSED 88406,
  return 88407, guard 88408; C 235182-84,
  comment 235185, block 235186), at dispatch
  tail (N-out-of-scope fallthrough follows: C
  235377, py 88490; early same-text guards at C
  158475 / py 54601 are the T4-plateau-B n<=
  1077 check, unrelated scope). Matches A-871
  geometry (values re-checked in audit above;
  NO D dips: ownloop tags exactly the 6 P330
  blocks).
- Edges own-loop ownloop438.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  b438 tier fully cache-warm from sweep2 leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P330R N=131924 off=255.
  edges438.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  f3/03, f5/03 == raw lencode) + aform 16/16 (A
  head f7/03 STEP 131583 off4 ff/03 -> 131584
  off5 01/04 tail 15/04, exactly 1 ff in 16;
  b4 base 0xf7 step2 16/16; b5set {03,04}) +
  cform 10/10 (C head 17/04 tail 29/04 b5set
  {04} NO step, 0 ff) + qform 64/64 + qb5const
  64/64 (Q head 2b/04 tail a9/04 b4 base 0x2b
  step2 64/64 range 2b..a9 b5set {04} NO step,
  NO edge, 0 ff in 64) + ring counter 256/256
  + ringraw 256/256 (head ab/04; 131711 off42
  ff/04 -> 131712 off43 01/05; mid off128
  ab/05 @131797; 131839 off170 ff/05 -> 131840
  off171 01/06; tail off255 a9/06; exactly 2
  ff in 256; Q tail a9/04 vs R tail a9/06
  differ in b5 -- labeled apart). S0/S1
  embedded b4/b5 (f3/03, f5/03) match raw
  lencode. Odd-lencode 348/348 (346 + S0/S1
  embedded). Ring edges + mid + tail 131924 in
  for-list + 2 PASS lines each py+C. Tail
  131924: oracle rav sha matches PINS (match
  True; rawlen 104 re-checked); py+C CLOSED
  T10P330R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf438.py (cache path, 0 miss-warmed
  after ownloop) + secf438b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (131577 +
  131229 + 131578 + 131230); S0: oracle131577-
  vs-131229 33/84, codeS0-vs-P329S0 33/84,
  positions identical (differ-pos 4,5,32-35,
  37-55,72-79 listed); DIRECT 33/84 agree. S1:
  oracle131578-vs-131230 59/88, codeS1-vs-
  P329S1 59/88, positions identical (differ-pos
  4-7,9-14,16-25,28-31,36-43,45-59,76-87
  listed); DIRECT 59/88 agree. Triple-derived
  both pairs (same novel shape both tiers:
  84/84/84/84 + 88/88/88/88). S1-vs-own-C10
  secf438c.py (oracle C10 cells n131595-604):
  [30]x10 TRUE UNIFORM staged+oracle, cells0-9
  positions identical (cell0 pos 4,5,8-11,16-
  31,60-63,84-87 == staged EXACT), sig
  0b000000 both, NOT byte-equal. UNIFORM -- new
  case (record 22->23). Byte-diff discipline
  observed throughout.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  233/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw C
  608 total = 603 content + 5 bare-blank / 0
  del (verified bare `+` lines; GATE states
  "603 content + 5 bare-blank" EXACT -- class
  clean this band; total overcount instances
  stay at 5). full-digit norm (rgramc.c scope):
  C del-uniq 0 all 4 variants, add-uniq 151/
  148/150/147 (147 = strip+dropempty), missing
  0 every variant; py del-uniq 0 add-uniq 175
  x4, missing 0 (integrity intact, variant-
  robust); C-tempnorm del-uniq 0 add-uniq 380
  missing 0 / py-tempnorm add-uniq 192
  recorded. Band-level sole del = old for-line
  churn (1/1).
- Wall on band diff added lines (scope 3c686253..
  7d7d1ea8, 904 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 233/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks,
  tier-comments `# T10P` 1868->1874 +6,
  singletons `if n == ` 692->694 +2 (unanchored;
  4sp 682->684 +2) / range-guards `<= n <=`
  772->776 +4 (unanch and 4sp 750->754 +4) = +6
  py (== GATE deltas); C guards: singleton `if
  ((n) == (` 687->689 +2 / range 772->776 +4
  (5-count C-vs-py singleton offset pre-
  existing, unchanged: 694-689 = 692-687 = 5),
  CLOSED T10P prints 1868->1874 +6 py +
  1868->1874 +6 C (seal 1962->1968 +6; offset
  +94 vs CLOSED-T10P: 1968-1874 = 94, stable
  b401-b438). All agree (stated literal methods
  first-hand; deltas agree every method;
  viewer-vs-sweep absolute convention
  reconciled: GATE states 4-space dispatch-
  exact, unanchored corroborates). Deliberate
  structural add: none (no elif either side:
  py elif 50->50 pre-existing, C else-if 0->0;
  A/C/Q use raw lencode, no counter literals).
- CONFIRM evidence (CONVERT-01 rule b): A-871-
  q1042 verdict CONFIRM 65/66 + section-F (own
  bed r3-P330 131577..131956 BAD=0 + own r3-
  P329, verifier v257.py 65/66 PASS, single
  FAIL = Q-claim witness: r0/r1/r2 share 11B
  prefix (all non-tail b0,11,19,20-27), differ
  at b84 (ce/ee/46 all distinct) -- Q claimed
  12B; writer corrects prefix gloss, no table
  impact; seat finds gloss still "12B" in
  committed py+C comments; file present,
  counts verified; novelty COLSIG T-ring gated;
  exact-value corroboration incl PB0 sig-eq-
  P329PB0 33/84, PB1 sig-eq-P329PB1 59/88
  SAME-as-own-C10 30/88, PBA88-STEP-M6b20
  sig-be M6 16/16 NO pair, C10-1SIG-88-TAIL
  SAME-as-PB1-sig M4 10/10 diverge, QUAD88-
  2SIG-4R-NOFRAG bex48-rows0-2-SAME-as-PBA +
  5f-row3 + R15 rows + r012-share-11B + b84-
  ce/ee/46 + r01-TRUE-3B + r2/r3-lcs0 + b87-
  {11,2c,5b} + QM8 + NO frags + b5-const-04 +
  M-tails NEW, T88-RING-COLSIG + TM10-by-COL/
  b0-led + TR8-by-ROW + b1-04 + b84-87 8fed394b
  + counter + edges; sheet INCL PBA 80 / C10 83
  / quad 64 / T88 68; section Q1/Q2/Q3 all
  CONFIRM) + A-1042-q1042 verdict CONFIRM 47/47
  CLEAN (own bed r6-P330 131577..131952 + r6-
  P329, BAD=0 + direct-oracle 2/2 byte-match,
  verifier v600f3.py 47/47 PASS; suffix-lcs
  3/0/0/0/0/0 + M-tails NEW + b0-COLSPLIT
  112+144 + consts excl 80/82/63/68 script-
  claimed corroborated; file present, counts
  verified; tier GATED PORT). Agrees with cport
  commit msg (PYID 9814, RGRAM 19628). No
  viewer P330 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b438
  (own seat CLAIM only; exactly 1 GATE-7d7d1ea8;
  zero FLAG hits; odd base b437 respected;
  b439+ = future turf, untouched except A-871
  Next-P331 forward note banked below, used as
  nothing here). PROSE-01: all hex/counts above
  copied from own run output; GATE-7d7d1ea8
  re-read in FULL before filing (substance
  exact, no prose notes on code/behavior legs
  this band).
- RQ==M chain: b438 even FULL 16/16 string-
  identical INTRA-tier (set-eq True, ordered-eq
  True, diag-16 all 8 lanes; off-diag (6,7)=
  (7,6)=1 intra-row coincidence only). 37th
  even-band instance (viewer chain b434-FULL-
  eq-positions-identical/b436-string-eq-
  positions-differ/b438-string-eq-positions-
  differ sequential). Payload positions DIFFER
  (QM8 b80-83 vs TR8 b76-79). Memo-silent on
  the relation; batteries confirm; tier stands.
- TRUE-uniform chain: b438 UNIFORM [30]x10
  SAMESIG (staged+oracle, positions identical).
  Record 22->23 (22 excl P299).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; zero prose notes this band (raw-C
token stated correctly; full-LCS/substr/suffix
conventions all exact; stale-12B comment already
documented by memo + GATE).
FWD-bank for r68 (consume-first): A-871 Next
P331 -- PB0 6db29605 NEW-sig 29/84 @131925 +
PB1 09000000 NEW-sig 51/88 vs n131578 @131926 +
PBA88 b1000000 x16 @131927-942 + C10 09000000
x10 @131943-952 SAME-as-PB1-sig.
