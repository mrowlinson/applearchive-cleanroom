# GATE 33d2c85b b432 T10P324 pins 129489..129836 (1932 tiers) PASS-functional

Seat sweep2-r71, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r71/w432 @33d2c85b.
Band = f5a4d51d (py merge w2b@2b4193d8 partial, +6 tiers, +64 pins)
+ 33d2c85b (C port). Base 608c167f (b431 tip, 1926 tiers sealed,
GATE-filed PASS-functional by odd seat).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both);
w432 +__pycache__ battery byproduct after runs, w431base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build432/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 93cd6068 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r71
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9628/9628 covered=9628/9628 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 19256/19256 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 19256/19256 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 19256/19256).
- PINS-RGRAM cells set-eq 19256/19256 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9628/9628 xor 0;
  PINS 19258 rows (2 hdr + 19256 = PASS lines, +64 vs base
  19194). For-list union 9596->9628 +32 (129489 129490
  129491 129492 129498 129499 129505 129506 129507 129508
  129511 129512 129515 129516 129517 129532 129533 129535
  129536 129548 129549 129564 129565 129580 129581 129644
  129645 129663 129664 129791 129792 129836),
  0 removed, range 129489..129836 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 32x2 = 64 = 19256-19192.
  The 32 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid/tail pairs (6) + Q head/2-mids/B5EDGE-pair/
  2-mids/2-mids/tail (10: head 129517, mids 129532/129533,
  B5EDGE pair 129535/129536 pinned off18/19, mids
  129548/129549 + 129564/129565, tail 129580) +
  R head/sig-pair/edge-pairs/tail (8: head 129581,
  2SIG-boundary pair 129644/129645 off63/64, edge pairs
  129663/129664 + 129791/129792, tail 129836).
  PINS-new-N == for-added 32/32 (4th set-eq way),
  PINS removed 0. PINS numstat 64/0 clean append (all in
  py-merge leg 608c167f..f5a4d51d; C-port leg touched zero
  PINS rows); all 19256 rows test_rgram_fast.py-tagged;
  cols1-4 purity +64/-0, cols5-7 unchanged first-hand.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P324 C-vs-py, script-compared, TABAUDIT-GREEN
  508 PASS 0 FAIL (tabaudit324.py rc=0, fourth run: 2 seat
  script bugs fixed first, prefix-strip off-by-one + PAIRW
  triple-underscore regex, then LCS convention aligned to
  memo tail-LCS with first-hand full-LCS recorded):
  S0 168ch sig b7ce3001 NEW (32/84 payload diff vs P323S0
  first-hand, NOT byte-equal; sig differs vs P323 heads
  b7ce7001/02000000) / S1 176ch sig 02000000 sig-eq-P323PB1
  (41/88 payload diff vs P323S1 n129142, NOT byte-equal;
  59/88 diff vs own-C10[0] assembled n129507, NOT byte-equal;
  sig SAME-as-own-C10; differs vs own PB0), staged as
  full-payload singletons,
  AM 16/16 16ch distinct, CM 10/10 8ch distinct, M 16/16
  18ch distinct, QR 4/4 22ch distinct, RM 16/16 12ch
  distinct, RQ 16/16 18ch distinct UNPAIRED, no QT
  (quad tails live in R11) + no RT (2SIG-B0ROW tails) +
  no F (no frag this tier),
  M-vs-RQ TAILS-EQ 16/16 positional (M b80-83 == RQ b76-79
  per index) with full strings 0/16 identical (QM9 heads
  b13-17 vs TR9 heads b0,9-11,16 differ; running pattern:
  b414 full-eq, b416 tail-eq, b418 full-eq, b420/b422
  string-eq-positions-differ, b424 tail-eq-positions-differ,
  b426 full-eq, b428/b430 string-eq-tails-split, b432
  tails-eq-strings-differ),
  AC 78, CC 82, QC 66, RC 71; C _N decls 78/82/66/71
  match actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M8b6 sig 29000000 (b0 const 29, b5 const
  f3 via raw lencode; AM 16/16 distinct NO pair; M8
  b6-9,80-83) + vs P323PBA 2d000000 (novelty =
  new sig 29 + AM 0-overlap).
  C10-1SIG-88-TAIL sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 8ch:
  a4ebc6d4/c4ebc6d4/e4ebc6d4/dc3c4cd7/61f523f4/
  81f523f4/4c3172f9/6c3172f9/8c3172f9/ac3172f9;
  CC has no b5, b5 const f3 full block via lencode).
  QUAD88-1SIG-4R-NOFRAG-B5EDGE 1-sig 26000000 x64
  DIFFERS-from-PBA-sig (QC b0 const 26; b5 edge f3->f4
  @off18/19, edge 129535 ff/f3 -> 129536 01/f4, exactly
  1 ff in 64; QM9 b13-17,80-83 16/16 distinct NO
  frags + R11 b6-8,52-55,84-87 rows 4/4 NO
  pairing pairwise-disjoint: r0/r1 share 7B prefix
  5f4c22c5da3764, differ in 8th byte b84 (02 vs 92);
  r2/r3 full tuples unequal; full-LCS r01=8 (prefix-7 +
  b87-23),
  tails b84-87 4/4 distinct 02bb2623/927c7623/
  60f8796f/6435f8a3, r01 pair-only 1B 0x23 @b87,
  b87 NOT const quad-wide [23,23,6f,a3],
  tail-LCS r01-vs-r23 cross 0/0/0/0, tail-LCS r2r3=1
  (shared byte 0xf8; full-LCS r2r3=3; cross full-LCS
  02=1/03=1/12=0/13=1 recorded first-hand).
  Ring 2SIG-B0ROW: 50020000 x64 (rows0-3) + 19020000
  x192 (rows4-15); TM6 b18,19,80-83 by COL RM 16/16 +
  TR9 b0,9-11,16,76-79 by ROW RQ 16/16 UNPAIRED;
  b0 row-led (50 rows0-3, 19 rows4-15, all 16 row
  heads verified); sig boundary off63/64 =
  129644->129645 pinned in for-list; b1 const 02;
  b84-87 a17b14ad ring-wide NEW.
  VPOS partitions re-derived from code: PBA 9
  (b4+M8) / C10 5 (b4+M4 b84-87) / quad 22
  (b4,b5+QM9+R11) / T 17 (b0,b4,b5+TM6+TR9)
  -- all match A-834.
  Code-consts vs A-834 (PBA 79 / C10 83 /
  quad 66 / T88 71): impl 78/82/66/71 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-916 sheet counts b5 (memo A-834 confirms the
  sheet AND the excl-b5 convention accounted) --
  S-F arithmetic persists in committed tables though
  the sheet is FIXED; memo-exact on quad (b5 edge-varies,
  in VPOS) and T88 (b5 varies, no deduction); geometry
  exact, PORT verdict stands; FLAGGED for memo (11th
  band running: b412/b414/b416/b418/b420/b422/b424/
  b426/b428/b430/b432; PBA/C10 lag this tier).
  QUAD 1SIG 26 DIFFERS-from-PBA-sig 29 this tier (vs
  P322 SAME-sig-as-PBA tier); PBA sig 29 NEW vs P323 2d;
  AC-QC both=65 sameval=8 (tables differ).
  M-tails 16/16 ALL NEW vs P323 (zero overlap vs
  P323M AND vs P323RM-tail8 AND vs P323RQ-tail8).
  AM/CM/M/QR/RM/RQ 0-overlap vs P323 (prev lens
  16/10/16/4/16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=129489 (PB0 sig b7ce3001 NEW, 32/84 diff,
  lenB 84),
  S1 n=129490 (fat PB1 sig 02000000 sig-eq-P323PB1,
  41/88 diff vs P323S1 n129142, 59/88 diff vs C10[0]
  n129507, lenB 88),
  A 129491-506 PBA88-PLAIN-M8b6 (sig 29000000 via AC
  b0-b3, b0 const 29, AM 16/16 distinct 16ch, mtab
  b6-9,80-83, raw lencode b5 const f3),
  C 129507-516 C10-1SIG-88-TAIL (02000000 x10
  SAME-as-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87, b5 const f3 raw lencode),
  Q 129517-580 QUAD88-1SIG-4R-NOFRAG-B5EDGE (QM9
  b13-17,80-83 M 16/16 18ch + R11 b6-8,52-55,84-87
  rows above (4/4 NO pairing, r01 share-7B-prefix)
  + tails above, NO frags, raw lencode b5=f3+(off>=19)
  edge 129535->129536),
  R 129581-836 T88-RING-2SIG-B0ROW (50020000 rows0-3
  + 19020000 rows4-15, TM6 b18,19,80-83 by COL RM
  16/16, TR9 b0,9-11,16,76-79 by ROW RQ 16/16
  UNPAIRED, b0 row-led 50x4/19x12, b1 const 02,
  b84-87 const a17b14ad ring-wide,
  b4=(0x5b+2off)&FF, b5=0xf4+(off>=83)+(off>=211)).
  C blocks carry T86982/86987/86992/87007/87022/
  87043 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 16ch,
  C 8ch, Q 18/22ch, R 12/18ch),
  A/C/Q raw lencode (no counter literals) +
  R counter b4=(0x5b+2off)&FF + (off>=83)+(off>=211)
  (C literals 91/244 verified == 0x5b/0xf4),
  temps _t6635-6650 (base max _t6634, no reuse) +
  _i4016/4018/4021/4024 (base max _i4014,
  no reuse) + _b4015/4017/4019/4020/4022/4023
  (base max _b4013, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P323R close
  (C 231472-74, block 231475; py CLOSED 86980, guard
  86982), at dispatch tail (N-out-of-scope fallthrough
  follows: C 231663, py 87062; early same-text guards at
  C 155925 / py 53671 are the T4-plateau-B n<=1077 check,
  unrelated scope).
  Matches A-834 geometry (PB0 NEW-sig b7ce3001 32/84;
  PB1 sig-eq-P323PB1 41/88 SAME-as-C10 59/88;
  PBA88-PLAIN-M8b6 VPOS 9 sig-29 b5 const f3 M8
  16/16 distinct; C10-TAIL VPOS 5 SAME-as-PB1-sig
  b5 const M4 10/10 diverge; QUAD88-1SIG-4R-NOFRAG-
  B5EDGE VPOS 22 + R11 4/4 UNPAIRED + r01-share-7B +
  r01-paironly-23 + b87-[23,23,6f,a3] + cross-tail-
  lcs0 + QM9 + NO frags + b5-edge-off19 + M-tails NEW;
  T88-RING-2SIG-B0ROW VPOS 17 + TM6/TR9 + b0-row-led +
  sig-boundary-off63/64 + b84-87 a17b14ad + counter
  5b/f4/83/211; lencode 348/348 whole-tier, Q b5 edge
  129535->129536, ring edges 129663->129664 +
  129791->129792, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R11 rows + tails + LCS,
  2SIG-B0ROW split + consts stand; sheet-vs-tables
  const-count note is S-F arithmetic in tables only
  per memo, geometry unaffected; lcs-gloss §F is
  comment-only per memo, bytes unaffected; M-vs-RQ
  tails-eq unmentioned by memo, batteries confirm,
  tier stands).
- Edges via counter formula first-hand: A head a7/f3
  tail c5/f3 b5set {f3} NO step, 0 ff;
  C head c7/f3 tail d9/f3 b5set {f3} NO step, 0 ff;
  Q head db/f3 edge 129535 (off18, ff/f3) ->
  129536 (off19, 01/f4) tail 59/f4, exactly 1 ff in 64
  (b5 edge f3->f4 @off19);
  ring 129663 (off82, ff/f4) -> 129664 (off83, 01/f5);
  129791 (off210, ff/f5) -> 129792 (off211, 01/f6);
  exactly 2 ff in 256; R head 5b/f4 tail
  59/f6 (Q tail 59/f4 vs R tail 59/f6 differ in b5 --
  labeled apart); formulas re-derived from T10P324Q
  lencode (db/f3/19) + T10P324R text
  (5b/f4/83/211) + T10P324A/C text
  (raw lencode, b5 const f3); all edge pins + sig-pair
  + tail 129836 in for-list + 2 PASS lines each py+C.
  S0/S1 embedded b4/b5 (a3/f3, a5/f3) match raw lencode.
  Odd-lencode 348/348. No DISSENT on cut bytes
  (edges324.py EDGES-GREEN 171 PASS 0 FAIL, first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 230/0 (rgram.py) + 1/1 (for-line) +
  64/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 429).
- Wall on band diff added lines (scope 608c167f..
  33d2c85b, 903 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 670->672 +2 /
  ranges 726->730 +4 = +6, C identical deltas 670->672
  +2 / 726->730 +4 (py=C dispatch-exact deltas; no
  elif added either side: py file-wide elif 48->48
  pre-existing elsewhere, C else-if 0->0; deltas agree
  every side), CLOSED T10P prints 1832->1838 +6 both
  sides, seal 1926->1932 +6 (commit msgs): all agree,
  no slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-834-q916-P324
  verdict CONFIRM 67/68 + section-F (own bed r3-P324
  129489..129868 BAD=0 + own r3-P323, verifier v220.py
  67/68 PASS, single FAIL = Q-claim witness; file
  present, counts verified; geometry GATED PORT, writer
  corrects lcs gloss per section-F, no table impact;
  exact-value corroboration incl PB0 NEW-sig b7ce3001
  32/84, PB1 sig-eq-P323PB1 41/88 SAME-as-C10 59/88,
  PBA88-PLAIN-M8b6 sig-29 M8, C10-TAIL SAME-as-PB1-sig
  M4, QUAD88-1SIG-4R-NOFRAG-B5EDGE 1-sig-26 + R11 rows +
  r01-share-7B + r01-paironly-23 + b87-[23,23,6f,a3] +
  cross-tail-lcs0 + QM9 + NO frags + b5-edge-off19 +
  M-tails NEW, T88-RING-2SIG-B0ROW + TM6/TR9 + b0-row-led
  + sig-boundary-off63/64 + b84-87 a17b14ad + edges +
  consts; plus sheet-vs-tables const-count note: Q-916
  sheet 79/83/66/71 memo-exact, committed tables
  78/82/66/71 still deduct const-b5 on PBA/C10 --
  S-F arithmetic in tables only, geometry exact, PORT
  verdict stands; plus section-F: r2/r3 tails share
  byte 0xf8 so code comment "other pairs lcs=0"
  overclaims -- seat confirms first-hand tail-LCS
  r2r3=1 (full-LCS 3) with cross pairs 0/0/0/0,
  comment-gloss only, bytes unaffected).
  Agrees with cport commit msg (PYID 9628, RGRAM 19256).
- FWD-check first-hand: A-834 "Next P325" forward note
  verified against P325 lane code (6cb51277, no checkout):
  PB0 b7ce3001 SAME-sig-as-P324PB0 32/84 @129837 + PB1
  02000000 66/88 vs n129490 @129838 + PBA88
  21000000 x16 @129839-54 + C10 04000000 x10 @129855-64
  DIFFERS-from-PB1-sig -- all exact, same-sig era
  continues (P324 PB0 b7ce3001 was NEW vs P323 b7ce7001;
  P325 PB0 retains it).
- Quiz: no conflicting CLAIM/GATE/FLAG on b432 (adjacent
  odds b431/b433 GATED-or-sweep-turf: b431 GATE filed PASS
  by odd seat, base-use and adjacency acknowledged;
  b433 = sweep-r70 live turf per CLAIM-encode-sweep, no
  verdict on b432; both adjacency notes, no verdict
  on b432).
  Activity polled (no b432 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r71/ (build432.log,
  build432.sha, pyid432.log, rgram432py/c.log, cmp432.py/
  .c/.pyo/.co, for432.nums/for431base.nums, for432.added,
  pass432.names/pins432.names, pins432N.nums/
  pins431N.nums, pins432added.nums, smoke432.log,
  units432.log, tables432.log, tabaudit324.py, edges324.py,
  edges432.log, numstat432.txt/py/c, addnorm432.txt,
  delnorm432.txt, alladded432.txt, fwd325.txt,
  banddiff via git, pydiff324.txt, cdiff432.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
