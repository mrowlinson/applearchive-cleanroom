# GATE 09b93c5d b478 T10P370 pins 145497..145844 (2208 tiers) PASS-functional

Seat sweep2-r82, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r82/wB478 @09b93c5d.
Band = a97cf8ea (py merge w2b@6e17eacd partial, +6 tiers, +58 pins)
+ 09b93c5d (C port). Base e9c52e90 (b477 tip, 2202 tiers sealed,
odd-seat turf, used as diff-base only).
Band number from lane commit msg first-hand
(C port: "band478 T10P370 (pins 145497..145844, 2208 tiers sealed)";
py merge: "rgram T10P370 (pins 145497..145844, +6 tiers, +58 pins)").
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB478/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced2...
  (aae d6e27c97 = b288-b354 pinned + r52-r82 builds; r82 buildB478.sha
  d6e27c97ced21673...; band touches no aae sources per numstat:
  rgramc.c + rgram.py + test_rgram.sh + PINS only).
- RGRAMC-PYID 11003/11003 covered=11003/11003 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 22006/22006 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 22006/22006 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 22006/22006).
- PINS-RGRAM cells set-eq 22006/22006 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 11003/11003 xor 0;
  PINS 22008 rows (2 hdr + 22006 = PASS lines, +58 vs base
  21950).
  For-list union 10974->11003 +29 (145497 145498
  145499 145500 145506 145507 145513 145514 145515 145516
  145519 145520 145523 145524 145525 145535 145536 145540
  145556 145572 145588 145589 145602 145603 145663 145664
  145791 145792 145844),
  0 removed, range 145497..145844 exact. Each for-N yields
  2 PASS lines (g-zN + g-zN-closed). 29x2 = 58 = 22006-21948.
  The 29 = S0/S1 (2) + A head-pair/mid-pair/tail-pair (6:
  head pair 145499/145500 off0/1, mid pair 145506/145507
  off7/8, tail pair 145513/145514 off14/15; b5 const 70
  range-emergent NO step, PLAIN tier) +
  C head/mid/tail pairs (6: 145515/145516 off0/1,
  mid pair 145519/145520 off4/5, tail pair 145523/145524
  off8/9; b5 const 70 NO step) +
  Q head/edge-pair/mid/mid/mid/tail (7: head 145525 off0,
  edge pair 145535/145536 off10/11 (B5EDGE 70->71),
  mid 145540 off15, mid 145556 off31, mid 145572 off47,
  tail 145588 off63) +
  R head/mid-pair/edge-pair/edge-pair/tail
  (8: head 145589 off0, mid pair 145602/145603 off13/14,
  edge pair 145663/145664 off74/75,
  edge pair 145791/145792 off202/203,
  tail 145844 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg a97cf8ea; C-port leg 09b93c5d touched zero
  PINS rows + zero for-line); all 22006 rows
  test_rgram_fast.py-tagged; added 58 names == for-added
  closed+open pairs (29x2),
  sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P370 C-vs-py, script-compared, TABAUDIT-GREEN
  136 PASS 0 FAIL (tabaudit478.py rc=0, fresh first-hand;
  coverage checks run pre-exit, no dead code;
  1 pre-run script fix: CC-sig b1 byte 01->00, tree untouched):
  S0 168ch sig ef928b0c NEW-sig 1B-off (34/84 payload diff vs
  P369S0 first-hand, NOT byte-equal) /
  S1 176ch sig 19000000 NEW-sig (56/88 payload diff vs
  P369S1 first-hand, NOT byte-equal;
  28/88 diff vs own-C10[0] assembled n145515 first-hand,
  NOT byte-equal; sig SAME-as-own-C10 19-vs-19),
  staged as full-payload singletons,
  AM 16/16 14ch distinct, CM 10/10 10ch distinct,
  M 16/16 16ch distinct, QR 4/4 4ch distinct, RM 16/16
  20ch distinct, RQ 16/16 16ch distinct, no QT (quad
  tails = R2 + consts b86/b87) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; Q uses M b28,29,30,31,80-83 by COL m=off&15 vs R
  uses RQ b28,29,30,31,76-79 by ROW r=off>>4 first-hand;
  string-identical HOLDS this tier -- reported, not gated),
  AC 79, CC 81, QC 76, RC 68; C _N decls
  79/81/76/68 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b20 sig 92010000 (b0 const 92, b5 const
  70 range-emergent via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M7 b20,21,22,80-83; lencode b4=(0xb7+2off)
  &FF raw) + vs P369PBA sig e5 (novelty = NEW-sig 92,
  AM 0-overlap).
  C10-1SIG-88-M5b20 sig 19000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 10ch b20,84,85,86,87; CC has no b20/b84-87
  (all in CM lane); b5 CONST 70 range-emergent via raw
  lencode NO step; M5 FIRST this lane: CM 10-char rows).
  QUAD88-1SIG-QM8/R2-B5EDGE 1-sig 92010000
  SAME-sig-as-PBA (QC b0 const 92; b5 STEPS 70->71
  edge 145535->145536 via raw lencode; QM8 b28,29,30,31,80-83
  M 16/16 16ch NO frags, m = off&15 first-hand;
  b84,85 R2 lane rows + b86 const ce + b87 const 40 quad-wide) +
  r2 b84,85 R2 4/4 UNPAIRED BY-ROW (q = off>>4 first-hand;
  rows e45a/045b/245b/445b 4-char FIRST);
  tails = R2 + ce40 8ch quad-wide,
  full-tail row+ce40 blcs 2/2/2/3/3/3 + R2 all-distinct).
  Ring T88-2SIG-COLSPLIT
  (sigs 8c180000 x32 (c=14,15 col-led b0=8c) + 82180000 x224;
  b1 const 18, b2/b3 const 0;
  code-TM10 b0,11,19,27,34,35,80-83 by COL RM 16/16 (RM rows
  20ch FIRST) + code-TR8 b28,29,30,31,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79 row); b84-87 const
  645bce40 ring-wide; b4=(0x6b+2off)&FF +
  b5=0x71+(off>=75)+(off>=203) (C literals
  107/2/75/203 verified == 0x6b/step2/75/203)).
  VPOS partitions re-derived from code: PBA 8
  (b4 + M7 b20,21,22,80-83; b5 range-const in lencode) / C10 7
  (b4,b5 + M5 b20,84,85,86,87; b5 const via lencode range) /
  quad 11 (b4 + QM8 8 + R2 2) / T 20
  (b4,b5 + TM10 10 + TR8 8)
  -- all match qTBD-p370 census geometry.
  Code-consts vs census excl (PBA 79 / C10 81 /
  quad 76 / T88 68): impl 79/81/76/68 =
  exact all four, NO writer lag: committed tables match
  the census excl values exactly; geometry exact, PORT stands;
  FLAGGED for memo (35th even band running, no-lag this tier).
  QUAD 1SIG 92 SAME-sig-as-PBA-sig this tier;
  PBA sig 92 NEW-vs-P369 (e5->92);
  AC-QC both=73 sameval=50 (tables differ).
  Extra table _T10P370C: pre-existing old-series head-row
  table (T10P370 head singleton, paylen 76), untouched by
  this band (zero added/removed lines; all band-diff hits
  are CM/CC prefix matches); harmless, covered by no-QT/no-F
  (not a quad/tail/frag table).
  M-tails 16/16 ALL NEW vs P369RM col-led tails
  (zero overlap first-hand) AND 16/16 ALL NEW vs P369RQ
  row-led tails (zero overlap first-hand; P369T is STANDARD,
  both refs novel).
  AM/CM/M/RM/RQ/QR 0-overlap vs P369 (widths P370 vs
  P369: AM 7B vs 8B, CM 5B vs 4B, M 8B vs 7B, RM 10B vs 7B,
  RQ 8B vs 7B, QR 2B vs 4B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=145497 (PB0 sig ef928b0c NEW-sig 1B-off,
  34/84 diff, payB 84, embed b4/b5 b3/70 == raw),
  S1 n=145498 (fat PB1 sig 19000000 NEW-sig,
  56/88 diff vs P369S1, 28/88 diff vs C10[0]
  n145515, SAME-as-own-C10, payB 88, embed b4/b5 b5/70),
  A 145499-514 PBA88-PLAIN-M7b20 (sig 92010000 via AC
  b0-b3, b0 const 92, mtab b20,21,22,80-83,
  lencode b4=(0xb7+2off)&FF b5 range-const 70 NO edge),
  C 145515-524 C10-1SIG-88-M5b20 (19000000 x10
  SAME-as-PB1-sig via CC b0-3 + CM tab, CM 10/10
  b20,84-87, b5 const 70 NO step raw lencode),
  Q 145525-588 QUAD88-1SIG-QM8/R2-B5EDGE (QM8
  b28,29,30,31,80-83 M 16/16 16ch NO-frags + R2
  b84,85 rows e45a/045b/245b/445b (4/4 UNPAIRED, BY-ROW const) +
  tails R2+ce40 above, b5 STEPS 70->71 edge
  145535->145536 raw lencode),
  R 145589-844 T88-ring 2SIG-COLSPLIT (sig 8c180000 x32
  col-led b0=8c iff c>=14 + sig 82180000 x224,
  b1 const 18,
  code-TM10 b0,11,19,27,34,35,80-83 by COL RM 16/16,
  code-TR8 b28,29,30,31,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b84-87 const 645bce40 ring-wide,
  b4=(0x6b+2off)&FF + b5=0x71+(off>=75)+(off>=203) (C literals
  107/2/75/203 verified == 0x6b/step2/75/203)),
  temps _t7373-7388 (base max _t7372, no reuse) +
  _i4477/4479/4482/4485 (base max _i4475, no reuse) +
  _b4476/4478/4480/4481/4483/4484 (base max _b4474,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P369R close
  (C "T10P3700 singleton" after "CLOSED T10P369R"; py
  return 0 + S0 guard 97675), at dispatch tail
  (N-out-of-scope fallthrough follows; plateau guards
  at C T34753 / py NOTE-w2s7-11 are the T4 plateau,
  unrelated scope).
  Matches census geometry (PB0 NEW-sig 1B-off 34/84;
  PB1 NEW-sig 56/88 SAME-own-C10 28/88; PBA88-PLAIN-M7b20
  VPOS 8 sig-92 b5-const M7 16/16 distinct; C10-1SIG-88-M5b20
  VPOS 7 SAME-as-PB1-sig b5-const M5 10/10 FIRST;
  QUAD88-1SIG-QM8/R2-B5EDGE VPOS 11 + R2 4/4 UNPAIRED
  e45a/045b/245b/445b + blcs-2/2/2/3/3/3 +
  R2-distinct + NO frags + M-tails NEW;
  T88-2SIG-COLSPLIT VPOS 20 + TM10-by-COL/TR8-by-ROW +
  SPLIT-tails + b84-87 645bce40 + 32/224 split +
  counter 6b/71/75/203; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + LCS + COLSPLIT frame + consts stand;
  M==RQ 16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head b7/70
  tail d5/70; 0 ff in 16 (PLAIN tier, b5 range-const);
  C head d7/70 tail e9/70; 0 ff in 10 (b5 const tier);
  Q pre-edge off10 (ff/70), edge off11 (01/71);
  exactly 1 ff in 64; Q head eb/70 tail 69/71;
  ring pre-edge off74 (ff/71), edge off75 (01/72);
  edge off202 (ff/72) -> off203 (01/73);
  exactly 2 ff in 256; R head 6b/71 tail 69/73; formulas
  re-derived from T10P370R code text (6b/71/75/203) +
  T10P370A/C/Q text (raw lencode + b5 step);
  all edge pins + mid pins + tail 145844 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (b3/70 +
  b5/70) match raw lencode. Ring counter==raw-lencode
  256/256 + Q b5-formula 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges478.py EDGES-GREEN 47 PASS 0 FAIL,
  first run -- PLAIN PBA + M5-C10 + B5EDGE-quad + COLSPLIT
  ring verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB477base.nums subset forB478.nums,
  removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons `^    if n == ` 762->764 (+2) /
  ranges `^    if N <= n` 910->914 (+4; C singletons 762->764 +2 /
  ranges 910->914 +4, same 6 P370 blocks both
  sides; no elif/else-if added either side: py file-wide
  elif 0 both, C else-if 0 both; deltas agree every side),
  CLOSED T10P prints 2108->2114 +6 both sides, seal
  2202->2208 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence: NO memo A-sheet for P370 at gate time
  (A-95x-q108x + Q-108x-w2b ABSENT for P370, verified first-hand
  via ls; cport-r66 claim concurs for P368, hb3 for P370).
  Substitute first-hand: writer census NOTE-w2b-r33-qTBD-p370
  (consts PBA 79 / C10 81 / quad 76 / T88 68; committed tables
  match excl exactly 79/81/76/68 -- no writer lag this tier,
  geometry exact, PORT verdict stands) + cport-r66-hb3 ev
  (SET-EQ 22006, PYID 11003, probes 29/29, RECORD FULL-IDENT
  22008 rows byte-ident, 0 DISSENT) + own full battery above.
  Agrees with cport commit msg (PYID 11003, RGRAM 22006)
  and py-merge commit msg (RGRAM 22006).
- FWD-check first-hand: b479 T10P371 bank 17479fd4 rev-parse
  verified on lanes/encode-writer2b (T10P371 pins 145845..146192
  per bank commit msg; r66 NEXT per hb3). P370 head details
  from r66 hb3 verified exact against lane code during this
  gate (PB0 @145497 sig ef928b0c pay84 NEW-sig-1B-off 34/84 +
  PB1 19000000 pay88 @145498 NEW-sig 56/88 +
  PBA88 sig 92010000 x16 @145499-514 + C10-region 19000000
  x10 @145515-524 SAME-PB1 -- all exact).
- Quiz: no conflicting CLAIM/GATE/FLAG on b478 (adjacent
  odds b477 = e9c52e90 C port + b479 unknown, base-use only,
  no verdict on odds).
  Activity polled (no b478 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above: S0 ef928b0c / S1 19000000 / PBA 92010000 /
  C10 19000000 / QUAD 92010000 / T 8c180000+82180000 /
  R2 e45a/045b/245b/445b / tails ce40 / b84-87 645bce40 /
  counter 6b/71/75/203 / embeds b3/70 + b5/70).
- Logs: NVME ws tmp/encode-sweep2/r82/ (buildB478.sha info,
  pyidB478.log, rgramB478py/c.log, cmp sets (passB478py/c.names,
  passB478pyo/co.txt), for-B477base/B478.nums, forB478.added/.removed,
  smokeB478.log, unitsB478.log, tablesB478.log, tabaudit478.py,
  edges478.py, edgesB478.log, bandB478.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
