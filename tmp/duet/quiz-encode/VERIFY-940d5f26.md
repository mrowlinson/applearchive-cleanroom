# VERIFY-940d5f26 b481 T10P373 pins 146541..146888 (348 pins) PASS

Seat viewer-r78, first-hand, tree @940d5f26,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r78.
Base da1ea8de (b480 tip, 2220 tiers sealed; this
seat's VERIFY-da1ea8de PASS-filed same round,
base-use only, respected). Band = 85d0148d (py
merge w2b@bbedd165 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 940d5f26 (C
port; parent == 85d0148d verified via git
rev-list --parents). Chain da1ea8de -> 85d0148d
-> 940d5f26, every sha via git log at takeover,
NO gap-jump. GATE-940d5f26 PASS-functional filed
by sweep-r82 -- reconciled first-hand below
(values agree; tier-count patterns + tail-metric
span + RQ==M ledger degree phrasing differ,
code facts identical). NO other GATE/FLAG on
b481 at file time.

Banked Next-P373 shape (Q-1120 forward note,
read first-hand) CONSUMED FIRST and VERIFIED
first-hand EXACT vs Q-1121/A-956: PB0
ef171613 @146541 (S0 head; NEW-sig 39/84 vs
P372PB0 @ n146193, sig b3 IN diff with b0-2
same, positions
[3-11,20,21,24-27,34,35,41-48,50-55,76-83]
first-hand, NOT byte-equal) + PB1 26000000
@146542 (S1 head; NEW-sig 68/88 vs
P372PB1 @ n146194, sig b0 IN diff with b1-3
same, positions
[0,4-27,36-38,40-43,48-55,60-83,84-87]
first-hand, NOT byte-equal; diffs vs own C10
cells 24x2 (cells 0,5) + 25x8 first-hand
(B5EDGE: cell-0 b5-match, cells-1-9 b5-diff;
cell-5 CM-b84 01-match offsets its b5-diff;
sig b0-3 same-sig NOT in diff; S1 SIG-EQ own
C10 (26==26); S1 SIG-DIFFERS own PB0 (26-vs-62)
and PBA sig (26-vs-62); C10 10/10 DIVERGE
staged+oracle: 39 stays (odd band): NOT TRUE-
UNIFORM under viewer convention (uniform-cells
required); P338 uniform-rule dispute stays
DEFERRED to sweep accounting, never
re-litigated) + PBA88-PLAIN-M8b28 sig
62020000 x16 @146543-558 (b0 const 0x62
first-hand) + C10-region 26000000 pay88 x10
@146559-568 (b0 const 0x26 first-hand,
SAME-as-PB1-sig) -- all corroborated against
lane code both sides plus Q-1121/A-956 before
any battery step (py==C S0/S1 staged strings;
staged-vs-oracle secf481a/b/c GREEN first-run;
no bank-miss).

- Build: seat-private build481/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 fd4b990d...
  (= GATE rgramc fd4b990d independent
  corroboration; no GATE absolutes cited --
  recorded first-hand here, never
  hand-transcribed).
- RGRAMC-PYID 11090/11090 covered=11090/11090
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch;
  +29 vs b480 11061).
- RGRAM py 22180/22180 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 22180/22180 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (22180/22180, sorted +
  raw identical; cmp481.py GREEN).
- PINS-RGRAM cells set-eq 22180/22180 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq481.py GREEN). PINS 22182 lines
  first-hand (2 hdr + 22180 rows; base 22124
  lines / 22122 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 11061->11090 +29/-0 (python
  sets, trailing-';' strip, never comm): 146541
  146542 146543 146544 146550 146551 146557
  146558 146559 146560 146563 146564 146567
  146568 146569 146584 146585 146600 146601
  146616 146632 146633 146687 146688 146752
  146815 146816 146817 146888 (= GATE 29-set
  exact, first-hand both sides; range
  146541..146888 exact).
  29 = 2 sing (146541 146542 offs 0/1) + A 6
  (head pair 146543/146544 off0/1 + mid pair
  146550/146551 off7/8 + tail pair 146557/
  146558 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 78 NO
  edge) + C 6 (head B5EDGE pair 146559/146560
  off0/1 + mid pair 146563/146564 off4/5 + tail
  pair 146567/146568 off8/9; offs 2,3,6,7
  unsampled first-hand; B5EDGE off0->1 pair-
  covered, head pair IS the edge) + Q 7 (head
  146569 off0 + row-boundary pairs 146584/
  146585 off15/16 + 146600/146601 off31/32 +
  mid 146616 off47 + tail 146632 off63; BOTH
  boundaries pair-covered (differs from b479
  single-sided @32); b5 const 79 NO edge) + R 8
  (head 146633 off0 + edge pair 146687/146688
  off54/55 + mid 146752 off119 + edge pair
  146815/146816 off182/183 + mate 146817
  off184 + tail 146888 off255; both counter
  edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  22180-22122.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit481.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 187 PASS 0 FAIL (after 3 own-script
  fixes: C10 M2->M4 lanes, CNQ/CNR base-block
  pointers, C-tail window; tree untouched).
  Inventory: exactly the 12 band tables both
  sides (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC;
  no F/FT, no F0/F1, no BM/BC, no M19/X19, no
  M42/X42/H42/L42, no QB/PT/FM, no RT/TT (ring,
  not ROWTAIL), no QT (R2 carries b84,85
  in-row, no const trailer); no _T10P373C
  numeric-head probe in either tree; base P372
  has no _T10P372C either -- verified harmless,
  nothing carried forward).
  S0 168ch sig ef171613 NEW-sig (39/84 payload
  diff vs P372S0, positions
  [3-11,20,21,24-27,34,35,41-48,50-55,76-83]
  first-hand, sig b3 IN diff with b0-2 same,
  NOT byte-equal) / S1 176ch sig 26000000
  NEW-sig (68/88 payload diff vs P372S1,
  positions
  [0,4-27,36-38,40-43,48-55,60-83,84-87]
  first-hand, sig b0 IN diff with b1-3 same,
  NOT byte-equal; vs own C10 cells 24x2
  (cells 0,5) + 25x8 staged+oracle: B5EDGE
  split (cell-0 b5-match; cells-1-9 b5-diff;
  cell-5 CM-b84 01-match offsets b5-diff);
  sig b0-3 same-sig NOT in diff; NOT byte-equal;
  S1 SIG-EQ own C10 (26==26); S1 SIG-DIFFERS
  own PB0 (26-vs-62); 39 stays (odd band)),
  staged as full-payload singletons; S0/S1
  embedded b4/b5 db/78 + dd/78 match raw
  lencode.
  AM 16/16 8ch distinct, CM 10/10 4ch diverge
  (b84-87 M4 lane, all 10 distinct), M 16/16
  7ch distinct, QR 4/4 4ch R2 rows
  a0ea/c0ea/e0ea/40eb exact (tails = R2 b84,85
  2B: tail == row 4/4; full 2B-tail pairs
  suffix/subseq/tshare (1,1,0,1,0,0) all-3
  viewer b84-85 span first-hand; writer/GATE
  full-tail b84-87 span suffix-lcs 3/3/2/3/2/2
  corroborated first-hand this round (own
  computation: (3,3,2,3,2,2) exact) -- both
  spans first-hand, bytes agree; full tuples
  pairwise unequal, distinct 4), RM 16/16 7ch
  distinct, RQ 16/16 6ch distinct, no QT + no
  RT + no F (no frags).
  M!=RQ this tier (DISJOINT-full + TAIL-
  IDENTITY, b479-pattern: lists differ, sets
  differ, cell-overlap 0/16, positional-same
  0/16 widths differ 7B vs 6B; TAIL-IDENTITY
  M-tail(b80-83)==RQ-tail(b76-79) ordered 16/16
  + set-eq 16/16, distinct lanes identical
  sequences) -- viewer odds 57->58 (b473
  tails-shared precedent counts every degree);
  32nd full/diff survey (survey counts every
  method RQ-vs-M regardless of degree).
  M-tails 16/16 ALL NEW vs P372T RM+RQ tails
  (overlap 0 both); RM-tails 16/16 ALL NEW vs
  P372T RM+RQ (overlap 0 both); RQ-tails same
  as M (identical sequences); AM/CM/M/QR/RM/RQ
  0-overlap vs P372 all six (widths P373 vs
  P372: AM 8B vs 7B, CM 4B vs 2B, M 7B vs 7B,
  QR 2B vs 2B, RM 7B vs 8B, RQ 6B vs 7B).
  AC 78, CC 82, QC 77, RC 73; C _N decls
  78/82/77/73 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M-tab computed; A b0 const 62 in
  AC (b1 const 02, b2-3 const 00; b5 const 78
  deducted, in AC-missing; b84-87 consts
  01,9f,83,f1 A-lane); C b0 const 26 in CC
  (b1-3 const 00/00/00 first-hand; b5 STEPS
  78->79 in CC (B5EDGE, in CC-missing? NO --
  b5 VARIES so not const; CC-missing is
  [4,5,84-87]: b4 + b5 vary + M4 lanes;
  b52 const 0x56 const-entry, in CC; CC has no
  b84-87 (all in CM lane)); Q b0 const 31 in
  QC (b1 const 02, b2-3 const 00; b5 const 79
  deducted, in QC-missing; b80-85 absent QM7/R2
  lanes, b86 const ae + b87 const f7 in QC);
  R b0 const b1 in RC (b1 const 26 256/256
  oracle, in RC table, code-indexed
  first-hand).
  PBA88-PLAIN-M8b28 sig 62020000 x16 (b0 const
  62 via AC b0; b5 const 78 deducted NOT in AC;
  AM 16/16 distinct NO pair; M8 b28,29,30,31,
  80-83 positions STAGED P365A per code comment)
  + PBA sig 62 NEW vs P372 ff (novelty = new sig
  ff->62 + AM 0-overlap; M8 widths P372 7B vs
  P373 8B differ).
  C10-1SIG-88-TAIL-M4-B5EDGE sig 26000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  26000000; CM 10/10 diverge 4ch b84-87; M4
  FIRST this tier (4B lane); b5 STEPS 78->79
  edge off0->1 in code; b5 varies NOT deducted).
  QUAD88-1SIG-QM7/R2-NOEDGE 1-sig 31020000
  x64 DIFFERS-from-PBA-sig (b0 const 31 in QC;
  b5 const 79 deducted; m-tab b29,34,35,80-83
  (M 16/16 7ch NO frags, m = off&15 first-hand;
  QM7 positions FIRST this lane per code
  comment; per-row 16 distinct NO frags) + r2
  b84,85 R2 4/4 UNPAIRED BY-ROW (q = off>>4
  first-hand); tails = R2 rows + aef7 consts;
  QM7-shared-x3 48/48).
  Ring T88-STANDARD-TM7/TR6 sig b1260000 x256
  (b0 const b1 256/256 oracle, in RC table;
  b1 const 26 256/256 oracle, in RC table;
  code-TM7 b40,41,42,80-83 by COL RM 16/16 7ch
  (positions staged P325R/P333R/P341R) +
  code-TR6 b32,33,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79
  row; positions FIRST this lane per code);
  b84-87 const 8d35aff7 ring-wide NEW; b4=
  (0x93+2off)&FF + b5=0x79+(off>=55)+
  (off>=183) (C literals 147/121/55/183
  verified == 0x93/0x79/55/183; py hex
  0x93/0x79)).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - 1; b4+M8 b28-31,80-83, b5 const
  deducted) / C10 6 (missing 6 - 0; b4,b5 vary+
  M4 b84-87, NO deduct) / quad 10 (missing
  11 - 1; b4+b5 const deducted+QM7 7+R2 2) /
  T 15 (missing 15 - 0; b4,b5 vary+TM7 7+TR6 6,
  NO deduct) -- all match Q-1121 census
  (VPOS 9/6/10/15 + PBA/C10/quad -1/-0/-1 for
  b5 per Q-1121 Q3; census consts 78/82/77/73
  EXACT).
  Code-consts vs census-script excl (PBA 78 /
  C10 82 / quad 77 / T88 73): impl 78/82/77/
  73 = census-script EXACT -- no lag on odd
  band (memo A-956 PRESENT-CONFIRM this tier;
  Q-1121 is the acting sheet). S-F lag stays 44.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 146541 / S1 146542 / A 146543-558 /
  C 146559-568 / Q 146569-632 / R 146633-888):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 STEPS emerges
  from raw lencode 78->79 edge off0->1; Q b5
  const emerges from raw lencode 79 NO edge/NO
  step; R explicit counter (b4=(0x93+2off)&FF
  b5=0x79+(off>=55)+(off>=183); py hex
  0x93/0x79; C staged decimal literals
  147/121/55/183 re-derived: 147==0x93,
  121==0x79)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 8ch M8 b28-31,80-83; C 4ch M4 b84-87; Q
  7ch/2B QM7 b29,34,35,80-83/R2 b84,85; R
  7ch/6ch TM7 b40,41,42,80-83 by COL /
  TR6 b32,33,76-79 by ROW).
  C blocks carry T98371/T98376/T98381/T98396/
  T98411/T98431 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 98371 verified
  in py; bounds + byte positions exact: A 8-lane,
  C 4-lane, Q 7ch+2B + r2, R 7-lane/6-lane),
  A b5 const deducted NOT in AC + C b5 varies
  (B5EDGE, in CC-missing via vary) + Q b5 const
  deducted NOT in QC + R b0 const b1 in RC (in
  table) + R counter b4=(147+2off)&FF +
  (121)+(off>=55)+(off>=183) (C literals
  147/121/55/183 verified), temps _t7421-7436
  (base max _t7420, no reuse) +
  _i4507/4509/4512/4515 (base max _i4505, no
  reuse) + _b4506/4508/4510/4511/4513/4514
  (base max _b4504, no reuse), union 4506-4515
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P372R close (C "T10P3730 singleton" after
  "CLOSED T10P372R"; py return 0 + S0 guard
  98371 after "CLOSED T10P372R" print), at
  dispatch tail (P373R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches census geometry (PB0 NEW-sig 39/84;
  PB1 NEW-sig 68/88 SAME-own-C10 24/25-split;
  PBA88-PLAIN-M8b28 VPOS 9 sig-62 b5 const M8
  16/16 distinct; C10-1SIG-88-TAIL-M4-B5EDGE
  VPOS 6 SAME-as-PB1-sig b5 STEPS M4 10/10 +
  b86 const ae + b87 const f7; QUAD88-1SIG-QM7/
  R2-NOEDGE VPOS 10 + R2 4/4 UNPAIRED
  a0ea/c0ea/e0ea/40eb + full-tail 3/3/2/3/2/2
  + R2-distinct + NO frags + M-tails NEW;
  T88-STANDARD-TM7/TR6 sig-b1260000 VPOS 15 +
  TM7-by-COL/TR6-by-ROW + SPLIT-tails + b84-87
  8d35aff7 + counter 93/79/55/183; lencode
  348/348 whole-tier, NO D dips) incl exact
  values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + consts + frame stand; const-count
  note is impl==census-script this tier per
  census, geometry exact, PORT verdict stands;
  M!=RQ disjoint+tail-identity first-hand this
  tier, tier stands).
