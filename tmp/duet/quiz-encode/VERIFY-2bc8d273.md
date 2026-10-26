# VERIFY-2bc8d273 b455 T10P347 pins 137493..137840 (348 pins) PASS

Seat viewer-r71, first-hand, tree @2bc8d273,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r71.
Base b64b17b6 (b454 tip, 2064 tiers sealed; this
seat's VERIFY-b64b17b6 PASS-filed same round,
base-use only, respected). Band = b94eec82 (py
merge w2b@6ddee87a partial, +6 tiers, +58 pins;
commit msg verified via git log) + 2bc8d273 (C
port; parent == b94eec82 verified). Trees via git
archive to TMPDIR tree-sha dirs; tests run from
NVME workdirs (no WT src/__pycache__).

Banked Next-P347 shape (VERIFY-b64b17b6 §Next-
P347: A-925 Q1 + A-1058 Q1 agree) CONSUMED FIRST
and VERIFIED first-hand EXACT: PB0 ef496f07
@137493 (S0 head; NEW-sig NEW family, 31/84
diff vs P346PB0) + PB1 0d000000 @137494 (S1
head; NEW-sig, 51/88 diff vs P346PB1; 26/88 vs
own C10[0] n137511, SAME-as-own-C10) + PBA
e8000000 x16 @137495-510 (AC b0-3 = e8/00/00/
00) + C10-region 0d000000 x10 @137511-520 (CC
b0-3 = 0d/00/00/00, SAME-as-PB1-sig) -- all
corroborated against lane code before any
battery step (no bank-miss).

- Build: make -C tree/src/c BUILDDIR=$R/build455
  aae rgramc, rc=0, 0 warnings, build455/{aae,
  rgramc}. aae sha256 d6e27c97... (pinned stable
  continues; band touches no aae sources per
  numstat). rgramc sha256 8bce9c44... == GATE.
- RGRAMC-PYID 10336/10336 covered=10336/10336
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, CT_CACHE_DIR
  default NVME).
- RGRAM py 20672/20672 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  default NVME, NVME workdir).
- RGRAM C 20672/20672 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (20672/20672, sorted;
  cmp455.py; GATE claims sorted only, raw
  corroborated too -- sorted-equal True +
  raw-identical True first-hand).
