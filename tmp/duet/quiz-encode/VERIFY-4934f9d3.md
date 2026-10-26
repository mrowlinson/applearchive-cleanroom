# VERIFY-4934f9d3 b459 T10P351 pins 138885..139232 (348 pins) PASS

Seat viewer-r72, first-hand, tree @4934f9d3,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r72.
Base cbae1809 (b458 tip, 2088 tiers sealed; this
seat's VERIFY-cbae1809 PASS-filed same round,
base-use only, respected). Band = add7c00d (py
merge w2b@baf89129 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 4934f9d3 (C
port; parent == add7c00d verified via git log).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P351 shape (A-937 Q1 + Q-1062 agree)
CONSUMED FIRST and VERIFIED first-hand EXACT:
PB0 ae40e406 @138885 (S0 head; NEW-sig 1B-off,
31/84 diff vs P350PB0) + PB1 0d000000 @138886
(S1 head; NEW-sig, 69/88 diff vs P350PB1; 79/88
vs own C10[0] n138903, SIG-EQ-own-C10) + PBA
dc000000 x16 @138887-902 (AC b0-3 = dc/00/00/
00) + C10-region 0d000000 x10 @138903-912 (CC
b0-3 = 0d/00/00/00, SAME-as-PB1-sig) -- all
corroborated against lane code both sides
before any battery step (no bank-miss).

- Build: seat-private build459/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 da96df64...
  == GATE.
- RGRAMC-PYID 10452/10452 covered=10452/10452
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 20904/20904 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 20904/20904 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (20904/20904, sorted).
- PINS-RGRAM cells set-eq 10452/10452 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq459.py GREEN). PINS 20906 lines
  first-hand (2 hdr + 20904 rows; base 20848
  lines / 20846 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10423->10452 +29/-0 (python
  sets, trailing-';' strip, never comm): 138885
  138886 138887 138888 138894 138895 138901
  138902 138903 138904 138907 138908 138911
  138912 138913 138928 138929 138944 138945
  138960 138961 138976 138977 139007 139008
  139060 139135 139136 139232 (== GATE sampled
  list EXACT).
  29 = 2 sing (138885 138886) + A 6 (head
  138887 + 138888 + pair 138894/138895 + pair
  138901/138902 tail; offs 0,1,7,8,14,15; offs
  2-6,9-13 unsampled) + C 6 (head 138903 +
  138904 + 138907 + 138908 + 138911 + tail
  138912; offs 0,1,4,5,8,9; offs 2,3,6,7
  unsampled) + Q 8 (head 138913 + boundary pairs
  138928/138929 + 138944/138945 + 138960/138961
  + tail 138976; offs 0,15,16,31,32,47,48,63;
  NO mid -- b5 const NO edge, all boundaries
  pair-covered, first-hand) + R 7 (head 138977 +
  edge pair 139007/139008 + mid 139060 + edge
  pair 139135/139136 + tail 139232; offs
  0,30/31,83,158/159,255; 1-mid shape off83
  NEW, both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  20904-20846.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit459.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 152 PASS 0 FAIL 2nd full-green run
  (1st run caught the seat-script 1B-off assert
  miss: required b3 EQUAL for a 1B-off sig --
  fixed to b3-IN-diff + b0-2-NOT (ae40e406 vs
  ae40e407: exactly b3 differs), re-greened;
  lesson: 1B-off means precisely one sig byte
  differs, assert the differing byte IN the
  diff).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ae40e406 NEW-sig 1B-off (31/84
  payload diff vs P350S0 @ b3-5,22,23,30-36,
  38-43,48,49,52-55,68-72,74,75 first-hand, sig
  b0-2 NOT in diff with b3 IN diff, NOT byte-
  equal) / S1 176ch sig 0d000000 NEW-sig (69/88
  payload diff vs P350S1 @ b0,4-59,76-87
  first-hand, sig b0 IN diff, NOT byte-equal; vs
  own C10 cells TRUE UNIFORM [79x10] staged+
  oracle, all-10 identical positions @ b4,6-55,
  60-87, sig b0-3 same-sig NOT in diff; NOT
  byte-equal),
  staged as full-payload singletons.
  AM 16/16 12ch distinct, CM 10/10 8ch distinct,
  M 16/16 14ch distinct, QR 4/4 6ch distinct
  UNPAIRED (R3 rows r0 97ce8a / r1 8ab198 / r2
  aab198 / r3 cab198 exact tuples; full tails =
  R3 pairs + const b87 0x6f quad-wide, 4/4
  distinct; trailing-suffix = TSHARE =
  1/1/1/3/3/3 (all pairs share b87 const 6f;
  r123 TRUE trailing 3 via b198) + subseq-lcs
  2/1/1/3/3/3 ((0,1) 2 via {8a,6f} -- trailing
  pair shares first-hand, memo suffix metric
  matched EXACT); tails 4 distinct),
  RM 16/16 14ch distinct, RQ 16/16 14ch distinct,
  no QT (R3 b84-86 inside QR + b87 const) + no
  RT (SWAPPED tails, not ROWTAIL) + no F (no
  frags). M-vs-RQ FULL7 (M 7B vs RQ 7B lanes
  [20,21,22,80,81,82,83] both: rows element-wise
  16/16, all 7 cols position-exact 16/16, full-
  row sets EQUAL, sorted rows equal; M list ==
  RQ list) -- 47th odd-band RQ==M instance,
  FULL7 degree (viewer chain: 10th full-identity
  survey -- b453 7th + b455 8th on file, b457
  9th same round 8OF9 unnumbered in its VERIFY;
  GATE cites sweep seat-map "SEVENTH"/P343-6th =
  sweep scope, distinct numbering; scopes noted,
  reconciliation deferred to sweep accounting);
  ordered per lesson (d) (full-row sets EQUAL);
  width predictor dead, never cited. AC 80, CC
  82, QC 76, RC 72; C _N decls 80/82/76/72
  match actual; byte-coverage unions exact every
  block (88/88/88/88, 0 overlap gap-free, M/R-tab
  computed; Q consts cover b86? no -- b86 in R3
  lane + b87 const 6f in QC). PBA88-PLAIN-M6b13
  sig dc000000 (b0 const dc via AC b0-3; AM 16/16
  distinct NO pair; M6 b13,14,80-83; A-b5set
  {3d} const first-hand).
  C10-1SIG-88-TAIL-M4 sig 0d000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 full-sig
  consts; CM 10/10 diverge 8ch b84-87; b5 const
  3d full block via lencode).
  QUAD88-1SIG-QM7/R3-NOEDGE 1-sig d2000000 x64
  DIFFERS-from-PBA-sig (b0 const d2 in QC, b1-3
  const 00; b5 const 3d NO edge full block via
  raw lencode; b4 base 0x43 step2 64/64
  contig+2 range 43..c1 NO wrap, 64 distinct;
  QM7 b20,21,22,80-83 M 16/16 14ch distinct NO
  frags (m = off&15 both sides) shared-x3-vs-row0
  48/48 oracle (lanes 20-22,80-83; see tabaudit459
  shared-x3) NO frags + R3 b84-86 rows above 4/4
  UNPAIRED BY-ROW const (q = off>>4 both sides);
  tails 4 distinct (r123 TRUE trailing-3 b198 +
  all-pairs b87-6f); b87 const 6f quad-wide
  64/64 oracle (see edges459 qb87); NO frags).
  Ring SWAPPED-split: sig 270d0000 x256;
  code-TM7 b28,29,30,76-79 by COL RM 16/16 +
  code-TR7 b20,21,22,80-83 by ROW RQ 16/16
  UNPAIRED (SWAPPED tails b80-83 row / b76-79
  col); b0 const 27 (256/256 oracle, in RC
  table); b1 const 0d (256/256 oracle, in RC
  table); b84-87 const eab1986f ring-wide NEW
  (256/256 oracle).
  VPOS partitions re-derived from code: PBA 7
  (missing 8 - 1: b4+M6, b5 const deducted) /
  C10 5 (missing 6 - 1; b4+M4, b5 const
  deducted) / quad 11 (missing 12 - 1; b4+QM7+
  R3, b5 const deducted -- 3rd shape, cf P347) /
  T 16 (missing 16 - 0; b4,b5+TM7+TR7, b0 const
  lives in-table, b5 counter-varies in VPOS) --
  all match A-938 (missing sets AC-8
  [4,5,13,14,80-83] / CC-6 [4,5,84-87] / QC-12
  [4,5,20,21,22,80-86] / RC-16
  [4,5,20,21,22,28,29,30,76-83] first-hand
  EXACT; deduct-const-b5-or-in-table convention
  holds incl the Q-const 3rd shape; b5 variance
  checked from oracle bytes: A {3d}, C {3d}, Q
  {3d} const).
  Code-consts vs A-938 INCL (PBA 81 / C10 83 /
  quad 77 / T88 72): impl 80/82/76/72 =
  memo-exact (A/C/Q b5 const 3d deducted; T
  counter, no deduction) = incl +3 for the three
  b5-const lanes; A-938 excl 80/82/76/72 = code
  EXACT -- no lag on odd band (deduct-only-
  when-vary holds: Q-const keeps b5 deducted,
  cf P347). VPOS 7/5/11/16 = memo EXACT.
  M-tails 16/16 ALL NEW vs P350T RQ row-led
  tails (overlap 0; P350T RQ9 frame first-hand
  from code, ref = RQ9 9B rows, position-aware
  tails last-4B) + RQ-tails (b80-83) 16/16 ALL
  NEW vs P350T RM col-led tails (overlap 0;
  ref = RM8 8B rows).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P350
  (all 0/16; widths P351 vs P350: AM 6B vs 8B,
  CM 4B vs 4B, M 7B vs 9B, QR 3B vs 2B, RM 7B
  vs 8B, RQ 7B vs 9B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 138885 / S1 138886 / A 138887-902 /
  C 138903-912 / Q 138913-976 / R 138977-232):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C/Q b5 const emerges
  from raw lencode) + R explicit counter
  (b4=(0xc3+2off)&FF b5=0x3d+(off>=31)+
  (off>=159); py hex 0xc3/0x3d; C staged
  literals 195/61/31/159 re-derived: 195==0xc3,
  61==0x3d) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 6B b13,14,80-83; C 4B lane
  b84-87; Q 7B/3B b20,21,22,80-83/b84-86; R
  7B/7B SWAPPED TM7 b28,29,30,76-79 by COL /
  TR7 b20,21,22,80-83 by ROW).
  C blocks carry T93278/93283/93288/93303/
  93318/93338 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present; bounds + byte positions
  exact: A 6B, C 4B, Q 7B/3B, R 7B/7B SWAPPED
  tails-split),
  A/C/Q raw lencode (no counter literals) + R
  counter b4=(0xc3+2off)&FF + (off>=31)+(off>=159)
  (C literals 195/61/31/159 verified), temps
  _t7069-7084 (base max _t7068, no reuse) +
  _i4287/4289/4292/4295 (base max _i4285, no
  reuse) + _b4286/4288/4290/4291/4293/4294 (base
  max _b4284, no reuse; union 4286-4295
  contiguous, first-hand), all 6 blocks verified.
  Insert position exact both sides: after
  T10P350R close (C comment + S0 block; py
  CLOSED + return + S0 guard 93278), at dispatch
  tail (N-out-of-scope fallthrough follows: C
  and py each 2 scope hits; early same-text
  guards unrelated scope).
  Matches A-938 geometry (framing 1x84+347x88
  pay = code dispatch 1+1+16+10+64+256 = 348
  pins; PB0 ae40e406 NEW-1B-off 31/84 + PB1
  0d000000 NEW 69/88 + SAME-as-own-C10 79/88 +
  differs-vs-own-PB0; PBA88-PLAIN-M6b13 VPOS 7
  b5 const 3d; C10-1SIG-88-TAIL-M4 VPOS 5 b5
  const 3d; QUAD88-1SIG-QM7/R3-NOEDGE VPOS 11 =
  b4+QM7+R3 (b5 const) + R3 4/4 UNPAIRED exact
  tuples + trailing 1/1/1/3/3/3 + b87 const +
  b5 const NO edge + M-tails NEW 16/16;
  T88-SWAPPED-RM7/RQ7 sig 270d0000 RM7 by COL +
  RQ7 by ROW UNPAIRED 16/16 + SWAPPED tails +
  b84-87 const eab1986f, ring counter +
  thresholds 31/159, NO D dips) + A-938 (suffix-
  lcs 1/1/1/3/3/3 = TAIL4 b84-87 all 3 metrics
  first-hand (subseq (0,1) 2 via {8a,6f} noted);
  consts excl 80/82/76/72 = lane EXACT).
