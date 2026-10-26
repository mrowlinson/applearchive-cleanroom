# VERIFY-be565d02 b465 T10P357 pins 140973..141320 (348 pins) PASS

Seat viewer-r74, first-hand, tree @be565d02,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r74.
Base f7832b11 (b464 tip, 2124 tiers sealed; this
seat's VERIFY-f7832b11 PASS-filed same round,
base-use only, respected). Band = 58b503c0 (py
merge w2b@07cea973 partial, +6 tiers, +58 pins;
commit msg verified via git log) + be565d02 (C
port; parent == 58b503c0 verified via git
rev-list --parents). Chain 58b503c0 parent ==
f7832b11 verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P357 shape (A-943 "Next P357" FWD,
CONSUMED at VERIFY-f7832b11 filing and
re-corroborated here pre-battery) CONSUMED
FIRST and VERIFIED first-hand EXACT: PB0
aefa600d @140973 (S0 head; NEW-sig-1B-off
31/84 diff vs P356PB0 @ n140625, b3 IN diff
with b0-2 NOT, positions
[3-11,34,35,42-48,50-55,76,78-83]
first-hand, NOT byte-equal) + PB1 1a000000
@140974 (S1 head; NEW-sig 66/88 diff vs P356PB1
@ n140626, sig b0 IN diff, positions
[0,4-14,16,17,19-27,36-38,40-43,48-55,60-87]
first-hand, NOT byte-equal; 24/88 vs own C10[0]
n140991, SIG-EQ-own-C10; DIFFERS-vs-own-PB0
ae-vs-1a) + PBA a6010000 x16 @140975-990 (AC
b0-3 = a6/01/00/00; A-mtab b28-31,80-83) +
C10-region 1a000000 pay88 x10 @140991-141000
(CC b0-3 = 1a/00/00/00, SAME-as-PB1-sig; CM
lanes b84,85 with b86 const 0xb8 + b87 const
0xae in CC; CM rows b84,85 diverge 4ch) -- all
corroborated against lane code both sides
before any battery step (no bank-miss).

- Build: seat-private build465/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 ba6b4ec6...
  (prefix == GATE; GATE states sha1 6a219659 +
  sha256 ba6b4ec6 this band; compared
  programmatically, never hand-transcribed).
- RGRAMC-PYID 10626/10626 covered=10626/10626
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21252/21252 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21252/21252 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21252/21252, sorted +
  raw identical; cmp465.py GREEN).
