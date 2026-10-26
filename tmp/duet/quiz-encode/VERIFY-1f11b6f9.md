# VERIFY-1f11b6f9 b436 T10P328 pins 130881..131228 (348 pins) PASS

Seat viewer-r67, first-hand, tree @1f11b6f9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r67.
Base a60294b6 (b435 tip, 1950 tiers sealed; this
seat's VERIFY-a60294b6... base-use only, respected;
r66 filed b432-b435 same base chain, respected).
Band = a83869f9 (py merge w2b@24550308 partial,
+6 tiers, +62 pins; commit msg verified via git log)
+ 1f11b6f9 (C port; parent == a83869f9 verified).
Trees manifest-identical to tips (git ls-tree vs
git ls-files cmp clean, 117/117 both; WT detached
at band, will return to lanes/encode-viewer at
round end).

Banked Next-P328 shape (r66-HANDOFF, cited
"GATE-a60294b6 FWD-check") CONSUMED FIRST and
REFUTED 4/4 first-hand (bank-miss, handoff flaw):
bank PB0 575f8102 NEW 31/84 @130881 vs actual
575f8102 sig-eq-P327PB0 30/84 (sig right, NEW +
count wrong); bank PB1 05000000 sig-eq-P327C10
54/88 vs n130551 vs actual sig-eq-P327PB1 80/88
vs n130534 + 29/88 vs own C10[0] (relation +
comparator + count wrong); bank PBA88 3f000000
x16 vs actual 42000000 x16 (WRONG); bank C10
06000000 x10 SAME-as-PB1 vs actual 05000000 x10
SAME-as-PB1 (sig WRONG, relation right). Cited
source GATE-a60294b6 contains NO FWD-check (grep
verified) -- bank has no valid provenance. Code +
GATE-1f11b6f9 + A-869 + A-1040 all agree on
actuals; verdict unaffected.

- Build: make -C WT/src/c BUILDDIR=$R/build436
  aae rgramc (absolute NVME path, flags -O2 -Wall
  -Wextra -std=c11 per Makefile), rc=0, 0 warnings
  (log = 2 mkdir/cc command echoes only),
  build436/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1
  r39-r70+, sha256 matches b354-b436 pinned value;
  band touches no aae sources), rgramc sha256
  d228bdad (== GATE both).
- RGRAMC-PYID 9752/9752 covered=9752/9752 GREEN
  rc=0 (tests/test_rgramc_fast.py, RGRAMC=seat
  binary, CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19504/19504 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19504/19504 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 19504/19504; cmp436.py; GATE claims
  sorted only, raw corroborated too).
