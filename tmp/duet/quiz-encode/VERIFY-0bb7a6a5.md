# VERIFY-0bb7a6a5 b456 T10P348 pins 137841..138188 (348 pins) PASS

Seat viewer-r72, first-hand, tree @0bb7a6a5,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r72.
Base 2bc8d273 (b455 tip, 2070 tiers sealed; this
seat's r71 VERIFY-2bc8d273 PASS-filed, base-use
only, respected). Band = 0c8b1c76 (py merge
w2b@9592dd82 partial, +6 tiers, +58 pins; commit
msg verified via git log) + 0bb7a6a5 (C port;
parent == 0c8b1c76 verified via git log). Trees
via git archive to TMPDIR tree-sha dirs; tests run
from NVME workdirs (no WT src/__pycache__).

Banked Next-P348 shape (r71 handoff §Next-P348:
A-926 Q1 + A-1059 Q1 agree) CONSUMED FIRST and
VERIFIED first-hand EXACT: PB0 ef49ef07 @137841
(S0 head; NEW-sig NEW family 1B-off, 33/84 diff
vs P347PB0) + PB1 0d000000 @137842 (S1 head;
SAME-sig-as-P347PB1, 44/88 diff vs P347PB1;
60/88 vs own C10[0] n137859, DIFFERS-from-own-
C10) + PBA d4000000 x16 @137843-858 (AC b0-3 =
d4/00/00/00) + C10-region 0f000000 x10
@137859-868 (CC b0-3 = 0f/00/00/00,
DIFFERS-from-PB1-sig) -- all corroborated
against lane code both sides before any battery
step (no bank-miss).

- Build: make -C tree/src/c BUILDDIR=$R/build456
  aae rgramc, rc=0, 0 warnings, build456/{aae,
  rgramc}. aae sha256 d6e27c97... (pinned stable
  continues; band touches no aae sources per
  numstat). rgramc sha256 114acabd... == GATE.
- RGRAMC-PYID 10365/10365 covered=10365/10365
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 20730/20730 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  default NVME, NVME workdir).
- RGRAM C 20730/20730 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (20730/20730, sorted +
  raw-identical first-hand; cmp456.py).
