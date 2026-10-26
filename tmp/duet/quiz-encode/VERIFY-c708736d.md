# VERIFY-c708736d b443 T10P335 pins 133317..133664 (348 pins) PASS

Seat viewer-r68, first-hand, tree @c708736d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r68.
Base b82fa688 (b442 tip, 1992 tiers sealed; this
seat's VERIFY-b82fa688 PASS-filed same round,
base-use only, respected). Band = ff5b855c (py
merge w2b@a716ffc5 partial, +6 tiers, +62 pins;
commit msg verified via git log) + c708736d (C
port; parent == ff5b855c verified). Trees via git
archive to TMPDIR tree443/tree443base; tests run
from NVME workdirs (no WT src/__pycache__).

Banked Next-P335 shape (b442 VERIFY, A-884 FWD +
lane code first-hand) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 2e01ac06 SAME-sig-as-
P334PB0 30/84 @133317 + PB1 0d000000 NEW-sig
69/88 vs n132970 @133318 + PBA88 d5000000 x16
@133319-334 + C10-region 0d000000 x10 SAME-as-
PB1-sig @133335-344 -- staged==oracle 0/0/0/0,
sigs exact, counts+positions identical. Bank-miss
lesson applied: no trust without code.

- Build: make -C tree443/src/c BUILDDIR=$R/build443
  aae rgramc, rc=0, 0 warnings, build443/{aae,
  rgramc}. aae sha256 d6e27c97 (pinned stable
  continues), rgramc sha256 4dad3bf5 (== GATE
  both).
- RGRAMC-PYID 9970/9970 covered=9970/9970 GREEN
  rc=0 (tests/test_rgramc_fast.py, RGRAMC=seat
  binary, CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19940/19940 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 19940/19940 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 19940/19940; cmp443.py; GATE claims
  sorted only, raw corroborated too).
