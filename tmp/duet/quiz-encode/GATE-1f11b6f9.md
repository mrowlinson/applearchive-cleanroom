# GATE 1f11b6f9 b436 T10P328 pins 130881..131228 (1956 tiers) PASS-functional

Seat sweep2-r72, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r72/w436 @1f11b6f9.
Band = a83869f9 (py merge w2b@24550308 partial, +6 tiers, +62 pins)
+ 1f11b6f9 (C port). Base a60294b6 (b435 tip, 1950 tiers sealed,
GATE-filed PASS-functional by odd seat).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build436/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc d228bdad / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r72
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9752/9752 covered=9752/9752 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 19504/19504 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 19504/19504 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 19504/19504).
- PINS-RGRAM cells set-eq 19504/19504 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9752/9752 xor 0;
  PINS 19506 rows (2 hdr + 19504 = PASS lines, +62 vs base
  19444). For-list union 9721->9752 +31 (130881 130882
  130883 130884 130890 130891 130897 130898 130899 130900
  130903 130904 130907 130908 130909 130924 130925 130940
  130941 130943 130944 130956 130957 130972 130973 131071
  131072 131150 131199 131200 131228),
  0 removed, range 130881..131228 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 19504-19442.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid/tail pairs (6) + Q head/row-boundary-pairs/
  B5EDGE-pair/tail (10: head 130909 off0, pairs 130924/
  130925 off15/16 + 130940/130941 off31/32, B5EDGE pair
  130943/130944 pinned off34/35, pair 130956/130957
  off47/48, tail 130972 off63) +
  R head/sig-pair/mid/edge-pair/tail (7: head 130973 off0,
  sig-boundary+lencode pair 131071/131072 off98/99, mid
  131150 off177, edge pair 131199/131200 off226/227,
  tail 131228 off255).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0. PINS numstat 62/0 clean append (all in
  py-merge leg a60294b6..a83869f9; C-port leg touched zero
  PINS rows); all 19504 rows test_rgram_fast.py-tagged;
  cols1-4 purity +62/-0, cols5-7 unchanged first-hand
  (test_rgram_fast.py/27.0.1/ct-lzraven uniform both).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir, os 27.0.1).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P328 C-vs-py, script-compared, TABAUDIT-GREEN
  129 PASS 0 FAIL (tabaudit328.py rc=0, second run: 1 seat
  script bug fixed first, C-search string for R-const failf):
  S0 168ch sig 575f8102 sig-eq-P327PB0 (30/84 payload diff vs
  P327S0 first-hand, NOT byte-equal; sig differs vs P327 C10
  heads) / S1 176ch sig 05000000 sig-eq-P327PB1 (80/88
  payload diff vs P327S1 n130534 first-hand, NOT byte-equal;
  29/88 diff vs own-C10[0] assembled n130899, NOT byte-equal;
  sig SAME-as-own-C10; differs vs own PB0), staged as
  full-payload singletons,
  AM 16/16 14ch distinct, CM 10/10 10ch distinct, M 16/16
  16ch distinct, QR 4/4 26ch distinct, RM 16/16 16ch
  distinct, RQ 16/16 16ch distinct UNPAIRED, no QT
  (quad tails live in R13) + no RT (MIDROW-SPLIT tails) +
  no F (no frag this tier),
  M==RQ FULL 16/16 string-identical INTRA-tier, byte
  positions DIFFER (tails-split: QM8 b40-43,80-83 vs TR8
  b40-43,76-79 slots; running pattern: b414 full-eq, b416
  tail-eq, b418 full-eq, b420/b422
  string-eq-positions-differ, b424 tail-eq-positions-differ,
  b426 full-eq, b428/b430 string-eq-tails-split, b432
  tails-eq-strings-differ, b434 full-eq-positions-identical,
  b435 full-identity (odd seat), b436
  string-eq-positions-differ; consistent with the cross-band
  M==RQ running pattern),
  AC 79, CC 81, QC 65, RC 61, RSA 9, RSB 9; C _N decls
  79/81/65/61/9/9 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b29 sig 42000000 (b0 const 42, b5 const
  fe via raw lencode NOT in AC; AM 16/16 distinct NO pair; M7
  b29,34,35,80-83) + vs P327PBA 50000000 (novelty =
  new sig 42 + AM 0-overlap).
  C10-1SIG-88-TAIL-M5b34 sig 05000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 10ch; b34 {f5 x5, f9 x5} first-hand;
  CC has no b5, b5 const fe full block via lencode).
  QUAD88-1SIG-4R-NOFRAG-B5EDGE 1-sig 6c000000 x64
  DIFFERS-from-PBA-sig (QC b0 const 6c; b5 edge fe->ff
  @off34/35, edge 130943 ff/fe -> 130944 01/ff, exactly
  1 ff in 64; b4 base 0xbb step2 64/64 range bb..ff,01..39;
  QM8 b40-43,80-83 16/16 distinct NO frags +
  R13 b29,30,33-39,84-87 rows 4/4 NO
  pairing pairwise-disjoint: r0/r1/r2 share 9B
  prefix b1b2c8e7f7b66ea269,
  differ in tails only with 3 distinct tail tuples;
  full tuples unequal; r3 full tuple unequal;
  tails b84-87 4/4 distinct 28b1be9f/48b1be9f/
  bf2401bd/0d10e165, r01 TRUE-3B b1be9f, r2/r3
  tail-LCS=0 vs all (full-LCS 9/9/0/9/0/0
  recorded first-hand);
  b87 set {9f,bd,65} NOT const).
  Ring 2SIG-MIDROW-SPLIT: sig ac050000 x99 (off0-98) +
  580b0000 x157 (off99-255); boundary off98/99 =
  N131071->131072 MID-row-6; code-TM8 b30,39,46,47,
  80-83 by COL RM 16/16 + code-TR8 b40-43,
  76-79 by ROW RQ 16/16 UNPAIRED (SPLIT tails
  b80-83 col / b76-79 row);
  SPLIT9 region-consts RSA off<99 / RSB off>=99
  (b0 ac/58, b1 05/0b, b6 67/cc, b7 bd/7a, b8 19/3a,
  b9 98/30, b10 17/2f, b11 1a/34, b52 91/92, A/B
  99/157 cells); b2/b3 const 00 ring-wide;
  b84-87 b6865167 ring-wide NEW.
  VPOS partitions re-derived from code: PBA 8
  (b4+M7) / C10 6 (b4+M5) / quad 23
  (b4,b5+QM8+R13) / T 27
  (b0,b1,b4,b5+TM8+TR8+SPLIT9-union, b0/b1 shared)
  -- all match A-869.
  Code-consts vs A-869 INCL (PBA 80 / C10 82 /
  quad 65 / T88 61): impl 79/81/65/61 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-1040 sheet counts b5 (memo A-869 confirms the
  sheet INCL values) -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  memo-exact on quad (b5 edge-varies, in VPOS)
  and T88 (b5 counter-varies, no deduction);
  geometry exact, PORT verdict stands; FLAGGED for
  memo (13th even band running: b412/b414/b416/b418/
  b420/b422/b424/b426/b428/b430/b432/b434/b436;
  PBA/C10 lag this tier).
  QUAD 1SIG 6c DIFFERS-from-PBA-sig 42 this tier;
  PBA sig 42 NEW vs P327 50; AC-QC both=65 sameval=49
  (tables differ).
  M-tails 16/16 ALL NEW vs P327 (zero overlap vs
  P327T RQ row-led tails).
  AM/CM/M/QR/RM/RQ 0-overlap vs P327 (QR widths
  differ 13B vs 10B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=130881 (PB0 sig 575f8102 sig-eq-P327PB0, 30/84 diff,
  lenB 84),
  S1 n=130882 (fat PB1 sig 05000000 sig-eq-P327PB1,
  80/88 diff vs P327S1 n130534, 29/88 diff vs C10[0]
  n130899, lenB 88),
  A 130883-898 PBA88-PLAIN-M7b29 (sig 42000000 via AC
  b0-b3, b0 const 42, AM 16/16 distinct 14ch, mtab
  b29,34,35,80-83, raw lencode b5 const fe),
  C 130899-908 C10-1SIG-88-TAIL-M5b34 (05000000 x10
  SAME-as-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 10ch b34,84-87, b34 {f5,f9}, b5 const fe
  raw lencode),
  Q 130909-972 QUAD88-1SIG-4R-NOFRAG-B5EDGE (QM8 b40-43,
  80-83 M 16/16 16ch + R13 b29,30,33-39,84-87
  rows above (4/4 NO pairing, r012 share-9B-prefix)
  + tails above, NO frags, raw lencode b5=fe+(off>=35)
  edge 130943->130944),
  R 130973-131228 T88-RING-2SIG-MIDROW-SPLIT (sig
  ac050000 off0-98 + 580b0000 off99-255,
  code-TM8 b30,39,46,47,80-83 by COL RM 16/16,
  code-TR8 b40-43,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT9 RSA off<99 / RSB off>=99, b2/b3 const 00,
  b84-87 const b6865167 ring-wide,
  b4=(0x3b+2off)&FF, b5=(0xff+(off>=99)+(off>=227))&FF).
  C blocks carry T87941/87946/87951/87966/87981/
  88002 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 14ch,
  C 10ch, Q 16/26ch, R 16/16ch),
  A/C/Q raw lencode (no counter literals) +
  R counter b4=(0x3b+2off)&FF + (off>=99)+(off>=227)
  (C literals 59/255 verified == 0x3b/0xff),
  temps _t6701-6716 (base max _t6700, no reuse) +
  _i4056/4058/4061/4064/4065 (base max _i4054,
  no reuse) + _b4055/4057/4059/4060/4062/4063
  (base max _b4053, no reuse), all 6 blocks verified.
  C R-block carries rs/rs_n region-select (RSA off<99 /
  RSB off>=99, FIRST-ported b7-anchored locals).
  Insert position exact both sides: after T10P327R close
  (C 233957-59, comment 233960, block 233961; py CLOSED 87939, guard
  87941), at dispatch tail (N-out-of-scope fallthrough
  follows: C 234161, py 88025; early same-text guards at
  C 157633 / py 54298 are the T4-plateau-B n<=1077 check,
  unrelated scope).
  Matches A-869 geometry (PB0 sig-eq-P327PB0 30/84;
  PB1 sig-eq-P327PB1 80/88 SAME-as-C10 29/88;
  PBA88-PLAIN-M7b29 VPOS 8 sig-42 b5 const fe M7
  16/16 distinct; C10-1SIG-88-TAIL-M5b34 VPOS 6
  SAME-as-PB1-sig b5 const b34-{f5,f9} M5 10/10
  diverge; QUAD88-1SIG-4R-NOFRAG-B5EDGE VPOS 23 +
  R13 4/4 UNPAIRED + r012-share-9B + r01-TRUE-3B +
  r2/r3-lcs0 + b87-{9f,bd,65} + QM8 + NO frags +
  b5-edge-off35 + M-tails NEW;
  T88-RING-2SIG-MIDROW-SPLIT VPOS 27 + TM8-by-COL/
  TR8-by-ROW + SPLIT9 + b2/b3-00 + b84-87 b6865167 +
  counter 3b/ff/99/227 + wrap ff->00->01; lencode
  348/348 whole-tier, Q b5 edge 130943->130944, ring
  edges 131071->131072 (COINCIDES sig boundary) +
  131199->131200, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R13 rows + tails + LCS,
  MIDROW-SPLIT split + consts stand; sheet-vs-tables
  const-count note is S-F arithmetic in tables only
  per memo, geometry unaffected; M==RQ
  string-eq-positions-differ unmentioned by memo,
  batteries confirm, tier stands).
