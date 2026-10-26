# VERIFY-cbae1809 b458 T10P350 pins 138537..138884 (348 pins) PASS

Seat viewer-r72, first-hand, tree @cbae1809,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r72.
Base c3383244 (b457 tip, 2082 tiers sealed; this
seat's VERIFY-c3383244 PASS-filed same round,
base-use only, respected). Band = b3a6b6d6 (py
merge w2b@54496646 partial, +6 tiers, +58 pins;
commit msg verified via git log) + cbae1809 (C
port; parent == b3a6b6d6 verified via git log).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P350 shape (A-936 Q1 + Q-1061 agree)
CONSUMED FIRST and VERIFIED first-hand EXACT:
PB0 ae40e407 @138537 (S0 head; NEW-sig NEW
family, 32/84 diff vs P349PB0) + PB1 0c000000
@138538 (S1 head; NEW-sig, 48/88 diff vs
P349PB1; 46/88 vs own C10[0] n138555, DIFFERS-
from-own-C10) + PBA 94000000 x16 @138539-554
(AC b0-3 = 94/00/00/00) + C10-region 0d000000
x10 @138555-564 (CC b0-3 = 0d/00/00/00,
DIFFERS-from-PB1-sig) -- all corroborated
against lane code both sides before any battery
step (no bank-miss).

- Build: seat-private build458/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 fa02115c...
  == GATE.
- RGRAMC-PYID 10423/10423 covered=10423/10423
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR set NVME).
- RGRAM py 20846/20846 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 20846/20846 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (20846/20846, sorted +
  raw-identical first-hand; cmp458.py).
- PINS-RGRAM cells set-eq 10423/10423 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq458.py GREEN, 1st full-green run -- no
  adapt miss this band). PINS 20848 lines
  first-hand (2 hdr + 20846 rows; base 20790
  lines / 20788 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10394->10423 +29/-0 (python
  sets, trailing-';' strip, never comm): 138537
  138538 138539 138540 138546 138547 138553
  138554 138555 138556 138559 138560 138563
  138564 138565 138580 138596 138612 138623
  138624 138627 138628 138629 138751 138752
  138800 138879 138880 138884 (== GATE sampled
  list EXACT).
  29 = 2 sing (138537 138538) + A head/mid/tail
  pairs (6: head pair 138539/138540 off0/1, pair
  138546/138547 off7/8, tail pair 138553/138554
  off14/15) + C head/mid/tail pairs (6: 138555/
  138556 off0/1, mid pair 138559/138560 off4/5,
  tail pair 138563/138564 off8/9) + Q head/off15/
  off31/off47/edge-pair/off62/tail (8: head
  138565 off0, 138580 off15, 138596 off31,
  138612 off47, EDGE pair 138623/138624 off58/59
  b5 edge, 138627 off62, tail 138628 off63) + R
  head/edge-pair/mid/edge-pair/tail (7: head
  138629 off0, edge pair 138751/138752 off122/
  123, mid 138800 off171, edge pair 138879/
  138880 off250/251, tail 138884 off255).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  20846-20788.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  no oracle).
