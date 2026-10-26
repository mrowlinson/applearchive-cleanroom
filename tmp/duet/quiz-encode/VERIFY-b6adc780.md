# VERIFY-b6adc780 b434 T10P326 pins 130185..130532 (348 pins) PASS

Seat viewer-r66, first-hand, tree @b6adc780,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r66.
Base 6cb51277 (b433 tip, 1938 tiers sealed; this
seat's VERIFY-6cb51277 PASS-filed same round,
base-use only, respected). Band = 85843096 (py merge
w2b@55ac18d2 partial, +6 tiers, +62 pins) + b6adc780
(C port, 1944 sealed). Trees manifest-identical to
tips (git ls-tree vs git ls-files cmp clean, 117/117
both; WT detached at band, will return to
lanes/encode-viewer at round end).

Banked Next-P326 shape (GATE-6cb51277 FWD-check, this
seat verified first-hand in VERIFY-6cb51277)
CONSUMED FIRST and corroborated below:
PB0 575f0102 pay84 NEW-sig 34/84 @130185 / PB1
04000000 pay88 sig-eq-P325C10region 37/88 vs
n129855 @130186 / PBA88 79000000 x16 @130187-202 /
C10 05000000 x10 DIFFERS-from-PB1-sig @130203-212 --
all exact.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/
  Makefile, seat-private build434/{aae,rgramc}
  (BUILDDIR= absolute NVME path), rc=0, 0 warnings.
  sha256 rgramc 4f5d448b (== GATE) / aae d6e27c97
  pinned (== GATE both; band touches no aae sources
  per numstat).
- RGRAMC-PYID 9690/9690 covered=9690/9690 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19380/19380 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19380/19380 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 19380/
  19380; cmp434.py; GATE claims sorted only, raw
  corroborated too).
