# VERIFY-a69ef1d1 b439 T10P331 pins 131925..132272 (348 pins) PASS

Seat viewer-r67, first-hand, tree @a69ef1d1,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r67.
Base 7d7d1ea8 (b438 tip, 1968 tiers sealed; this
seat's VERIFY-7d7d1ea8 PASS-filed same round,
base-use only, respected). Band = e13e76d3 (py
merge w2b@d2ec961f partial, +6 tiers, +62 pins;
commit msg verified via git log) + a69ef1d1 (C
port; parent == e13e76d3 verified). Trees
manifest-identical to tips (git ls-tree vs git
ls-files cmp clean, 117/117 both; WT detached
at band, will return to lanes/encode-viewer at
round end).

Banked Next-P331 shape (r67 FWD-bank from A-871
Next-P331 forward note) CONSUMED FIRST and
corroborated EXACT: PB0 6db29605 NEW-sig 29/84
@131925 + PB1 09000000 NEW-sig 51/88 vs
n131578 @131926 + PBA88 b1000000 x16 @131927-
942 + C10-region 09000000 x10 @131943-952
SAME-as-PB1-sig -- all exact.

- Build: make -C WT/src/c BUILDDIR=$R/build439
  aae rgramc (absolute NVME path, flags -O2 -Wall
  -Wextra -std=c11 per Makefile), rc=0, 0
  warnings (log = 2 mkdir/cc command echoes
  only), build439/{aae,rgramc}. aae sha1
  7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues; band touches no aae sources),
  rgramc sha1 5c23eab5 / sha256 369ce60c (==
  GATE both).
- RGRAMC-PYID 9845/9845 covered=9845/9845 GREEN
  rc=0 (tests/test_rgramc_fast.py, RGRAMC=seat
  binary, CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19690/19690 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 19690/19690 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 19690/19690; cmp439.py; GATE claims
  sorted only, raw corroborated too).
