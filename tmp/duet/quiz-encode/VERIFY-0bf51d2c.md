# VERIFY-0bf51d2c b469 T10P361 pins 142365..142712 (348 pins) PASS

Seat viewer-r75, first-hand, tree @0bf51d2c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r75.
Base 97337e61 (b468 tip, 2148 tiers sealed; this
seat's VERIFY-97337e61 PASS-filed same round,
base-use only, respected). Band = 3226e14d (py
merge w2b@902bea99 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 0bf51d2c (C
port; parent == 3226e14d verified via git
rev-list --parents). Chain 3226e14d parent ==
97337e61 verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P361 shape (A-947 + Q-1072 agree,
both read first-hand) CONSUMED FIRST and
VERIFIED first-hand EXACT: PB0 ef9ea60c @142365
(S0 head; NEW-sig sigdiff-3 32/84 diff vs
P360PB0 @ n142017, b0-2 IN diff with b3 same,
positions
[0-2,4,5,19-31,36,37,60-71] first-hand, NOT
byte-equal) + PB1 1d000000 @142366 (S1 head;
NEW-sig 58/88 diff vs P360PB1 @ n142018, sig
b0 IN diff with b1-3 same, positions
[0,4,5,11,19,26-44,46-75,84-87] first-hand,
NOT byte-equal; 40/88 vs own C10[0] n142383
(cell 0; cells 1-9 diff 41 extra [52] = b52
2-valued mid-body M; all-10 staged+oracle;
sig b0-3 same-sig NOT in diff; NOT-UNIFORM
[1x40+9x41] NOT TRUE-uniform: b52 step;
NOT byte-equal; S1 SIG-EQ own C10; S1 SIG-
DIFFERS own PB0 ef-vs-1d; 52/88 vs P360C10[0]
n142035 DIFFERS-sig) + PBA88-PLAIN-M8b52
ff010000 x16 @142367-382 + C10-region 1d000000
pay88 x10 @142383-392 (SAME-as-PB1-sig, M5
lane b52,84-87; b52 2-valued [0x92,0xb2]
first-hand) -- all corroborated against lane
code both sides before any battery step (no
bank-miss).

- Build: seat-private build469/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256
  7546e4c2... (prefix == GATE 9530fc99/sha256
  7546e4c2, verified programmatically, never
  hand-transcribed).
- RGRAMC-PYID 10742/10742 covered=10742/10742
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21484/21484 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21484/21484 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21484/21484, sorted +
  raw identical; cmp469.py GREEN).
- PINS-RGRAM cells set-eq 21484/21484 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq469.py GREEN). PINS 21486 lines
  first-hand (2 hdr + 21484 rows; base 21428
  lines / 21426 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10713->10742 +29/-0 (python
  sets, trailing-';' strip, never comm): 142365
  142366 142367 142368 142374 142375 142381
  142382 142383 142384 142387 142388 142391
  142392 142393 142408 142409 142424 142425
  142440 142441 142456 142457 142463 142464
  142530 142591 142592 142712 (== GATE sampled
  list EXACT).
  29 = 2 sing (142365 142366 offs 0/1) + A 6
  (head pair 142367/142368 off0/1 + mid pair
  142374/142375 off7/8 + tail pair 142381/
  142382 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 58 NO
  edge) + C 6 (head pair 142383/142384 off0/1
  + mid pair 142387/142388 off4/5 + tail pair
  142391/142392 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 58 NO edge) + Q 8 (head
  142393 off0 + boundary pairs 142408/142409
  off15/16 + 142424/142425 off31/32 + 142440/
  142441 off47/48 + tail 142456 off63; NO mid
  (b5 const 58 NO edge), all boundaries pair-
  covered, first-hand) + R 7 (head 142457 off0
  + edge pair 142463/142464 off6/7 + mid pin
  142530 off73 + edge pair 142591/142592
  off134/135 + tail 142712 off255; 1-mid shape
  off73 NEW, both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21484-21426.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit469.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 190 PASS 0 FAIL first-run (0 seat-script
  fixes; py A/C/Q raw-lencode pattern carried
  from b468 -- formulas in comments/Q-1073,
  corroborated by edges; C-counter space-strip
  carried; NO GATE prose slip this band: VPOS
  9/6/11/17 == code+Q-1073 viewer-convention
  EXACT; QC b1-3 is 01/00/00 first-hand both
  sides -- slip class clear 2 bands running).
  Inventory exactly the 12 tables both sides
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no M42/X42/
  H42/L42, no QB/PT/FM, no RT/TT (ring, not
  ROWTAIL), no QT (R2 carries b84,85 in-row +
  b86/b87 consts)) + _T10P361C numeric-head
  probe (74 entries py = 74 C _N, pre-exists
  since band29, not a table).
  S0 168ch sig ef9ea60c NEW-sig sigdiff-3 (32/84
  payload diff vs P360S0, positions
  [0-2,4,5,19-31,36,37,60-71] first-hand, b0-2
  IN diff with b3 same, NOT byte-equal) / S1
  176ch sig 1d000000 NEW-sig (58/88 payload diff
  vs P360S1, positions
  [0,4,5,11,19,26-44,46-75,84-87] first-hand,
  sig b0 IN diff with b1-3 same, NOT byte-
  equal; vs own C10 cells NOT-UNIFORM [1x40+
  9x41] staged+oracle: cell 0 diff 40 positions
  [4,19,38,39,46,48-51,53-79,84-87], cells 1-9
  diff 41 extra [52] (b52 2-valued mid-body
  [0x92,0xb2] first-hand), sig b0-3 same-sig
  NOT in diff; NOT byte-equal; S1 SIG-EQ own
  C10; S1 SIG-DIFFERS own PB0; S1[52]=0x92 ==
  CM cell-0 b52), staged as full-payload
  singletons.
  AM 16/16 16ch distinct, CM 10/10 10ch diverge
  (b52 2-valued mid-body M [0x92,0xb2]
  first-hand), M 16/16 16ch distinct, QR 4/4
  4ch R2 rows a3ac/c3ac/e3ac/03ad exact tuples
  (full tails = R2 + b86 f9 / b87 5d quad-wide
  exact; trailing-suffix = subseq = TSHARE =
  3/3/2/3/2/2 (all-3 agree first-hand; pairs
  (0,1)/(0,2)/(1,2) trailing 3 rest 2; full
  tuples pairwise unequal, 4 distinct)), RM
  16/16 14ch distinct, RQ 16/16 16ch distinct,
  no QT + no RT + no F (no frags).
  M-vs-RQ FULL8 (M 8B lanes [6,7,9,10,80-83] vs
  RQ 8B lanes [6,7,9,10,76-79]: rows 16/16
  EQUAL, per-col first-8 all 16/16, col uniqs
  [14,12,3,2,16,16,16,15] both sides EQUAL,
  full-row sets EQUAL, sorted rows EQUAL, M list
  == RQ list) -- 52nd odd-band RQ==M instance,
  10th FULL degree (FULL8-identity precedented,
  multiple on file; same-width 8B/8B, low lanes
  agree, tails b80-83 vs b76-79 differ; viewer
  chain: odds 51->52; 20th full-identity
  survey); ordered per lesson (d) (rows EQUAL +
  sets EQUAL + sorted EQUAL, same order;
  STANDARD-split (TM7 by COL / TR8 by ROW
  UNPAIRED) tails differ, tables equal); width
  predictor dead, never cited; Deduct never
  cross-cited in UNIQ (FULL assertion uses only
  within-band position-exact + set facts);
  M-tails 16/16 ALL NEW vs P360T RQ row-led
  tails (overlap 0; P360T RQ 16x6B frame first-
  hand from code, tails last-4B); RQ-tails 16/16
  ALL NEW vs P360T RM col-led tails (overlap 0)
  + 16/16 ALL NEW vs P360T RQ (overlap 0); RM-
  tails 16/16 ALL NEW vs P360T RM (overlap 0) +
  16/16 ALL NEW vs P360T RQ (overlap 0);
  AM/CM/M/QR/RM/RQ 0-overlap vs P360 all six
  (widths P361 vs P360: AM 8B vs 9B, CM 5B vs
  7B, M 8B vs 6B, QR 2B vs 1B, RM 7B vs 9B, RQ
  8B vs 6B).
  AC 78, CC 81, QC 76, RC 71; C _N decls
  78/81/76/71 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 const ff in
  AC (b1 const 01, b2-3 const 00; b5 const 58
  deducted, in AC-missing); C b0 const 1d in CC
  (b1-3 const 00; b5 const 58 deducted, in
  CC-missing; b52 2-valued mid-body, in CC-
  missing locus); Q b0 const d6 1-sig in QC
  first-hand (b1 const 01, b2-3 const 00; b5
  const 58 deducted, in QC-missing; b84/85
  absent R2-lane, b86 const f9 / b87 const 5d);
  R b0 const 26 + b1 const 1d in RC table,
  code-indexed first-hand).
  PBA88-PLAIN-M8b52 sig ff010000 x16 (b0 const
  ff via AC b0-3; AM 16/16 distinct NO pair; b5
  const 58 deducted NOT in AC; M8 b52-55,80-83
  positions STAGED P353A, shape filed b461, no
  FIRST claimed) + PBA sig ff NEW vs P360 b6.
  C10-1SIG-88-M5b52 sig 1d000000 x10 SAME-as-
  PB1-sig (full sig b0-3 in CC = 1d000000; CM
  10/10 diverge 10ch b52,84-87; CC has no
  b52,84-87 (all in CM lane); b52 2-valued
  [0x92,0xb2] mid-body M; b5 const 58 deducted
  NOT in CC).
  QUAD88-1SIG-QM8/R2-NOEDGE 1-sig d6010000 x64
  (b0 const d6 in QC; b5 const 58 deducted NOT
  in QC, NO edge; b4 base 0x73 step2 64/64
  range 73..f1 contig+2 NO wrap 0 ff; QM8
  b6,7,9,10,80-83 M 16/16 16ch distinct NO frags
  (m = off&15 first-hand; QM8 FIRST this lane,
  lane-set differs from b461, shape filed, no
  FIRST claimed) + R2 b84,85 rows a3ac/c3ac/
  e3ac/03ad 4/4 UNPAIRED BY-ROW const (q =
  off>>4 first-hand); tails = R2 + f9/5d
  quad-wide, full-tail trailing/subseq/TSHARE
  all-3 3/3/2/3/2/2 + R2-tuple-unequal).
  Ring T88-STANDARD-split-TM7/TR8 sig 261d0000
  x256 (b0 const 26 256/256 oracle, in RC
  table; b1 const 1d 256/256 oracle, in RC
  table; code-TM7 b13,14,15,80-83 by COL RM
  16/16 + code-TR8 b6,7,9,10,76-79 by ROW RQ
  16/16 UNPAIRED (SPLIT tails b80-83 col /
  b76-79 row; positions staged P313R/P350R-RM8,
  first STANDARD-TR use); b84-87 const
  23adf95d ring-wide NEW; b4=(243+2off)&FF +
  (88)+(off>=7)+(off>=135) (C literals
  243/88/7/135 verified == 0xf3/0x58/7/135; py
  hex 0xf3/0x58)).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - 1; b4+M8 b52-55,80-83, b5 const
  deducted) / C10 6 (missing 7 - 1; b4+M5
  b52,84-87, b5 const deducted) / quad 11
  (missing 12 - 1; b4+QM8 8+R2 2, b5 const
  deducted) / T 17 (missing 17 - 0; b4,b5+TM7
  7+TR8 8, counter varies, NO deduct) -- all
  match Q-1073 (9/6/11/17); GATE-0bf51d2c
  headlines 9/6/11/17 EXACT (viewer convention,
  no slip this band).
  Code-consts vs A-948 INCL/EXCL (PBA 78 / C10
  81 / quad 76 / T88 71 excl): impl 78/81/76/
  71 = memo-excl EXACT -- no lag on odd band
  (deduct-only-when-vary holds; Q b5-const here
  vs Q-steps at b461; A-948 INCL +3/+3/+3/+0
  = 81/84/79/71 for the three b5-const
  regions). VPOS 9/6/11/17 = memo EXACT.
  S-F lag stays 44; even sub-streak stays 26.
  M-tails 16/16 ALL NEW vs P360T row-led tails
  (overlap 0); RQ-tails 16/16 ALL NEW vs P360T
  RM col-led tails (overlap 0) + vs P360T RQ
  (overlap 0); RM-tails 16/16 ALL NEW vs P360T
  RM (overlap 0) + vs P360T RQ (overlap 0);
  AM/CM/M/QR/RM/RQ 0-overlap vs P360 all six.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 142365 / S1 142366 / A 142367-382 /
  C 142383-392 / Q 142393-456 / R 142457-712):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode; Q b5 const emerges from raw
  lencode) + R explicit counter (b4=(0xf3+2off)
  &FF b5=0x58+(off>=7)+(off>=135); py hex
  0xf3/0x58; C staged decimal literals 243/88/
  7/135 re-derived: 243==0xf3, 88==0x58) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 16ch b52-55,80-83 M8; C 10ch lane b52,84-
  87 M5; Q 16ch/4ch QM8 b6,7,9,10,80-83/R2
  b84,85; R 14ch/16ch STANDARD TM7 b13-15,
  80-83 by COL / TR8 b6,7,9,10,76-79 by ROW).
  C blocks carry T95592/T95597/T95602/T95617/
  T95632/T95652 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 95592 verified
  in py; bounds + byte positions exact: A 16ch,
  C 10ch, Q 16ch/4ch, R 14ch/16ch),
  A/C/Q raw lencode (no counter literals; C b5
  const deducted NOT in CC; Q b5 const deducted
  NOT in QC) + R counter b4=(243+2off)&FF +
  (88)+(off>=7)+(off>=135) (C literals
  243/88/7/135 verified), temps _t7229-7244
  (base max _t7228, no reuse) + _i4387/4389/
  4392/4395 (base max _i4385, no reuse) +
  _b4386/4388/4390/4391/4393/4394 (base max
  _b4384, no reuse), union 4386-4395
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P360R close (C "T10P3610 singleton" after
  "CLOSED T10P360R"; py return 0 + S0 guard
  95592 after "CLOSED T10P360R" print), at
  dispatch tail (P361R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side: C
  T34797/T4-plateau-B inner + dispatch tail; py
  dip-1077/T4-plateau-B inner line 59330 +
  dispatch tail 95671; unrelated scope).
  Matches A-948 geometry (PB0 NEW-sig sigdiff-3
  32/84; PB1 NEW-sig 58/88; SAME-as-own-C10
  40/88; differs-vs-own-PB0; PBA88-PLAIN-M8b52
  VPOS 9 sig-ff b5 const M8 16/16 distinct;
  C10-1SIG-88-M5b52 VPOS 6 SAME-as-PB1-sig b5
  const b52-2-valued M5 10/10 diverge;
  QUAD88-1SIG-QM8/R2-NOEDGE VPOS 11 + R2 4/4
  UNPAIRED a3ac/c3ac/e3ac/03ad + trailing
  3/3/2/3/2/2 all-3 agree + tuples-unequal +
  QM8 + NO frags + M-tails NEW; T88-STANDARD-
  split VPOS 17 + TM7-by-COL/TR8-by-ROW +
  SPLIT-tails + b84-87 23adf95d + counter
  f3/58/7/135; lencode 348/348 whole-tier, NO
  D dips) incl exact values (PBA/C10/QUAD/T88
  sigs, R2 rows + tails + LCS + SWP frame +
  consts stand; const-count note is impl==excl
  this tier per memo, geometry exact, PORT
  verdict stands; M-vs-RQ FULL8 first-hand
  this tier, tier stands).
