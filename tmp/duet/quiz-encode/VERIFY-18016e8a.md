# VERIFY-18016e8a b441 T10P333 pins 132621..132968 (348 pins) PASS

Seat viewer-r68, first-hand, tree @18016e8a,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r68.
Base 825bee89 (b440 tip, 1980 tiers sealed; this
seat's VERIFY-825bee89 PASS-filed same round,
base-use only, respected). Band = bb0cac91 (py
merge w2b@5cc39f53 partial, +6 tiers, +62 pins;
commit msg verified via git log) + 18016e8a (C
port; parent == bb0cac91 verified). Trees via git
archive to TMPDIR tree441/tree441base; tests run
from NVME workdirs (no WT src/__pycache__).

No banked shape consumed (Next-P332 bank closed
at b440; Next-P334 banked from A-883 + A-1044
agree recorded below for b442 CONSUME-first).

- Build: make -C tree441/src/c BUILDDIR=$R/build441
  aae rgramc, rc=0, 0 warnings, build441/{aae,
  rgramc}. aae sha256 d6e27c97 (pinned stable
  continues), rgramc sha256 769ef3ef (== GATE
  both).
- RGRAMC-PYID 9908/9908 covered=9908/9908 GREEN
  rc=0 (tests/test_rgramc_fast.py, RGRAMC=seat
  binary, CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19816/19816 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 19816/19816 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 19816/19816; cmp441.py; GATE claims
  sorted only, raw corroborated too).
