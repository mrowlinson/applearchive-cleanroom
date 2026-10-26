# VERIFY-6a7ad611 b479 T10P371 pins 145845..146192 (348 pins) PASS

Seat viewer-r77, first-hand, tree @6a7ad611,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r77.
Base 09b93c5d (b478 tip, 2208 tiers sealed; this
seat's VERIFY-09b93c5d PASS-filed same round,
base-use only, respected). Band = 26469ef3 (py
merge w2b@17479fd4 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 6a7ad611 (C
port; parent == 26469ef3 verified via git
rev-list --parents). Chain 09b93c5d -> 26469ef3
-> 6a7ad611, every sha via git log at takeover,
NO gap-jump. GATE-6a7ad611 PASS-functional filed
by sweep-r81 -- reconciled first-hand below
(values agree; span-convention noted, code facts
identical). NO other GATE/FLAG on b479 at file
time.

Banked Next-P371 shape (A-954 + Q-1079 forward
notes + w2b-r33 qTBD-p371 census [8/8 CAP] final
backfill, all read first-hand) CONSUMED FIRST
and VERIFIED first-hand EXACT: PB0 ef17960c
@145845 (S0 head; NEW-sig 29/84 vs P370PB0 @
n145497, sig b1,2 IN diff with b0,b3 same,
positions
[1,2,4-11,13,15-19,24,56-63,80-83]
first-hand, NOT byte-equal) + PB1 18000000
@145846 (S1 head; NEW-sig 50/88 vs
P370PB1 @ n145498, sig b0 IN diff with b1-3
same, positions
[0,4,5,9-11,16-43,60-71,84-87]
first-hand, NOT byte-equal; diffs
vs own C10[0] n145863 all-10 identical-26
first-hand, sig b0-3 same-sig NOT in diff;
S1 SIG-EQ own C10 (18==18); S1 SIG-DIFFERS
own PB0 (18-vs-ef) and PBA sig (18-vs-c9);
C10 10/10 DIVERGE staged+oracle: 39 stays
(odd band): NOT TRUE-UNIFORM under viewer
convention (uniform-cells required); P338
uniform-rule dispute stays DEFERRED to sweep
accounting, never re-litigated) +
PBA88-PLAIN-M6b40 sig c9010000 x16 @145847-862
(b0 const 0xc9 first-hand) + C10-region
18000000 pay88 x10 @145863-872 (b0 const 0x18
first-hand, SAME-as-PB1-sig) -- all corroborated
against lane code both sides before any battery
step (py==C S0/S1 staged strings; staged-vs-
oracle secf479a/b/c GREEN first-run; no
bank-miss).

- Build: seat-private build479/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 ab91cec1...
  (no GATE absolutes cited -- recorded first-hand
  here, never hand-transcribed).
- RGRAMC-PYID 11032/11032 covered=11032/11032
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  default CT cache; +29 vs b478 11003).
- RGRAM py 22064/22064 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 22064/22064 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (22064/22064, sorted +
  raw identical; cmp479.py GREEN).
