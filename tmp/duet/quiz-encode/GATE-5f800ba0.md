# GATE 5f800ba0 b466 T10P358 pins 141321..141668 (2136 tiers) PASS-functional

Seat sweep2-r79, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r79/w466 @5f800ba0.
Band = ee21fae8 (py merge w2b@367df011 partial, +6 tiers, +58 pins)
+ 5f800ba0 (C port). Base be565d02 (b465 tip, 2130 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build466/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 3cf5d0bda1be3e393b7b29b4d30de22ffdc40acd1c72955d727cfd3720fdd5d1 / aae d6e27c97ced21673cc73eee061ffdbd7f0358a87e482056c222a867202110785
  (aae d6e27c97 = b288-b354 pinned value + r52-r79
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 10655/10655 covered=10655/10655 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 21310/21310 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 21310/21310 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 21310/21310).
- PINS-RGRAM cells set-eq 21310/21310 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 10655/10655 xor 0;
  PINS 21312 rows (2 hdr + 21310 = PASS lines, +58 vs base
  21254). For-list union 10626->10655 +29 (141321 141322
  141323 141324 141330 141331 141337 141338
  141339 141340 141343 141344 141347 141348 141349 141364
  141365 141380 141381 141396 141397 141412 141413 141439
  141440 141500 141567 141568 141668),
  0 removed, range 141321..141668 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 29x2 = 58 = 21310-21252.
  The 29 = S0/S1 (2) + A head-pair/pair/tail-pair (6:
  head pair 141323/141324 off0/1, pair 141330/141331
  off7/8, tail pair 141337/141338 off14/15; b5 const 50
  NO step NO edge) +
  C head/mid/tail pairs (6: 141339/141340 off0/1,
  mid pair 141343/141344 off4/5, tail pair
  141347/141348 off8/9; b5 const 50 NO step) +
  Q head/off15/off16/pair/pair/tail (8: head
  141349 off0, 141364 off15, 141365 off16,
  pair 141380/141381 off31/32,
  pair 141396/141397 off47/48, tail 141412 off63;
  NO edge -- b5 const 50 this tier) +
  R head/edge-pair/mid-pin/edge-pair/tail (7: head 141413
  off0, edge pair 141439/141440 off26/27,
  mid pin 141500 off87, edge pair 141567/141568
  off154/155, tail 141668 off255; no pre-edge pin
  in for-list -- witness pattern differs, first-hand).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg be565d02..ee21fae8; C-port leg touched zero
  PINS rows); all 21310 rows test_rgram_fast.py-tagged;
  added 58 names == for-added closed+open pairs (29x2),
  checks sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P358 C-vs-py, script-compared, TABAUDIT-GREEN
  125 PASS 0 FAIL (tabaudit358.py rc=0, fresh first-hand;
  coverage checks run pre-exit, not dead code):
  S0 168ch sig ada6240d NEW-sig (31/84 payload diff vs P357S0
  sig aefa600d first-hand, NOT byte-equal) /
  S1 176ch sig 18000000 NEW-sig (49/88 payload diff vs
  P357S1 sig 1a000000 first-hand, NOT byte-equal;
  44/88 diff vs own-C10[0] assembled n141339 first-hand,
  NOT byte-equal; sig DIFFERS-from-own-C10 18-vs-1d;
  DIFFERS from own PB0 ad-vs-18),
  staged as full-payload singletons,
  AM 16/16 14ch distinct, CM 10/10 8ch distinct,
  M 16/16 14ch distinct, QR 4/4 2ch distinct, RM 16/16
  16ch distinct, RQ 16/16 14ch distinct, no QT (quad
  tails = R1 + const b85/86/87) + no RT (SWAPPED tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; QM7 b52,53,54,80-83 by COL m=off&15 vs TR7 b52,53,
  54,80-83 by ROW r=off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated),
  AC 79, CC 82, QC 78, RC 71; C _N decls
  79/82/78/71 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b30 sig e0010000 (b0 const e0, b5 const
  50 via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M7 b30,39,47,80-83) + vs P357PBA b0 a6
  (novelty = new sig e0 + AM 0-overlap).
  C10-1SIG-88-TAIL-M4 sig 1d000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 8ch b84,85,86,87; CC has no b84-87 (all in CM lane);
  b5 const 50 full block via lencode).
  QUAD88-1SIG-QM7/R1-NOEDGE 1-sig e0010000 x64
  SAME-sig-as-PBA (QC b0 const e0; b5 const 50
  deducted to raw lencode NO edge; b4 base
  0x4b step2 64/64 range 4b..c9, NO wrap; QM7 b52,53,54,
  80-83 M 16/16 14ch distinct NO frags (m = off&15
  first-hand) + R1 b84 rows 41/61/81/a1
  4/4 UNPAIRED BY-ROW const (q = off>>4 first-hand);
  tails = R1 + const b85 3f / b86 2b / b87 a9 quad-wide,
  full-tail suffix-lcs 3/3/3/3/3/3 + R1 all-distinct).
  Ring T88-SWAPPED 1-sig 051e0000 x256
  (b0 const 05, b1 const 1e; code-TM8
  b6,7,8,9,76-79 by COL RM 16/16 + code-TR7 b52,53,
  54,80-83 by ROW RQ 16/16 UNPAIRED (SWAPPED tails b80-83
  row / b76-79 col); b84-87 const
  c13f2ba9 ring-wide NEW; b4=(0xcb+2off)&FF +
  (off>=27)+(off>=155) (C literals 203/80/27/155 verified
  == 0xcb/0x50/27/155)).
  VPOS partitions re-derived from code: PBA 8
  (b4 + M7 b30,39,47,80-83) / C10 5 (b4 + M4 b84-87) /
  quad 9 (b4 + QM7 7 + R1) / T 17
  (b4,b5 + TM8 8 + TR7 7)
  -- all match A-945.
  Code-consts vs A-945 excl (PBA 79 / C10 82 /
  quad 78 / T88 71): impl 79/82/78/71 =
  exact all four, NO writer lag: committed tables match
  the sheet excl values (INCL +3 on PBA/C10/quad b5-const =
  80/85/79/71); geometry exact, PORT verdict stands;
  FLAGGED for memo (28th even band running: b412/b414/
  b416/b418/b420/b422/b424/b426/b428/b430/b432/b434/
  b436/b438/b440/b442/b444/b446/b448/b450/b452/b454/
  b456/b458/b460/b462/b464/b466; no-lag this tier).
  QUAD 1SIG e0 SAME-sig-as-PBA-sig this tier;
  PBA sig e0 NEW vs P357 a6; AC-QC both=75 sameval=55
  (tables differ).
  M-tails 16/16 ALL NEW vs P357T col-led tails
  (zero overlap vs P357T tails first-hand).
  AM/CM/M/RM/RQ/QR 0-overlap vs P357 (widths P358 vs
  P357: AM 7B vs 8B, CM 4B vs 2B, M 7B vs 9B, RM 8B vs 8B,
  RQ 7B vs 8B, QR 1B vs 2B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=141321 (PB0 sig ada6240d NEW-sig,
  31/84 diff, lenB 84),
  S1 n=141322 (fat PB1 sig 18000000 NEW-sig,
  49/88 diff vs P357S1, 44/88 diff vs C10[0]
  n141339, DIFFERS-sig-vs-own-C10, lenB 88),
  A 141323-338 PBA88-PLAIN-M7b30 (sig e0010000 via AC
  b0-b3, b0 const e0, AM 16/16 distinct 14ch, mtab
  b30,39,47,80-83, raw lencode b4=(0x17+2off)&FF
  b5 const 50 NO step NO edge),
  C 141339-348 C10-1SIG-88-TAIL-M4 (1d000000 x10
  DIFFERS-from-PB1-sig via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87,
  b5 const 50 raw lencode),
  Q 141349-412 QUAD88-1SIG-QM7/R1-NOEDGE (QM7
  b52,53,54,80-83 M 16/16 14ch NO-frags + R1
  b84 rows 41/61/81/a1 (4/4 UNPAIRED, BY-ROW const)
  + tails R1+3f2ba9 above, b5 const 50
  raw lencode NO edge),
  R 141413-668 T88-ring SWAPPED (sig 051e0000 x256,
  b0 const 05, b1 const 1e,
  code-TM8 b6,7,8,9,76-79 by COL RM 16/16,
  code-TR7 b52,53,54,80-83 by ROW RQ 16/16 UNPAIRED,
  SWAPPED tails, b84-87 const
  c13f2ba9 ring-wide, b4=(0xcb+2off)&FF +
  (off>=27)+(off>=155) (C literals 203/80/27/155
  verified == 0xcb/0x50/27/155)).
  C blocks carry T94899/94904/94909/94924/94939/94958
  py-line cites (each re-read: hits the exact
  py guard line, C comment text matches py), bounds +
  byte positions exact (A 14ch, C 8ch, Q 14/1ch,
  R 16/14ch),
  A/C/Q raw lencode (no counter literals) +
  R counter b4=(0xcb+2off)&FF + (off>=27)+(off>=155)
  (C literals 203/80/27/155 verified),
  temps _t7181-7196 (base max _t7180, no reuse) +
  _i4357/4359/4362/4365 (base max _i4355, no reuse) +
  _b4356/4358/4360/4361/4363/4364 (base max _b4354,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P357R close
  (C "T10P3580 singleton" after "CLOSED T10P357R"; py
  return 0 + S0 guard 94899), at dispatch tail
  (N-out-of-scope fallthrough follows: C 170526,
  py 94977; plateau guards at C 170460 /
  py 58826 are the T4 plateau, unrelated scope).
  Matches A-945 geometry (PB0 NEW-sig 31/84;
  PB1 NEW-sig 49/88; PBA88-PLAIN-M7b30 VPOS 8 sig-e0
  b5 const M7 16/16 distinct; C10-1SIG-88-TAIL-M4 VPOS 5
  DIFFERS-from-PB1-sig b5 const M4 10/10 diverge;
  QUAD88-1SIG-QM7/R1-NOEDGE VPOS 9 + R1 4/4 UNPAIRED
  41/61/81/a1 + suffix-lcs-3/3/3/3/3/3 +
  R1-distinct + NO frags + M-tails NEW;
  T88-SWAPPED VPOS 17 + TM8-by-COL/TR7-by-ROW +
  SWAPPED-tails + b84-87 c13f2ba9 +
  counter cb/50/27/155; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R1 rows +
  tails + LCS + SWP frame + consts stand;
  const-count note is tables==excl this tier per memo,
  geometry unaffected; M==RQ
  16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 17/50
  tail 35/50 b5set {50} NO step, 0 ff;
  C head 37/50 tail 49/50 b5set {50} NO step, 0 ff;
  Q head 4b/50 tail c9/50 b5set {50} NO edge, 0 ff
  (b4 base 0x4b step2 64/64 range 4b..c9, NO wrap);
  ring pre-edge off26 (ff/50), edge off27 (01/51);
  edge off154 (ff/51) -> off155 (01/52);
  exactly 2 ff in 256; R head cb/50 tail
  c9/52; formulas re-derived from T10P358R code text
  (cb/50/27/155) + T10P358A/C/Q text (raw lencode);
  all edge pins + mid pin 141500 + tail 141668 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (13/15 +
  50) match raw lencode. Ring counter==raw-lencode
  256/256 + Q 64/64 + A 16/16 + C 10/10. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges358.py EDGES-GREEN 71 PASS 0 FAIL,
  first run -- Q-range NO-wrap verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (for465base.nums subset for466.nums,
  removed 0; C-scope del 0).
- Wall on band diff added lines (scope be565d02..
  5f800ba0, 898 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons py-ind4 738->740 (+2: 141321/141322) /
  ranges py-ind4 862->866 (+4; C singletons 743->745 +2 /
  ranges 884->888 +4, same 6 P358 blocks both
  sides; no elif/else-if added either side: py file-wide
  elif 50 both, C else-if 0 both; deltas agree every side),
  CLOSED T10P prints 2036->2042 +6 both sides, seal
  2130->2136 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-945-q1070-P358
  verdict CONFIRM 50/50 CLEAN (own bed r5-P358
  141321..141696 + r5-P357 cross-refs, BAD=0;
  verifier v501.py P358 50/50 PASS; file present, counts
  verified; tier GATED PORT; novelty gated: M-tails 16/16
  ALL NEW vs P357T col-led tails; exact-value corroboration
  incl PB0 NEW-sig 31/84, PB1 NEW-sig 49/88,
  PBA16 sig-e0 VPOS 8, C10 sig-1d DIFFERS-PB1 VPOS 5,
  QUAD64 1-sig-NOEDGE + R1 rows +
  suffix-lcs-3/3/3/3/3/3 + R1-distinct +
  QM7 + NO frags + M-tails NEW, T256-SWAPPED
  + TM8-by-COL/TR7-by-ROW + SWAPPED-tails +
  const c13f2ba9 + counter/edges; plus const-count note:
  A-945 excl 79/82/78/71 memo-exact, committed
  tables match excl exactly -- no writer lag this tier,
  geometry exact, PORT verdict stands).
  Agrees with cport commit msg (PYID 10655, RGRAM 21310).
- FWD-check first-hand: A-945 "Next P359"
  forward notes verified against P359 lane code
  (6e01480c, git show, no checkout): PB0 ada6a40c @141669
  (168ch pay84) + PB1 19000000 @141670 (176ch pay88) +
  PBA multi d4010000+d5010000 (guard 141671..141686,
  16 cells) + C10-region 19000000 x10 (guard 141687..141696,
  10 cells) -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b466 (adjacent
  odds b465/b467 = sweep turf incl b465 C port be565d02 +
  b467 py-merge 6e01480c live, base-use only, no verdict
  on b466).
  Activity polled (no b466 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above).
- Logs: NVME ws tmp/encode-sweep2/r79/ (build466.log,
  build466.sha, pyid466.log, rgram466py/c.log, cmp sets
  (pass466py/c.names, pass466pyo/co.txt), for-466/465base.nums,
  for466.added/.removed, smoke466.log, units466.log, tables466.log,
  tabaudit358.py, edges358.py, edges466.log, band466.addedlines,
  band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