- PINS 19818 rows (2 hdr + 19816, +62 vs base
  19756; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq441.py). For-list
  union delta vs base +31/-0 (9877->9908):
  132621 132622 132623 132624 132630 132631
  132637 132638 132639 132640 132643 132644
  132647 132648 132649 132656 132664 132665
  132680 132681 132696 132697 132704 132712
  132713 132735 132736 132802 132863 132864
  132968 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (132621/22) + A head pair 623/624 off0/1
  + 630/631 off7/8 + tail pair 637/638 off14/15
  (6: offs 0,1,7,8,14,15) + C head pair
  639/640 off0/1 + 643/644 off4/5 + 647/648
  off8/9 (6: offs 0,1,4,5,8,9; unsampled offs
  2,3,6,7 = 641/642/645/646) + Q head 649
  off0 + row0-mid 656 off7 + boundary pairs
  664/665 off15/16 + 680/681 off31/32 +
  696/697 off47/48 + row3-mid 704 off55 + tail
  712 off63 (10: offs 0,7,15,16,31,32,47,48,
  55,63; NEW dual-mid off7+off55 shape) + R
  head 713 off0 + edge pair 735/736 off22/23 +
  mid 802 off89 + edge pair 863/864 off150/151
  + tail 968 off255 (7: offs 0,22/23,89,150/
  151,255; 1-mid off89 NEW shape, both counter
  edges pair-covered). 31x2=62 rows, range
  132621..132968 exact. PINS-new-N == for-added
  31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit441.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 153 PASS 0 FAIL first run. Inventory
  exactly the 12 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no QB/PT/FM, no M42/
  X42/H42/L42, no RT/TT, no QT). S0 168ch sig
  6db29606 NEW (32/84 payload diff vs P332S0 @
  3-11,34,35,41-43,45-48,50-55,76-83 first-hand
  incl NEW-sig b3 exactly (6db29606 vs 6db29604
  differ b3 only per sig compare), NOT byte-
  equal; differs vs P332 heads 6db29604/
  0b000000) / S1 176ch sig 0d000000 NEW (64/88
  payload diff vs P332S1 @ 0,4-9,11-14,17-27,
  36,37,40-43,48-55,60-87 first-hand incl sig
  b0, NOT byte-equal; 26/88 diff vs own C10[0]
  staged cell0; sig SAME-as-own-C10; differs vs
  own PB0), staged as full-payload singletons.
  AM 16/16 14ch distinct (7B), CM 10/10 4ch
  distinct (2B: M2 b84,85), M 16/16 16ch
  distinct (8B: M7 b28-30,80-83), QR 4/4 8ch
  distinct (4B R4 rows fbfe25ec/1bff25ec/
  792d6aee/992d6aee) UNPAIRED, RM 16/16 14ch
  distinct (7B TM7), RQ 16/16 16ch distinct (8B
  TR8) UNPAIRED, no QT (R4 carries b84-87
  inside QR rows) + no RT (ring, not ROWTAIL)
  + no F (no frags). AC 79, b0-3 de000000 (b0
  const de), no b4/b5. C10-1SIG-88-TAIL-M2 sig
  0d000000 x10 SAME-as-PB1-sig (sig in CC b0-3
  consts; CM 10/10 diverge, b86,87 const e034
  in CC; CC has no b4/b5, b5 const 0c full
  block via raw lencode; FIRST C10-TAIL-M2).
  S1-vs-own-C10 staged per-cell (M2 b84,85 +
  b0-3 CC sig + b4/b5 lencode, each cell own
  assembly) [26]x10 TRUE UNIFORM, cells0-9
  positions identical (cell0 @ 4,16-18,22-35,
  64-67,84-87 first-hand; oracle secf441c same
  vector; sig b0 same-sig NOT in diff), sig
  0d000000 both, NOT byte-equal -- 12th TRUE-
  uniform case in sweep accounting (after P299/
  P303/P307/P311/P315/P317/P319/P323/P325/P329/
  P331); viewer record 24->25.
  QUAD88-1SIG-4R-NOFRAG-B5CONST 1-sig d3000000
  x64 SAME-shape-as-PBA-class (QC b0 const d3,
  b1-3 const 00; b5 const 0c NO edge 64/64;
  b4 base 0x53 step2 64/64 contig+2 range
  53..d1): QM8 b29,30,34,35,80-83 M 16/16
  shared x3 vs row0 (M indexed by col off&15
  first-hand) NO frags + R4 b84-87 rows r0
  fbfe25ec / r1 1bff25ec / r2 792d6aee / r3
  992d6aee exact tuples 4/4 NO pairing
  pairwise-unequal; tails b84-87 row-led: r01
  TRUE 2B 25ec (@b86,87, FIRST TRUE-2B) + r23
  TRUE 3B 2d6aee (@b85,86,87) + else pairs
  (r02,r03,r12,r13) byte-LCS 0 all 4; b87 set
  {ec,ee} NOT const (first-hand); TAIL4 substr
  = TSHARE = subseq = 2/0/0/0/0/3 (order
  01,02,03,12,13,23; == A-1045 suffix-lcs at
  all 3 metrics, computed all three first-
  hand); NO frags.
  R legs M[m] + QR[q] both sides, NO F-row leg,
  NO F-scalar leg; Q region m=off&15/q=off>>4.
  P333R(T88-ring STANDARD) 132713..132968
  off=n-132713 sig db0e0000 x256; TM7 b40-42,
  80-83 by COL + TR8 b29,30,34,35,76-79 by ROW
  UNPAIRED SPLIT tails (b80-83 col / b76-79
  row, 16/16 distinct each, 0 overlap
  UNPAIRED); b0 const db ring-wide; b1 const
  0e ring-wide; b84-87 const 9ab6561c ring-
  wide; counter b4=(0xd3+2off)&FF b5=0x0c+
  (off>=23)+(off>=151) (py hex 0xd3/0x0c; C
  staged literals 211/12, re-derived:
  211==0xd3, 12==0x0c; edges off22/23 EARLY +
  off150/151 + mid off89 first-hand). R legs
  RM[c] + RQ[r] both sides, NO F anywhere in R.
  RM 16/16 distinct + RQ 16/16 distinct.
  M==RQ 7OF8 (M 8B vs RQ 8B: agree (0,0),(1,1),
  (3,3),(4,4),(5,5),(6,6),(7,7) 16/16 each =
  full-column lanes incl tails; b34 (2,2) fully
  disjoint 0/16; zero strays (max non-target
  0); full-row sets disjoint -- widths equal
  8B/8B yet rows differ: same-width outlier per
  rewritten predictor, no width rule cited) --
  38th odd-band RQ==M instance (viewer chain
  b435-35th FULL8/b437-36th FULL6/b439-37th
  TAILS4-ONLY/b441-38th 7OF8 sequential; FIRST
  7OF8 degree on file; sweep column-agreement
  7OF8 + cport full-row DISJOINT both true).
  Tails STANDARD-split (RM b80-83 by COL
  c=off&15, RQ b76-79 by ROW r=off>>4, 16/16
  distinct each, 0 overlap UNPAIRED); M-tails
  16/16 ALL NEW vs P332T RM col-led tails
  (overlap 0; P332T ROWBND frame, ref = RM
  col-led 6B rows, position-aware tails
  last-4B); RM-tails (b80-83) ALL NEW vs P332T
  RM col-led tails (overlap 0).
  S0 string 32/84 differ vs P332S0 (NEW-sig
  incl b3) + S1 string 64/88 differ vs P332S1
  (incl sig b0; [26x10] vs own C10 TRUE
  UNIFORM -- new uniform case). S1 sig-EQ
  P332C10 (0d000000; asserted per lesson (h)).
  P333 actuals (S0 6db29606/S1 0d000000/PBA88
  de000000/C10 0d000000 x10 SAME-as-PB1-sig +
  PB0-vs-P332PB0 32/84 + PB1-vs-P332PB1 64/88)
  == A-883 predicted next EXACT.
  Missing-sets first-hand EXACT: AC-9
  [4,5,28,29,30,80-83] = b4,b5+M7 (b28-30,
  80-83; b5 const 0c deducted from AC) / CC-4
  [4,5,84,85] = b4,b5+M2 (b84,85 tails-only,
  full sig b0-3 in CC = 0d,00,00,00 ->
  0d000000 x10 SAME-as-PB1-sig; b86,87 const
  e034 in CC; b5 const 0c deducted) / QC-14
  [4,5,29,30,34,35,80,81,82,83,84,85,86,87]
  = b4,b5+QM8 (b29,30,34,35,80-83)+R4 (b84-87;
  b0 const d3 in QC = 1SIG, b1-3 const 00;
  b86,87 in R lanes NOT const) / RC-17
  [4,5,29,30,34,35,40,41,42,76-83] = b4,b5+TR8
  (b29,30,34,35,76-79)+TM7 (b40-42,80-83).
  PLAIN first-hand: AC b0-3 = de,00,00,00 ->
  sig de000000 x16, b0 const de; AM 16/16
  distinct; b5 const 0c. TAIL-M2 first-hand: CC
  b0-3 full sig 0d000000 x10 SAME-as-PB1-sig
  (S1 sig-eq own C10); CM 10/10 diverge, b86,87
  const e034; b5 const 0c. Code AC79/CC84/
  QC74/RC71; incl = +1/+1/+1/+0 (A b5 const 0c,
  C b5 const 0c, Q b5 const 0c NO edge, T
  counter) = 80/85/75/71; lane consts = A-883
  INCL EXACT (deduct-b5-only-when-b5vary rule
  holds; A-1045 excl 79/84/74/71 = code EXACT
  -- no lag on odd band). VPOS 8/3/13/17 =
  memo EXACT (A b4+M7; C b4+M2; Q b4+QM8+R4; T
  b0,b4,b5+TM7+TR8). Sorted-unique + _N decls
  79/84/74/71 match actual. Coverage unions
  exact every block (const U tab U lencode ==
  88 x4, 0 overlap; each missing == region
  pay-index set minus lencode EXACT all 4).
  Base temp maxes _t6780/_b4104/_i4105 (no
  reuse: band adds _t6781-6796 continuous-16 +
  _i4107/09/4112/4115 + _b4106/08/4110/4111/
  4113/4114, whole-file max _t6796, all above
  base maxes).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 132621 / S1 132622 / A 132623-638 /
  C 132639-648 / Q 132649-712 / R 132713-968):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A b5 const 0c, C b5
  const 0c, Q b5 const 0c NO edge; A/C/Q use
  raw lencode, no counter literals anywhere
  A/C/Q) + R explicit counter (b4=(0xd3+2off)&
  FF b5=0x0c+(off>=23)+(off>=151); py hex
  0xd3/0x0c; C staged literals 211/12,
  re-derived: 211==0xd3, 12==0x0c) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 14ch
  b28-30,80-83; C 4ch b84,85; Q 16/8ch; R
  14/16ch). C blocks carry T89106/89111/89116/
  89131/89145/89165 py-line mirrors (all 6
  present, bounds + byte positions exact).
  Insert exact both sides: after T10P332R close
  (py 89087-block then guards 89106+; C
  tables-then-dispatch in band order), at
  dispatch tail (N-out-of-scope fallthrough
  follows; C has 2 scope hits, py 2 scope hits
  per GATE). Matches A-883 geometry (values re-
  checked in audit above; NO D dips: ownloop
  tags exactly the 6 P333 blocks).