- Tables audit own script tabaudit458.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 147 PASS 0 FAIL 1st full-green run (no
  seat-script miss; RC-b1-const-09 asserted
  first-hand from code: sig 4d090000 b0/b1 both
  in-table).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ae40e407 NEW-sig (32/84 payload
  diff vs P349S0 @ b0-2,4,5,11,13-17,19-21,24-29,
  56-67 first-hand incl sig b0, NOT byte-equal) /
  S1 176ch sig 0c000000 NEW-sig (48/88 payload
  diff vs P349S1 @ b0,4,5,17-19,22-47,64-75,84-87
  first-hand, sig b0 IN diff, NOT byte-equal; vs
  own C10 cells NOT UNIFORM [46x10] staged+
  oracle, sig DIFFERS 0c-vs-0d with b0 IN diff
  all 10 cells; sig differs vs own PB0),
  staged as full-payload singletons.
  AM 16/16 16ch distinct, CM 10/10 8ch distinct,
  M 16/16 18ch distinct, QR 4/4 4ch distinct
  UNPAIRED (R2 rows r0 c7a6 / r1 e7a6 / r2 07a7 /
  r3 27a7 exact tuples; full tails = R2 pairs +
  const b86 ae / b87 d9 quad-wide, 4/4 distinct;
  suffix-lcs (01,02,03,12,13,23) = 3/2/2/2/2/3 +
  subseq-lcs 3/2/2/2/2/3 + tshare 3/2/2/2/2/3
  all-3 agree first-hand (== A-937 Q2); r01 and
  r23 share-3 pairs, rest 2),
  RM 16/16 16ch distinct, RQ 16/16 18ch distinct,
  no QT (quad tails = R2 pairs + const b86/87
  inside QR) + no RT (SWAPPED tails, not ROWTAIL)
  + no F (no frags). M-vs-RQ 16/16 string-
  identical SAME-ORDER (M list == RQ list; QM9
  b51-55,80-83 col-indexed (m = off&15 both
  sides) vs RQ9 b51-55,80-83 by ROW (r = off>>4
  both sides); string-eq HOLDS this tier --
  reported, not gated) -- 46th even-band RQ==M
  instance, ORDERED-IDENTICAL (cf b452/b454/
  b456); ordered per lesson (d) (string-
  identical same-order); width predictor dead,
  never cited. AC 78, CC 82, QC 75, RC 69; C _N
  decls 78/82/75/69 match actual; byte-coverage
  unions exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; Q consts cover
  b86/b87 ae/d9). PBA88-PLAIN-M8b38 sig 94000000
  (b0 const 94 via AC b0-3; AM 16/16 distinct NO
  pair; M8 b38,39,46,47,80-83; A-b5set {3a}
  const first-hand).
  C10-1SIG-88-TAIL-M4 sig 0d000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 full-sig
  consts; CM 10/10 diverge 8ch b84-87; CC has no
  b84-87 (all in CM lane) and no b5, b5 const 3a
  full block via lencode).
  QUAD88-1SIG-QM9/R2-B5EDGE 1-sig 94000000 x64
  SAME-sig-as-PBA (b0 const 94 in QC, b1-3 const
  00; b5 STEP 3a->3b @off58/59 via raw lencode
  NOT in QC (deducted, in VPOS); b4 base 0x8b
  step2 64/64 range 8b..ff,01..09, 64 distinct;
  QM9 b51-55,80-83 M 16/16 18ch distinct NO frags
  (m = off&15 first-hand) + R2 b84,85 rows above
  4/4 UNPAIRED BY-ROW const (q = off>>4
  first-hand); tails = R2 pairs + const b86 ae /
  b87 d9 quad-wide; b5-step @58/59 edge pair-
  covered; shared-x3-vs-row0 48/48 oracle (lanes
  51-55,80-83; see tabaudit458 shared-x3) NO
  frags).
  Ring SWAPPED-split: sig 4d090000 x256;
  code-RM8 b6,7,9,10,76-79 by COL RM 16/16 +
  code-RQ9 b51-55,80-83 by ROW RQ 16/16 UNPAIRED
  (SWAPPED tails b80-83 row / b76-79 col); b0
  const 4d (256/256 oracle, in RC table,
  deducted from VPOS per convention); b1 const
  09 (in RC table, first-hand); b84-87 const
  47a7aed9 ring-wide NEW (256/256 oracle).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - 1: b4+M8, b5 const deducted) /
  C10 5 (missing 6 - 1; b4+M4, b5 const
  deducted) / quad 13 (missing 13 - 0; b4,b5-
  step+QM9+R2, b5 step in VPOS no deduct) / T
  19 (missing 19 - 0; b4,b5+RM8+RQ9, b0 const
  lives in-table, b5 counter-varies in VPOS) --
  all match A-937 (missing sets AC-10
  [4,5,38,39,46,47,80-83] / CC-6 [4,5,84-87] /
  QC-13 [4,5,51-55,80-85] / RC-19
  [4,5,6,7,9,10,51-55,76-83] first-hand EXACT;
  deduct-const-b5-or-in-table convention holds;
  b5 variance checked from oracle bytes: A {3a},
  C {3a}, Q {3a,3b} steps).
  Code-consts vs A-937 INCL (PBA 79 / C10 83 /
  quad 75 / T88 69): impl 78/82/75/69 =
  writer-1 on PBA/C10 (impl tables still deduct
  const-b5 while A-937 sheet counts b5; memo
  confirms the sheet INCL values) -- S-F
  arithmetic persists in committed tables though
  the sheets are FIXED; memo-exact on quad (b5
  step-varies, in VPOS, no deduction) and T88
  (b5 counter-varies, in VPOS, no deduction);
  geometry exact, PORT verdict stands; FLAGGED
  for memo (24th even band running: .../b454/
  b456/b458; PBA/C10 lag this tier).
  QUAD 1SIG 94 SAME-sig-as-PBA this tier; PBA sig
  94 NEW vs P349 f4; AC∩QC 55 shared (b,v)
  pairs first-hand (GATE "AC-QC both=71
  sameval=55": the 55 verifies; "both=71" left
  uninterpretted -- recorded, not a slip: no
  code/behavior claim hangs on it).
  M-tails 16/16 ALL NEW vs P349T col-led tails
  (overlap 0; P349T RM8 frame first-hand from
  code, ref = RM8 8B rows, position-aware tails
  last-4B) + RQ-tails (b80-83) 16/16 ALL NEW vs
  P349T RQ row-led tails (overlap 0).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P349
  (all 0/16; widths P350 vs P349: AM 8B vs 7B,
  CM 4B vs 3B, M 9B vs 9B, QR 2B vs 4B, RM 8B
  vs 8B, RQ 9B vs 9B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 138537 / S1 138538 / A 138539-554 /
  C 138555-564 / Q 138565-628 / R 138629-884):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C/Q b5 const/step
  emerges from raw lencode) + R explicit
  counter (b4=(0x0b+2off)&FF b5=0x3b+(off>=123)+
  (off>=251); py hex 0x0b/0x3b; C staged
  literals 11/59/123/251 re-derived: 11==0x0b,
  59==0x3b) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 16ch b38,39,46,47,80-83;
  C 8ch lane b84-87; Q 18/4ch b51-55,80-83/
  b84,85; R 16/18ch SWAPPED RM8 b6,7,9,10,76-79
  by COL / RQ9 b51-55,80-83 by ROW).
  C blocks carry T93044/93049/93054/93069/
  93084/93105 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present; bounds + byte positions
  exact),
  A/C raw lencode (no counter literals) + Q
  b5-edge emergent + R counter b4=(0x0b+2off)&FF
  + (off>=123)+(off>=251) (C literals 11/59/123/
  251 verified), temps _t7053-7068 (base max
  _t7052, no reuse) + _i4277/4279/4282/4285
  (base max _i4275, no reuse) + _b4276/4278/
  4280/4281/4283/4284 (base max _b4274, no
  reuse; union 4276-4285 contiguous, first-hand),
  all 6 blocks verified.
  Insert position exact both sides: after
  T10P349R close (C 247353 print + return,
  comment 247356, S0 block; py CLOSED + return +
  S0 guard 93044), at dispatch tail (N-out-of-
  scope fallthrough follows: C 247537, py
  93125-26; early same-text guards at C 167003 /
  py 57606 are the T4 plateau-A n<=1076 check,
  unrelated scope).
  Matches A-937 geometry (PB0 NEW-sig 32/84;
  PB1 NEW-sig 48/88 DIFFERS-from-own-C10;
  PBA88-PLAIN-M8b38 VPOS 9 b5 const M8 16/16
  distinct; C10-1SIG-88-TAIL-M4 VPOS 5 DIFFERS-
  from-PB1-sig b5 const M4 10/10 diverge;
  QUAD88-1SIG-QM9/R2-B5EDGE VPOS 13 + R2 4/4
  UNPAIRED exact rows + suffix-lcs-3/2/2/2/2/3 +
  b86-ae/b87-d9 + b5-step + M-tails NEW;
  T88-SWAPPED-split VPOS 19 + RM8-by-COL/RQ9-by-
  ROW + SWAPPED-tails + b0-const-deducted +
  b84-87 47a7aed9 + counter 0b/3b/123/251;
  lencode 348/348 whole-tier, NO D dips) + A-937
  (suffix-lcs 3/2/2/2/2/3 = TAIL4 b84-87 all 3
  metrics first-hand; consts excl 78/82/75/69 =
  lane EXACT).