- PINS-RGRAM cells set-eq 10365/10365 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq456.py GREEN, 1st full-green run -- no
  adapt miss this band). PINS 20732 lines
  first-hand (2 hdr + 20730 rows; base 20674
  lines / 20672 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10336->10365 +29/-0 (python
  sets, trailing-';' strip, never comm): 137841
  137842 137843 137844 137850 137855 137856
  137858 137859 137860 137863 137864 137867
  137868 137869 137884 137885 137900 137901
  137916 137917 137932 137933 137983 137984
  138050 138111 138112 138188 (== GATE sampled
  list EXACT).
  29 = 2 sing (137841 137842) + A head-pair/mid/
  edge-pair/tail (6: head pair 137843/137844
  off0/1, 137850 off7, edge pair 137855/137856
  off12/13, tail 137858 off15; offs 2-6,9-11,14
  unsampled: 137845-849, 137851-854, 137857) +
  C head/mid/tail pairs (6: 137859/137860 off0/1,
  mid pair 137863/137864 off4/5, tail pair
  137867/137868 off8/9; offs 2,3,6,7 unsampled:
  137861, 137862, 137865, 137866) + Q head/off15/
  off16/pair/pair/tail (8: head 137869 off0,
  137884 off15, 137885 off16, pair 137900/137901
  off31/32, pair 137916/137917 off47/48, tail
  137932 off63; NO edge -- b5 const 35 this tier,
  first-hand) + R head/edge-pair/mid/edge-pair/
  tail (7: head 137933 off0, edge pair 137983/
  137984 off50/51, mid 138050 off117, edge pair
  138111/138112 off178/179, tail 138188 off255;
  both counter edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  20730-20672.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  no oracle).
- Tables audit own script tabaudit456.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 145 PASS 0 FAIL 2nd full-green run
  (1st run caught the seat-script VPOS-PBA adapt
  miss: carried r71 `-1` (const-b5 deduct) wrong
  for this band -- A b5 STEPS 34->35 (varies, in
  VPOS), so NO deduct: missing 9 = VPOS 9 = 2+7;
  fixed, re-greened. Lesson reinforced: re-derive
  deduct-const-b5-or-in-table per band from code,
  never carry).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ef49ef07 NEW-sig 1B-off (33/84
  payload diff vs P347S0 @ b2,4,5,20,21,23,25-30,
  32-34,36-41,64-75 first-hand incl sig b2, NOT
  byte-equal) / S1 176ch sig 0d000000 SAME-sig-
  as-P347PB1 (44/88 payload diff vs P347S1 @ b4,
  5,11,19,26,27,34-59,72-79,84-87 first-hand, sig
  b0 NOT in diff, NOT byte-equal; vs own C10
  cells NOT UNIFORM [60x10] staged+oracle, sig
  DIFFERS 0d-vs-0f with b0 IN diff all 10 cells;
  sig differs vs own PB0),
  staged as full-payload singletons.
  AM 16/16 14ch distinct, CM 10/10 8ch distinct,
  M 16/16 12ch distinct, QR 4/4 8ch distinct
  UNPAIRED (R4 rows r0 742b3d63 / r1 102c3d63 /
  r2 b4b15a77 / r3 d4b15a77 exact tuples; r23
  TRUE 3B b15a77 + rest suffix-lcs 0 (anchored):
  suffix-lcs (01,02,03,12,13,23) = 2/0/0/0/0/3 +
  subseq-lcs 2/0/0/0/0/3 + tshare 2/0/0/0/0/3
  all-3 agree first-hand (== A-935 Q2); r23 full
  tuple unequal; b87 NOT-const {63,77} quad-wide),
  RM 16/16 14ch distinct, RQ 16/16 12ch distinct,
  no QT (R4 b84-87 inside QR) + no RT (SPLIT
  tails, not ROWTAIL) + no F (no frags). M-vs-RQ
  16/16 string-identical SAME-ORDER (M list == RQ
  list; QM6 b13,14,80-83 by COL RM... M 16/16
  12ch col-indexed (m = off&15 both sides) vs RQ
  TR6 b10,11,76-79 by ROW (r = off>>4 both
  sides); string-eq HOLDS this tier -- reported,
  not gated) -- 45th even-band RQ==M instance,
  ORDERED-IDENTICAL (cf b452/b454); ordered per
  lesson (d) (string-identical same-order);
  width predictor dead, never cited. AC 79, CC
  82, QC 76, RC 73; C _N decls 79/82/76/73 match
  actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap gap-free, M/R-tab
  computed). PBA88-PLAIN-M7b6 sig d4000000 (b0
  const d4 via AC b0-3; AM 16/16 distinct NO
  pair; M7 b6,7,8,80-83; A-b5set {34,35} steps
  34x13+35x3 @off13 first-hand).
  C10-1SIG-88-TAIL-M4 sig 0f000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 full-sig
  consts; CM 10/10 diverge 8ch b84-87; CC has no
  b84-87 (all in CM lane) and no b5, b5 const 35
  full block via lencode).
  QUAD88-1SIG-QM6/R4-NOEDGE 1-sig fd000000 x64
  DIFFERS-from-PBA-sig (b0 const fd in QC, b1-3
  const 00; b5 const 35 NO edge full block via
  raw lencode; b4 base 0x1b step2 64/64
  contig+2 range 1b..99 NO wrap, 64 distinct;
  QM6 b13,14,80-83 M 16/16 12ch distinct NO frags
  (m = off&15 both sides) shared-x3-vs-row0
  48/48 oracle (see tabaudit456 shared-x3) NO
  frags + R4 b84-87 rows above 4/4 UNPAIRED
  BY-ROW const (q = off>>4 both sides); tails 4
  distinct (r23 TRUE-3B b15a77 + rest 0); b87
  NOT-const {63,77}; NO frags).
  Ring STANDARD-split: sig 800f0000 x256;
  code-TM7 b12,18,19,80-83 by COL RM 16/16 +
  code-TR6 b10,11,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79 row);
  b0 const 80 (256/256 oracle, in RC table,
  deducted from VPOS per convention); b1 const
  0f (256/256 oracle); b84-87 const 13b25a77
  ring-wide NEW (256/256 oracle).
  VPOS partitions re-derived from code: PBA 9
  (missing 9 - 0: b4,b5 vary + M7, b5 step in
  VPOS no deduct) / C10 5 (missing 6 - 1; b4+M4,
  b5 const deducted) / quad 11 (missing 12 - 1;
  b4+QM6+R4, b5 const deducted) / T 15
  (missing 15 - 0; b4,b5+TM7+TR6, b0 const
  lives in-table, b5 counter-varies in VPOS) --
  all match A-935 (missing sets AC-9
  [4,5,6,7,8,80-83] / CC-6 [4,5,84-87] / QC-12
  [4,5,13,14,80-87] / RC-15
  [4,5,10,11,12,18,19,76-83] first-hand EXACT;
  deduct-const-b5-or-in-table convention holds;
  b5 variance checked from oracle bytes: A
  {34,35} steps, C {35}, Q {35}).
  Code-consts vs A-935 INCL (PBA 79 / C10 83 /
  quad 77 / T88 73): impl 79/82/76/73 =
  writer-1 on C10/quad (impl tables still deduct
  const-b5 while A-935 sheet counts b5; memo
  confirms the sheet INCL values) -- S-F
  arithmetic persists in committed tables though
  the sheets are FIXED; memo-exact on PBA (b5
  step-varies, in VPOS, no deduction) and T88
  (b5 counter-varies, in VPOS, no deduction);
  geometry exact, PORT verdict stands; FLAGGED
  for memo (23rd even band running: .../b454/
  b456; C10/quad lag this tier).
  QUAD 1SIG fd DIFFERS-from-PBA-sig d4 this tier;
  PBA sig d4 NEW vs P347 e8; C10 0f DIFFERS-
  from-PB1-sig 0d.
  M-tails 16/16 ALL NEW vs P347T RM col-led
  tails (overlap 0; P347T RM7 frame first-hand
  from code, ref = RM7 7B rows, position-aware
  tails last-4B) + RQ-tails (b76-79) 16/16 ALL
  NEW vs P347T RQ row-led tails (overlap 0).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P347
  (all 0/16; widths P348 vs P347: AM 7B vs 8B,
  CM 4B vs 4B, M 6B vs 9B, QR 4B vs 4B, RM 7B
  vs 7B, RQ 6B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 137841 / S1 137842 / A 137843-858 /
  C 137859-868 / Q 137869-932 / R 137933-188):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides + R explicit counter
  (b4=(0x9b+2off)&FF b5=0x35+(off>=51)+
  (off>=179); py hex 0x9b/0x35; C staged
  literals 155/53/51/179 re-derived: 155==0x9b,
  53==0x35) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 7B b6-8,80-83; C 8ch lane
  b84-87; Q 6B/4B b13,14,80-83/b84-87; R 7B/6B
  SPLIT TM7 b12,18,19,80-83 by COL / TR6
  b10,11,76-79 by ROW). C blocks carry T92579/
  92584/92589/92604/92619/92639 py-line cites
  (each re-read: hits the exact py guard line, C
  comment text matches py, all 6 present; bounds
  + byte positions exact),
  A/C/Q raw lencode (no counter literals) + R
  counter b4=(0x9b+2off)&FF + (off>=51)+(off>=179)
  (C literals 155/53/51/179 verified), temps
  _t7021-7036 (base max _t7020, no reuse) +
  _i4257/4259/4262/4265 (base max _i4255, no
  reuse) + _b4256/4258/4260/4261/4263/4264 (base
  max _b4254, no reuse; union 4256-4265 with
  i-lane interleaved, contiguous, first-hand),
  all 6 blocks verified.
  Insert position exact both sides: after
  T10P347R close (C comment + S0 block; py
  CLOSED + return + S0 guard 92579), at dispatch
  tail (N-out-of-scope fallthrough follows: py
  92658-59 scope region, C 246321 area; early
  same-text guards unrelated scope).
  Matches A-935 geometry (PB0 NEW-sig 33/84;
  PB1 SAME-sig 44/88 DIFFERS-from-own-C10;
  PBA88-PLAIN-M7b6 VPOS 9 b5 step; C10-1SIG-88-
  TAIL-M4 VPOS 5 DIFFERS-from-PB1-sig b5 const;
  QUAD88-1SIG-QM6/R4-NOEDGE VPOS 11 + R4 4/4
  UNPAIRED exact tuples + r23-3/rest-0 + b0-const-
  DIFFERS-from-PBA + b87-NOT-const + b5-const-NO-
  edge + M-tails NEW; T88-RING-STANDARD-split
  VPOS 15 + TM7-by-COL/TR6-by-ROW + SPLIT-tails +
  b0-const-80 + b84-87 13b25a77 + counter
  9b/35/51/179; lencode 348/348 whole-tier, NO D
  dips) + A-935 (suffix-lcs 2/0/0/0/0/3 = TAIL4
  b84-87 all 3 metrics first-hand; consts excl
  79/82/76/73 = lane EXACT).
