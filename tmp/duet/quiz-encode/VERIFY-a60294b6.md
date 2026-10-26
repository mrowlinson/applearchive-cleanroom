# VERIFY-a60294b6 b435 T10P327 pins 130533..130880 (348 pins) PASS

Seat viewer-r66, first-hand, tree @a60294b6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r66.
Base b6adc780 (b434 tip, 1944 tiers sealed; this
seat's VERIFY-b6adc780 PASS-filed same round,
base-use only, respected). Band = 3e9a68d9 (py merge
w2b@530f8665 partial, +6 tiers, +62 pins) + a60294b6
(C port, 1950 sealed). Trees manifest-identical to
tips (git ls-tree vs git ls-files cmp clean, 117/117
both; WT detached at band, will return to
lanes/encode-viewer at round end).

Banked Next-P327 shape (GATE-b6adc780 FWD-check, this
seat verified first-hand in VERIFY-b6adc780)
CONSUMED FIRST and corroborated below:
PB0 575f8102 pay84 NEW-sig 31/84 @130533 / PB1
05000000 pay88 sig-eq-P326C10region 84/88 vs n130203
@130534 / PBA88 50000000 x16 @130535-550 / C10
05000000 x10 SAME-as-PB1-sig @130551-560 -- all
exact.

- Build: make -C tree435/src/c BUILDDIR=$R/build435
  aae rgramc (absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build435/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r70+, sha256 matches b354-b435
  pinned value; band touches no aae sources), rgramc
  sha1 3dae00d7 / sha256 52eaf75d (== GATE both).
- RGRAMC-PYID 9721/9721 covered=9721/9721 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19442/19442 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19442/19442 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 19442/19442;
  cmp435.py; GATE claims sorted only, raw corroborated
  too).
