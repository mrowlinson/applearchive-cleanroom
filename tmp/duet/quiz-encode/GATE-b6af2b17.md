# GATE b6af2b17 b430 T10P322 pins 128793..129140 (1920 tiers) PASS-functional

Seat sweep2-r70, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r70/w430 @b6af2b17.
Band = e5d6a3b5 (py merge w2b@f5cfd527 partial, +6 tiers, +62 pins)
+ b6af2b17 (C port). Base aaaaa11f (b429 tip, 1914 tiers sealed,
GATE-filed PASS-functional by odd seat).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both);
w430 +__pycache__ battery byproduct after runs, w429base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build430/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc dd0262c8 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r70
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9563/9563 covered=9563/9563 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 19126/19126 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 19126/19126 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 19126/19126).
- PINS-RGRAM cells set-eq 19126/19126 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9563/9563 xor 0;
  PINS 19128 rows (2 hdr + 19126 = PASS lines, +62 vs base
  19066). For-list union 9532->9563 +31 (128793 128794
  128795 128796 128802 128803 128809 128810 128811 128812
  128815 128816 128819 128820 128821 128828 128837 128844
  128853 128860 128869 128876 128883 128884 128885 128895
  128896 128950 129023 129024 129140),
  0 removed, range 128793..129140 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 19126-19064.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid/tail pairs (6) + Q head/7-mids/tail-pair (10:
  head 128821, mids 128828/128837/128844/128853/128860/
  128869/128876, tail pair 128883/128884, NO step this
  tier, quad b5 const) +
  R head/edge-pairs/mid/tail (7: head 128885, edge pairs
  128895/128896 + 129023/129024, mid 128950, tail 129140).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0. PINS numstat 62/0 clean append (all in
  py-merge leg aaaaa11f..e5d6a3b5; C-port leg touched zero
  PINS rows); all 19126 rows test_rgram_fast.py-tagged;
  cols1-4 purity +62/-0 first-hand.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P322 C-vs-py, script-compared, TABAUDIT-GREEN
  448 PASS 0 FAIL (tabaudit322.py rc=0, first run):
  S0 168ch sig 77435801 sig-eq-P321PB0 (47/84 payload
  diff vs P321S0 first-hand, NOT byte-equal) / S1 176ch
  sig 02000000 sig-eq-P321PB1 (76/88 payload diff vs
  P321S1, NOT byte-equal; 29/88 diff vs own-C10[0]
  assembled, NOT byte-equal; sig SAME-as-own-C10; differs
  vs own PB0), staged as full-payload singletons,
  AM 16/16 14ch distinct, CM 10/10 6ch distinct, M 16/16
  16ch distinct, QR 4/4 22ch distinct, RM 16/16 16ch
  distinct, RQ 16/16 16ch distinct UNPAIRED, no QT
  (quad tails live in R11) + no RT (STANDARD tails) +
  no F (no frag this tier),
  M==RQ 16/16 FULL string-identical INTRA-tier, byte
  positions PARTIALLY differ (QM8 b28-31,80-83 vs TR8
  b28-31,76-79: b28-31 shared positions, tails SPLIT
  b80-83 col / b76-79 row; running pattern: b414 full-eq,
  b416 tail-eq, b418 full-eq, b420/b422
  string-eq-positions-differ, b424 tail-eq-positions-differ,
  b426 full-eq, b428/b430 string-eq-tails-split),
  AC 79, CC 83, QC 67, RC 70; C _N decls 79/83/67/70
  match actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b20 sig 29000000 (b0 const 29, b5 const
  ee via raw lencode; AM 16/16 distinct NO pair; M7
  b20,21,22,80-83) + vs P321PBA 3d000000 (novelty =
  new sig 29 + AM 0-overlap).
  C10-1SIG-88-M3 sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 6ch:
  d269b8/f269b8/126ab8/326ab8/526ab8/
  b86ab8/38b8d4/58b8d4/78b8d4/98b8d4;
  CC b87 const 9f, CC has no b5, b5 const ee
  full block via lencode).
  QUAD88-1SIG-4R 1-sig 29000000 x64 SAME-sig-as-PBA
  (QC b0 const 29, b0 NOT in tab; b5 const ee full 64,
  NO step, 0 ff; b4 base 0x6b step2 64/64 range 6b..e9
  NO edge; QM8 b28-31,80-83 16/16 distinct NO frags +
  R11 b20-26,84-87 rows 4/4 NO pairing
  pairwise-disjoint: r0/r1 share 7B prefix 39da13aa3398e6,
  differ in first tail byte b84 (b8 vs d8); r2/r3 fully
  distinct; tails b84-87 4/4 distinct b8b8d49f/d8b8d49f/
  e23a1c36/d3ec8ee1, r01 TRUE-3B b8d49f, r2/r3-lcs0 vs
  all, r0r1-lcs3, all other pairs lcs0).
  Ring STANDARD: sig 5e020000 x256; TM8 b19,27,34,35,
  80-83 by COL RM 16/16 + TR8 b28-31,76-79 by ROW RQ
  16/16 UNPAIRED (tails SPLIT b80-83 col / b76-79 row);
  b0 const 5e b1 const 02; b84-87 2b3b1c36 ring-wide
  NEW (P321 STANDARD-split era per Q-914: P321T b80-83
  COL-led via RM).
  VPOS partitions re-derived from code: PBA 8
  (b4+M7) / C10 4 (b4+M3 b84-86) / quad 20
  (b4+QM8+R11, b5-const excluded) /
  T 18 (b4,b5+TM8+TR8) -- all match A-832.
  Code-consts vs A-832 (PBA 80 / C10 84 /
  quad 68 / T88 70): impl 79/83/67/70 =
  writer-1 on PBA/C10/quad: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-914 sheet counts b5 (memo A-832 confirms the
  sheet) -- S-F arithmetic persists in committed
  tables though the sheet is FIXED; memo-exact on
  T88 (b5 varies, no deduction); geometry exact,
  PORT verdict stands; FLAGGED for memo (10th band
  running: b412/b414/b416/b418/b420/b422/b424/b426/
  b428/b430; PBA/C10/quad lag this tier).
  QUAD 1SIG 29 SAME-as-PBA vs P321; PBA sig
  29 NEW vs P321 3d; AC-QC both=67 sameval=51
  (tables differ).
  M-tails 16/16 ALL NEW vs P321 (zero overlap vs
  P321M AND vs P321RM-tail8 AND vs P321RQ-tail8 --
  memo cites RM col-led tails, 0/16 confirmed).
  AM/CM/M/QR/RM/RQ 0-overlap vs P321 (prev lens
  16/10/16/4/16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=128793 (PB0 sig 77435801 sig-eq-P321PB0,
  47/84 diff, lenB 84),
  S1 n=128794 (fat PB1 sig 02000000 sig-eq-P321PB1,
  76/88 diff vs P321S1 n128446, 29/88 diff vs C10[0]
  n128811, lenB 88),
  A 128795-810 PBA88-PLAIN-M7b20 (sig 29000000 via AC
  b0-b3, b0 const 29, AM 16/16 distinct 14ch, mtab
  b20,21,22,80-83, raw lencode b5 const ee),
  C 128811-820 C10-1SIG-88-M3 (02000000 x10
  SAME-as-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 6ch b84-86, b87 const 9f, b5 const ee
  raw lencode),
  Q 128821-884 QUAD88-1SIG-4R (QM8 b28-31,80-83 M
  16/16 16ch + R11 b20-26,84-87 rows above
  (4/4 NO pairing, r01 share-7B-prefix) + tails above,
  NO frags, raw lencode b5 const ee b4 6b..e9),
  R 128885-129140 T88-RING-STANDARD (sig 5e020000,
  TM8 b19,27,34,35,80-83 by COL RM 16/16, TR8
  b28-31,76-79 by ROW RQ 16/16 UNPAIRED, b0 const
  5e b1 const 02, b84-87 const 2b3b1c36 ring-wide,
  b4=(0xeb+2off)&FF, b5=0xee+(off>=11)+(off>=139)).
  C blocks carry T86495/86500/86505/86520/86535/
  86556 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 14ch,
  C 6ch, Q 16/22ch, R 16/16ch),
  A/C/Q raw lencode (no counter literals) +
  R counter b4=(0xeb+2off)&FF + (off>=11)+(off>=139)
  (C literals 235/238 verified == 0xeb/0xee),
  temps _t6601-6616 (base max _t6600, no reuse) +
  _i3996/3998/4001/4004 (base max _i3994,
  no reuse) + _b3995/3997/3999/4000/4002/4003
  (base max _b3993, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P321R close
  (C 230222-24, block 230225; py CLOSED 86493, guard
  86495), at dispatch tail (N-out-of-scope fallthrough
  follows: C 230411, py 86575; early same-text guards at
  C 155060 / py 53352 are the T4-plateau-B n<=1077 check,
  unrelated scope).
  Matches A-832 geometry (PB0 sig-eq-P321PB0 47/84;
  PB1 sig-eq-P321PB1 76/88 SAME-as-C10 29/88;
  PBA88-PLAIN-M7b20 VPOS 8 sig-29 b5 const ee M7
  16/16 distinct; C10-M3 VPOS 4 SAME-as-PB1-sig
  b5 const b87-9f M3 10/10 diverge; QUAD88-1SIG-4R
  VPOS 20 + R11 4/4 UNPAIRED + r01-share-7B +
  r01-TRUE-3B + r2/r3-lcs0 + QM8 + NO frags + b5-const +
  M-tails NEW; T88-RING-STANDARD VPOS 18 + TM8/TR8 +
  tails-split + b84-87 2b3b1c36 + counter eb/ee/11/139;
  lencode 348/348 whole-tier, NO quad edge, ring edges
  128895->128896 + 129023->129024, NO D dips) incl exact
  values (PBA/C10/QUAD/T88 sigs, R11 rows + tails + LCS,
  STANDARD split + consts stand; sheet-vs-tables
  const-count note is S-F arithmetic in tables only per
  memo, geometry unaffected; M==RQ full-equality
  unmentioned by memo, batteries confirm, tier stands).
- Edges via counter formula first-hand: A head 37/ee
  tail 55/ee b5set {ee} NO step, 0 ff;
  C head 57/ee tail 69/ee b5set {ee} NO step, 0 ff;
  Q head 6b/ee tail e9/ee b4 base 0x6b step2 64/64
  range 6b..e9 b5set {ee} NO step, 0 ff NO edge;
  ring 128895 (off10, ff/ee) -> 128896 (off11, 01/ef);
  129023 (off138, ff/ef) -> 129024 (off139, 01/f0);
  exactly 2 ff in 256; R head eb/ee tail
  e9/f0 (Q tail e9/ee vs R tail e9/f0 differ in b5 --
  labeled apart); formulas re-derived from T10P322R
  code text (eb/ee/11/139) + T10P322A/C/Q text
  (raw lencode, b5 const ee); all edge pins + tail
  129140 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (33/ee, 35/ee) match raw lencode.
  Odd-lencode 348/348. No DISSENT on cut bytes
  (edges322.py EDGES-GREEN 31 PASS 0 FAIL, first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 370).
- Wall on band diff added lines (scope aaaaa11f..
  b6af2b17, 903 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 666->668 +2 /
  ranges 718->722 +4 = +6, C identical deltas 671->673
  +2 / 740->744 +4 (py=C dispatch-exact deltas; no
  elif added either side: py file-wide elif 46->46
  pre-existing elsewhere, C 0->0; deltas agree every
  side), CLOSED T10P prints 1820->1826 +6 both sides,
  seal 1914->1920 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-832-q914-P322
  verdict CONFIRM 62/62 CLEAN (own bed r3-P322
  128793..129172 BAD=0 + own r3-P321, verifier v218.py
  62/62 PASS; file present, counts verified;
  exact-value corroboration incl PB0 sig-eq-P321PB0
  47/84, PB1 sig-eq-P321PB1 76/88 SAME-as-C10 29/88,
  PBA88-PLAIN-M7b20 sig-29 M7, C10-M3 SAME-as-PB1-sig
  b87-9f, QUAD88-1SIG-4R SAME-sig-as-PBA + R11 rows +
  r01-share-7B + r01-TRUE-3B + r2/r3-lcs0 + QM8 + NO
  frags + b5-const + M-tails NEW, T88-RING-STANDARD +
  TM8/TR8 + tails-split + b84-87 2b3b1c36 + edges +
  consts; plus sheet-vs-tables const-count note: Q-914
  sheet 80/84/68/70 memo-exact, committed tables
  79/83/67/70 still deduct const-b5 on PBA/C10/quad --
  S-F arithmetic in tables only, geometry exact, PORT
  verdict stands).
  Agrees with cport commit msg (PYID 9563, RGRAM 19126).
- FWD-check first-hand: A-832 "Next P323" forward note
  verified against P323 lane code (608c167f, no checkout):
  PB0 b7ce7001 NEW-sig @129141 + PB1 02000000
  sig-eq-P322PB1 50/88 vs n128794 @129142 + PBA88
  2d000000 x16 @129143-58 + C10 02000000 x10 @129159-68
  -- all exact, new-sig era continues (P322 PB0
  77435801 was sig-eq-P321; P323 PB0 breaks new).
- Quiz: no conflicting CLAIM/GATE/FLAG on b430 (adjacent
  odds b429/b431 GATED PASS by odd seat, base-use and
  adjacency acknowledged -- b429 GATE notes b430 as
  sweep2 turf, b431 GATE uses b430 tip as base + P322
  tables as novelty baseline; both adjacency notes,
  no verdict on b430).
  Activity polled (no b430 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r70/ (build430.log,
  build430.sha, pyid430.log, rgram430py/c.log, cmp430.py/
  .c/.pyo/.co, for430.nums/for429base.nums, for430.added,
  for430added.list, pass430.names/pins430.names, pins430N.nums/
  pins429N.nums, pins430added.list, pins430.c14/
  pins429.c14, smoke430.log, units430.log, tables430.log,
  tabaudit322.py, edges322.py, edges430.log,
  numstat430.txt, addnorm430.txt, delnorm430.txt, alladded430.txt,
  banddiff via git, pydiff322.txt, cdiff430.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
