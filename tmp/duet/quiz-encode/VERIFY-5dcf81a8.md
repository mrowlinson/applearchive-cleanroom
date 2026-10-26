# VERIFY-5dcf81a8 b471 T10P363 pins 143061..143408 (348 pins) PASS

Seat viewer-r75, first-hand, tree @5dcf81a8,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r75.
Base 2ded9376 (b470 tip, 2160 tiers sealed; this
seat's VERIFY-2ded9376 PASS-filed same round,
base-use only, respected). Band = 3c030696 (py
merge w2b@027a0ffc partial, +6 tiers, +58 pins;
commit msg verified via git log) + 5dcf81a8 (C
port; parent == 3c030696 verified via git
rev-list --parents). Chain 3c030696 parent ==
2ded9376 verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P363 shape (A-949 + Q-1074 agree,
both read first-hand) CONSUMED FIRST and
VERIFIED first-hand EXACT: PB0 ef0da90e @143061
(S0 head; NEW-sig sigdiff-2 30/84 diff vs
P362PB0 @ n142713, sig b1-2 IN diff with b0/b3
same, positions
[1,2,4-11,13-19,24,56-63,80-83] first-hand, NOT
byte-equal) + PB1 1c000000 @143062 (S1 head;
NEW-sig 50/88 diff vs P362PB1 @ n142714, sig
b0 IN diff with b1-3 same, positions
[0,4,5,9-11,16-43,60-71,84-87] first-hand, NOT
byte-equal; 26/88 vs own C10[0] n143079
(cells 0-9 all-10 identical positions
[4,19,26,27,34-47,72-75,84-87], sig b0-3 same-
sig NOT in diff; TRUE UNIFORM [10x26] 37th
TRUE-uniform case (odd): uniform + SIG-EQ +
differs-PB0; P338 uniform-rule dispute stays
DEFERRED to sweep accounting (numbering
collisions 18th/19th/20th/21st deferred as
before), uniformity verified first-hand; NOT
byte-equal; S1 SIG-EQ own C10; S1 SIG-DIFFERS
own PB0 ef-vs-1c) + PBA88-PLAIN-M6b40 96010000
x16 @143063-078 + C10-region 1c000000 pay88
x10 @143079-088 (SAME-as-PB1-sig, TAIL lane
b40,84-87; b40 2-valued [0xa8,0xa9] 7x+3x
first-hand) -- all corroborated against lane
code both sides before any battery step (no
bank-miss).

- Build: seat-private build471/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 0b6c47fd...
  (prefix == GATE sha256 0b6c47fd, verified
  programmatically, never hand-transcribed).
- RGRAMC-PYID 10800/10800 covered=10800/10800
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21600/21600 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21600/21600 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21600/21600, sorted +
  raw identical; cmp471.py GREEN).