- Edges own-loop ownloop459.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P351R N=139232 off=255.
  edges459.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0 embedded b4/b5
  0b/3d, S1 0d/3d == raw lencode) + aform 16/16
  (A head 0f/3d tail 2d/3d b5set {3d} NO step,
  0 ff) + cform 10/10 (C head 2f/3d tail 41/3d
  b5set {3d} NO step, 0 ff) + qform 64/64 (Q
  head 43/3d tail c1/3d; b5 const 3d 64/64 NO
  edge + qb87 64/64 const 6f; quad b4=(0x43+
  2off) 64/64 contig+2 range 43..c1 NO wrap, 64
  distinct) + ring counter 256/256 + ringraw
  256/256 (head c3/3d; off30/31 (139007->139008)
  ff/3d->01/3e; mid off83 69/3e @139060;
  off158/159 (139135->139136) ff/3e->01/3f;
  tail off255 c1/3f @139232; exactly 2 ff in
  348, both ring-edge) + b0 const 27 256/256 +
  b1 const 0d 256/256 + b84-87 const eab1986f
  256/256 (all from oracle bytes first-hand).
  Odd-lencode 348/348 (346 + S0/S1 embedded).
  Ring counter==raw-lencode 256/256 b4
  mismatches 0 (thresholds 31/159 identical
  first-hand arithmetic); quad counter==raw-
  lencode 64/64 b4 mismatches 0. Ring edges +
  mid 139060 + tail 139232 in for-list + 2 PASS
  lines each py+C. Tail 139232: oracle rav sha
  9501a01d... == PINS (match True; rawlen 104);
  py+C CLOSED T10P351R off=255 agree. No
  DISSENT: cut bytes verify.
