# VERIFY-09b93c5d b478 T10P370 pins 145497..145844 (348 pins) PASS

Seat viewer-r77, first-hand, tree @09b93c5d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r77.
Base e9c52e90 (b477 tip, 2202 tiers sealed; this
seat's VERIFY-e9c52e90 PASS-filed same round,
base-use only, respected). Band = a97cf8ea (py
merge w2b@6e17eacd partial, +6 tiers, +58 pins;
commit msg verified via git log) + 09b93c5d (C
port; parent == a97cf8ea verified via git
rev-list --parents). Chain e9c52e90 -> a97cf8ea
-> 09b93c5d, every sha via git log at takeover,
NO gap-jump. GATE-09b93c5d PASS-functional filed
by sweep2-r82 -- reconciled first-hand below
(values agree; counting-conventions differ where
noted, code facts identical). NO other GATE/FLAG
on b478 at file time.

Banked Next-P370 shape (A-954 + Q-1079 forward
notes + w2b-r33 qTBD-p370 census, all read
first-hand) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 ef928b0c @145497
(S0 head; NEW-sig 1B-off vs P369PB0 @
n145149, 34/84 payload diff, sig b3 IN diff,
positions
[3,4,5,32-35,37-55,72-79]
first-hand, NOT byte-equal) + PB1 19000000
@145498 (S1 head; NEW-sig 56/88 vs
P369PB1 @ n145150, sig b0 IN diff with b1-3
same, positions
[0,4-14,16-19,24,25,28-31,36-43,45,46,48-59,
76-87]
first-hand, NOT byte-equal; diffs
vs own C10[0] n145515 all-10 identical-28
first-hand, sig b0-3 same-sig NOT in diff;
S1 SIG-EQ own C10 (19==19); S1 SIG-DIFFERS
own PB0 (19-vs-ef) and PBA sig (19-vs-92);
C10 10/10 DIVERGE staged+oracle: 39 stays
(even band): NOT TRUE-UNIFORM under viewer
convention (uniform-cells required); P338
uniform-rule dispute stays DEFERRED to sweep
accounting, never re-litigated) +
PBA88-PLAIN-M7b20 sig 92010000 x16 @145499-514
(b0 const 0x92 first-hand) + C10-region
19000000 pay88 x10 @145515-524 (b0 const 0x19
first-hand, SAME-as-PB1-sig) -- all corroborated
against lane code both sides before any battery
step (py==C S0/S1 staged strings; staged-vs-
oracle secf478a/b/c GREEN first-run; no bank-miss).

- Build: seat-private build478/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 ec9374cd...
  (no GATE absolutes cited -- recorded first-hand
  here, never hand-transcribed).
- RGRAMC-PYID 11003/11003 covered=11003/11003
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  default CT cache; +29 vs b477 10974).
- RGRAM py 22006/22006 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 22006/22006 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (22006/22006, sorted +
  raw identical; cmp478.py GREEN).
