# VERIFY-44ad8496 b472 T10P364 pins 143409..143756 (348 pins) PASS

Seat viewer-r76, first-hand, tree @44ad8496,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r76.
Base 5dcf81a8 (b471 tip, 2166 tiers sealed; this
seat's VERIFY-5dcf81a8 PASS-filed r75,
base-use only, respected). Band = fbf28aed (py
merge w2b@59a9e107 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 44ad8496 (C
port; parent == fbf28aed verified via git
rev-list --parents). Chain fbf28aed parent ==
5dcf81a8 verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__; PYTHONDONTWRITEBYTECODE=1).

Banked Next-P364 shape (forward note on file in
A-950 + Q-1075, both read first-hand; brief named
A-949+Q-1074 but those sheets carry only the P363
forward -- memo-side label variance, content ==
banked shape) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 ef0da90f @143409
(S0 head; NEW-sig 1B-off 32/84 diff vs
P363PB0 @ n143061, sig b3 IN diff with b0-2
same, positions
[3,4,5,20-23,25-30,32,33,36-39,41,64-75]
first-hand, NOT byte-equal) + PB1 1e000000
@143410 (S1 head; NEW-sig 43/88 diff vs
P363PB1 @ n143062, sig b0 IN diff with b1-3
same, positions
[0,4,5,19,26,27,34-43,45-59,72-79,84-87]
first-hand, NOT byte-equal; 57/88 vs own C10[0]
n143427 (all-10 identical 57-diff positions,
sig b0 IN diff with b1-3 same; UNIFORM-57
SIG-DIFFERS, NOT TRUE-uniform; chain stays 37,
b468 class; P338 uniform-rule dispute stays
DEFERRED to sweep accounting, never
re-litigated) + PBA88-PLAIN-M7b6 e6010000
x16 @143411-426 + C10-region 1f000000 pay88
x10 @143427-436 (DIFFERS-from-PB1-sig 1f-vs-1e)
-- all corroborated against lane code both sides
before any battery step (py==C S0/S1 staged
strings; no bank-miss).

- Build: seat-private build472/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 c06de752...
  (GATE-44ad8496 states no rgramc sha -- sha
  granularity variance class, recorded first-hand
  here, never hand-transcribed).
- RGRAMC-PYID 10829/10829 covered=10829/10829
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21658/21658 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21658/21658 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21658/21658, sorted +
  raw identical; cmp472.py GREEN).
