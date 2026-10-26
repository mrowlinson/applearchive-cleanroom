# VERIFY-648dd0de b482 T10P374 pins 146889..147236 (348 pins) PASS

Seat viewer-r78, first-hand, tree @648dd0de,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r78.
Base 940d5f26 (b481 tip, 2226 tiers sealed; this
seat's VERIFY-940d5f26 PASS-filed same round,
base-use only, respected). Band = 83dbd944 (py
merge w2b@635e3941 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 648dd0de (C
port; parent == 83dbd944 verified via git
rev-list --parents). Chain 940d5f26 -> 83dbd944
-> 648dd0de, every sha via git log at takeover,
NO gap-jump. GATE-648dd0de PASS-functional filed
by sweep2-r83 (pre-battery) -- reconciled
first-hand below (values agree; RQ==M ledger
degree phrasing + edge-triple naming differ,
code facts identical). NO other GATE/FLAG on
b482 at file time.

Banked Next-P374 shape (Q-1121 forward note,
read first-hand) CONSUMED FIRST and VERIFIED
first-hand EXACT vs Q-1122/A-957: PB0
6e586913 @146889 (S0 head; NEW-sig 33/84 vs
P373PB0 @ n146541, sig b0-2 IN diff,
positions
[0,1,2,4,5,13-21,24-30,56-67]
first-hand, NOT byte-equal) + PB1 26000000
@146890 (S1 head; sig-REPEAT of P373PB1 sig
(b0-3 same, NOT in diff positions); 48/88
payload diff vs P373PB1 @ n146542, positions
[4,5,11,19-47,64-75,84-87]
first-hand, NOT byte-equal; diffs vs own C10
cells 45 x10 staged+oracle; sig b0-3 same-sig
NOT in diff; S1 SIG-DIFFERS own C10 (26-vs-20)
and own PB0 (26-vs-6e); C10 10/10 DIVERGE
staged+oracle: 39 stays (even band): NOT TRUE-
UNIFORM under viewer convention (uniform-cells
required); P338 uniform-rule dispute stays
DEFERRED to sweep accounting, never
re-litigated) + PBA88 sig 5e020000 x16
@146891-906 (b0 const 0x5e first-hand) + C10-
region 20000000 pay88 x10 @146907-916 (b0
const 0x20 first-hand, DIFFERS-from-PB1-sig)
-- all corroborated against lane code both
sides plus Q-1122/A-957 before any battery step
(py==C S0/S1 staged strings; staged-vs-oracle
secf482a/b/c GREEN first-run; no bank-miss).

- Build: seat-private build482/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 896538f5...
  (recorded first-hand here, never
  hand-transcribed).
- RGRAMC-PYID 11119/11119 covered=11119/11119
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch;
  +29 vs b481 11090; background run, result
  delivered terminal).
- RGRAM py 22238/22238 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 22238/22238 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (22238/22238, sorted +
  raw identical; cmp482.py GREEN).