- PINS-RGRAM cells set-eq 22006/22006 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq478.py GREEN first-run). PINS 22008 lines
  first-hand (2 hdr + 22006 rows; base 21950
  lines / 21948 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 10974->11003 +29/-0 (python
  sets, trailing-';' strip, never comm): 145497
  145498 145499 145500 145506 145507 145513
  145514 145515 145516 145519 145520 145523
  145524 145525 145535 145536 145540 145556
  145572 145588 145589 145602 145603 145663
  145664 145791 145792 145844 (no GATE list at
  battery start -- GATE filed mid-battery with
  the identical 29-set; range 145497..145844
  exact).
  29 = 2 sing (145497 145498 offs 0/1) + A 6
  (head pair 145499/145500 off0/1 + mid pair
  145506/145507 off7/8 + tail pair 145513/
  145514 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 70 NO
  edge) + C 6 (head pair 145515/145516 off0/1
  + mid pair 145519/145520 off4/5 + tail pair
  145523/145524 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 70 NO edge) + Q 7 (head
  145525 off0 + pre-edge/edge 145535/145536
  off10/11 (B5EDGE 70->71) + mid 145540 off15 +
  mid 145556 off31 + mid 145572 off47 + tail
  145588 off63; edge pair-covered, single-sided
  mates unsampled; b5 STEPS 70->71) + R 8 (head
  145589 off0 + colsplit-boundary pair 145602/
  145603 off13/14 (last-82/first-8c) + edge pair
  145663/145664 off74/75 + edge pair 145791/
  145792 off202/203 + tail 145844 off255; both
  counter edges + colsplit boundary pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  22006-21948.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit478.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 181 PASS 0 FAIL first-run (no dead code).
  Inventory: exactly the 12 band tables both
  sides (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC;
  no F/FT, no F0/F1, no BM/BC, no M19/X19, no
  M42/X42/H42/L42, no QB/PT/FM, no RT/TT (ring,
  not ROWTAIL), no QT (R2 carries b84-85 in-row
  + b86/b87 consts); no _T10P370C numeric-head
  probe in band scope) + 1 noted pre-existing
  extra: _T10P370C old-series head-row table
  (line 7724 BOTH trees; band-diff hits are
  CM/CC prefix matches only -- verified
  first-hand harmless, untouched).
  S0 168ch sig ef928b0c NEW-sig 1B-off (34/84
  payload diff vs P369S0, positions
  [3,4,5,32-35,37-55,72-79]
  first-hand, sig b3 IN diff, NOT byte-equal) /
  S1 176ch sig 19000000 NEW-sig (56/88 payload
  diff vs P369S1, positions
  [0,4-14,16-19,24,25,28-31,36-43,45,46,48-59,
  76-87]
  first-hand, sig b0 IN diff with b1-3 same, NOT
  byte-equal; vs own C10 cells 10/10 DIVERGE
  staged+oracle: all-10 diff=28 uniform-diff,
  sig b0-3 same-sig NOT in diff; NOT byte-equal;
  S1 SIG-EQ own C10 (19==19); S1 SIG-DIFFERS
  own PB0 (19-vs-ef); 39 stays (even band)),
  staged as full-payload singletons; S0/S1
  embedded b4/b5 b3/70 + b5/70 match raw lencode.
  AM 16/16 14ch distinct, CM 10/10 10ch diverge
  (b20,84,85,86,87 M5 lane, all 10 distinct),
  M 16/16 16ch distinct, QR 4/4 4ch R2 rows
  e45a/045b/245b/445b exact (tails = R2 + ce/40
  quad-wide exact; full-tail suffix = subseq =
  TSHARE = (2,2,2,3,3,3): pairs (0,1),(0,2),
  (0,3) share trailing 2, pairs (1,2),(1,3),
  (2,3) share trailing 3, all-3 agree first-hand;
  full tuples pairwise unequal, 4 distinct),
  RM 16/16 20ch distinct, RQ 16/16 16ch
  distinct, no QT + no RT + no F (no frags).
  M==RQ 16/16 string-identical SAME-ORDER (M
  list == RQ list, 16ch; QM8 b28,29,30,31,80-83
  by COL m=off&15 vs TR8... RQ8 b28,29,30,31,
  76-79 by ROW r=off>>4 first-hand; string-eq
  HOLDS this tier -- reported, not gated) --
  55th even-band RQ==M instance (evens 54->55);
  29th full/diff survey (survey counts every
  method RQ-vs-M regardless of degree; 6th
  identical case: b472, b474, b475, b476, b477,
  b478).
  M-tails 16/16 ALL NEW vs P369T col-led tails
  (overlap 0; P369T RM 16x7B frame first-hand
  from code, tails last-4B); RQ-tails 16/16 ALL
  NEW vs P369T RQ (overlap 0) + 16/16 ALL NEW
  vs P369T RM (overlap 0); RM-tails 16/16 ALL
  NEW vs P369T RM (overlap 0) + 16/16 ALL NEW
  vs P369T RQ (overlap 0); AM/CM/M/QR/RM/RQ
  0-overlap vs P369 all six (widths P370 vs
  P369: AM 7B vs 8B, CM 5B vs 4B, M 8B vs 7B,
  QR 2B vs 4B, RM 10B vs 7B, RQ 8B vs 7B).
  AC 79, CC 81, QC 76, RC 68; C _N decls
  79/81/76/68 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 const 92 in
  AC (b1 const 01, b2-3 const 00; b5 const 70
  deducted, in AC-missing; b84-87 consts
  2a,30,0c,8d A-lane); C b0 const 19 in CC
  (b1-3 const 00/00/00 first-hand; b5
  const 70 deducted, in CC-missing; b52 const
  0x4a const-entry, in CC; CC has no b20/b84-87
  (all in CM lane)); C b20,b84-87 absent (M5
  lane); Q b0 const 92 1-sig SAME-as-PBA in QC
  first-hand (b1 const 01, b2-3 const 00; b5
  STEPS 70->71 in VPOS (in QC-missing); b84-85
  absent R2 lane, b86 const ce / b87 const 40);
  R b0 VARIES colsplit (absent from RC table,
  in RC-missing; 32x8c iff col>=14 else 82) +
  b1 const 18 in RC table, code-indexed
  first-hand).
  PBA88-PLAIN-M7b20 sig 92010000 x16 (b0 const
  92 via AC b0; b5 const 70 deducted NOT in AC;
  AM 16/16 distinct NO pair; M7 b20,21,22,80-83
  positions STAGED P346A per code comment) +
  PBA sig 92 NEW vs P369 e5 (novelty = new sig
  e5->92 + AM 0-overlap; M7 widths P364 7B /
  P365 8B / P366 7B / P367 6B / P368 9B /
  P369 8B all differ).
  C10-1SIG-88-M5b20 sig 19000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  19000000; CM 10/10 diverge 10ch b20,84,85,
  86,87; CC has no b20/b84-87 (all in CM lane);
  M5 FIRST this lane; b5 const 70 deducted NOT
  in CC).
  QUAD88-1SIG-QM8/R2-B5EDGE 1-sig 92010000
  SAME-sig-as-PBA (b0 const 92 in QC; b5 STEPS
  70->71 edge off10->11 in VPOS; m-tab
  b28,29,30,31,80-83 (M 16/16 16ch NO frags,
  m = off&15 first-hand; QM8 positions staged
  P306Q/P322Q/P346Q per census) + r2 b84,85 R2
  4/4 UNPAIRED BY-ROW (q = off>>4 first-hand);
  tails = R2+ce/40 quad-wide, full-tail pairs
  (2,2,2,3,3,3) per guard + R2 all-distinct +
  QM8-shared-x3 48/48).
  Ring T88-2SIG-COLSPLIT sigs 8c180000 x32
  (col>=14) + 82180000 x224 (b0 col-led:
  32+224 first-hand; in RC-missing; b1 const 18
  256/256 oracle, in RC table; code-TM10
  b0,11,19,27,34,35,80-83 by COL RM 16/16
  20ch (positions FIRST this lane per census) +
  code-TR8 b28,29,30,31,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79 row);
  b84-87 const 645bce40 ring-wide NEW; b4=
  (0x6b+2off)&FF + b5 = 0x71+(off>=75)+(off>=203)
  (C literals 107/113/75/203 verified ==
  0x6b/0x71/75/203; py hex 0x6b/0x71)).
  VPOS partitions re-derived from code: PBA 8
  (missing 9 - 1; b4+M7 b20,21,22,80-83, b5
  const deducted) / C10 6 (missing 7 - 1; b4+M5
  b20,84,85,86,87, b5 const deducted) / quad 12
  (missing 12 - 0; b4,b5+QM8 8+R2 2, b5 STEPS
  varies, NO deduct) / T 20 (missing 20 - 0;
  b0,b4,b5+TM10 10+TR8 8, b0/b5 vary, NO deduct)
  -- all match qTBD-p370 census (8/6/12/20).
  Code-consts vs census-script excl (PBA 79 /
  C10 81 / quad 76 / T88 68): impl 79/81/76/
  68 = census-script EXACT -- no lag on even
  band (deduct-varying-holds; no memo A-sheet
  for P370 at file time; qTBD-p370 census-script
  is the acting sheet). VPOS 8/6/12/20 =
  census EXACT. S-F lag stays 44.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 145497 / S1 145498 / A 145499-514 /
  C 145515-524 / Q 145525-588 / R 145589-844):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode; Q b5 STEP emerges from raw
  lencode 70->71 @off10/11; R explicit counter
  (b4=(0x6b+2off)&FF b5=0x71+(off>=75)+(off>=203);
  py hex 0x6b/0x71; C staged decimal literals
  107/113/75/203 re-derived: 107==0x6b, 113==0x71)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 14ch M7 b20,21,22,80-83; C 10ch M5
  b20,84-87; Q 16ch/4ch QM8 b28,29,30,31,80-83/
  R2 b84,85; R 20ch/16ch TM10 b0,11,19,27,34,35,
  80-83 by COL / TR8 b28,29,30,31,76-79 by ROW;
  R1... R b0 colsplit c>=14).
  C blocks carry T97675/T97680/T97685/T97700/
  T97715/T97735 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 97675 verified
  in py; bounds + byte positions exact: A 7-lane,
  C 5-lane, Q 8ch+2ch + r2, R 10-lane/8-lane),
  A b5 const deducted NOT in AC + C b5 const
  deducted NOT in CC + Q b5 STEP in VPOS via
  lencode (in QC-missing) + R b0/b5 vary (in
  RC-missing) + R counter b4=(107+2off)&FF +
  (113)+(off>=75)+(off>=203) (C literals
  107/113/75/203 verified), temps _t7373-7388
  (base max _t7372, no reuse) +
  _i4477/4479/4482/4485 (base max _i4475, no
  reuse) + _b4476/4478/4480/4481/4483/4484
  (base max _b4474, no reuse), union 4476-4485
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P369R close (C "T10P3700 singleton" after
  "CLOSED T10P369R"; py return 0 + S0 guard
  97675 after "CLOSED T10P369R" print), at
  dispatch tail (P370R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches census geometry (PB0 NEW-sig 1B-off
  34/84; PB1 NEW-sig 56/88 SAME-own-C10 28/88;
  PBA88-PLAIN-M7b20 VPOS 8 sig-92 b5 const M7
  16/16 distinct; C10-1SIG-88-M5b20 VPOS 6
  SAME-as-PB1-sig b5 const M5 10/10 FIRST;
  QUAD88-1SIG-QM8/R2-B5EDGE VPOS 12 + R2 4/4
  UNPAIRED e45a/045b/245b/445b + blcs-(2,2,2,3,3,3)
  + R2-distinct + NO frags + M-tails NEW;
  T88-2SIG-COLSPLIT VPOS 20 + TM10-by-COL/
  TR8-by-ROW + SPLIT-tails + b84-87 645bce40 +
  32/224 colsplit + counter 6b/71/75/203;
  lencode 348/348 whole-tier, NO D dips) incl
  exact values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + LCS + frame + consts stand; const-count
  note is impl==census-script this tier per
  census, geometry exact, PORT verdict stands;
  M==RQ identical first-hand this tier, tier
  stands).
