# VERIFY-6a9df578 b475 T10P367 pins 144453..144800 (348 pins) PASS

Seat viewer-r76, first-hand, tree @6a9df578,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r76.
Base 69e06615 (b474 tip, 2184 tiers sealed; this
seat's VERIFY-69e06615 PASS-filed same round,
base-use only, respected). Band = df52359f (py
merge w2b@1cb13bd6 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 6a9df578 (C
port; parent == df52359f verified via git
rev-list --parents). Chain df52359f parent ==
69e06615 verified, NO gap-jump (every sha via
git log at takeover). NO GATE filed for b475 at
battery time -- asserts derived from A-954 +
Q-1079 + lane code first-hand (noted wherever a
GATE value would otherwise be cited).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__; PYTHONDONTWRITEBYTECODE=1).

Banked Next-P367 shape (A-953 + Q-1078 forward
notes, both read first-hand) CONSUMED FIRST and
VERIFIED first-hand EXACT: PB0 2f9a600e @144453
(S0 head; NEW-sig 33/84 diff vs P366PB0 @
n144105, sig b2-3 IN diff with b0-1 same,
positions
[2,3,4,5,22,23,30,31,33-43,48,49,52-55,68-75]
first-hand, NOT byte-equal) + PB1 1c000000
@144454 (S1 head; sig-REPEAT 65/88 diff vs
P366PB1 @ n144106, sig b0-3 NOT in diff,
positions
[4-15,19-59,76-87] first-hand, NOT byte-equal;
79/88 vs own C10[0] n144471 (all-10 identical
79-diff positions
[4,6-55,60-87], sig b0-3 same-sig NOT in diff;
TRUE UNIFORM [10x79] 39th TRUE-uniform case
(odd): uniform + SIG-EQ + differs-PB0; P338
uniform-rule dispute stays DEFERRED to sweep
accounting, never re-litigated) + PBA88-PLAIN-
M6b10 b6010000 x16 @144455-470 + C10-region
1c000000 pay88 x10 @144471-480 (SAME-as-PB1-sig)
-- all corroborated against lane code both sides
before any battery step (py==C S0/S1 staged
strings; no bank-miss).

- Build: seat-private build475/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 681dbf6e...
  (no GATE filed -- recorded first-hand here,
  never hand-transcribed).
- RGRAMC-PYID 10916/10916 covered=10916/10916
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21832/21832 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21832/21832 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21832/21832, sorted +
  raw identical; cmp475.py GREEN).