- Edges own-loop ownloop441.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P333R N=132968 off=255.
  edges441.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  1b/0c, 1d/0c == raw lencode) + aform 16/16 (A
  head 1f/0c tail 3d/0c b5set {0c} NO step, 0
  ff) + cform 10/10 (C head 3f/0c tail 51/0c
  b5set {0c} NO step, 0 ff) + qform 64/64 +
  qb5const 64/64 (Q head 53/0c tail d1/0c b4
  base 0x53 step2 64/64 contig+2 range 53..d1
  b5set {0c} NO edge, 0 ff in 64) + ring
  counter 256/256 + ringraw 256/256 (head
  d3/0c; 132735 off22 ff/0c -> 132736 off23
  01/0d EARLY; mid off89 85/0d @132802; 132863
  off150 ff/0d -> 132864 off151 01/0e; tail
  off255 d1/0e; exactly 2 ff in 256). S0/S1
  embedded b4/b5 match raw lencode.
  Odd-lencode 348/348. Ring edges + mid + tail
  132968 in for-list + 2 PASS lines each py+C.
  Tail 132968: oracle rav sha 9a9b111d10d62a12...
  == PINS (match True; rawlen 104 re-checked);
  py+C CLOSED T10P333R off=255 agree. No
  DISSENT: cut bytes verify.
