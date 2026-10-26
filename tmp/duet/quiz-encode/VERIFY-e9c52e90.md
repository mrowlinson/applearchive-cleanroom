# VERIFY-e9c52e90 b477 T10P369 pins 145149..145496 (348 pins) PASS

Seat viewer-r77, first-hand, tree @e9c52e90,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r77.
Base 0c29b70b (b476 tip, 2196 tiers sealed; this
seat's VERIFY-0c29b70b PASS-filed same round,
base-use only, respected). Band = 9367008d (py
merge w2b@e5a89b49 partial, +6 tiers, +58 pins;
commit msg verified via git log) + e9c52e90 (C
port; parent == 9367008d verified via git
rev-list --parents). Chain 0c29b70b -> 9367008d
-> e9c52e90, every sha via git log at takeover,
NO gap-jump. GATE-e9c52e90 PASS-functional filed
by sweep-r81 -- reconciled first-hand below
(values agree; ledger conventions differ where
the OPEN P338 dispute lives, code facts
identical). NO other GATE/FLAG on b477 at file
time.

Banked Next-P369 shape (A-954 + Q-1079 forward
notes + w2b-r33 qTBD-p369 census, all read
first-hand) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 ef928b0e @145149
(S0 head; NEW-sig 33/84 vs P368PB0 @
n144801, sig b0-2 IN diff with b3 same,
positions
[0,1,2,4,5,11,19-31,36,37,60-71]
first-hand, NOT byte-equal) + PB1 1e000000
@145150 (S1 head; NEW-sig 56/88 vs
P368PB1 @ n144802, sig b0 IN diff with b1-3
same, positions
[0,4,5,19,26-44,46-54,56-75,84-87]
first-hand, NOT byte-equal; diffs
vs own C10[0] n145167 all-10 identical-40
positions [4,5,19,38,39,45,46,48-50,53-75,
77-79,84-87] per cell staged+oracle, sig b0-3
same-sig NOT in diff; S1 SIG-EQ own C10
(1e==1e); S1 SIG-DIFFERS own PB0 (1e-vs-ef)
and PBA sig (1e-vs-e5); C10 10/10 DIVERGE
staged+oracle: 39 stays (odd band): NOT
TRUE-UNIFORM under viewer convention
(uniform-cells required); P338 uniform-rule
dispute stays DEFERRED to sweep accounting,
never re-litigated; GATE sweep-ledger counts
its own 25th TRUE-uniform (SIG-EQ + differs-PB0
ledger) -- ledgers differ, facts identical)
+ PBA88-STEP-M8b52 sig e5010000 x16 @145151-166
(b0 const 0xe5 first-hand) + C10-region
1e000000 pay88 x10 @145167-176 (b0 const 0x1e
first-hand, SAME-as-PB1-sig) -- all corroborated
against lane code both sides before any battery
step (py==C S0/S1 staged strings; staged-vs-
oracle secf477a/b/c GREEN first-run; no
bank-miss).

- Build: seat-private build477/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 968a39a6...
  (no GATE absolutes cited -- recorded first-hand
  here, never hand-transcribed).
- RGRAMC-PYID 10974/10974 covered=10974/10974
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  default CT cache; +29 vs b476 10945).
- RGRAM py 21948/21948 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21948/21948 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21948/21948, sorted +
  raw identical; cmp477.py GREEN).
