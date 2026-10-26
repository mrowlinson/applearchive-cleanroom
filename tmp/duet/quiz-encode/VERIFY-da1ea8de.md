# VERIFY-da1ea8de b480 T10P372 pins 146193..146540 (348 pins) PASS

Seat viewer-r78, first-hand, tree @da1ea8de,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r78.
Base 6a7ad611 (b479 tip, 2214 tiers sealed; this
seat's VERIFY-6a7ad611 PASS-filed r77,
base-use only, respected). Band = 7779190f (py
merge w2b@f6cdd371 partial, +6 tiers, +58 pins;
commit msg verified via git log) + da1ea8de (C
port; parent == 7779190f verified via git
rev-list --parents). Chain 6a7ad611 -> 7779190f
-> da1ea8de, every sha via git log at takeover,
NO gap-jump. GATE-da1ea8de PASS-functional filed
by sweep2-r83 -- reconciled first-hand below
(values agree; VPOS-C10 4-vs-3 + tail-metric
b84-87-vs-b84-85 spans + RQ==M ledger degree
phrasing differ, code facts identical). NO other
GATE/FLAG on b480 at file time.

Banked Next-P372 shape (w2b-r33 qTBD-p371 forward
note, read first-hand) CONSUMED FIRST and
VERIFIED first-hand EXACT: PB0 ef17160d
@146193 (S0 head; NEW-sig 33/84 vs P371PB0 @
n145845, sig b2,3 IN diff with b0,1 same,
positions
[2,3,4,5,20,21,25-33,36-41,64-75]
first-hand, NOT byte-equal) + PB1 1f000000
@146194 (S1 head; NEW-sig 44/88 vs
P371PB1 @ n145846, sig b0 IN diff with b1-3
same, positions
[0,4,5,19,26-59,72-79,84-87]
first-hand, NOT byte-equal; diffs
vs own C10[0] n146211 all-10 identical-57
first-hand, sig b0-3 same-sig NOT in diff;
S1 SIG-DIFFERS own C10 (1f-vs-26); S1 SIG-
DIFFERS own PB0 (1f-vs-ef); C10 10/10 DIVERGE
staged+oracle: 39 stays
(even band): NOT TRUE-UNIFORM under viewer
convention (uniform-cells required); P338
uniform-rule dispute stays DEFERRED to sweep
accounting, never re-litigated) +
PBA88-PLAIN-M7b6 sig ff010000 x16 @146195-210
(b0 const 0xff first-hand) + C10-region
26000000 pay88 x10 @146211-220 (b0 const 0x26
first-hand, DIFFERS-from-PB1-sig) -- all
corroborated against lane code both sides plus
Q-1120/A-955 before any battery step (py==C
S0/S1 staged strings; staged-vs-oracle
secf480a/b/c GREEN first-run; no bank-miss).

- Build: seat-private build480/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 78b826d9...
  (no GATE absolutes cited -- recorded first-hand
  here, never hand-transcribed).
- RGRAMC-PYID 11061/11061 covered=11061/11061
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch;
  +29 vs b479 11032).
- RGRAM py 22122/22122 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 22122/22122 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (22122/22122, sorted +
  raw identical; cmp480.py GREEN).