- PINS 19382 rows (2 hdr + 19380, +62 vs base 19320;
  +62 = 31 for-Ns x2); PASS-names vs PINS-names xor 0
  py+C; PINS-baseN vs for-list xor 0 (4-way set-eq,
  seteq434.py). For-list union delta vs base +31/-0
  (9659->9690):
  130185 130186 130187 130188 130194 130195 130201
  130202 130203 130204 130207 130208 130211 130212
  130213 130228 130229 130237 130244 130245 130260
  130261 130269 130276 130277 130303 130304 130405
  130431 130432 130532
  (== GATE sampled list EXACT). Decomposition first-hand
  from the added set: 2 sing (130185/86) + A head-pair
  87/88 + mids 94/95 + tail-pair 201/202 (6: offs 0,1,
  7,8,14,15) + C head 203/204 + mids 207/208 + tail
  211/212 (6: offs 0,1,4,5,8,9; offs 2,3,6,7 =
  205/206/209/210 unsampled) + Q head 213/off0 + mids
  228/229 (offs 15,16) + 237 (off24) + 244/245 (offs
  31,32) + 260/261 (offs 47,48) + 269 (off56) + tail
  276 (10: offs 0,15,16,24,31,32,47,48,56,63; NO
  step, quad b5 const, first-hand) + R head 277 +
  edge-pair 303/304 (offs 26/27) + mid 405 (off128,
  1-mid shape) + edge-pair 431/432 (offs 154/155) +
  tail 532 (7: offs 0,26/27,128,154/155,255; both
  counter edges pair-covered, first-hand). 31x2=62
  rows, range 130185..130532 exact. PINS-new-N ==
  for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle
  backend, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit434.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 157 PASS
  0 FAIL after 1 seat-script fix (AC-QC token: my
  first set-intersection reading (39) was the wrong
  convention -- first-hand per-byte accounting gives
  53 common byte positions with 43 same value, differ
  at 40-44,55,72-75 == GATE; token means common-bytes/
  sameval, recorded; caught by runs).
  Inventory exactly the 12 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F anywhere this tier,
  no FT46, no F0/F1, no QT (quad tails live in R26),
  no RT (SWAPPED tails), no TT, no BM/BC, no M19/X19,
  no QB/PT/FM, no M42/X42/H42/L42).
  S0 168ch sig 575f0102 NEW (34/84 payload diff vs
  P325S0 @ b0-5,13-17,19-29,56-67 first-hand, NOT
  byte-equal; differs vs P325 heads
  b7ce3001/02000000/04000000) / S1 176ch sig 04000000
  sig-eq-P325C10region (37/88 payload diff vs
  P325C10[0] n129855 assembled first-hand, NOT
  byte-equal; 46/88 diff vs own-C10[0] assembled
  n130203, NOT byte-equal; sig DIFFERS-from-own-C10
  04-vs-05; differs vs own PB0; S1-vs-P325S1 48/88
  recorded, unclaimed), staged as full-payload
  singletons.
  AM 16/16 16ch (8B) distinct, CM 10/10 10ch (5B)
  diverge (b45 {27 x4, 67 x6} first byte first-hand),
  M 16/16 14ch (7B) distinct, QR 4/4 52ch (26B)
  distinct UNPAIRED, RM 16/16 14ch (7B) distinct, RQ
  16/16 14ch (7B) distinct UNPAIRED, no QT + no RT
  (SWAPPED tails) + no F (no frag this tier).
  AC 78, b0-3 79000000 (b0 const 79), no b4/b5.
  C10-1SIG-88-DIFFSIG-M5b45 sig 05000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM
  10/10 diverge, b45 {27,67}; CC has no b4/b5, b5
  const f9 full block via lencode).
  S1-vs-own-C10 staged per-cell (M5 b45,84-87, b4/b5
  lencode, each cell own assembly) [46]x10
  TRUE-UNIFORM count+position (cell0 46 @
  0,4,11,19,38-75,84-87 EXACT; positions identical
  all 10 staged AND oracle; sig 04000000-vs-05000000
  DIFFSIG, NOT byte-equal -- 21st TRUE-uniform case
  on record, 20th excluding unverified P299;
  beyond-GATE values corroborated by oracle leg
  below).
  QUAD88-2SIG-4R-NOFRAG 79000000 x48 (rows0-2)
  SAME-sig-as-PBA + 2d000000 x16 (row3) (QC has no b0,
  b0 row-led in tab: QR b0s 79/79/79/2d; b5 const f9
  full 64, NO step, 0 ff; b4 base 0x4b step2 64/64
  range 4b..c9 NO edge; QM7 b52-54,80-83 16/16
  distinct NO frags + R26 b0,11,19,26-35,38,39,45-51,
  84-87 rows 4/4 NO pairing pairwise-disjoint:
  r0/r1/r2 share 22B non-tail prefix
  79d7f8453c4dffc26b60c7947f945d671f4f75088d1c,
  differ in tails only with 3 distinct tail tuples;
  full tuples unequal; r3 full tuple unequal;
  tails b84-87 4/4 distinct 99627102/48ce7102/
  68ce7102/1e156fc8, r12 TRUE-3B ce7102, r0 shares
  exactly 2B 7102 with r1/r2, r3 tail-LCS=0 vs all
  (full-LCS 2); tail-LCS r01=2/r02=2/r12=3;
  full-LCS r01=24/r02=24/r12=25 recorded first-hand).
  Ring SWAPPED: sig 9d070000 x256; code-RM7 b6,7,9,
  76-79 by COL RM 16/16 + code-RQ7 b52-54,80-83 by
  ROW RQ 16/16 UNPAIRED (tails SWAPPED b80-83 row /
  b76-79 col per A-836: memo-TM7 by ROW = code-RQ
  slots, memo-TR7 by COL = code-RM slots, label swap);
  b0 const 9d b1 const 07; b84-87 5ad8e80b ring-wide
  NEW.
  M==RQ FULL 16/16 string-identical INTRA-tier, byte
  positions IDENTICAL (QM7 b52-54,80-83 == RQ7 b52-54,
  80-83 slots; M0==RQ0 f1deef7df176b9; ordered-equal
  16/16). Even tier: no RQ==M ordinal (viewer evens
  convention: b414-full/b416-tail/b418-full/b420-
  string-eq-positions-differ/b424-tail-eq-positions-
  differ/b426-full/b428-string-split/b430-string-
  split/b432-tails-eq-strings-differ/b434-full-eq-
  positions-identical).
  Sorted-unique + _N decls 78/81/53/72 match actual.
  Missing-sets EXACT: AC-10 [4,5,38,39,46,47,80-83] =
  b4,b5+M8b38 / CC-7 [4,5,45,84-87] = b4,b5+M5b45 /
  QC-35 [0,4,5,11,19,26-35,38,39,45-54,80-87] = b4,b5+
  QM7+R26 (b0 in R lanes row-led, NOT const) /
  RC-16 [4,5,6,7,9,52,53,54,76-83] = b4,b5+
  TM7(RQ-slots)+TR7(RM-slots). VPOS 9/6/34/16 ==
  A-836 EXACT (PBA b4+M8 (b5 const deducted) / C10
  b4+M5 / quad b4+QM7+R26, b5 const excluded / T
  b4,b5+TM7+TR7). Coverage unions exact every block
  (const U tab U {b4,b5} == 88 x4, 0 overlap); each
  missing == region pay-index set minus {b4,b5} EXACT
  all 4 (A/C/Q/R region text re-derived first-hand,
  tab == region-idx minus {b4,b5} EXACT).
  Q legs M[m] + QR[q] both sides, NO F-row leg, NO
  F-scalar leg either side (no frag class this tier);
  R legs RM[c] + RQ[r] both sides, NO F anywhere in R
  (SWAPPED RM-col / RQ-row verified in region text
  both sides). RM 16/16 distinct + RQ 16/16 distinct,
  sets disjoint.
  P325 refs re-read: S0 b7ce3001 / S1 02000000 /
  PBA 21000000 / C10 04000000 / QUAD 3SIG 41/4c/78 /
  T ring 72040000 (STANDARD-split).
  PBA sig 79 NEW vs P325 21 (79000000 != 21000000);
  QUAD 2SIG 79/2d rows0-2-SAME-as-PBA vs P325 3SIG.
  AM/CM/M/QR/RM/RQ 0-overlap vs P325 (prev lens
  16/10/16/4/16/16); M-tails 16/16 ALL NEW vs P325T
  (zero overlap vs P325M AND vs P325RM-tail8 AND vs
  P325RQ-tail8). AC-QC: 53 common byte positions, 43
  same value (differ at 40-44,55,72-75), tables
  differ. Memo INCL PBA 79 / C10 82 / quad 54 / T88 72
  (A-836 re-read): impl 78/81/53/72 = b5 const
  deducted on PBA/C10/quad (b5 covered by lencode),
  T b5 varies counted -- INCL arithmetic exact,
  geometry exact, PORT verdict stands. 29th
  consecutive tables-lag band (b434 pattern +1/+1/+1/
  +0: PBA/C10/quad lag 1 each, T exact; running
  b412-b433 per GATE + r64/r65/r66 records).
  Base temp maxes _t6668/_b4033/_i4034 (no reuse:
  band adds _t6669-6684 continuous-16 + _b4035/37/39/
  40/42/43 + _i4036/38/41/44, whole-file max _t6684,
  all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 130185 / S1 130186 / A 130187-202 / C 130203-212 /
  Q 130213-276 / R 130277-532): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C/Q both sides
  (raw, b5 const f9 every block, NO step anywhere A/C/
  Q) + R explicit counter (b4=(0xcb+2off)&FF b5=0xf9+
  (off>=27)+(off>=155); py hex 0xcb/0xf9; C staged
  literals 203/249, re-derived: 203==0xcb, 249==0xf9;
  ring thresholds coincide with lencode high-byte
  steps first-hand) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions
  exact (A M8b38 b38,39,46,47,80-83; C M5b45 b45,
  84-87; Q QM7 b52-54,80-83 + R26 b0,11,19,26-35,38,
  39,45-51,84-87; R memo-TM7 b52-54,80-83 by ROW
  (code-RQ7) + memo-TR7 b6,7,9,76-79 by COL
  (code-RM7), tails SWAPPED) + C guards
  `if ((n) == (130185))` / `(130186)` + 4 range
  guards exact + counter literals exact + C byte-index
  lists match py per block (A 16ch, C 10ch, Q 14/52ch,
  R 14/14ch SWAPPED-split). C blocks carry T87468/
  87473/87478/87493/87508/87532 py-line mirrors
  (all 6 re-read: hit the exact py guard lines above);
  bounds + byte positions exact. Insert exact both
  sides: after T10P325R close (py CLOSED-then-guard;
  C block follows P325R close @232711-13, block
  @232714), at dispatch tail (N-out-of-scope
  fallthrough follows: C 232915, py 87551; early
  same-text guards at C 156772 / py 53988 are the
  T4-plateau-B n<=1077 check, unrelated scope).
  Matches A-836 geometry (values re-checked in audit
  above; NO D dips: ownloop tags exactly the 6 P326
  blocks).