- PINS-RGRAM cells set-eq 21948/21948 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq477.py GREEN first-run). PINS 21950 lines
  first-hand (2 hdr + 21948 rows; base 21892
  lines / 21890 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 10945->10974 +29/-0 (python
  sets, trailing-';' strip, never comm): 145149
  145150 145151 145152 145158 145159 145165
  145166 145167 145168 145171 145172 145175
  145176 145177 145192 145193 145208 145209
  145225 145240 145241 145279 145280 145344
  145407 145408 145409 145496 (no GATE list at
  battery start -- GATE filed mid-battery with
  the identical 29-set; range 145149..145496
  exact).
  29 = 2 sing (145149 145150 offs 0/1) + A 6
  (STEP edge-pair 145151/145152 off0/1 + mid pair
  145158/145159 off7/8 + tail pair 145165/
  145166 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; A b5 STEP 6d->6e
  @off0/1 edge pair-covered) + C 6 (head pair
  145167/145168 off0/1 + mid pair 145171/145172
  off4/5 + tail pair 145175/145176 off8/9; offs
  2,3,6,7 unsampled first-hand; b5 const 6e NO
  edge) + Q 7 (head 145177 off0 + row pair
  145192/145193 off15/16 + row pair 145208/
  145209 off31/32 + mid 145225 off48 + tail
  145240 off63; row boundaries (16,32) pair-
  covered, off48 single-sided mate off47
  unsampled; b5 const 6e NO edge) + R 8 (head
  145241 off0 + edge pair 145279/145280 off38/39
  + mid 145344 off103 + edge pair 145407/145408
  off166/167 + mate 145409 off168 + tail 145496
  off255; both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21948-21890.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit477.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 179 PASS 0 FAIL second-run (1 own-assert
  fix + rerun: py-A used raw lencode not explicit
  counter -- assert text fixed to raw-lencode +
  STEP-comment form, code values untouched,
  reran GREEN; no dead code).
  Inventory exactly the 12 tables both sides
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no M42/X42/
  H42/L42, no QB/PT/FM, no RT/TT (ring, not
  ROWTAIL), no QT (R4 carries b84-87 in-row,
  no const trailer); no _T10P369C numeric-head
  probe -- precedent since band29, only band29-
  range cover it).
  S0 168ch sig ef928b0e NEW-sig (33/84 payload
  diff vs P368S0, positions
  [0,1,2,4,5,11,19-31,36,37,60-71]
  first-hand, sig b0-2 IN diff with b3 same, NOT
  byte-equal) / S1 176ch sig 1e000000 NEW-sig
  (56/88 payload diff vs P368S1, positions
  [0,4,5,19,26-44,46-54,56-75,84-87]
  first-hand, sig b0 IN diff with b1-3 same, NOT
  byte-equal; vs own C10 cells 10/10 DIVERGE
  staged+oracle: all-10 diff=40 uniform-diff,
  sig b0-3 same-sig NOT in diff; NOT byte-equal;
  S1 SIG-EQ own C10 (1e==1e); S1 SIG-DIFFERS own
  PB0 (1e-vs-ef); 39 stays (odd band)), staged
  as full-payload singletons; S0/S1 embedded b4/b5
  fb/6d + fd/6d match raw lencode.
  AM 16/16 16ch distinct, CM 10/10 8ch diverge
  (b84,85,86,87 M4 lane, all 10 distinct), M 16/16
  14ch distinct, QR 4/4 8ch R4 rows
  8e9e54d5/ae9e54d5/234c14d7/434c14d7 exact
  (tails = full b84-87 R4 rows; full-tail suffix
  = subseq = TSHARE = (3,0,0,0,0,3): pairs
  (0,1),(2,3) share trailing 3, rest 0, all-3
  agree first-hand; full tuples pairwise unequal,
  4 distinct), RM 16/16 14ch distinct, RQ 16/16
  14ch distinct, no QT + no RT + no F (no frags).
  M==RQ 16/16 string-identical SAME-ORDER (M list
  == RQ list, 14ch; QM7 b6,7,8,80-83 by COL
  m=off&15 vs TR7... RQ7 b6,7,8,76-79 by ROW
  r=off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated) -- 56th odd-band
  RQ==M instance (odds 55->56); 28th full/diff
  survey (survey counts every method RQ-vs-M
  regardless of degree; 5th identical case:
  b472, b474, b475, b476, b477; GATE sweep-ledger
  counts its own 12th FULL-identity degree --
  ledgers differ, facts identical).
  M-tails 16/16 ALL NEW vs P368T row-led tails
  (overlap 0; P368T RQ 16x8B frame first-hand
  from code, tails last-4B); RQ-tails 16/16 ALL
  NEW vs P368T RQ (overlap 0) + 16/16 ALL NEW
  vs P368T RM (overlap 0); RM-tails 16/16 ALL
  NEW vs P368T RM (overlap 0) + 16/16 ALL NEW
  vs P368T RQ (overlap 0); AM/CM/M/QR/RM/RQ
  0-overlap vs P368 all six (widths P369 vs
  P368: AM 8B vs 9B, CM 4B vs 4B, M 7B vs 8B, QR
  4B vs 1B, RM 7B vs 8B, RQ 7B vs 8B).
  AC 78, CC 82, QC 75, RC 72; C _N decls
  78/82/75/72 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 const e5 in
  AC (b1 const 01, b2-3 const 00; b5 STEPS
  6d->6e in VPOS, in AC-missing; b84-87 consts
  af,2c,47,9c A-lane); C b0 const 1e in CC
  (b1-3 const 00; b5 const 6e deducted, in
  CC-missing; b52 const 0xd2 const-entry, in CC;
  CC has no b84,85,86,87 (all in CM lane));
  C b84,85,86,87 absent (M4/TAIL lane);
  Q b0 const ef 1-sig DIFFERS-from-PBA in QC
  first-hand (b1 const 01, b2-3 const 00; b5
  const 6e deducted NOT in QC (in QC-missing),
  NO step; b80-87 absent QM7/R4 lanes, no b85-87
  consts this tier); R b0 const ff + b1 const 1e
  in RC table, code-indexed first-hand).
  PBA88-STEP-M8b52 sig e5010000 x16 (b0 const
  e5 via AC b0; b5 STEPS 6d->6e @off0/1 in VPOS;
  AM 16/16 distinct NO pair; M8 b52,53,54,55,
  80-83 positions STAGED P353A/P361A per code
  comment, FIRST-shape per census) + PBA sig e5
  NEW vs P368 88 (novelty = new sig 88->e5 + AM
  0-overlap; M8 FIRST this lane: A-mtab widths
  P364 7B / P365 8B / P366 7B / P367 6B / P368
  9B all differ).
  C10-1SIG-88-TAIL-M4 sig 1e000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  1e000000; CM 10/10 diverge 8ch b84,85,86,87;
  CC has no b84-87 (all in CM lane); b5 const
  6e deducted NOT in CC).
  QUAD88-1SIG-QM7/R4-NOEDGE 1-sig ef010000
  DIFFERS-from-PBA-sig (b0 const ef in QC; b5
  const 6e deducted, NO step; m-tab b6,7,8,
  80-83 (M 16/16 14ch NO frags, m = off&15
  first-hand; QM7 positions staged P321Q per
  census) + r4 b84-87 R4 4/4 UNPAIRED BY-ROW
  (q = off>>4 first-hand); tails = R4 rows,
  full-tail pairs (3,0,0,0,0,3) per guard +
  R4 all-distinct + QM7-shared-x3 48/48).
  Ring T88-STANDARD-TM7/TR7 1-sig ff1e0000 x256
  (b0 const ff 256/256 oracle, in RC table; b1
  const 1e 256/256 oracle, in RC table; code-TM7
  b13,14,15,80-83 by COL RM 16/16 (positions
  staged P313R per census) + code-TR7
  b6,7,8,76-79 by ROW RQ 16/16 UNPAIRED (SPLIT
  tails b80-83 col / b76-79 row); b84-87 const
  824c14d7 ring-wide NEW; b4=(0xb3+2off)&FF +
  b5 = 0x6e+(off>=39)+(off>=167) (C literals
  179/110/39/167 verified == 0xb3/0x6e/39/167;
  py hex 0xb3/0x6e)).
  VPOS partitions re-derived from code: PBA 10
  (missing 10 - 0; b4,b5+M8
  b52,53,54,55,80-83, b5 STEPS varies, NO
  deduct) / C10 5 (missing 6 - 1; b4+M4
  b84,85,86,87, b5 const deducted) / quad 12
  (missing 13 - 1; b4,b5+QM7 7+R4 4, b5 const
  deducted, NO step) / T 16 (missing 16 - 0;
  b4,b5+TM7 7+TR7 7, counter varies, NO deduct)
  -- all match qTBD-p369 census (10/5/12/16).
  Code-consts vs census-script excl (PBA 78 /
  C10 82 / quad 75 / T88 72): impl 78/82/75/
  72 = census-script EXACT -- no lag on odd
  band; memo-side recorded (no memo A-sheet for
  P369 at file time; qTBD-p369 census-script is
  the acting sheet). VPOS 10/5/12/16 =
  census EXACT. S-F lag stays 44.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 145149 / S1 145150 / A 145151-166 /
  C 145167-176 / Q 145177-240 / R 145241-496):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 STEP emerges
  from raw lencode 6d->6e @off0/1; C b5 const
  emerges from raw lencode; Q b5 const emerges
  from raw lencode; R explicit counter
  (b4=(0xb3+2off)&FF b5=0x6e+(off>=39)+(off>=167);
  py hex 0xb3/0x6e; C staged decimal literals
  179/110/39/167 re-derived: 179==0xb3, 110==0x6e)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 16ch M8 b52,53,54,55,80-83; C 8ch M4 b84-87;
  Q 14ch/8ch QM7 b6,7,8,80-83/R4 b84-87; R 14ch/
  14ch TM7 b13,14,15,80-83 by COL / TR7
  b6,7,8,76-79 by ROW).
  C blocks carry T97443/T97448/T97453/T97468/
  T97483/T97503 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 97443 verified
  in py; bounds + byte positions exact: A 8-lane,
  C 4-lane, Q 7ch+4B + r4, R 7-lane/7-lane),
  A raw lencode (no counter literals; A b5 STEP
  in VPOS via lencode, in AC-missing) + C b5
  const deducted NOT in CC + Q b5 const 6e NO
  step (deducted NOT in QC) + R counter
  b4=(179+2off)&FF + (110)+(off>=39)+(off>=167)
  (C literals 179/110/39/167 verified), temps
  _t7357-7372 (base max _t7356, no reuse) +
  _i4467/4469/4472/4475 (base max _i4465, no
  reuse) + _b4466/4468/4470/4471/4473/4474
  (base max _b4464, no reuse), union 4466-4475
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P368R close (C "T10P3690 singleton" after
  "CLOSED T10P368R"; py return 0 + S0 guard
  97443 after "CLOSED T10P368R" print), at
  dispatch tail (P369R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches census geometry (PB0 NEW-sig 33/84;
  PB1 NEW-sig 56/88 SAME-own-C10 40/88;
  PBA88-STEP-M8b52 VPOS 10 sig-e5 b5-step M8
  16/16 distinct; C10-1SIG-88-TAIL-M4 VPOS 5
  SAME-as-PB1-sig b5 const M4 10/10 diverge;
  QUAD88-1SIG-QM7/R4-NOEDGE VPOS 12 + R4 4/4
  UNPAIRED 8e9e54d5/ae9e54d5/234c14d7/434c14d7
  + suffix-(3,0,0,0,0,3) + R4-distinct + QM7-
  shared-x3 + NO frags + M-tails NEW;
  T88-STANDARD-TM7/TR7 VPOS 16 + TM7-by-COL/
  TR7-by-ROW + SPLIT-tails + b84-87 824c14d7 +
  counter b3/6e/39/167; lencode 348/348
  whole-tier, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R1... R4 rows + tails
  + LCS + frame + consts stand; const-count note
  is impl==census-script this tier per census,
  geometry exact, PORT verdict stands; M==RQ
  identical first-hand this tier, tier stands).
- Edges via counter formula first-hand: A head
  ff/6d edge 01/6e b5set {6d,6e} STEP, 1 ff
  (b4 base 0xff step2 16/16, b0 const e5 16/16);
  C head 1f/6e tail 31/6e b5set {6e} NO step,
  0 ff (b0 const 1e 10/10); Q head 33/6e
  tail b1/6e b5set {6e} NO step, 0 ff (b4 base
  0x33 step2 64/64 exact-set range 33..b1 NO
  wrap, min 0x33 max 0xb1); ring pre-edge off38
  (ff/6e), edge off39 (01/6f); pre-edge off166
  (ff/6f) -> edge off167 (01/70); exactly 2 ff
  in 256 (R b4 exact-set b3-step2 256 vals / 128
  uniq); R head b3/6e tail b1/70; formulas
  re-derived from T10P369R code text (b3/6e/39/
  167 hex==dec) + T10P369A/C/Q text (raw lencode
  + b5 const/STEP comments); all edge pins +
  head/tail pins + for-list R mids + 2 PASS lines
  each py+C. S0/S1 embedded b4/b5 match raw
  lencode (fb/6d + fd/6d). Ring counter==raw-
  lencode 256/256 + Q 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges477.py EDGES-GREEN, A STEP-
  edge + C NO-ff + Q NO-ff + ring 2-ff range-with-
  wrap + Q-range exact + R counter asserts
  verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 231/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 231 content / 0 del (content-line
  variance 231 recorded: b468/b469/b474/b475/
  b477 231-class; b470/b471/b472/b473 232-class;
  b476 230 new class); for-line replaced by
  superset (base for-N subset of band, removed
  0); fine-norm equivalent (for477base.nums
  subset for477.nums, removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-indented 760->762
  (+2: 145149/145150) / ranges py-indented 906->
  910 (+4; C singletons 765->767 +2 / C
  all-range-guards 928->932 +4, same 6 P369 blocks
  both sides; no elif/else-if added either side:
  py file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2102->2108 +6 both sides, seal 2196->2202 +6
  (commit msgs; offset +94 vs CLOSED-T10P stable):
  all agree, no slip (absolute seal inherits lane
  tally; delta verified).
  GATE-e9c52e90 reconcile (viewer-vs-sweep
  first-hand): GATE values agree on PYID/RGRAM/
  smoke/units/for-added-29/PINS+58/temps/seal/
  CLOSED/embeds/counters/consts/tails/R4 rows.
  Diffs: (a) uniform ledger: GATE sweep-ledger
  counts its own 25th TRUE-uniform (SIG-EQ +
  differs-PB0); viewer chain stays 39 (uniform-
  cells required; C10 10/10 DIVERGE) -- P338
  dispute OPEN, deferred to sweep accounting,
  never re-litigated; facts identical.
  (b) singleton-count pattern: GATE counts all
  `if n == ` 770->772; viewer counts indented
  dispatch `^    if n == ` 760->762 -- same
  delta +2, pattern differs; py file-wide elif
  absolute is 50 both (no elif added), C else-if
  0 both. (c) RQ==M ledgers: viewer odds 56 /
  survey 28 (every-method count) vs sweep 56th
  odd / 12th FULL-identity degree -- facts
  identical (M==RQ 16/16 same-order).
  No code dispute; PORT stands both sides.
- CONFIRM evidence (CONVERT-01 rule b):
  NO memo A-sheet for P369 at file time
  (A-956-q1081 ABSENT per GATE filename survey;
  Q-1081 UNANSWERED; viewer has no P369 geometry
  answer on file). Substitute first-hand: writer
  census NOTE-w2b-r33-qTBD-p369 (consts PBA 78 /
  C10 82 / quad 75 / T88 72; committed tables
  match excl exactly -- no writer lag this tier,
  geometry exact, PORT verdict stands) +
  cport commit msgs (PYID 10974, RGRAM 21948
  both legs per msg; py-merge RGRAM 21948) +
  own full battery above. Novelty gated:
  b52-const-entry variant 0xd2 in CC (P368 0x84,
  P367 0x84, P366 0x72, P365 0xc5, P364 0xb9,
  P363 0xb8); M-tails 16/16 ALL NEW vs P368T
  row-led tails.
- FWD-check: banked Next-P370 (qTBD-p369 forward
  note, read first-hand): PB0 @145497 sig
  ef928b0c pay84 NEW-sig 1B-off vs P369PB0
  (34/84 diff, NOT byte-equal) + PB1 19000000
  pay88 @145498 NEW-sig vs P369 heads (56/88
  diff vs P369PB1, NOT byte-equal) + PBA88
  92010000 x16 @145499-514 + C10-region 19000000
  pay88 x10 @145515-524 SAME-as-PB1-sig --
  b478 py-merge a97cf8ea + C port 09b93c5d
  ALREADY LANDED (next battery, no poll-wait);
  pre-corroboration at that battery; CONSUME-FIRST
  per bank-miss lesson.
- Quiz: no conflicting CLAIM/GATE/FLAG on b477
  (adjacent evens b476 = 0c29b70b C port live
  used as diff-base only, no verdict beyond;
  adjacent evens b478 = 09b93c5d C port live,
  next battery, no verdict beyond; FLAG files
  name no b477 band; DISSENTs are q846/847/849
  unrelated tiers).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r77/
  (build477/, pyid477.log, rgram477py/c.log,
  cmp477.py, seteq477.py, ownloop477.py (+
  w477loop.log), secf477a/b/c.py, edges477.py
  (+.log), tabaudit477.py (+.log), smoke477.log,
  units477.log, band477.diff/addedlines/.addedc,
  for477.nums/added/for477base.nums).

Verdict: PASS. No RED. 348-pin contiguous range
145149..145496 sealed. Round 2/4.