- PINS-RGRAM cells set-eq 22064/22064 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq479.py GREEN first-run). PINS 22066 lines
  first-hand (2 hdr + 22064 rows; base 22008
  lines / 22006 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 11003->11032 +29/-0 (python
  sets, trailing-';' strip, never comm): 145845
  145846 145847 145848 145854 145855 145861
  145862 145863 145864 145867 145868 145871
  145872 145873 145888 145889 145904 145919
  145920 145936 145937 146047 146048 146112
  146175 146176 146177 146192 (no GATE list at
  battery start -- GATE filed mid-battery with
  the identical 29-set; range 145845..146192
  exact).
  29 = 2 sing (145845 145846 offs 0/1) + A 6
  (head pair 145847/145848 off0/1 + mid pair
  145854/145855 off7/8 + tail pair 145861/
  145862 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 73 NO
  edge) + C 6 (head pair 145863/145864 off0/1
  + mid pair 145867/145868 off4/5 + tail pair
  145871/145872 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 73 NO edge) + Q 7 (head
  145873 off0 + row pair 145888/145889 off15/16
  + mid 145904 off31 + pre-edge/edge 145919/
  145920 off46/47 + tail 145936 off63; row
  boundary off16 pair-covered, off32 single-
  sided (mate off32 145905 unsampled), B5EDGE
  @off47 pair-covered; b5 STEPS 73->74) + R 8
  (head 145937 off0 + edge pair 146047/146048
  off110/111 + mid 146112 off175 + edge pair
  146175/146176 off238/239 + post-edge mate
  146177 off240 + tail 146192 off255; both
  counter edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  22064-22006.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit479.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 187 PASS 0 FAIL first-run (no dead code).
  Inventory: exactly the 12 band tables both
  sides (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC;
  no F/FT, no F0/F1, no BM/BC, no M19/X19, no
  M42/X42/H42/L42, no QB/PT/FM, no RT/TT (ring,
  not ROWTAIL), no QT (R5 carries b40,84-87
  in-row, no const trailer); no _T10P371C
  numeric-head probe in band scope) + 1 noted
  pre-existing extra: _T10P371C old-series
  head-row table (P-head row n<=29614) in BOTH
  trees (base has it at same shape; band-diff
  hits are CM/CC prefix matches only -- verified
  first-hand harmless, untouched).
  S0 168ch sig ef17960c NEW-sig (29/84 payload
  diff vs P370S0, positions
  [1,2,4-11,13,15-19,24,56-63,80-83]
  first-hand, sig b1,2 IN diff with b0,b3 same,
  NOT byte-equal) / S1 176ch sig 18000000
  NEW-sig (50/88 payload diff vs P370S1,
  positions
  [0,4,5,9-11,16-43,60-71,84-87]
  first-hand, sig b0 IN diff with b1-3 same,
  NOT byte-equal; vs own C10 cells 10/10
  DIVERGE staged+oracle: all-10 diff=26
  uniform-diff, sig b0-3 same-sig NOT in diff;
  NOT byte-equal; S1 SIG-EQ own C10 (18==18);
  S1 SIG-DIFFERS own PB0 (18-vs-ef); 39 stays
  (odd band)), staged as full-payload singletons;
  S0/S1 embedded b4/b5 6b/73 + 6d/73 match raw
  lencode.
  AM 16/16 12ch distinct, CM 10/10 4ch diverge
  (b84,85 M2 lane, all 10 distinct), M 16/16
  12ch distinct, QR 4/4 10ch R5 rows
  7fa0b0a3ed/80712873aa/80477654f7/80677654f7
  exact (tails = R5 b84-87 + b40 head: b40 ==
  R5-row[0] 4/4 + tail == R5-row[1:5] 4/4;
  full-tuple (b40+b84-87) suffix = subseq =
  TSHARE = (0,0,0,0,0,3): pair (2,3) shares
  trailing 3, rest 0, all-3 agree first-hand
  on b84-87 span; full-row span (b40+b84-87)
  corroborated first-hand: suffix (0,0,0,0,0,3)
  / subseq (0,0,0,1,1,4) / tshare (0,0,0,1,1,3)
  (shared head 0x80 across rows 1-3) -- span-
  convention noted, facts identical; full
  tuples pairwise unequal, distinct 4), RM
  16/16 18ch distinct, RQ 16/16 16ch distinct,
  no QT + no RT + no F (no frags).
  M!=RQ this tier (FIRST non-identical in r77
  chain): DISJOINT-full + TAIL-IDENTITY,
  P365/b473-pattern -- lists differ, sets
  differ, cell-overlap 0/16, positional-same
  0/16, TAIL-IDENTITY M-tail(b80-83)==RQ-tail
  (b76-79) ordered 16/16 + set-eq 16/16,
  shared-lane-b47 overlap 0/16 (all first-hand;
  NOT string-eq -- reported, not gated) --
  57th odd-band RQ==M instance (odds 56->57;
  b473 tails-shared precedent counts every
  degree); 30th full/diff survey (survey counts
  every method RQ-vs-M regardless of degree;
  FIRST non-identical case in chain: b472-b478
  identical, b479 disjoint+tail-identity).
  M-tails 16/16 ALL NEW vs P370T col-led tails
  (overlap 0; P370T RM 16x10B frame first-hand
  from code, tails last-4B) and vs P370T
  row-led tails (overlap 0); RQ-tails 16/16
  ALL NEW vs P370T RQ (overlap 0) and vs P370T
  RM (overlap 0); RM-tails 16/16 ALL NEW vs
  P370T RM (overlap 0) and vs P370T RQ
  (overlap 0); AM/CM/M/QR/RM/RQ 0-overlap vs
  P370 all six (widths P371 vs P370: AM 6B vs
  7B, CM 2B vs 5B, M 6B vs 8B, QR 5B vs 2B, RM
  9B vs 10B, RQ 8B vs 8B).
  AC 80, CC 84, QC 75, RC 69; C _N decls
  80/84/75/69 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 const c9 in
  AC (b1 const 01, b2-3 const 00; b5 const 73
  deducted, in AC-missing; b84-87 consts
  eb,09,cb,55 A-lane); C b0 const 18 in CC
  (b1-3 const 00/00/00 first-hand; b5 const 73
  deducted, in CC-missing; b52 const 0x4a
  const-entry, in CC; CC has no b84,85 (both
  in CM lane)); C b84,85 absent (M2 lane);
  Q b0 const c9 1-sig SAME-as-PBA in QC
  first-hand (b1 const 01, b2-3 const 00; b5
  STEPS 73->74 in VPOS (in QC-missing); b80-87
  absent QM6/R5 lanes, no b86/b87 consts this
  tier -- R5 carries b84-87 in-row); R b0
  const c9 + b1 const 18 in RC table,
  code-indexed first-hand).
  PBA88-PLAIN-M6b40 sig c9010000 x16 (b0 const
  c9 via AC b0; b5 const 73 deducted NOT in AC;
  AM 16/16 distinct NO pair; M6 b40,41,80-83
  positions STAGED P363A per code comment) +
  PBA sig c9 NEW vs P370 92 (novelty = new sig
  92->c9 + AM 0-overlap; M6 widths P364 7B /
  P365 8B / P366 7B / P367 6B / P368 9B /
  P369 8B / P370 7B all differ).
  C10-1SIG-88-TAIL-M2 sig 18000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  18000000; CM 10/10 diverge 4ch b84,85;
  CC has no b84,85 (both in CM lane); M2 FIRST
  this lane; b5 const 73 deducted NOT in CC).
  QUAD88-1SIG-QM6/R5-B5EDGE 1-sig c9010000
  SAME-sig-as-PBA (b0 const c9 in QC; b5 STEPS
  73->74 edge off46->47 in VPOS; m-tab
  b39,47,80-83 (M 16/16 12ch NO frags, m =
  off&15 first-hand; QM6 positions FIRST this
  lane per code comment) + r5 b40,84-87 R5 4/4
  UNPAIRED BY-ROW (q = off>>4 first-hand);
  tails = R5 rows, full-tuple pairs (0,0,0,0,0,
  3) per guard + R5 all-distinct + QM6-shared-
  x3 48/48).
  Ring T88-STANDARD-TM9/TR8 sig c9180000 x256
  (b0 const c9 256/256 oracle, in RC table; b1
  const 18 256/256 oracle, in RC table; code-TM9
  b50,52,53,54,55,80-83 by COL RM 16/16 18ch
  (positions FIRST this lane per code) +
  code-TR8 b40,41,46,47,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79 row);
  b84-87 const 877654f7 ring-wide NEW; b4=
  (0x23+2off)&FF + b5 = 0x74+(off>=111)+
  (off>=239) (C literals 35/116/111/239 verified
  == 0x23/0x74/111/239; py hex 0x23/0x74)).
  VPOS partitions re-derived from code: PBA 7
  (missing 8 - 1; b4+M6 b40,41,80-83, b5 const
  deducted) / C10 3 (missing 4 - 1; b4+M2
  b84,85, b5 const deducted) / quad 13
  (missing 13 - 0; b4,b5+QM6 6+R5 5, b5 STEPS
  varies, NO deduct) / T 19 (missing 19 - 0;
  b4,b5+TM9 9+TR8 8, b0/b5 vary, NO deduct)
  -- all match qTBD-p371 census (7/3/13/19).
  Code-consts vs census-script excl (PBA 80 /
  C10 84 / quad 75 / T88 69): impl 80/84/75/
  69 = census-script EXACT -- no lag on odd
  band (deduct-varying-holds; no memo A-sheet
  for P371 at file time; qTBD-p371 census-script
  is the acting sheet). VPOS 7/3/13/19 =
  census EXACT. S-F lag stays 44.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 145845 / S1 145846 / A 145847-862 /
  C 145863-872 / Q 145873-936 / R 145937-192):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode; Q b5 STEP emerges from raw
  lencode 73->74 @off47; R explicit counter
  (b4=(0x23+2off)&FF b5=0x74+(off>=111)+(off>=239);
  py hex 0x23/0x74; C staged decimal literals
  35/116/111/239 re-derived: 35==0x23, 116==0x74)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 12ch M6 b40,41,80-83; C 4ch M2 b84,85; Q
  12ch/10ch QM6 b39,47,80-83/R5 b40,84-87; R
  18ch/16ch TM9 b50,52,53,54,55,80-83 by COL /
  TR8 b40,41,46,47,76-79 by ROW).
  C blocks carry T97907/T97912/T97917/T97932/
  T97947/T97967 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 97907 verified
  in py; bounds + byte positions exact: A 6-lane,
  C 2-lane, Q 6ch+5ch + r5, R 9-lane/8-lane),
  A b5 const deducted NOT in AC + C b5 const
  deducted NOT in CC + Q b5 STEP in VPOS via
  lencode (in QC-missing) + R b0/b5 vary... R b0
  CONST c9 in RC (in table, colsplit GONE this
  tier) + R counter b4=(35+2off)&FF +
  (116)+(off>=111)+(off>=239) (C literals
  35/116/111/239 verified), temps _t7389-7404
  (base max _t7388, no reuse) +
  _i4487/4489/4492/4495 (base max _i4485, no
  reuse) + _b4486/4488/4490/4491/4493/4494
  (base max _b4484, no reuse), union 4486-4495
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P370R close (C "T10P3710 singleton" after
  "CLOSED T10P370R"; py return 0 + S0 guard
  97907 after "CLOSED T10P370R" print), at
  dispatch tail (P371R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches census geometry (PB0 NEW-sig 29/84;
  PB1 NEW-sig 50/88 SAME-own-C10 26/88;
  PBA88-PLAIN-M6b40 VPOS 7 sig-c9 b5 const M6
  16/16 distinct; C10-1SIG-88-TAIL-M2 VPOS 3
  SAME-as-PB1-sig b5 const M2 10/10 FIRST +
  b86 const a3 + b87 const ed; QUAD88-1SIG-QM6/
  R5-B5EDGE VPOS 13 + R5 4/4 UNPAIRED
  7fa0b0a3ed/80712873aa/80477654f7/80677654f7 +
  tail-(0,0,0,0,0,3) + R5-distinct + NO const
  trailer + M-tails NEW; T88-STANDARD-TM9/TR8
  sig-c9180000 VPOS 19 + TM9-by-COL/TR8-by-ROW
  + SPLIT-tails + b84-87 877654f7 + colsplit
  GONE (b0 const) + counter 23/74/111/239;
  lencode 348/348 whole-tier, NO D dips) incl
  exact values (PBA/C10/QUAD/T88 sigs, R5 rows +
  tails + LCS + frame + consts stand; const-count
  note is impl==census-script this tier per
  census, geometry exact, PORT verdict stands;
  M!=RQ disjoint+tail-identity first-hand this
  tier, tier stands).
- Edges via counter formula first-hand: A head
  6f/73 tail 8d/73 b5set {73} NO step, 0 ff
  (b4 base 0x6f step2 16/16, b0 const c9 16/16);
  C head 8f/73 tail a1/73 b5set {73} NO step,
  0 ff (b0 const 18 10/10); Q head a3/73
  pre-edge off46 (ff/73) edge off47 (01/74)
  b5set {73,74} STEP, 1 ff (b4 base 0xa3 step2
  64/64 exact-set range a3..21 wraps-once
  min 0x01 max 0xff); ring pre-edge off110
  (ff/74), edge off111 (01/75); pre-edge off238
  (ff/75) -> edge off239 (01/76); exactly 2 ff
  in 256 (R b4 exact-set 23-step2 256 vals / 128
  uniq); R head 23/74 tail 21/76; formulas
  re-derived from T10P371R code text (23/74/
  111/239 hex==dec) + T10P371A/C/Q text (raw
  lencode + b5 const/STEP comments); all edge
  pins + head/tail pins + for-list R mid + mate
  pins + 2 PASS lines each py+C. S0/S1 embedded
  b4/b5 match raw lencode (6b/73 + 6d/73).
  Ring counter==raw-lencode 256/256 + Q 64/64 +
  A 16/16 + C 10/10. Odd-lencode 348/348
  (16+10+64+256+2). No DISSENT on cut bytes
  (edges479.py EDGES-GREEN, A/C NO-ff + Q
  single-ff + ring 2-ff range-with-wrap + Q-range
  exact + R counter asserts verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 232/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 232 content / 0 del (content-line
  variance 232 recorded: b470/b471/b472/b473/
  b478/b479 232-class; b468/b469/b474/b475/b477
  231-class; b476 230 new class); for-line
  replaced by superset (base for-N subset of
  band, removed 0); fine-norm equivalent
  (for479base.nums subset for479.nums, removed
  0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-indented 764->766
  (+2: 145845/145846) / ranges py-indented 914->
  918 (+4; C singletons 769->771 +2 / C
  all-range-guards 936->940 +4, same 6 P371 blocks
  both sides; no elif/else-if added either side:
  py file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2114->2120 +6 both sides, seal 2208->2214 +6
  (commit msgs; offset +94 vs CLOSED-T10P stable):
  all agree, no slip (absolute seal inherits lane
  tally; delta verified).
  GATE-6a7ad611 reconcile (viewer-vs-sweep
  first-hand): GATE values agree on PYID/RGRAM/
  smoke/units/for-added-29/PINS+58/temps/seal/
  CLOSED/embeds/counters/consts/R5 rows/tails/
  extra table/QM6-shared/tail-identity. Diffs:
  (a) uniform ledger: GATE sweep-ledger counts
  its own 26th TRUE-uniform (SIG-EQ +
  differs-PB0); viewer chain stays 39
  (uniform-cells required; C10 10/10 DIVERGE)
  -- P338 dispute OPEN, deferred to sweep
  accounting, never re-litigated; facts
  identical. (b) RQ==M ledgers: viewer odds 57
  / survey 30 (every-degree count; b473 tails-
  shared precedent) vs GATE 57th odd / FULL-
  identity degree unchanged (b477 12th stands;
  this tier DISJOINT, not full) -- facts
  identical (lists/sets differ, cell-overlap 0,
  positional 0/16, tail-identity ordered+seteq
  16/16, shared-lane-b47 0/16). (c) tail-metric
  spans: viewer audit uses b84-87 tail span
  (suffix/subseq/tshare (0,0,0,0,0,3) all-3);
  GATE uses full R5-row span (suffix
  (0,0,0,0,0,3) / subseq (0,0,0,1,1,4) /
  tshare (0,0,0,1,1,3)) -- both spans
  corroborated first-hand this round; facts
  identical. (d) dispatch-count patterns: viewer
  counts stated with patterns (py 766/918; C
  771/940); GATE C labels carry py-pattern
  values on some lines -- deltas +2/+4 agree
  both sides; py file-wide elif absolute is 50
  both (no elif added), C else-if 0 both.
  No code dispute; PORT stands both sides.
- CONFIRM evidence (CONVERT-01 rule b):
  NO memo A-sheet for P371 at file time
  (A-959-q1083 ABSENT per GATE filename survey;
  Q-1083 UNANSWERED at gate time; viewer has no
  P371 geometry answer on file). Substitute
  first-hand: writer census NOTE-w2b-r33-qTBD-
  p371 [8/8 CAP] (consts PBA 80 / C10 84 /
  quad 75 / T88 69; committed tables match excl
  exactly -- no writer lag this tier, geometry
  exact, PORT verdict stands) + cport commit
  msgs (PYID 11032, RGRAM 22064 both legs per
  msg; py-merge RGRAM 22064) + own full battery
  above. Novelty gated: b52-const-entry variant
  0x4a in CC (P370 0x4a same value this tier,
  carry; P369 0xd2, P368/P367 0x84, P366 0x72,
  P365 0xc5, P364 0xb9, P363 0xb8); M-tails
  16/16 ALL NEW vs P370T col-led tails.
- FWD-check: banked Next-P372 (qTBD-p371 forward
  note, read first-hand): PB0 @146193 sig
  ef17160d pay84 NEW-sig (33/84 diff, NOT
  byte-equal) + PB1 1f000000 pay88 @146194
  NEW-sig (44/88 diff, NOT byte-equal) + PBA88
  ff010000 x16 @146195-210 + C10-region 26000000
  pay88 x10 @146211-220 DIFFERS-from-PB1-sig --
  b480 C port da1ea8de + b481 py-merge 85d0148d
  ALREADY LANDED (next round's turf, b480+;
  beyond cap 4/4; no battery this round);
  pre-corroboration deferred to next round;
  CONSUME-FIRST per bank-miss lesson.
- Quiz: no conflicting CLAIM/GATE/FLAG on b479
  (adjacent evens b478 = 09b93c5d C port live
  used as diff-base only, no verdict beyond;
  adjacent b480 = da1ea8de C port live, NEXT
  ROUND's turf, no verdict beyond; FLAG files
  name no b479 band; DISSENTs are q846/847/849
  unrelated tiers).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r77/
  (build479/, pyid479.log, rgram479py/c.log,
  cmp479.py, seteq479.py, ownloop479.py (+
  w479loop.log), secf479a/b/c.py, edges479.py
  (+.log), tabaudit479.py (+.log), smoke479.log,
  units479.log, band479.diff/addedlines/.addedc,
  for479.nums/added/for479base.nums).

Verdict: PASS. No RED. 348-pin contiguous range
145845..146192 sealed. Round 4/4 = cap 4/4.
