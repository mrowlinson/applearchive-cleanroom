# VERIFY-f433ef98 b467 T10P359 pins 141669..142016 (348 pins) PASS

Seat viewer-r74, first-hand, tree @f433ef98,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r74.
Base 5f800ba0 (b466 tip, 2136 tiers sealed; this
seat's VERIFY-5f800ba0 PASS-filed same round,
base-use only, respected). Band = 6e01480c (py
merge w2b@46e06388 partial, +6 tiers, +58 pins;
commit msg verified via git log) + f433ef98 (C
port; parent == 6e01480c verified via git
rev-list --parents). Chain 6e01480c parent ==
5f800ba0 verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P359 shape (VERIFY-5f800ba0 "Next
P359" FWD, CONSUMED at that filing and
re-corroborated here pre-battery) CONSUMED
FIRST and VERIFIED first-hand EXACT: PB0
ada6a40c @141669 (S0 head; NEW-sig sigdiff-2
32/84 diff vs P358PB0 @ n141321, b2-3 IN diff
with b0-1 same, positions
[2-5,22,23,30-34,36-43,48,49,52-55,68-73,75]
first-hand, NOT byte-equal) + PB1 19000000
@141670 (S1 head; NEW-sig 66/88 diff vs P358PB1
@ n141322, sig b0 IN diff, positions
[0,4-15,19-59,76-87] first-hand, NOT
byte-equal; 78/88 vs own C10[0] n141687 (cells
0-8), 79/88 vs cell 9 n141696, SIG-EQ-own-C10;
DIFFERS-vs-own-PB0 ad-vs-19) + PBA 2SIG-M7b0
d4010000 x4 (off<4) + d5010000 x12 ORDERED
@141671-686 (FIRST this lane; A-mtab
b0,10,11,80-83) + C10-region 19000000 pay88
x10 @141687-696 (SAME-as-PB1-sig; M6b8 lane
b8,9,84-87 all in CM, FIRST this lane; CM rows
b8,9,84-87 diverge 12ch) -- all corroborated
against lane code both sides before any battery
step (no bank-miss).

- Build: seat-private build467/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 69d77005...
  (prefix == GATE 69d77005; GATE states sha1
  prefix this band; compared programmatically,
  never hand-transcribed).
- RGRAMC-PYID 10684/10684 covered=10684/10684
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21368/21368 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21368/21368 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21368/21368, sorted +
  raw identical; cmp467.py GREEN).