- PINS 19506 rows (2 hdr + 19504, +62 vs base
  19444; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq436.py). For-list
  union delta vs base +31/-0 (9721->9752):
  130881 130882 130883 130884 130890 130891
  130897 130898 130899 130900 130903 130904
  130907 130908 130909 130924 130925 130940
  130941 130943 130944 130956 130957 130972
  130973 131071 131072 131150 131199 131200
  131228 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set:
  2 sing (130881/82) + A head 883 + 884 + 890 +
  891 + 897 + tail 898 (6: offs 0,1,7,8,14,15)
  + C head 899 + 900 + 903 + 904 + edge pair
  907/908 (offs 0,1,4,5,8,9; unsampled offs
  2,3,6,7 = 901/902/905/906) + Q
  head 909 + off15 pair 924/925 + off31/32 pair
  940/941 + B5EDGE pair 943/944 pinned off34/35
  + pair 956/957 off47/48 + tail 972 (10: offs
  0,15,16,31,32,34,35,47,48,63) + R head 973
  off0 + sig-boundary+lencode pair 131071/
  131072 off98/99 + mid 131150 off177 + edge
  pair 131199/131200 off226/227 + tail 131228
  (7: offs 0,98,99,177,226,227,255; boundary
  pair COINCIDES with sig boundary first-hand).
  31x2=62 rows, range 130881..131228 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit436.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 166 PASS 0 FAIL after 1 seat-script fix
  (C S0/S1 string-literal decl regex dropped;
  re-added, re-ran). Inventory exactly the 14
  both sides, C==py (S0/S1/AM/AC/CM/CC/M/QR/QC/
  RM/RQ/RC/RSA/RSB; no F/FT, no F0/F1, no QT, no
  RT/TT, no BM/BC, no M19/X19, no QB/PT/FM, no
  M42/X42/H42/L42). S0 168ch sig 575f8102
  sig-eq-P327PB0 (30/84 payload diff vs P327S0 @
  4,5,6,7,9-11,13-18,44-47,51,56-59,76-83
  first-hand, NOT byte-equal; differs vs P327 C10
  heads; sig differs vs own PB1); S1 176ch sig
  05000000 sig-eq-P327PB1 (80/88 payload diff vs
  P327S1 @ 4-55,60-87 first-hand, NOT
  byte-equal; 29/88 diff vs own C10[0] staged
  cell0; sig SAME-as-own-C10; differs vs own
  PB0), staged as full-payload singletons. AM
  16/16 14ch distinct, CM 10/10 10ch diverge
  (b34 {f5 x5 rows0-4, f9 x5 rows5-9} first-hand,
  flips at edge rows), M 16/16 16ch distinct,
  QR 4/4 26ch distinct UNPAIRED, RM 16/16 16ch
  distinct, RQ 16/16 16ch distinct UNPAIRED, no
  QT (quad tails live in QR rows) + no RT
  (MIDROW-SPLIT tails) + no F (no frag this
  tier). AC 79, b0-3 42000000 (b0 const 42), no
  b4/b5. C10-1SIG-88-TAIL-M5b34 sig 05000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM
  10/10 diverge, b34 {f5,f9}; CC has no b4/b5,
  b5 const fe full block via raw lencode).
  S1-vs-own-C10 staged per-cell (M5 b34,84-87,
  b4/b5 lencode, each cell own assembly) counts
  [29,28,28,28,28,29,29,29,29,29] cell0==29 per
  GATE; oracle cells same vector (secf436c);
  sig 05000000 both, NOT byte-equal, NOT uniform
  -- no new uniform case; record stays 21.
  QUAD88-1SIG-4R-NOFRAG-B5EDGE 1-sig 6c000000
  x64 DIFFERS-from-PBA-sig-42 (QC b0 const 6c
  via generic QC const-loop both sides, not a
  0x6c literal -- re-read region code both
  sides; b5 edge fe->ff @off34/35, exactly 1 ff
  in 64; b4 base 0xbb step2 64/64 range
  bb..ff,01..39; QM8 b40-43,80-83 M 16/16 NO
  frags + R13 b29,30,33-39,84-87 rows 4/4 NO
  pairing pairwise-unequal: r0/r1/r2 share 9B
  prefix b1b2c8e7f7b66ea269, differ in tails
  only with 3 distinct tail tuples; full tuples
  unequal; r3 fully distinct; tails b84-87 4
  distinct 28b1be9f/48b1be9f/bf2401bd/0d10e165,
  r01 TRUE-3B b1be9f suffix, r2/r3 suffix-LCS 0
  vs all; full-LCS prefix-9 r012 / 0 r3x (GATE
  "9/9/0/9/0/0" = longest-common-prefix
  convention; true subsequence (0,1)=12 from
  shared tail b1be9f -- GATE prose slip, mild,
  behavior legs exact); b87 [9f,9f,bd,65] NOT
  const, set {9f,bd,65}).
  R legs M[m] + QR[q] both sides, NO F-row leg,
  NO F-scalar leg; Q region m=off&15/q=off>>4.
  P328R(T88-ring-2SIG-MIDROW-SPLIT) 130973..
  131228 off=n-130973 c=off&15 r=off>>4, sigs
  ac050000 x99 (off0-98) + 580b0000 x157
  (off99-255), boundary off98/99 MID-row-6;
  RM TM8 b30,39,46,47,80-83 by COL + RQ TR8
  b40-43,76-79 by ROW UNPAIRED, SPLIT tails
  b80-83 col / b76-79 row UNPAIRED 16/16
  distinct each, 0 overlap; RSA 9 (ac,05,67,bd,
  19,98,17,1a,91) off<99 / RSB 9 (58,0b,cc,7a,
  3a,30,2f,34,92) off>=99; b2/b3 const 00
  ring-wide; b84-87 const b6865167 ring-wide
  NEW; counter b4=(0x3b+2off)&FF b5=((0xff+
  (off>=99)+(off>=227)))&FF (py hex 0x3b/0xff;
  C staged literals 59/255, re-derived:
  59==0x3b, 255==0xff; wrap ff->00->01
  first-hand; ring thresholds coincide with
  sig boundary first-hand). R legs RM[c] +
  RQ[r] both sides, NO F anywhere in R. RM
  16/16 distinct + RQ 16/16 distinct.
  M==RQ FULL 16/16 string-identical INTRA-tier:
  set-eq True AND ordered-eq True (matrices:
  diag-16 all 8 lanes; off-diag (0,3)=(3,0)=1
  = intra-row byte coincidence, harmless);
  payload positions DIFFER (QM8 b40-43,80-83
  vs TR8 b40-43,76-79 slots, verified in region
  code both sides) -- 36th even-band RQ==M
  instance, class string-eq-positions-differ
  (viewer chain: b432 tails-eq-strings-differ /
  b434 FULL-eq-positions-identical / b436
  string-eq-positions-differ; sweep GATE
  convention "FULL 16/16 string-identical,
  byte positions DIFFER" reconciled first-hand:
  tables ordered-identical, payload slots
  split). Tails SPLIT (RM b80-83 by COL
  c=off&15, RQ b76-79 by ROW r=off>>4, 16/16
  distinct each, 0 overlap UNPAIRED); M-tails
  16/16 ALL NEW vs P327 (vs P327M/RM/RQ tails
  0 overlap); RM-tails ALL NEW vs P327RM;
  RQ-tails ALL NEW vs P327RQ; cross overlaps 0.
  S0 string 30/84 differ vs P327S0 (sig-eq
  P327PB0) + S1 string 80/88 differ vs P327S1
  (sig-eq P327PB1; NOT uniform vs own C10).
  P328 actuals (S0 575f8102/S1 05000000/PBA88
  42000000/C10 05000000 x10 SAME-as-PB1-sig +
  S1-vs-P327S1 80/88) == A-869 + A-1040
  predicted shape EXACT (both memos agree on
  geometry; bank-miss above is handoff-only).
  Missing-sets first-hand EXACT: AC-9
  [4,5,29,34,35,80-83] = b4,b5+M7 (b29,34,35,
  80-83) / CC-7 [4,5,34,84-87] = b4,b5+M5
  (b34,84-87, full sig b0-3 in CC = 05,00,00,00
  -> 05000000 x10 SAME-as-PB1-sig) / QC-23
  [4,5,29,30,33-43,80-87] = b4,b5+QM8 (b40-43,
  80-83)+R13 (b29,30,33-39,84-87; b0 const 6c
  in QC = 1SIG) / RC-27 [0,1,4,5,6-11,30,39,
  40-43,46,47,52,76-83] = b4,b5+RSA/B9
  (b0,1,6-11,52)+TM8 (b30,39,46,47,80-83)+TR8
  (b40-43,76-79). PLAIN first-hand: AC b0-3 =
  42,00,00,00 -> sig 42000000 x16, b0 const 42;
  AM 16/16 distinct; b5 const fe. B5EDGE
  first-hand: CC b0-3 full sig 05000000 x10
  SAME-as-PB1-sig (S1 sig-eq own C10); CM 10/10
  diverge; b34 {f5,f9} rows0-4/5-9; b5 const fe
  full block; CC FIXED exact (b5 in VPOS).
  Code AC79/CC81/QC65/RC61/RSA9/RSB9; incl =
  +1/+1/+0/+0 (A b5 const fe, C b5 const fe, Q
  b5 edge fe->ff exact, T counter) = 80/82/65/
  61; lane consts = A-869 INCL EXACT (PBA/C10
  lag this tier, 31st consecutive S-F + 13th
  even-band PBA/C10-lag per GATE running
  counts; memo-exact on quad (b5 edge-varies,
  in VPOS) and T88 (b5 counter-varies, no
  deduction); geometry exact, PORT verdict
  stands). Sorted-unique + _N decls 79/81/65/
  61/9/9 match actual. Coverage unions exact
  every block (const U tab U {b4,b5} == 88 x4,
  0 overlap; T-block const = RC U RSA/B split;
  each missing == region pay-index set minus
  {b4,b5} EXACT all 4 (A/C/Q region text
  re-derived; R static part + rs-loop both
  sides verified)). Base temp maxes _t6700/
  _b4053/_i4054 (no reuse: band adds
  _t6701-6716 continuous-16 + _i4056/58/61/64/
  65 + _b4055/57/59/60/62/63, whole-file max
  _t6716, all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 130881 / S1 130882 / A 130883-898 /
  C 130899-908 / Q 130909-972 / R 130973-
  131228): bounds + paylens (1x84 + 347x88) +
  lencode l16 A/C/Q both sides (A b5 const fe,
  C b5 const fe, Q b5=fe+(off>=35); A/C/Q use
  raw lencode, no counter literals anywhere
  A/C/Q) + R explicit counter (b4=(0x3b+2off)
  &FF b5=((0xff+(off>=99)+(off>=227)))&FF; py
  hex 0x3b/0xff; C staged literals 59/255, re-
  derived: 59==0x3b, 255==0xff; wrap ff->00->
  01 first-hand) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A M7 b29,34,35,80-83; C M5
  b34,84-87; Q QM8 b40-43,80-83 + R13 b29,30,
  33-39,84-87; R TM8 b30,39,46,47,80-83 by COL
  (code-RM8) + TR8 b40-43,76-79 by ROW
  (code-RQ8), tails SPLIT) + C guards
  `if ((n) == (130881))` / `(130882)` + 4 range
  guards exact + counter literals exact + C
  byte-index lists match py per block (A 7B, C
  5B, Q 8B/13B, R 8B/8B SPLIT). C blocks carry
  T87941/87946/87951/87966/87981/88002 py-line
  mirrors (all 6 re-read verbatim against the
  py guard lines above); bounds + byte
  positions exact. Insert exact both sides:
  after T10P327R close (py CLOSED-then-guard;
  C block follows P327R close @233957, P328
  blocks through @234159), at dispatch tail
  (N-out-of-scope fallthrough follows: C 234161,
  py 88025; early same-text guards unrelated
  scope). Matches A-869 geometry (values re-
  checked in audit above; NO D dips: ownloop
  tags exactly the 6 P328 blocks).
