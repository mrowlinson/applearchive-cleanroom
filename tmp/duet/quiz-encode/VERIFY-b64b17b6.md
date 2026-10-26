# VERIFY-b64b17b6 b454 T10P346 pins 137145..137492 (348 pins) PASS

Seat viewer-r71, first-hand, tree @b64b17b6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r71.
Base 3672d433 (b453 tip, 2058 tiers sealed; this
seat's VERIFY-3672d433 PASS-filed same round,
base-use only, respected). Band = f6c7385a (py
merge w2b@220b7680 partial, +6 tiers, +62 pins;
commit msg verified via git log) + b64b17b6 (C
port; parent == f6c7385a verified). Trees via git
archive to TMPDIR tree-sha dirs; tests run from
NVME workdirs (no WT src/__pycache__).

Banked Next-P346 shape (VERIFY-3672d433 §Next-
P346: A-924 Q1 + A-1057 Q1 agree) CONSUMED FIRST
and VERIFIED first-hand EXACT: PB0 adcf0b07
@137145 (S0 head; SAME-sig-as-P345PB0, 32/84
diff) + PB1 0e000000 @137146 (S1 head; NEW-sig,
60/88 diff vs P345PB1; 29/88 vs own C10[0]
n137163, SAME-as-own-C10) + PBA ed000000 x16
@137147-162 (AC b0-3 = ed/00/00/00) + C10-region
0e000000 x10 @137163-172 (CC b0-3 = 0e/00/00/00,
SAME-as-PB1-sig) -- all corroborated against lane
code before any battery step (no bank-miss).

- Build: cc -O2 -Wall -Wextra -std=c11 via
  src/c/Makefile, seat-private
  BUILDDIR=$R/build454 aae rgramc, rc=0,
  0 warnings, build454/{aae,rgramc}. aae sha256
  d6e27c97... (pinned stable continues; band
  touches no aae sources per numstat). rgramc
  sha256 c0570f1f... == GATE.
- RGRAMC-PYID 10307/10307 covered=10307/10307
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR set).
- RGRAM py 20614/20614 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 20614/20614 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (ordered identical +
  raw-order identical, 20614/20614; cmp454.py;
  GATE claims sorted only, raw corroborated
  too).
- PINS-RGRAM cells set-eq 20614/20614 (xor 0,
  PASS-N vs PINS-N); PINS N set vs for-list
  10307/10307 xor 0; PINS 20616 lines (2 hdr +
  20614, +62 vs base 20554; +62 = 31 for-Ns x2;
  4-way set-eq, seteq454.py GREEN 16/16, 2nd run
  -- 1st run caught the seat-script adapt miss
  base-pins 20490 vs 20552, fixed, re-greened).
  For-list union delta vs base +31/-0 (10276->
  10307): 137145 137146 137147 137148 137154
  137155 137161 137162 137163 137164 137167
  137168 137171 137172 137173 137188 137189
  137204 137205 137215 137216 137220 137221
  137236 137237 137343 137344 137408 137471
  137472 137492 (== GATE sampled list EXACT).
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6:
  head pair 137147/137148 off0/1, pair
  137154/137155 off7/8, tail pair 137161/137162
  off14/15) + C head/mid/tail pairs (6:
  137163/137164 off0/1, mid pair 137167/137168
  off4/5, tail pair 137171/137172 off8/9) + Q
  head/off15/off16/pair/edge-pair/pair/tail
  (10: head 137173 off0, 137188 off15, 137189
  off16, pair 137204/137205 off31/32, EDGE pair
  137215/137216 off42/43 (b5 edge r2c10/c11
  first-hand), pair 137220/137221 off47/48,
  tail 137236 off63; NO mid -- b5 edge, not
  const) + R head/edge-pair/mid/edge-pair/tail
  (7: head 137237 off0, edge pair 137343/137344
  off106/107, mid 137408 off171, edge pair
  137471/137472 off234/235, tail 137492
  off255).
  PINS-new-N == for-added 31/31, PINS removed 0.
  PINS numstat 62/0 clean append (all in py-merge
  leg 3672d433..f6c7385a; C-port leg touched
  zero PINS rows); all 20614 rows
  test_rgram_fast.py-tagged; cols1-4 purity
  +62/-0, cols5-7 uniform first-hand; added-row
  names == for-added 31/31.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  no oracle).