- Edges own-loop ownloop434.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc): 348/348 CLOSED
  rc=0 (68 miss-warmed; b434 tier mostly cache-warm
  from prior legs). Census R256/Q64/A16/C10/S0/S1
  exact. Tail line: CLOSED T10P326R N=130532 off=255.
  edges434.py: paylens 1x84 + 347x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 embedded b4/b5 13/f9, 15/f9
  == raw lencode) + aform 16/16 (A head 17/f9 tail
  35/f9 b5set {f9} NO step, 0 ff) + cform 10/10 (C
  head 37/f9 tail 49/f9 b5set {f9} NO step, 0 ff) +
  qform 64/64 + qb5const 64/64 (Q head 4b/f9 tail
  c9/f9 b4 base 0x4b step2 64/64 range 4b..c9 b5set
  {f9} NO step, NO edge, 0 ff in 64) + ring counter
  256/256 + ringraw 256/256 (head cb/f9; 130303
  off26 ff/f9 -> 130304 off27 01/fa; mid off128
  cb/fa @130405; 130431 off154 ff/fa -> 130432
  off155 01/fb; tail off255 c9/fb; exactly 2 ff in
  256; thresholds 27/155 coincide with lencode
  high-byte steps first-hand); ff total x2 (both R);
  ff-in-Q 0. S0/S1 embedded b4/b5 (13/f9, 15/f9)
  match raw lencode. Odd-lencode 348/348 (346 + S0/S1
  embedded). Ring edges + mid + tail 130532 in
  for-list + 2 PASS lines each py+C. Tail 130532:
  oracle rav sha 8e7bdfd6c3bb4691 == PINS (rawlen
  104 re-checked: paylen 88 + 12 + 4); py+C CLOSED
  T10P326R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf434.py (cache path, 0 miss-warmed after
  ownloop) + secf434b.py (DIRECT tool, no cache):
  staged-vs-oracle 0/0 + assembled-P325C10[0]-vs-
  oracle 0 (130185 + 129837 + 130186 + 129855); S0:
  oracle130185-vs-129837 34/84, codeS0-vs-P325S0
  34/84, positions identical (differ-pos 0-5,13-17,
  19-29,56-67 listed); DIRECT 34/84 agree. S1:
  oracle130186-vs-129855 37/88, codeS1-vs-P325C10[0]
  37/88, positions identical; DIRECT 37/88 agree.
  Triple-derived both pairs (same novel shape both
  tiers: 84 + 88/88). S1-vs-P325S1 48/88 recorded,
  unclaimed by GATE (positions listed in logs).
  S1-vs-own-C10 secf434c.py (oracle C10 cells n130203-
  212): [46]x10 TRUE-UNIFORM counts AND positions
  identical all 10 (cell0 pos 0,4,11,19,38-75,84-87
  == staged EXACT; sig 04000000-vs-05000000 DIFFSIG,
  NOT byte-equal). Byte-diff discipline observed
  throughout.