- PINS 19692 rows (2 hdr + 19690, +62 vs base
  19628; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq439.py). For-list
  union delta vs base +31/-0 (9814->9845):
  131925 131926 131927 131928 131934 131935
  131941 131942 131943 131944 131947 131948
  131951 131952 131953 131967 131968 131969
  131977 131984 131985 132000 132001 132016
  132017 132095 132096 132145 132223 132224
  132272 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (131925/26) + A head pair 927/928 off0/1
  + 934/935 off7/8 + 941 off14 + tail 942 off15
  (6: offs 0,1,7,8,14,15) + C
  head pair 943/944 off0/1 + 947/948 off4/5 +
  951/952 off8/9 (6: offs 0,1,4,5,8,9; unsampled
  offs 2,3,6,7 = 945/946/949/950) + Q head 953
  off0 + B5EDGE pair 967/968 off14/15 (edge
  pair off15 shared with row0/1 boundary) +
  boundary pair 968/969 off15/16 + 984/985
  off31/32 + 2000/2001 off47/48 (Q 132000 =
  953+47, 132001 = 953+48) + row1-mid 977 off24
  (FIRST off24 mid + edge-carry, NEW shape) +
  tail 2016 off63 (10: offs 0,14,15,16,24,31,
  32,47,48,63) + R head 2017 off0 + edge pair
  2095/2096 off78/79 + mid 2145 off128 (1-mid
  shape) + edge pair 2223/2224 off206/207 +
  tail 2272 (7: offs 0,78/79,128,206/207,255;
  both counter edges pair-covered first-hand).
  31x2=62 rows, range 131925..132272 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
  PINS adds = same 31 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 31x2 = 62 =
  19690-19628.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit439.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 159 PASS 0 FAIL after 1 seat-script fix
  (VPOS-PBA-9 assert dropped the deducted-b5 -1;
  fixed, re-ran). Inventory exactly the 12 both
  sides, C==py (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/
  RQ/RC; no F/FT, no F0/F1, no BM/BC, no M19/
  X19, no QB/PT/FM, no M42/X42/H42/L42, no
  RT/TT, no QT). S0 168ch sig 6db29605 NEW
  (29/84 payload diff vs P330S0 @ 0-2,4-11,13,
  15,17-19,24,56-63,80-83 first-hand incl
  NEW-sig b0-2, NOT byte-equal; differs vs P330
  heads eed6f805/0b000000) / S1 176ch sig
  09000000 NEW (51/88 payload diff vs P330S1 @
  0,4,5,8-11,16-43,60-71,84-87 first-hand incl
  sig b0, NOT byte-equal; 26/88 diff vs own
  C10[0] staged cell0; sig SAME-as-own-C10;
  differs vs own PB0), staged as full-payload
  singletons. AM 16/16 16ch distinct (8B), CM
  10/10 10ch diverge (5B: b40 {9b x5 rows0-4,
  9c x5 rows5-9} first-hand, full sig b0-3 in
  CC), M 16/16 20ch distinct (10B, FIRST 10B
  per cport-r56 novelty log), QR 4/4 6ch
  distinct (3B R3 rows) UNPAIRED, RM 16/16 14ch
  distinct (7B TM7), RQ 16/16 18ch distinct (9B
  TR9) UNPAIRED, no QT (R3 carries b84-86
  inside QR rows) + no RT (ring, not ROWTAIL)
  + no F (no frags). AC 78, b0-3 b1000000 (b0
  const b1), no b4/b5. C10-1SIG-88-TAIL-M5b40
  sig 09000000 x10 SAME-as-PB1-sig (sig in CC
  b0-3 consts; CM 10/10 diverge, M5 b40,84-87;
  CC has no b4/b5, b5 const 06 full block via
  raw lencode). S1-vs-own-C10 staged per-cell
  (M5 b40,84-87 + b0-3 CC sig + b4/b5 lencode,
  each cell own assembly) [26]x10 TRUE UNIFORM,
  cells0-9 positions identical (cell0 @ 4,19,26,
  27,34-47,72-75,84-87 first-hand; oracle
  secf439c same vector), sig 09000000 both, NOT
  byte-equal -- 11th TRUE-uniform case in sweep
  accounting (after P299/P303/P307/P311/P315/
  P317/P319/P323/P325/P329); viewer record
  23->24 (23 excl P299).
  QUAD88-1SIG-4R-NOFRAG-B5EDGE-C87 1-sig
  b1000000 x64 SAME-sig-as-PBA: QM10 b30,31,38,
  39,46,47,80-83 M 16/16 shared NO frags (10B
  width verified first-hand) + R3 b84-86 rows
  r0 5e3c67 / r1 7e3c67 / r2 9e3c67 / r3 d77a8f
  exact tuples 4/4 NO pairing pairwise-unequal;
  tails b84-87 = row+c1: r012 TRUE 3B 3c67c1
  (@b85,86,87) + r3 shares 1B c1 (b87) with
  all; b87 CONST c1 quad-wide IN QC (FIRST
  const-b87-QC, FIRST R3 quad); TAIL4(+c1)
  suffix = TSHARE = subseq = 3/3/1/3/1/1
  (r012 pairs 3, r3 pairs 1; == A-1043 suffix-
  lcs at all 3 metrics, computed all three
  first-hand); ROW3-substr (3B rows w/o c1)
  r012=2 r3x=0; b0 const b1 in QC (1SIG, b5
  edge 06->07 @off14/15 exact in VPOS, edge
  131967->131968 r0c14/c15 first-hand); b4
  base 0xe3 step2 64/64 contig+2 range
  e3..ff,01..61; NO frags.
  R legs M[m] + QR[q] both sides, NO F-row leg,
  NO F-scalar leg; Q region m=off&15/q=off>>4.
  P331R(T88-ring STANDARD-split) 132017..
  132272 off=n-132017 c=off&15 r=off>>4 sig
  310b0000 x256; TM7 b52-54,80-83 by COL + TR9
  b40-42,46,47,76-79 by ROW UNPAIRED SPLIT
  tails (b80-83 col / b76-79 row, 16/16
  distinct each, 0 overlap UNPAIRED); b0 const
  31 ring-wide; b84-87 const 5137c211 ring-
  wide (bytes 51,37,c2,11); counter b4=
  (0x63+2off)&FF b5=0x07+(off>=79)+(off>=207)
  (py hex 0x63/0x07; C staged literals 99/7,
  re-derived: 99==0x63; edges off78/79 +
  off206/207 first-hand). R legs RM[c] + RQ[r]
  both sides, NO F anywhere in R. RM 16/16
  distinct + RQ 16/16 distinct.
  M==RQ TAILS4-ONLY (M 10B vs RQ 9B: agree
  (6,5),(7,6),(8,7),(9,8) 16/16 each = tails
  b80-83 cross-lane b76-79; heads disjoint
  (nontail max 4 at (1,1), rest <=2);
  full-row sets disjoint -- widths differ 10B/
  9B) -- 37th odd-band RQ==M instance (sweep
  column-agreement TAILS4-ONLY + cport full-row
  ORDERED-DISJOINT both true; width-equality
  predictor holds: mismatch => no full-row
  order; viewer chain b435-35th FULL8/b437-36th
  FULL6/b439-37th TAILS4-ONLY sequential).
  Tails STANDARD-split (RM b80-83 by COL
  c=off&15, RQ b76-79 by ROW r=off>>4, 16/16
  distinct each, 0 overlap UNPAIRED); M-tails
  16/16 ALL NEW vs P330T RM col-led tails
  (overlap 0); RM-tails (b80-83) ALL NEW vs
  P330T RM col-led tails (overlap 0; P330T
  COLSIG frame, ref = RM col-led 10B rows,
  position-aware).
  S0 string 29/84 differ vs P330S0 (NEW-sig
  incl b0-2) + S1 string 51/88 differ vs P330S1
  (incl sig b0; [26x10] vs own C10 TRUE
  UNIFORM -- new uniform case). P331 actuals
  (S0 6db29605/S1 09000000/PBA88 b1000000/C10
  09000000 x10 SAME-as-PB1-sig + PB0-vs-P330PB0
  29/84 + PB1-vs-P330PB1 51/88) == A-871
  predicted next EXACT.
  Missing-sets first-hand EXACT: AC-10
  [4,5,40-43,80-83] = b4,b5+M8 (b40-43,80-83;
  b5 const 06 deducted from AC) / CC-7
  [4,5,40,84-87] = b4,b5+M5 (b40,84-87, full
  sig b0-3 in CC = 09,00,00,00 -> 09000000 x10
  SAME-as-PB1-sig; b5 const 06 deducted) /
  QC-15 [4,5,30,31,38,39,46,47,80,81,82,83,
  84,85,86]
  = b4,b5+QM10 (b30,31,38,39,46,47,80-83)+R3
  (b84-86; b0 const b1 in QC = 1SIG, b87 CONST
  c1 in QC quad-wide) / RC-18 [4,5,40,41,42,
  46,47,52,53,54,76-83] = b4,b5+TR9 (b40-42,
  46,47,76-79)+TM7 (b52-54,80-83). PLAIN
  first-hand: AC b0-3 = b1,00,00,00 -> sig
  b1000000 x16, b0 const b1; AM 16/16
  distinct; b5 const 06. TAIL first-hand: CC
  b0-3 full sig 09000000 x10 SAME-as-PB1-sig
  (S1 sig-eq own C10); CM 10/10 diverge, b40
  {9b x5, 9c x5}; b5 const 06 full block.
  Code AC78/CC81/QC73/RC70; incl = +1/+1/+0/+0
  (A b5 const 06, C b5 const 06, Q b5 EDGE
  06->07 exact, T counter) = 79/82/73/70;
  lane consts = A-872 INCL EXACT (deduct-b5-
  only-when-b5vary rule holds; writer
  CORRECTION quad 71->73 verified: 73 = 88-15
  first-hand; A-1043 excl 78/81/73/70 = code
  EXACT -- no lag on odd band). Sorted-unique
  + _N decls 78/81/73/70 match actual.
  Coverage unions exact every block (const U
  tab U lencode == 88 x4, 0 overlap; each
  missing == region pay-index set minus
  lencode EXACT all 4 (A/C/Q/R region text
  re-derived; Q b0 via QC loop both sides)).
  Base temp maxes _t6748/_b4084/_i4085 (no
  reuse: band adds _t6749-6764 continuous-16 +
  _i4087/89/92/95 + _b4086/88/90/91/93/94,
  whole-file max _t6764, all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 131925 / S1 131926 / A 131927-942 /
  C 131943-952 / Q 131953-2016 / R 132017-272):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A b5 const 06, C b5
  const 06, Q b5=06+(off>=15); A/C/Q use raw
  lencode, no counter literals anywhere A/C/Q)
  + R explicit counter (b4=(0x63+2off)&FF b5=
  0x07+(off>=79)+(off>=207); py hex 0x63/0x07;
  C staged literals 99/7, re-derived:
  99==0x63) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 8B b40-43,80-83; C 5B
  b40,84-87; Q 10B/3B; R 7B/9B STANDARD
  tails-split). C blocks carry T88642/88647/
  88652/88667/88682/88702 py-line mirrors (all
  6 re-read verbatim against the py guard lines
  above); bounds + byte positions exact. Insert
  exact both sides: after T10P330R close (py
  CLOSED-then-guard; C block follows P330R
  close, P331 blocks follow), at dispatch tail
  (N-out-of-scope fallthrough follows: C + py
  scope hits; early same-text guards unrelated
  scope). Matches A-872 geometry (values re-
  checked in audit above; NO D dips: ownloop
  tags exactly the 6 P331 blocks).