- Edges via counter formula first-hand: A head
  df/78 tail fd/78 b5set {78} NO step, 0 ff
  (b4 base 0xdf step2 16/16, b0 const 62 16/16);
  C head ff/78 (edge) tail 11/79 b5set {78,79}
  B5EDGE off0->1, 1 ff (b0 const 26 10/10); Q
  head 13/79 tail 91/79 b5set {79} NO step,
  0 ff (b4 base 0x13 step2 64/64 exact-set
  range 13..91 wraps-never; b0 const 31 64/64);
  ring pre-edge off54 (ff/79), edge off55
  (01/7a); pre-edge off182 (ff/7a) -> edge
  off183 (01/7b); exactly 2 ff in 256 (R b4
  exact-set 93-step2 256 vals / 128 uniq); R
  head 93/79 tail 91/7b; b1 const 26 256/256;
  formulas re-derived from T10P373R code text
  (93/79/55/183 hex==dec) + T10P373A/C/Q text
  (raw lencode + b5 const/step comments); all
  edge pins + head/tail pins + for-list R mid +
  mate + 2 PASS lines each py+C. S0/S1 embedded
  b4/b5 match raw lencode (db/78 + dd/78).
  Ring counter==raw-lencode 256/256 + Q 64/64 +
  A 16/16 + C 10/10. Odd-lencode 348/348
  (16+10+64+256+2). No DISSENT on cut bytes
  (edges481.py EDGES-GREEN, A/Q NO-ff + C
  single-ff B5EDGE + ring 2-ff, all edge asserts
  verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 232/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 232 content / 0 del (content-line
  variance 232 recorded: b478/b479/b480/b481
  232-class); for-line replaced by superset
  (base for-N subset of band, removed 0);
  fine-norm equivalent (for481base.nums subset
  for481.nums, removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-indented 768->
  770 (+2: 146541/146542) / ranges py-indented
  922->926 (+4; C singletons 773->775 +2 / C all-range-guards
  944->948 +4, same 6 P373 blocks both sides;
  no elif/else-if added either side: py
  file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2126->2132 +6 both sides, seal 2220->2226 +6
  (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
  GATE-940d5f26 reconcile (viewer-vs-sweep
  first-hand): GATE values agree on PYID/RGRAM/
  smoke/units/for-added-29 (identical 29-set
  both sides)/PINS+58/temps/seal/CLOSED/
  embeds/counters/consts/R2 rows/tails/M!=RQ
  disjoint+tail-identity/S1-vs-P372C10 79/88
  (own one-line cross-check: 79 exact)/VPOS
  9/6/10/15/extra-table/QM7-shared. Diffs:
  (a) tier-count patterns: GATE counts py
  singletons 778->780 / ranges 944->948 (wider
  grep patterns); viewer counts py-indented
  768->770 / 922->926 + C 773->775 / 940->944
  (anchored patterns) -- deltas +2/+4 agree
  every side/pattern; C-vs-py singleton offset
  5 pre-existing both (GATE-noted C-only dip
  guards, unchanged by band); facts identical.
  (b) uniform ledger: GATE box-score notes
  b477/b479 TRUE-uniform do NOT carry to this
  B5EDGE tier; viewer chain stays 39
  (uniform-cells required; C10 10/10 DIVERGE)
  -- P338 OPEN, deferred to sweep accounting,
  never re-litigated; facts identical.
  (c) RQ==M ledgers: viewer odds 57->58
  (disjoint+tail-identity; b473 precedent counts
  every degree) / survey 31->32 (every-method
  count); GATE 58th odd-band instance + FULL-
  identity degree unchanged (b477 12th stands;
  this tier not full-identity) -- facts
  identical (lists/sets differ, overlap 0,
  positional 0/16, tail-identity ordered+seteq
  16/16). (d) tail-metric spans: viewer audit
  uses b84-85 tail span (suffix/subseq/tshare
  (1,1,0,1,0,0) all-3) + b84-87 cell-tail span
  (suffix (3,3,2,3,2,2) own computation);
  GATE uses full b84-87 span (trailing=TSHARE=
  subseq 3/3/2/3/2/2 all-3 agree) -- b84-87
  suffix vectors agree exactly (3,3,2,3,2,2);
  underlying bytes agree (R2 rows + ae/f7
  consts); facts identical. No code dispute;
  PORT stands both sides.
- CONFIRM evidence (CONVERT-01 rule b):
  memo A-sheet PRESENT for P373 (A-956-q1121
  CONFIRM 50/50 CLEAN: Q1 1x(100,84)+347x
  (104,88) EXACT + PBA 62/M8/b5-78 + C10 26/
  M84-87/b5-steps + QUAD 1-sig-31 + T b1260000
  STANDARD + Q2 QM/R2 tails + suffix 3/3/2/3/
  2/2 + M-tails NEW + TM-by-COL/TR-by-ROW +
  8d35aff7; Q3 lencode 348/348 + consts 78/82/
  77/73 + 0 stragglers NO D dips) + writer
  census Q-1121 (consts PBA 78 / C10 82 /
  quad 77 / T88 73; committed tables match excl
  exactly -- no writer lag this tier, geometry
  exact, PORT verdict stands) + cport commit
  msgs (PYID 11090, RGRAM 22180 both legs per
  msg; py-merge RGRAM 22180) + own full battery
  above. Novelty gated: b52-const-entry variant
  0x56 in CC (P372 0x94, P371/P370 0x4a, P369
  0xd2, P368/P367 0x84, P366 0x72, P365 0xc5,
  P364 0xb9, P363 0xb8); M-tails 16/16 ALL NEW
  vs P372T tails; no _T10P373C either side.
- FWD-check: banked Next-P374 (Q-1121 forward
  note, read first-hand): PB0 @146889 sig
  6e586913 pay84 NEW-sig (33/84 diff vs
  P373PB0, NOT byte-equal) + PB1 26000000
  pay88 @146890 sig-REPEAT (same sig as
  P373PB1; 48/88 diff, NOT byte-equal) + PBA88
  5e020000 x16 @146891-906 + C10-region
  20000000 pay88 x10 @146907-916 DIFFERS-from-
  PB1-sig -- b482 C port 648dd0de (T10P374 pins
  146889..147236, 2232 sealed) ALREADY LANDED
  (this round's turf, b482+; battery next in
  round); CONSUME-FIRST per bank-miss lesson.
- Quiz: no conflicting CLAIM/GATE/FLAG on b481
  (adjacent even b480 = da1ea8de C port live
  used as diff-base only, no verdict beyond;
  adjacent b482 = 648dd0de C port live, NEXT
  battery this round, no verdict yet; FLAG
  files name no b481 band; DISSENTs q846/847/
  849 unrelated tiers; no conflicting
  CLAIM/GATE/FLAG at filing -- GATE-940d5f26
  reconciled mid-battery).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r78/
  (build481/, pyid481.log, rgram481py/c.log,
  cmp481.py, seteq481.py, ownloop481.py (+
  w481loop.log), secf481a/b/c.py, edges481.py
  (+.log), tabaudit481.py (+.log), smoke481.log,
  units481.log, band481.diff/addedlines/.addedc,
  for481.nums/added/for481base.nums).

Verdict: PASS. No RED. 348-pin contiguous range
146541..146888 sealed. Round 2/4 = cap 2/4.