- PINS-RGRAM cells set-eq 10626/10626 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq465.py GREEN). PINS 21254 lines
  first-hand (2 hdr + 21252 rows; base 21196
  lines / 21194 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10597->10626 +29/-0 (python
  sets, trailing-';' strip, never comm): 140973
  140974 140975 140976 140982 140983 140989
  140990 140991 140992 140995 140996 140999
  141000 141001 141016 141017 141032 141033
  141055 141056 141064 141065 141183 141184
  141240 141311 141312 141320 (== GATE sampled
  list EXACT).
  29 = 2 sing (140973 140974; offs 0,1) + A 6
  (head 140975 + 140976 + edge pair 140982/
  140983 off7/8 + pair 140989/140990 off14/15;
  offs 0,1,7,8,14,15; b5 const 4d NO step) + C
  6 (head 140991 + 140992 + 140995 + 140996 +
  140999 + tail 141000; offs 0,1,4,5,8,9; b5
  const 4d NO step) + Q 8 (head 141001 +
  boundary pairs 141016/141017 off15/16 +
  141032/141033 off31/32 + edge pair 141055/
  141056 off55 B5EDGE pair-covered + tail
  141064 off63; offs 0,15,16,31,32,47,48,63;
  NO mid (b5 edge off55 pair-covered 141055+
  141056), all boundaries pair-covered,
  first-hand) + R 7 (head 141065 + edge pair
  141183/141184 off118/119 + mid 141240 off175
  + edge pair 141311/141312 off246/247 + tail
  141320 off255; 1-mid shape off175 NEW, both
  counter edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21252-21194.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit465.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 160 PASS 0 FAIL second-run (1
  seat-script carried-value fix: QC b1-3 is
  01/00/00 first-hand both sides -- GATE prose
  "b1-3 const 00" is a mild slip; sig f8010000
  exact, code GREEN; recorded + still PASS).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig aefa600d NEW-sig-1B-off (31/84
  payload diff vs P356S0, positions
  [3-11,34,35,42-48,50-55,76,78-83]
  first-hand, b3 IN diff with b0-2 NOT, NOT
  byte-equal) / S1 176ch sig 1a000000 NEW-sig
  (66/88 payload diff vs P356S1, positions
  [0,4-14,16,17,19-27,36-38,40-43,48-55,60-87]
  first-hand, sig b0 IN diff, NOT byte-equal;
  vs own C10 cells TRUE UNIFORM [10x24]
  staged+oracle: all-10 identical positions
  [4,20-28,30-35,64-67,84-87], sig b0-3
  same-sig NOT in diff; NOT byte-equal; S1
  SIG-EQ own C10; S1 SIG-DIFFERS own PB0),
  staged as full-payload singletons.
  AM 16/16 8B distinct, CM 10/10 2B diverge,
  M 16/16 9B distinct, QR 4/4 2B distinct
  UNPAIRED (R2 rows r0 53f3 / r1 73f3 / r2 f4f3
  / r3 14f4 exact tuples; full tails = R2 pairs
  + b86 const 0xb8 + b87 const 0xae, 4/4
  distinct; trailing-suffix = 3/3/2/3/2/2,
  subseq = 3/3/2/3/2/3, TSHARE = 3/3/2/3/2/2
  (5/6 agree, pair (2,3) divergent
  first-hand); tails 4 distinct), RM 16/16 8B
  distinct, RQ 16/16 8B distinct, no QT (R2
  b84,85 inside QR + b86/b87 consts) + no RT
  (STANDARD-split tails) + no F (no frags).
  M-vs-RQ 0OF8 (M 9B lanes [29,30,31,34,35]+
  tails vs RQ 8B lanes [32,33,34,35,76-79]:
  widths differ so rows 0/16; first-8 per-col
  position-exact all 0/16; full-row sets
  DISJOINT (intersect 0); M list != RQ list)
  -- 50th odd-band RQ==M instance, FIRST 0OF8
  fully-disjoint degree (no precedent on file;
  viewer chain: odds 49->50; 16th full-identity
  survey); ordered per lesson (d) (rows
  DISJOINT + heads fully disjoint position +
  set, same order); width predictor dead, never
  cited; AM-vs-RQ same-width cross-check 8B/8B
  (rows 0/16, per-col [0,3,0,0,0,0,0,0], sets
  DISJOINT, agrees disjoint); tails STANDARD-
  split (TM b40-43,80-83 by COL c=off&15, TR
  b32-35,76-79 by ROW r=off>>4, 16/16 distinct
  each, sequences UNPAIRED); M-tails 16/16 ALL
  NEW vs P356T RQ row-led tails (overlap 0;
  P356T RQ 16x7B frame first-hand from code,
  tails last-4B); RQ-tails (b76-79) 16/16 ALL
  NEW vs P356T RM col-led tails (overlap 0;
  P356T RM 16x8B frame first-hand from code,
  tails last-4B); AM/CM/M/QR/RM/RQ full-row
  0-overlap vs P356 (all 0/16; widths P357 vs
  P356: AM 8B vs 7B, CM 2B vs 2B, M 9B vs 7B,
  QR 2B vs 1B, RM 8B vs 8B, RQ 8B vs 7B).
  AC 78, CC 84, QC 75, RC 70; C _N decls
  78/84/75/70 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; Q b0 const f8
  1-sig in QC first-hand (b1 const 01, b2-3
  const 00); C b86/b87 const b8/ae in CC
  first-hand).
  PBA88-PLAIN-M8b28 sig a6010000 (b0 const a6
  via AC b0-3; AM 16/16 distinct NO pair; M8
  b28-31,80-83; b5 const 4d NO step NO edge --
  b5 const deducted, in AC-missing).
  C10-1SIG-88-TAIL-M2 sig 1a000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  1a000000; CM 10/10 diverge 4ch b84,85; CC has
  no b84,85 (both in CM lane); b86,87 const b8/
  ae; b5 const 4d full block via lencode).
  QUAD88-1SIG-QM9/R2-B5EDGE 1-sig f8010000 x64
  (b0 const f8 in QC; b5 = 0x4d+(off>=55) in
  VPOS, edge off55 B5EDGE pair-covered 141055->
  141056; b4 base 0x93 step2 64/64 range
  93..11 contig+2 NO wrap, 64 distinct; QM9
  b29,30,31,34,35,80-83 M 16/16 9B distinct NO
  frags (m = off&15 first-hand) + R2 b84,85
  rows 53f3/73f3/f4f3/14f4 4/4 UNPAIRED BY-ROW
  const (q = off>>4 first-hand); tails = R2 +
  const b86 b8 / b87 ae quad-wide, full-tail
  trailing 3/3/2/3/2/2 + subseq 3/3/2/3/2/3 +
  TSHARE 3/3/2/3/2/2 + R2 all-distinct).
  Ring T88-STANDARD-split sig f8180000 x256
  (b0 const f8 256/256 oracle, in RC table; b1
  const 18 256/256 oracle, in RC table; code-
  TM8 b40-43,80-83 by COL RM 16/16 + code-TR8
  b32-35,76-79 by ROW RQ 16/16 UNPAIRED
  (SPLIT tails b80-83 col / b76-79 row);
  b84-87 const 53f4b8ae ring-wide NEW;
  b4=(0x13+2off)&FF + (off>=119)+(off>=247)
  (C literals 19/78/119/247 verified ==
  0x13/0x4e/119/247; py hex 0x13/0x4e)).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - 1; b4+M8 b28-31,80-83, b5
  const deducted) / C10 3 (missing 4 - 1;
  b4+M2 b84,85, b5 const deducted) / quad 13
  (missing 13 - 0; b4,b5-step+QM9 9+R2 2, b5
  STEPS B5EDGE in VPOS, NO deduct) / T 18
  (missing 18 - 0; b4,b5+TM8+TR8, b0/b1 consts
  live in-table) -- all match A-944 (missing
  sets AC-10 [4,5,28-31,80-83] / CC-4
  [4,5,84,85] / QC-13 [4,5,29-31,34,35,80-85]
  / RC-18 [4,5,32-35,40-43,76-83] first-hand
  EXACT; deduct-const-b5-or-in-table convention
  holds incl the QM9/B5EDGE shapes; b5 variance
  checked from oracle bytes: A {4d} const, C
  {4d} const, Q {4d,4e} steps, T
  counter-varies).
  Code-consts vs A-944 INCL/EXCL (PBA 78 / C10
  84 / quad 75 / T88 70 excl): impl 78/84/75/
  70 = memo-excl EXACT -- no lag on odd band
  (deduct-only-when-vary holds; A-944 INCL
  +1/+1 for the two b5-const lanes = 79/85/75/
  70). VPOS 9/3/13/18 = memo EXACT. S-F lag
  stays 44; even sub-streak stays 26.
  M-tails 16/16 ALL NEW vs P356T RQ row-led
  tails (overlap 0); RQ-tails 16/16 ALL NEW vs
  P356T RM col-led tails (overlap 0); AM/CM/M/
  QR/RM/RQ 0-overlap vs P356 all six.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 140973 / S1 140974 / A 140975-990 /
  C 140991-141000 / Q 141001-064 / R 141065-
  320): bounds + paylens (1x84 + 347x88) +
  lencode l16 A/C/Q both sides (A/C b5 const
  emerges from raw lencode; Q b5 step emerges
  from raw lencode + b4 formula) + R explicit
  counter (b4=(0x13+2off)&FF b5=0x4e+(off>=
  119)+(off>=247); py hex 0x13/0x4e; C staged
  decimal literals 19/78/119/247 re-derived:
  19==0x13, 78==0x4e) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/rtab
  byte positions exact (A 8B b28-31,80-83; C
  2B lane b84,85 + b86/b87 consts; Q 9B/2B
  b29,30,31,34,35,80-83/b84,85; R 8B/8B
  STANDARD-split TM8 b40-43,80-83 by COL / TR8
  b32-35,76-79 by ROW).
  C blocks carry T94672/T94677/T94692/T94707/
  T94727 py-line cites (each re-read: hits the
  exact py guard line, C comment text matches
  py, all 5 present + S0 guard 94667 verified
  in py; bounds + byte positions exact: A 8B,
  C 2B, Q 9B/2B, R 8B/8B STANDARD tails-split),
  A/C/Q raw lencode (no counter literals) + R
  counter b4=(19+2off)&FF + (off>=119)+
  (off>=247) (C literals 19/78/119/247
  verified), temps _t7165-7180 (base max _t7164,
  no reuse) + _i4347/4349/4352/4355 (base max
  _i4345, no reuse) + _b4346/4348/4350/4351/
  4353/4354 (base max _b4344, no reuse),
  union 4346-4355 contiguous, all 6 blocks
  verified.
  Insert position exact both sides: after
  T10P356R close (C "T10P3570 singleton" after
  "CLOSED T10P356R"; py return 0 + S0 guard
  94667), at dispatch tail (N-out-of-scope
  fallthrough follows; plateau guards at C
  169595 / py 58521 are the T4 plateau,
  unrelated scope).
  Matches A-944 geometry (PB0 NEW-sig-1B-off
  31/84; PB1 NEW-sig 66/88 SAME-as-own-C10
  24/88; PBA88-PLAIN-M8b28 VPOS 9 sig-a6 b5
  const M8 16/16 distinct; C10-1SIG-88-TAIL-M2
  VPOS 3 SAME-as-PB1-sig b5 const M2 10/10
  diverge; QUAD88-1SIG-QM9/R2-B5EDGE VPOS 13 +
  R2 4/4 UNPAIRED 53f3/73f3/f4f3/14f4 +
  trailing 3/3/2/3/2/2 + subseq 5/6 + b86/b87
  const + M-tails NEW 16/16;
  T88-RING-STANDARD-split VPOS 18 + TM8-by-COL/
  TR8-by-ROW UNPAIRED 16/16 + SPLIT-tails +
  b84-87 53f4b8ae + counter 19/78/119/247;
  lencode 348/348 whole-tier, NO D dips) incl
  exact values; M-vs-RQ 0OF8 fully-disjoint
  first-hand this tier, tier stands.