- PINS-RGRAM cells set-eq 10684/10684 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq467.py GREEN). PINS 21370 lines
  first-hand (2 hdr + 21368 rows; base 21312
  lines / 21310 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10655->10684 +29/-0 (python
  sets, trailing-';' strip, never comm): 141669
  141670 141671 141672 141674 141675 141676
  141686 141687 141688 141691 141692 141695
  141696 141697 141712 141713 141728 141729
  141744 141745 141760 141761 141823 141824
  141890 141951 141952 142016 (== GATE sampled
  list EXACT).
  29 = 2 sing (141669 141670) + A 6 (head pair
  141671/141672 off0/1 + off2-is-141674 (NO
  141673: 2-sig boundary pair 141674/141675
  off3/4, boundary pair-covered, first-hand) +
  141676 off5 + tail 141686 off15; offs
  0,1,3,4,5,15; b5 const 52 NO step) + C 6
  (head 141687/141688 off0/1 + mid pair 141691/
  141692 off4/5 + edge pair 141695/141696 off8/9
  B5EDGE pair-covered; b5 STEPS 52->53) + Q 8
  (head 141697 + pairs 141712/141713 off15/16 +
  141728/141729 off31/32 + 141744/141745 off47/
  48 + tail 141760 off63; NO mid (all
  boundaries pair-covered, first-hand)) + R 7
  (head 141761 + edge pair 141823/141824 off62/
  63 + mid 141890 off129 + edge pair 141951/
  141952 off190/191 + tail 142016 off255; 1-mid
  shape off129 NEW, both counter edges pair-
  covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21368-21310.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit467.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 162 PASS 0 FAIL first-run (0
  seat-script fixes; 1 GATE prose note in the
  b465 class: QC b1-3 is 01/00/00 first-hand
  both sides -- GATE prose "b1-3 const 00"
  loose; sig 9f010000 exact, code GREEN;
  recorded + still PASS).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ada6a40c NEW-sig sigdiff-2
  (32/84 payload diff vs P358S0, positions
  [2-5,22,23,30-34,36-43,48,49,52-55,68-73,75]
  first-hand, b2-3 IN diff with b0-1 same, NOT
  byte-equal) / S1 176ch sig 19000000 NEW-sig
  (66/88 payload diff vs P358S1, positions
  [0,4-15,19-59,76-87] first-hand, sig b0 IN
  diff, NOT byte-equal; vs own C10 cells
  NOT-UNIFORM [9x78+1x79] staged+oracle: cells
  0-8 identical positions
  [4,6-55,60-71,73-87], cell 9 adds [5]
  (B5EDGE step in last cell), sig b0-3 same-sig
  NOT in diff; NOT byte-equal; S1 SIG-EQ own
  C10; S1 SIG-DIFFERS own PB0), staged as
  full-payload singletons.
  AM 16/16 14ch distinct, CM 10/10 12ch diverge
  M6b8 (b8,9,84-87 all in CM lane, FIRST this
  lane), M 16/16 14ch distinct, QR 4/4 8ch
  distinct UNPAIRED (R4 rows r0 22d47814 / r1
  42d47814 / r2 62d47814 / r3 77496d43 exact
  tuples; tails = R4 rows exact, NO b86/b87
  consts (R4 carries b84-87); trailing-suffix =
  subseq = TSHARE = 3/3/0/3/0/0 (all-3 agree
  first-hand); tails 4 distinct), RM 16/16 16ch
  distinct, RQ 16/16 14ch distinct, no QT (R4
  b84-87 inside QR, no consts) + no RT
  (SWAPPED tails) + no F (no frags).
  M-vs-RQ FULL7 (M 7B lanes [20,21,22,80-83]
  vs RQ 7B lanes [20,21,22,80-83]: rows 16/16
  EQUAL, per-col first-7 all 16/16, col uniqs
  [16,3,2,16,13,15,16] both sides EQUAL, full-
  row sets EQUAL, sorted rows EQUAL, M list ==
  RQ list) -- 51st odd-band RQ==M instance, 9th
  FULL degree (no precedent on file; viewer
  chain: odds 50->51; 18th full-identity
  survey); ordered per lesson (d) (rows EQUAL
  + sets EQUAL + sorted EQUAL, same order;
  QM7/R4-NOEDGE vs RM8/RQ7-SWAPPED tails
  differ, tables equal); width predictor dead,
  never cited; Deduct never cross-cited in UNIQ
  (FULL assertion uses only within-band
  position-exact + set facts); M-tails 16/16
  ALL NEW vs P358T RQ row-led tails (overlap 0;
  P358T RQ 16x7B frame first-hand from code,
  tails last-4B); RQ-tails (b80-83) 16/16 ALL
  NEW vs P358T RM col-led tails (overlap 0;
  P358T RM 16x8B frame first-hand from code,
  tails last-4B); RM-tails 16/16 ALL NEW vs
  P358T RQ row-led tails (overlap 0) + 16/16
  ALL NEW vs P358T RM col-led tails (overlap
  0); AM/CM/M/QR/RM/RQ full-row 0-overlap vs
  P358 (all 0/16; widths P359 vs P358: AM 7B
  vs 7B, CM 6B vs 4B, M 7B vs 7B, QR 4B vs 1B,
  RM 8B vs 8B, RQ 7B vs 7B).
  AC 79, CC 80, QC 75, RC 71; C _N decls
  79/80/75/71 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; A b0 VARIES 2-sig
  d4/d5 ORDERED off<4 in VPOS (b1 const 01,
  b2-3 const 00; b84-87 consts ff/f9/ac/dd in
  AC); Q b0 const 9f 1-sig in QC first-hand
  (b1 const 01, b2-3 const 00); R4 carries
  b84-87 with NO b86/b87 consts first-hand).
  PBA88-2SIG-M7b0 (d4010000 x4 off<4 +
  d5010000 x12 ORDERED, FIRST this lane; b0
  VARIES in VPOS via AM lane b0,10,11,80-83;
  AM 16/16 distinct NO pair; b5 const 52 NO
  step NO edge -- b5 const deducted, in
  AC-missing).
  C10-1SIG-88-M6b8-B5EDGE sig 19000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  19000000; CM 10/10 diverge 12ch b8,9,84-87;
  CC has no b8,9,84-87 (all in CM lane); b5 =
  0x52+(off>=9) in VPOS, edge off8->9 B5EDGE
  pair-covered 141695->141696).
  QUAD88-1SIG-QM7/R4-NOEDGE 1-sig 9f010000 x64
  (b0 const 9f in QC; b5 const 53 deducted to
  raw lencode NO edge; b4 base 0x03 step2 64/64
  range 03..81, NO wrap; QM7 b20,21,22,80-83
  M 16/16 14ch distinct NO frags (m = off&15
  first-hand) + R4 b84,85,86,87 rows 4/4
  UNPAIRED BY-ROW const (q = off>>4
  first-hand); tails = R4 rows exact quad-wide,
  full-tail trailing 3/3/0/3/0/0 + subseq same
  + TSHARE same + R4 all-distinct).
  Ring T88-SWAPPED-RM8/RQ7 sig f4190000 x256
  (b0 const f4 256/256 oracle, in RC table; b1
  const 19 256/256 oracle, in RC table; code-
  RM8 b28,29,30,31,76-79 by COL RM 16/16 +
  code-RQ7 b20,21,22,80-83 by ROW RQ 16/16
  UNPAIRED (SWAPPED tails b80-83 row / b76-79
  col); b84-87 const 97496d43 ring-wide NEW;
  b4=(131+2off)&FF + (off>=63)+(off>=191) (C
  literals 131/83/63/191 verified == 0x83/0x53/
  63/191; py hex 0x83/0x53)).
  VPOS partitions re-derived from code: PBA 8
  (missing 9 - 1; b0,b4+M6 b10,11,80-83, b5
  const deducted) / C10 8 (missing 8 - 0;
  b4,b5+M6 b8,9,84-87, b5 STEPS B5EDGE in VPOS,
  NO deduct) / quad 12 (missing 13 - 1; b4+QM7
  7+R4 4, b5 const deducted NOEDGE) / T 17
  (missing 17 - 0; b4,b5+RM8+RQ7, b0/b1 consts
  live in-table) -- all match A-946 (missing
  sets AC-9 [0,4,5,10,11,80-83] / CC-8
  [4,5,8,9,84-87] / QC-13 [4,5,20-22,80-87] /
  RC-17 [4,5,20-22,28-31,76-83] first-hand
  EXACT; deduct-const-b5-or-in-table convention
  holds incl the 2SIG/M6b8/B5EDGE shapes; b5
  variance checked from oracle bytes: A {52}
  const, C {52,53} steps, Q {53} const, T
  counter-varies).
  Code-consts vs A-946 INCL/EXCL (PBA 79 / C10
  80 / quad 75 / T88 71 excl): impl 79/80/75/
  71 = memo-excl EXACT -- no lag on odd band
  (deduct-only-when-vary holds; A-946 INCL
  +1/+0/+1 for the two b5-const lanes =
  80/80/76/71). VPOS 8/8/12/17 = memo EXACT.
  S-F lag stays 44; even sub-streak stays 26.
  M-tails 16/16 ALL NEW vs P358T row-led tails
  (overlap 0); RQ-tails 16/16 ALL NEW vs P358T
  RM col-led tails (overlap 0); RM-tails 16/16
  ALL NEW vs both P358T tails (overlap 0);
  AM/CM/M/QR/RM/RQ 0-overlap vs P358 all six.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 141669 / S1 141670 / A 141671-686 /
  C 141687-696 / Q 141697-760 / R 141761-142016):
  bounds + paylens (1x84 + 347x88) +
  lencode l16 A/Q both sides (A b5 const
  emerges from raw lencode; C b5 step emerges
  from raw lencode + b4 formula; Q b5 const
  emerges from raw lencode) + R explicit
  counter (b4=(131+2off)&FF b5=83+(off>=63)+
  (off>=191); py hex 0x83/0x53; C staged
  decimal literals 131/83/63/191 re-derived:
  131==0x83, 83==0x53) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/rtab
  byte positions exact (A 14ch b0,10,11,80-83
  2-sig; C 12ch lane b8,9,84-87 + no consts; Q
  14ch/8ch b20,21,22,80-83/b84-87; R 16ch/14ch
  SWAPPED RM8 b28-31,76-79 by COL / RQ7
  b20-22,80-83 by ROW).
  C blocks carry T95135/T95140/T95155/T95170/
  T95190 py-line cites (each re-read: hits the
  exact py guard line, C comment text matches
  py, all 5 present + S0 guard 95130 verified
  in py; bounds + byte positions exact: A 14ch
  2-sig, C 12ch, Q 14ch/8ch, R 16ch/14ch),
  A/C raw lencode (no counter literals; C b5
  step in VPOS) + Q raw lencode + R counter
  b4=(131+2off)&FF + (off>=63)+(off>=191) (C
  literals 131/83/63/191 verified), temps
  _t7197-7212 (base max _t7196, no reuse) +
  _i4367/4369/4372/4375 (base max _i4365, no
  reuse) + _b4366/4368/4370/4371/4373/4374
  (base max _b4364, no reuse), union
  4366-4375 contiguous, all 6 blocks verified.
  Insert position exact both sides: after
  T10P358R close (C "T10P3590 singleton" after
  "CLOSED T10P358R"; py return 0 + S0 guard
  95130), at dispatch tail (N-out-of-scope
  fallthrough follows; plateau guards at C
  170850 / py 59209 are the T4 plateau,
  unrelated scope).
  Matches A-946 geometry (PB0 NEW-sig sigdiff-2
  32/84; PB1 NEW-sig 66/88; PBA88-2SIG-M7b0
  VPOS 8 b5 const M7 16/16 distinct FIRST;
  C10-1SIG-88-M6b8-B5EDGE VPOS 8 SAME-as-PB1-
  sig b5 STEPS M6 10/10 diverge FIRST;
  QUAD88-1SIG-QM7/R4-NOEDGE VPOS 12 + R4 4/4
  UNPAIRED 22d47814/42d47814/62d47814/77496d43
  + trailing 3/3/0/3/0/0 + subseq same + R4-
  distinct + QM7 + NO frags + M-tails NEW;
  T88-SWAPPED-RM8/RQ7 VPOS 17 + RM8-by-COL/
  RQ7-by-ROW UNPAIRED 16/16 + SWAPPED-tails +
  b84-87 97496d43 + counter 131/83/63/191;
  lencode 348/348 whole-tier, NO D dips) incl
  exact values; M-vs-RQ FULL7 first-hand this
  tier, tier stands.