- Edges via counter formula first-hand: A head 87/fe
  tail a5/fe b5set {fe} NO step, 0 ff;
  C head a7/fe tail b9/fe b5set {fe} NO step, 0 ff;
  Q head bb/fe edge 130943 (off34, ff/fe) ->
  130944 (off35, 01/ff) tail 39/ff, exactly 1 ff in 64
  (b5 edge fe->ff @off35; b4 base 0xbb step2 64/64
  range bb..ff,01..39);
  ring 131071 (off98, ff/ff) -> 131072 (off99, 01/00);
  131199 (off226, ff/00) -> 131200 (off227, 01/01);
  exactly 2 ff in 256; R head 3b/ff tail
  39/01 mid177 9d/00 (Q tail 39/ff vs R tail 39/01
  differ in b5 -- labeled apart); formulas re-derived
  from T10P328R code text (3b/ff/99/227) + T10P328A/C/Q
  text (raw lencode, b5 const fe / edge); all edge pins
  + mid 131150 + tail 131228 in for-list + 2 PASS lines
  each py+C. S0/S1 embedded b4/b5 (83/fe, 85/fe)
  match raw lencode. Ring counter==raw-lencode 256/256.
  Odd-lencode 348/348. No DISSENT on cut bytes
  (edges328.py EDGES-GREEN 61 PASS 0 FAIL, first run).