- Edges via counter formula first-hand: A head
  5f/4d tail 7d/4d b5set {4d} NO step, 0 ff; C
  head 7f/4d tail 91/4d b5set {4d} NO step, 0
  ff; Q head 93/4d edge off54 (141055 ff/4d)
  -> off55 (141056 01/4e),
  B5EDGE pair-covered, exactly 1 ff; ring
  pre-edge off118 (ff/4e), edge off119 (01/
  4f); edge off246 (ff/4f) -> off247 (01/50);
  exactly 2 ff in 256; R head 13/4e (141065)
  mid off175 71/4f (141240) tail off255 11/50
  (141320); formulas re-derived from T10P357R
  code text (13/4e/119/247 decimal == 0x13/
  0x4e) + T10P357A/C/Q text (raw lencode); all
  edge pins + mid pin 141240 + tail 141320 in
  for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 match raw lencode. Ring
  counter==raw-lencode 256/256 + Q 64/64 + A
  16/16 + C 10/10. Odd-lencode 348/348
  (16+10+64+256+2). No DISSENT on cut bytes
  (edges465.py EDGES-GREEN, Q B5EDGE edge +
  range-with-wrap asserts verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 231/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; for-line replaced by superset (base
  for-N subset of band, removed 0); fine-norm
  equivalent (for464base.nums subset
  for465.nums, removed 0; C-scope del 0).
- Wall on band diff added lines (scope
  f7832b11..be565d02, 898 added lines): vendor
  0 hits, disasm 0 hits, depload 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits; 1 `aea` substring = PINS sha hex
  fragment (d886ee70..., 0 invocations -- same
  hex-fragment class as b464). Files touched:
  rgramc.c 608/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line
  extension), PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-file-wide 746->
  748 (+2: 140973/140974) / ranges py-file-wide
  880->884 (+4; 4sp dispatch 736->738 +2 /
  4sp ranges 858->862 +4; C
  singletons 741->743 +2 / ranges 880->884 +4,
  same 6 P357 blocks both sides; no elif/
  else-if added either side: py file-wide elif
  50 both, C else-if 0 both; deltas agree every
  side), CLOSED T10P prints 2030->2036 +6 both
  sides, seal 2124->2130 +6 (commit msgs;
  offset +94 vs CLOSED-T10P stable): all agree,
  no slip (absolute seal inherits lane tally;
  delta verified).
  Viewer-vs-sweep reconcile first-hand:
  GATE-tier absolutes file-wide-exact (py 746->
  748, ranges 880->884 -- all EXACT, no slip
  this band); 4sp dispatch 736->738 / 858->862
  reconciled first-hand; file-wide unanchored
  differs from 4sp by 10 non-dispatch
  early-tier guards + 5-count C-vs-py dip-guard
  offset; deltas +2/+4/+6 every method.