- PINS-RGRAM cells set-eq 22238/22238 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq482.py GREEN). PINS 22240 lines
  first-hand (2 hdr + 22238 rows; base 22182
  lines / 22180 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 11090->11119 +29/-0 (python
  sets, trailing-';' strip, never comm): 146889
  146890 146891 146892 146898 146899 146905
  146906 146907 146908 146911 146912 146915
  146916 146917 146932 146943 146944 146949
  146964 146980 146981 147071 147072 147136
  147199 147200 147201 147236 (= GATE 29-set
  exact, first-hand both sides; range
  146889..147236 exact).
  29 = 2 sing (146889 146890 offs 0/1) + A 6
  (head pair 146891/146892 off0/1 + mid pair
  146898/146899 off7/8 + tail pair 146905/
  146906 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 7b NO
  edge) + C 6 (head pair 146907/146908 off0/1
  + mid pair 146911/146912 off4/5 + tail pair
  146915/146916 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 7b NO edge) + Q 7 (head
  146917 off0 + mid 146932 off15 + B5EDGE pair
  146943/146944 off26/27 + mid 146949 off32 +
  mid 146964 off47 + tail 146980 off63; edge
  pair-covered, first-hand) + R 8 (head 146981
  off0 + edge pair 147071/147072 off90/91 + mid
  147136 off155 + edge triple 147199/147200/
  147201 off218/219/220 (pre-edge+edge+post-
  edge, first-hand; GATE names the same triple)
  + tail 147236 off255; both counter edges
  pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  22238-22180.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit482.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 188 PASS 0 FAIL (1 own-script fix:
  py-Q-b5steps comment text vs actual "b5=
  0x7b+(off>=27)" spacing; tree untouched).
  Inventory: exactly the 12 band tables both
  sides (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC;
  no F/FT, no F0/F1, no BM/BC, no M19/X19, no
  M42/X42/H42/L42, no QB/PT/FM, no RT/TT (ring,
  not ROWTAIL), no QT (R2 carries b84,85
  in-row, no const trailer); no _T10P374C
  numeric-head probe in either tree; base P373
  has no _T10P373C either -- verified harmless,
  nothing carried forward).
  S0 168ch sig 6e586913 NEW-sig (33/84 payload
  diff vs P373S0, positions
  [0-2,4,5,13-21,24-30,56-67]
  first-hand, sig b0-2 IN diff, NOT byte-equal)
  / S1 176ch sig 26000000 sig-REPEAT of P373PB1
  (b0-3 same, NOT in diff; 48/88 payload diff
  vs P373S1, positions
  [4,5,11,19-47,64-75,84-87]
  first-hand, NOT byte-equal; vs own C10 cells
  45 x10 staged+oracle; sig b0-3 same-sig NOT
  in diff; NOT byte-equal; S1 SIG-DIFFERS own
  C10 (26-vs-20) and own PB0 (26-vs-6e); 39
  stays (even band)), staged as full-payload
  singletons; S0/S1 embedded b4/b5 93/7b +
  95/7b match raw lencode.
  AM 16/16 7ch distinct, CM 10/10 6ch diverge
  (b84,85,86 M3 lane, all 10 distinct), M 16/16
  7ch distinct, QR 4/4 4ch R2 rows
  ec37/0c38/2c38/4c38 exact (tails = R2 b84,85
  2B: tail == row 4/4; full 2B-tail pairs
  suffix/subseq/tshare (0,0,0,1,1,1) all-3
  viewer b84-85 span first-hand; writer/GATE
  full-tail b84-87 span suffix-lcs 2/2/2/3/3/3
  corroborated first-hand this round (own
  computation: (2,2,2,3,3,3) exact; GATE also
  reports trailing=TSHARE=subseq 2/2/2/3/3/3
  all-3 agree) -- both spans first-hand, bytes
  agree (R2 rows + b2/b8 consts); full tuples
  pairwise unequal, distinct 4), RM 16/16 9ch
  distinct, RQ 16/16 7ch distinct, no QT + no
  RT + no F (no frags).
  M==RQ this tier (IDENTICAL lists same-order,
  sets equal, cell-overlap 16/16, positional
  16/16; TAIL-IDENTITY ordered+seteq 16/16 as a
  consequence) -- viewer evens 55->56 (b473
  tails-shared precedent counts every degree);
  33rd full/diff survey (survey counts every
  method RQ-vs-M regardless of degree).
  M-tails 16/16 ALL NEW vs P373T RM col-led
  tails (overlap 0) and vs P373T RQ row-led
  tails (overlap 0); RM-tails 16/16 ALL NEW vs
  P373T RM+RQ (overlap 0 both); AM/CM/M/QR/RM/
  RQ 0-overlap vs P373 all six (widths P374 vs
  P373: AM 7B vs 8B, CM 3B vs 4B, M 7B vs 7B,
  QR 2B vs 2B, RM 9B vs 7B, RQ 7B vs 6B).
  AC 79, CC 83, QC 77, RC 70; C _N decls
  79/83/77/70 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M-tab computed; A b0 const 5e in
  AC (b1 const 02, b2-3 const 00; b5 const 7b
  deducted, in AC-missing; b84-87 consts
  11,a8,c5,5c A-lane); C b0 const 20 in CC
  (b1-3 const 00/00/00 first-hand; b5 const 7b
  deducted, in CC-missing; b52 const 0xD2 entry
  variant, in CC; CC has no b84,85,86 (all in
  CM lane); C b87 const b8); Q b0 const 5e in
  QC (b1 const 02, b2-3 const 00; b5 STEPS
  7b->7c varies, in QC-missing; b80-85 absent
  QM7/R2 lanes, b86 const b2 + b87 const b8 in
  QC); R b0 const ef in RC (b1 const 25
  256/256 oracle, in RC table, code-indexed
  first-hand).
  PBA88-PLAIN-M7b30 sig 5e020000 x16 (b0 const
  5e via AC b0; b5 const 7b deducted NOT in AC;
  AM 16/16 distinct NO pair; M7 b30,39,47,80-83
  positions STAGED P373A per code comment)
  + PBA sig 5e NEW vs P373 62 (novelty = new sig
  62->5e + AM 0-overlap; M7 widths P373 8B vs
  P374 7B differ).
  C10-1SIG-88-TAIL-M3 sig 20000000 x10
  DIFFERS-from-PB1-sig (full sig b0-3 in CC =
  20000000; CM 10/10 diverge 6ch b84-86; M3
  FIRST this tier (3B lane); b5 const 7b
  deducted NOT in CC).
  QUAD88-1SIG-QM7/R2-B5EDGE 1-sig 5e020000
  SAME-sig-as-PBA (b0 const 5e in QC; b5 STEPS
  7b->7c edge off26->27 in code; m-tab b52,53,
  54,80-83 (M 16/16 7ch NO frags, m = off&15
  first-hand; QM7 positions FIRST this lane per
  code comment; per-row 16 distinct NO frags)
  + r2 b84,85 R2 4/4 UNPAIRED BY-ROW (q =
  off>>4 first-hand); tails = R2 rows + b2b8
  consts; QM7-shared-x3 48/48).
  Ring T88-STANDARD-TM9/TR7 sig ef250000 x256
  (b0 const ef 256/256 oracle, in RC table;
  b1 const 25 256/256 oracle, in RC table;
  code-TM9 b6,7,8,9,10,80-83 by COL RM 16/16
  9ch (positions staged P373R) + code-TR7
  b52,53,54,76-79 by ROW RQ 16/16 UNPAIRED
  (SPLIT tails b80-83 col / b76-79 row;
  positions FIRST this lane per code); b84-87
  const 6c38b2b8 ring-wide NEW; b4=(0x4b+2off)
  &FF + b5=0x7c+(off>=91)+(off>=219) (C
  literals 75/124/91/219 verified == 0x4b/0x7c/
  91/219; py hex 0x4b/0x7c)).
  VPOS partitions re-derived from code: PBA 8
  (missing 9 - 1; b4+M7 b30,39,47,80-83, b5
  const deducted) / C10 4 (missing 5 - 1;
  b4+M3 b84-86, b5 const deducted) / quad 11
  (missing 11 - 0; b4,b5 vary+QM7 7+R2 2, NO
  deduct) / T 18 (missing 18 - 0; b4,b5 vary+
  TM9 9+TR7 7, NO deduct) -- all match Q-1122
  census (VPOS 8/4/11/18 + PBA/C10 -1 each for
  b5-const per Q-1122 Q3; census consts 79/83/
  77/70 EXACT).
  Code-consts vs census-script excl (PBA 79 /
  C10 83 / quad 77 / T88 70): impl 79/83/77/
  70 = census-script EXACT -- no lag on even
  band (memo A-957 PRESENT-CONFIRM this tier;
  Q-1122 is the acting sheet). S-F lag stays 44.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 146889 / S1 146890 / A 146891-906 /
  C 146907-916 / Q 146917-980 / R 146981-147236):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode 7b NO edge/NO step; Q b5
  STEPS emerges from raw lencode 7b->7c edge
  off26->27; R explicit counter (b4=(0x4b+2off)
  &FF b5=0x7c+(off>=91)+(off>=219); py hex
  0x4b/0x7c; C staged decimal literals 75/124/
  91/219 re-derived: 75==0x4b, 124==0x7c)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 7ch M7 b30,39,47,80-83; C 6ch M3 b84-86;
  Q 7ch/4ch QM7 b52,53,54,80-83/R2 b84,85; R
  9ch/7ch TM9 b6-10,80-83 by COL / TR7
  b52,53,54,76-79 by ROW).
  C blocks carry T98603/T98608/T98613/T98628/
  T98643/T98663 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 98603 verified
  in py; bounds + byte positions exact: A 7-lane,
  C 3-lane, Q 7ch+2B + r2, R 9-lane/7-lane),
  A b5 const deducted NOT in AC + C b5 const
  deducted NOT in CC + Q b5 varies (B5EDGE, in
  QC-missing via vary) + R b0 const ef in RC
  (in table) + R counter b4=(75+2off)&FF +
  (124)+(off>=91)+(off>=219) (C literals
  75/124/91/219 verified), temps _t7437-7452
  (base max _t7436, no reuse) +
  _i4517/4519/4522/4525 (base max _i4515, no
  reuse) + _b4516/4518/4520/4521/4523/4524
  (base max _b4514, no reuse), union 4516-4525
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P373R close (C "T10P3740 singleton" after
  "CLOSED T10P373R"; py return 0 + S0 guard
  98603 after "CLOSED T10P373R" print), at
  dispatch tail (P374R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches census geometry (PB0 NEW-sig 33/84;
  PB1 sig-REPEAT 48/88 DIFFERS-own-C10 45/88;
  PBA88-PLAIN-M7b30 VPOS 8 sig-5e b5 const M7
  16/16 distinct; C10-1SIG-88-TAIL-M3 VPOS 4
  DIFFERS-from-PB1-sig b5 const M3 10/10 +
  b87 const b8; QUAD88-1SIG-QM7/R2-B5EDGE VPOS
  11 SAME-as-PBA-sig b5-STEPS + R2 4/4 UNPAIRED
  ec37/0c38/2c38/4c38 + full-tail 2/2/2/3/3/3
  + R2-distinct + NO frags + M-tails NEW;
  T88-STANDARD-TM9/TR7 VPOS 18 + TM9-by-COL/
  TR7-by-ROW + SPLIT-tails + b84-87 6c38b2b8 +
  1-sig-const-b0 + counter 4b/7c/91/219;
  lencode 348/348 whole-tier, NO D dips) incl
  exact values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + LCS + B5EDGE frame + consts stand;
  const-count note is impl==census-script this
  tier per census, geometry exact, PORT verdict
  stands; M==RQ identical same-order first-hand
  this tier, tier stands).