- PINS 19942 rows (2 hdr + 19940, +62 vs base
  19880; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq443.py). For-list
  union delta vs base +31/-0 (9939->9970):
  133317 133318 133319 133320 133326 133327
  133333 133334 133335 133336 133339 133340
  133343 133344 133345 133360 133361 133375
  133376 133377 133392 133393 133400 133408
  133409 133503 133504 133568 133631 133632
  133664 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (133317/18) + A head pair 319/320 off0/1
  + 326/327 off7/8 + tail pair 333/334 off14/15
  (6: offs 0,1,7,8,14,15) + C head pair
  335/336 off0/1 + 339/340 off4/5 + 343/344
  off8/9 (6: offs 0,1,4,5,8,9; unsampled offs
  2,3,6,7 = 337/338/341/342) + Q head 345
  off0 + boundary pair 360/361 off15/16 +
  B5EDGE pair 375/376 off30/31 + boundary pair
  376/377 off31/32 (off31 shared edge/boundary)
  + boundary pair 392/393 off47/48 + row3-mid
  400 off55 + tail 408 off63 (10: offs 0,15,16,
  30,31,32,47,48,55,63; NEW edge-carry +
  off55-mid shape) + R head 409 off0 + edge
  pair 503/504 off94/95 + mid 568 off159 + edge
  pair 631/632 off222/223 + tail 664 off255 (7:
  offs 0,94/95,159,222/223,255; 1-mid off159
  NEW shape, both counter edges pair-covered).
  31x2=62 rows, range 133317..133664 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit443.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 149 PASS 0 FAIL first run. Inventory
  exactly the 12 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no QB/PT/FM, no M42/
  X42/H42/L42, no RT/TT, no QT). S0 168ch sig
  2e01ac06 sig-EQ-P334PB0 (b0-3 byte-equal; 2nd
  sig-eq-PB0 after b433 P325, NOT first; 30/84
  payload diff vs P334S0 @ 4,5,22,23,30-33,
  35-43,48,52-55,68-75 first-hand, NO sig bytes
  in diff, NOT byte-equal; differs vs P334 heads
  0e000000-side) / S1 176ch sig 0d000000 NEW
  (69/88 payload diff vs P334S1 @ 0,4-59,76-87
  first-hand incl sig b0, NOT byte-equal; 79/88
  diff vs own C10[0] staged cell0; sig SAME-as-
  own-C10; differs vs own PB0), staged as
  full-payload singletons. AM 16/16 14ch
  distinct (7B), CM 10/10 4ch distinct (2B: M2
  b84,85), M 16/16 12ch distinct (6B: QM6
  b20,21,80-83), QR 4/4 10ch distinct (5B R5
  rows 1fa86deedf/1fc86deedf/21308ea108/
  21e4829c4f; b13 pairs 1f/1f/21/21 full-
  unequal) UNPAIRED, RM 16/16 14ch distinct (7B
  RM7 b28-30,76-79), RQ 16/16 12ch distinct (6B
  RQ6 b20,21,80-83) UNPAIRED, no QT (R5 carries
  b13,84-87 inside QR) + no RT (ring, not
  ROWTAIL) + no F (no frags). AC 79, b0-3
  d5000000 (b0 const d5), no b4/b5. C10-1SIG-88-
  TAIL-M2 sig 0d000000 x10 SAME-as-PB1-sig (sig
  in CC b0-3 consts; CM 10/10 diverge, b86,87
  const eedf in CC; CC has no b4/b5, b5 const
  11 full block via raw lencode; 2nd TAIL-M2
  after P333). S1-vs-own-C10 staged per-cell
  (M2 b84,85 + b0-3 CC sig + b4/b5 lencode, each
  cell own assembly) [79]x10 TRUE UNIFORM,
  cells0-9 positions identical (cell0 @ 4,6-55,
  60-87 first-hand; oracle secf443c same vector;
  sig b0-3 same-sig NOT in diff), sig 0d000000
  both, NOT byte-equal -- 13th TRUE-uniform case
  in sweep accounting (after P299/P303/P307/P311/
  P315/P317/P319/P323/P325/P329/P331/P333);
  viewer record 25->26. FIRST 79-wide uniform
  (b435 P327 [79x9,80] was NOT uniform).
  QUAD88-1SIG-4R-NOFRAG-R5-B5EDGE 1-sig d5000000
  x64 SAME-sig-as-PBA (QC b0 const d5, b1-3
  const 00; b5 edge 11->12 @off30/31 exact in
  VPOS, edge 133375->133376 r1c14/c15
  first-hand; b4 base 0xc3 step2 64/64 contig+2):
  QM6 b20,21,80-83 M 16/16 shared x3 vs row0 (M
  indexed by col off&15 first-hand) NO frags +
  R5 b13,84-87 rows r0 1fa86deedf / r1
  1fc86deedf / r2 21308ea108 / r3 21e4829c4f
  exact tuples 4/4 NO pairing pairwise-unequal;
  tails b84-87 row-led: r01 TRUE 3B 6deedf
  (@b85,86,87) + else trailing-suffix lcs 0
  incl r23 (all 5 else-pairs); b87 {df,08,4f}
  tri-state NOT const (first-hand); TAIL4
  substr = TSHARE = subseq = 3/0/0/0/0/0 (order
  01,02,03,12,13,23; == A-1047 suffix-lcs at
  all 3 metrics, computed all three first-
  hand); ROW5-substr r23=1 via b13 (ROW vs TAIL
  pinned both); b5 edge + M-tails NEW; FIRST
  R5-b13 quad global (no prior QUAD-R5 on file).
  R legs M[m] + QR[q] both sides, NO F-row leg,
  NO F-scalar leg; Q region m=off&15/q=off>>4.
  P335R(T88-ring SWAPPED) 133409..133664
  off=n-133409 1-sig 550d0000 x256; RM7 b28-30,
  76-79 by COL + RQ6 b20,21,80-83 by ROW
  UNPAIRED (SWAPPED tails b80-83 row / b76-79
  col, 16/16 distinct each, 0 overlap
  UNPAIRED); b0 const 55 ring-wide; b1 const 0d
  ring-wide; b84-87 const 04839c4f ring-wide;
  counter b4=(0x43+2off)&FF b5=0x12+(off>=95)+
  (off>=223) (py hex 0x43/0x12; C staged
  literals 67/18, re-derived: 67==0x43,
  18==0x12; edges off94/95 + off222/223 + mid
  off159 first-hand). R legs RM[c] + RQ[r] both
  sides, NO F anywhere in R. RM 16/16 distinct
  + RQ 16/16 distinct.
  M==RQ FULL6 (M 6B vs RQ 6B same-lanes: agree
  (0,0)-(5,5) 16/16 each; zero strays; full-row
  sets EQUAL) -- 39th odd-band RQ==M instance
  (viewer chain b435-35th FULL8/b437-36th FULL6/
  b439-37th TAILS4-ONLY/b441-38th 7OF8/b443-39th
  FULL6 sequential; 5th FULL6 degree (4 FULL6 on
  file); sweep column-agreement FULL6 + cport
  full-row ORDERED 6B/6B same-lanes both true;
  width rule REWRITTEN r57: same-lanes =>
  ordered, no width rule cited). Tails SWAPPED-
  split (RM b76-79 by COL c=off&15, RQ b80-83 by
  ROW r=off>>4, 16/16 distinct each, 0 overlap
  UNPAIRED); M-tails 16/16 ALL NEW vs P334T RQ
  row-led tails (overlap 0; P334T SWAPPED frame,
  ref = RQ row-led 8B rows, position-aware tails
  last-4B; RQ-ref precedented b436, NOT first);
  RQ-tails (b80-83) ALL NEW vs P334T RQ row-led
  tails (overlap 0).
  S0 string 30/84 differ vs P334S0 (sig-EQ, NO
  sig bytes in diff) + S1 string 69/88 differ vs
  P334S1 (incl sig b0; [79x10] vs own C10 TRUE
  UNIFORM -- new uniform case, first 79-wide).
  P335 actuals (S0 2e01ac06 sig-EQ-P334PB0/S1
  0d000000/PBA88 d5000000/C10 0d000000 x10
  SAME-as-PB1-sig + PB0-vs-P334PB0 30/84 +
  PB1-vs-P334PB1 69/88) == A-884 predicted next
  EXACT.
  Missing-sets first-hand EXACT: AC-9
  [4,5,13,14,15,80-83] = b4,b5+M7 (b13-15,
  80-83; b5 const 11 deducted from AC) / CC-4
  [4,5,84,85] = b4,b5+M2 (b84,85 tails-only,
  full sig b0-3 in CC = 0d,00,00,00 ->
  0d000000 x10 SAME-as-PB1-sig; b86,87 const
  eedf in CC; b5 const 11 deducted) / QC-13
  [4,5,13,20,21,80-87] = b4,b5+QM6
  (b20,21,80-83)+R5 (b13,84-87; b0 const d5 in
  QC = 1SIG SAME-as-PBA, b1-3 const 00; b13 in
  R lanes NOT const) / RC-15
  [4,5,20,21,28-30,76-83] = b4,b5+RQ6
  (b20,21,80-83)+RM7 (b28-30,76-79). PLAIN
  first-hand: AC b0-3 = d5,00,00,00 -> sig
  d5000000 x16, b0 const d5; AM 16/16 distinct;
  b5 const 11. TAIL-M2 first-hand (2nd after
  P333): CC b0-3 full sig 0d000000 x10 SAME-as-
  PB1-sig (S1 sig-eq own C10); CM 10/10 diverge,
  b86,87 const eedf; b5 const 11. Code AC79/
  CC84/QC75/RC73; incl = +1/+1/+0/+0 (A b5 const
  11, C b5 const 11, Q b5 EDGE 11->12 exact, T
  counter) = 80/85/75/73; lane consts = A-889
  INCL EXACT (deduct-b5-only-when-b5vary rule
  holds; A-1047 excl 79/84/75/73 = code EXACT
  -- no lag on odd band). VPOS 8/3/13/15 = memo
  EXACT (A b4+M7; C b4+M2; Q b4,b5+QM6+R5; T
  b4,b5+RM7+RQ6). Sorted-unique + _N decls
  79/84/75/73 match actual. Coverage unions
  exact every block (const U tab U lencode ==
  88 x4, 0 overlap; each missing == region
  pay-index set minus lencode EXACT all 4).
  Base temp maxes _t6812/_b4124/_i4125 (no
  reuse: band adds _t6813-6828 continuous-16 +
  _i4127/29/4132/4135 + _b4126/28/4130/4131/
  4133/4134, whole-file max _t6828, all above
  base maxes).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 133317 / S1 133318 / A 133319-334 /
  C 133335-344 / Q 133345-408 / R 133409-664):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A b5 const 11, C b5
  const 11, Q b5=11+(off>=31) edge 133375->
  133376 r1c14/c15; A/C/Q use raw lencode, no
  counter literals anywhere A/C/Q) + R explicit
  counter (b4=(0x43+2off)&FF b5=0x12+(off>=95)+
  (off>=223); py hex 0x43/0x12; C staged
  literals 67/18, re-derived: 67==0x43,
  18==0x12) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions
  exact (A 14ch b13-15,80-83; C 4ch b84,85; Q
  12/10ch; R 14/12ch). C blocks carry T89568/
  89573/89578/89593/89607/89627 py-line mirrors
  (all 6 present, bounds + byte positions exact).
  Insert exact both sides: after T10P334R close,
  at dispatch tail (N-out-of-scope fallthrough
  follows; C has 2 scope hits, py 2 scope hits
  per GATE). Matches A-889 geometry (values re-
  checked in audit above; NO D dips: ownloop
  tags exactly the 6 P335 blocks).
