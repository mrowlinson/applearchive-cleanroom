# VERIFY-0c29b70b b476 T10P368 pins 144801..145148 (348 pins) PASS

Seat viewer-r77, first-hand, tree @0c29b70b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r77.
Base 6a9df578 (b475 tip, 2190 tiers sealed; this
seat's VERIFY-6a9df578 PASS-filed r76,
base-use only, respected). Band = b5f97d8f (py
merge w2b@0e637fcb partial, +6 tiers, +58 pins;
commit msg verified via git log) + 0c29b70b (C
port; parent == b5f97d8f verified via git
rev-list --parents). Chain 6a9df578 -> b5f97d8f
-> 0c29b70b, every sha via git log at takeover,
NO gap-jump. GATE-0c29b70b PASS-functional filed
mid-battery by sweep2-r82 -- reconciled first-hand
below (values agree; one counting-convention diff
noted, code facts identical). NO other GATE/FLAG
on b476 at file time.

Banked Next-P368 shape (A-954 + Q-1079 forward
notes + w2b-r33 qTBD-p368 census, all read
first-hand) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 2f9a600e @144801
(S0 head; sig-REPEAT 30/84 vs P367PB0 @
n144453, sig b0-3 NOT in diff, positions
[4,5,6,7,9-11,13,15-18,44-47,50,51,56-59,76-83]
first-hand, NOT byte-equal) + PB1 1c000000
@144802 (S1 head; sig-REPEAT 80/88 vs
P367PB1 @ n144454, sig b0-3 NOT in diff,
positions [4-55,60-87] first-hand, NOT byte-equal;
79... no: 80/88 vs own C10[0] n144819 all-10
identical-30-diff positions recorded per-cell
diff=30 x10 uniform-diff, sig b0-3 same-sig
NOT in diff; S1 SIG-DIFFERS own C10
(1c-vs-1f000000); 39 stays (even band):
NOT TRUE-UNIFORM (C10 10/10 DIVERGE +
SIG-DIFFERS); P338 uniform-rule dispute stays
DEFERRED to sweep accounting, never re-litigated)
+ PBA88-PLAIN-M9b29 sig 88010000 x16 @144803-818
(b0 const 0x88 first-hand) + C10-region
1f000000 pay88 x10 @144819-828 (b0 const 0x1f
first-hand, SAME b0-1-2-3 shape DIFFERS-from-PB1-sig
1f-vs-1c) -- all corroborated against lane code
both sides before any battery step (py==C S0/S1
staged strings; staged-vs-oracle secf476a/b/c
GREEN first-run; no bank-miss).

- Build: seat-private build476/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned-stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 fcc71851...
  (no GATE absolutes cited -- recorded first-hand
  here, never hand-transcribed).
- RGRAMC-PYID 10945/10945 covered=10945/10945
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  default CT cache; +29 vs b475 10916).
- RGRAM py 21890/21890 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21890/21890 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21890/21890, sorted +
  raw identical; cmp476.py GREEN).