- PB-diff secf441.py (cache path, 0 miss-warmed
  after ownloop) + secf441b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (132621 +
  132273 + 132622 + 132274); S0: oracle132621-
  vs-132273 32/84, codeS0-vs-P332S0 32/84,
  positions identical (differ-pos 3-11,34,35,
  41-43,45-48,50-55,76-83 listed); DIRECT
  32/84 agree. S1: oracle132622-vs-132274
  64/88, codeS1-vs-P332S1 64/88, positions
  identical (differ-pos 0,4-9,11-14,17-27,36,
  37,40-43,48-55,60-87 listed); DIRECT 64/88
  agree. Triple-derived both pairs (same novel
  shape both tiers: 84/84/84/84 + 88/88/88/88).
  S1-vs-own-C10 secf441c.py (oracle C10 cells
  n132639-648): [26]x10 TRUE UNIFORM
  staged+oracle, cells0-9 positions identical
  (cell0 pos 4,16-18,22-35,64-67,84-87 ==
  staged EXACT), sig 0d000000 both, NOT
  byte-equal. UNIFORM -- 12th case (record
  24->25). Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  231/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw C
  608 total = 603 content + 5 bare-blank / 0
  del (verified bare `+` lines; GATE states
  "608 content + 5 blank-only" which sums 613
  vs numstat 608?? -- first-hand: 603 content
  + 5 bare-blank = 608 total == numstat. 7th
  raw-C overcount-by-5 instance (b429/b431/
  b433/b435/b437/b439/b441); code GREEN since
  gated artifact == verified artifact).
  Band-level sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope 825bee89..
  18016e8a, 902 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 231/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1886->1892 +6, singletons
  `if n == ` 698->700 +2 (unanchored; 4sp
  693->695 +2) / range-guards `<= n <=`
  784->788 +4 (unanch and 4sp) = +6 py (==
  GATE deltas); C guards: singleton `if
  ((n) == (` 693->695 +2 / range 784->788 +4 /
  CLOSED T10P prints 1886->1892 +6 both sides
  (seal 1980->1986 +6; offset +94 vs CLOSED-
  T10P: 1986-1892 = 94, stable b401-b441). All
  agree (stated literal methods first-hand;
  deltas agree every method; 5-count C-vs-py
  singleton offset pre-existing, unchanged:
  700-695 = 698-693 = 5; viewer-vs-sweep
  absolute convention reconciled). No elif
  either side (py elif 50->50, C else-if 0->0;
  A/C/Q use raw lencode, no counters).