- C diff pure-add: numstat 608/0 (rgramc.c) + 231/0
  (rgram.py) + 1/1 (for-line) + PINS +62/+0 (clean
  append, 31 Ns x2) == GATE; raw C 608 total = 603
  content + 5 bare-blank / 0 del (verified bare `+`
  lines; GATE states "603 content + 5 bare-blank"
  correctly -- no overcount this band; full-digit norm
  ([0-9]+ -> N): C del-uniq 0 (all 4 variants),
  add-uniq 153/150/152/149 (variants as cited),
  missing 0 every variant; py del-uniq 0 add-uniq 174
  x4, missing 0 (integrity intact, variant-robust);
  C-tempnorm del-uniq 0 add-uniq 371 missing 0 (==
  GATE). Band-level sole del = old for-line churn
  (1/1).
- Wall on band diff added lines (scope 6cb51277..
  b6adc780, 902 added lines == GATE): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files: rgramc.c 608/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks,
  tier-comments `# T10P` 1844->1850 +6, 4-space
  dispatch-exact singletons 674->676 +2 /
  range-guards 734->738 +4 = +6 py AND C identical
  (== GATE method; unanchored literal counts recorded
  in logs), CLOSED T10P prints 1844->1850 +6 py +
  1844->1850 +6 C (seal 1938->1944 +6; offset +94 vs
  CLOSED-T10P: 1944-1850 = 94, stable b401-b434). All
  agree (stated literal methods first-hand; no
  method-mix this band). Deliberate structural add:
  none (no elif/else-if either side: py elif 50->50
  pre-existing, C else-if 0->0; Q uses raw lencode,
  no counter literals).
- CONFIRM evidence (CONVERT-01 rule b): A-836-q918
  memo CONFIRM 65/65 CLEAN (own bed r3-P326 130185..
  130564 BAD=0 + own r3-P325, verifier v222.py 65/65
  PASS; file present, counts verified; tier GATED
  PORT, tier novelty SWAPPED-frame T; exact-value
  corroboration incl PB0 NEW-sig 575f0102 34/84, PB1
  sig-eq-P325C10region 37/88 DIFFERS-from-own-C10
  04-vs-05 46/88, PBA88-PLAIN-M8b38 sig-79 M8,
  C10-DIFFSIG-M5b45 DIFFERS-from-PB1-sig b45-{27,67},
  QUAD88-2SIG-4R-NOFRAG 79x48-rows0-2-SAME-as-PBA +
  2d-row3 + R26 rows + r012-share-22B + r12-TRUE-3B +
  r0-2B-7102 + r3-lcs0 + QM7 + NO frags + b5-const +
  M-tails NEW, T88-RING-SWAPPED + TM7-by-ROW/TR7-by-
  COL + tails-swapped + b84-87 5ad8e80b + edges +
  consts; plus sheet-vs-tables const-count note: Q-918
  sheet 79/82/54/72 memo-exact, committed tables
  78/81/53/72 still deduct const-b5 on PBA/C10/quad --
  S-F arithmetic in tables only, geometry exact, PORT
  verdict stands; section-F clean (65/65, novelty is
  the SWAPPED frame, no gloss issue this tier); M==RQ
  full-equality unmentioned by memo, batteries
  confirm, tier stands).
  Agrees with cport commit msg (PYID 9690, RGRAM
  19380). No viewer P326 geometry answer on file at
  gate time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b434 (own
  seat CLAIM only; exactly 1 GATE-b6adc780; zero FLAG
  hits; even base b433 respected; b435 = sweep turf
  untouched, used as nothing here). PROSE-01: all
  hex/counts above copied from own run output; GATE-
  b6adc780 re-read in FULL before filing (1 resolved
  convention note below, substance exact).
- RQ==M chain: b434 EVEN FULL-eq-positions-identical
  (QM7 b52-54,80-83 == RQ7 b52-54,80-83 slots; M0==
  RQ0 f1deef7df176b9; ordered-equal 16/16). No
  ordinal (viewer evens convention as above).
- TRUE-uniform chain: 21st case (20th excl P299):
  P326 S1-vs-C10 [46/88]x10 staged+oracle NEW this
  band (GATE/memo cell0-only; beyond-GATE finding,
  code GREEN since gated artifact == verified
  artifact).

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 resolved convention note (AC-QC "both=53
sameval=43" reads as 53 common byte positions / 43
same value, verified first-hand per-byte; the
set-intersection reading (39) is the wrong convention;
code GREEN since gated artifact == verified artifact).