- Edges via counter formula first-hand: A head
  97/7b tail b5/7b b5set {7b} NO step, 0 ff
  (b4 base 0x97 step2 16/16, b0 const 5e 16/16);
  C head b7/7b tail c9/7b b5set {7b} NO step,
  0 ff (b0 const 20 10/10); Q head cb/7b tail
  49/7c b5set {7b,7c} B5EDGE off26->27, 1 ff
  (b4 base 0xcb step2 64/64 exact-set wraps
  once, ff@off26; b0 const 5e 64/64); ring
  pre-edge off90 (ff/7c), edge off91 (01/7d);
  pre-edge off218 (ff/7d) -> edge off219 (01/7e);
  exactly 2 ff in 256 (R b4 exact-set 4b-step2
  256 vals / 128 uniq); R head 4b/7c tail 49/7e;
  b1 const 25 256/256; formulas re-derived from
  T10P374R code text (4b/7c/91/219 hex==dec) +
  T10P374A/C/Q text (raw lencode + b5 step/const
  comments); all edge pins + head/tail pins +
  for-list R mid (147136 off155) + edge triple
  (147199/147200/147201) + 2 PASS lines each
  py+C. S0/S1 embedded b4/b5 match raw lencode
  (93/7b + 95/7b). Ring counter==raw-lencode
  256/256 + Q 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No
  DISSENT on cut bytes (edges482.py EDGES-GREEN,
  A/C NO-ff + Q single-ff B5EDGE + ring 2-ff,
  all edge asserts verified first-hand, never
  assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 232/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 232 content / 0 del (content-line
  variance 232 recorded: b478/b479/b480/b481/
  b482 232-class); for-line replaced by superset
  (base for-N subset of band, removed 0); fine-
  norm equivalent (for482base.nums subset
  for482.nums, removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-indented 770->
  772 (+2: 146889/146890) / ranges py-indented
  926->930 (+4; C singletons 775->777 +2 / C
  all-range-guards 948->952 +4, same 6 P374
  blocks both sides; no elif/else-if added either
  side: py file-wide elif 50 both, C else-if 0
  both; deltas agree every side), CLOSED T10P
  prints 2132->2138 +6 both sides, seal 2226->
  2232 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
  GATE-648dd0de reconcile (viewer-vs-sweep
  first-hand): GATE values agree on PYID/RGRAM/
  smoke/units/for-added-29 (identical 29-set
  both sides)/PINS+58/temps/seal/CLOSED/
  embeds/counters/consts/R2 rows/tails/M==RQ
  identical/VPOS 8/4/11/18/extra-table/QM7-shared/
  S1-vs-P373-sig-repeat/S1-vs-own-C10 45/88.
  Diffs: (a) RQ==M ledgers: viewer evens 55->56
  (identical degree; b473 precedent counts every
  degree) / survey 32->33 (every-method count);
  GATE 37th even band + FULL-identity degree
  unchanged (b477 12th stands; this tier full-
  identity) -- facts identical (lists/sets
  equal, overlap 16, positional 16/16,
  tail-identity ordered+seteq 16/16). (b) edge-
  triple naming: GATE "pre-edge+edge+post-edge"
  147199/147200/147201 off218/219/220; viewer
  for-added R8 same triple (mate 147201 off220)
  + edges assert pre+edge pins -- facts
  identical. (c) uniform ledger: GATE box-score
  notes b477/b479 TRUE-uniform do not carry to
  this PLAIN tier; viewer chain stays 39
  (uniform-cells required; C10 10/10 DIVERGE +
  SIG-DIFFERS PB1) -- P338 OPEN, deferred to
  sweep accounting, never re-litigated; facts
  identical. No code dispute; PORT stands both
  sides.
- CONFIRM evidence (CONVERT-01 rule b):
  memo A-sheet PRESENT for P374 (A-957-q1122
  CONFIRM 50/50 CLEAN: Q1 1x(100,84)+347x
  (104,88) EXACT + PB1 sig-repeat + PBA 5e/M7/
  b5-7b + C10 20/M84-86/b5-7b + QUAD 1-sig-5e
  SAME-PBA + T 1-sig-ef250000 STANDARD; Q2
  QM/R2 tails + suffix-lcs 2/2/2/3/3/3 +
  M-tails NEW + TM-by-COL/TR-by-ROW + 6c38b2b8;
  Q3 lencode 348/348 + consts 79/83/77/70 +
  0 stragglers NO D dips -- memo present both
  tiers this round) + writer census Q-1122
  (consts PBA 79 / C10 83 / quad 77 / T88 70;
  committed tables match excl exactly --
  no writer lag this tier, geometry exact, PORT
  verdict stands) + cport commit msgs (PYID
  11119, RGRAM 22238 both legs per msg; py-merge
  RGRAM 22238) + own full battery above.
  Novelty gated: b52-const-entry variant 0xD2
  in CC (P373 0x56, P372 0x94, P371/P370 0x4a,
  P369 0xd2, P368/P367 0x84, P366 0x72, P365
  0xc5, P364 0xb9, P363 0xb8); M-tails 16/16
  ALL NEW vs P373T tails; no _T10P374C either
  side.
- FWD-check: banked Next-P375 (Q-1122 forward
  note, read first-hand): PB0 @147237 sig
  6e586911 pay84 NEW-sig + PB1 @147238 sig
  22000000 pay88 + PBA multi-region
  08020000+10020000+24020000 + C10-region
  45000000 x10 -- b483 C port 246d3408
  (T10P375 pins 147237..147584, 2238 sealed)
  ALREADY LANDED (this round's turf, b483+;
  battery next in round); CONSUME-FIRST per
  bank-miss lesson.
- Quiz: no conflicting CLAIM/GATE/FLAG on b482
  (adjacent odd b481 = 940d5f26 C port live
  used as diff-base only, no verdict beyond;
  adjacent b483 = 246d3408 C port live, NEXT
  battery this round, no verdict yet; FLAG
  files name no b482 band; DISSENTs q846/847/
  849 unrelated tiers; no conflicting
  CLAIM/GATE/FLAG at filing -- GATE-648dd0de
  reconciled pre-battery + mid-battery values
  agree).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r78/
  (build482/, pyid482.log, rgram482py/c.log,
  cmp482.py, seteq482.py, ownloop482.py (+
  w482loop.log), secf482a/b/c.py, edges482.py
  (+.log), tabaudit482.py (+.log), smoke482.log,
  units482.log, band482.diff/addedlines/.addedc,
  for482.nums/added/for482base.nums).

Verdict: PASS. No RED. 348-pin contiguous range
146889..147236 sealed. Round 3/4 = cap 3/4.