- PINS-RGRAM cells set-eq 21600/21600 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq471.py GREEN). PINS 21602 lines
  first-hand (2 hdr + 21600 rows; base 21544
  lines / 21542 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10771->10800 +29/-0 (python
  sets, trailing-';' strip, never comm): 143061
  143062 143063 143064 143070 143071 143077
  143078 143079 143080 143083 143084 143087
  143088 143089 143103 143104 143105 143120
  143121 143137 143152 143153 143231 143232
  143290 143359 143360 143408 (== GATE sampled
  list EXACT).
  29 = 2 sing (143061 143062 offs 0/1) + A 6
  (head pair 143063/143064 off0/1 + mid pair
  143070/143071 off7/8 + tail pair 143077/
  143078 off14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 5d NO
  edge) + C 6 (head pair 143079/143080 off0/1
  + mid pair 143083/143084 off4/5 + tail pair
  143087/143088 off8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 5d NO edge) + Q 8 (head
  143089 off0 + edge pair 143103/143104 off14/
  15 (ff->01 + b5 STEP 5d->5e) + 143105 off16
  + boundary pair 143120/143121 off31/32 +
  boundary-single 143137 off48 (off47 mate
  unsampled first-hand) + tail 143152 off63;
  b5 B5EDGE off14->15, pair-covered except off47
  mate) + R 7 (head 143153 off0 + edge pair
  143231/143232 off78/79 + mid pin 143290 off137
  + edge pair 143359/143360 off206/207 + tail
  143408 off255; 1-mid shape off137 NEW, both
  counter edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21600-21542.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit471.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 192 PASS 0 FAIL second-run (1 seat-
  script deduct fix: P363 quad b5 STEPS (varies,
  in missing) -- NO deduct, viewer VPOS 11 =
  missing 11, same class as P360 quad, carried
  deduct-re-derivation lesson; NO GATE prose
  slip this band: VPOS 7/6/11/19 == code+Q-1075
  viewer-convention EXACT; QC b1-3 is 01/00/00
  first-hand both sides -- slip class clear 4
  bands running).
  Inventory exactly the 12 tables both sides
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no M42/X42/
  H42/L42, no QB/PT/FM, no RT/TT (ring, not
  ROWTAIL), no QT (R2 carries b84,85 in-row +
  b86/b87 consts); no _T10P363C numeric-head
  probe -- precedent since band29, only band29-
  range cover it).
  S0 168ch sig ef0da90e NEW-sig sigdiff-2
  (30/84 payload diff vs P362S0, positions
  [1,2,4-11,13-19,24,56-63,80-83] first-hand,
  sig b1-2 IN diff with b0/b3 same, NOT byte-
  equal) / S1 176ch sig 1c000000 NEW-sig (50/88
  payload diff vs P362S1, positions
  [0,4,5,9-11,16-43,60-71,84-87] first-hand,
  sig b0 IN diff with b1-3 same, NOT byte-
  equal; vs own C10 cells TRUE UNIFORM [10x26]
  staged+oracle: all-10 identical positions
  [4,19,26,27,34-47,72-75,84-87], sig b0-3
  same-sig NOT in diff; NOT byte-equal; S1 SIG-
  EQ own C10; S1 SIG-DIFFERS own PB0; S1[40]=
  0x4c vs CM b40 2-valued [0xa8,0xa9] 7x+3x
  first-hand), staged as full-payload
  singletons.
  AM 16/16 12ch distinct, CM 10/10 10ch diverge
  (b40 2-valued [0xa8,0xa9] 7x+3x first-hand),
  M 16/16 14ch distinct, QR 4/4 4ch R2 rows
  4131/6131/0732/2732 exact tuples (full tails
  = R2 + b86 bc / b87 37 quad-wide exact;
  trailing-suffix = subseq = TSHARE =
  3/2/2/2/2/3 (all-3 agree first-hand; pairs
  (0,1)/(2,3) trailing 3 rest 2; full tuples
  pairwise unequal, 4 distinct)), RM 16/16 16ch
  distinct, RQ 16/16 18ch distinct, no QT + no
  RT + no F (no frags).
  M-vs-RQ 0OF7 fully-disjoint (M 7B lanes
  [30,39,47,80-83] vs RQ 9B lanes [40,41,42,
  46,47,76-79]: rows 0/16, per-col first-7 all
  0/16, col-set overlaps [0,0,0,0,0,3,0]
  (only c5 shares 3), full-row sets DISJOINT;
  AM-vs-RQ 6B-prefix crosscheck rows 0/16 +
  per-col 0/16 + overlaps [0,0,0,0,1,1] agrees)
  -- 53rd odd-band RQ==M instance, 2nd fully-
  disjoint degree (after b465 0OF8 FIRST-
  disjoint; 0OF-precedent multiple on file;
  disjoint by full-row criterion, low lanes
  differ, tails differ); viewer chain: odds
  52->53; 22nd full/diff survey (survey counts
  every method RQ-vs-M regardless of degree).
  M-tails 16/16 ALL NEW vs P362T RM col-led
  tails (overlap 0; P362T RM 16x9B frame
  first-hand from code, tails last-4B); RQ-tails
  16/16 ALL NEW vs P362T TR7 (overlap 0) +
  16/16 ALL NEW vs P362T RM (overlap 0); RM-
  tails 16/16 ALL NEW vs P362T RM (overlap 0) +
  16/16 ALL NEW vs P362T TR7 (overlap 0);
  AM/CM/M/QR/RM/RQ 0-overlap vs P362 all six
  (widths P363 vs P362: AM 6B vs 6B, CM 5B vs
  4B, M 7B vs 7B, QR 2B vs 3B, RM 8B vs 9B, RQ
  9B vs 7B).
  AC 80, CC 81, QC 77, RC 69; C _N decls
  80/81/77/69 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 const 96 in
  AC (b1 const 01, b2-3 const 00; b5 const 5d
  deducted, in AC-missing; b84-87 consts
  fc,85,b6,29 A-lane); C b0 const 1c in CC
  (b1-3 const 00; b5 const 5d deducted, in
  CC-missing; b52 const 0xb9 const-entry, b40
  2-valued locus in CC-missing; no filed
  precedent for b52-const-entry, recorded); C
  b84-87 absent (M5/TAIL lane); Q b0 const 96
  1-sig in QC first-hand (b1 const 01, b2-3
  const 00; b5 STEPS in VPOS, NO deduct; b84/85
  absent R2-lane, b86 const bc / b87 const 37);
  R b0 const 96 + b1 const 1d in RC table,
  code-indexed first-hand).
  PBA88-PLAIN-M6b40 sig 96010000 x16 (b0 const
  96 via AC b0; b5 const 5d deducted NOT in AC;
  AM 16/16 distinct NO pair; M6 b40,41,80-83
  positions FIRST this lane) + PBA sig 96 NEW
  vs P362 db.
  C10-1SIG-88-TAIL-M5b40 sig 1c000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  1c000000; CM 10/10 diverge 10ch b40,84-87;
  CC has no b40,84-87 EXCEPT b52 0xb9
  const-entry (ALL in CM lane + b52 entry); b5
  const 5d deducted NOT in CC).
  QUAD88-1SIG-QM7/R2-B5EDGE 1-sig 96010000 x64
  SAME-sig-as-PBA (b0 const 96 in QC; b5 STEP
  0x5d+(off>=15) in VPOS edge 143103->143104;
  b4 base 0xe3 step2 64/64 range e3..61 wrap+2,
  exactly 1 ff in 64 (off14); QM7 b30,39,47,
  80-83 M 16/16 14ch distinct NO frags (m =
  off&15 first-hand; QM7 FIRST this lane per
  A-950, lane-set differs, shape filed, no
  FIRST claimed) + R2 b84,85 rows 4131/6131/
  0732/2732 4/4 UNPAIRED BY-ROW const (q =
  off>>4 first-hand); tails = R2 + bc/37
  quad-wide, full-tail trailing/subseq/TSHARE
  all-3 3/2/2/2/2/3 + R2-tuple-unequal).
  Ring T88-STANDARD-split-TM8/TR9 sig 961d0000
  x256 (b0 const 96 256/256 oracle, in RC
  table; b1 const 1d 256/256 oracle, in RC
  table; code-TM8 b52,53,54,55,80-83 by COL RM
  16/16 (staged P267R) + code-TR9 b40,41,42,
  46,47,76-79 by ROW RQ 16/16 UNPAIRED (SPLIT
  tails b80-83 col / b76-79 row; positions
  FIRST this lane); b84-87 const 4732bc37
  ring-wide NEW; b4=(99+2off)&FF + (94)+
  (off>=79)+(off>=207) (C literals 99/94/79/
  207 verified == 0x63/0x5e/79/207; py hex
  0x63/0x5e)).
  VPOS partitions re-derived from code: PBA 7
  (missing 8 - 1; b4+M6 b40,41,80-83, b5 const
  deducted) / C10 6 (missing 7 - 1; b4+M5
  b40,84-87, b5 const deducted) / quad 11
  (missing 11 - 0; b4,b5+QM7 7+R2 2, b5 STEPS
  in VPOS, NO deduct) / T 19 (missing 19 - 0;
  b4,b5+TM8 8+TR9 9, counter varies, NO deduct)
  -- all match Q-1075 (7/6/11/19); GATE-5dcf81a8
  headlines 7/6/11/19 EXACT (viewer convention,
  no slip this band).
  Code-consts vs A-950 INCL/EXCL (PBA 80 / C10
  81 / quad 77 / T88 69 excl): impl 80/81/77/
  69 = memo-excl EXACT -- no lag on odd band
  (deduct-only-when-vary holds; A-950 INCL
  +2/+2/+2/+0 = 82/83/79/69 for the two b5-
  const regions A/C; memo-side, differs from
  P362 sheet -- recorded, no code impact). VPOS
  7/6/11/19 = memo EXACT.
  S-F lag stays 44; even sub-streak stays 26.
  M-tails 16/16 ALL NEW vs P362T col-led tails
  (overlap 0); RQ-tails 16/16 ALL NEW vs P362T
  TR7 (overlap 0) + vs P362T RM (overlap 0);
  RM-tails 16/16 ALL NEW vs P362T RM (overlap
  0) + vs P362T TR7 (overlap 0); AM/CM/M/QR/RM/
  RQ 0-overlap vs P362 all six.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 143061 / S1 143062 / A 143063-078 /
  C 143079-088 / Q 143089-152 / R 143153-408):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q/C both sides (A b5 const
  emerges from raw lencode; C b5 const emerges
  from raw lencode; Q b5 step emerges from raw
  lencode + b5 formula comment) + R explicit
  counter (b4=(0x63+2off)&FF b5=0x5e+(off>=79)+
  (off>=207); py hex 0x63/0x5e; C staged
  decimal literals 99/94/79/207 re-derived:
  99==0x63, 94==0x5e) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact
  (A 12ch b40,41,80-83 M6; C 10ch lane b40,84-
  87 M5; Q 14ch/4ch QM7 b30,39,47,80-83/R2
  b84,85; R 16ch/18ch STANDARD TM8 b52-55,
  80-83 by COL / TR9 b40-42,46,47,76-79 by
  ROW).
  C blocks carry T96056/T96061/T96066/T96081/
  T96096/T96116 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present + S0 guard 96056 verified
  in py; bounds + byte positions exact: A 12ch,
  C 10ch, Q 14ch/4ch, R 16ch/18ch),
  A/C/Q raw lencode (no counter literals; C b5
  const deducted NOT in CC; Q b5 STEP 0x5d+
  (off>=15) in VPOS) + R counter b4=(99+2off)&
  FF + (94)+(off>=79)+(off>=207) (C literals
  99/94/79/207 verified), temps _t7261-7276
  (base max _t7260, no reuse) + _i4407/4409/
  4412/4415 (base max _i4405, no reuse) +
  _b4406/4408/4410/4411/4413/4414 (base max
  _b4404, no reuse), union 4406-4415
  contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P362R close (C "T10P3630 singleton" after
  "CLOSED T10P362R"; py return 0 + S0 guard
  96056 after "CLOSED T10P362R" print), at
  dispatch tail (P363R immediately precedes LAST
  N-out-of-scope hit; 2 scope-hits each side:
  C T34797/T4-plateau-B inner + dispatch tail;
  py dip-1077/T4-plateau-B inner line 59636 +
  dispatch tail 96135; unrelated scope).
  Matches A-950 geometry (PB0 NEW-sig sigdiff-2
  30/84; PB1 NEW-sig 50/88; SAME-as-own-C10
  26/88; differs-vs-own-PB0; PBA88-PLAIN-M6b40
  VPOS 7 sig-96 b5 const M6 16/16 distinct;
  C10-1SIG-88-TAIL-M5b40 VPOS 6 SAME-as-PB1-sig
  b5 const b40-2-valued M5 10/10 diverge;
  QUAD88-1SIG-QM7/R2-B5EDGE VPOS 11 + R2 4/4
  UNPAIRED 4131/6131/0732/2732 + trailing
  3/2/2/2/2/3 all-3 agree + tuples-unequal +
  QM7 + NO frags + M-tails NEW; T88-STANDARD-
  split VPOS 19 + TM8-by-COL/TR9-by-ROW +
  SPLIT-tails + b84-87 4732bc37 + counter
  63/5e/79/207; lencode 348/348 whole-tier, NO
  D dips) incl exact values (PBA/C10/QUAD/T88
  sigs, R2 rows + tails + LCS +
  STANDARD-split frame + consts stand; const-
  count note is impl==excl this tier per memo,
  geometry exact, PORT verdict stands; M-vs-RQ
  0OF7 fully-disjoint first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head
  af/5d tail cd/5d b5set {5d} NO step, 0 ff
  (b4 base 0xaf step2 16/16, b0 const 96 16/16);
  C head cf/5d tail e1/5d b5set {5d} NO step,
  0 ff (b0 const 1c 10/10); Q head e3/5d pre-
  edge off14 (ff/5d) edge off15 (01/5e) 143105
  03/5e off48 43/5e tail 61/5e b5set {5d,5e}
  STEP (b4 base 0xe3 step2 64/64 range e3..61
  wrap+2, exactly 1 ff in 64); ring pre-edge
  off78 (ff/5e), edge off79 (01/5f); edge
  off206 (ff/5f) -> off207 (01/60); exactly 2
  ff in 256; R head 63/5e tail 61/60; mid off137
  @143290 (75/5f); formulas re-derived from
  T10P363R code text (63/5e/79/207 hex==dec) +
  T10P363A/C/Q text (raw lencode + STEP
  comment); all edge pins + mid pin 143290 +
  tail 143408 in for-list + 2 PASS lines each
  py+C. S0/S1 embedded b4/b5 match raw lencode
  (ab/5d + ad/5d). Ring counter==raw-lencode
  256/256 + Q 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No
  DISSENT on cut bytes (edges471.py EDGES-
  GREEN, A/C NO-ff + Q single-ff + ring 2-ff
  range-with-wrap + Q-range wrap+2 + R counter
  asserts verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 232/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; raw py 232 content / 0 del (GATE agrees
  232/0 -- no slip); for-line replaced by
  superset (base for-N subset of band, removed
  0); fine-norm equivalent (for470base.nums
  subset for471.nums, removed 0; C-scope del 0).
- Wall on band diff added lines (scope
  2ded9376..5dcf81a8, 899 added lines): vendor
  0 hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits; 1 `aea` hex-fragment (PINS sha
  ...79aea034... line g-z143088, verified
  non-invocation); 0 true hits. Files touched:
  rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line
  extension), PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-ind4 748->750
  (+2: 143061/143062) / ranges py-ind4 882->
  886 (+4; py file-wide 758->760 +2 / ranges
  900->908 +4; C singletons 753->755 +2 /
  ranges 904->908 +4, same 6 P363 blocks both
  sides; no elif/else-if added either side: py
  file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2066->2072 +6 both sides, seal 2160->2166 +6
  (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
  Viewer-vs-sweep reconcile first-hand:
  GATE-tier absolutes file-wide-exact (py 758->
  760, ranges 900->908 -- all EXACT, no slip
  this band); 4sp dispatch 748->750 / 882->886
  reconciled first-hand; file-wide unanchored
  differs by 10 non-dispatch early-tier guards +
  5-count C-vs-py dip-guard offset; deltas
  +2/+4/+6 every method.
- CONFIRM evidence (CONVERT-01 rule b):
  A-950-q1075-P363 verdict CONFIRM 50/50 CLEAN
  (own bed r5-P363 143061..143436 + r5-P362
  cross-refs, BAD=0; verifier v501.py P363
  50/50 PASS; file present, counts verified;
  tier GATED PORT; novelty gated: no filed
  precedent for b52-const-entry (in CC), M-tails
  16/16 ALL NEW vs P362T col-led tails; exact-
  value corroboration incl PB0 NEW-sig sigdiff-2
  30/84, PB1 NEW-sig 50/88, PBA16 sig-96 VPOS 7,
  C10 sig-1c SAME-PB1 VPOS 6 b40-2-valued, QUAD64
  1-sig-B5EDGE + R2 rows + suffix-lcs-3/2/2/2/2/
  3 + R2-distinct + QM7 + NO frags + M-tails
  NEW, T256-STANDARD + TM8-by-COL/TR9-by-ROW +
  SPLIT-tails + const 4732bc37 + counter/edges;
  plus const-count note: A-950 excl 80/81/77/69
  memo-exact, committed tables match excl
  exactly -- no writer lag this tier, geometry
  exact, PORT verdict stands). Agrees with cport
  commit msg (PYID 10800, RGRAM 21600).
- FWD-check: banked Next-P364 from A-949+Q-1074
  agreement (both read first-hand)
  pre-corroborated EXACT vs b472 py-merge
  fbf28aed (on file, git show, no checkout):
  PB0 ef0da90f 168ch pay84 @143409 (NEW-sig
  1B-off 32/84 vs P363PB0) + PB1 1e000000 176ch
  pay88 @143410 (NEW-sig 43/88 vs P363PB1) +
  PBA88 sig e6010000 guard 143411..143426 (16
  cells) + C10-region 1f000000 x10 guard
  143427..143436 (10 cells, DIFFERS-from-PB1-
  sig) -- banked for r76 CONSUME-FIRST and re-
  corroborate EXACT at that time per bank-miss
  lesson (fbf28aed on file; corroboration
  mandatory; C port for b472 uncut at r75
  exit).
- Quiz: no conflicting CLAIM/GATE/FLAG on b471
  (adjacent odds b469/b473-live + evens incl
  b470 tip live base-use only, no verdict on
  b471).
  PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-viewer/r75/
  (build471/, pyid471.log, rgram471py/c.log,
  cmp471.py, seteq471.py, ownloop471.py,
  secf471a/b/c.py, edges471.py, tabaudit471.py,
  w471loop.log, smoke471.log, units471.log,
  band diff via git).

Verdict: PASS. No RED. 348-pin contiguous range
143061..143408 sealed. Round 4/4 = cap reached.
