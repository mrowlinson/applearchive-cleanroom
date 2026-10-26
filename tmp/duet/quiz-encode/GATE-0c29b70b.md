# GATE 0c29b70b b476 T10P368 pins 144801..145148 (2196 tiers) PASS-functional

Seat sweep2-r82, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r82/wB476 @0c29b70b.
Band = b5f97d8f (py merge w2b@0e637fcb partial, +6 tiers, +58 pins)
+ 0c29b70b (C port). Base 6a9df578 (b475 tip, 2190 tiers sealed,
odd-seat turf, used as diff-base only).
Band number from lane commit msg first-hand
(C port: "band476 T10P368 (pins 144801..145148, 2196 tiers sealed)";
py merge: "rgram T10P368 (pins 144801..145148, +6 tiers, +58 pins)").
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB476/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced2...
  (aae d6e27c97 = b288-b354 pinned + r52-r82 builds; r82 buildB476.sha
  d6e27c97ced21673...; band touches no aae sources per numstat:
  rgramc.c + rgram.py + test_rgram.sh + PINS only).
- RGRAMC-PYID 10945/10945 covered=10945/10945 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 21890/21890 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 21890/21890 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 21890/21890).
- PINS-RGRAM cells set-eq 21890/21890 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 10945/10945 xor 0;
  PINS 21892 rows (2 hdr + 21890 = PASS lines, +58 vs base
  21834).
  For-list union 10916->10945 +29 (144801 144802
  144803 144804 144810 144811 144817 144818 144819 144820
  144823 144824 144827 144828 144829 144844 144845 144860
  144861 144877 144892 144893 144895 144896 144897 145023
  145024 145025 145148),
  0 removed, range 144801..145148 exact. Each for-N yields
  2 PASS lines (g-zN + g-zN-closed). 29x2 = 58 = 21890-21832.
  The 29 = S0/S1 (2) + A head-pair/mid-pair/tail-pair (6:
  head pair 144803/144804 off0/1, mid pair 144810/144811
  off7/8, tail pair 144817/144818 off14/15; b5 const 6b
  range-emergent NO step, PLAIN tier) +
  C head/mid/tail pairs (6: 144819/144820 off0/1,
  mid pair 144823/144824 off4/5, tail pair 144827/144828
  off8/9; b5 const 6b NO step) +
  Q head/pair/pair/mid/tail (7: head 144829 off0,
  pair 144844/144845 off15/16, pair 144860/144861 off31/32,
  mid 144877 off48, tail 144892 off63; NO edge --
  b5 const 6b this tier) +
  R head/edge-pair/post-edge/pre-edge/edge/post-edge/tail
  (8: head 144893 off0, edge pair 144895/144896 off2/3,
  post-edge 144897 off4, pre-edge 145023 off130,
  edge 145024 off131, post-edge 145025 off132,
  tail 145148 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg b5f97d8f; C-port leg 0c29b70b touched zero
  PINS rows + zero for-line); all 21890 rows
  test_rgram_fast.py-tagged; added 58 names == for-added
  closed+open pairs (29x2),
  sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P368 C-vs-py, script-compared, TABAUDIT-GREEN
  134 PASS 0 FAIL (tabaudit476.py rc=0, fresh first-hand;
  coverage checks run pre-exit, no dead code):
  S0 168ch sig 2f9a600e SIG-REPEAT (30/84 payload diff vs
  P367S0 sig 2f9a600e first-hand, NOT byte-equal) /
  S1 176ch sig 1c000000 SIG-REPEAT (80/88 payload diff vs
  P367S1 first-hand, NOT byte-equal;
  30/88 diff vs own-C10[0] assembled n144819 first-hand,
  NOT byte-equal; sig DIFFERS-from-own-C10 1c-vs-1f),
  staged as full-payload singletons,
  AM 16/16 18ch distinct, CM 10/10 8ch distinct,
  M 16/16 16ch distinct, QR 4/4 2ch distinct, RM 16/16
  16ch distinct, RQ 16/16 16ch distinct, no QT (quad
  tails = R1 + consts b85/b86/b87) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; Q uses M b40,41,42,43,80-83 by COL m=off&15 vs R
  uses RQ b40,41,42,43,80-83 by ROW r=off>>4 first-hand;
  string-eq HOLDS this tier -- reported, not gated),
  AC 77, CC 82, QC 77, RC 70; C _N decls
  77/82/77/70 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M9b29 sig 88010000 (b0 const 88, b5 const
  6b range-emergent via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M9 b29,30,31,34,35,80-83; lencode b4=(0x47+2off)
  &FF raw) + vs P367PBA sig b6 (novelty = NEW-sig 88,
  AM 0-overlap; M9 FIRST this lane: P364 7B / P365 8B /
  P366 7B / P367 6B A-mtab widths all narrower).
  C10-1SIG-88-TAIL-M4 sig 1f000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 8ch b84,85,86,87; CC has no b84-87 (all in CM lane);
  b5 CONST 6b range-emergent via raw lencode NO step).
  QUAD88-1SIG-QM8/R1-NOEDGE 1-sig e5010000
  DIFFERS-from-PBA-sig (QC b0 const e5; b5 const 6b
  range-emergent raw lencode; QM8 b40,41,42,43,80-83
  M 16/16 16ch NO frags, m = off&15 first-hand;
  b85 const 57 + b86 const 97 + b87 const b2 quad-wide) +
  r1 b84 R1 4/4 UNPAIRED BY-ROW (q = off>>4 first-hand);
  tails = R1 + 5797b2 8ch quad-wide,
  full-tail suffix-lcs 3/3/3/3/3/3 + R1 all-distinct).
  Ring T88-SWAPPED-RM8/RQ8 1-sig
  (sig e51e0000 x256; b0 const e5; b1 const 1e;
  code-RM8 b30,39,46,47,76-79 by COL RM 16/16 (RM rows
  16ch) + code-RQ8 b40,41,42,43,80-83 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b76-79 col / b80-83 row); b84-87 const
  c9878ab4 ring-wide; b4=(0xfb+2off)&FF +
  b5=0x6b+(off>=3)+(off>=131) (C literals
  251/2/3/131 verified == 0xfb/step2/3/131)).
  VPOS partitions re-derived from code: PBA 10
  (b4 + M9 b29,30,31,34,35,80-83; b5 range-const in lencode) / C10 6
  (b4,b5 + M4 84,85,86,87; b5 const via lencode range) /
  quad 10 (b4 + QM8 8 + R1 1) / T 18
  (b4,b5 + RM8 8 + RQ8 8)
  -- all match qTBD-p368 census geometry.
  Code-consts vs census excl (PBA 77 / C10 82 /
  quad 77 / T88 70): impl 77/82/77/70 =
  exact all four, NO writer lag: committed tables match
  the census excl values exactly; geometry exact, PORT stands;
  FLAGGED for memo (34th even band running, no-lag this tier).
  QUAD 1SIG e5 DIFFERS-from-PBA-sig this tier;
  PBA sig 88 NEW-vs-P367 (b6->88);
  AC-QC both=72 sameval=49 (tables differ).
  M-tails 16/16 ALL NEW vs P367RM col-led tails
  (zero overlap first-hand) AND 16/16 ALL NEW vs P367RQ
  row-led tails (zero overlap first-hand; P367T is SWAPPED,
  both refs novel).
  AM/CM/M/RM/RQ/QR 0-overlap vs P367 (widths P368 vs
  P367: AM 9B vs 6B, CM 4B vs 3B, M 8B vs 7B, RM 8B vs 8B,
  RQ 8B vs 7B, QR 1B vs 1B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=144801 (PB0 sig 2f9a600e SIG-REPEAT,
  30/84 diff, payB 84, embed b4/b5 43/6b == raw),
  S1 n=144802 (fat PB1 sig 1c000000 SIG-REPEAT,
  80/88 diff vs P367S1, 30/88 diff vs C10[0]
  n144819, DIFFERS-from-own-C10, payB 88, embed 45/6b),
  A 144803-818 PBA88-PLAIN-M9b29 (sig 88010000 via AC
  b0-b3, b0 const 88, mtab b29,30,31,34,35,80-83,
  lencode b4=(0x47+2off)&FF b5 range-const 6b NO edge),
  C 144819-828 C10-1SIG-88-TAIL-M4 (1f000000 x10
  DIFFERS-from-PB1-sig via CC b0-3 + CM tab, CM 10/10
  b84-87, b5 const 6b NO step raw lencode),
  Q 144829-892 QUAD88-1SIG-QM8/R1-NOEDGE (QM8
  b40,41,42,43,80-83 M 16/16 16ch NO-frags + R1
  b84 rows 93/b3/d3/f3 (4/4 UNPAIRED, BY-ROW const) +
  tails R1+5797b2 above, b5 const 6b raw lencode NO edge),
  R 144893-145148 T88-ring SWAPPED (sig e51e0000 x256,
  b0 const e5, b1 const 1e,
  code-RM8 b30,39,46,47,76-79 by COL RM 16/16,
  code-RQ8 b40,41,42,43,80-83 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b84-87 const c9878ab4 ring-wide,
  b4=(0xfb+2off)&FF + b5=0x6b+(off>=3)+(off>=131) (C literals
  251/2/3/131 verified == 0xfb/step2/3/131)),
  temps _t7341-7356 (base max _t7340, no reuse) +
  _i4457/4459/4462/4465 (base max _i4455, no reuse) +
  _b4456/4458/4460/4461/4463/4464 (base max _b4454,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P367R close
  (C "T10P3680 singleton" after "CLOSED T10P367R"; py
  return 0 + S0 guard 97213), at dispatch tail
  (N-out-of-scope fallthrough follows; plateau guards
  at C T34753 / py NOTE-w2s7-11 are the T4 plateau,
  unrelated scope).
  Matches census geometry (PB0 SIG-REPEAT 30/84;
  PB1 SIG-REPEAT 80/88 DIFFERS-own-C10 30/88; PBA88-PLAIN-M9b29
  VPOS 10 sig-88 b5-const M9 16/16 distinct; C10-1SIG-88-TAIL-M4
  VPOS 6 DIFFERS-from-PB1-sig b5-const M4 10/10;
  QUAD88-1SIG-QM8/R1-NOEDGE VPOS 10 + R1 4/4 UNPAIRED
  93/b3/d3/f3 + suffix-lcs-3/3/3/3/3/3 +
  R1-distinct + NO frags + M-tails NEW;
  T88-SWAPPED-RM8/RQ8 VPOS 18 + RM8-by-COL/RQ8-by-ROW +
  SPLIT-tails + b84-87 c9878ab4 +
  counter fb/6b/3/131; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R1 rows +
  tails + LCS + SWAPPED frame + consts stand;
  M==RQ 16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 47/6b
  tail 65/6b; 0 ff in 16 (PLAIN tier, b5 range-const);
  C head 67/6b tail 79/6b; 0 ff in 10 (b5 const tier);
  Q head 7b/6b tail f9/6b b5set {6b} NO edge, 0 ff
  (b4 base 0x7b step2 64/64 range 7b..f9, NO wrap);
  ring pre-edge off2 (ff/6b), edge off3 (01/6c);
  edge off130 (ff/6c) -> off131 (01/6d);
  exactly 2 ff in 256; R head fb/6b tail f9/6d; formulas
  re-derived from T10P368R code text (fb/6b/3/131) +
  T10P368A/C/Q text (raw lencode + b5 const);
  all edge pins + mid pins + tail 145148 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (43/6b +
  45/6b) match raw lencode. Ring counter==raw-lencode
  256/256 + Q 64/64 + A 16/16 + C 10/10. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges476.py EDGES-GREEN 45 PASS 0 FAIL,
  first run -- PLAIN PBA + const-C10 + NOEDGE-quad verified
  first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 230/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB475base.nums subset forB476.nums,
  removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons `^    if n == ` 758->760 (+2) /
  ranges `^    if N <= n` 902->906 (+4; C singletons 758->760 +2 /
  ranges 902->906 +4, same 6 P368 blocks both
  sides; no elif/else-if added either side: py file-wide
  elif 0 both, C else-if 0 both; deltas agree every side),
  CLOSED T10P prints 2096->2102 +6 both sides, seal
  2190->2196 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence: NO memo A-sheet for P368 at gate time
  (A-955-q1080 + Q-1080-w2b ABSENT, verified first-hand via
  ls; cport-r66 claim concurs). Substitute first-hand:
  writer census NOTE-w2b-r33-qTBD-p368 (consts PBA 77 / C10
  82 / quad 77 / T88 70; committed tables match excl
  exactly 77/82/77/70 -- no writer lag this tier, geometry
  exact, PORT verdict stands) + cport-r66-hb1 ev (SET-EQ
  21890, PYID 10945, probes 29/29, RECORD FULL-IDENT 21892
  rows byte-ident, 0 DISSENT) + own full battery above.
  Agrees with cport commit msg (PYID 10945, RGRAM 21890)
  and py-merge commit msg (RGRAM 21890).
- FWD-check first-hand: b477 T10P369 bank e5a89b49 rev-parse
  verified on lanes/encode-writer2b (T10P369 pins 145149..145496
  per bank commit msg); r66 NEXT per hb1. P368 head details
  from r65 handoff verified exact against lane code during
  this gate (PB0 @144801 sig 2f9a600e pay84 sigREPEAT 30/84 +
  PB1 1c000000 pay88 @144802 sigREPEAT 80/88 +
  PBA88 sig 88010000 x16 @144803-818 + C10-region 1f000000
  x10 @144819-828 DIFFERS-PB1 -- all exact).
- Quiz: no conflicting CLAIM/GATE/FLAG on b476 (adjacent
  odds b475 = 6a9df578 C port + b477 unknown, base-use only,
  no verdict on odds).
  Activity polled (no b476 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above: S0 2f9a600e / S1 1c000000 / PBA 88010000 /
  C10 1f000000 / QUAD e5010000 / T e51e0000 / R1 93/b3/d3/f3 /
  tails 5797b2 / b84-87 c9878ab4 / counter fb/6b/3/131 /
  embeds 43/6b + 45/6b; 1 pre-file slip fixed -- hb30
  T10P typo, no gate impact).
- Logs: NVME ws tmp/encode-sweep2/r82/ (buildB476.sha info,
  pyidB476.log, rgramB476py/c.log, cmp sets (passB476py/c.names,
  passB476pyo/co.txt), for-B475base/B476.nums, forB476.added/.removed,
  smokeB476.log, unitsB476.log, tablesB476.log, tabaudit476.py,
  edges476.py, edgesB476.log, bandB476.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