- Edges own-loop ownloop443.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P335R N=133664 off=255.
  edges443.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  8b/11, 8d/11 == raw lencode) + aform 16/16 (A
  head 8f/11 tail ad/11 b5set {11} NO step, 0
  ff) + cform 10/10 (C head af/11 tail c1/11
  b5set {11} NO step, 0 ff) + qform 64/64 +
  qb5edge 64/64 (Q head c3/11 edge off30->31
  133375 ff/11 -> 133376 01/12 tail 41/12 b4
  base 0xc3 step2 64/64 contig+2 b5set {11,12}
  (11 offs 0-30, 12 offs 31-63), exactly 1 ff
  in 64) + ring counter 256/256 + ringraw
  256/256 (head 43/12; 133503 off94 ff/12 ->
  133504 off95 01/13; mid off159 81/13 @133568;
  133631 off222 ff/13 -> 133632 off223 01/14;
  tail off255 41/14; exactly 2 ff in 256). S0/S1
  embedded b4/b5 match raw lencode.
  Odd-lencode 348/348. Ring edges + mid + tail
  133664 in for-list + 2 PASS lines each py+C.
  Tail 133664: oracle rav sha 82cf7919572b4b0d...
  == PINS (match True; rawlen 104 re-checked);
  py+C CLOSED T10P335R off=255 agree. No
  DISSENT: cut bytes verify.