- PINS-RGRAM cells set-eq 10336/10336 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq455.py GREEN 16/16, 2nd run -- 1st run
  caught the seat-script adapt miss for-added
  count 31 vs 29, fixed, re-greened; EXP_ADDED
  list itself P347-correct, verified pre-run).
  PINS 20674 lines first-hand (2 hdr + 20672
  rows; base 20616 lines / 20614 rows; line
  delta +58 = row delta +58 = 29 for-Ns x2;
  GATE states "+60 vs base 20614" = 20674-20614
  = 60 mixed lines-vs-rows arithmetic, off by
  2: mild GATE prose slip, substance exact).
  For-list union 10307->10336 +29/-0 (python
  sets, trailing-';' strip, never comm): 137493
  137494 137495 137496 137502 137503 137509
  137510 137511 137512 137515 137516 137519
  137520 137521 137536 137537 137552 137553
  137568 137569 137584 137585 137599 137600
  137664 137727 137728 137840 (== GATE sampled
  list EXACT).
  29 = 2 sing (137493 137494) + A 6 (head
  137495 + 137496 + pair 137502/137503 + pair
  137509/137510 tail; offs 0,1,7,8,14,15; offs
  2-6,9-13 unsampled: 137497-501, 137504-508)
  + C 6 (head 137511 + 137512 + 137515 + 137516
  + 137519 + tail 137520; offs 0,1,4,5,8,9;
  offs 2,3,6,7 unsampled: 137513, 137514,
  137517, 137518) + Q 8 (head 137521 +
  boundary pairs 137536/137537 + 137552/137553
  + 137568/137569 + tail 137584; offs 0,15,16,
  31,32,47,48,63; NO mid (b5 const NO edge),
  all boundaries pair-covered, first-hand) + R
  7 (head 137585 + edge pair 137599/137600 +
  mid 137664 + edge pair 137727/137728 + tail
  137840; offs 0,14/15,79,142/143,255; 1-mid
  shape off79 NEW, both counter edges pair-
  covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  20672-20614.
- SMOKE-GREEN rc=0 (2nd run -- 1st run botched
  $R in my shell, log path read-only; reran
  correctly; 6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  no oracle).
- Tables audit own script tabaudit455.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 128 PASS 0 FAIL first full-green run
  (asserts derived from GATE shape throughout:
  novelty-first band, never cloned-shape
  asserts).
  Inventory exactly the 12 both sides, C==py
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no M42/X42/
  H42/L42, no QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ef496f07 NEW-sig NEW family (31/
  84 payload diff vs P346S0 @ b0-2,4-11,13-19,
  24,56-63,80-83 first-hand incl sig b0-2, NOT
  byte-equal) / S1 176ch sig 0d000000 NEW-sig
  (51/88 payload diff vs P346S1 @ b0,4,5,8-11,
  16-43,60-71,84-87 first-hand incl sig b0,
  NOT byte-equal; vs own C10 cells NOT UNIFORM
  26x9+25x1 staged+oracle -- odd-cell5 k5
  n137516 missing b84 from diff (CM[5][0]=0x9e
  ==S1[84] m-lane coincidence in exactly one
  cell); sig b0-3 same-sig NOT in diff; NOT
  byte-equal; oracle triple in secf455c;
  novelty-first: uniformity never assumed,
  GATE-shape-derived),
  staged as full-payload singletons.
  AM 16/16 8B distinct, CM 10/10 4B distinct,
  M 16/16 9B distinct, QR 4/4 4B distinct
  UNPAIRED (R4 rows r0 3e34f1c8 / r1 5e34f1c8 /
  r2 7e34f1c8 / r3 3d6e3bca exact tuples; r012
  TRUE 3B 34f1c8 + r3 trailing-suffix lcs 0 vs
  all (anchored): suffix-lcs (01,02,03,12,13,
  23) = 3/3/0/3/0/0 + subseq-lcs 3/3/0/3/0/0 +
  tshare 3/3/0/3/0/0 all-3 agree first-hand (==
  A-926 Q2 + A-1059 Q2); r3 3d6e3bca unequal
  full tuple; b87 NOT-const {c8,ca} quad-wide),
  RM 16/16 7B distinct, RQ 16/16 8B distinct,
  no QT (R4 b84-87 inside QR) + no RT (ring,
  not ROWTAIL) + no F (no frags). M-vs-RQ 4OF6
  (M 9B b30,38,39,46,47,80-83 by COL vs RQ 8B
  b40,41,46,47,76-79 by ROW; 6 comparable cols
  = 2 shared + 4 tail-correspondent; tails
  (80,76),(81,77),(82,78),(83,79) 16/16
  position-exact; tail SETS EQUAL (overlap
  16/16); shared b46/b47 0/16 each FULLY
  DISJOINT; M-only b30,38,39 / RQ-only b40,41
  no counterpart) -- 45th odd-band RQ==M
  instance, FIRST 4OF6 degree (no 9B-vs-8B
  degree on file; full shape-name survey
  first-hand); ordered per lesson (d) (tails
  position-exact + tail-sets EQUAL, cf P341
  8OF9); width predictor dead, never cited. AC
  78, CC 82, QC 73, RC 71; C _N decls 78/82/
  73/71 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed). PBA88-PLAIN-
  M8b40 sig e8000000 (b0 const e8 via AC b0-3;
  AM 16/16 distinct NO pair; M8 b40-43,80-83;
  A-b5set {0x32} const first-hand).
  C10-1SIG-88-TAIL-M4 sig 0d000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 full-sig
  consts; CM 10/10 diverge 4B b84-87; b5 const
  32 full block via lencode; C-b5set {0x32}
  const first-hand).
  QUAD88-1SIG-QM9/R4-NOEDGE 1-sig e8000000 x64
  SAME-sig-as-PBA (b0 const e8 in QC, b1-3
  const 00; b5 const 32 NO edge full block via
  raw lencode; b4 base 0x63 step2 64/64
  contig+2 range 63..e1 NO wrap, 64 distinct;
  QM9 b30,38,39,46,47,80-83 16/16 col-indexed
  (m = off&15 both sides) shared-x3-vs-row0
  48/48 oracle (see tabaudit455 shared-x3) NO
  frags + R4 b84-87 rows above 4/4 UNPAIRED
  BY-ROW const (q = off>>4 both sides); tails 4
  distinct (r012 TRUE-3B 34f1c8 + r3 lcs 0 vs
  all (anchored)); b87 NOT-const {c8,ca}; NO
  frags).
  Ring STANDARD-split: sig 680d0000 x256;
  code-TM7 b52-54,80-83 by COL RM 16/16 +
  code-TR8 b40,41,46,47,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79
  row); b0 const 68 (256/256 oracle, in RC
  table); b1 const 0d (256/256 oracle); b84-87
  const 5d6e3bca ring-wide NEW (256/256
  oracle).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - deduct const-b5; b4+M8) / C10 5
  (missing 6 - 1; b4+M4, b5 const) / quad 14
  (missing 15 - 1; b4+QM9+R4, b5 const) / T 17
  (missing 17 - 0; b4,b5+TM7+TR8, b0 const
  lives in-table, b5 counter-varies in VPOS) --
  all match A-926 (missing sets AC-10
  [4,5,40-43,80-83] / CC-6 [4,5,84-87] / QC-15
  [4,5,30,38,39,46,47,80-87] / RC-17
  [4,5,40,41,46,47,52-54,76-83] first-hand
  EXACT; deduct-const-b5-or-in-table convention
  holds; b5 variance checked from oracle bytes:
  A {32}, C {32}, Q {32}).
  Code-consts vs A-926 INCL (PBA 79 / C10 83 /
  quad 74 / T88 71): impl 78/82/73/71 =
  memo-exact (A b5 const 32, C b5 const 32, Q b5
  const 32 deducted; T counter, no deduction)
  = 79/83/74/71 INCL; A-1059 excl 78/82/73/71
  = code EXACT -- no lag on odd band. VPOS
  9/5/14/17 = memo EXACT.
  M-tails 16/16 ALL NEW vs P346T RM col-led
  tails (overlap 0; P346T RM8 frame first-hand
  from code, ref = RM8 8B rows, position-aware
  tails last-4B) + RQ-tails (b76-79) 16/16 ALL
  NEW vs P346T RQ row-led tails (overlap 0).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P346
  (all 0/16; widths P347 vs P346: AM 8B vs 7B,
  CM 4B vs 3B, M 9B vs 8B, QR 4B vs 4B, RM 7B
  vs 8B, RQ 8B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 137493 / S1 137494 / A 137495-510 /
  C 137511-520 / Q 137521-584 / R 137585-840):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C/Q b5 const 32
  emerges from raw lencode) + R explicit
  counter (b4=(0xe3+2off)&FF b5=0x32+(off>=15)+
  (off>=143); py hex 0xe3/0x32; C staged
  literals 227/50/15/143 re-derived: 227==0xe3,
  50==0x32) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 8B b40-43,80-83; C 4B
  b84-87; Q 9B/4B b30,38,39,46,47,80-83/
  b84-87; R 7B/8B SPLIT TM7 b52-54,80-83 by COL
  / TR8 b40,41,46,47,76-79 by ROW). C blocks
  carry T92345/92350/92355/92370/92385/92406
  py-line mirrors (each re-read: hits the exact
  py guard line, C comment text matches py, all
  6 present; bounds + byte positions exact).
  A/C/Q raw lencode (no counter literals) + R
  counter b4=(0xe3+2off)&FF + (off>=15)+
  (off>=143) (C literals 227/50/15/143
  verified), temps _t7005-7020 (base max _t7004,
  no reuse) + _i4247/4249/4252/4255 (base max
  _i4245, no reuse) + _b4246/4248/4250/4251/
  4253/4254 (base max _b4244, no reuse; union
  4246-4255 contiguous), all 6 blocks verified.
  Insert position exact both sides: after
  T10P346R close (C comment + S0 block; py
  CLOSED + return + S0 guard 92345), at dispatch
  tail (N-out-of-scope fallthrough follows: C
  scope hits 2, py 2 scope hits; early
  same-text plateau guard unrelated scope).
  Matches A-1059 geometry (PB0 NEW-sig NEW
  family 31/84; PB1 NEW 51/88 SAME-as-own-C10
  26/88 + differs-vs-own-PB0; PBA88-PLAIN-M8b40
  VPOS 9 b5 const 32; C10-1SIG-88-TAIL-M4 VPOS
  5 b5 const; QUAD88-1SIG-QM9/R4-NOEDGE VPOS 14
  + R4 4/4 UNPAIRED exact tuples + r012-3/r3-0
  + b0-const-SAME-as-PBA + b87-NOT-const + b5
  const NO edge + M-tails NEW; T88-RING-
  STANDARD-split VPOS 17 + TM7-by-COL/TR8-
  by-ROW + SPLIT-tails + b0/b1-const + b84-87
  5d6e3bca + counter e3/32/15/143; lencode
  348/348 whole-tier, NO D dips) + A-926
  (suffix-lcs 3/3/0/3/0/0 all 3 metrics +
  consts incl 79/83/74/71 lane EXACT) incl exact
  values (PBA/C10/QUAD/T88 sigs, R4 tuples +
  TRUE-3Bs + rest-0 + B5EDGE... b5-const-NOEDGE
  + consts stand).