- Edges own-loop ownloop456.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P348R N=138188 off=255.
  edges456.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0 embedded b4/b5
  e3/34, S1 e5/34 == raw lencode) + aform 16/16
  (A head e7/34 tail 05/35 b5set {34,35} step
  @off12->13, exactly 1 ff in 16) + cform 10/10
  (C head 07/35 tail 19/35 b5set {35} NO step, 0
  ff) + qform 64/64 (Q head 1b/35 tail 99/35;
  b5 const 35 64/64 NO edge; quad b4=(0x1b+2off)
  64/64 contig+2 range 1b..99 NO wrap, 64
  distinct) + qb5const 64/64 + ring counter
  256/256 + ringraw 256/256 (head 9b/35;
  off50 (137983->137984) ff/35->01/36; off178
  (138111->138112) ff/36->01/37; tail off255
  9d/37 @138188; exactly 3 ff in 348: 1 A-edge
  + 2 ring-edge) + b0 const 80 256/256 + b1
  const 0f 256/256 + b84-87 const 13b25a77
  256/256 (all from oracle bytes first-hand).
  Odd-lencode 348/348 (346 + S0/S1 embedded).
  Ring edges + mid 138050 + tail 138188 in
  for-list + 2 PASS lines each py+C. Tail
  138188: oracle rav sha matches PINS (match
  True; rawlen 104); py+C CLOSED T10P348R
  off=255 agree. No DISSENT: cut bytes verify.