- PB-diff secf443.py (cache path, 0 miss-warmed
  after ownloop) + secf443b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (133317 +
  132969 + 133318 + 132970); S0: oracle133317-
  vs-132969 30/84, codeS0-vs-P334S0 30/84,
  positions identical (differ-pos 4,5,22,23,
  30-33,35-43,48,52-55,68-75 listed); DIRECT
  30/84 agree. S1: oracle133318-vs-132970
  69/88, codeS1-vs-P334S1 69/88, positions
  identical (differ-pos 0,4-59,76-87 listed);
  DIRECT 69/88 agree. Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf443c.py
  (oracle C10 cells n133335-344): [79]x10 TRUE
  UNIFORM staged+oracle, cells0-9 positions
  identical (cell0 pos 4,6-55,60-87 == staged
  EXACT), sig 0d000000 both, NOT byte-equal.
  UNIFORM -- 13th case (record 25->26; FIRST
  79-wide). Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  232/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw C
  608 total = 603 content + 5 bare-blank / 0
  del (verified bare `+` lines; GATE states
  "608 content + 5 blank-only" which sums 613
  vs numstat 608?? -- first-hand: 603 content
  + 5 bare-blank = 608 total == numstat. 8th
  raw-C overcount-by-5 instance (b429/b431/
  b433/b435/b437/b439/b441/b443); code GREEN
  since gated artifact == verified artifact).
  Band-level sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope b82fa688..
  c708736d, 903 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 232/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1898->1904 +6, singletons
  `if n == ` 702->704 +2 (unanchored; 4sp
  697->699 +2) / range-guards `<= n <=` 792->796
  +4 (unanch and 4sp) = +6 py (== GATE deltas
  702->704 / 792->796); C guards: singleton
  `if ((n) == (` 697->699 +2 / range 792->796 +4
  / CLOSED T10P
  prints 1898->1904 +6 both sides (seal 1992->
  1998 +6; offset +94 vs CLOSED-T10P: 1998-1904
  = 94, stable b401-b443). All agree (stated
  literal methods first-hand; deltas agree every
  method; 5-count C-vs-py singleton offset
  pre-existing, unchanged: 704-699 = 702-697
  = 5; viewer-vs-sweep absolute convention
  reconciled). No elif either side (py elif
  50->50, C else-if 0->0; A/C/Q use raw lencode,
  no counters).