- PB-diff secf459a.py (cache path, 0 miss-warmed
  after ownloop) + secf459b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (138885 +
  138537 + 138886 + 138538); S0: oracle138885-
  vs-138537 31/84, codeS0-vs-P350S0 31/84,
  positions identical + staged-derived EXACT,
  sig b0-2 NOT in diff with b3 IN diff (NEW-sig
  1B-off ae40e406 vs ae40e407); DIRECT 31/84
  agree. S1: oracle138886-vs-138538 69/88,
  codeS1-vs-P350S1 69/88, positions identical +
  staged-derived EXACT, sig b0 IN diff (NEW-sig
  0d vs 0c); DIRECT 69/88 agree. Triple-derived
  both pairs (S0 NEW-sig 1B-off + S1 NEW-sig,
  staged novelty both tiers).
  S1-vs-own-C10 secf459c.py (staged assembly vs
  oracle C10 cells n138903-912: 10/10 byte-
  equal; staged S1 vs staged cells): [79x10] in
  all 10 cells at IDENTICAL positions, sig b0-3
  same-sig NOT in diff, sig 0d000000 all, NOT
  byte-equal. TRUE UNIFORM -- record 32->33
  (novelty-first: uniformity never assumed,
  GATE-shape-derived).
  Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  232/0 (rgram.py) + 1/1 (for-line) + PINS +58/
  +0 (clean append, 29 Ns x2) == GATE; band
  added lines 899 first-hand (== numstat sums
  608+232+1+58; sole del = old for-line
  replaced by superset); rgramc.c splits 603
  content + 5 bare-blank (exactly `+`, verified
  0 ws-only) = 608 == numstat; GATE states raw C
  "608 content+blank (5 blank-only)" exactly --
  NO overcount this odd band either (b457 same;
  odds overcount pattern b429-b455 closed or
  GATE learned; recorded). Code GREEN since
  gated artifact == verified artifact.