- Edges own-loop ownloop458.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P350R N=138884 off=255.
  edges458.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0 embedded b4/b5
  53/3a, S1 55/3a == raw lencode) + aform 16/16
  (A head 57/3a tail 75/3a b5set {3a} NO step,
  0 ff) + cform 10/10 (C head 77/3a tail 89/3a
  b5set {3a} NO step, 0 ff) + qform 64/64 (Q
  head 8b/3a, edge off58 (138623->138624)
  ff/3a->01/3b, tail 09/3b; b5set {3a,3b};
  quad b4=(0x8b+2off) 64/64 contig+2 range
  8b..ff,01..09, 64 distinct) + qb5step 64/64 +
  ring counter 256/256 + ringraw 256/256 (head
  0b/3b; off122 (138751->138752) ff/3b->01/3c;
  mid off171 61/3c @138800; off250 (138879->
  138880) ff/3c->01/3d; tail off255 09/3d
  @138884; exactly 3 ff in 348: 1 Q-edge + 2
  ring-edge; Q tail 09/3b vs R tail 09/3d same
  b4 differ in b5 labeled apart) + b0 const 4d
  256/256 + b1 const 09 256/256 + b84-87 const
  47a7aed9 256/256 (all from oracle bytes
  first-hand).
  Odd-lencode 348/348 (346 + S0/S1 embedded).
  Ring counter==raw-lencode 256/256 b4
  mismatches 0; quad counter==raw-lencode 64/64
  b4 mismatches 0. Ring edges + mid 138800 +
  tail 138884 in for-list + 2 PASS lines each
  py+C. Tail 138884: oracle rav sha == PINS
  (match True; rawlen 104); py+C CLOSED
  T10P350R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf458a.py (cache path, 0 miss-warmed
  after ownloop) + secf458b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (138537 +
  138189 + 138538 + 138190); S0: oracle138537-
  vs-138189 32/84, codeS0-vs-P349S0 32/84,
  positions identical + staged-derived EXACT,
  sig b0 IN diff (NEW-sig ae40e407 vs ef49ef07);
  DIRECT 32/84 agree. S1: oracle138538-vs-
  138190 48/88, codeS1-vs-P349S1 48/88,
  positions identical + staged-derived EXACT,
  sig b0 IN diff (NEW-sig 0c vs 0f); DIRECT
  48/88 agree. Triple-derived both pairs
  (S0 NEW-sig + S1 NEW-sig, staged novelty both
  tiers).
  S1-vs-own-C10 secf458c.py (staged assembly vs
  oracle C10 cells n138555-564: 10/10 byte-
  equal; staged S1 vs staged cells): [46x10] in
  all 10 cells, sig DIFFERS 0c-vs-0d with b0 IN
  diff all cells, NOT byte-equal. NOT UNIFORM --
  sig-differ (novelty-first: uniformity never
  assumed, GATE-shape-derived; chain TRUE-uniform
  stays 32).
  Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  233/0 (rgram.py) + 1/1 (for-line) + PINS +58/
  +0 (clean append, 29 Ns x2) == GATE; band
  added lines 900 first-hand (== numstat sums
  608+233+1+58; sole del = old for-line
  replaced by superset); rgramc.c splits 603
  content + 5 bare-blank (exactly `+`, verified
  0 ws-only) = 608 == numstat; GATE states raw C
  even-band shape correctly (603+5=608, no
  overcount -- evens-correct pattern holds).
  Code GREEN since gated artifact == verified
  artifact.
