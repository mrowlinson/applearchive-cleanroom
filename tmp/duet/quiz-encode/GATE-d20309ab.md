# GATE d20309ab b484 T10P376 pins 147585..147932 (2244 tiers) PASS-functional

Seat sweep2-r84, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r84/wB484 @d20309ab.
Band = 5101a773 (py merge w2b@6f57f6dc partial, +6 tiers, +58 pins)
+ d20309ab (C port). Base 246d3408 (b483 tip, odd-seat turf,
used as diff-base only).
Band number from lane commit msg first-hand
(C port: "band484 T10P376 (pins 147585..147932, 2244 tiers sealed)";
py merge: "rgram T10P376 (pins 147585..147932, +6 tiers, +58 pins)").
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB484/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced2...
  (aae d6e27c97 = b288-b354 pinned + r52-r84 builds; r84 buildB484.sha
  d6e27c97ced21673...; band touches no aae sources per numstat:
  rgramc.c + rgram.py + test_rgram.sh + PINS only).
- RGRAMC-PYID 11177/11177 covered=11177/11177 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 22354/22354 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 22354/22354 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 22354/22354).
- PINS-RGRAM cells set-eq 22354/22354 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 11177/11177 xor 0;
  PINS 22356 rows (2 hdr + 22354 = PASS lines, +58 vs base
  22298).
  For-list union 11148->11177 +29 (147585 147586
  147587 147588 147595 147596 147601 147602 147603 147604
  147607 147608 147611 147612 147613 147628 147629 147644
  147645 147660 147676 147677 147711 147712 147776 147839
  147840 147841 147932),
  0 removed, range 147585..147932 exact. Each for-N yields
  2 PASS lines (g-zN + g-zN-closed). 29x2 = 58 = 22354-22296.
  The 29 = S0/S1 (2) + A head-pair/mid-pair/tail-pair (6:
  head pair 147587/147588 off0/1, mid pair 147595/147596
  off8/9, tail pair 147601/147602 off14/15; b5 const 81
  range-emergent NO step, PLAIN tier) +
  C head/mid/tail pairs (6: 147603/147604 off0/1,
  mid pair 147607/147608 off4/5, tail pair 147611/147612
  off8/9; b5 const 81 NO step) +
  Q head/mid-pair/mid-pair/mid/tail (7: head 147613 off0,
  mid pair 147628/147629 off15/16, mid pair 147644/147645
  off31/32, mid 147660 off47, tail 147676 off63; b5 const
  81 tier-flat NO edge) +
  R head/edge-pair/mid/edge-triple/tail
  (8: head 147677 off0, edge pair 147711/147712 off34/35
  (pre-edge+edge),
  mid 147776 off99,
  edge triple 147839/147840/147841 off162/163/164
  (pre-edge+edge+post-edge),
  tail 147932 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg 5101a773; C-port leg d20309ab touched zero
  PINS rows + zero for-line); all 22354 rows
  test_rgram_fast.py-tagged; added 58 names == for-added
  closed+open pairs (29x2),
  sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P376 C-vs-py, script-compared, TABAUDIT-GREEN
  133 PASS 0 FAIL (tabaudit484.py rc=0, fresh first-hand;
  coverage checks run pre-exit, no dead code;
  1 pre-run script fix: P375-AC-missing b0 (b0 lane-led in
  P375's 3SIG PBA, caught pre-run; tree untouched)):
  S0 168ch sig dcb0d222 NEW-sig (36/84 payload diff vs
  P375S0 first-hand, NOT byte-equal) /
  S1 176ch sig 44000000 NEW-sig (same sig-NEW vs P375S1
  22000000; 80/88 payload diff vs P375S1 first-hand, NOT
  byte-equal; 41/88 diff vs own-C10[0] assembled n147603
  first-hand, NOT byte-equal; sig DIFFERS-from-own-C10
  44-vs-45),
  staged as full-payload singletons,
  AM 16/16 9ch distinct, CM 10/10 4ch distinct,
  M 16/16 9ch distinct, QR 4/4 2ch distinct, RM 16/16
  7ch distinct, RQ 16/16 9ch distinct, no QT (quad
  tails = R2 + consts b86/b87) + no RT (SWAPPED tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; Q uses M b40,41,42,43,44,80-83 by COL m=off&15 vs R
  uses RQ b40,41,42,43,44,80-83 by ROW r=off>>4 first-hand;
  string-identical HOLDS this tier -- reported, not gated),
  AC 77, CC 82, QC 75, RC 70; C _N decls
  77/82/75/70 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M9b29 sig 29040000 (b0 const 29, b5 const
  81 range-emergent via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M9 b29,30,31,34,35,80-83; lencode
  b4=(0x07+2off)&FF raw) + vs P375PBA 3SIG-M7b0
  (08020000 x6 + 10020000 x1 + 24020000 x9 ORDERED,
  b0 lane-led 08/10/24; novelty = NEW-sig 29,
  AM 0-overlap).
  C10-1SIG-88-TAIL-M4 sig 45000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 4ch b84,85,86,87; CC HAS b80-83 consts
  c7/f4/c3/86; b5 CONST 81 range-emergent via
  raw lencode NO step; M4 4B lane) + sig-REPEATs-P375-C10
  (45 SAME as P375C10 45 -- first REPEAT-note this tier
  family; S1 does NOT repeat).
  QUAD88-1SIG-QM9/R2-NOEDGE 1-sig d8040000
  DIFFERS-from-PBA-sig (b0 const d8 in QC; b5 CONST 81
  tier-flat via raw lencode NO edge -- differs from P374
  B5EDGE quad;
  QM9 b40,41,42,43,44,80-83 M 16/16 9ch NO frags, m = off&15
  first-hand; b84,85 R2 lane rows + b86 const 3d +
  b87 const f8 quad-wide) +
  r2 b84,85 R2 4/4 UNPAIRED BY-ROW (q = off>>4 first-hand;
  rows aeee/ceee/eeee/0eef 4-char exact);
  tails = R2 + 3df8 8ch quad-wide,
  full-tail suffix-lcs 3/3/2/3/2/2 + R2 all-distinct).
  Ring T88-SWP-TM7/TR9 1-sig d8410000 x256
  (b0 const d8 in RC, SWAPPED frame -- differs from P374
  STANDARD ring;
  code-TM7 b39,46,47,76-79 by COL RM 16/16 + code-TR9
  b40,41,42,43,44,80-83 by ROW RQ 16/16 UNPAIRED
  (SWAPPED tails: M carries 76-79 here, RQ carries 80-83;
  positions FIRST this lane);
  b84-87 const 2eef3df8 ring-wide; b4=(0xbb+2off)&FF +
  b5=0x81+(off>=35)+(off>=163) (C literals
  187/129/35/163 verified == 0xbb/0x81/35/163)).
  VPOS partitions re-derived from code: PBA 10
  (b4 + M9 b29,30,31,34,35,80-83; b5 range-const in lencode) /
  C10 5 (b4 + M4 b84,85,86,87; b5 const via lencode range) /
  quad 12 (b4 + QM9 9 + R2 2; b5 flat-const, NO step this tier) /
  T 18 (b4,b5 + TM7 7 + TR9 9)
  -- all match q1124/A-959 census geometry.
  Code-consts vs census excl (PBA 77 / C10 82 /
  quad 75 / T88 70): impl 77/82/75/70 =
  exact all four, NO writer lag: committed tables match
  the census excl values exactly; geometry exact, PORT stands;
  memo PRESENT-CONFIRM this tier (38th even band running,
  no-lag this tier).
  QUAD 1SIG d8 DIFFERS-sig-from-PBA-sig this tier;
  PBA sig 29 NEW-vs-P375 (3SIG 08/10/24);
  C10 sig 45 REPEATs-P375-C10;
  AC-QC both=70 sameval=42 (tables differ).
  No extra _T10P376 tables (12 symbols only: S0/S1/AM/AC/
  CM/CC/M/QR/QC/RM/RQ/RC; no pre-existing collision this tier).
  M-tails 16/16 ALL NEW vs P375RM col-led tails
  (zero overlap first-hand) AND 16/16 ALL NEW vs P375RQ
  row-led tails (zero overlap first-hand).
  AM/CM/M/RM/RQ/QR 0-overlap vs P375 (widths P376 vs
  P375: AM 9B vs 7B, CM 4B vs 5B, M 9B vs 8B, RM 7B vs 6B,
  RQ 9B vs 8B, QR 2B vs 1B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=147585 (PB0 sig dcb0d222 NEW-sig 36/84,
  payB 84, embed b4/b5 03/81 == raw),
  S1 n=147586 (fat PB1 sig 44000000 NEW-sig,
  80/88 diff vs P375S1, 41/88 diff vs C10[0]
  n147603, DIFFERS-own-C10, payB 88, embed b4/b5 05/81),
  A 147587-602 PBA88-PLAIN-M9b29 (sig 29040000 via AC
  b0-b3, b0 const 29, mtab b29,30,31,34,35,80-83,
  lencode b4=(0x07+2off)&FF b5 range-const 81 NO edge),
  C 147603-612 C10-1SIG-88-TAIL-M4 (45000000 x10
  DIFFERS-from-PB1-sig via CC b0-3 + CM tab, CM 10/10
  b84,85,86,87, b5 const 81 NO step raw lencode),
  Q 147613-676 QUAD88-1SIG-QM9/R2-NOEDGE (QM9
  b40,41,42,43,44,80-83 M 16/16 9ch NO-frags + R2
  b84,85 rows aeee/ceee/eeee/0eef (4/4 UNPAIRED, BY-ROW const) +
  tails R2+3df8 above, b5 CONST 81 tier-flat NO edge
  raw lencode tier-designed),
  R 147677-147932 T88-ring SWAPPED (sig d8410000 x256
  b0 const d8, code-TM7 b39,46,47,76-79 by COL RM 16/16,
  code-TR9 b40,41,42,43,44,80-83 by ROW RQ 16/16 UNPAIRED,
  SWAPPED tails, b84-87 const 2eef3df8 ring-wide,
  b4=(0xbb+2off)&FF + b5=0x81+(off>=35)+(off>=163) (C literals
  187/129/35/163 verified == 0xbb/0x81/35/163)),
  temps _t7469-7484 (base max _t7468, no reuse) +
  _i4537/4539/4542/4545 (base max _i4535, no reuse) +
  _b4536/4538/4540/4541/4543/4544 (base max _b4534,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P375R close
  (C "T10P3760 singleton" after "CLOSED T10P375R"; py
  return 0 + S0 guard 99065), at dispatch tail
  (N-out-of-scope fallthrough follows; plateau guards
  at C T34753 / py NOTE-w2s7-11 are the T4 plateau,
  unrelated scope).
  Matches census geometry (PB0 NEW-sig 36/84;
  PB1 NEW-sig 80/88 DIFFERS-own-C10 41/88; PBA88-PLAIN-M9b29
  VPOS 10 sig-29 b5-const M9 16/16 distinct; C10-1SIG-88-TAIL-M4
  VPOS 5 DIFFERS-from-PB1-sig b5-const M4 10/10 +
  sig-REPEATs-P375-C10; QUAD88-1SIG-QM9/R2-NOEDGE VPOS 12 +
  R2 4/4 UNPAIRED aeee/ceee/eeee/0eef + suffix-lcs-3/3/2/3/2/2 +
  R2-distinct + NO frags + M-tails NEW;
  T88-SWP-TM7/TR9 VPOS 18 + TM7-by-COL/TR9-by-ROW +
  SWAPPED-tails + b84-87 2eef3df8 + 1-sig-const-b0 +
  counter bb/81/35/163; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + LCS + NOEDGE-quad + consts stand;
  M==RQ 16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 07/81
  tail 25/81; 0 ff in 16 (PLAIN tier, b5 range-const);
  C head 27/81 tail 39/81; 0 ff in 10 (b5 const tier);
  Q 0 ff in 64 (b5 flat-const tier, NO edge);
  Q head 3b/81 tail b9/81;
  ring pre-edge off34 (ff/81), edge off35 (01/82);
  pre-edge off162 (ff/82) -> edge off163 (01/83);
  exactly 2 ff in 256; R head bb/81 tail b9/83; formulas
  re-derived from T10P376R code text (bb/81/35/163) +
  T10P376A/C/Q text (raw lencode + b5 const);
  all edge pins + mid pins + tail 147932 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (03/81 +
  05/81) match raw lencode. Ring b5==raw-lencode
  256/256 + b4==raw 256/256 (tier-designed) +
  Q b5-formula 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges484.py EDGES-GREEN 45 PASS 0 FAIL;
  1 post-write script fix: Q-tail b9-not-a9 hand-slip,
  caught pre-final-run; tree untouched -- PLAIN PBA +
  M4-C10 + NOEDGE-quad + SWAPPED ring verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB483base.nums subset forB484.nums,
  removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons `^    if n == ` 774->776 (+2) /
  ranges `^    if N <= n <= ` 934->938 (+4; C singletons
  779->781 +2 / ranges 956->960 +4, same 6 P376 blocks both
  sides; py file-wide elif 50 both (0 added), C else-if 0 both;
  deltas agree every side),
  CLOSED T10P prints 2144->2150 +6 both sides, seal
  2238->2244 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence: memo A-sheet PRESENT for P376
  (A-959-q1124-P376 CONFIRM 49/49 CLEAN: Q1 geometry
  1x(100,84)+347x(104,88) EXACT + PB1 44000000 + PBA
  29/M9/b5-81 + C10 45/M84-87/b5-81 + QUAD 1-sig-d8
  DIFFERS-PBA + T 1-sig-d8410000 SWP; Q2 QM/R2 tails +
  suffix-lcs 3/3/2/3/2/2 + M-tails NEW + TM-by-COL/TR-by-ROW +
  2eef3df8; Q3 lencode 348/348 + consts 77/82/75/70 +
  0 stragglers NO D dips -- memo present).
  Substitute first-hand (standing rule): writer census Q-1124
  (consts PBA 77 / C10 82 / quad 75 / T88 70; committed tables
  match excl exactly 77/82/75/70 -- no writer lag this tier,
  geometry exact, PORT verdict stands) + cport commit msg ev
  (PYID 11177, RGRAM 22354) + py-merge commit msg
  (RGRAM 22354) + own full battery above.
  Agrees with cport commit msg (PYID 11177, RGRAM 22354)
  and py-merge commit msg (RGRAM 22354).
- FWD-check first-hand: b485 T10P377 bank c37c2d27 ancestor-verified
  on lanes/encode-writer2b (T10P377 pins 147933..148280 per bank
  commit msg; b485 C port NOT landed, odd sweep turf, base-use
  only for NEXT round). P376 head details verified exact against
  lane code during this gate (PB0 @147585 sig dcb0d222 pay84
  NEW-sig 36/84 + PB1 44000000 pay88 @147586 NEW-sig 80/88 +
  PBA88 sig 29040000 x16 @147587-602 + C10-region 45000000
  x10 @147603-612 DIFFERS-PB1 -- all exact).
- Quiz: no conflicting CLAIM/GATE/FLAG on b484 (adjacent
  odds b483 = 246d3408 C port + b485 C port NOT landed, base-use
  only, no verdict on odds).
  Activity polled (no b484 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above: S0 dcb0d222 / S1 44000000 / PBA 29040000 /
  C10 45000000 / QUAD d8040000 / T d8410000 /
  R2 aeee/ceee/eeee/0eef / tails 3df8 / b84-87 2eef3df8 /
  counter bb/81/35/163 / embeds 03/81 + 05/81).
- Logs: NVME ws tmp/encode-sweep2/r84/ (buildB484.sha info,
  pyidB484.log, rgramB484py/c.log, cmp sets (passB484py/c.names,
  passB484pyo/co.txt), for-B483base/B484.nums, forB484.added/.removed,
  smokeB484.log, unitsB484.log, tablesB484.log, tabaudit484.py,
  edges484.py, edgesB484.log, bandB484.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