- CONFIRM evidence (CONVERT-01 rule b): A-889-
  q1047 verdict CONFIRM 62/62 CLEAN (own beds
  r3-P335 133317..133696 + r3-P334 379 cells,
  BAD=0, verifier v275.py 62/62 PASS; tier GATED
  PORT; novelties R5-b13 quad FIRST global +
  SWAPPED RM7/RQ6 T gated; exact-value
  corroboration incl PB0 sig-EQ 30/84 + PB1 NEW
  69/88 SAME-as-own-C10 79/88 + PBA88-PLAIN-M7b13
  sig-d5 + C10-TAIL-M2 + QUAD d5-SAME-as-PBA +
  R5 exact tuples + b13 1f/1f/21/21 + r01-TRUE3
  + else-0 + b0 const in QC SAME-as-PBA + b5
  edge @30/31 + M-tails NEW + T88-SWAPPED +
  counter + edges; sheet INCL PBA 80 / C10 85 /
  quad 75 / T88 73) + A-1047-q1047 verdict
  CONFIRM 47/47 CLEAN (own bed r6-P335
  133317..133692 + r6-P334, BAD=0, verifier
  v600f3.py 47/47 PASS; suffix-lcs 3/0/0/0/0/0
  at all 3 metrics (computed suffix+subseq+
  substr first-hand) + M-tails NEW + consts excl
  79/84/75/73 script-claimed corroborated; files
  present, counts verified; tier GATED PORT).
  Agrees with cport commit msg (PYID 9970, RGRAM
  19940). No viewer P335 geometry answer on file
  at gate time (memo-only recon; this VERIFY is
  the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b443
  (own seat CLAIM only; exactly 1 GATE-c708736d;
  zero FLAG hits; even base b442 respected; no
  future turf touched). PROSE-01: all hex/counts
  above copied from own run output; GATE-c708736d
  re-read in FULL before filing (1 mild prose
  note above, substance exact).
- RQ==M chain: b443 odd FULL6 (M 6B vs RQ 6B
  same-lanes diag-16, zero strays, sets EQUAL).
  39th odd-band instance (viewer chain b435-35th
  FULL8/b437-36th FULL6/b439-37th TAILS4-ONLY/
  b441-38th 7OF8/b443-39th FULL6 sequential;
  5th FULL6). Memo-silent on the relation;
  batteries confirm; tier stands.
- TRUE-uniform chain: b443 UNIFORM [79]x10
  SAMESIG (staged+oracle, positions identical).
  Record 25->26 (25 excl P299). 13th case, FIRST
  79-wide uniform.
- S-F tables-lag: b443 odd band sheet==code (impl
  79/84/75/73 vs A-889 INCL 80/85/75/73 with
  +1/+1/+0/+0, A-1047 excl EXACT) -- no lag on
  odds (deduct-b5-only-when-b5vary holds); even
  sub-streak stays 16.
- Next-P336 SHAPE banked (A-889 + A-1047 agree,
  for r69 to CONSUME FIRST): PB0 2e01ac06
  32/84 @133665 + PB1 0d000000 sigeq 79/88
  @133666 + PBA88 98000000 x16 @133667-682 +
  C10-region 0e000000 x10 DIFFERS-from-PB1-sig
  @133683-692 (memo-derived; lane-code verify
  pending at CONSUME time per bank-miss lesson).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 1 mild GATE prose note (raw-C
"608 content + 5 blank" overcounts by 5: first-
hand 608 total = 603 content + 5 bare-blank --
same token as b429/b431/b433/b435/b437/b439/b441
GATEs, 8th instance; code GREEN since gated
artifact == verified artifact).