- PINS-RGRAM cells set-eq 21832/21832 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq475.py GREEN first-run). PINS 21834 lines
  first-hand (2 hdr + 21832 rows; base 21776
  lines / 21774 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10887->10916 +29/-0 (python
  sets, trailing-';' strip, never comm): 144453
  144454 144455 144456 144462 144463 144469
  144470 144471 144472 144475 144476 144479
  144480 144481 144496 144497 144511 144512
  144528 144544 144545 144639 144640 144704
  144767 144768 144769 144800 (no GATE list at
  file time -- shapes verified vs code blocks:
  see below; range 144453..144800 exact).
  29 = 2 sing (144453 144454 offs 0/1) + A 6
  (head pair 144455/144456 off0/1 + mid pair
  144462/144463 off7/8 + tail pair 144469/
  144470 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 68 NO
  edge) + C 6 (head pair 144471/144472 off0/1
  + mid pair 144475/144476 off4/5 + tail pair
  144479/144480 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 68 NO edge) + Q 7 (head
  144481 off0 + 144496 off15 + 144497 off16 +
  B5EDGE pair 144511/144512 off30/31 (ff->01 +
  b5 STEP 68->69) + 144528 off47 + tail 144544
  off63; off31 mate pair-covered) + R 8 (head
  144545 off0 + pre-edge/edge 144639/144640
  off94/95 + mid pin 144704 off159 + pre-edge/
  edge 144767/144768 off222/223 + 144769 off224
  + tail 144800 off255; both counter edges
  pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21832-21774.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit475.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 190 PASS 0 FAIL second-run (3 stale-
  assert fixes + rerun: 2 C-index cites from a
  dropped [:] slice + 1 genuinely absent comment
  text -- all fixed, reran GREEN; no GATE at file
  time -- VPOS/cites compared vs A-954+Q-1079
  only; QC b1-3 is 01/00/00 first-hand both sides
  -- slip class clear 8 bands running).
  Inventory exactly the 12 tables both sides
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no M42/X42/
  H42/L42, no QB/PT/FM, no RT/TT (ring, not
  ROWTAIL), no QT (R1 carries b84 in-row +
  b85/b86/b87 consts); no _T10P367C numeric-head
  probe -- precedent since band29, only band29-
  range cover it).
  S0 168ch sig 2f9a600e NEW-sig (33/84 payload
  diff vs P366S0, positions
  [2,3,4,5,22,23,30,31,33-43,48,49,52-55,68-75]
  first-hand, sig b2-3 IN diff with b0-1 same,
  NOT byte-equal) / S1 176ch sig 1c000000
  sig-REPEAT (65/88 payload diff vs P366S1,
  positions [4-15,19-59,76-87] first-hand, sig
  b0-3 NOT in diff, NOT byte-equal; vs own C10
  cells TRUE UNIFORM [10x79] staged+oracle:
  all-10 identical 79-diff positions
  [4,6-55,60-87], sig b0-3 same-sig NOT in diff;
  NOT byte-equal; S1 SIG-EQ own C10; S1
  SIG-DIFFERS own PB0 (1c-vs-2f9a600e); 39th
  TRUE-uniform case (odd)), staged as
  full-payload singletons; S0/S1 embedded b4/b5
  8b/68 + 8d/68 match raw lencode.
  AM 16/16 12ch distinct, CM 10/10 6ch diverge
  (b84,85,86 M3 lane, all 10 distinct), M 16/16
  14ch distinct, QR 4/4 2ch R1 rows 59/79/99/b9
  exact (tails = R1 + 9b/ed/86 quad-wide exact;
  full-tail suffix = subseq = TSHARE =
  3/3/3/3/3/3 (all-3 agree first-hand; full
  tuples pairwise unequal, 4 distinct)), RM 16/16
  16ch distinct, RQ 16/16 14ch distinct, no QT +
  no RT + no F (no frags).
  M==RQ 16/16 string-identical SAME-ORDER (M list
  == RQ list, 14ch; QM7 b20,21,22,80-83 by COL
  m=off&15 vs RQ7 b20,21,22,80-83 by ROW
  r=off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated) -- 55th odd-band
  RQ==M instance (odds 54->55); 26th full/diff
  survey (survey counts every method RQ-vs-M
  regardless of degree; 3rd identical case:
  b472, b474, b475).
  M-tails 16/16 ALL NEW vs P366T col-led tails
  (overlap 0; P366T RM 16x8B frame first-hand
  from code, tails last-4B); RQ-tails 16/16 ALL
  NEW vs P366T TR9 (overlap 0) + 16/16 ALL NEW
  vs P366T RM (overlap 0); RM-tails 16/16 ALL
  NEW vs P366T RM (overlap 0) + 16/16 ALL NEW
  vs P366T TR9 (overlap 0); AM/CM/M/QR/RM/RQ
  0-overlap vs P366 all six (widths P367 vs
  P366: AM 6B vs 7B, CM 3B vs 6B, M 7B vs 9B, QR
  1B vs 1B, RM 8B vs 8B, RQ 7B vs 9B).
  AC 80, CC 83, QC 78, RC 71; C _N decls
  80/83/78/71 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 const b6 in
  AC (b1 const 01, b2-3 const 00; b5 const 68
  deducted, in AC-missing; b84-87 consts
  95,76,58,3a A-lane); C b0 const 1c in CC
  (b1-3 const 00; b5 const 68 deducted, in
  CC-missing; b52 const 0x84 const-entry, in CC;
  b87 const 0x86 in CC; CC has no b84,85,86 (all
  in CM lane)); C b84,85,86 absent (M3/TAIL
  lane); Q b0 const cf 1-sig DIFFERS-from-PBA in
  QC first-hand (b1 const 01, b2-3 const 00; b5
  STEPS in VPOS, NO deduct; b84 absent R1-lane,
  b85 const 9b / b86 const ed / b87 const 86);
  R b0 const f3 + b1 const 1c in RC table,
  code-indexed first-hand).
  PBA88-PLAIN-M6b10 sig b6010000 x16 (b0 const
  b6 via AC b0; b5 const 68 deducted NOT in AC;
  AM 16/16 distinct NO pair; M6 b10,11,80-83
  positions FIRST this lane per code comment) +
  PBA sig b6 NEW vs P366 f5 (novelty = new sig
  b6 + AM 0-overlap).
  C10-1SIG-88-TAIL-M3 sig 1c000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  1c000000; CM 10/10 diverge 6ch b84,85,86;
  b87 const 0x86 in CC; b5 const 68 deducted NOT
  in CC).
  QUAD88-1SIG-QM7/R1-B5EDGE 1-sig cf010000
  DIFFERS-from-PBA-sig (b0 const cf in QC; b5
  STEPS 68->69 edge off30->31, in VPOS; m-tab
  b20,21,22,80-83 (M 16/16 14ch NO frags, m =
  off&15 first-hand; QM7 positions staged
  P351Q/P359Q per A-954, shape filed, no FIRST
  claimed beyond sheet) + r1 b84 R1 4/4 UNPAIRED
  BY-ROW const (q = off>>4 first-hand); tails =
  R1+9b/ed/86 quad-wide, full-tail pairs all lcs
  3 per guard + suffix/subseq/TSHARE 3/3/3/3/3/3
  + R1 all-distinct + QM7-shared-x3 48/48).
  Ring T88-SWAPPED-RM8/RQ7 1-sig f31c0000 x256
  (b0 const f3 256/256 oracle, in RC table; b1
  const 1c 256/256 oracle, in RC table; code-RM8
  b28,29,30,31,76-79 by COL RM 16/16 (positions
  staged P359R per A-954) + code-RQ7 b20,21,22,
  80-83 by ROW RQ 16/16 UNPAIRED (SWAPPED tails
  b80-83 row / b76-79 col; positions staged
  P343/P351R/P359R); b84-87 const d99bed86
  ring-wide NEW; b4=(0x43+2off)&FF + b5 = 0x69+
  (off>=95)+(off>=223) (C literals 67/105/95/223
  verified == 0x43/0x69/95/223; py hex 0x43/
  0x69)).
  VPOS partitions re-derived from code: PBA 7
  (missing 8 - 1; b4+M6 b10,11,80-83, b5 const
  deducted) / C10 4 (missing 5 - 1; b4+M3
  b84,85,86, b5 const deducted) / quad 10
  (missing 10 - 0; b4,b5+QM7 7+R1 1, b5 STEPS
  in VPOS, NO deduct) / T 17 (missing 17 - 0;
  b4,b5+RM8 8+RQ7 7, counter varies, NO deduct)
  -- all match Q-1079 (7/4/10/17); no GATE filed
  for b475 at battery time (nothing to compare).
  Code-consts vs A-954 INCL/EXCL (PBA 80 / C10
  83 / quad 78 / T88 71 excl): impl 80/83/78/
  71 = memo-excl EXACT -- no lag on odd band
  (deduct-only-when-vary holds; A-954 INCL
  +2/+2/+0/+0 = 82/85/78/71 for the two b5-
  const regions PBA/C10; memo-side, recorded, no
  code impact). VPOS 7/4/10/17 = memo EXACT.
  S-F lag stays 44.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 144453 / S1 144454 / A 144455-470 /
  C 144471-480 / Q 144481-544 / R 144545-800):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode; Q b5 step emerges from raw
  lencode + b5 formula comment) + R explicit
  counter (b4=(0x43+2off)&FF b5=0x69+(off>=95)+
  (off>=223); py hex 0x43/0x69; C staged
  decimal literals 67/105/95/223 re-derived:
  67==0x43, 105==0x69) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 12ch b10,11,80-83 M6; C 6ch lane b84-86 M3;
  Q 14ch/2ch QM7 b20,21,22,80-83/R1 b84; R 16ch/
  14ch RM8 b28,29,30,31,76-79 by COL / RQ7
  b20,21,22,80-83 by ROW).
  C blocks carry T96983/T96988/T96993/T97008/
  T97023/T97042 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 96983 verified
  in py; bounds + byte positions exact: A 12ch,
  C 6ch, Q 14ch/2ch, R 16ch/14ch),
  A/C raw lencode (no counter literals; A/C b5
  const deducted NOT in AC/CC) + Q b5 STEP
  0x68+(off>=31) edge 144511->144512 + R counter
  b4=(67+2off)&FF + (105)+(off>=95)+(off>=223)
  (C literals 67/105/95/223 verified), temps
  _t7325-7340 (base max _t7324, no reuse) +
  _i4447/4449/4452/4455 (base max _i4445, no
  reuse) + _b4446/4448/4450/4451/4453/4454
  (base max _b4444, no reuse), union 4446-4455
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P366R close (C "T10P3670 singleton" after
  "CLOSED T10P366R"; py return 0 + S0 guard
  96983 after "CLOSED T10P366R" print), at
  dispatch tail (P367R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches A-954 geometry (PB0 NEW-sig 33/84;
  PB1 sig-REPEAT 65/88 SAME-own-C10 79/88;
  PBA88-PLAIN-M6b10 VPOS 7 sig-b6 b5 const M6
  16/16 distinct; C10-1SIG-88-TAIL-M3 VPOS 4
  SAME-as-PB1-sig b5 const M3 10/10 diverge;
  QUAD88-1SIG-QM7/R1-B5EDGE VPOS 10 + R1 4/4
  UNPAIRED 59/79/99/b9 + suffix-lcs-3/3/3/3/3/3
  + R1-distinct + QM7 + NO frags + M-tails NEW;
  T88-SWAPPED-RM8/RQ7 VPOS 17 + RM8-by-COL/
  RQ7-by-ROW + SWAPPED-tails + b84-87 d99bed86
  + counter 43/69/95/223; lencode 348/348
  whole-tier, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R1 rows + tails + LCS
  + frame + consts stand; const-count note is
  impl==excl this tier per memo, geometry exact,
  PORT verdict stands; M==RQ identical first-hand
  this tier, tier stands).
- Edges via counter formula first-hand: A head
  8f/68 tail ad/68 b5set {68} NO step, 0 ff
  (b4 base 0x8f step2 16/16, b0 const b6 16/16);
  C head af/68 tail c1/68 b5set {68} NO step,
  0 ff (b0 const 1c 10/10); Q head c3/68
  pre-edge off30 (ff/68) edge off31 (01/69)
  144512 tail 41/69 b5set {68,69} EDGE (b4 base
  0xc3 step2 64/64 exact-set range c3..41
  wraps-once, min 0x01 max 0xff, exactly 1 ff in
  64); ring pre-edge off94 (ff/69), edge off95
  (01/6a); pre-edge off222 (ff/6a) -> edge
  off223 (01/6b); exactly 2 ff in 256 (R b4
  exact-set 43-step2 256 vals / 128 uniq); R head
  43/69 tail 41/6b; formulas re-derived from
  T10P367R code text (43/69/95/223 hex==dec) +
  T10P367A/C/Q text (raw lencode + B5EDGE
  comment); all edge pins + head/tail pins +
  for-list Q boundary + R mid pins in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5
  match raw lencode (8b/68 + 8d/68). Ring
  counter==raw-lencode 256/256 + Q 64/64 + A
  16/16 + C 10/10. Odd-lencode 348/348
  (16+10+64+256+2). No DISSENT on cut bytes
  (edges475.py EDGES-GREEN, A/C NO-ff + Q
  single-ff + ring 2-ff range-with-wrap + Q-range
  wrap+2 + R counter asserts verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 231/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 231 content / 0 del (no GATE at file
  time; content-line variance 231/232 recorded:
  b468/b469/b474/b475 231, b470/b471/b472/
  b473 232); for-line replaced by superset (base
  for-N subset of band, removed 0); fine-norm
  equivalent (for475base.nums subset for475.nums,
  removed 0; C-scope del 0).
- Wall on band diff added lines (scope
  69e06615..6a9df578, 898 added lines): vendor
  0 hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits; 0 `aea` substrings (hex-fragment pattern
  of b470/b471 did NOT resume any band this
  round); 0 true hits. Files touched: rgramc.c
  608/0, rgram.py 231/0 purely additive,
  test_rgram.sh 1/1 (for-line extension), PINS
  +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-ind4 756->758
  (+2: 144453/144454) / ranges py-ind4 898->
  902 (+4; py file-wide 766->768 +2 / ranges
  920->924 +4 (+10 early-tier singleton guards /
  +22 early-tier range guards first-hand); C
  dispatch singletons 761->763 +2 / ranges 920->
  924 +4 (C dispatch = ind4 + 5; C unanchored
  766->768 = dispatch + 5 dip-ternary guards,
  same 5 lines first-hand); same 6 P367 blocks
  both sides; no elif/else-if added either side:
  py file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2090->2096 +6 both sides, seal 2184->2190 +6
  (commit msgs; offset +94 vs CLOSED-T10P stable):
  all agree, no slip (absolute seal inherits lane
  tally; delta verified).
  Viewer-vs-sweep reconcile first-hand (no GATE
  absolutes at file time; reconciled vs A-954
  commit-msg seal + code): dispatch-exact ind4
  758/902 + file-wide 768/924 (py) + C dispatch
  763 / unanchored 768 / ranges 924; 4sp dispatch
  reconciled first-hand; file-wide unanchored
  differs by 10 non-dispatch early-tier singleton
  guards + 5-count C-vs-py dip-guard offset;
  deltas +2/+4/+6 every method.
- CONFIRM evidence (CONVERT-01 rule b):
  A-954-q1079-P367 verdict CONFIRM 52/52 CLEAN
  (own bed r5-P367 144453..144828 + r5-P366
  cross-refs, BAD=0 + direct-oracle 2/2
  byte-match; verifier v501.py P367 52/52 PASS;
  file present, counts verified; tier GATED PORT;
  novelty gated: b52-const-entry variant 0x84 in
  CC (P366 0x72, P365 0xc5, P364 0xb8, P363
  0xb9); M-tails 16/16 ALL NEW vs P366T col-led
  tails; exact-value corroboration incl PB0
  NEW-sig 33/84, PB1 sig-REPEAT 65/88 SAME-own-
  C10 79/88, PBA16-PLAIN sig-b6 VPOS 7, C10
  sig-1c SAME-PB1 VPOS 4, QUAD64 1-sig-B5EDGE +
  R1 rows + suffix-lcs-3/3/3/3/3/3 + R1-distinct
  + QM7 + NO frags + M-tails NEW, T256-SWAPPED +
  RM8-by-COL/RQ7-by-ROW + SWAPPED-tails + const
  d99bed86 + counter/edges; plus const-count
  note: A-954 excl 80/83/78/71 memo-exact,
  committed tables match excl exactly -- no
  writer lag this tier, geometry exact, PORT
  verdict stands). Agrees with cport commit msg
  (PYID 10916, RGRAM 21832).
- FWD-check: banked Next-P368 (A-954 + Q-1079
  forward notes, both read first-hand): PB0
  2f9a600e @144801 (pay84, sig-REPEAT 30/84 vs
  P367PB0) + PB1 1c000000 @144802 (pay88,
  sig-REPEAT 80/88 vs P367PB1) + PBA sig 88010000
  (144803..144818, 16 cells) + C10-region 1f000000
  x10 (144819..144828, 10 cells, DIFFERS-from-
  PB1-sig) -- no lane code landed at file time;
  pre-corroboration DEFERRED; CONSUME-FIRST with
  re-corroboration at that time per bank-miss
  lesson.
- Quiz: no conflicting CLAIM/GATE/FLAG on b475
  (adjacent evens b474 = 69e06615 C port live,
  base-use only, no verdict beyond; FLAG files
  name no b475 band; DISSENTs are q846/847/849
  unrelated tiers).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r76/
  (build475/, pyid475.log, rgram475py/c.log,
  cmp475.py, seteq475.py, ownloop475.py,
  secf475a/b/c.py, edges475.py (+.log),
  tabaudit475.py (+.log), w475loop.log,
  smoke475.log, units475.log, band475.diff/
  .addedlines/.addedc, for475.nums/added).

Verdict: PASS. No RED. 348-pin contiguous range
144453..144800 sealed. Round 4/4 = CAP.