- PINS 19444 rows (2 hdr + 19442, +62 vs base 19382;
  +62 = 31 for-Ns x2); PASS-names vs PINS-names xor 0
  py+C; PINS-baseN vs for-list xor 0 (4-way set-eq,
  seteq435.py). For-list union delta vs base +31/-0
  (9690->9721):
  130533 130534 130535 130536 130542 130543 130549
  130550 130551 130552 130555 130556 130559 130560
  130561 130569 130576 130577 130592 130593 130608
  130609 130617 130624 130625 130687 130688 130753
  130815 130816 130880
  (== GATE sampled list EXACT). Decomposition first-hand
  from the added set: 2 sing (130533/34) + A head 535
  + 536 + 542 + 543 + 549 + tail 550 (6: offs 0,1,7,8,
  14,15) + C head 551 + 552 + 555 + 556 + edge pair
  559/560 (offs 0,1,4,5,8,9; B5EDGE pair-covered; offs
  2,3,6,7 = 553/554/557/558 unsampled) + Q head 561 +
  off8 569 + boundary pairs 576/577 + 592/593 + 608/
  609 + off56 617 + tail 624 (10: offs 0,8,15,16,31,
  32,47,48,56,63; const-b5 NO step, first-hand, NEW
  shape) + R head 625 + edge pair 687/688 (offs 62/63)
  + mid 753 (off128, 1-mid shape) + edge pair 815/816
  (offs 190/191) + tail 880 (7: offs 0,62/63,128,190/
  191,255; both counter edges pair-covered, first-hand).
  31x2=62 rows, range 130533..130880 exact. PINS-new-N
  == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit435.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 169 PASS
  0 FAIL after 1 seat-script fix (Q-b0 literal form:
  b0-const-57 enforced via the generic QC const-loop
  both sides, not a 0x57 literal -- re-read region
  code both sides, fixed check; caught by runs).
  Inventory exactly the 12 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT tabs, no F0/F1,
  no BM/BC, no M19/X19, no QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig 575f8102 NEW (31/84 payload diff vs
  P326S0 @ b2,4,5,22,23,30,31,33-43,48,52-55,68-75
  first-hand incl NEW-sig b2, NOT byte-equal; differs
  vs P326 heads 575f0102/04000000/05000000) / S1
  176ch sig 05000000 sig-eq-P326C10region (69/88
  payload diff vs P326S1 @ b0,4-59,76-87 first-hand
  incl sig b0, NOT byte-equal; sig SAME-as-own-C10;
  [79x9,80] vs own C10 assembled, NOT uniform --
  cell9 = cell0 + b5 B5EDGE extra first-hand; differs
  vs own PB0), staged as full-payload singletons.
  AM 16/16 14ch (7B) distinct, CM 10/10 10ch (5B)
  diverge (b8 {19 x8, 59 x2} rows 0-7 = 19, rows 8-9 =
  59, flips at edge rows first-hand), M 16/16 16ch
  (8B) distinct, QR 4/4 20ch (10B) distinct UNPAIRED,
  RM 16/16 14ch (7B) distinct, RQ 16/16 16ch (8B)
  distinct UNPAIRED, no F/FT tabs, no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no QB/PT/FM, no
  M42/X42/H42/L42, no RT/TT (ring, not ROWTAIL), no
  QT (R10 carries b84-87 inside QR); table inventory
  exactly the 12.
  AC 79, b0-3 50000000 (b0 const 50), no b4/b5.
  C10-1SIG-88-TAIL-M5b8-B5EDGE sig 05000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge, b8 {19,59}; CC has no b4/b5, b5 edge
  fb->fc @off8/9 exact in raw lencode; CC FIXED exact
  (b5 in VPOS)).
  S1-vs-own-C10 staged per-cell (M5 b8,84-87, b4/b5
  lencode, each cell own assembly) [79]x9 + [80] NOT
  uniform (cells0-8 79 @ b4,6-55,60-87 EXACT,
  positions identical cells0-8 staged AND oracle;
  cell9 = cell0 + b5-B5EDGE extra [5] first-hand;
  sig 05000000 both, NOT byte-equal -- no new uniform
  case this band; record stays 21).
  QUAD88-1SIG-4R-NOFRAG 1-sig 57000000 x64 (M 8B
  b20-23,80-83 QM8 shared NO frags + R10 b13,14,16-19,
  84-87 r0 bdbcfc993645eec93f08 / r1
  bdbcfc9936450eca3f08 / r2 bdbcfc9936452eca3f08
  share 6B prefix bdbcfc993645, tails-only-diff 3
  distinct + r3 e23cbc41a204904af7fb fully distinct,
  tails b84-87 4 distinct eec93f08/0eca3f08/2eca3f08/
  904af7fb, r12 TRUE 3B ca3f08, r0 2B 3f08 vs r1/r2,
  TAIL4 suffix (01)=2 (02)=2 (12)=3 r3x=0, HEAD6
  r012=6 r3x=1, FULL10 01=8 02=8 12=9 r3x=1 (memo
  "r3 lcs=0" TRUE tail-level, "HEAD6 r3x=1 / FULL10
  r3x=1" verified subsequence-1 first-hand);
  b87 [08,08,08,fb] NOT const, b0 const 57 in QC
  via generic const-loop both sides (1SIG), b5 const
  fc NO edge, b4 0x03+2off range 03..81, NO frags).
  R legs M[m] + QR[q] both sides, NO F-row leg, NO
  F-scalar leg; Q region m=off&15/q=off>>4.
  P327R(T88-ring) 130625..130880 off=n-130625 c=off&15
  r=off>>4 SWAPPED sig 7f050000 (RM 7B b28-30,76-79 by
  COL + RQ 8B b20-23,80-83 by ROW SWAPPED tails b80-83
  row / b76-79 col UNPAIRED 16/16, b84-87 const
  b44af7fb); R legs RM[c] + RQ[r] both sides, NO F
  anywhere in R (SWAPPED RM-col / RQ-row verified in
  region text both sides). RM 16/16 distinct + RQ
  16/16 distinct, sets disjoint.
  M==RQ FULL8 (M 8B vs RQ 8B: agree (0,0),(1,1),
  (2,2),(3,3),(4,4),(5,5),(6,6),(7,7) 16/16 each;
  tabs byte-identical; same lanes b20-23,80-83) -- 5th
  full-identity instance (after P311 + P313 + P319 +
  P321); 35th odd-band RQ==M instance (viewer chain
  b421-28th FULL7/b423-29th TAILS4-ONLY/b425-30th
  TAILS4-ONLY/b427-31st FULL6/b429-32nd FULL7/b431-33rd
  TAILS4-ONLY/b433-34th HEADS4+TAILS4/b435-35th FULL8
  sequential). Tails SWAPPED-split (RM b76-79 by COL
  c=off&15, RQ b80-83 by ROW r=off>>4, 16/16 distinct
  each, 0 overlap UNPAIRED); M-tails 16/16 ALL NEW vs
  P326T RQ row-led tails (overlap 0; FIRST swapped
  ref); RM-tails (b76-79) ALL NEW vs P326T RM col-led
  tails (overlap 0); RQ-tails (b80-83) ALL NEW vs
  P326T RQ row-led tails (overlap 0); cross overlaps 0
  (P326T widths RM 7B/RQ 7B SWAPPED first-hand; tails
  compared position-aware + orientation-aware against
  col-led/row-led sets).
  S0 string 31/84 differ vs P326S0 (NEW-sig incl b2)
  + S1 string 69/88 differ vs P326S1 (incl sig b0;
  [79x9,80] vs own C10 NOT uniform -- cell9 B5EDGE b5
  extra; no new uniform case).
  P327 actuals (S0 575f8102/S1 05000000/PBA88
  50000000/C10 05000000 x10 SAME-as-PB1-sig +
  PB1-vs-P326C10[0] 84/88) == A-836 predicted next
  EXACT.
  Missing-sets first-hand EXACT: AC-9 [4,5,13,14,15,
  80-83] = b4,b5+M7 (b13-15,80-83) / CC-7
  [4,5,8,84-87] = b4,b5+M5 (b8,84-87, full sig b0-3
  in CC = 05,00,00,00 -> 05000000 x10 SAME-as-PB1-sig) /
  QC-20 [4,5,13,14,16-23,80-87] = b4,b5+QM8 (b20-23,
  80-83)+R10 (b13,14,16-19,84-87; b0 const 57 in QC =
  1SIG) / RC-17 [4,5,20-23,28-30,76-83] = b4,b5+RQ8
  (b20-23,80-83)+RM7 (b28-30,76-79).
  PLAIN first-hand: AC b0-3 = 50,00,00,00 -> sig
  50000000 x16, b0 const 50; AM 16/16 distinct; b5
  const fb. B5EDGE first-hand: CC b0-3 full sig
  05000000 x10 SAME-as-PB1-sig (S1 sig-eq own C10);
  CM 10/10 diverge; b8 {19,59} (rows 0-7 = 19, rows
  8-9 = 59, flips at edge rows); b5 edge fb->fc @off8/
  9; CC FIXED exact (b5 in VPOS).
  Code AC79/CC81/QC68/RC71; incl = +1/+0/+1/+0 (A b5
  const fb, C b5 EDGE fb->fc exact, Q b5 const fc, T
  counter) = 80/81/69/71; lane consts = A-837 INCL
  EXACT (FIRST exact-C10: edge-b5 => exact,
  deduct-b5-only-when-b5vary rule holds).
  Sorted-unique + _N decls 79/81/68/71 match actual.
  Coverage unions exact every block (const U tab U
  {b4,b5} == 88 x4, 0 overlap); each missing ==
  region pay-index set minus {b4,b5} EXACT all 4
  (A/C/Q/R region text re-derived first-hand).
  Base temp maxes _t6684/_b4043/_i4044 (no reuse:
  band adds _t6685-6700 continuous-16 + _b4045/47/49/
  50/52/53 + _i4046/48/51/54, whole-file max _t6700,
  all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 130533 / S1 130534 / A 130535-550 / C 130551-560 /
  Q 130561-624 / R 130625-880): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C/Q both sides
  (A b5 const fb, C b5=fb+(off>=9) emerges from raw
  lencode, Q b5 const fc; A/C/Q use raw lencode, no
  counter literals anywhere A/C/Q) + R explicit
  counter (b4=(0x83+2off)&FF b5=0xfc+(off>=63)+
  (off>=191); py hex 0x83/0xfc; C staged literals
  131/252, re-derived: 131==0x83, 252==0xfc; ring
  thresholds coincide with lencode high-byte steps
  first-hand) + m=off&15/q=off>>4/c=off&15/r=off>>4
  both sides + mtab/rtab byte positions exact (A M7
  b13-15,80-83; C M5 b8,84-87; Q QM8 b20-23,80-83 +
  R10 b13,14,16-19,84-87; R memo-TM8 b20-23,80-83 by
  ROW (code-RQ8) + memo-TR7 b28-30,76-79 by COL
  (code-RM7), tails SWAPPED) + C guards
  `if ((n) == (130533))` / `(130534)` + 4 range
  guards exact + counter literals exact + C byte-index
  lists match py per block (A 7B, C 5B, Q 8B/10B, R
  7B/8B SWAPPED-split). C blocks carry T87703/87708/
  87713/87728/87743/87764 py-line mirrors (all 6
  re-read verbatim against the py guard lines above);
  bounds + byte positions exact. Insert exact both
  sides: after T10P326R close (py CLOSED-then-guard;
  C block follows P326R close @233334, P327 blocks
  through @233519), at dispatch tail (N-out-of-scope
  fallthrough follows: C 2 scope hits, py 2 scope
  hits). Matches A-837 geometry (values re-checked in
  audit above; NO D dips: ownloop tags exactly the 6
  P327 blocks).
- Edges own-loop ownloop435.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc): 348/348 CLOSED
  rc=0 (0 miss-warmed; b435 tier fully cache-warm
  from PYID/RGRAM legs). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P327R N=130880
  off=255. edges435.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  cb/fb, cd/fb == raw lencode) + aform 16/16 (A head
  cf/fb tail ed/fb b5set {fb} NO step, 0 ff) + cform
  10/10 (C head ef/fb edge off8->9 130559 ff/fb ->
  130560 01/fc tail 81/fc b5set {fb,fc}) + qform 64/64
  + qb5const 64/64 (Q head 03/fc tail 81/fc b4 base
  0x03 step2 64/64 range 03..81 b5set {fc} NO step,
  NO edge, 0 ff in 64) + ring counter 256/256 +
  ringraw 256/256 (head 83/fc; 130687 off62 ff/fc ->
  130688 off63 01/fd; mid off128 83/fd @130753;
  130815 off190 ff/fd -> 130816 off191 01/fe; tail
  off255 81/fe; exactly 2 ff in 256). S0/S1 embedded
  b4/b5 (cb/fb, cd/fb) match raw lencode.
  Odd-lencode 348/348 (346 + S0/S1 embedded). Ring
  edges + mid + tail 130880 in for-list + 2 PASS lines
  each py+C. Tail 130880: oracle rav sha
  69f14791961461ac == PINS (== GATE prefix EXACT;
  rawlen 104 re-checked: paylen 88 + 12 + 4); py+C
  CLOSED T10P327R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf435.py (cache path, 0 miss-warmed after
  ownloop) + secf435b.py (DIRECT tool, no cache):
  staged-vs-oracle 0/0/0/0 (130533 + 130185 + 130534 +
  130186); S0: oracle130533-vs-130185 31/84,
  codeS0-vs-P326S0 31/84, positions identical
  (differ-pos 2,4,5,22,23,30,31,33-43,48,52-55,68-75
  listed); DIRECT 31/84 agree. S1: oracle130534-
  vs-130186 69/88, codeS1-vs-P326S1 69/88, positions
  identical (differ-pos 0,4-59,76-87 listed); DIRECT
  69/88 agree. Triple-derived both pairs (same novel
  shape both tiers: 84/84/84/84 + 88/88/88/88).
  S1-vs-own-C10 secf435c.py (oracle C10 cells n130551-
  560): [79]x9+[80] staged+oracle, cells0-8 positions
  identical (cell0 pos 4,6-55,60-87 == staged EXACT),
  cell9 = cell0 + b5-edge extra [5]; sig 05000000
  both, NOT byte-equal. NOT uniform -- no new case.
  Byte-diff discipline observed throughout.