- CONFIRM evidence (CONVERT-01 rule b):
  A-944-q1069 memo CONFIRM 52/52 CLEAN
  (verifier v501.py 52/52 PASS; tier GATED PORT;
  novelty M-tails 16/16 ALL NEW vs P356T +
  RQ-tails 16/16 ALL NEW vs P356T RM; cited
  from body read first-hand; exact-value
  corroboration incl PB0 NEW-sig-1B-off 31/84,
  PB1 NEW-sig 66/88 SAME-as-own-C10 24/88,
  PBA16 sig-a6 VPOS 9, C10 sig-1a SAME-PB1
  VPOS 3, QUAD64 1-sig + R2 rows + trailing/
  subseq + b86/b87 const + QM9 + NO frags +
  M-tails NEW, T256-STANDARD + TM8-by-COL/TR8-
  by-ROW + SPLIT-tails + const 53f4b8ae +
  counter/edges; plus const-count note: A-944
  excl 78/84/75/70 memo-exact, committed
  tables match excl exactly -- no writer lag
  this tier, geometry exact, PORT verdict
  stands). Agrees with cport commit msg (PYID
  10626, RGRAM 21252).
- FWD-check first-hand: A-944 "Next P358"
  forward notes verified against P358 lane code
  (ee21fae8, git show, no checkout): PB0
  ada6240d @141321 (168ch pay84) + PB1
  18000000 @141322 (176ch pay88) + PBA
  e0010000 x16 (guard 141323..141338) +
  C10-region 1d000000 x10 (guard 141339..
  141348) -- all exact (banked for b466
  CONSUME).
- Quiz: no conflicting CLAIM/GATE/FLAG on b465.
  Activity polled (no b465 conflict); PROSE-01
  re-read before filing (all hex/counts copied
  from run output above).
- Logs: NVME ws tmp/encode-viewer/r74/
  (build465.log, pyid465.log, rgram465py/c.log,
  cmp465.py, seteq465.py, ownloop465.py,
  secf465a/b/c.py, edges465.py, tabaudit465.py,
  w465loop.log, smoke465.log, units465.log,
  band diff via git).

Verdict: PASS. No RED. 348-pin contiguous range
140973..141320 sealed. Ready for viewer b466.