- Edges own-loop ownloop455.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P347R N=137840 off=255.
  edges455.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  2b/32, 2d/32 == raw lencode) + aform 16/16 (A
  head 2f/32 tail 4d/32 b5set {32} NO step, 0
  ff) + cform 10/10 (C head 4f/32 tail 61/32
  b5set {32} NO step, 0 ff) + qform 64/64 (Q
  head 63/32 tail e1/32; b5 const 32 64/64 NO
  edge; quad b4=(0x63+2off) 64/64 contig+2
  range 63..e1 NO wrap, 64 distinct) + qb5const
  64/64 + ring counter 256/256 + ringraw 256/
  256 (head e3/32; mid off79 81/33 @137664;
  off14/15 (137599->137600) ff/32->01/33;
  off142/143 (137727->137728) ff/33->01/34;
  tail off255 e1/34 @137840; exactly 2 ff in
  348, both ring-edge) + b0 const 68 256/256 +
  b1 const 0d 256/256 + b84-87 const 5d6e3bca
  256/256 (all from oracle bytes first-hand).
  Odd-lencode 348/348 (346 + S0/S1 embedded).
  Ring edges + mid + tail 137840 in for-list +
  2 PASS lines each py+C. Tail 137840: oracle
  rav sha 4ab4a87a... == PINS (match True;
  rawlen 104); py+C CLOSED T10P347R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf455.py (cache path, 0 miss-warmed
  after ownloop) + secf455b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (137493 +
  137145 + 137494 + 137146); S0: oracle137493-
  vs-137145 31/84, codeS0-vs-P346S0 31/84,
  positions identical + GATE-exact, sig b0-2 IN
  diff (NEW-sig NEW family); DIRECT 31/84
  agree. S1: oracle137494-vs-137146 51/88,
  codeS1-vs-P346S1 51/88, positions identical +
  GATE-exact, sig b0 IN diff (NEW-sig); DIRECT
  51/88 agree. Triple-derived both pairs
  (S0 NEW family + S1 NEW-sig, staged novelty
  both tiers).
  S1-vs-own-C10 secf455c.py (staged assembly vs
  oracle C10 cells n137511-520: 10/10 byte-
  equal; staged S1 vs staged cells): 26/88 in 9
  cells + 25/88 in odd-cell5 (k5 n137516,
  CM[5][0]=0x9e==S1[84] m-lane coincidence
  removes b84 from diff; sig b0-3 same-sig NOT
  in diff), sig 0d000000 all, NOT byte-equal.
  NOT UNIFORM -- 26x9+25x1 (novelty-first:
  uniformity never assumed, GATE-shape-derived;
  chain TRUE-uniform stays 31).
  Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  232/0 (rgram.py) + 1/1 (for-line) + PINS +58/
  +0 (clean append, 29 Ns x2) == GATE; band
  added lines 899 first-hand (== numstat sums
  608+232+1+58); rgramc.c splits 603 content +
  5 bare-blank (exactly `+`, verified 0 ws-only)
  = 608 == numstat; GATE states raw C 608
  content + 5 blank (sums 613 vs numstat 608 --
  overcounts by 5: 14th raw-C overcount-by-5
  odds instance, odds pattern b429-b455). Code
  GREEN since gated artifact == verified
  artifact.