- Wall on band diff added lines (scope cbae1809..
  4934f9d3, 899 added lines first-hand): vendor
  0 hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits, aea-invoke 0 hits. Files: rgramc.c
  608/0, rgram.py 232/0 purely additive,
  test_rgram.sh 1/1 (for-line), PINS +58/+0.
  (GATE wall scope 840 = src-only 608+232; my
  wall covers the FULL 899 band-diff lines, 0
  hits -- superset.)
- Tiers: merge-msg +6/+58, code 6 blocks, tier-
  comments `# T10P` 1994->2000 +6, dispatch
  singletons 4sp (anchored) 724->726 +2 /
  file-wide unanchored 734->736 +2 = 4sp + 10
  non-dispatch early-tier guards / range-guards
  856->860 +4 = +6, C singletons 4sp 724->726
  +2 / file-wide 729->731 +2 (4sp + 5 dip-guard
  offset, pre-existing) / ranges 856->860 +4 =
  +6, CLOSED T10P prints 1994->2000 +6 both
  sides, seal 2088->2094 +6 (commit msgs; offset
  +94 vs CLOSED-T10P, stable b401-b459). All
  agree (stated literal methods first-hand: py
  file-wide elif 50->50, C else-if 0->0; A/C use
  raw lencode + Q b5-const + R counter, no stray
  counters; deltas agree every side: +2/+4/+6).