- Edges via counter formula first-hand: A head
  cf/52 (d4) off3 d5/52 (sig d4) -> off4 d7/52
  (sig d5) tail ed/52 b5set {52} NO step, 0 ff
  (b4 base 0xcf step2 16/16; b0 2-sig d4 iff
  off<4 ORDERED, boundary pair-covered
  141674+141675); C head ef/52 pre-edge off8
  (ff/52), edge off9 (01/53) B5EDGE pair-
  covered 141695->141696, tail 141696 (01/53);
  b5set {52,53}; Q head 03/53 tail 81/53 b5set
  {53} NO edge, 0 ff (b4 base 0x03 step2 64/64
  range 03..81, NO wrap); ring pre-edge off62
  (ff/53), edge off63 (01/54); edge off190
  (ff/54) -> off191 (01/55); exactly 2 ff in
  256; R head 83/53 (141761) mid off129 85/54
  (141890) tail off255 81/55 (142016); formulas
  re-derived from T10P359R
  code text (83/53/63/191 hex==dec) +
  T10P359A/C/Q text (raw lencode); all edge
  pins + mid pin 141890 + tail 142016 in
  for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 match raw lencode. Ring
  counter==raw-lencode 256/256 + Q 64/64 + A
  16/16 + C 10/10. Odd-lencode 348/348
  (16+10+64+256+2). No DISSENT on cut bytes
  (edges467.py EDGES-GREEN, C-B5EDGE edge + Q-
  range NO-wrap + range-with-wrap asserts
  verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 232/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; for-line replaced by superset (base
  for-N subset of band, removed 0); fine-norm
  equivalent (for466base.nums subset
  for467.nums, removed 0; C-scope del 0).
- Wall on band diff added lines (scope
  5f800ba0..f433ef98, 899 added lines): vendor
  0 hits, disasm 0 hits, depload 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits; 0 `aea` substrings (cleanest band of
  the round -- no hex-fragment hits at all).
  Files touched: rgramc.c 608/0, rgram.py
  232/0 purely additive, test_rgram.sh 1/1
  (for-line extension), PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-file-wide 750->
  752 (+2: 141669/141670) / ranges py-file-wide
  888->892 (+4; 4sp dispatch 740->742 +2 /
  4sp ranges 866->870 +4; C singletons 745->
  747 +2 / ranges 888->892 +4, same 6 P359
  blocks both sides; no elif/else-if added
  either side: py file-wide elif 50 both, C
  else-if 0 both; deltas agree every side),
  CLOSED T10P prints 2042->2048 +6 both sides,
  seal 2136->2142 +6 (commit msgs; offset +94
  vs CLOSED-T10P stable): all agree, no slip
  (absolute seal inherits lane tally; delta
  verified).
  Viewer-vs-sweep reconcile first-hand:
  GATE-tier absolutes file-wide-exact (py 750->
  752, ranges 888->892 -- all EXACT, no slip
  this band); 4sp dispatch 740->742 / 866->870
  reconciled first-hand; file-wide unanchored
  differs from 4sp by 10 non-dispatch
  early-tier guards + 5-count C-vs-py dip-guard
  offset; deltas +2/+4/+6 every method.
- CONFIRM evidence (CONVERT-01 rule b):
  A-946-q1071-P359 verdict CONFIRM 52/52 CLEAN
  (own bed r5-P359 141669..142044 + r5-P358
  cross-refs, BAD=0; verifier v501.py P359
  52/52 PASS; file present, counts verified;
  tier GATED PORT; novelty gated: M-tails 16/16
  ALL NEW vs P358T + RQ-tails 16/16 ALL NEW vs
  P358T RM + RM-tails 16/16 ALL NEW vs both
  P358T; exact-value corroboration incl PB0
  NEW-sig sigdiff-2 32/84, PB1 NEW-sig 66/88,
  PBA16 2SIG-M7b0 VPOS 8, C10 sig-19 SAME-PB1
  VPOS 8 B5EDGE, QUAD64 1-sig-NOEDGE + R4 rows
  + trailing/subseq + R4-distinct + QM7 + NO
  frags + M-tails NEW, T256-SWAPPED + RM8-by-
  COL/RQ7-by-ROW + SWAPPED-tails + const
  97496d43 + counter/edges; plus const-count
  note: A-946 excl 79/80/75/71 memo-exact,
  committed tables match excl exactly -- no
  writer lag this tier, geometry exact, PORT
  verdict stands). Agrees with cport commit msg
  (PYID 10684, RGRAM 21368).
- FWD-check: banked Next-P360 from A-946+Q-1071
  agreement (both read first-hand; P360 lane
  code not on file at VERIFY time): PB0 @142017
  sig ada6a40c pay84 SIG-REPEAT of P359PB0
  (payload 32/84 diff, NOT byte-equal) + PB1
  19000000 pay88 @142018 SIG-REPEAT of P359PB1
  (79/88 diff, NOT byte-equal) + PBA88 b6010000
  x16 @142019-034 + C10-region 18000000 pay88
  x10 @142035-044 DIFFERS-from-PB1-sig (banked
  for r75 CONSUME-FIRST and corroborate EXACT
  at that time per bank-miss lesson).
- Quiz: no conflicting CLAIM/GATE/FLAG on b467.
  Activity polled (no b467 conflict); PROSE-01
  re-read before filing (all hex/counts copied
  from run output above).
- Logs: NVME ws tmp/encode-viewer/r74/
  (build467.log, pyid467.log, rgram467py/c.log,
  cmp467.py, seteq467.py, ownloop467.py,
  secf467a/b/c.py, edges467.py, tabaudit467.py,
  w467loop.log, smoke467.log, units467.log,
  band diff via git).

Verdict: PASS. No RED. 348-pin contiguous range
141669..142016 sealed. Round cap 4/4 reached.