- PINS-RGRAM cells set-eq 21890/21890 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq476.py GREEN first-run). PINS 21892 lines
  first-hand (2 hdr + 21890 rows; base 21834
  lines / 21832 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 10916->10945 +29/-0 (python
  sets, trailing-';' strip, never comm): 144801
  144802 144803 144804 144810 144811 144817
  144818 144819 144820 144823 144824 144827
  144828 144829 144844 144845 144860 144861
  144877 144892 144893 144895 144896 144897
  145023 145024 145025 145148 (no GATE list at
  file time -- shapes verified vs code blocks:
  see below; range 144801..145148 exact).
  29 = 2 sing (144801 144802 offs 0/1) + A 6
  (head pair 144803/144804 off0/1 + mid pair
  144810/144811 off7/8 + tail pair 144817/
  144818 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 6b NO
  edge) + C 6 (head pair 144819/144820 off0/1
  + mid pair 144823/144824 off4/5 + tail pair
  144827/144828 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 6b NO edge) + Q 7 (head
  144829 off0 + 144844 off15 + 144845 off16 +
  144860 off31 + 144861 off32 + 144877 off48 +
  tail 144892 off63; NOEDGE b5 const 6b; NO
  edge pair) + R 8 (head 144893 off0 + pre-edge/
  edge 144895/144896 off2/3 + mid pin 144897
  off4 + pre-edge/edge 145023/145024 off130/131
  + mid 145025 off132 + tail 145148 off255;
  both counter edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21890-21832.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit476.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 181 PASS 0 FAIL second-run (1 own-assert
  case-fix + 1 rerun: py-R-counter hex-case
  0xFB->0xfb in assert text only -- code values
  untouched, reran GREEN; no dead code).
  Inventory exactly the 12 tables both sides
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no M42/X42/
  H42/L42, no QB/PT/FM, no RT/TT (SPLIT tails,
  not ROWTAIL), no QT (R1 carries b84 in-row +
  b85/b86/b87 consts); no _T10P368C numeric-head
  probe -- precedent since band29, only band29-
  range cover it).
  S0 168ch sig 2f9a600e sig-REPEAT (30/84 payload
  diff vs P367S0, positions
  [4,5,6,7,9,10,11,13,15,16,17,18,44,45,46,47,
  50,51,56,57,58,59,76,77,78,79,80,81,82,83]
  first-hand, sig b0-3 NOT in diff, NOT
  byte-equal) / S1 176ch sig 1c000000
  sig-REPEAT (80/88 payload diff vs P367S1,
  positions [4-55,60-87] first-hand, sig
  b0-3 NOT in diff, NOT byte-equal; vs own C10
  cells 10/10 DIVERGE staged+oracle: all-10
  diff=30 uniform-diff, sig b0-3 same-sig NOT
  in diff; NOT byte-equal; S1 SIG-DIFFERS own
  C10 (1c-vs-1f); 39 stays (even band)), staged
  as full-payload singletons; S0/S1 embedded b4/b5
  43/6b + 45/6b match raw lencode.
  AM 16/16 18ch distinct, CM 10/10 8ch diverge
  (b84,85,86,87 M4 lane, all 10 distinct), M 16/16
  16ch distinct, QR 4/4 2ch R1 rows 93/b3/d3/f3
  exact (tails = R1 + 57/97/b2 quad-wide exact;
  full-tail suffix = subseq = TSHARE =
  3/3/3/3/3/3 (all-3 agree first-hand; full
  tuples pairwise unequal, 4 distinct)), RM 16/16
  16ch distinct, RQ 16/16 16ch distinct, no QT +
  no RT + no F (no frags).
  M==RQ 16/16 string-identical SAME-ORDER (M list
  == RQ list, 16ch; QM8 b40,41,42,43,80-83 by COL
  m=off&15 vs RQ8 b40,41,42,43,80-83 by ROW
  r=off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated) -- 55th even-band
  RQ==M instance (evens 54->55); 27th full/diff
  survey (survey counts every method RQ-vs-M
  regardless of degree; 4th identical case:
  b472, b474, b475, b476).
  M-tails 16/16 ALL NEW vs P367T col-led tails
  (overlap 0; P367T RM 16x8B frame first-hand
  from code, tails last-4B); RQ-tails 16/16 ALL
  NEW vs P367T TR8 (overlap 0) + 16/16 ALL NEW
  vs P367T RM (overlap 0); RM-tails 16/16 ALL
  NEW vs P367T RM (overlap 0) + 16/16 ALL NEW
  vs P367T TR8 (overlap 0); AM/CM/M/QR/RM/RQ
  0-overlap vs P367 all six (widths P368 vs
  P367: AM 9B vs 6B, CM 4B vs 3B, M 8B vs 7B, QR
  1B vs 1B, RM 8B vs 8B, RQ 8B vs 7B).
  AC 77, CC 82, QC 77, RC 70; C _N decls
  77/82/77/70 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 const 88 in
  AC (b1 const 01, b2-3 const 00; b5 const 6b
  deducted, in AC-missing; b84-87 consts
  0a,73,4f,f6 A-lane); C b0 const 1f in CC
  (b1-3 const 00; b5 const 6b deducted, in
  CC-missing; b52 const 0x84 const-entry, in CC;
  CC has no b84,85,86,87 (all in CM lane); CC
  has no b87 const-entry this tier (M4 lane));
  C b84,85,86,87 absent (M4/TAIL lane);
  Q b0 const e5 1-sig DIFFERS-from-PBA in QC
  first-hand (b1 const 01, b2-3 const 00; b5
  const 6b deducted NOT in QC (in QC-missing),
  NO step; b84 absent R1-lane, b85 const 57 /
  b86 const 97 / b87 const b2); R b0 const e5
  + b1 const 1e in RC table, code-indexed
  first-hand).
  PBA88-PLAIN-M9b29 sig 88010000 x16 (b0 const
  88 via AC b0; b5 const 6b deducted NOT in AC;
  AM 16/16 distinct NO pair; M9
  b29,30,31,34,35,80-83 positions FIRST this
  lane per code comment) + PBA sig 88 NEW vs
  P367 b6 (novelty = new sig b6->88 + AM
  0-overlap; M9 FIRST this lane: A-mtab widths
  P364 7B / P365 8B / P366 7B / P367 6B all
  narrower).
  C10-1SIG-88-TAIL-M4 sig 1f000000 x10
  DIFFERS-from-PB1-sig (full sig b0-3 in CC =
  1f000000; CM 10/10 diverge 8ch b84,85,86,87;
  CC has no b84-87 (all in CM lane); b5 const
  6b deducted NOT in CC).
  QUAD88-1SIG-QM8/R1-NOEDGE 1-sig e5010000
  DIFFERS-from-PBA-sig (b0 const e5 in QC; b5
  const 6b deducted, NO step; m-tab b40,41,42,
  43,80-83 (M 16/16 16ch NO frags, m = off&15
  first-hand; QM8 positions staged P336Q per
  census) + r1 b84 R1 4/4 UNPAIRED BY-ROW
  (q = off>>4 first-hand); tails = R1+57/97/b2
  quad-wide, full-tail pairs all lcs 3 per guard
  + R1 all-distinct + QM8-shared-x3 48/48).
  Ring T88-SWAPPED-RM8/RQ8 1-sig e51e0000 x256
  (b0 const e5 256/256 oracle, in RC table; b1
  const 1e 256/256 oracle, in RC table; code-RM8
  b30,39,46,47,76-79 by COL RM 16/16 (positions
  FIRST this lane per census) + code-RQ8
  b40,41,42,43,80-83 by ROW RQ 16/16 UNPAIRED
  (SPLIT tails b80-83 row / b76-79 col;
  positions FIRST this lane); b84-87 const
  c9878ab4 ring-wide NEW; b4=(0xfb+2off)&FF +
  b5 = 0x6b+(off>=3)+(off>=131) (C literals
  251/107/3/131 verified == 0xfb/0x6b/3/131;
  py hex 0xfb/0x6b)).
  VPOS partitions re-derived from code: PBA 10
  (missing 11 - 1; b4+M9
  b29,30,31,34,35,80-83, b5 const deducted) /
  C10 5 (missing 6 - 1; b4+M4 b84,85,86,87,
  b5 const deducted) / quad 10 (missing 11 - 1;
  b4,b5+QM7... QM8 8+R1 1, b5 const deducted,
  NO step) / T 18 (missing 18 - 0;
  b4,b5+RM8 8+RQ8 8, counter varies, NO deduct)
  -- all match qTBD-p368 census (10/5/10/18);
  GATE-0c29b70b reports C10 6 (counts b5; code
  missing-set [4,5,84,85,86,87] identical both
  sides -- convention diff only, reconciled).
  Code-consts vs census-script excl (PBA 77 /
  C10 82 / quad 77 / T88 70): impl 77/82/77/
  70 = census-script EXACT -- no lag on even
  band (deduct-const-b5 holds; no memo A-sheet
  for P368 at file time; qTBD-p368 census-script
  is the acting sheet). VPOS 10/5/10/18 =
  census EXACT. S-F lag stays 44.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 144801 / S1 144802 / A 144803-818 /
  C 144819-828 / Q 144829-892 / R 144893-148):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode; Q b5 const emerges from raw
  lencode; R explicit counter (b4=(0xfb+2off)&FF
  b5=0x6b+(off>=3)+(off>=131); py hex 0xfb/
  0x6b; C staged decimal literals 251/107/3/131
  re-derived: 251==0xfb, 107==0x6b) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 18ch/8ch... A 9-lane M9 b29,30,31,34,35,
  80-83; C 4-lane M4 b84-87; Q 16ch/2ch QM8
  b40,41,42,43,80-83/R1 b84; R 16ch/16ch RM8
  b30,39,46,47,76-79 by COL / RQ8
  b40,41,42,43,80-83 by ROW).
  C blocks carry T97213/T97218/T97223/T97238/
  T97253/T97272 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 97213 verified
  in py; bounds + byte positions exact: A 9-lane,
  C 4-lane, Q 8ch/1ch + r1, R 8-lane/8-lane),
  A/C raw lencode (no counter literals; A/C b5
  const deducted NOT in AC/CC) + Q b5 const
  6b NO step (deducted NOT in QC) + R counter
  b4=(251+2off)&FF + (107)+(off>=3)+(off>=131)
  (C literals 251/107/3/131 verified), temps
  _t7341-7356 (base max _t7340, no reuse) +
  _i4457/4459/4462/4465 (base max _i4455, no
  reuse) + _b4456/4458/4460/4461/4463/4464
  (base max _b4454, no reuse), union 4456-4465
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P367R close (C "T10P3680 singleton" after
  "CLOSED T10P367R"; py return 0 + S0 guard
  97213 after "CLOSED T10P367R" print), at
  dispatch tail (P368R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches census geometry (PB0 sig-REPEAT 30/84;
  PB1 sig-REPEAT 80/88 DIFFERS-own-C10 30/88;
  PBA88-PLAIN-M9b29 VPOS 10 sig-88 b5 const M9
  16/16 distinct; C10-1SIG-88-TAIL-M4 VPOS 5
  DIFFERS-from-PB1-sig b5 const M4 10/10 diverge;
  QUAD88-1SIG-QM8/R1-NOEDGE VPOS 10 + R1 4/4
  UNPAIRED 93/b3/d3/f3 + suffix-lcs-3/3/3/3/3/3
  + R1-distinct + QM8-shared-x3 + NO frags +
  M-tails NEW; T88-SWAPPED-RM8/RQ8 VPOS 18 +
  RM8-by-COL/RQ8-by-ROW + SPLIT-tails + b84-87
  c9878ab4 + counter fb/6b/3/131; lencode 348/348
  whole-tier, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R1 rows + tails + LCS
  + frame + consts stand; const-count note is
  impl==census-script this tier per census, geometry
  exact, PORT verdict stands; M==RQ identical
  first-hand this tier, tier stands).
- Edges via counter formula first-hand: A head
  47/6b tail 65/6b b5set {6b} NO step, 0 ff
  (b4 base 0x47 step2 16/16, b0 const 88 16/16);
  C head 67/6b tail 79/6b b5set {6b} NO step,
  0 ff (b0 const 1f 10/10); Q head 7b/6b
  tail f9/6b b5set {6b} NO step, 0 ff (b4 base
  0x7b step2 64/64 exact-set range 7b..f9 NO
  wrap, min 0x7b max 0xf9); ring pre-edge off2
  (ff/6b), edge off3 (01/6c); pre-edge off130
  (ff/6c) -> edge off131 (01/6d); exactly 2 ff
  in 256 (R b4 exact-set fb-step2 256 vals / 128
  uniq); R head fb/6b tail f9/6d; formulas
  re-derived from T10P368R code text (fb/6b/3/131
  hex==dec) + T10P368A/C/Q text (raw lencode +
  b5 const comment); all edge pins + head/tail
  pins + for-list R mid pins + 2 PASS lines each
  py+C. S0/S1 embedded b4/b5 match raw lencode
  (43/6b + 45/6b). Ring counter==raw-lencode
  256/256 + Q 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges476.py EDGES-GREEN, A/C NO-ff
  + Q NO-ff + ring 2-ff range-no-wrap + Q-range
  exact + R counter asserts verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 230/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 230 content / 0 del (content-line
  variant 230 recorded: new class this tier;
  prior b468/b469/b474/b475 231, b470/b471/b472/
  b473 232); for-line replaced by superset (base
  for-N subset of band, removed 0); fine-norm
  equivalent (for476base.nums subset for476.nums,
  removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-indented 758->760
  (+2: 144801/144802) / ranges py-indented 902->
  906 (+4; C singletons 763->765 +2 / C
  all-range-guards 924->928 +4, same 6 P368 blocks
  both sides; no elif/else-if added either side:
  py file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2096->2102 +6 both sides, seal 2190->2196 +6
  (commit msgs; offset +94 vs CLOSED-T10P stable):
  all agree, no slip (absolute seal inherits lane
  tally; delta verified).
  GATE-0c29b70b reconcile (viewer-vs-sweep
  first-hand): GATE values agree on PYID/RGRAM/
  smoke/units/for-added-29/PINS+58/temps/seal/
  CLOSED/embeds/counters/consts/M==RQ/tails.
  Diffs: (a) VPOS-C10 6-vs-5: code missing-set
  [4,5,84,85,86,87] identical; GATE counts b5,
  viewer+qTBD-census deduct b5-const (viewer
  convention since r76, census VPOS 5). (b) py
  file-wide elif: 50 both (no elif added), C
  else-if 0 both (GATE prose "elif 0 both"
  reads as added-count; absolute is 50). No
  code dispute; PORT stands both sides.
- CONFIRM evidence (CONVERT-01 rule b):
  NO memo A-sheet for P368 at file time
  (A-955-q1080 + Q-1080-w2b ABSENT, verified
  first-hand via ls; cport-r66 claim concurs;
  A-hits for P368 are incidental mentions only).
  Substitute first-hand: writer census
  NOTE-w2b-r33-qTBD-p368 (consts PBA 77 / C10
  82 / quad 77 / T88 70; committed tables match
  excl exactly -- no writer lag this tier,
  geometry exact, PORT verdict stands) +
  cport commit msgs (PYID 10945, RGRAM 21890
  both legs per msg; py-merge RGRAM 21890) +
  own full battery above. Novelty gated:
  b52-const-entry variant 0x84 in CC (P367 0x84
  same value this tier, carry; P366 0x72, P365
  0xc5, P364 0xb8, P363 0xb9); M-tails 16/16
  ALL NEW vs P367T col-led tails.
- FWD-check: banked Next-P369 (qTBD-p368 forward
  note + GATE-0c29b70b FWD-check, both read
  first-hand): PB0 @145149 sig ef928b0e pay84
  NEW-sig (33/84 diff vs P368PB0, NOT byte-equal)
  + PB1 1e000000 pay88 @145150 NEW-sig vs P368
  heads (56/88 diff vs P368PB1, NOT byte-equal)
  + PBA sig e5010000 x16 @145151-166 + C10-region
  1e000000 pay88 x10 @145167-176
  SAME-as-PB1-sig -- bank e5a89b49 rev-parse
  verified on lanes/encode-writer2b per GATE;
  no lane code landed at file time; pre-
  corroboration DEFERRED; CONSUME-FIRST with
  re-corroboration at b477 battery per bank-miss
  lesson.
- Quiz: no conflicting CLAIM/GATE/FLAG on b476
  (adjacent evens b475 = 6a9df578 C port live
  used as diff-base only, no verdict beyond;
  adjacent odds b477 = e9c52e90 C port live,
  next battery, no verdict beyond; FLAG files
  name no b476 band; DISSENTs are q846/847/849
  unrelated tiers).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r77/
  (build476/, pyid476.log, rgram476py/c.log,
  cmp476.py, seteq476.py, ownloop476.py,
  secf476a/b/c.py, edges476.py (+.log),
  tabaudit476.py (+.log), w476loop.log,
  smoke476.log, units476.log, band476.diff/
  addedlines/.addedc, for476.nums/added/
  for476base.nums).

Verdict: PASS. No RED. 348-pin contiguous range
144801..145148 sealed. Round 1/4.