- Edges own-loop ownloop439.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  b439 tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P331R N=132272 off=255.
  edges439.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  ab/06, ad/06 == raw lencode) + aform 16/16 (A
  head af/06 tail cd/06 b5set {06} NO step, 0
  ff) + cform 10/10 (C head cf/06 tail e1/06
  b5set {06} NO step, 0 ff) + qform 64/64 +
  qb5edge 64/64 (Q head e3/06 edge off14->15
  131967 ff/06 -> 131968 01/07 tail 61/07 b4
  base 0xe3 step2 64/64 contig+2 range
  e3..ff,01..61 b5set {06,07} (06 offs 0-14,
  07 offs 15-63), exactly 1 ff in 64) + ring
  counter 256/256 + ringraw 256/256 (head
  63/07; 132095 off78 ff/07 -> 132096 off79
  01/08; mid off128 63/08 @132145; 132223
  off206 ff/08 -> 132224 off207 01/09; tail
  off255 61/09; exactly 2 ff in 256). S0/S1
  embedded b4/b5 (ab/06, ad/06) match raw
  lencode. Odd-lencode 348/348 (346 + S0/S1
  embedded). Ring edges + mid + tail 132272 in
  for-list + 2 PASS lines each py+C. Tail
  132272: oracle rav sha 2242fc3824d03207...
  == PINS (match True prefix; rawlen 104 re-
  checked); py+C CLOSED T10P331R off=255 agree.
  No DISSENT: cut bytes verify.