- Edges via counter formula first-hand: A head
  3f/58 tail 5d/58 b5set {58} NO step, 0 ff
  (b4 base 0x3f step2 16/16, b0 const ff 16/16;
  GATE decimal {88} == 0x58 first-hand); C head
  5f/58 tail 71/58 b5set {58} NO step, 0 ff
  (b0 const 1d 10/10); Q head 73/58 tail f1/58
  b5set {58} NO step, 0 ff (b4 base 0x73 step2
  64/64 range 73..f1 contig+2 NO wrap); ring
  pre-edge off6 (ff/58), edge off7 (01/59);
  edge off134 (ff/59) -> off135 (01/5a);
  exactly 2 ff in 256; R head f3/58 tail f1/5a;
  mid off73 @142530 (85/59); formulas re-derived
  from T10P361R code text (f3/58/7/135 hex==dec)
  + T10P361A/C/Q text (raw lencode); all edge
  pins + mid pin 142530 + tail 142712 in for-
  list + 2 PASS lines each py+C. S0/S1 embedded
  b4/b5 match raw lencode (3b/58 + 3d/58). Ring
  counter==raw-lencode 256/256 + Q 64/64 + A
  16/16 + C 10/10. Odd-lencode 348/348
  (16+10+64+256+2). No DISSENT on cut bytes
  (edges469.py EDGES-GREEN, ring 2-ff range-with-
  wrap + Q-range NO-wrap asserts verified
  first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 231/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 231 content / 0 del (odd band 231
  like evens -- content-line count varies
  231/232, recorded); C+py-leg del-uniq 0 (sole
  del = old for-line churn); for-line replaced
  by superset (base for-N subset of band,
  removed 0); fine-norm equivalent
  (for468base.nums subset for469.nums, removed
  0; C-scope del 0).
- Wall on band diff added lines (scope
  97337e61..0bf51d2c, 898 added lines): vendor
  0 hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits; 0 `aea` substrings. Files touched:
  rgramc.c 608/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line
  extension), PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-ind4 744->746
  (+2: 142365/142366) / ranges py-ind4 874->
  878 (+4; py file-wide 754->756 +2 / ranges
  896->900 +4; C singletons 749->751 +2 /
  ranges 896->900 +4, same 6 P361 blocks both
  sides; no elif/else-if added either side: py
  file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2054->2060 +6 both sides, seal 2148->2154 +6
  (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
  Viewer-vs-sweep reconcile first-hand:
  GATE-tier absolutes file-wide-exact (py 754->
  756, ranges 896->900 -- all EXACT, no slip
  this band); 4sp dispatch 744->746 / 874->878
  reconciled first-hand; file-wide unanchored
  differs by 10 non-dispatch early-tier guards +
  5-count C-vs-py dip-guard offset; deltas
  +2/+4/+6 every method.
- CONFIRM evidence (CONVERT-01 rule b):
  A-948-q1073-P361 verdict CONFIRM 50/50 CLEAN
  (own bed r5-P361 142365..142740 + r5-P360
  cross-refs, BAD=0; verifier v501.py P361
  50/50 PASS; file present, counts verified;
  tier GATED PORT; novelty gated: M-tails 16/16
  ALL NEW vs P360T row-led tails; exact-value
  corroboration incl PB0 NEW-sig sigdiff-3
  32/84, PB1 NEW-sig 58/88, PBA16 sig-ff VPOS
  9, C10 sig-1d SAME-PB1 VPOS 6 b52-2-valued,
  QUAD64 1-sig-NOEDGE + R2 rows + trailing
  3/3/2/3/2/2 all-3 agree + tuples-unequal +
  QM8 + NO frags + M-tails NEW, T256-STANDARD
  + TM7-by-COL/TR8-by-ROW + SPLIT-tails +
  const 23adf95d + counter/edges; plus const-
  count note: A-948 excl 78/81/76/71 memo-
  exact, committed tables match excl exactly
  -- no writer lag this tier, geometry exact,
  PORT verdict stands). Agrees with cport
  commit msg (PYID 10742, RGRAM 21484).
- FWD-check: banked Next-P362 from A-948+Q-1073
  agreement (both read first-hand)
  pre-corroborated EXACT vs P362 lane code
  (d02550f5, git show, no checkout): PB0
  ef9ea60e 168ch pay84 @142713 (NEW-sig 1B-off
  31/84 vs P361PB0) + PB1 1d000000 176ch
  pay88 @142714 (SIG-REPEAT 52/88 vs P361PB1) +
  PBA88 sig db010000 guard 142715..142730 (16
  cells) + C10-region 1d000000 x10 guard
  142731..142740 (10 cells, SAME-as-PB1-sig) --
  banked for b470 CONSUME-FIRST and re-
  corroborate EXACT at that time per bank-miss
  lesson (P362 lane code on file; corroboration
  mandatory).
- Quiz: no conflicting CLAIM/GATE/FLAG on b469
  (adjacent odds b467/b471 + evens live base-
  use only, no verdict on b469).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r75/
  (build469/, pyid469.log, rgram469py/c.log,
  cmp469.py, seteq469.py, ownloop469.py,
  secf469a/b/c.py, edges469.py, tabaudit469.py,
  w469loop.log, smoke469.log, units469.log,
  band diff via git).

Verdict: PASS. No RED. 348-pin contiguous range
142365..142712 sealed. Round 2/4 toward cap.
