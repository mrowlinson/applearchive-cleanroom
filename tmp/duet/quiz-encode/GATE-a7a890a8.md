# GATE a7a890a8 b490 T10P382 pins 149673..150020 (348) PASS-functional

Seat sweep2-r86c, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r86c/wB490 @a7a890a8.
Band = 1e3ca791 (py merge w2b@a068b673 partial, +6 tiers, +58 pins)
+ a7a890a8 (C port). Base b396d725 (b489 tip, 2274 tiers sealed,
odd-seat turf, used as diff-base only).
Band number from lane commit msg first-hand
(C port: "band490 T10P382 (pins 149673..150020, 2280 tiers sealed)";
py merge: "rgram T10P382 (pins 149673..150020, +6 tiers, +58 pins)").
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB490/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced21673
  (aae d6e27c97 = r52-r84 pinned + r86c buildB490.sha
  d6e27c97ced21673...; band touches no aae sources per numstat:
  rgramc.c + rgram.py + test_rgram.sh + PINS only).
- RGRAMC-PYID 11351/11351 covered=11351/11351 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 22702/22702 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 22702/22702 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 22702/22702; 11351 unique).
- PINS-RGRAM cells set-eq 22702/22702 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 11351/11351 xor 0;
  PINS 22704 rows (2 hdr + 22702 = PASS lines, +58 vs base
  22646).
  For-list union 11322->11351 +29 (149673 149674
  149675 149676 149682 149683 149689 149690 149691 149692
  149695 149696 149699 149700 149701 149716 149717 149733
  149759 149760 149764 149765 149887 149888 149951 150015
  150016 150017 150020),
  0 removed, added range 149673..150020 exact. Each for-N yields
  2 PASS lines (g-zN + g-zN-closed). 29x2 = 58 = 22702-22644.
  The 29 = S0/S1 (2) +
  A head-pair + mid-pair + tail-pair (6:
  head pair 149675/149676 off0/1, mid pair 149682/149683
  off7/8, tail pair 149689/149690 off14/15; b5 const 91
  NO step, PLAIN tier) +
  C head/mid/tail pairs (6: 149691/149692 off0/1,
  mid pair 149695/149696 off4/5, tail pair 149699/149700
  off8/9; b5 const 91 NO step) +
  Q head/mid-pair/mid/edge-pair/tail (7: head 149701 off0,
  mid pair 149716/149717 off15/16, mid 149733 off32,
  edge pair 149759/149760 off58/59 (pre-edge + B5EDGE 91->92),
  tail 149764 off63) +
  R head/edge-pair/mid/edge-triple/tail
  (8: head 149765 off0, edge pair 149887/149888 off122/123
  (pre-edge+edge),
  mid 149951 off186,
  edge triple 150015/150016/150017 off250/251/252
  (pre-edge+edge+post-edge),
  tail 150020 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg 1e3ca791; C-port leg a7a890a8 touched zero
  PINS rows + zero for-line); all 22702 rows
  test_rgram_fast.py-tagged, added 58 names == for-added
  closed+open pairs (29x2),
  sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P382 C-vs-py, script-compared, TABAUDIT-GREEN
  124 PASS 0 FAIL (tabaudit490.py rc=0, fresh first-hand,
  first green, no code findings;
  coverage checks run pre-exit, no dead code):
  S0 168ch sig 5f522927 NEW-sig (31/84 payload diff vs
  P381S0 5f522926 first-hand, NOT byte-equal) /
  S1 176ch sig 48000000 NEW-sig (48/88 payload diff vs P381S1
  4c000000 first-hand, NOT byte-equal; 41/88 diff vs
  own-C10[0] assembled n149691 first-hand, NOT byte-equal;
  sig DIFFERS-from-own-C10 48-vs-45),
  staged as full-payload singletons,
  AM 16/16 7ch distinct, CM 10/10 5ch distinct,
  M 16/16 8ch distinct, QR 4/4 2ch distinct, RM 16/16
  8ch distinct, RQ 16/16 8ch distinct, no QT (quad
  tails = R2 + consts b86/b87) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; Q uses M b52,53,54,55,80-83 by COL m=off&15 vs R
  uses RQ b52,53,54,55,76-79 by ROW r=off>>4 first-hand;
  string-identical HOLDS this tier -- reported, not gated),
  AC 79, CC 81, QC 76, RC 70; C _N decls
  79/81/76/70 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b30 sig 7e040000 (b0 const 7e, b5 CONST
  91 range-emergent via raw lencode NO step NO edge; AM 16/16
  distinct NO pair; M7 b30,39,47,80-83; lencode
  b4=(0x57+2off)&FF raw) + vs P381PBA (b0 const f0;
  novelty = NEW-sig 7e, AM 0-overlap).
  C10-1SIG-88-DIFFSIG-M5b45 sig 45000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 5ch b45,84,85,86,87; b5 CONST 91 range-emergent via
  raw lencode NO step; M5 DIFFSIG lane) + NEW-sig-vs-P381C10
  (45-vs-4f first-hand).
  QUAD88-1SIG-QM8/R2-B5EDGE 1-sig 7e040000
  SAME-sig-as-PBA (b0 const 7e in QC; b5 STEPS 91->92
  edge 149759->149760 via raw lencode tier-designed;
  QM8 b52,53,54,55,80-83 M 16/16 8ch NO frags, m = off&15
  first-hand; b84,85 R2 lane rows + b86 const 88 +
  b87 const 00 quad-wide) +
  r2 b84,85 R2 4/4 UNPAIRED BY-ROW (q = off>>4 first-hand;
  rows bef1/def1/fef1/1ef2 2ch exact);
  tails = R2 + 8800 4ch quad-wide,
  full-tail suffix-lcs 3/3/2/3/2/2 + R2 all-distinct +
  NO frags + M-tails NEW.
  Ring T88-STANDARD-TM8/TR8 1-sig e0470000 x256
  (b0 const e0 in RC, STANDARD frame;
  code-TM8 b6,7,8,9,80-83 by COL RM 16/16 + code-TR8
  b52,53,54,55,76-79 by ROW RQ 16/16 UNPAIRED
  (SPLIT tails b80-83 col / b76-79 row; positions staged
  P366R/P238R/P246R);
  b84-87 const 3ef28800 ring-wide;
  b4=(0x0b+2off)&FF +
  b5=0x92+(off>=123)+(off>=251) (C literals
  11/146/123/251 verified == 0x0b/0x92/123/251)).
  VPOS partitions re-derived from code: PBA 8
  (b4 + M7 b30,39,47,80-83; b5 const in lencode) /
  C10 6 (b4 + M5 b45,84,85,86,87; b5 const via lencode range) /
  quad 12 (b4,b5 + QM8 8 + R2 2) / T 18
  (b4,b5 + TM8 8 + TR8 8)
  -- all match q1130/A-965 census geometry.
  Code-consts vs census excl (PBA 79 / C10 81 /
  quad 76 / T88 70): impl 79/81/76/70 =
  exact all four, NO writer lag: committed tables match
  the census excl values exactly; geometry exact, PORT stands;
  memo PRESENT-CONFIRM this tier (41st even band running,
  no-lag this tier).
  QUAD 1SIG 7e SAME-sig-as-PBA this tier;
  PBA sig 7e NEW-vs-P381 (b0 f0);
  C10 sig 45 DIFFERS-as-own-PB1 + NEW-vs-P381C10;
  AC-QC both=73 sameval=55 (tables differ).
  No extra _T10P382 tables (12 symbols only: S0/S1/AM/AC/
  CM/CC/M/QR/QC/RM/RQ/RC; no T/Q/R/A/C -- tier-head C table
  absent this band, present-then-absent P380 vs P379/P381/P382
  first-hand, both legs agree).
  M-tails 16/16 ALL NEW vs P381RM col-led tails
  (zero overlap first-hand) AND 16/16 ALL NEW vs P381RQ
  row-led tails (zero overlap first-hand).
  AM/CM/M/RM/RQ/QR 0-overlap vs P381 (widths P382 vs
  P381: AM 7B vs 7B, CM 5B vs 5B, M 8B vs 7B, RM 8B vs 7B,
  RQ 8B vs 6B, QR 2B vs 4B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=149673 (PB0 sig 5f522927 NEW-sig 31/84,
  payB 84, embed b4/b5 53/91 == raw),
  S1 n=149674 (fat PB1 sig 48000000 NEW-sig,
  48/88 diff vs P381S1, 41/88 diff vs C10[0]
  n149691, DIFFERS-from-own-C10, payB 88, embed b4/b5 55/91),
  A 149675-690 PBA88-PLAIN-M7b30 (sig 7e040000 via AC
  b0-b3, b0 const 7e, mtab b30,39,47,80-83,
  lencode b4=(0x57+2off)&FF b5 const 91 NO edge raw),
  C 149691-149700 C10-1SIG-88-DIFFSIG-M5b45 (45000000 x10
  DIFFERS-from-PB1-sig via CC b0-3 + CM tab, CM 10/10
  b45,84,85,86,87, b5 const 91 NO step raw lencode),
  Q 149701-149764 QUAD88-1SIG-QM8/R2-B5EDGE (QM8
  b52,53,54,55,80-83 M 16/16 8ch NO-frags + R2
  b84,85 rows bef1/def1/fef1/1ef2
  (4/4 UNPAIRED, BY-ROW const, tails R2+8800) +
  tails R2+8800 above, b5 STEPS 91->92 edge
  149759->149760 pre-edge-ff/edge-01 raw lencode),
  R 149765-150020 T88-ring STANDARD-split (sig e0470000 x256
  b0 const e0, code-TM8 b6,7,8,9,80-83 by COL RM 16/16,
  code-TR6 b52,53,54,55,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b84-87 const 3ef28800 ring-wide,
  b4=(0x0b+2off)&FF + b5=0x92+(off>=123)+(off>=251) (C literals
  11/146/123/251 verified == 0x0b/0x92/123/251)),
  temps _t7565-7580 (base max _t7564, no reuse) +
  _i4597/4599/4602/4605 (base max _i4595, no reuse) +
  _b4596/4598/4600/4601/4603/4604 (base max _b4594,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P381R close
  (C "T10P3820 singleton" after "CLOSED T10P381R"; py
  return 0 + S0 guard 100455), at dispatch tail
  (N-out-of-scope fallthrough follows; plateau guards
  at C T34753 / py NOTE-w2s7-11 are the T4 plateau,
  unrelated scope).
  Matches census geometry (PB0 NEW-sig 31/84;
  PB1 NEW-sig 48/88 DIFFERS-as-own-C10 41/88; PBA88-PLAIN-M7b30
  VPOS 8 sig-7e b5-const M7 16/16 distinct; C10-1SIG-88-DIFFSIG-M5b45
  VPOS 6 DIFFERS-as-PB1-sig b5-const M5 10/10 +
  NEW-vs-P381C10; QUAD88-1SIG-QM8/R2-B5EDGE VPOS 12 +
  R2 4/4 UNPAIRED bef1/def1/fef1/1ef2 +
  suffix-lcs-3/3/2/3/2/2 +
  R2-distinct + NO frags + M-tails NEW;
  T88-STANDARD-TM8/TR8 VPOS 18 + TM8-by-COL/TR8-by-ROW +
  SPLIT-tails + b84-87 3ef28800 + 1-sig-const-b0 +
  counter 0b/92/123/251; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + LCS + M-tails NEW;
  M==RQ 16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 57/91
  tail 75/91; 0 ff in 16 (b5 const tier, PLAIN);
  C head 77/91 tail 89/91; 0 ff in 10 (b5 const tier);
  Q pre-edge off58 (ff/91), edge off59 (01/92);
  exactly 1 ff in 64; Q head 8b/91 tail 09/92;
  ring pre-edge off122 (ff/92), edge off123 (01/93);
  pre-edge off250 (ff/93) -> edge off251 (01/94);
  exactly 2 ff in 256; R head 0b/92 tail 09/94; formulas
  re-derived from T10P382R code text (0b/92/123/251) +
  T10P382A/C/Q text (raw lencode + b5 const/step);
  all edge pins + mid pins + tail 150020 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (53/91 +
  55/91) match raw lencode. Ring b5==raw-lencode
  256/256 + b4==raw 256/256 (tier-designed) +
  A b5-const 16/16 + C b5-const 10/10 + Q b5-formula 64/64.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges490.py EDGES-GREEN 47 PASS 0 FAIL,
  first green -- PLAIN-PBA + const-C10 + B5EDGE-quad +
  STANDARD-split ring verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB489base.nums subset forB490.nums,
  removed 0; C-scope del 0).
  Leg attribution first-hand: C-port leg a7a890a8 =
  rgramc.c 608/0 only; py-merge leg 1e3ca791 = rgram.py
  231/0 + test_rgram.sh 1/1 + PINS 58/0 only.
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons `^    if n == ` 786->788 (+2) /
  ranges `^    if N <= n <= ` 958->962 (+4; C singletons
  791->793 +2 / ranges 980->984 +4, same 6 P382 blocks both
  sides; py file-wide elif 50 both (0 added), C else-if 0 both;
  deltas agree every side),
  CLOSED T10P prints 2180->2186 +6 both sides, seal
  2274->2280 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence: memo A-sheet PRESENT for P382
  (A-965-q1130-P382 CONFIRM 50/50 CLEAN: Q1 geometry
  1x(100,84)+347x(104,88) EXACT + PB0 5f522927 pay84 +
  PB1 48000000 + PBA 7e/M7/b5-const + C10 45/M45,84-87/b5-const +
  QUAD 1-sig-7e SAME-PBA + T 1-sig-e0470000 STD; Q2 QM/R
  tails + suffix-lcs 3/3/2/3/2/2 + M-tails NEW + TM-by-COL/
  TR-by-ROW + 3ef28800; Q3 lencode 348/348 + consts 79/81/76/70 +
  0 stragglers NO D dips -- memo present).
  NOTE (first-hand correction, carried): r85-handoff cited A-1276/A-1278
  (P488/P490 = T10P488/490, wrong tiers -- band/tier number
  collision). Correct memos for b488=T10P380 were A-963/Q-1128
  and for b490=T10P382 are A-965/Q-1130,
  read first-hand this round, values match code exactly.
  Substitute first-hand (standing rule): writer census Q-1130
  (consts PBA 79 / C10 81 / quad 76 / T88 70; committed tables
  match excl exactly 79/81/76/70 -- no writer lag this tier,
  geometry exact, PORT verdict stands) + cport commit msg ev
  (PYID 11351, RGRAM 22702) + py-merge commit msg
  (RGRAM 22702) + own full battery above.
  Agrees with cport commit msg (PYID 11351, RGRAM 22702)
  and py-merge commit msg (RGRAM 22702).
- FWD-check first-hand: b491 T10P383 bank 46adc59a ancestor-verified
  on lanes/encode-writer2b (T10P383 pins 150021..150368 per bank
  commit msg; b491 C port status TBD, sweep turf TBD,
  base-use only for NEXT round). P382 head details verified exact
  against lane code during this gate (PB0 @149673 sig 5f522927 pay84
  NEW-sig 31/84 + PB1 48000000 pay88 @149674 NEW-sig 48/88 +
  PBA88 sig 7e040000 x16 @149675-690 + C10-region 45000000
  x10 @149691-149700 DIFFERS-PB1 -- all exact).
- Quiz: no conflicting CLAIM/GATE/FLAG on b490 (adjacent
  odds b489 = b396d725 C port + b491 C port TBD, base-use
  only, no verdict on odds).
  Activity polled (no b490 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above: S0 5f522927 / S1 48000000 / PBA 7e040000 /
  C10 45000000 / QUAD 7e040000 / T e0470000 /
  R2 bef1/def1/fef1/1ef2 / tails R2+8800 / b84-87 3ef28800 /
  counter 0b/92/123/251 / embeds 53/91 + 55/91).
- Logs: NVME ws tmp/encode-sweep2/r86c/ (buildB490.sha info,
  pyidB490.log, rgramB490py/c.log, cmp sets (passB490py/c.names,
  passB490pyo/co.txt), for-B489base/B490.nums, forB490.added/.removed,
  smokeB490.log, unitsB490.log, tablesB490.log, tabaudit490.py,
  edges490.py, edgesB490.log, band addedlines via git diff).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.