- PB-diff secf439.py (cache path, 0 miss-warmed
  after ownloop) + secf439b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (131925 +
  131577 + 131926 + 131578); S0: oracle131925-
  vs-131577 29/84, codeS0-vs-P330S0 29/84,
  positions identical (differ-pos 0-2,4-11,13,
  15,17-19,24,56-63,80-83 listed); DIRECT
  29/84 agree. S1: oracle131926-vs-131578
  51/88, codeS1-vs-P330S1 51/88, positions
  identical (differ-pos 0,4,5,8-11,16-43,60-71,
  84-87 listed); DIRECT 51/88 agree. Triple-
  derived both pairs (same novel shape both
  tiers: 84/84/84/84 + 88/88/88/88). S1-vs-own-
  C10 secf439c.py (oracle C10 cells n131943-
  952): [26]x10 TRUE UNIFORM staged+oracle,
  cells0-9 positions identical (cell0 pos 4,19,
  26,27,34-47,72-75,84-87 == staged EXACT),
  sig 09000000 both, NOT byte-equal. UNIFORM --
  new case (record 23->24). Byte-diff
  discipline observed throughout.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  231/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw C
  608 total = 603 content + 5 bare-blank / 0
  del (verified bare `+` lines; GATE states
  "608 content + 5 blank-only" which sums 613
  vs numstat 608?? -- first-hand: 603 content
  + 5 bare-blank = 608 total == numstat. full-
  digit norm (rgramc.c scope): C del-uniq 0 all
  4 variants, add-uniq 166/163/165/162 (162 =
  strip+dropempty), missing 0 every variant; py
  del-uniq 0 add-uniq 186 x4, missing 0
  (integrity intact, variant-robust); C-
  tempnorm del-uniq 0 add-uniq 404 missing 0 /
  py-tempnorm add-uniq 200 recorded. Band-level
  sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope 7d7d1ea8..
  a69ef1d1, 902 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 231/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1874->1880 +6, singletons
  `if n == ` 694->696 +2 (unanchored; 4sp
  684->686 +2) / range-guards `<= n <=`
  776->780 +4 (unanch and 4sp 754->758 +4) = +6
  py (== GATE deltas); C guards: singleton `if
  ((n) == (` 689->691 +2 / range 776->780 +4
  (5-count C-vs-py singleton offset pre-
  existing, unchanged: 696-691 = 694-689 = 5),
  CLOSED T10P prints 1874->1880 +6 py +
  1874->1880 +6 C (seal 1968->1974 +6; offset
  +94 vs CLOSED-T10P: 1974-1880 = 94, stable
  b401-b439). All agree (stated literal methods
  first-hand; deltas agree every method;
  viewer-vs-sweep absolute convention
  reconciled). Deliberate structural add: none
  (no elif either side: py elif 50->50 pre-
  existing, C else-if 0->0; A/C/Q use raw
  lencode, no counter literals).
- CONFIRM evidence (CONVERT-01 rule b): A-872-
  q1043 verdict CONFIRM 63/63 CLEAN (own bed
  r3-P331 131925..132304 BAD=0 + own r3-P330,
  verifier v258.py 63/63 PASS; tier GATED PORT;
  novelties FIRST R3 quad + r012 TRUE 3B tail-
  share gated; writer CORRECTION quad 71->73
  verified 73 = 88-15 first-hand; section Q1/
  Q2/Q3 all CONFIRM, no gloss issue this tier;
  exact-value corroboration incl PB0 6db29605
  NEW 29/84 + PB1 09000000 NEW 51/88 +
  SAME-as-own-C10 26/88 + PBA88-PLAIN-M8b40
  VPOS 9 b5 const 06 + C10-1SIG-88-TAIL-M5b40
  VPOS 6 b5 const 06 b40-{9b,9c} + QUAD88-1SIG-
  4R-NOFRAG-B5EDGE-C87 1-sig-b1 SAME-as-PBA +
  R3 4/4 + r012-TRUE3 + r3-1B + b87-const-c1 +
  b0-const-b1 + B5EDGE-14/15 + M-tails ALL NEW
  16/16, T88-RING-STANDARD + TM7-by-COL + TR9-
  by-ROW + b84-87 5137c211 + counter + edges;
  sheet INCL PBA 79 / C10 82 / quad 73 / T88
  70) + A-1043-q1043 verdict CONFIRM 47/47
  CLEAN (own bed r6-P331 131925..132300 + r6-
  P330, BAD=0 + verifier v600f3.py 47/47 PASS;
  suffix-lcs 3/3/1/3/1/1 at all 3 metrics
  (computed suffix+subseq+substr first-hand) +
  M-tails NEW + SPLIT
  tails EXACT + consts excl 78/81/73/70
  script-claimed corroborated; file present,
  counts verified; tier GATED PORT). Agrees
  with cport commit msg (PYID 9845, RGRAM
  19690). No viewer P331 geometry answer on
  file at gate time (memo-only recon; this
  VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b439
  (own seat CLAIM only; exactly 1 GATE-a69ef1d1;
  zero FLAG hits; even base b438 respected;
  b440+ = future turf, untouched, used as
  nothing here). PROSE-01: all hex/counts above
  copied from own run output; GATE-a69ef1d1
  re-read in FULL before filing (1 mild prose
  note below, substance exact).
- RQ==M chain: b439 odd TAILS4-ONLY (M 10B vs
  RQ 9B; tails (6,5),(7,6),(8,7),(9,8) 16/16;
  heads disjoint; full-row sets disjoint).
  37th odd-band instance (viewer chain b435-35th
  FULL8/b437-36th FULL6/b439-37th TAILS4-ONLY
  sequential; width-equality predictor holds).
  Memo-silent on the relation; batteries
  confirm; tier stands.
- TRUE-uniform chain: b439 UNIFORM [26]x10
  SAMESIG (staged+oracle, positions identical).
  Record 23->24 (23 excl P299). FIRST R3-quad
  uniform (tails row+c1).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 1 mild GATE prose note (raw-C
"608 content + 5 blank" overcounts by 5: first-
hand 608 total = 603 content + 5 bare-blank --
same token as b429/b431/b433/b435/b437 GATEs,
6th instance; code GREEN since gated artifact ==
verified artifact).