- Tables audit own script tabaudit454.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 131 PASS 0 FAIL (2nd run -- 1st run
  caught the seat-script RC-missing literal
  unsorted; set identical, reordered,
  re-greened; asserts derived from GATE shape
  throughout: no cloned-shape asserts).
  Inventory exactly the 12 both sides, C==py
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42, no RT/TT, no QT).
  S0 168ch sig adcf0b07 SAME-sig-as-P345PB0
  (32/84 payload diff vs P345S0 first-hand, NOT
  byte-equal) / S1 176ch sig 0e000000 NEW-sig
  (60/88 payload diff vs P345S1 n136798
  first-hand, NOT byte-equal; 29/88 diff vs
  own-C10[0] assembled n137163, NOT byte-equal;
  sig SAME-as-own-C10 0e-vs-0e; differs vs own
  PB0 adcf0b07),
  staged as full-payload singletons.
  AM 16/16 14ch distinct, CM 10/10 6ch
  distinct, M 16/16 16ch distinct, QR 4/4 8ch
  distinct UNPAIRED (R4 rows r0 9437b852 / r1
  b437b852 / r2 d437b852 / r3 ae291d7d exact
  tuples; r012 TRUE-3B 37b852 + r3 trailing-
  suffix lcs 0 vs all (anchored): suffix-lcs
  (01,02,03,12,13,23) = 3/3/0/3/0/0 +
  subseq-lcs 3/3/0/3/0/0 + tshare 3/3/0/3/0/0
  all-3 agree first-hand (== A-1058 Q2); r3
  ae291d7d unequal full tuple; b87 NOT-const
  {52,7d} quad-wide),
  RM 16/16 16ch distinct, RQ 16/16 16ch
  distinct, no QT (quad tails = R4 b84-87 full
  tuples) + no RT (SPLIT tails) + no F (no
  frags). M-vs-RQ ORDERED-IDENTICAL (M 8B
  b28-31,80-83 by COL vs RQ 8B b28-31,76-79 by
  ROW; agree all 8 lanes 16/16 each; tabs
  byte-identical element-wise; full-row sets
  EQUAL; M list == RQ list) -- 44th even-band
  RQ==M instance, even ordered-identical degree;
  same-lanes + full-row sets EQUAL => ordered
  per lesson (d); width predictor dead, never
  cited. AC 79, CC 83, QC 74, RC 70; C _N decls
  79/83/74/70 match actual; byte-coverage
  unions exact every block (88/88/88/88,
  0 overlap gap-free, M/R-tab computed).
  PBA88-PLAIN-M7b20 sig ed000000 (b0 const ed
  via AC b0-3; AM 16/16 distinct NO pair; M7
  b20,21,22,80-83; A-b5set {0x2f} const
  first-hand). C10-1SIG-88-TAIL-M3 sig 0e000000
  x10 SAME-as-PB1-sig (sig in CC b0-3 consts;
  CM 10/10 diverge 6ch b84-86; b87 const 52 in
  CC; CC has no b84-86 (all in CM lane) and no
  b5, b5 const 2f full block via lencode --
  C-b5set {0x2f} const first-hand).
  QUAD88-1SIG-QM8/R4-B5EDGE 1-sig ed000000 x64
  SAME-sig-as-PBA (b0 const ed in QC, b1-3
  const 00; b5 edge 2f->30 @off42/43 emergent
  from raw lencode NOT in QC const table
  (deducted, in VPOS); b4 base 0xab step2 64/64
  contig+2 range ab..ff,01..29; QM8 b28-31,
  80-83 16/16 col-indexed (m = off&15 both
  sides) shared-x3-vs-row0 48/48 oracle (see
  tabaudit454 shared-x3) NO frags + R4 b84-87
  rows above 4/4 UNPAIRED BY-ROW const
  (q = off>>4 both sides); tails full tuples
  4/4 distinct (r012 TRUE-3B 37b852 + r3 lcs 0
  vs all (anchored)); b87 NOT-const {52,7d};
  NO frags).
  Ring STANDARD-split: sig c90d0000 x256;
  code-TM8 b19,27,34,35,80-83 by COL RM 16/16 +
  code-TR8 b28-31,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79
  row); b0 const c9 (deducted; in RC table);
  b1 const 0d (256/256 oracle); b84-87 const
  ce291d7d ring-wide NEW (256/256 oracle).
  VPOS partitions re-derived from code: PBA 8
  (missing 9 - deduct const-b5; b4+M7) / C10 4
  (missing 5 - 1; b4+M3, b5 const, b87 const
  in-table) / quad 14 (missing 14 - 0; b4,b5-
  edge+QM8+R4, b5 edge-varies in VPOS) / T 18
  (missing 18 - 0; b4,b5+TM8+TR8, b0 const
  lives in-table, b5 counter-varies in VPOS) --
  all match A-925 (missing sets AC-9
  [4,5,20-22,80-83] / CC-5 [4,5,84-86] / QC-14
  [4,5,28-31,80-87] / RC-18
  [4,5,19,27-31,34,35,76-83] first-hand EXACT;
  deduct-const-b5-or-in-table convention holds;
  b5 variance checked from oracle bytes: A
  {2f}, C {2f}, Q {2f,30}).
  Code-consts vs A-925 INCL (PBA 80 / C10 84 /
  quad 74 / T88 70): impl 79/83/74/70 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead)
  while A-925/A-1058 sheets count b5 (memo
  confirms the sheet INCL values) -- S-F
  arithmetic persists in committed tables
  though the sheets are FIXED; memo-exact on
  quad (b5 edge-varies, in VPOS, no deduction)
  and T88 (b5 counter-varies, in VPOS, no
  deduction); geometry exact, PORT verdict
  stands; FLAGGED for memo (GATE-counted 22nd
  even band running: 40th tables-lag instance;
  PBA/C10 lag this tier).
  QUAD 1SIG ed SAME-sig-as-PBA this tier; PBA
  sig ed NEW vs P345 c5; AC-QC positional
  both=71 sameval=50 corroborated first-hand
  (71 shared byte positions, 50 same-value;
  tables differ).
  M-tails 16/16 ALL NEW vs P345T RM col-led
  tails (zero overlap vs P345T tails first-
  hand).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P345
  (all 0/16; widths P346 vs P345: AM 7B vs 6B,
  CM 3B vs 4B, M 8B vs 9B, QR 4B vs 4B, RM 8B
  vs 6B, RQ 8B vs 9B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 137145 / S1 137146 / A 137147-162 /
  C 137163-172 / Q 137173-236 / R 137237-492):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C b5 const 2f emerges
  from raw lencode; Q b5 edge 2f->30 emerges
  64/64) + R explicit counter (b4=(0x2b+2off)&
  FF b5=0x30+(off>=107)+(off>=235); py hex
  0x2b/0x30; C staged literals 43/48/107/235
  re-derived: 43==0x2b, 48==0x30) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 14ch b20-22,
  80-83; C 6ch b84-86 + b87-const-52; Q 16/8ch
  b28-31,80-83/b84-87; R 16/16ch TM8 b19,27,34,
  35,80-83 by COL / TR8 b28-31,76-79 by ROW).
  C blocks carry T92114/92119/92124/92139/92154/
  92174 py-line cites (each re-read: hits the
  exact py guard line, C comment text matches
  py, all 6 present; bounds + byte positions
  exact (A 14ch, C 6ch, Q 16/8ch, R 16/16ch)).
  A/C raw lencode (no counter literals) +
  Q b5-edge emergent + R counter
  b4=(0x2b+2off)&FF + (off>=107)+(off>=235) (C
  literals 43/48/107/235 verified), temps
  _t6989-7004 (base max _t6988, no reuse) +
  _i4237/4239/4242/4245 (base max _i4235, no
  reuse) + _b4236/4238/4240/4241/4243/4244
  (base max _b4234, no reuse), all 6 blocks
  verified. Insert position exact both sides:
  after T10P345R close (C 244923, comment
  244926, S0 block; py CLOSED + return + S0
  guard 92114), at dispatch tail
  (N-out-of-scope fallthrough follows: C 245105,
  py 92193; early same-text guards at C 165350 /
  py 57040 are the plateau n<=1077 check,
  unrelated scope).
  Matches A-925 geometry (PB0 SAME-sig-as-P345
  32/84; PB1 NEW-sig 60/88 SAME-as-C10 29/88;
  PBA88-PLAIN-M7b20 VPOS 8 sig-ed b5 const 2f
  M7 16/16 distinct; C10-1SIG-88-TAIL-M3 VPOS 4
  SAME-as-PB1-sig b5 const M3 10/10 diverge +
  b87-const-52; QUAD88-1SIG-QM8/R4-B5EDGE VPOS
  14 + R4 4/4 UNPAIRED exact tuples + r012-
  TRUE-3B + r3-lcs0 + b87-notconst + QM8-
  shared-x3 + NO frags + b5-edge + M-tails NEW;
  T88-STANDARD-split VPOS 18 + TM8-by-COL/TR8-
  by-ROW + SPLIT-tails + b0-const-deducted +
  b1-0d + b84-87 ce291d7d + counter 2b/30/107/
  235; lencode 348/348 whole-tier, NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R4
  rows + tails + LCS + STANDARD frame + consts
  stand; sheet-vs-tables const-count note is
  S-F arithmetic in tables only per memo,
  geometry unaffected; M==RQ 16/16 string-
  identical same-order first-hand this tier,
  tier stands).