- Edges own-loop ownloop436.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  b436 tier fully cache-warm from sweep2 leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P328R N=131228 off=255.
  edges436.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  83/fe, 85/fe == raw lencode) + aform 16/16 (A
  head 87/fe tail a5/fe b5set {fe} NO step, 0
  ff) + cform 10/10 (C head a7/fe tail b9/fe
  b5set {fe} NO step, 0 ff) + qform 64/64 +
  qb5edge 64/64 (Q head bb/fe edge 130943
  off34 ff/fe -> 130944 off35 01/ff tail 39/ff
  b5set {fe,ff} edge off35, exactly 1 ff in
  64; b4 base 0xbb step2 64/64 range
  bb..ff,01..39) + ring counter 256/256 +
  ringraw 256/256 (head 3b/ff; 131071 off98
  ff/ff -> 131072 off99 01/00 COINCIDES sig
  boundary; mid off177 9d/00 @131150; 131199
  off226 ff/00 -> 131200 off227 01/01; tail
  off255 39/01; exactly 2 ff in 256). S0/S1
  embedded b4/b5 (83/fe, 85/fe) match raw
  lencode. Odd-lencode 348/348 (346 + S0/S1
  embedded). Ring edges + mid + tail 131228 in
  for-list + 2 PASS lines each py+C. Tail
  131228: oracle rav sha 997c462e902931f1 ==
  PINS (match True; rawlen 104 re-checked);
  py+C CLOSED T10P328R off=255 agree. No
  DISSENT: cut bytes verify.