- Wall on band diff added lines (scope b64b17b6..
  2bc8d273, 899 added lines first-hand): vendor
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
  comments `# T10P` 1970->1976 +6, dispatch
  singletons (4sp) 716->718 +2 / range-guards
  (4sp) 818->822 +4 = +6, C singletons 721->723
  +2 (4sp 716->718 + 5 dip-guard offset) /
  ranges 840->844 +4 = +6, CLOSED T10P prints
  1970->1976 +6 both sides, seal 2064->2070 +6
  (commit msgs; offset +94 vs CLOSED-T10P, stable
  b401-b455). All agree (stated literal methods
  first-hand: 4sp py / file-wide py 726->728 =
  4sp + 10 non-dispatch early-tier guards; C
  file-wide 721->723 = 4sp + 5; C ranges == py
  file-wide 840->844; deltas agree every side).
  No elif either side (py file-wide elif 50->50,
  C else-if 0->0; A/C/Q use raw lencode, no
  counters).
- CONFIRM evidence (CONVERT-01 rule b): A-1059-
  q1059-P347 verdict CONFIRM 45/45 CLEAN (own
  bed r6-P347 137493..137868, 376 cells + r6-
  P346 cross-refs, BAD=0 + direct-oracle 2/2
  byte-match; verifier v600f3.py P347 45/45
  PASS; file present, counts verified; tier
  GATED PORT; suffix-lcs 3/3/0/3/0/0 (all-3
  corroborated first-hand) + M-tails NEW + STD
  frame + consts excl 78/82/73/71 script-
  claimed corroborated; w2b-r30 8/8 CAP, cited
  from body read first-hand) + A-926-q1059-P347
  verdict CONFIRM 50/50 CLEAN (own beds r4-P347
  137493..137868 + r4-P346 cross-refs, BAD=0,
  direct-oracle spot 4/4 byte-match; verifier
  v306.py P347 50/50 PASS; file present, counts
  verified; tier GATED PORT; novelty gated
  M-tails 16/16 ALL NEW vs P346T RM col-led
  tails + RQ-tails NEW; w2b-r30 8/8 CAP, cited
  from body read first-hand). Agrees with cport
  commit msg (PYID 10336, RGRAM 20672). No
  viewer P347 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b455/
  2bc8d273 (quiz poll + filename grep first-
  hand; b456-GATE b455 mentions are base-use
  only; zero FLAG hits on T10P347; even base
  b454 respected; no future turf touched; CLAIM
  at brief path tmp/duet/). PROSE-01: all hex/
  counts above copied from own run output;
  GATE-2bc8d273 re-read in FULL before filing
  (3 mild GATE prose notes: raw-C overcount-by-5
  14th odds instance; wall scope 840 vs
  first-hand 899 -- 840 = src-only 608+232, my
  wall covers the FULL band diff, 0 hits; PINS
  "+60 vs base 20614" = mixed lines-vs-rows
  20674-20614, true delta +58 lines / +58 rows).