- C diff purely additive: numstat 638 add / 0 del
  (rgramc.c) + 242/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 633 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 410).
- Wall on band diff added lines (scope a60294b6..
  1f11b6f9, 943 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 638/0, rgram.py 242/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 678->680 +2 /
  ranges 742->746 +4 = +6, C identical deltas 683->685
  +2 / 764->768 +4 (py=C dispatch-exact deltas; 5-count
  C-vs-py singleton offset pre-existing C-only dip
  guards, unchanged by band; no elif added either side:
  py file-wide elif 50->50 pre-existing elsewhere,
  C else-if 0->0; deltas agree every side), CLOSED T10P
  prints 1856->1862 +6 both sides, seal 1950->1956 +6
  (commit msgs; offset +94 vs CLOSED-T10P stable): all
  agree, no slip (absolute seal inherits lane tally;
  delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-869-q1040-P328
  verdict CONFIRM 67/67 CLEAN (own bed r3-P328
  130881..131260 BAD=0 + own r3-P327, verifier v255.py
  67/67 PASS; file present, counts verified; geometry
  GATED PORT, major novelty 2SIG-MIDROW-SPLIT T-ring
  gated; exact-value corroboration incl PB0
  sig-eq-P327PB0 30/84, PB1 sig-eq-P327PB1 80/88
  SAME-as-own-C10 29/88, PBA88-PLAIN-M7b29 sig-42 M7,
  C10-1SIG-88-TAIL-M5b34 SAME-as-PB1-sig b34-{f5,f9},
  QUAD88-1SIG-4R-NOFRAG-B5EDGE 1-sig-6c + R13 rows +
  r012-share-9B + r01-TRUE-3B + r2/r3-lcs0 +
  b87-{9f,bd,65} + QM8 + NO frags + b5-edge-off35 +
  M-tails NEW, T88-RING-2SIG-MIDROW-SPLIT + TM8-by-COL/
  TR8-by-ROW + SPLIT9 + b2/b3-00 + b84-87 b6865167 +
  counter + wrap + edges; plus sheet-vs-tables
  const-count note: Q-1040 sheet 80/82/65/61 memo-exact,
  committed tables 79/81/65/61 still deduct const-b5 on
  PBA/C10 -- S-F arithmetic in tables only, geometry
  exact, PORT verdict stands) + A-1040-q1040-P328
  verdict CONFIRM 46/46 CLEAN (own bed r6-P328
  130881..131256 + r6-P327, BAD=0 + direct-oracle 2/2
  byte-match, verifier v600f3.py 46/46 PASS; file
  present, counts verified; tier GATED PORT; suffix-lcs
  3/0/0/0/0/0 + M-tails NEW + SPLIT9 EXACT + consts excl
  79/81/65/61 script-claimed corroborated).
  Agrees with cport commit msg (PYID 9752, RGRAM 19504).
- FWD-check first-hand: A-869 "Next P329" forward note
  verified against P329 lane code (56829bfc, no checkout):
  PB0 eed6f805 NEW-sig 40/84 @131229 + PB1
  0b000000 NEW-sig 67/88 vs n130882 @131230 +
  PBA88 d8000000 x16 @131231-246 + C10
  0b000000 x10 SAME-as-PB1-sig @131247-256
  -- all exact, new-sig era opens (P328 PB0
  575f8102 was SAME-as-P327PB0; P329 PB0 breaks new).
- Quiz: no conflicting CLAIM/GATE/FLAG on b436 (adjacent
  odds b435/b437: b435 GATE filed PASS by odd seat,
  base-use and adjacency acknowledged; b437 = cport-r56
  live cut (py merge 56829bfc landed, C-port pending),
  no verdict on b436; both adjacency notes, no verdict
  on b436).
  Activity polled (no b436 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r72/ (build436.log,
  build436.sha, pyid436.log, rgram436py/c.log, cmp436.py/
  .c/.pyo/.co, for436.nums/for435base.nums, for436.added,
  pass436.names/pins436.names, pins436N.nums/
  pins435N.nums, pins436added.nums, smoke436.log,
  units436.log, tables436.log, tabaudit328.py, edges328.py,
  edges436.log, numstat436.txt, addnorm436.txt,
  delnorm436.txt, alladded436.txt, fwd329.txt, p329.py,
  banddiff via git, pydiff via git, cdiff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