- PB-diff secf436.py (cache path, 0 miss-warmed
  after ownloop) + secf436b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (130881 +
  130533 + 130882 + 130534); S0: oracle130881-
  vs-130533 30/84, codeS0-vs-P327S0 30/84,
  positions identical (differ-pos 4,5,6,7,9,10,
  11,13-18,44-47,51,56-59,76-83 listed);
  DIRECT 30/84 agree. S1: oracle130882-vs-
  130534 80/88, codeS1-vs-P327S1 80/88,
  positions identical (differ-pos 4-55,60-87
  listed); DIRECT 80/88 agree. Triple-derived
  both pairs (same novel shape both tiers:
  84/84/84/84 + 88/88/88/88). S1-vs-own-C10
  secf436c.py (oracle C10 cells n130899-908):
  [29,28,28,28,28,29,29,29,29,29] staged+oracle,
  cells vary (CM diverge); sig 05000000 both,
  NOT byte-equal. NOT uniform -- no new case;
  record stays 21. Byte-diff discipline
  observed throughout.
- C diff pure-add: numstat 638/0 (rgramc.c) +
  242/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw C
  638 total = 633 content + 5 bare-blank / 0
  del (verified bare `+` lines; GATE states
  "633 content + 5 bare-blank" EXACT -- no
  overcount this band). full-digit norm
  (rgramc.c scope): C del-uniq 0 all 4 variants,
  add-uniq 165/162/164/161 (161 = strip+
  dropempty), missing 0 every variant; py del-
  uniq 0 add-uniq 179 x4, missing 0 (integrity
  intact, variant-robust); C-tempnorm del-uniq
  0 add-uniq 410 missing 0 / py-tempnorm add-
  uniq 195 recorded. Band-level sole del = old
  for-line churn (1/1).