- CONFIRM evidence (CONVERT-01 rule b): A-938-
  q1063-P351 verdict CONFIRM 49/49 CLEAN (own
  bed r5-P351 138885..139260 + r5-P350 cross-
  refs, BAD=0 + direct-oracle 2/2 byte-match;
  verifier v501.py P351 49/49 PASS; file present,
  counts verified; tier GATED PORT; novelty gated
  M-tails 16/16 ALL NEW vs P350T RQ row-led
  tails + RQ-tails NEW; exact-value corroboration
  incl PB0 NEW-1B-off 31/84, PB1 NEW 69/88
  SAME-as-own-C10 79/88, PBA16 sig-dc VPOS 7,
  C10 sig-0d SAMESIG VPOS 5, QUAD64 1-sig-d2
  DIFFERS-from-PBA + R3 rows +
  suffix-lcs-1/1/1/3/3/3 (subseq (0,1) 2 noted)
  + b87-const +
  QM7 + NO frags + b5 const + M-tails NEW,
  T256-SWAPPED + RM7-by-COL/RQ7-by-ROW +
  SWAPPED-tails + b0-27 + const eab1986f +
  counter/edges; plus sheet-vs-tables const-count
  note: A-938 sheet excl 80/82/76/72 memo-exact
  (incl +3 b5-const PBA/C10/quad), committed
  tables 80/82/76/72 deduct-where-const --
  S-F arithmetic only where b5 const, geometry
  exact, PORT verdict stands; w2b-r31 4/8, cited
  from body read first-hand). Agrees with cport
  commit msg (PYID 10452, RGRAM 20904). No
  viewer P351 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record). No DISSENT on P351; no FLAG
  names P351/b459/4934f9d3 (filename + body-grep
  survey first-hand).