- PINS-RGRAM cells set-eq 21658/21658 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq472.py GREEN). PINS 21660 lines
  first-hand (2 hdr + 21658 rows; base 21602
  lines / 21600 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10800->10829 +29/-0 (python
  sets, trailing-';' strip, never comm): 143409
  143410 143411 143412 143418 143419 143425
  143426 143427 143428 143431 143432 143435
  143436 143437 143439 143468 143484 143487
  143488 143500 143501 143532 143533 143615
  143616 143743 143744 143756 (== GATE sampled
  list EXACT).
  29 = 2 sing (143409 143410 offs 0/1) + A 6
  (head pair 143411/143412 off0/1 + mid pair
  143418/143419 off7/8 + tail pair 143425/
  143426 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 60 NO
  edge) + C 6 (head pair 143427/143428 off0/1
  + mid pair 143431/143432 off4/5 + tail pair
  143435/143436 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 60 NO edge) + Q 7 (head
  143437 off0 + 143439 off2 + mid 143468 off31
  + pre-edge 143484 off47 + edge pair 143487/
  143488 off50/51 (ff->01 + b5 STEP 60->61) +
  tail 143500 off63; b5 B5EDGE off50->51,
  pair-covered except off47 mate) + R 8 (head
  143501 off0 + pair 143532/143533 off31/32 +
  edge pair 143615/143616 off114/115 + edge pair
  143743/143744 off242/243 + tail 143756 off255;
  both counter edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21658-21600.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit472.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 190 PASS 0 FAIL first-run (NO seat-script
  fix needed this band; NO GATE prose slip in the
  tables themselves; 1 GATE headline note in the
  VPOS class below + 1 GATE arithmetic note;
  QC b1-3 is 01/00/00 first-hand both sides --
  slip class clear 5 bands running).
  Inventory exactly the 12 tables both sides
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no M42/X42/
  H42/L42, no QB/PT/FM, no RT/TT (ring, not
  ROWTAIL), no QT (R4 carries b84-87 in-row, no
  b86/b87 consts); no _T10P364C numeric-head
  probe -- precedent since band29, only band29-
  range cover it).
  S0 168ch sig ef0da90f NEW-sig 1B-off
  (32/84 payload diff vs P363S0, positions
  [3,4,5,20-23,25-30,32,33,36-39,41,64-75]
  first-hand, sig b3 IN diff with b0-2 same, NOT
  byte-equal) / S1 176ch sig 1e000000 NEW-sig
  (43/88 payload diff vs P363S1, positions
  [0,4,5,19,26,27,34-43,45-59,72-79,84-87]
  first-hand, sig b0 IN diff with b1-3 same, NOT
  byte-equal; vs own C10 cells UNIFORM-57
  staged+oracle: all-10 identical 57-diff
  positions [0,4,6-15,19-55,80-87], sig b0 IN
  diff with b1-3 same; NOT byte-equal; S1 SIG-
  DIFFERS own C10 (1e-vs-1f); S1 SIG-DIFFERS own
  PB0; NOT TRUE-uniform, chain stays 37),
  staged as full-payload singletons;
  S0/S1 embedded b4/b5 63/60 + 65/60 match raw
  lencode.
  AM 16/16 14ch distinct, CM 10/10 8ch diverge
  (b84-87 M4 lane, all 10 distinct), M 16/16
  16ch distinct, QR 4/4 8ch R4 rows 422ff583/
  622ff583/982ab2c4/46ecbff1 exact (tails = R4
  rows 8ch quad-wide exact; full-tail suffix =
  subseq = TSHARE = 3/0/0/0/0/0 (all-3 agree
  first-hand; pair (0,1) trailing 3 rest 0; full
  tuples pairwise unequal, 4 distinct)), RM 16/16
  16ch distinct, RQ 16/16 16ch distinct, no QT +
  no RT + no F (no frags).
  M==RQ 16/16 string-identical SAME-ORDER (M list
  == RQ list; QM8 b0,10,11,16,80-83 by COL
  m=off&15 vs TR9 b0,10,11,16,76-79 by ROW
  r=off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated) -- 53rd even-band
  RQ==M instance (evens 52->53); 23rd full/diff
  survey (survey counts every method RQ-vs-M
  regardless of degree).
  M-tails 16/16 ALL NEW vs P363T col-led tails
  (overlap 0; P363T RM 16x8B frame first-hand
  from code, tails last-4B); RQ-tails 16/16 ALL
  NEW vs P363T TR7 (overlap 0) + 16/16 ALL NEW
  vs P363T RM (overlap 0); RM-tails 16/16 ALL
  NEW vs P363T RM (overlap 0) + 16/16 ALL NEW
  vs P363T TR7 (overlap 0); AM/CM/M/QR/RM/RQ
  0-overlap vs P363 all six (widths P364 vs
  P363: AM 7B vs 6B, CM 4B vs 5B, M 8B vs 7B, QR
  4B vs 2B, RM 8B vs 8B, RQ 8B vs 9B).
  AC 79, CC 82, QC 74, RC 70; C _N decls
  79/82/74/70 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 const e6 in
  AC (b1 const 01, b2-3 const 00; b5 const 60
  deducted, in AC-missing; b84-87 consts
  64,cc,5f,b7 A-lane); C b0 const 1f in CC
  (b1-3 const 00; b5 const 60 deducted, in
  CC-missing; b52 const 0xb8 const-entry, in CC;
  CC has no b84-87 (all in CM lane)); C b84-87
  absent (M4/TAIL lane); Q b0 ABSENT colsplit
  (b0=42 iff col<2, 8 cells 42 + 56x95 via M
  rows 0,1; b1 const 01, b2-3 const 00; b5 STEPS
  in VPOS, NO deduct; b84-87 absent R4-lane, no
  b86/b87 consts); R b0 ABSENT row-led (b0=42
  rows0-1 else 95 via RQ rows 0,1; b1 const 1f
  in RC table, code-indexed first-hand);
  R b84-87 const 66ecbff1 ring-wide).
  PBA88-PLAIN-M7b6 sig e6010000 x16 (b0 const
  e6 via AC b0; b5 const 60 range-emergent via
  raw lencode NOT in AC; AM 16/16 distinct NO
  pair; M7 b6,7,9,80-83 positions staged P356A
  per code comment) + PBA sig e6 NEW vs P363 96
  (novelty = new sig e6 + AM 0-overlap).
  C10-1SIG-88-TAIL-M4 sig 1f000000 x10
  DIFFERS-from-PB1-sig (full sig b0-3 in CC =
  1f000000; CM 10/10 diverge 8ch b84-87;
  CC has no b84-87 (all in CM lane); b5 const
  60 range-emergent raw lencode).
  QUAD88-2SIG-QM8/R4-COLSPLIT 2-sig 42010000/
  95010000 (b0=42 iff (off&15)<2: 8 cells 42 +
  56x95; M-b0 entries 0,1 = 42 rest 95) m-tab
  b0,10,11,16,80-83 (M 16/16 16ch NO frags, m =
  off&15 first-hand; QM8 positions FIRST this
  lane per A-951, lane-set differs, shape filed,
  no FIRST claimed beyond sheet) + r4 b84,85,
  86,87 R4 4/4 UNPAIRED BY-ROW const (q =
  off>>4 first-hand); tails = R4 rows 8ch
  quad-wide, full-tail pairs (0,1,3) rest 0 per
  guard, full-tail suffix/subseq/TSHARE
  3/0/0/0/0/0 + R4 all-distinct + QM8-shared-x3
  48/48).
  Ring T88-2SIG-TM8/TR9-ROWSPLIT 2-sig
  (rows0-1 421f0000 x32 + rows2-15 951f0000
  x224 staged+oracle first-hand; RQ b0 row-led
  42 rows0-1 else 95; b1 const 1f; code-TM8
  b12,13,18,19,80-83 by COL RM 16/16 (staged
  P356R) + code-TR9 b0,10,11,16,76-79 by ROW RQ
  16/16 UNPAIRED (SPLIT tails b80-83 col /
  b76-79 row; positions FIRST this lane);
  b84-87 const 66ecbff1 ring-wide NEW; b4=
  (0x1b+2off)&FF + b5 = 0x61+(off>=115)+
  (off>=243) (C literals 27/97/115/243 verified
  == 0x1b/0x61/115/243; py hex 0x1b/0x61)).
  VPOS partitions re-derived from code: PBA 8
  (missing 9 - 1; b4+M7 b6,7,9,80-83, b5 const
  deducted) / C10 5 (missing 6 - 1; b4+M4
  b84-87, b5 const deducted) / quad 14
  (missing 14 - 0; b0,b4,b5+QM8 8+R4 4, b5 STEPS
  in VPOS, NO deduct) / T 18 (missing 18 - 0;
  b0,b4,b5+TM8 8+TR9 8, counter varies, NO
  deduct) -- code+Q-1076 8/5/14/18; GATE-44ad8496
  headlines 8/6/14/18 (C10 differs by 1; A-951
  carries consts only, no VPOS headlines) --
  VPOS-number variance class instance (sweep-seat
  GATE vs viewer varying-of-{b4,b5}+mtab+rtab
  with deduct-const-b5; Q-sheets agree viewer
  convention); recorded + still PASS (code GREEN).
  Code-consts vs A-951 INCL/EXCL (PBA 79 / C10
  82 / quad 74 / T88 70 excl): impl 79/82/74/
  70 = memo-excl EXACT -- no lag on even band
  (deduct-only-when-vary holds; const = W-|VPOS|
  per A-773 with PBA/C10 -1 each for b5-const
  per Q-1076 sheet-side note -- recorded, no code
  impact). VPOS 8/5/14/18 viewer-convention.
  S-F lag stays 44.
  GATE "32nd even band running" list holds 31
  (b412..b472 step 2 = 31 bands) -- correct is
  31st; GATE arithmetic slip, memo-side, recorded.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 143409 / S1 143410 / A 143411-426 /
  C 143427-436 / Q 143437-500 / R 143501-756):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode; Q b5 step emerges from raw
  lencode + b5 formula comment) + R explicit
  counter (b4=(0x1b+2off)&FF b5=0x61+(off>=115)+
  (off>=243); py hex 0x1b/0x61; C staged
  decimal literals 27/97/115/243 re-derived:
  27==0x1b, 97==0x61) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 14ch b6,7,9,80-83 M7; C 8ch lane b84-87
  M4; Q 16ch/8ch QM8 b0,10,11,16,80-83/R4
  b84,85,86,87; R 16ch/16ch TM8 b12,13,18,19,
  80-83 by COL / TR9 b0,10,11,16,76-79 by
  ROW).
  C blocks carry T96288/T96293/T96298/T96313/
  T96328/T96348 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 96288 verified
  in py; bounds + byte positions exact: A 14ch,
  C 8ch, Q 16ch/8ch, R 16ch/16ch),
  A/C/Q raw lencode (no counter literals; A/C b5
  const deducted NOT in AC/CC; Q b5 STEP 0x60+
  (off>=51) in comment + edge 143487->143488) +
  R counter b4=(27+2off)&FF + (97)+(off>=115)+
  (off>=243) (C literals 27/97/115/243
  verified), temps _t7277-7292 (base max _t7276,
  no reuse) + _i4417/4419/4422/4425 (base max
  _i4415, no reuse) + _b4416/4418/4420/4421/
  4423/4424 (base max _b4414, no reuse), union
  4416-4425 contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P363R close (C "T10P3640 singleton" after
  "CLOSED T10P363R"; py return 0 + S0 guard
  96288 after "CLOSED T10P363R" print), at
  dispatch tail (P364R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side by
  count, tail hit verified just after R close
  both sides; inner hit identity not probed this
  band -- counts + tail verified, unrelated
  scope).
  Matches A-951 geometry (PB0 NEW-sig 1B-off
  32/84; PB1 NEW-sig 43/88 DIFFERS-own-C10
  57/88; PBA88-PLAIN-M7b6 VPOS 8 sig-e6 b5
  const M7 16/16 distinct; C10-1SIG-88-TAIL-M4
  VPOS 5 DIFFERS-from-PB1-sig b5 const M4 10/10
  diverge; QUAD88-2SIG-QM8/R4-COLSPLIT VPOS 14
  + R4 4/4 UNPAIRED 422ff583/622ff583/982ab2c4/
  46ecbff1 + suffix-lcs-3/0/0/0/0/0 + R4-
  distinct + QM8 + NO frags + M-tails NEW;
  T88-2SIG-TM8/TR9-ROWSPLIT VPOS 18 + TM8-by-
  COL/TR9-by-ROW + SPLIT-tails + b84-87 66ecbff1
  + counter 1b/61/115/243; lencode 348/348
  whole-tier, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R4 rows + tails + LCS
  + COLSPLIT frame + consts stand; const-count
  note is impl==excl this tier per memo,
  geometry exact, PORT verdict stands; M==RQ
  16/16 string-identical same-order first-hand
  this tier, tier stands).