- C diff pure-add: numstat 608/0 (rgramc.c) + 232/0
  (rgram.py) + 1/1 (for-line) + PINS +62/+0 (clean
  append, 31 Ns x2) == GATE; raw C 608 total = 603
  content + 5 bare-blank / 0 del (verified bare `+`
  lines; GATE states "608 content + 5 blank" which
  sums 613 vs numstat 608?? -- wait: GATE b435 line
  241 states "raw C 608 content + 5 blank-only `+`
  lines (verified bare, no whitespace) / 0 del".
  First-hand: 603 content + 5 bare = 608 total ==
  numstat. full-digit norm ([0-9]+ -> N): C del-
  uniq 0 (all 4 variants), add-uniq 149/146/148/145
  (145 = strip+dropempty, as cited), missing 0 every
  variant; py del-uniq 0 add-uniq 167 x4, missing 0
  (integrity intact, variant-robust); C-tempnorm
  del-uniq 0 add-uniq 403 missing 0 / py-tempnorm
  add-uniq 188 recorded. Band-level sole del = old
  for-line churn (1/1).
- Wall on band diff added lines (scope b6adc780..
  a60294b6, 903 added lines == GATE): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files: rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks,
  tier-comments `# T10P` 1850->1856 +6, singletons
  `if n == ` 686->688 +2 / range-guards `<= n <=`
  760->764 +4 = +6 py (== GATE absolutes); C guards:
  singleton `if ((n) == (` 681->683 +2 / range
  760->764 +4 (5-count C-vs-py singleton offset
  pre-existing, unchanged: 688-683 = 686-681 = 5),
  CLOSED T10P prints 1850->1856 +6 py + 1850->1856 +6
  C (seal 1944->1950 +6; offset +94 vs CLOSED-T10P:
  1950-1856 = 94, stable b401-b435). 4-space
  dispatch-exact 676->678 +2 / 738->742 +4 both
  sides (deltas agree, method-label noted). All agree
  (stated literal methods first-hand). Deliberate
  structural add: none (no elif/else-if either side:
  py elif 50->50 pre-existing, C else-if 0->0; A/C/Q
  use raw lencode, no counter literals).
- CONFIRM evidence (CONVERT-01 rule b): A-837-q919
  memo CONFIRM 65/65 CLEAN (own bed r3-P327 130533..
  130912 BAD=0 + own r3-P326, verifier v224.py 65/65
  PASS; file present, counts verified; exact-value
  corroboration incl PB0 NEW-sig 575f8102 31/84, PB1
  sig-eq-P326C10region 84/88 SAME-as-own-C10
  [79x9,80], PBA88-PLAIN-M7b13 sig-50 M7,
  C10-SAME-as-PB1-sig-TAIL-M5b8 b8-{19,59} B5EDGE
  fb->fc @off8/9, QUAD88-1SIG-4R-NOFRAG 1-sig-57 +
  R10 rows + r012-share-6B + r12-TRUE-3B + r0-2B-3f08
  + r3-head6-1/full10-1 + b87-[08,08,08,fb] + QM8 +
  NO frags + b5-const + M-tails NEW, T88-RING-
  SWAPPED + code-RM7-by-COL/RQ8-by-ROW + tails-
  swapped + b84-87 b44af7fb + edges + consts;
  section-F clean (65/65, no gloss issue this tier);
  M==RQ full8-equality unmentioned by memo, batteries
  confirm, tier stands).
  Agrees with cport commit msg (PYID 9721, RGRAM
  19442). No viewer P327 geometry answer on file at
  gate time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b435 (own
  seat CLAIM only; exactly 1 GATE-a60294b6; zero FLAG
  hits; even base b434 respected; b436+ = future
  turf, untouched, used as nothing here). PROSE-01:
  all hex/counts above copied from own run output;
  GATE-a60294b6 re-read in FULL before filing (1 mild
  prose note below, substance exact).
- RQ==M chain: b435 odd FULL8 (M 8B vs RQ 8B; agree
  (0,0)..(7,7) 16/16; tabs byte-identical; same lanes
  b20-23,80-83). 35th odd-band instance (viewer chain
  b421-28th FULL7/b423-29th TAILS4-ONLY/b425-30th
  TAILS4-ONLY/b427-31st FULL6/b429-32nd FULL7/b431-33rd
  TAILS4-ONLY/b433-34th HEADS4+TAILS4/b435-35th FULL8
  sequential); 5th full-identity instance (after P311+
  P313+P319+P321). Memo-silent on the relation.
- TRUE-uniform chain: b435 NOT uniform ([79]x9+[80];
  cell9 B5EDGE-b5 extra [5]). Record stays 21 (20
  excl P299).

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 mild prose-level note (raw-C "608 content + 5
blank" overcounts by 5: first-hand 608 total = 603
content + 5 bare-blank -- same token as b429/b431/b433
GATEs, 4th instance; code GREEN since gated artifact ==
verified artifact).
