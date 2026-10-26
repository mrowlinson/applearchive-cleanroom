# GATE 825bee89 b440 T10P332 pins 132273..132620 (1980 tiers) PASS-functional

Seat sweep2-r73, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r73/w440 @825bee89.
Band = bb7f912a (py merge w2b@9c14a0a4 partial, +6 tiers, +64 pins)
+ 825bee89 (C port). Base a69ef1d1 (b439 tip, 1974 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build440/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc aee644f6 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r73
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9877/9877 covered=9877/9877 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 19754/19754 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 19754/19754 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 19754/19754).
- PINS-RGRAM cells set-eq 19754/19754 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9877/9877 xor 0;
  PINS 19756 rows (2 hdr + 19754 = PASS lines, +64 vs base
  19692). For-list union 9845->9877 +32 (132273 132274
  132275 132276 132282 132283 132289 132290 132291 132292
  132295 132296 132299 132300 132301 132317 132332 132333
  132348 132349 132351 132352 132353 132364 132365 132479
  132480 132524 132525 132607 132608 132620),
  0 removed, range 132273..132620 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 32x2 = 64 = 19754-19690.
  The 32 = S0/S1 (2) + A head/mid/tail pairs (6:
  head pair 132275/132276 off0/1, pair 132282/132283
  off7/8, tail pair 132289/132290 off14/15) +
  C head/mid/tail pairs (6: 132291/132292, 132295/132296,
  132299/132300) + Q head/off16/row-boundary-pairs/
  B5EDGE-pair/off52/tail (10: head 132301 off0, 132317
  off16, pairs 132332/132333 off31/32 + 132348/132349
  off47/48, B5EDGE pair 132351/132352 pinned off50/51,
  132353 off52, tail 132364 off63) +
  R head/edge-pair/sigbnd-pair/edge-pair/tail (8: head
  132365 off0, edge pair 132479/132480 off114/115,
  sig-boundary pair 132524/132525 off159/160, edge pair
  132607/132608 off242/243, tail 132620 off255).
  R carries 8 for-pins (extra sig-boundary pair for the
  ROWBND novelty) -- the +32nd pin vs the usual 31.
  PINS-new-N == for-added 32/32 (4th set-eq way),
  PINS removed 0. PINS numstat 64/0 clean append (all in
  py-merge leg a69ef1d1..bb7f912a; C-port leg touched zero
  PINS rows); all 19754 rows test_rgram_fast.py-tagged;
  cols1-4 purity +64/-0, cols5-7 unchanged first-hand
  (test_rgram_fast.py/27.0.1/ct-lzraven uniform both).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P332 C-vs-py, script-compared, TABAUDIT-GREEN
  120 PASS 0 FAIL (tabaudit332.py rc=0, first run):
  S0 168ch sig 6db29604 NEW (differs vs P331 heads
  6db29605/09000000; 35/84 payload diff vs P331S0
  first-hand, NOT byte-equal) / S1 176ch sig 0b000000
  NEW (differs vs P331 heads; 44/88 payload diff vs
  P331S1 n131926 first-hand, NOT byte-equal; 60/88 diff
  vs own-C10[0] assembled n132291, NOT byte-equal;
  sig DIFFERS-from-own-C10 0b-vs-0d; differs vs own
  PB0), staged as full-payload singletons,
  AM 16/16 18ch distinct, CM 10/10 8ch distinct,
  M 16/16 14ch distinct, QR 4/4 2ch distinct, RM 16/16
  12ch distinct, RQ 16/16 14ch distinct, no QT (quad
  tails = R1 b84 + consts) + no RT (ROWBND tails) +
  no F (no frag this tier),
  M-vs-RQ 0/16 identical INTRA-tier (lanes differ: QM7
  b13-15,80-83 vs TR7 b0,10,11,76-79; 0 overlap; the
  cross-band string-eq running pattern (b414-b438 all
  eq variants) is N/A this tier -- first 0/16,
  batteries confirm, tier stands),
  AC 77, CC 82, QC 78, RC 73; C _N decls
  77/82/78/73 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M9b6 sig b3000000 (b0 const b3, b5 const
  09 via raw lencode NOT in AC; AM 16/16 distinct NO pair; M9
  b6-10,80-83) + vs P331PBA b1000000 (novelty =
  new sig b3 + AM 0-overlap).
  C10-1SIG-88-DIFFSIG sig 0d000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 8ch; CC has no b5, b5 const 09 full block
  via lencode).
  QUAD88-1SIG-4R-NOFRAG-B5EDGE-C87 1-sig d2000000 x64
  DIFFERS-from-PBA-sig (QC b0 const d2; b5 edge 09->0a
  @off50/51, edge 132351 ff/09 -> 132352 01/0a r3c2/c3,
  exactly 1 ff in 64; b4 base 0x9b step2 64/64 range
  9b..ff,01..19; QM7 b13-15,80-83 16/16 shared x3 vs
  row0 (M indexed by col off&15 first-hand) NO frags +
  R1 b84 rows 59/79/99/b9 4/4 NO pairing BY-ROW const
  (QR indexed by row off>>4 first-hand);
  tails b84-87 4/4 distinct 5933fde9/7933fde9/
  9933fde9/b933fde9, r0123 TRUE-3B 33fde9 ALL pairs,
  suffix-LCS 3/3/3/3/3/3 recorded first-hand;
  b87 CONST e9 quad-wide (QC const; R1 rows carry b84
  only so all 64 cells).
  Ring 2SIG-ROWBND: sig d20d0000 x160 (off0-159) +
  d30d0000 x96 (off160-255); boundary off159/160 =
  N132524->132525 ROW-9/10 boundary; code-TM6 b18,19,
  80-83 by COL RM 16/16 + code-TR7 b0,10,11,
  76-79 by ROW RQ 16/16 UNPAIRED;
  b0 row-led (d2 rows0-9, d3 rows10-15, RQ first bytes
  d2 x10 + d3 x6 first-hand); b1 const 0d ring-wide;
  b84-87 3bfd54d5 ring-wide NEW.
  VPOS partitions re-derived from code: PBA 10
  (b4+M9) / C10 5 (b4+M4) / quad 10
  (b4,b5+QM7+R1) / T 15
  (b0,b4,b5+TM6+TR7)
  -- all match A-882.
  Code-consts vs A-882 INCL (PBA 78 / C10 83 /
  quad 78 / T88 73): impl 77/82/78/73 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-1044 sheet counts b5 (memo A-882 confirms the
  sheet INCL values) -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  memo-exact on quad (b5 edge-varies, in VPOS)
  and T88 (b5 counter-varies, no deduction);
  geometry exact, PORT verdict stands; FLAGGED for
  memo (15th even band running: b412/b414/b416/b418/
  b420/b422/b424/b426/b428/b430/b432/b434/b436/b438/
  b440; PBA/C10 lag this tier).
  QUAD 1SIG d2 DIFFERS-from-PBA-sig b3 this tier;
  PBA sig b3 NEW vs P331 b1; AC-QC both=73 sameval=8
  (tables differ).
  M-tails 16/16 ALL NEW vs P331 (zero overlap vs
  P331T RM col-led tails).
  AM/CM/M/QR/RM/RQ 0-overlap vs P331 (widths P332 vs
  P331: AM 9B vs 8B, CM 4B vs 5B, M 7B vs 10B, QR 1B
  vs 3B, RM 6B vs 7B, RQ 7B vs 9B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=132273 (PB0 sig 6db29604 NEW, 35/84 diff,
  lenB 84),
  S1 n=132274 (fat PB1 sig 0b000000 NEW,
  44/88 diff vs P331S1 n131926, 60/88 diff vs C10[0]
  n132291, DIFFERS-from-own-C10, lenB 88),
  A 132275-290 PBA88-PLAIN-M9b6 (sig b3000000 via AC
  b0-b3, b0 const b3, AM 16/16 distinct 18ch, mtab
  b6-10,80-83, raw lencode b5 const 09),
  C 132291-300 C10-1SIG-88-DIFFSIG (0d000000 x10
  DIFFERS-from-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87, b5 const 09 raw lencode),
  Q 132301-364 QUAD88-1SIG-4R-NOFRAG-B5EDGE-C87 (QM7
  b13-15,80-83 M 16/16 14ch shared-x3-by-col + R1 b84
  rows above (4/4 NO pairing, BY-ROW const)
  + tails above, NO frags, raw lencode b5=09+(off>=51)
  edge 132351->132352 r3c2/c3),
  R 132365-620 T88-RING-2SIG-ROWBND (sig
  d20d0000 off0-159 + d30d0000 off160-255,
  code-TM6 b18,19,80-83 by COL RM 16/16,
  code-TR7 b0,10,11,76-79 by ROW RQ 16/16 UNPAIRED,
  b0 row-led d2-rows0-9/d3-rows10-15, b1 const 0d,
  b84-87 const 3bfd54d5 ring-wide,
  b4=(0x1b+2off)&FF, b5=0x0a+(off>=115)+(off>=243)).
  C blocks carry T88874/88879/88884/88900/88915/
  88934 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 18ch,
  C 8ch, Q 14/2ch, R 12/14ch),
  A/C/Q raw lencode (no counter literals) +
  R counter b4=(0x1b+2off)&FF + (off>=115)+(off>=243)
  (C literals 27/10 verified == 0x1b/0x0a),
  temps _t6765-6780 (base max _t6764, no reuse) +
  _i4097/4099/4102/4105 (base max _i4095,
  no reuse) + _b4096/4098/4100/4101/4103/4104
  (base max _b4094, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P331R close
  (C 236415-17, comment 236418, block 236419; py CLOSED
  88872, guard 88874), at dispatch tail
  (N-out-of-scope fallthrough follows: C 236593,
  py 88953; early same-text guards at C 159334 /
  py 54905 are the T4-plateau-B n<=1077 check,
  unrelated scope).
  Matches A-882 geometry (PB0 NEW-sig 35/84;
  PB1 NEW-sig 44/88 DIFFERS-from-C10 60/88;
  PBA88-PLAIN-M9b6 VPOS 10 sig-b3 b5 const 09 M9
  16/16 distinct; C10-1SIG-88-DIFFSIG VPOS 5
  DIFFERS-from-PB1-sig b5 const M4 10/10
  diverge; QUAD88-1SIG-4R-NOFRAG-B5EDGE-C87 VPOS 10 +
  R1 4/4 UNPAIRED 59/79/99/b9 + TRUE-3B-33fde9 +
  suffix-LCS-3x6 + b87-CONST-e9 + QM7-shared-x3 +
  NO frags + b5-edge-off51 + M-tails NEW;
  T88-RING-2SIG-ROWBND VPOS 15 + TM6-by-COL/
  TR7-by-ROW + b0-row-led-d2/d3 + b1-0d + b84-87
  3bfd54d5 + counter 1b/0a/115/243; lencode
  348/348 whole-tier, Q b5 edge 132351->132352,
  ring edges 132479->132480 + 132607->132608,
  sig boundary 132524->132525 ROW-9/10, NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R1 rows +
  tails + LCS, ROWBND split + consts stand;
  sheet-vs-tables const-count note is S-F arithmetic
  in tables only per memo, geometry unaffected; M-vs-RQ
  0/16 unmentioned by memo, batteries confirm, tier
  stands).
- Edges via counter formula first-hand: A head 67/09
  tail 85/09 b5set {09} NO step, 0 ff;
  C head 87/09 tail 99/09 b5set {09} NO step, 0 ff;
  Q head 9b/09 edge 132351 (off50, ff/09) ->
  132352 (off51, 01/0a) r3c2/c3 tail 19/0a, exactly
  1 ff in 64 (b5 edge 09->0a @off51; b4 base 0x9b
  step2 64/64 range 9b..ff,01..19);
  ring 132479 (off114, ff/0a) -> 132480 (off115, 01/0b);
  132607 (off242, ff/0b) -> 132608 (off243, 01/0c);
  exactly 2 ff in 256; R head 1b/0a tail
  19/0c sigbnd 59/0b->5b/0b (Q tail 19/0a vs R tail
  19/0c differ in b5 -- labeled apart); formulas
  re-derived from T10P332R code text (1b/0a/115/243)
  + T10P332A/C/Q text (raw lencode, b5 const 09 /
  edge); all edge pins + sigbnd pair 132524/132525 +
  tail 132620 in for-list + 2 PASS lines each py+C.
  S0/S1 embedded b4/b5 (63/09, 65/09) match raw
  lencode. Ring counter==raw-lencode 256/256.
  Odd-lencode 348/348. No DISSENT on cut bytes
  (edges332.py EDGES-GREEN 71 PASS 0 FAIL, first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  64/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 424).
- Wall on band diff added lines (scope a69ef1d1..
  825bee89, 905 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 686->688 +2 /
  ranges 758->762 +4 = +6, C identical deltas AND
  identical sets (py-only 0, C-only 0; no C-only offset
  this window; no elif added either side: py file-wide
  elif 50->50 pre-existing elsewhere, C else-if 0->0;
  deltas agree every side), CLOSED T10P prints
  1880->1886 +6 both sides, seal 1974->1980 +6
  (commit msgs; offset +94 vs CLOSED-T10P stable): all
  agree, no slip (absolute seal inherits lane tally;
  delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-882-q1044-P332
  verdict CONFIRM 64/64 CLEAN (own bed r3-P332
  132273..132652 BAD=0 + own r3-P331, verifier v268.py
  64/64 PASS; file present, counts verified; geometry
  GATED PORT, novelties FIRST-R1-quad + 2SIG-ROWBND
  T-ring gated; exact-value corroboration incl PB0
  NEW-sig 35/84, PB1 NEW-sig 44/88
  DIFFERS-from-own-C10 60/88, PBA88-PLAIN-M9b6 sig-b3
  M9, C10-1SIG-88-DIFFSIG DIFFERS-from-PB1-sig,
  QUAD88-1SIG-4R-NOFRAG-B5EDGE-C87 1-sig-d2 + R1 rows
  59/79/99/b9 + TRUE-3B-33fde9 + b87-CONST-e9 + QM7 +
  NO frags + b5-edge-off51 + M-tails NEW,
  T88-RING-2SIG-ROWBND + TM6-by-COL/TR7-by-ROW +
  b0-row-led + b1-0d + b84-87 3bfd54d5 + counter +
  edges; plus sheet-vs-tables const-count note: Q-1044
  sheet 78/83/78/73 memo-exact, committed tables
  77/82/78/73 still deduct const-b5 on PBA/C10 -- S-F
  arithmetic in tables only, geometry exact, PORT
  verdict stands) + A-1044-q1044-P332 verdict CONFIRM
  48/48 CLEAN (own bed r6-P332 132273..132648 +
  r6-P331, BAD=0 + direct-oracle 2/2 byte-match,
  verifier v600f3.py 48/48 PASS; file present, counts
  verified; tier GATED PORT; suffix-lcs 3/3/3/3/3/3 +
  M-tails NEW + b0-row-led-d2/d3 + consts excl
  77/82/78/73 script-claimed corroborated).
  Agrees with cport commit msg (PYID 9877, RGRAM 19754).
- FWD-check first-hand: A-882 "Next P333" forward note
  verified against P333 lane code (bb0cac91, no checkout):
  PB0 6db29606 NEW-sig 32/84 @132621 + PB1
  0d000000 NEW-sig 64/88 vs n132274 @132622 +
  PBA88 de000000 x16 @132623-638 + C10
  0d000000 x10 SAME-as-PB1-sig @132639-648
  -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b440 (adjacent
  odds b439/b441 = sweep turf, base-use only, no verdict
  on b440).
  Activity polled (no b440 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r73/ (build440.log,
  build440.sha, pyid440.log, rgram440py/c.log, cmp440.py/
  .c/.pyo/.co, for440.nums/for439base.nums, for440.added,
  pass440.names/pins440.names, pins440N.nums/
  pins439N.nums, pins440added.nums, smoke440.log,
  units440.log, tables440.log, tabaudit332.py, edges332.py,
  edges440.log, numstat440.txt, addnorm440.txt,
  delnorm440.txt, alladded440.txt, fwd333.txt, p333.py,
  banddiff via git, pydiff via git, cdiff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