- RQ==M chain: b455 odd 4OF6 (M 9B vs RQ 8B: 4
  tail-correspondent cols position-exact 16/16
  each; tail SETS EQUAL; shared b46/b47 0/16
  each FULLY DISJOINT; M-only b30,38,39 +
  RQ-only b40,41 no counterpart; M list != RQ
  list) -- 45th odd-band RQ==M instance, FIRST
  4OF6 degree (no 9B-vs-8B degree on file) +
  8th full-identity (7 on file); tails
  position-exact + tail-sets EQUAL => ordered
  per lesson (d), cf P341 8OF9; width predictor
  dead, never cited. Viewer-vs-sweep convention
  reconciled first-hand (4sp-dispatch-exact both
  sides; file-wide +10 guards py / +5 C dip
  offset).
- TRUE-uniform chain: b455 NOT uniform (S1
  SAME-sig but 26x9+25x1 with b84 coincidence
  in exactly one cell) -- record stays 31. No
  new SAMESIG-same-sig even case (P338 dispute
  stays DEFERRED to sweep accounting).
- S-F tables-lag: b455 odd band sheet==code
  (impl 78/82/73/71 == A-1059 excl; incl
  +1/+1/+1/+0 = 79/83/74/71 == A-926 INCL) --
  no lag on odds (deduct-b5-only-when-b5vary
  holds: Q b5 const deducted here since VPOS
  counts b4 only... b5 const lives out of VPOS;
  even sub-streak stays 22 (b454 last even).
- Next-P348 banked (A-926 Q1 + A-1059 Q1 agree,
  for r72 to CONSUME FIRST): PB0 @137841 sig
  ef49ef07 NEW 1B-off (33/84 vs P347PB0) + PB1
  @137842 sig 0d000000 SAME-as-P347PB1 (44/88
  vs P347PB1) + PBA d4000000 x16 + C10-region
  0f000000 x10 DIFFERS-from-PB1 (memo-derived;
  lane-code verify pending at CONSUME time per
  bank-miss lesson; FWD-check this VERIFY
  corroborated all four vs 0c8b1c76 lane code).
- Shared-x3 (chain-level): memo phrase "QM
  shared x3 16/16 vs row0 NO frags" (A-926 Q2)
  verified 48/48 from oracle bytes for P347-QM9
  (SHAREDX3-style check inside tabaudit455
  GREEN) -- proves col-only indexing + NO frags
  from oracle data. Memo phrase family resolved,
  NOT a slip.

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 3 mild GATE prose notes (raw-C
overcount-by-5 14th odds instance: 603 content
+ 5 bare-blank = 608 == numstat; wall scope 840
vs first-hand 899 -- 840 = src-only 608+232, my
wall covers the FULL band diff, 0 hits; PINS
"+60 vs base 20614" mixed lines-vs-rows, true
+58/+58). Code GREEN since gated artifact ==
verified artifact. Viewer scars (2 seat-script,
both caught pre-file): seteq adapt miss
(for-added count carried 31, fixed to 29,
EXP_ADDED list itself correct, re-greened) +
smoke shell slip ($R unset, log path read-only;
reran correctly, GREEN).