- Edges own-loop ownloop454.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P346R N=137492 off=255.
  edges454.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  73/2f, 75/2f == raw lencode) + aform 16/16 (A
  head 77/2f tail 95/2f b5set {2f} NO step, 0
  ff) + cform 10/10 (C head 97/2f tail a9/2f
  b5set {2f} NO step, 0 ff) + qform 64/64 (Q
  head ab/2f edge off42->43 (137215->137216)
  ff/2f->01/30 tail 29/30; b5set {2f,30} (2f
  offs 0-42, 30 offs 43-63); quad b4=(0xab+2off)
  64/64 contig+2 range ab..ff,01..29) + qb5edge
  64/64 + ring counter 256/256 + ringraw 256/
  256 (head 2b/30; mid off171 81/31 @137408;
  off106/107 (137343->137344) ff/30->01/31;
  off234/235 (137471->137472) ff/31->01/32;
  tail off255 29/32 @137492; exactly 3 ff in
  348: Q-edge-ff + 2 ring-edge-ff) + b0 const
  c9 256/256 + b1 const 0d 256/256 + b84-87
  const ce291d7d 256/256 (all from oracle bytes
  first-hand).
  Odd-lencode 348/348 (346 + S0/S1 embedded).
  Ring edges + mid + tail 137492 in for-list +
  2 PASS lines each py+C. Tail 137492: oracle
  rav sha 5fd14f45... == PINS (match True;
  rawlen 104); py+C CLOSED T10P346R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf454.py (cache path, 0 miss-warmed
  after ownloop) + secf454b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (137145 +
  136797 + 137146 + 136798); S0: oracle137145-
  vs-136797 32/84, codeS0-vs-P345S0 32/84,
  positions identical; DIRECT 32/84 agree.
  S1: oracle137146-vs-136798 60/88, codeS1-vs-
  P345S1 60/88, positions identical, sig b0 NEW
  (NEW-sig 0e vs 0c); DIRECT 60/88 agree.
  Triple-derived both pairs (S0 SAME-sig +
  S1 NEW-sig, staged novelty both tiers).
  S1-vs-own-C10 secf454c.py (staged assembly vs
  oracle C10 cells n137163-172: 10/10 byte-
  equal; staged S1 vs staged cells): [29x10]
  TRUE UNIFORM staged+oracle, cells0-9
  positions identical (cell0 pos 4,8-11,16-31,
  60-63,84-87 == staged EXACT; sig b0-3
  same-sig NOT in diff), sig 0e000000 all, NOT
  byte-equal. UNIFORM -- 18th TRUE-uniform case
  in sweep accounting, 29-wide; NEW-sig S1 +
  EVEN band (parity half of novelty/parity rule
  challenged; adjudication DEFERRED to sweep
  accounting, evidence on file).
  Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  232/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; band
  added lines 903 first-hand (== numstat sums
  608+232+1+62); rgramc.c splits 603 content +
  5 bare-blank (exactly `+`, verified 0 ws-only)
  = 608 == numstat; GATE states raw C 898
  content + 5 bare-blank (898+5 = 903 exact) --
  evens-correct, no overcount (odds overcount
  count stays 13). Code GREEN since gated
  artifact == verified artifact.