- Edges via counter formula first-hand: A head
  67/60 tail 85/60 b5set {60} NO step, 0 ff
  (b4 base 0x67 step2 16/16, b0 const e6 16/16);
  C head 87/60 tail 99/60 b5set {60} NO step,
  0 ff (b0 const 1f 10/10); Q head 9b/60 pre-
  edge off50 (ff/60) edge off51 (01/61) 143488
  tail 19/61 b5set {60,61} STEP (b4 base 0x9b
  step2 64/64 exact-set range 9b..19 wrap+2,
  exactly 1 ff in 64, min 0x01 max 0xff); ring
  pre-edge off114 (ff/61), edge off115 (01/62);
  edge off242 (ff/62) -> off243 (01/63); exactly
  2 ff in 256 (R b4 exact-set 1b-step2 256 vals /
  128 uniq); R head 1b/61 tail 19/63; formulas
  re-derived from T10P364R code text (1b/61/115/
  243 hex==dec) + T10P364A/C/Q text (raw lencode
  + STEP comment); all edge pins + head/tail pins
  + for-list R pair pins in for-list + 2 PASS
  lines each py+C. S0/S1 embedded b4/b5 match
  raw lencode (63/60 + 65/60). Ring counter==
  raw-lencode 256/256 + Q 64/64 + A 16/16 + C
  10/10 (counters == lencode whole-tier: A/C/Q
  lencode 92/92 + ring 256/256). Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT on cut
  bytes (edges472.py EDGES-GREEN, A/C NO-ff + Q
  single-ff + ring 2-ff range-with-wrap + Q-range
  wrap+2 + R counter asserts verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 232/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 232 content / 0 del (GATE agrees
  232/0 -- content-line variance 231/232
  recorded: b468/b469 231, b470/b471/b472 232);
  for-line replaced by superset (base for-N
  subset of band, removed 0); fine-norm
  equivalent (for472base.nums subset for472.nums,
  removed 0; C-scope del 0).
- Wall on band diff added lines (scope
  5dcf81a8..44ad8496, 899 added lines): vendor
  0 hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits; 0 `aea` substrings (hex-fragment pattern
  of b470/b471 did NOT resume this band); 0 true
  hits. Files touched: rgramc.c 608/0,
  rgram.py 232/0 purely additive, test_rgram.sh
  1/1 (for-line extension), PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-ind4 750->752
  (+2: 143409/143410) / ranges py-ind4 886->
  890 (+4; py file-wide 760->762 +2 / ranges
  908->912 +4 (+10 early-tier singleton guards /
  +22 early-tier range guards first-hand); C
  dispatch singletons 755->757 +2 / ranges 908->
  912 +4 (C dispatch = ind4 + 5; C unanchored
  760->762 = dispatch + 5 dip-ternary guards,
  all 5 verified non-dispatch early-tier
  `((n)==(N))?...` ternaries first-hand); same 6
  P364 blocks both sides; no elif/else-if added
  either side: py file-wide elif 50 both, C
  else-if 0 both; deltas agree every side),
  CLOSED T10P prints 2072->2078 +6 both sides,
  seal 2166->2172 +6 (commit msgs; offset +94 vs
  CLOSED-T10P stable): all agree, no slip
  (absolute seal inherits lane tally; delta
  verified).
  Viewer-vs-sweep reconcile first-hand:
  GATE-tier absolutes dispatch-exact (ind4 752/
  890) + file-wide-exact (py 760->762, ranges
  908->912; C unanchored 760->762 / 908->912 --
  all EXACT, no tier slip this band); 4sp
  dispatch 750->752 / 886->890 reconciled
  first-hand; file-wide unanchored differs by 10
  non-dispatch early-tier singleton guards + 5-
  count C-vs-py dip-guard offset (dispatch) + 5
  dip-ternaries (unanchored); deltas +2/+4/+6
  every method.
- CONFIRM evidence (CONVERT-01 rule b):
  A-951-q1076-P364 verdict CONFIRM 48/48 CLEAN
  (own bed r5-P364 143409..143784 + r5-P363
  cross-refs, BAD=0 + direct-oracle 2/2
  byte-match; verifier v501.py P364 48/48 PASS;
  file present, counts verified; tier GATED PORT;
  novelty gated: no filed precedent for b52-
  const-entry carried from P363 (here 0xb8 in
  CC); M-tails 16/16 ALL NEW vs P363T col-led
  tails; exact-value corroboration incl PB0
  NEW-sig-1B-off 32/84, PB1 NEW-sig 43/88
  DIFFERS-own-C10 57/88, PBA16-PLAIN sig-e6
  VPOS 8, C10 sig-1f DIFFERS-PB1 VPOS 5 (M4
  b84-87 lane 10/10 diverge; b40 const 0x8a in
  CC this tier), QUAD64 2-sig-COLSPLIT + R4 rows +
  suffix-lcs-3/0/0/0/0/0 + R4-distinct + QM8 +
  NO frags + M-tails NEW, T256-2SIG-ROWSPLIT +
  TM8-by-COL/TR9-by-ROW + SPLIT-tails + const
  66ecbff1 + counter/edges; plus const-count
  note: A-951 excl 79/82/74/70 memo-exact,
  committed tables match excl exactly -- no
  writer lag this tier, geometry exact, PORT
  verdict stands). Agrees with cport commit msg
  (PYID 10829, RGRAM 21658).
- FWD-check first-hand: A-951 + Q-1076 "Next
  P365" forward notes verified against P365 lane
  code (88f78a91 py-merge w2b@6a384310, git show,
  no checkout): PB0 ef0da90f @143757 (pay84 per
  guard, sig-REPEAT vs n143409) + PB1 1f000000
  @143758 (pay88 per guard, NEW-sig 65/88 vs
  P364PB1 per guard, SAME-as-own-C10 per guard)
  + PBA sig f5010000 (guard 143759..143774,
  16 cells) + C10-region 1f000000 x10 (guard
  143775..143784, 10 cells, SAME-as-PB1-sig per
  guard) -- all exact; S0/S1 staged sigs pinned
  (ef0da90f / 1f000000 heads first-hand); banked
  for CONSUME-FIRST with re-corroboration at
  that time per bank-miss lesson (C port for b473
  uncut at file time).
- Quiz: no conflicting CLAIM/GATE/FLAG on b472
  (adjacent odds b471 = 5dcf81a8 C port + b473
  py-merge 88f78a91 live, base-use only, no
  verdict on odds; FLAG files name no b472 band;
  DISSENTs are q846/847/849 unrelated tiers).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r76/
  (build472/, pyid472.log, rgram472py/c.log,
  cmp472.py, seteq472.py, ownloop472.py,
  secf472a/b/c.py, edges472.py (+.log),
  tabaudit472.py (+.log), w472loop.log,
  smoke472.log, units472.log, band472.diff/
  .addedlines, for472.nums/added).

Verdict: PASS. No RED. 348-pin contiguous range
143409..143756 sealed. Round 1/4 toward cap.