- Wall on band diff added lines (scope a60294b6..
  1f11b6f9, 943 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 638/0, rgram.py 242/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks,
  tier-comments `# T10P` 1856->1862 +6,
  singletons `if n == ` unanchored 688->690 +2
  (dispatch-exact-4sp 678->680 +2)
  / range-guards `<= n <=` 764->768 +4 (unanch
  and 4sp 742->746 +4) = +6 py (== GATE
  deltas); C guards: singleton `if ((n) == (`
  683->685 +2 / range 764->768 +4 (5-count
  C-vs-py singleton offset pre-existing,
  unchanged: 690-685 = 688-683 = 5), CLOSED
  T10P prints 1856->1862 +6 py + 1856->1862 +6
  C (seal 1950->1956 +6; offset +94 vs
  CLOSED-T10P: 1956-1862 = 94, stable b401-
  b436). All agree (stated literal methods
  first-hand; deltas agree every method;
  viewer-vs-sweep absolute convention
  reconciled: unanchored vs dispatch-exact
  differ by pre-existing non-dispatch hits,
  deltas identical). Deliberate structural add:
  none (no elif either side: py elif 50->50
  pre-existing, C else-if 0->0; A/C/Q use raw
  lencode, no counter literals).
- CONFIRM evidence (CONVERT-01 rule b): A-869-
  q1040-P328 verdict CONFIRM 67/67 CLEAN (own
  bed r3-P328 130881..131260 BAD=0 + own r3-
  P327, verifier v255.py 67/67 PASS; file
  present, counts verified; major novelty 2SIG-
  MIDROW-SPLIT gated; exact-value corroboration
  incl PB0 sig-eq-P327PB0 30/84, PB1 sig-eq-
  P327PB1 80/88 SAME-as-own-C10 29/88, PBA88-
  PLAIN-M7b29 sig-42 M7 16/16 NO pair, C10-
  1SIG-88-TAIL-M5b34 SAME-as-PB1-sig b34-{f5,
  f9} 10/10 diverge, QUAD88-1SIG-4R-NOFRAG-
  B5EDGE 1-sig-6c DIFFERS-from-PBA + R13 rows +
  r012-share-9B + r01-TRUE-3B + r2/r3-lcs0 +
  b87-{9f,bd,65} + QM8 + NO frags + b5-edge-
  off35 + M-tails NEW, T88-RING-2SIG-MIDROW-
  SPLIT + TM8-by-COL/TR8-by-ROW + SPLIT9 (b0
  ac/58 ...) + b2/b3-00 + b84-87 b6865167 +
  counter + wrap + edges; sheet INCL PBA 80 /
  C10 82 / quad 65 / T88 61; section Q1/Q2/Q3
  all CONFIRM, no gloss issue) + A-1040-q1040-
  P328 verdict CONFIRM 46/46 CLEAN (own bed
  r6-P328 130881..131256 + r6-P327, BAD=0 +
  direct-oracle 2/2 byte-match, verifier
  v600f3.py 46/46 PASS; file present, counts
  verified; suffix-lcs + M-tails NEW + SPLIT9
  EXACT + consts excl 79/81/65/61 script-
  claimed corroborated). Agrees with cport
  commit msg (PYID 9752, RGRAM 19504). No
  viewer P328 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b436
  (own seat CLAIM only; exactly 1 GATE-1f11b6f9;
  zero FLAG hits; even base b435 respected;
  b437+ = future turf, untouched, used as
  nothing here). PROSE-01: all hex/counts above
  copied from own run output; GATE-1f11b6f9
  re-read in FULL before filing (1 mild prose
  note + 1 handoff-bank flaw below, substance
  exact).
- RQ==M chain: b436 even FULL 16/16 string-
  identical INTRA-tier (set-eq True, ordered-eq
  True, diag-16 all 8 lanes; off-diag (0,3)=
  (3,0)=1 intra-row coincidence only). 36th
  even-band instance (viewer chain b432-tails-
  eq-strings-differ/b434-FULL-eq-positions-
  identical/b436-string-eq-positions-differ
  sequential). Payload positions DIFFER (QM8
  b80-83 vs TR8 b76-79). Memo-silent on the
  relation; batteries confirm; tier stands.
- TRUE-uniform chain: b436 NOT uniform (S1 vs
  own C10 [29,28,...] staged+oracle). Record
  stays 21 (20 excl P299).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 1 mild GATE prose note (full-LCS
(0,1): stated 9 = longest-common-prefix
convention; true subsequence 12 via shared tail
b1be9f -- code GREEN since gated artifact ==
verified artifact) + 1 HANDOFF-bank flaw (r66
Next-P328 shape 4/4 wrong, cited FWD-check
absent from cited source -- recorded for parent,
not a code issue).
FWD-bank for r68 (consume-first): A-869 + GATE-
1f11b6f9 agree -- Next P329: PB0 eed6f805
NEW-sig 40/84 @131229 + PB1 0b000000 NEW-sig
67/88 vs n130882 @131230 + PBA88 d8000000 x16
@131231-246 + C10-region 0b000000 x10 @131247-
256 SAME-as-PB1-sig.