- Edges via counter formula first-hand: A head
  b7/70 tail d5/70 b5set {70} NO step, 0 ff
  (b4 base 0xb7 step2 16/16, b0 const 92 16/16);
  C head d7/70 tail e9/70 b5set {70} NO step,
  0 ff (b0 const 19 10/10); Q head eb/70
  pre-edge off10 (ff/70) edge off11 (01/71)
  b5set {70,71} STEP, 1 ff (b4 base 0xeb step2
  64/64 exact-set range eb..69 wraps-once
  min 0x01 max 0xff); ring pre-edge off74
  (ff/71), edge off75 (01/72); pre-edge off202
  (ff/72) -> edge off203 (01/73); exactly 2 ff
  in 256 (R b4 exact-set 6b-step2 256 vals / 128
  uniq); R head 6b/71 (b0 82) tail 69/73
  (b0 8c); formulas re-derived from T10P370R
  code text (6b/71/75/203 hex==dec) +
  T10P370A/C/Q text (raw lencode + b5 const/STEP
  comments); all edge pins + head/tail pins +
  for-list R mid/boundary pins + 2 PASS lines
  each py+C. S0/S1 embedded b4/b5 match raw
  lencode (b3/70 + b5/70). Ring counter==raw-
  lencode 256/256 + Q 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges478.py EDGES-GREEN, A/C NO-ff
  + Q single-ff + ring 2-ff range-with-wrap +
  colsplit 32/224 exact + R counter asserts
  verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 232/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 232 content / 0 del (content-line
  variance 232 recorded: b470/b471/b472/b473/
  b478 232-class; b468/b469/b474/b475/b477
  231-class; b476 230 new class); for-line
  replaced by superset (base for-N subset of
  band, removed 0); fine-norm equivalent
  (for478base.nums subset for478.nums, removed
  0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-indented 762->764
  (+2: 145497/145498) / ranges py-indented 910->
  914 (+4; C singletons 767->769 +2 / C
  all-range-guards 932->936 +4, same 6 P370 blocks
  both sides; no elif/else-if added either side:
  py file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2108->2114 +6 both sides, seal 2202->2208 +6
  (commit msgs; offset +94 vs CLOSED-T10P stable):
  all agree, no slip (absolute seal inherits lane
  tally; delta verified).
  GATE-09b93c5d reconcile (viewer-vs-sweep
  first-hand): GATE values agree on PYID/RGRAM/
  smoke/units/for-added-29/PINS+58/temps/seal/
  CLOSED/embeds/counters/consts/M==RQ identical/
  tails/R2 rows/extra table. Diffs: (a) VPOS-C10
  7-vs-6 + VPOS-quad 11-vs-12: code missing-sets
  identical (CC [4,5,20,84-87], QC 12-entry set);
  GATE counts const-b5 in C10 and deducts varying-
  b5 in quad; viewer+qTBD-census deduct const-b5
  and keep varying-b5 (deduct-only-when-const,
  viewer convention since r76; census VPOS
  6/12). Facts identical. (b) dispatch-count
  patterns: GATE C labels carry py-pattern values
  (762->764 / 910->914); viewer counts with
  stated patterns (py 762->764 / 910->914; C
  767->769 / 932->936) -- deltas +2/+4 agree
  both sides; py file-wide elif absolute is 50
  both (no elif added), C else-if 0 both.
  (c) RQ==M ledgers: viewer evens 55 / survey 29
  (every-method count); GATE reports holds, not
  gated -- facts identical. (d) extra _T10P370C:
  pre-existing both trees (line 7724), untouched
  (band-diff hits are CM/CC prefix matches only)
  -- harmless, noted both sides.
  No code dispute; PORT stands both sides.
- CONFIRM evidence (CONVERT-01 rule b):
  NO memo A-sheet for P370 at file time
  (A-95x-q108x + Q-108x-w2b ABSENT per GATE
  filename survey). Substitute first-hand: writer
  census NOTE-w2b-r33-qTBD-p370 (consts PBA 79 /
  C10 81 / quad 76 / T88 68; committed tables
  match excl exactly -- no writer lag this tier,
  geometry exact, PORT verdict stands) +
  cport commit msgs (PYID 11003, RGRAM 22006
  both legs per msg; py-merge RGRAM 22006) +
  own full battery above. Novelty gated:
  b52-const-entry variant 0x4a in CC (P369 0xd2,
  P368 0x84, P367 0x84, P366 0x72, P365 0xc5,
  P364 0xb9, P363 0xb8); M-tails 16/16 ALL NEW
  vs P369T col-led tails.
- FWD-check: banked Next-P371 (qTBD-p370 forward
  note, read first-hand): PB0 @145845 sig
  ef17960c pay84 NEW-sig (29/84 diff vs P370PB0,
  NOT byte-equal) + PB1 18000000 pay88 @145846
  NEW-sig vs P370 heads (50/88 diff vs P370PB1,
  NOT byte-equal) + PBA88 c9010000 x16 @145847-
  862 + C10-region 18000000 pay88 x10 @145863-
  872 SAME-as-PB1-sig -- b479 py-merge 26469ef3
  + C port 6a7ad611 ALREADY LANDED (next battery,
  no poll-wait); pre-corroboration at that
  battery; CONSUME-FIRST per bank-miss lesson.
- Quiz: no conflicting CLAIM/GATE/FLAG on b478
  (adjacent odds b477 = e9c52e90 C port live
  used as diff-base only, no verdict beyond;
  adjacent odds b479 = 6a7ad611 C port live,
  next battery, no verdict beyond; FLAG files
  name no b478 band; DISSENTs are q846/847/849
  unrelated tiers).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r77/
  (build478/, pyid478.log, rgram478py/c.log,
  cmp478.py, seteq478.py, ownloop478.py (+
  w478loop.log), secf478a/b/c.py, edges478.py
  (+.log), tabaudit478.py (+.log), smoke478.log,
  units478.log, band478.diff/addedlines/.addedc,
  for478.nums/added/for478base.nums).

Verdict: PASS. No RED. 348-pin contiguous range
145497..145844 sealed. Round 3/4.