- CONFIRM evidence (CONVERT-01 rule b): A-883-
  q1045 verdict CONFIRM 62/62 CLEAN (own bed
  r3-P333 132621..133000 BAD=0 + own r3-P332,
  verifier v269.py 62/62 PASS; tier GATED PORT;
  novelties FIRST C10-TAIL-M2 + FIRST TRUE-2B
  tail-share gated; exact-value corroboration
  incl PB0 NEW-sig 32/84 + PB1 NEW-sig 64/88
  SAME-as-own-C10 26/88 + PBA88-PLAIN-M7b28
  sig-de + C10-TAIL-M2 + QUAD d3 + R4 exact
  tuples + r01-TRUE2 + r23-TRUE3 + b0 const in
  QC + b5 const NO edge + M-tails NEW +
  T88-STANDARD + counter + edges; sheet INCL
  PBA 80 / C10 85 / quad 75 / T88 71) +
  A-1045-q1045 verdict CONFIRM 47/47 CLEAN
  (own bed r6-P333 132621..132996 + r6-P332,
  BAD=0, verifier v600f3.py 47/47 PASS; suffix-
  lcs 2/0/0/0/0/3 at all 3 metrics (computed
  suffix+subseq+substr first-hand) + M-tails
  NEW + consts excl 79/84/74/71 script-claimed
  corroborated; files present, counts verified;
  tier GATED PORT). Agrees with cport commit
  msg (PYID 9908, RGRAM 19816). No viewer P333
  geometry answer on file at gate time (memo-
  only recon; this VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b441
  (own seat CLAIM only; exactly 1 GATE-18016e8a;
  zero FLAG hits; even base b440 respected;
  b442+ = future turf, untouched, used as
  nothing here). PROSE-01: all hex/counts above
  copied from own run output; GATE-18016e8a
  re-read in FULL before filing (1 mild prose
  note above, substance exact).
- RQ==M chain: b441 odd 7OF8 (M 8B vs RQ 8B;
  agree 7 lanes 16/16; b34 (2,2) disjoint;
  heads-noted positions; full-row sets
  disjoint). 38th odd-band instance (viewer
  chain b435-35th FULL8/b437-36th FULL6/b439-
  37th TAILS4-ONLY/b441-38th 7OF8 sequential;
  width-equality predictor REWRITTEN per GATE,
  no width rule cited). Memo-silent on the
  relation; batteries confirm; tier stands.
- TRUE-uniform chain: b441 UNIFORM [26]x10
  SAMESIG (staged+oracle, positions identical).
  Record 24->25 (24 excl P299). 12th case
  (after P299/P303/P307/P311/P315/P317/P319/
  P323/P325/P329/P331).
- S-F tables-lag: b441 odd band sheet==code (impl
  79/84/74/71 vs A-883 INCL 80/85/75/71 with
  +1/+1/+1/+0, A-1045 excl EXACT) -- no lag on
  odds (deduct-b5-only-when-b5vary holds);
  even sub-streak stays 15.
- Next-P334 SHAPE banked (A-883 + A-1045 agree,
  for b442 to CONSUME FIRST): PB0 2e01ac06
  NEW-sig 31/84 @132969 + PB1 0e000000 NEW-sig
  47/88 vs n132622 @132970 + PBA88 fb000000
  x16 @132971-986 + C10-region 0c000000 x10
  @132987-996 (A-1045; A-883 adds DIFFERS-from-
  PB1-sig per Q1 text "C10 0c000000 x10 @
  132987-996 DIFFERS-from-PB1-sig" -- verify
  against code first-hand at CONSUME time).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 1 mild GATE prose note (raw-C
"608 content + 5 blank" overcounts by 5: first-
hand 608 total = 603 content + 5 bare-blank --
same token as b429/b431/b433/b435/b437/b439
GATEs, 7th instance; code GREEN since gated
artifact == verified artifact).