- Wall on band diff added lines (scope c3383244..
  cbae1809, 900 added lines first-hand): vendor
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
  comments `# T10P` 1988->1994 +6, dispatch
  singletons 4sp (anchored) 722->724 +2 /
  file-wide unanchored 732->734 +2 = 4sp + 10
  non-dispatch early-tier guards / range-guards
  852->856 +4 = +6, C singletons 4sp 722->724
  +2 / file-wide 727->729 +2 (4sp + 5 dip-guard
  offset, pre-existing) / ranges 852->856 +4 =
  +6, CLOSED T10P prints 1988->1994 +6 both
  sides, seal 2082->2088 +6 (commit msgs; offset
  +94 vs CLOSED-T10P, stable b401-b458). All
  agree (stated literal methods first-hand: py
  file-wide elif 50->50, C else-if 0->0; A/C use
  raw lencode + Q b5-edge emergent + R counter,
  no stray counters; deltas agree every side:
  +2/+4/+6).
- CONFIRM evidence (CONVERT-01 rule b): A-937-
  q1062-P350 verdict CONFIRM 49/49 CLEAN (own
  bed r5-P350 138537..138912 + r5-P349 cross-
  refs, BAD=0; verifier v501.py P350 49/49 PASS;
  file present, counts verified; tier GATED PORT;
  novelty gated M-tails 16/16 ALL NEW vs P349T
  RM col-led tails + RQ-tails NEW; exact-value
  corroboration incl PB0 NEW-sig 32/84, PB1 NEW-
  sig 48/88 DIFFERS-from-own-C10 46/88, PBA16
  sig-94 VPOS 9, C10 sig-0d DIFFSIG VPOS 5,
  QUAD64 1-sig-94 SAME-as-PBA + R2 rows +
  suffix-lcs-3/2/2/2/2/3 + b86-ae/b87-d9 +
  QM9 + NO frags + b5 const/step + M-tails NEW,
  T256-SWAPPED + RM8-by-COL/RQ9-by-ROW +
  SWAPPED-tails + b0-4d + const 47a7aed9 +
  counter/edges; plus sheet-vs-tables const-count
  note: A-937 sheet excl 78/82/75/69 memo-exact
  (incl +2 b5-const PBA/C10), committed tables
  78/82/75/69 still deduct const-b5 on PBA/C10 --
  S-F arithmetic in tables only, geometry exact,
  PORT verdict stands; w2b-r31 3/8, cited from
  body read first-hand). Agrees with cport
  commit msg (PYID 10423, RGRAM 20846). No
  viewer P350 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b458/
  cbae1809 (quiz poll + filename grep first-
  hand; adjacent odds b457/b459 = sweep turf
  incl b457 C port c3383244 live + b459 C port
  4934f9d3 live, base-use only, no verdict on
  b458; zero FLAG hits on T10P350/b458; CLAIM at
  brief path is this seat's own r72 claim).
  PROSE-01: all hex/counts above copied from own
  run output; GATE-cbae1809 re-read in FULL
  before filing (1 mild GATE obscurity, not a
  slip: "AC-QC both=71 sameval=55" -- the 55
  verifies first-hand as shared (b,v) pairs;
  "both=71" uninterpretted, recorded; no code/
  behavior claim hangs on it).
- RQ==M chain: b458 even ORDERED-IDENTICAL (M
  list == RQ list string-identical same-order,
  16/16) -- 46th even-band RQ==M instance (cf
  b452 43rd + b454 44th + b456 45th).
  Viewer-vs-sweep convention reconciled
  first-hand (GATE-tier absolutes 4sp-dispatch-
  exact both sides; file-wide +10 guards py / +5
  C dip offset; deltas +2/+4/+6 every method).
- TRUE-uniform chain: b458 NOT uniform (S1
  DIFFERS-from-own-C10 sig 0c-vs-0d, [46x10]
  with b0 in diff) -- record stays 32. No new
  SAMESIG-same-sig even case (P338 dispute stays
  DEFERRED to sweep accounting).
- S-F tables-lag: b458 even band sheet!=code
  (impl 78/82/75/69 == A-937 excl; sheet INCL
  79/83/75/69; PBA/C10 lag, quad/T exact) --
  42nd consecutive tables-lag; even sub-streak
  24th (GATE-counted; PBA b5-const deducted, T
  b0-in-table + b5-counter in VPOS).
- Next-P351 banked (A-937 Q1 + Q-1062 agree,
  for b459 to CONSUME FIRST): PB0 @138885 sig
  ae40e406 NEW-sig 1B-off (31/84 vs P350PB0) +
  PB1 @138886 sig 0d000000 NEW-sig (69/88 vs
  P350PB1) + PBA dc000000 x16 + C10-region
  0d000000 x10 SAME-as-PB1 (FWD-check in GATE-
  cbae1809 corroborated all four vs 4934f9d3
  lane code -- still re-verify at consume time
  per bank-miss lesson).
- Shared-x3 (chain-level): memo phrase "QM
  shared 16/16 x3 vs row0 NO frags" (A-937 Q2)
  verified 48/48 from oracle bytes for P350-QM9
  (lanes 51-55,80-83 col-only indexing + NO
  frags from oracle data, all 9 lanes x3 q-rows
  x16 cells). Memo phrase family holds, NOT a
  slip.

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 1 mild GATE obscurity (not a
slip): "AC-QC both=71 sameval=55" -- 55
verifies as shared (b,v) pairs; "both=71"
uninterpretted, recorded. Code GREEN since
gated artifact == verified artifact. Viewer
scars: none this band (1st full-green run, 0
seat-script fixes; RC-b1 assert added
first-hand, no run needed).