- PB-diff secf456a.py (cache path, 0 miss-warmed
  after ownloop) + secf456b.py
  (DIRECT tool, no cache): staged-vs-oracle
  0/0/0/0 (137841 + 137493 + 137842 + 137494);
  S0: oracle137841-vs-137493 33/84, codeS0-vs-
  P347S0 33/84, positions identical + staged-
  derived EXACT, sig b2 IN diff (NEW-sig 1B-off:
  ef49ef07 vs ef496f07); DIRECT 33/84 agree.
  S1: oracle137842-vs-137494 44/88, codeS1-vs-
  P347S1 44/88, positions identical + staged-
  derived EXACT, sig b0 NOT in diff (SAME-sig
  0d==0d); DIRECT 44/88 agree. Triple-derived
  both pairs (S0 NEW-sig 1B-off + S1 SAME-sig,
  staged novelty both tiers).
  S1-vs-own-C10 secf456c.py (staged assembly vs
  oracle C10 cells n137859-868: 10/10 byte-
  equal; staged S1 vs staged cells): [60x10] in
  all 10 cells (sig 0d vs 0f DIFFERS, b0 IN diff
  all cells), NOT byte-equal. NOT UNIFORM --
  sig-differ (novelty-first: uniformity never
  assumed, GATE-shape-derived; chain TRUE-uniform
  stays 31).
  Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  233/0 (rgram.py) + 1/1 (for-line) + PINS +58/
  +0 (clean append, 29 Ns x2) == GATE; band
  added lines 900 first-hand (== numstat sums
  608+233+1+58); rgramc.c splits 603 content +
  5 bare-blank (exactly `+`, verified 0 ws-only)
  = 608 == numstat; GATE states raw C even-band
  shape correctly (603+5=608, no overcount --
  evens-correct pattern holds). Code GREEN since
  gated artifact == verified artifact.
- Wall on band diff added lines (scope 2bc8d273..
  0bb7a6a5, 900 added lines first-hand): vendor
  0 hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits, aea-invoke 0 hits. Files: rgramc.c
  608/0, rgram.py 233/0 purely additive,
  test_rgram.sh 1/1 (for-line), PINS +58/+0.
  (GATE wall scope 608 = src-only rgramc.c; my
  wall covers the FULL 900 band-diff lines, 0
  hits -- superset.)
- Tiers: merge-msg +6/+58, code 6 blocks, tier-
  comments `# T10P` 1976->1982 +6, dispatch
  singletons 4sp (anchored) 718->720 +2 /
  file-wide unanchored 728->730 +2 = 4sp + 10
  non-dispatch early-tier guards / range-guards
  844->848 +4 = +6, C singletons 4sp 718->720
  +2 / file-wide 723->725 +2 (4sp + 5 dip-guard
  offset, pre-existing) / ranges 844->848 +4 =
  +6, CLOSED T10P prints 1976->1982 +6 both
  sides, seal 2070->2076 +6 (commit msgs; offset
  +94 vs CLOSED-T10P, stable b401-b456). All
  agree (stated literal methods first-hand: py
  elif 50->50, C else-if 0->0; A/C/Q use raw
  lencode, no counters; deltas agree every side:
  +2/+4/+6).