- Wall on band diff added lines (scope 3672d433..
  b64b17b6, 903 added lines first-hand): vendor
  0 hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits, aea-invoke 0 hits. Files: rgramc.c
  608/0, rgram.py 232/0 purely additive,
  test_rgram.sh 1/1 (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1964->1970 +6, dispatch
  singletons (4sp) 714->716 +2 / range-guards
  (4sp) 814->818 +4 = +6, C singletons 719->721
  +2 (4sp 714->716 + 5 dip-guard offset) /
  ranges 836->840 +4 = +6, CLOSED T10P prints
  1964->1970 +6 both sides, seal 2058->2064 +6
  (commit msgs; offset +94 vs CLOSED-T10P, stable
  b401-b454). All agree (stated literal methods
  first-hand: 4sp py / file-wide py 724->726 =
  4sp + 10 non-dispatch early-tier guards; C
  file-wide 719->721 = 4sp + 5; C ranges == py
  file-wide 836->840; deltas agree every side).
  No elif either side (py file-wide elif 50->50,
  C else-if 0->0; A/C/Q use raw lencode, no
  counters).
- CONFIRM evidence (CONVERT-01 rule b): A-925-
  q1058-P346 verdict CONFIRM 51/51 CLEAN (own
  beds r4-P346 137145..137520 + r4-P345 cross-
  refs, BAD=0, direct-oracle spot 4/4 byte-match;
  verifier v306.py P346 51/51 PASS; file
  present, counts verified; tier GATED PORT;
  novelty gated M-tails 16/16 ALL NEW vs P345T
  RM col-led tails; exact-value corroboration
  incl PB0 SAME-sig 32/84, PB1 NEW-sig 60/88
  SAME-as-own-C10 29/88, PBA16 sig-ed VPOS 8,
  C10 sig-0e SAME-as-PB1 VPOS 4 (CM 10/10
  diverge 6ch b84-86 + b87-const-52), QUAD64
  1-sig-ed SAME-as-PBA + R4 rows +
  r012-TRUE-3B + r3-lcs0 + b87-notconst +
  QM8 + NO frags + b5-edge + M-tails NEW, T256-
  STANDARD + TM8-by-COL/TR8-by-ROW +
  SPLIT-tails + b0-c9 + b1-0d + const ce291d7d
  + counter/edges; plus sheet-vs-tables
  const-count note: A-925 sheet 80/84/74/70
  memo-exact, committed tables 79/83/74/70
  still deduct const-b5 on PBA/C10 -- S-F
  arithmetic in tables only, geometry exact,
  PORT verdict stands) + A-1058-q1058-P346
  verdict CONFIRM 46/46 CLEAN (own bed r6-P346
  137145..137520, 376 cells + r6-P345 cross-
  refs, BAD=0; verifier v600f3.py P346 46/46
  PASS; file present, counts verified; tier
  GATED PORT; suffix-lcs 3/3/0/3/0/0 (all-3
  corroborated first-hand) + M-tails NEW + STD
  frame + consts excl 79/83/74/70
  script-claimed corroborated; w2b-r30 7/8,
  cited from body read first-hand). Agrees with
  cport commit msg (PYID 10307, RGRAM 20614).
  No viewer P346 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b454/
  b64b17b6 (quiz poll + filename grep first-
  hand; later-GATE b454 mentions are base-use
  only; zero FLAG hits on T10P346; odd base
  b453 respected; no future turf touched; CLAIM
  at brief path tmp/duet/). PROSE-01: all hex/
  counts above copied from own run output;
  GATE-b64b17b6 re-read in FULL before filing
  (zero GATE slips this band: raw-C stated
  correctly, temps exact, wall scope 903 exact).
- RQ==M chain: b454 even ORDERED-IDENTICAL (M
  8B vs RQ 8B: agree all 8 lanes 16/16 each;
  tabs byte-identical element-wise; full-row
  sets EQUAL; M list == RQ list) -- 44th
  even-band RQ==M instance; same-lanes +
  full-row sets EQUAL => ordered per lesson
  (d); width predictor dead, never cited.
  Viewer-vs-sweep convention reconciled
  first-hand (4sp-dispatch-exact both sides;
  file-wide +10 guards py / +5 C dip offset).
- TRUE-uniform chain: b454 UNIFORM [29x10]
  SAMESIG (staged+oracle, positions identical).
  Record 30->31. 18th case, 29-wide (NEW-sig
  S1 + EVEN band -- parity half of novelty/
  parity rule challenged; adjudication
  DEFERRED to sweep accounting, evidence on
  file; no new SAMESIG-same-sig even case --
  P338 dispute untouched).
- S-F tables-lag: b454 even band sheet!=code
  (impl 79/83/74/70 == A-1058 excl; sheet INCL
  80/84/74/70 per A-925) -- 40th consecutive
  tables-lag; even sub-streak 22nd (GATE-
  counted; PBA/C10 lag, quad/T exact).
- Next-P347 banked (A-925 Q1 + A-1058 Q1 agree,
  for r72 to CONSUME FIRST): PB0 @137493 sig
  ef496f07 NEW (31/84 vs P346PB0) + PB1 @137494
  sig 0d000000 NEW (51/88 vs P346PB1) + PBA
  e8000000 x16 + C10-region 0d000000 x10
  SAME-as-PB1 (memo-derived; lane-code verify
  pending at CONSUME time per bank-miss lesson;
  FWD-check this VERIFY corroborated all four
  vs b94eec82 lane code).
- Shared-x3 (chain-level): memo phrase "QM
  shared x3 16/16 vs row0 NO frags" (A-925 Q2)
  verified 48/48 from oracle bytes for P346-QM8
  (SHAREDX3-style check inside tabaudit454
  GREEN) -- proves col-only indexing + NO frags
  from oracle data. Memo phrase family resolved,
  NOT a slip.

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; zero GATE prose notes (raw-C
stated correctly: 898+5=903 exact; temps exact;
wall scope 903 exact). Code GREEN since gated
artifact == verified artifact. Viewer scars
(2 seat-script, both caught pre-file): seteq
adapt miss (base-pins assert left at 20490,
fixed to 20552, re-greened) + tabaudit
RC-missing literal unsorted (set identical,
reordered, re-greened).
