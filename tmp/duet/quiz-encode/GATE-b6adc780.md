# GATE b6adc780 b434 T10P326 pins 130185..130532 (1944 tiers) PASS-functional

Seat sweep2-r71, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r71/w434 @b6adc780.
Band = 85843096 (py merge w2b@55ac18d2 partial, +6 tiers, +62 pins)
+ b6adc780 (C port). Base 6cb51277 (b433 tip, 1938 tiers sealed,
GATE-filed PASS-functional by odd seat).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both);
w434 +__pycache__ battery byproduct after runs, w433base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build434/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4f5d448b / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r71
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9690/9690 covered=9690/9690 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 19380/19380 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 19380/19380 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 19380/19380).
- PINS-RGRAM cells set-eq 19380/19380 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9690/9690 xor 0;
  PINS 19382 rows (2 hdr + 19380 = PASS lines, +62 vs base
  19320). For-list union 9659->9690 +31 (130185 130186
  130187 130188 130194 130195 130201 130202 130203 130204
  130207 130208 130211 130212 130213 130228 130229 130237
  130244 130245 130260 130261 130269 130276 130277 130303
  130304 130405 130431 130432 130532),
  0 removed, range 130185..130532 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 19380-19318.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid/tail pairs (6) + Q head/8-mids/tail (10:
  head 130213, mids 130228/130229/130237/130244/130245/
  130260/130261/130269, tail 130276, NO step this
  tier, quad b5 const) +
  R head/edge-pair/mid/edge-pair/tail (7: head 130277,
  edge pair 130303/130304, mid 130405, edge pair
  130431/130432, tail 130532).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0. PINS numstat 62/0 clean append (all in
  py-merge leg 6cb51277..85843096; C-port leg touched zero
  PINS rows); all 19380 rows test_rgram_fast.py-tagged;
  cols1-4 purity +62/-0, cols5-7 unchanged first-hand.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P326 C-vs-py, script-compared, TABAUDIT-GREEN
  491 PASS 0 FAIL (tabaudit326.py rc=0, second run: 1 seat
  parser fix, mtab-window grabbed lencode lines):
  S0 168ch sig 575f0102 NEW (34/84 payload diff vs P325S0
  first-hand, NOT byte-equal; sig differs vs P325 heads
  b7ce3001/02000000 + C10-region 04000000) / S1 176ch
  sig 04000000 sig-eq-P325C10region (37/88 payload diff vs
  P325C10[0] n129855 assembled first-hand, NOT byte-equal;
  46/88 diff vs own-C10[0] assembled n130203, NOT
  byte-equal; sig DIFFERS-from-own-C10 04-vs-05; differs
  vs own PB0), staged as full-payload singletons,
  AM 16/16 16ch distinct, CM 10/10 10ch distinct, M 16/16
  14ch distinct, QR 4/4 52ch distinct, RM 16/16 14ch
  distinct, RQ 16/16 14ch distinct UNPAIRED, no QT
  (quad tails live in R26) + no RT (SWAPPED tails) +
  no F (no frag this tier),
  M==RQ FULL 16/16 string-identical INTRA-tier, byte
  positions IDENTICAL (QM7 b52-54,80-83 == RQ7 b52-54,
  80-83 slots; running pattern: b414 full-eq, b416
  tail-eq, b418 full-eq, b420/b422
  string-eq-positions-differ, b424 tail-eq-positions-differ,
  b426 full-eq, b428/b430 string-eq-tails-split, b432
  tails-eq-strings-differ, b434 full-eq-positions-identical;
  consistent with the cross-band M==RQ running pattern,
  sweep-r70 notes 34th odd-band RQ==M instance),
  AC 78, CC 81, QC 53, RC 72; C _N decls 78/81/53/72
  match actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M8b38 sig 79000000 (b0 const 79, b5 const
  f9 via raw lencode; AM 16/16 distinct NO pair; M8
  b38,39,46,47,80-83) + vs P325PBA 21000000 (novelty =
  new sig 79 + AM 0-overlap).
  C10-1SIG-88-DIFFSIG-M5b45 sig 05000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 10ch: 27cf164acd/27ef164acd/270f174acd/
  274e174acd/6781cfc401/67a1cfc401/67c1cfc401/
  67e1cfc401/6720d0c401/675a627102; b45 {27 x4, 67 x6};
  CC has no b5, b5 const f9 full block via lencode).
  QUAD88-2SIG-4R-NOFRAG 79000000 x48 (rows0-2)
  SAME-sig-as-PBA + 2d000000 x16 (row3) (QC has no b0,
  b0 row-led in tab; b5 const f9 full 64, NO step,
  0 ff; b4 base 0x4b step2 64/64 range 4b..c9 NO
  edge; QM7 b52-54,80-83 16/16 distinct NO frags +
  R26 b0,11,19,26-35,38,39,45-51,84-87 rows 4/4 NO
  pairing pairwise-disjoint: r0/r1/r2 share 22B
  prefix 79d7f8453c4dffc26b60c7947f945d671f4f75088d1c,
  differ in tails only with 3 distinct tail tuples;
  full tuples unequal; r3 full tuple unequal;
  tails b84-87 4/4 distinct 99627102/48ce7102/
  68ce7102/1e156fc8, r12 TRUE-3B ce7102, r0 shares
  exactly 2B 7102 with r1/r2, r3 tail-LCS=0 vs all
  (full-LCS 2); tail-LCS r01=2/r02=2/r12=3;
  full-LCS r01=24/r02=24/r12=25 recorded first-hand).
  Ring SWAPPED: sig 9d070000 x256; code-RM7 b6,7,9,
  76-79 by COL off&15 RM 16/16 + code-RQ7 b52-54,
  80-83 by ROW off>>4 RQ 16/16 UNPAIRED (tails
  SWAPPED b80-83 row / b76-79 col per A-836: memo-TM7
  by ROW = code-RQ slots, memo-TR7 by COL = code-RM
  slots, label swap); b0 const 9d b1 const 07;
  b84-87 5ad8e80b ring-wide NEW.
  VPOS partitions re-derived from code: PBA 9
  (b4+M8) / C10 6 (b4+M5 b45,84-87) / quad 34
  (b4+QM7+R26, b0 inside R26 no double-count) /
  T 16 (b4,b5+TM7+TR7) -- all match A-836.
  Code-consts vs A-836 (PBA 79 / C10 82 /
  quad 54 / T88 72): impl 78/81/53/72 =
  writer-1 on PBA/C10/quad: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-918 sheet counts b5 -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  memo-exact on T88 (b5 varies, no deduction);
  geometry exact, PORT verdict stands; FLAGGED for
  memo (12th band running: b412/b414/b416/b418/b420/
  b422/b424/b426/b428/b430/b432/b434; PBA/C10/quad
  lag this tier).
  QUAD 2SIG 79/2d rows0-2-SAME-as-PBA vs P325; PBA
  sig 79 NEW vs P325 21; AC-QC both=53 sameval=43
  (tables differ).
  M-tails 16/16 ALL NEW vs P325 (zero overlap vs
  P325M AND vs P325RM-tail8 AND vs P325RQ-tail8).
  AM/CM/M/QR/RM/RQ 0-overlap vs P325 (prev lens
  16/10/16/4/16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=130185 (PB0 sig 575f0102 NEW, 34/84 diff,
  lenB 84),
  S1 n=130186 (fat PB1 sig 04000000 sig-eq-P325C10region,
  37/88 diff vs P325C10[0] n129855, 46/88 diff vs C10[0]
  n130203, lenB 88),
  A 130187-202 PBA88-PLAIN-M8b38 (sig 79000000 via AC
  b0-b3, b0 const 79, AM 16/16 distinct 16ch, mtab
  b38,39,46,47,80-83, raw lencode b5 const f9),
  C 130203-212 C10-1SIG-88-DIFFSIG-M5b45 (05000000 x10
  DIFFERS-from-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 10ch b45,84-87, b45 {27,67}, b5 const f9
  raw lencode),
  Q 130213-276 QUAD88-2SIG-4R-NOFRAG (QM7 b52-54,80-83 M
  16/16 14ch + R26 b0,11,19,26-35,38,39,45-51,84-87
  rows above (4/4 NO pairing, r012 share-22B-prefix)
  + tails above, NO frags, raw lencode b5 const f9
  b4 4b..c9),
  R 130277-532 T88-RING-SWAPPED (sig 9d070000,
  code-RM7 b6,7,9,76-79 by COL RM 16/16, code-RQ7
  b52-54,80-83 by ROW RQ 16/16 UNPAIRED, b0 const
  9d b1 const 07, b84-87 const 5ad8e80b ring-wide,
  b4=(0xcb+2off)&FF, b5=0xf9+(off>=27)+(off>=155)).
  C blocks carry T87468/87473/87478/87493/87508/
  87532 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 16ch,
  C 10ch, Q 14/52ch, R 14/14ch),
  A/C/Q raw lencode (no counter literals) +
  R counter b4=(0xcb+2off)&FF + (off>=27)+(off>=155)
  (C literals 203/249 verified == 0xcb/0xf9),
  temps _t6669-6684 (base max _t6668, no reuse) +
  _i4036/4038/4041/4044 (base max _i4034,
  no reuse) + _b4035/4037/4039/4040/4042/4043
  (base max _b4033, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P325R close
  (C 232711-13, block 232714; py CLOSED 87466, guard
  87468), at dispatch tail (N-out-of-scope fallthrough
  follows: C 232915, py 87551; early same-text guards at
  C 156772 / py 53988 are the T4-plateau-B n<=1077 check,
  unrelated scope).
  Matches A-836 geometry (PB0 NEW-sig 575f0102 34/84;
  PB1 sig-eq-P325C10region 37/88 DIFFERS-from-own-C10
  04-vs-05 46/88; PBA88-PLAIN-M8b38 VPOS 9 sig-79
  b5 const f9 M8 16/16 distinct; C10-DIFFSIG-M5b45
  VPOS 6 DIFFERS-from-PB1-sig b5 const b45-{27,67}
  M5 10/10 diverge; QUAD88-2SIG-4R-NOFRAG VPOS 34 +
  R26 4/4 UNPAIRED + r012-share-22B + r12-TRUE-3B +
  r0-2B-7102 + r3-lcs0 + QM7 + NO frags + b5-const +
  M-tails NEW; T88-RING-SWAPPED VPOS 16 + TM7-by-ROW/
  TR7-by-COL + tails-swapped + b84-87 5ad8e80b +
  counter cb/f9/27/155; lencode 348/348 whole-tier,
  NO quad edge, ring edges 130303->130304 +
  130431->130432, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R26 rows + tails + LCS,
  SWAPPED split + consts stand; sheet-vs-tables
  const-count note is S-F arithmetic in tables only
  per memo, geometry unaffected; M==RQ full-equality
  unmentioned by memo, batteries confirm, tier stands).
- Edges via counter formula first-hand: A head 17/f9
  tail 35/f9 b5set {f9} NO step, 0 ff;
  C head 37/f9 tail 49/f9 b5set {f9} NO step, 0 ff;
  Q head 4b/f9 tail c9/f9 b4 base 0x4b step2 64/64
  range 4b..c9 b5set {f9} NO step, 0 ff NO edge;
  ring 130303 (off26, ff/f9) -> 130304 (off27, 01/fa);
  130431 (off154, ff/fa) -> 130432 (off155, 01/fb);
  exactly 2 ff in 256; R head cb/f9 tail
  c9/fb (Q tail c9/f9 vs R tail c9/fb differ in b5 --
  labeled apart); formulas re-derived from T10P326R
  code text (cb/f9/27/155) + T10P326A/C/Q text
  (raw lencode, b5 const f9); all edge pins + mid
  130405 + tail 130532 in for-list + 2 PASS lines
  each py+C. S0/S1 embedded b4/b5 (13/f9, 15/f9)
  match raw lencode. Odd-lencode 348/348. No DISSENT
  on cut bytes (edges326.py EDGES-GREEN 160 PASS
  0 FAIL, first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 371).
- Wall on band diff added lines (scope 6cb51277..
  b6adc780, 902 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 674->676 +2 /
  ranges 734->738 +4 = +6, C identical deltas 674->676
  +2 / 734->738 +4 (py=C dispatch-exact deltas; no
  elif added either side: py file-wide elif 50->50
  pre-existing elsewhere, C else-if 0->0; deltas agree
  every side), CLOSED T10P prints 1844->1850 +6 both
  sides, seal 1938->1944 +6 (commit msgs): all agree,
  no slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-836-q918-P326
  verdict CONFIRM 65/65 CLEAN (own bed r3-P326
  130185..130564 BAD=0 + own r3-P325, verifier v222.py
  65/65 PASS; file present, counts verified; geometry
  GATED PORT, tier novelty SWAPPED-frame T;
  exact-value corroboration incl PB0 NEW-sig 575f0102
  34/84, PB1 sig-eq-P325C10region 37/88
  DIFFERS-from-own-C10 04-vs-05 46/88,
  PBA88-PLAIN-M8b38 sig-79 M8, C10-DIFFSIG-M5b45
  DIFFERS-from-PB1-sig b45-{27,67},
  QUAD88-2SIG-4R-NOFRAG 79x48-rows0-2-SAME-as-PBA +
  2d-row3 + R26 rows + r012-share-22B + r12-TRUE-3B +
  r0-2B-7102 + r3-lcs0 + QM7 + NO frags + b5-const +
  M-tails NEW, T88-RING-SWAPPED + TM7-by-ROW/TR7-by-COL
  + tails-swapped + b84-87 5ad8e80b + edges + consts;
  plus sheet-vs-tables const-count note: Q-918 sheet
  79/82/54/72 memo-exact, committed tables 78/81/53/72
  still deduct const-b5 on PBA/C10/quad -- S-F
  arithmetic in tables only, geometry exact, PORT
  verdict stands).
  Agrees with cport commit msg (PYID 9690, RGRAM 19380).
- FWD-check first-hand: A-836 "Next P327" forward note
  verified against P327 lane code (a60294b6, no checkout):
  PB0 575f8102 NEW-sig 31/84 @130533 + PB1
  05000000 sig-eq-P326C10region 84/88 vs n130203
  @130534 + PBA88 50000000 x16 @130535-550 + C10
  05000000 x10 SAME-as-PB1-sig @130551-560
  -- all exact, new-sig era continues (P326 PB0
  575f0102 was NEW vs P325; P327 PB0 breaks new again).
- Quiz: no conflicting CLAIM/GATE/FLAG on b434 (adjacent
  odds b433/b435 GATED PASS by odd seat -- b433 GATE
  filed PASS, b435 GATED per sweep-r70 HANDOFF (at cap,
  EXIT); base-use and adjacency acknowledged; both
  adjacency notes, no verdict on b434).
  Activity polled (no b434 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r71/ (build434.log,
  build434.sha, pyid434.log, rgram434py/c.log, cmp434.py/
  .c/.pyo/.co, for434.nums/for433base.nums, for434.added,
  pass434.names/pins434.names, pins434N.nums/
  pins433N.nums, pins434added.nums, smoke434.log,
  units434.log, tables434.log, tabaudit326.py, edges326.py,
  edges434.log, numstat434.txt/py/c, addnorm434.txt,
  delnorm434.txt, alladded434.txt, fwd327.txt,
  banddiff via git, pydiff326.txt, cdiff434.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