- PINS-RGRAM cells set-eq 22122/22122 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq480.py GREEN). PINS 22124 lines
  first-hand (2 hdr + 22122 rows; base 22066
  lines / 22064 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 11032->11061 +29/-0 (python
  sets, trailing-';' strip, never comm): 146193
  146194 146195 146196 146202 146203 146209
  146210 146211 146212 146215 146216 146219
  146220 146221 146227 146228 146244 146260
  146276 146284 146285 146303 146304 146396
  146397 146431 146432 146540 (= GATE 29-set
  exact, first-hand both sides; range
  146193..146540 exact).
  29 = 2 sing (146193 146194 offs 0/1) + A 6
  (head pair 146195/146196 off0/1 + mid pair
  146202/146203 off7/8 + tail pair 146209/
  146210 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 76 NO
  edge) + C 6 (head pair 146211/146212 off0/1
  + mid pair 146215/146216 off4/5 + tail pair
  146219/146220 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 76 NO edge) + Q 7 (head
  146221 off0 + colsplit pair 146227/146228
  off6/7 + mid 146244 off23 + mid 146260 off39
  + mid 146276 off55 + tail 146284 off63; b5
  const 76 NO step NO edge) + R 8 (head 146285
  off0 + edge pair 146303/146304 off18/19 +
  mid pair 146396/146397 off111/112 + edge pair
  146431/146432 off146/147 + tail 146540
  off255; both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  22122-22064.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit480.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 186 PASS 0 FAIL first-run (after 2 own-
  script fixes: PYR/N-scope slice end + dup
  check-name; tree untouched).
  Inventory: exactly the 12 band tables both
  sides (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC;
  no F/FT, no F0/F1, no BM/BC, no M19/X19, no
  M42/X42/H42/L42, no QB/PT/FM, no RT/TT (ring,
  not ROWTAIL), no QT (R2 carries b84,85
  in-row, no const trailer); no _T10P372C
  numeric-head probe in either tree; base keeps
  its pre-existing old-series _T10P371C, band
  adds none -- verified harmless, untouched).
  S0 168ch sig ef17160d NEW-sig (33/84 payload
  diff vs P371S0, positions
  [2,3,4,5,20,21,25-33,36-41,64-75]
  first-hand, sig b2,3 IN diff with b0,1 same,
  NOT byte-equal) / S1 176ch sig 1f000000
  NEW-sig (44/88 payload diff vs P371S1,
  positions
  [0,4,5,19,26-59,72-79,84-87]
  first-hand, sig b0 IN diff with b1-3 same,
  NOT byte-equal; vs own C10 cells 10/10
  DIVERGE staged+oracle: all-10 diff=57
  uniform-diff, sig b0-3 same-sig NOT in diff;
  NOT byte-equal; S1 SIG-DIFFERS own C10
  (1f-vs-26); S1 SIG-DIFFERS own PB0 (1f-vs-ef);
  39 stays (even band)), staged as full-payload
  singletons; S0/S1 embedded b4/b5 23/76 +
  25/76 match raw lencode.
  AM 16/16 7ch distinct, CM 10/10 4ch diverge
  (b84,85 M2 lane, all 10 distinct), M 16/16
  7ch distinct, QR 4/4 4ch R2 rows
  d82f/457b/657b/857b exact (tails = R2 b84,85
  bytes: tail == row 4/4; full 2B rows pairwise
  unequal, distinct 4), RM 16/16 8ch distinct,
  RQ 16/16 7ch distinct, no QT + no RT + no F
  (no frags).
  M==RQ this tier (IDENTICAL lists same-order,
  sets equal, cell-overlap 16/16, positional
  16/16; TAIL-IDENTITY ordered+seteq 16/16 as a
  consequence) -- viewer evens 54->55 (b473
  tails-shared precedent counts every degree);
  31st full/diff survey (survey counts every
  method RQ-vs-M regardless of degree).
  M-tails 16/16 ALL NEW vs P371T RM col-led
  tails (overlap 0) and vs P371T RQ row-led
  tails (overlap 0); RM-tails 16/16 ALL NEW vs
  P371T RM (overlap 0) and vs P371T RQ
  (overlap 0); AM/CM/M/QR/RM/RQ 0-overlap vs
  P371 all six (widths P372 vs P371: AM 7B vs
  6B, CM 2B vs 2B, M 7B vs 6B, QR 2B vs 5B, RM
  8B vs 9B, RQ 7B vs 8B).
  AC 79, CC 84, QC 77, RC 71; C _N decls
  79/84/77/71 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M-tab computed; A b0 const ff in
  AC (b1 const 01, b2-3 const 00; b5 const 76
  deducted, in AC-missing; b84-87 consts
  65,c3,28,b4 A-lane); C b0 const 26 in CC
  (b1-3 const 00/00/00 first-hand; b5 const 76
  deducted, in CC-missing; b52 const 0x94
  const-entry, in CC; CC has no b84,85 (both
  in CM lane); C b86 const ba + b87 const 78);
  Q b0 ABSENT (colsplit-varies, in QC-missing;
  b1 const 02, b2-3 const 00; b5 const 76
  deducted, in QC-missing; b80-85 absent QM7/R2
  lanes, b86 const 90 + b87 const 79 in QC);
  R b0 ABSENT (rowsplit-varies, in RC-missing;
  b1 const 26 in RC table, code-indexed
  first-hand).
  PBA88-PLAIN-M7b6 sig ff010000 x16 (b0 const
  ff via AC b0; b5 const 76 deducted NOT in AC;
  AM 16/16 distinct NO pair; M7 b6,7,9,80-83
  positions STAGED P356A/P364A per code comment)
  + PBA sig ff NEW vs P371 c9 (novelty = new sig
  c9->ff + AM 0-overlap; M7 widths P371 6B vs
  P372 7B differ).
  C10-1SIG-88-TAIL-M2 sig 26000000 x10
  DIFFERS-from-PB1-sig (full sig b0-3 in CC =
  26000000; CM 10/10 diverge 4ch b84,85;
  CC has no b84,85 (both in CM lane); M2 FIRST
  ...(continued NOVEL this lane per code
  positions P356C/P371C); b5 const 76 deducted
  NOT in CC).
  QUAD88-2SIG-QM7/R2-COLSPLIT 2-sig
  31020000/46020000 x64 DIFFERS-from-PBA-sig
  (b0=31 iff col<7: 28+36 in QC-missing; b5
  const 76 deducted; m-tab b0,10,11,80-83 (M
  16/16 7ch NO frags, m = off&15 first-hand;
  QM7 positions FIRST this lane per code
  comment, split col<7 vs P356 col<5) + r2
  b84,85 R2 4/4 UNPAIRED BY-ROW (q = off>>4
  first-hand); tails = R2 rows + 9079 consts;
  full 2B-tail pairs: viewer span b84-85 gives
  suffix/subseq/tshare (0,0,0,1,1,1) all-3
  first-hand; writer Q-1120 full-tail triples
  recorded but span-unresolved (values 3 exceed
  any 2B metric; bytes agree: rows d82f/457b/
  657b/857b + consts 90/79 both sides) --
  span-convention noted, facts identical; full
  tuples pairwise unequal, distinct 4;
  QM7-shared-x3 48/48).
  Ring T88-2SIG-TM8/TR7-ROWSPLIT sigs
  31260000 x112 + 46260000 x144 (b0=31 iff
  row<7, in RC-missing; b1 const 26 256/256
  oracle, in RC table; code-TM8
  b16,17,18,19,80-83 by COL RM 16/16 8ch
  (positions FIRST this lane per code) +
  code-TR7 b0,10,11,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79
  row); b84-87 const a57b9079 ring-wide NEW;
  b4=(0xdb+2off)&FF + b5=0x76+(off>=19)+
  (off>=147) (C literals 219/118/19/147
  verified == 0xdb/0x76/19/147; py hex
  0xdb/0x76)).
  VPOS partitions re-derived from code: PBA 8
  (missing 9 - 1; b4+M7 b6,7,9,80-83, b5 const
  deducted) / C10 3 (missing 4 - 1; b4+M2
  b84,85, b5 const deducted) / quad 10
  (missing 11 - 1; b0 varies+b4+b5 const
  deducted+QM7 7+R2 2) / T 17 (missing 17 - 0;
  b0,b4,b5 vary+TM8 8+TR7-minus-b0 6, NO
  deduct) -- all match Q-1120 census
  (quad VPOS 10 + T VPOS 17 + PBA/C10 -1 for
  b5-const per Q-1120 Q3; census consts
  79/84/77/71 EXACT).
  Code-consts vs census-script excl (PBA 79 /
  C10 84 / quad 77 / T88 71): impl 79/84/77/
  71 = census-script EXACT -- no lag on even
  band (memo A-955 PRESENT-CONFIRM this tier;
  Q-1120 is the acting sheet). S-F lag stays 44.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 146193 / S1 146194 / A 146195-210 /
  C 146211-220 / Q 146221-284 / R 146285-540):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode; Q b5 const emerges from raw
  lencode 76 NO edge/NO step; R explicit counter
  (b4=(0xdb+2off)&FF b5=0x76+(off>=19)+
  (off>=147); py hex 0xdb/0x76; C staged decimal
  literals 219/118/19/147 re-derived: 219==0xdb,
  118==0x76)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 7ch M7 b6,7,9,80-83; C 4ch M2 b84,85; Q
  7ch/4ch QM7 b0,10,11,80-83/R2 b84,85; R
  8ch/7ch TM8 b16,17,18,19,80-83 by COL /
  TR7 b0,10,11,76-79 by ROW).
  C blocks carry T98139/T98144/T98149/T98164/
  T98179/T98199 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 98139 verified
  in py; bounds + byte positions exact: A 7-lane,
  C 2-lane, Q 7ch+2ch + r2, R 8-lane/7-lane),
  A b5 const deducted NOT in AC + C b5 const
  deducted NOT in CC + Q b5 const deducted NOT
  in QC + R b0/b5 vary... R b0 VARIES rowsplit
  in RC-missing + R counter b4=(219+2off)&FF +
  (118)+(off>=19)+(off>=147) (C literals
  219/118/19/147 verified), temps _t7405-7420
  (base max _t7404, no reuse) +
  _i4497/4499/4502/4505 (base max _i4495, no
  reuse) + _b4496/4498/4500/4501/4503/4504
  (base max _b4494, no reuse), union 4496-4505
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P371R close (C "T10P3720 singleton" after
  "CLOSED T10P371R"; py return 0 + S0 guard
  98139 after "CLOSED T10P371R" print), at
  dispatch tail (P372R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches census geometry (PB0 NEW-sig 33/84;
  PB1 NEW-sig 44/88 DIFFERS-own-C10 57/88;
  PBA88-PLAIN-M7b6 VPOS 8 sig-ff b5 const M7
  16/16 distinct; C10-1SIG-88-TAIL-M2 VPOS 3
  DIFFERS-from-PB1-sig b5 const M2 10/10 +
  b86 const ba + b87 const 78; QUAD88-2SIG-QM7/
  R2-COLSPLIT VPOS 10 + R2 4/4 UNPAIRED
  d82f/457b/657b/857b + tails + QM7-shared +
  NO const trailer + M-tails NEW; T88-2SIG-
  TM8/TR7-ROWSPLIT sig-31260000/46260000
  VPOS 17 + TM8-by-COL/TR7-by-ROW +
  SPLIT-tails + b84-87 a57b9079 + 112/144
  split + counter db/76/19/147; lencode 348/348
  whole-tier, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R2 rows + tails +
  consts + frame stand; const-count note is
  impl==census-script this tier per census,
  geometry exact, PORT verdict stands; M==RQ
  identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head
  27/76 tail 45/76 b5set {76} NO step, 0 ff
  (b4 base 0x27 step2 16/16, b0 const ff 16/16);
  C head 47/76 tail 59/76 b5set {76} NO step,
  0 ff (b0 const 26 10/10); Q head 5b/76 tail
  d9/76 b5set {76} NO step, 0 ff (b4 base 0x5b
  step2 64/64 exact-set range 5b..d9 wraps-never
  min 0x5b max 0xd9; b0 colsplit 28x31+36x46);
  ring pre-edge off18 (ff/76), edge off19
  (01/77); pre-edge off146 (ff/77) -> edge
  off147 (01/78); exactly 2 ff in 256 (R b4
  exact-set db-step2 256 vals / 128 uniq); R
  head db/76 tail d9/78; b1 const 26 256/256;
  formulas re-derived from T10P372R code text
  (db/76/19/147 hex==dec) + T10P372A/C/Q text
  (raw lencode + b5 const 76 comments); all edge
  pins + head/tail pins + for-list R mid pair +
  colsplit/rowsplit counts + 2 PASS lines each
  py+C. S0/S1 embedded b4/b5 match raw lencode
  (23/76 + 25/76). Ring counter==raw-lencode
  256/256 + Q 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No
  DISSENT on cut bytes (edges480.py EDGES-GREEN,
  A/C/Q NO-ff + ring 2-ff + Q-range exact + R
  counter asserts verified first-hand, never
  assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 232/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; for-line replaced by superset (base for-N
  subset of band, removed 0); fine-norm
  equivalent (for480base.nums subset for480.nums,
  removed 0; C-scope del 0). Content-line
  variance 232 recorded (b478/b479/b480
  232-class; b476 230, b477 231).
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-indented 766->
  768 (+2: 146193/146194) / ranges py-indented
  918->922 (+4; C singletons 771->773 +2 / C
  all-range-guards 940->944 +4, same 6 P372
  blocks both sides; no elif/else-if added either
  side: py file-wide elif 50 both, C else-if 0
  both; deltas agree every side), CLOSED T10P
  prints 2120->2126 +6 both sides, seal 2214->
  2220 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
  GATE-da1ea8de reconcile (viewer-vs-sweep
  first-hand): GATE values agree on PYID/RGRAM/
  smoke/units/for-added-29 (identical 29-set
  both sides)/PINS+58/temps/seal/CLOSED/
  embeds/counters/consts/R2 rows/tails/M==RQ
  identical/extra-table/QM7-shared. Diffs:
  (a) VPOS-C10: GATE counts VPOS 4 (b4,b5+M2,
  b5 range-const via lencode); viewer chain
  counts 3 (viewer convention deducts b5-const:
  missing 4-1; same convention as r77 PBA 7 /
  C10 3 / quad 13 / T 19) -- missing set
  [4,5,84,85] identical both sides; facts
  identical. (b) uniform ledger: GATE sweep-
  ledger counts its own 36th even band
  (memo-present tier); viewer chain stays 39
  (uniform-cells required; C10 10/10 DIVERGE +
  SIG-DIFFERS PB1) -- P338 OPEN, deferred to
  sweep accounting, never re-litigated; facts
  identical. (c) RQ==M ledgers: viewer evens
  54->55 (identical degree; b473 precedent
  counts every degree) / survey 30->31 (every-
  method count); GATE reports M==RQ 16/16
  string-identical SAME-ORDER "reported, not
  gated" -- facts identical (lists/sets equal,
  overlap 16, positional 16/16). (d) tail-
  metric spans: viewer audit uses b84-85 tail
  span (suffix/subseq/tshare (0,0,0,1,1,1)
  all-3); GATE uses full b84-87 cell-tail
  span (suffix-lcs 2/2/2/3/3/3) -- both spans
  computed first-hand this round; underlying
  bytes agree (R2 rows + 90/79 consts);
  facts identical. No code dispute; PORT
  stands both sides.
- CONFIRM evidence (CONVERT-01 rule b):
  memo A-sheet PRESENT for P372 (A-955-q1120
  CONFIRM 50/50 CLEAN: Q1 1x(100,84)+347x
  (104,88) EXACT + PBA ff/M7/b5-76 + C10
  26/M84-85/b5-76 + QUAD 31/46 COLSPLIT
  28+36 + T 31260000/46260000 ROWSPLIT
  112+144; Q2 QM/R2 tails + M-tails NEW +
  TM-by-COL/TR-by-ROW + a57b9079; Q3 lencode
  348/348 + consts 79/84/77/71 + 0 stragglers
  NO D dips) + writer census Q-1120 (consts
  PBA 79 / C10 84 / quad 77 / T88 71;
  committed tables match excl exactly --
  no writer lag this tier, geometry exact,
  PORT verdict stands) + cport commit msgs
  (PYID 11061, RGRAM 22122 both legs per msg;
  py-merge RGRAM 22122) + own full battery
  above. Novelty gated: b52-const-entry variant
  0x94 in CC (P371/P370 0x4a, P369 0xd2,
  P368/P367 0x84, P366 0x72, P365 0xc5,
  P364 0xb9, P363 0xb8); M-tails 16/16 ALL NEW
  vs P371T col-led tails; base has _T10P371C
  but band adds no _T10P372C.
- FWD-check: banked Next-P373 (Q-1120 forward
  note, read first-hand): PB0 @146541 sig
  ef171613 pay84 NEW-sig (39/84 diff vs
  P372PB0, NOT byte-equal) + PB1 26000000
  pay88 @146542 NEW-sig vs P372 heads (68/88
  diff vs P372PB1, NOT byte-equal) + PBA88
  62020000 x16 @146543-558 + C10-region
  26000000 pay88 x10 @146559-568 SAME-as-PB1-
  sig -- b481 C port 940d5f26 (T10P373 pins
  146541..146888, 2226 sealed) + py-merge
  85d0148d ALREADY LANDED (this round's turf,
  b481+; battery next in round); CONSUME-FIRST
  per bank-miss lesson.
- Quiz: no conflicting CLAIM/GATE/FLAG on b480
  (adjacent odd b479 = 6a7ad611 C port live
  used as diff-base only, no verdict beyond;
  adjacent b481 = 940d5f26 C port live, NEXT
  battery this round, no verdict yet; FLAG
  files name no b480 band; DISSENTs q846/847/
  849 unrelated tiers; no conflicting
  CLAIM/GATE/FLAG at filing -- GATE-da1ea8de
  reconciled mid-battery).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r78/
  (build480/, pyid480.log, rgram480py/c.log,
  cmp480.py, seteq480.py, ownloop480.py (+
  w480loop.log), secf480a/b/c.py, edges480.py
  (+.log), tabaudit480.py (+.log), smoke480.log,
  units480.log, band480.diff/addedlines/.addedc,
  for480.nums/added/for480base.nums).

Verdict: PASS. No RED. 348-pin contiguous range
146193..146540 sealed. Round 1/4 = cap 1/4.
