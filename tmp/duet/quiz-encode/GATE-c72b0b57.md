# GATE c72b0b57 b428 T10P320 pins 128097..128444 (1908 tiers) PASS-functional

Seat sweep2-r70, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r70/w428 @c72b0b57.
Band = aab116ae (py merge w2b@aa3789ae partial, +6 tiers, +62 pins)
+ c72b0b57 (C port). Base 49f9f3e4 (b427 tip, 1902 tiers sealed,
GATE-filed PASS-functional by odd seat).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both);
w428 +__pycache__ battery byproduct after runs, w427base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build428/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc c0fdc195 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r70
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9501/9501 covered=9501/9501 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 19002/19002 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 19002/19002 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 19002/19002).
- PINS-RGRAM cells set-eq 19002/19002 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9501/9501 xor 0;
  PINS 19004 rows (2 hdr + 19002 = PASS lines, +62 vs base
  18942). For-list union 9470->9501 +31 (128097 128098
  128099 128100 128106 128107 128113 128114 128115 128116
  128119 128120 128123 128124 128125 128127 128128 128141
  128156 128157 128173 128180 128187 128188 128189 128255
  128256 128300 128383 128384 128444),
  0 removed, range 128097..128444 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 19002-18940.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid/tail pairs (6) + Q head/edge-pair/5-mids/
  tail-pair (10: head 128125, b5-step EARLY edge pair
  128127/128128 pinned, mids 128141/128156/128157/128173/
  128180, tail pair 128187/128188) +
  R head/edge-pairs/mid/tail (7: head 128189, edge pairs
  128255/128256 + 128383/128384, mid 128300, tail 128444).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0.
  PINS-FORMAT-NOTE (first-hand, no gate impact): the py merge
  leg did a full-file RECORD regeneration (numstat
  10730/10668, all in 49f9f3e4..aab116ae; C-port leg
  aab116ae..c72b0b57 touched zero PINS rows): generator col5
  normalized test_rgram.sh -> test_rgram_fast.py on all
  18940 old rows (mixed tags since earlier bands: 10668 .sh
  + 8210 fast at b426 tip f278bdf0). Pin-value purity
  cols1-4 verified first-hand +62/-0 (0 removed-or-changed);
  cols6-7 unchanged (27.0.1,ct-lzraven both sides). Both
  battery legs ran GREEN against these exact pins.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P320 C-vs-py, script-compared, TABAUDIT-GREEN
  427 PASS 0 FAIL (tabaudit320.py rc=0; first run 70/71,
  1 FAIL = seat's own VPOS-Q arithmetic double-counting b0,
  fixed to b0-inside-R29, re-ran GREEN; per-row + per-const
  depth added after):
  S0 168ch sig 36ac2c01 sig-eq-P319PB0 (30/84 payload
  diff vs P319S0 first-hand) / S1 176ch sig 02000000
  sig-eq-P319PB1 (76/88 payload diff vs P319S1, NOT
  byte-equal; 28/88 diff vs own-C10[0] assembled,
  NOT byte-equal; sig SAME-as-own-C10; differs vs own PB0),
  staged as full-payload singletons,
  AM 16/16 18ch distinct, CM 10/10 8ch distinct, M 16/16
  16ch distinct, QR 4/4 58ch distinct, RM 16/16 16ch
  distinct, RQ 16/16 16ch distinct UNPAIRED, no QT
  (quad tails live in R29) + no RT (STANDARD tails) +
  no F (no frag this tier),
  M==RQ 16/16 FULL string-identical INTRA-tier, byte
  positions PARTIALLY differ (QM8 b40-43,80-83 vs TR8
  b40-43,76-79: b40-43 shared positions, tails SPLIT
  b80-83 col / b76-79 row; running pattern: b414 full-eq,
  b416 tail-eq, b418 full-eq, b420/b422
  string-eq-positions-differ, b424 tail-eq-positions-differ,
  b426 full-eq, b428 string-eq-tails-split),
  AC 77, CC 82, QC 49, RC 70; C _N decls 77/82/49/70
  match actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M9 sig 36000000 (b0 const 36, b5 const
  e8 via raw lencode; AM 16/16 distinct NO pair; M9
  b29,30,31,34,35,80-83) + vs P319PBA 25000000 (novelty =
  new sig 36 + AM 0-overlap).
  C10-1SIG-88-TAIL sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 8ch:
  fb512d1b/1b522d1b/3b522d1b/5b522d1b/7b522d1b/
  1a852d1b/3a852d1b/834b651d/a34b651d/c34b651d;
  CC has no b5, b5 const e8 full block via lencode).
  QUAD88-2SIG-PAIRED-4R rows0-1 3d000000 x32 + rows2-3
  11000000 x32 (QC has no b0, b0 in tab; row sigs
  assembled b0(row)+000000; b5 STEP e8->e9 @off3 EARLY,
  edge 128127 ff/e8 -> 128128 01/e9, exactly 1 ff in 64;
  b4 base 0xfb; QM8 b40-43,80-83 16/16 distinct NO
  frags + R29 b0,8-15,19,25-39,84-87 rows 4/4 NO
  pairing pairwise-disjoint (sig-paired r01/r23, full
  tuples all distinct),
  tails b84-87 4/4 distinct 32e7ff26/18cbe58f/
  75305c25/4062d425, r2r3 pair-only 1B 0x25 @pos3,
  b87 NOT const quad-wide {25,8f,26},
  r0/r1-lcs0 vs all pairs, r2r3-lcs1, all other pairs lcs0).
  Ring STANDARD: sig bd020000 x256; TM8 b30,39,46,47,
  80-83 by COL RM 16/16 + TR8 b40-43,76-79 by ROW RQ
  16/16 UNPAIRED (tails SPLIT b80-83 col / b76-79 row);
  b0 const bd b1 const 02; b84-87 16cb2a30 ring-wide
  NEW (P319 SWAPPED-split era per Q-912: P319T b80-83
  ROW-led via RQ).
  VPOS partitions re-derived from code: PBA 10
  (b4+M9) / C10 5 (b4+M4 b84-87) / quad 39
  (b4,b5+QM8+R29, b0 inside R29 no double-count) /
  T 18 (b4,b5+TM8+TR8) -- all match A-830.
  Code-consts vs A-830 (PBA 78 / C10 83 /
  quad 49 / T88 70): impl 77/82/49/70 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-912 sheet counts b5 (memo A-830 confirms the
  sheet) -- S-F arithmetic persists in committed
  tables though the sheet is FIXED; memo-exact on
  quad (b5 STEP-varies, in tab) and T88 (b5 varies,
  no deduction); geometry exact, PORT verdict stands;
  FLAGGED for memo (9th band running: b412/b414/b416/
  b418/b420/b422/b424/b426/b428; PBA/C10 lag this tier).
  QUAD 2SIG 3d/11 vs P319; PBA sig
  36 NEW vs P319 25; AC-QC both=49 sameval=41
  (tables differ).
  M-tails 16/16 ALL NEW vs P319 (zero overlap vs
  P319M AND vs P319RM-tail8 AND vs P319RQ-tail8).
  AM/CM/M/QR/RM/RQ 0-overlap vs P319 (prev lens
  16/10/16/4/16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=128097 (PB0 sig 36ac2c01 sig-eq-P319PB0,
  30/84 diff, lenB 84),
  S1 n=128098 (fat PB1 sig 02000000 sig-eq-P319PB1,
  76/88 diff vs P319S1 n127750, 28/88 diff vs C10[0]
  n128115, lenB 88),
  A 128099-114 PBA88-PLAIN-M9 (sig 36000000 via AC
  b0-b3, b0 const 36, AM 16/16 distinct 18ch, mtab
  b29,30,31,34,35,80-83, raw lencode b5 const e8),
  C 128115-124 C10-1SIG-88-TAIL (02000000 x10
  SAME-as-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87, b5 const e8
  raw lencode),
  Q 128125-188 QUAD88-2SIG-PAIRED-4R (QM8 b40-43,80-83 M
  16/16 16ch + R29 b0,8-15,19,25-39,84-87 rows above
  (4/4 NO pairing, sig-paired r01/r23) + tails above,
  NO frags, counter b4=(0xfb+2off)&FF
  b5=0xe8+(off>=3) EARLY),
  R 128189-444 T88-RING-STANDARD (sig bd020000,
  TM8 b30,39,46,47,80-83 by COL RM 16/16, TR8
  b40-43,76-79 by ROW RQ 16/16 UNPAIRED, b0 const
  bd b1 const 02, b84-87 const 16cb2a30 ring-wide,
  b4=(0x7b+2off)&FF, b5=0xe9+(off>=67)+(off>=195)).
  C blocks carry T86027/86032/86037/86053/86068/
  86092 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 18ch,
  C 8ch, Q 16/58ch, R 16/16ch),
  Q counter b4=(0xfb+2off)&FF + (off>=3)
  (C literals 251/232 verified == 0xfb/0xe8) +
  R counter b4=(0x7b+2off)&FF + (off>=67)+(off>=195)
  (C literals 123/233 verified == 0x7b/0xe9),
  temps _t6569-6584 (base max _t6568, no reuse) +
  _i3976/3978/3981/3984 (base max _i3974,
  no reuse) + _b3975/3977/3979/3980/3982/3983
  (base max _b3973, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P319R close
  (C 228987-89, block 228990; py CLOSED 86025, guard
  86027), at dispatch tail (N-out-of-scope fallthrough
  follows: C 229196, py 86111; early same-text guards at
  C 154214 / py 53047 are the T4-plateau-B n<=1077 check,
  unrelated scope).
  Matches A-830 geometry (PB0 sig-eq-P319PB0 30/84;
  PB1 sig-eq-P319PB1 76/88 SAME-as-C10 28/88;
  PBA88-PLAIN-M9 VPOS 10 sig-36 b5 const e8 M9
  16/16 distinct; C10-TAIL VPOS 5 SAME-as-PB1-sig
  b5 const M4 10/10 diverge; QUAD88-2SIG-PAIRED-4R
  VPOS 39 + R29 4/4 UNPAIRED + sig-paired-r01/r23 +
  r2r3-paironly-25 + b87-{25,8f,26} + r0/r1-lcs0 +
  QM8 + NO frags + b5-step-EARLY-off3 + M-tails NEW;
  T88-RING-STANDARD VPOS 18 + TM8/TR8 + tails-split +
  b84-87 16cb2a30 + counter 7b/e9/67/195; lencode
  348/348 whole-tier, Q step edge 128127->128128,
  ring edges 128255->128256 + 128383->128384, NO D
  dips) incl exact values (PBA/C10/QUAD/T88 sigs,
  R29 rows + tails + LCS, STANDARD split + consts
  stand; sheet-vs-tables const-count note is S-F
  arithmetic in tables only per memo, geometry
  unaffected; M==RQ full-equality unmentioned by
  memo, batteries confirm, tier stands).
- Edges via counter formula first-hand: A head c7/e8
  tail e5/e8 b5set {e8} NO step, 0 ff;
  C head e7/e8 tail f9/e8 b5set {e8} NO step, 0 ff;
  Q head fb/e8 edge 128127 (off2, ff/e8) ->
  128128 (off3, 01/e9) tail 79/e9, exactly 1 ff in 64
  (b5 STEP e8->e9 @off3 EARLY);
  ring 128255 (off66, ff/e9) -> 128256 (off67, 01/ea);
  128383 (off194, ff/ea) -> 128384 (off195, 01/eb);
  exactly 2 ff in 256; R head 7b/e9 tail
  79/eb (Q tail 79/e9 vs R tail 79/eb differ in b5 --
  labeled apart); formulas re-derived from T10P320Q
  code text (fb/e8/3) + T10P320R text
  (7b/e9/67/195) + T10P320A/C text
  (raw lencode, b5 const e8); all edge pins + tail
  128444 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (c3/e8, c5/e8) match raw lencode.
  Odd-lencode 348/348. No DISSENT on cut bytes
  (edges320.py EDGES-GREEN 33 PASS 0 FAIL, first run
  after 1 seat paren-typo fix, re-ran GREEN).
- C diff purely additive: numstat 607 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  PINS full-file RECORD regen (cols1-4 purity +62/-0,
  see PINS-FORMAT-NOTE); raw C grep 602 content + 5
  bare-blank `+` lines (verified bare, no whitespace)
  / 0 del; fine-norm (rgramc.c scope, _tN/_iN/_bN
  temp-norm, BSD tools, empty-excluding) del-subset-add
  0 missing (del-uniq 0, add-uniq 399).
- Wall on band diff added lines (scope 49f9f3e4..
  c72b0b57, 11570 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 607/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS regen (values +62/-0).
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 662->664 +2 /
  ranges 710->714 +4 = +6, C identical deltas 667->669
  +2 / 732->736 +4 (py=C dispatch-exact deltas; no
  elif added either side: py file-wide elif 46->46
  pre-existing elsewhere, C 0->0; deltas agree every
  side), CLOSED T10P prints 1808->1814 +6 both sides,
  seal 1902->1908 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-830-q912-P320
  verdict CONFIRM 63/63 CLEAN (own bed r3-P320
  128097..128476 BAD=0 + own r3-P319, verifier v216.py
  63/63 PASS; writer CORRECTION PBA M8->M9 verified:
  9-pos list b29-31,34,35,80-83, VPOS 10 exact; file
  present, counts verified; exact-value corroboration
  incl PB0 sig-eq-P319PB0 30/84, PB1 sig-eq-P319PB1
  76/88 SAME-as-C10 28/88, PBA88-PLAIN-M9 sig-36 M9,
  C10-TAIL SAME-as-PB1-sig M4, QUAD88-2SIG-PAIRED-4R
  rows0-1-3d/rows2-3-11 + R29 rows + r2r3-paironly-25 +
  b87-{25,8f,26} + r0/r1-lcs0 + QM8 + NO frags +
  b5-step-EARLY + M-tails NEW, T88-RING-STANDARD + TM8/
  TR8 + tails-split + b84-87 16cb2a30 + edges + consts;
  plus sheet-vs-tables const-count note: Q-912 sheet
  78/83/49/70 memo-exact, committed tables 77/82/49/70
  still deduct const-b5 on PBA/C10 -- S-F arithmetic
  in tables only, geometry exact, PORT verdict stands).
  Agrees with cport commit msg (PYID 9501, RGRAM 19002).
- FWD-check first-hand: A-830 "Next P321" forward note
  verified against P321 lane code (aaaaa11f, no checkout):
  PB0 77435801 NEW-sig @128445 + PB1 02000000
  sig-eq-P320PB1 62/88 vs n128098 @128446 + PBA88
  3d000000 x16 @128447-62 (SAME-sig-as-P320Q-r01
  confirmed) + C10 02000000 x10 @128463-72
  -- all exact, new-sig era continues (P320 PB0
  36ac2c01 was sig-eq-P319; P321 PB0 breaks new).
- Quiz: no conflicting CLAIM/GATE/FLAG on b428 (adjacent
  odds b427/b429 GATED PASS by odd seat, base-use and
  adjacency acknowledged -- b427 GATE notes b428 as
  sweep2 turf, b429 GATE uses b428 tip as base + P320
  tables as novelty baseline; both adjacency notes,
  no verdict on b428).
  Activity polled (no b428 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r70/ (build428.log,
  build428.sha, pyid428.log, rgram428py/c.log, cmp428.py/
  .c/.pyo/.co, for428.nums/for427base.nums, for428.added,
  for428added.list, pass428.names/pins428.names, pins428N.nums/
  pins427N.nums, pins428added.nums/.list, pins428.c14/
  pins427.c14, smoke428.log, units428.log, tables428.log,
  tabaudit320.py, edges320.py, edges428.log,
  numstat428.txt, addnorm428.txt, delnorm428.txt, alladded428.txt,
  banddiff via git, pydiff320.txt, cdiff428.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