- CONFIRM evidence (CONVERT-01 rule b): A-935-
  q1060-P348 verdict CONFIRM 47/47 CLEAN (own
  bed r5-P348 137841..138216 + r5-P347 cross-
  refs, BAD=0 + direct-oracle 2/2 byte-match;
  verifier v501.py P348 47/47 PASS; file present,
  counts verified; tier GATED PORT; novelty gated
  M-tails 16/16 ALL NEW vs P347T RM col-led
  tails; exact-value corroboration incl PB0 NEW-
  sig 33/84, PB1 SAME-sig 44/88, PBA16 sig-d4
  VPOS 9, C10 sig-0f DIFFSIG VPOS 5, QUAD64
  1-sig-fd DIFFERS-from-PBA + R4 rows +
  suffix-lcs-2/0/0/0/0/3 + b87-notconst + QM6 +
  NO frags + b5 const/step + M-tails NEW,
  T256-STANDARD + TM7-by-COL/TR6-by-ROW +
  SPLIT-tails + b0-80 + const 13b25a77 +
  counter/edges; plus sheet-vs-tables const-count
  note: A-935 sheet excl 79/82/76/73 memo-exact
  (incl +2 b5-const C10/quad), committed tables
  79/82/76/73 still deduct const-b5 on C10/quad --
  S-F arithmetic in tables only, geometry exact,
  PORT verdict stands; w2b-r31 1/8, cited from
  body read first-hand). Agrees with cport
  commit msg (PYID 10365, RGRAM 20730). No
  viewer P348 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b456/
  0bb7a6a5 (quiz poll + filename grep first-
  hand; b455-GATE b457 mentions are base-use
  only; adjacent odds b455/b457 = sweep turf
  incl b457 C port c3383244 live, base-use only,
  no verdict on b456; zero FLAG hits on T10P348;
  CLAIM at brief path is this seat's own r72
  claim). PROSE-01: all hex/counts above copied
  from own run output; GATE-0bb7a6a5 re-read in
  FULL before filing (zero GATE slips this band
  -- even-band raw-C stated correctly, wall scope
  608 src-only noted as subset, temps exact,
  PINS exact).
- RQ==M chain: b456 even ORDERED-IDENTICAL (M
  list == RQ list string-identical same-order,
  16/16) -- 45th even-band RQ==M instance (cf
  b452 43rd + b454 44th). Viewer-vs-sweep
  convention reconciled first-hand (GATE-tier
  absolutes 4sp-dispatch-exact both sides;
  file-wide +10 guards py / +5 C dip offset;
  deltas agree +2/+4/+6 every method).
- TRUE-uniform chain: b456 NOT uniform (S1
  DIFFERS-from-own-C10 sig 0d-vs-0f, [60x10] with
  b0 in diff) -- record stays 31. No new
  SAMESIG-same-sig even case (P338 dispute stays
  DEFERRED to sweep accounting).
- S-F tables-lag: b456 even band sheet!=code
  (impl 79/82/76/73 == A-935 excl; sheet INCL
  79/83/77/73; C10/quad lag, PBA/T exact) --
  41st consecutive tables-lag; even sub-streak
  23rd (GATE-counted; PBA b5-step in VPOS no
  deduct, T b0-in-table + b5-counter in VPOS).
- Next-P349 banked (A-935 Q1 + Q-1060 agree,
  for b457 to CONSUME FIRST): PB0 @138189 sig
  ef49ef07 SAME-as-P348PB0 (32/84 diff) + PB1
  @138190 sig 0f000000 NEW-sig (67/88 vs
  P348PB1) + PBA f4000000 x16 + C10-region
  0f000000 x10 SAME-as-PB1 (FWD-check in GATE-
  0bb7a6a5 corroborated all four vs c3383244
  lane code -- still re-verify at consume time
  per bank-miss lesson).
- Shared-x3 (chain-level): memo phrase "QM
  shared 16/16 x3 vs row0 NO frags" (A-935 Q2)
  verified 48/48 from oracle bytes for P348-QM6
  (lanes 13,14,80-83 col-only indexing + NO
  frags from oracle data, all 6 lanes x3 q-rows
  x16 cells). Memo phrase family holds, NOT a
  slip.

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; zero GATE prose slips this band
(even-band raw-C 603+5 stated exactly; wall
scope 608 = src-only rgramc.c, my wall covers
the FULL 900 band-diff lines with 0 hits).
Viewer scars (1 seat-script, caught pre-file):
tabaudit VPOS-PBA adapt miss (carried r71 `-1`
const-b5 deduct; fixed to no-deduct since A b5
steps 34->35 in VPOS, re-greened 145/145).