- Quiz: no conflicting CLAIM/GATE/FLAG on b459/
  4934f9d3 (quiz poll + filename grep first-
  hand; adjacent evens b458/b460 = sweep2 turf
  incl b460 C port 03dfc04c live, base-use only,
  no verdict on b459; zero FLAG hits on T10P351/
  b459; CLAIM at brief path is this seat's own
  r72 claim). PROSE-01: all hex/counts above
  copied from own run output; GATE-4934f9d3
  re-read in FULL before filing (zero GATE slips
  this band; "18th/19th" numbering notes below
  are cross-seat accounting, not GATE errors).
- RQ==M chain: b459 odd FULL7 (M 7B vs RQ 7B
  lanes [20,21,22,80-83] both: rows element-wise
  16/16, all 7 cols position-exact, full-row sets
  EQUAL, sorted rows equal; M list == RQ list)
  -- 47th odd-band RQ==M instance, FULL7 degree
  (second FULL degree on file after P343 per
  GATE). Viewer-vs-sweep convention reconciled
  first-hand (4sp-dispatch-exact both sides;
  file-wide +10 guards py / +5 C dip offset;
  deltas +2/+4/+6 every method).
- TRUE-uniform chain: b459 UNIFORM [79x10]
  SAMESIG (staged+oracle, positions identical
  all-10, sig same-sig NOT in diff). Record
  32->33. GATE numbers it "19th TRUE-uniform
  case" -- collides with P346-18th on file in
  this chain (in sweep accounting) plus P349
  claimed 18th by sweep GATE-c3383244; numbering
  ADJUDICATION DEFERRED to sweep accounting
  (evidence on file, secf459c). No new
  SAMESIG-same-sig even case (b459 odd; P338
  dispute untouched).
- S-F tables-lag: b459 odd band sheet==code
  (impl 80/82/76/72 == A-938 excl; incl
  +1/+1/+1/+0 = 81/83/77/72 == memo INCL) --
  no lag on odds (deduct-only-when-b5-const
  holds incl the Q-const 3rd shape, cf P347).
  Lag stays 42; even sub-streak stays 24 (b458
  last even).
- Next-P352 banked (A-938 Q1 + Q-1063 agree,
  for r73 to CONSUME FIRST): PB0 @139233 sig
  ae40e406 SAME-as-P351PB0 (31/84 diff, NOT
  byte-equal) + PB1 @139234 sig 0d000000
  SAME-as-P351PB1 (80/88 diff, NOT byte-equal) +
  PBA b2000000 x16 @139235-250 + C10-region
  0d000000 pay88 x10 @139251-260 (banked from
  dual memos; lane-code verify pending at
  CONSUME time per bank-miss lesson).
- Shared-x3 (chain-level): memo phrase "QM
  shared 16/16 x3 vs row0 NO frags" (A-938 Q2)
  verified 48/48 from oracle bytes for P351-QM7
  (lanes 20-22,80-83 col-only indexing + NO
  frags from oracle data, all 7 lanes x3 q-rows
  x16 cells). Memo phrase family holds, NOT a
  slip.

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; zero GATE slips this band (cross-
seat numbering notes on TRUE-uniform 19th and
full-identity 7th are accounting scope, not GATE
errors; uniformity + FULL7 themselves first-hand
GREEN). Code GREEN since gated artifact ==
verified artifact. Viewer scars (1 seat-script,
caught pre-file): tabaudit S0 1B-off assert miss
(required b3 EQUAL; fixed to b3-IN-diff +
b0-2-NOT, re-greened 152/152).
