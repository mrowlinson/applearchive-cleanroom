# GATE e988dbb5 b486 T10P378 pins 148281..148628 (2256 tiers) PASS-functional

Seat sweep2-r84, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r84/wB486 @e988dbb5.
Band = a0fd3014 (py merge w2b@68747e6d partial, +6 tiers, +58 pins)
+ e988dbb5 (C port). Base ac53e2c4 (b485 tip, 2250 tiers sealed,
odd-seat turf, used as diff-base only).
Band number from lane commit msg first-hand
(C port: "band486 T10P378 (pins 148281..148628, 2256 tiers sealed)";
py merge: "rgram T10P378 (pins 148281..148628, +6 tiers, +58 pins)").
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB486/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced2...
  (aae d6e27c97 = b288-b354 pinned + r52-r84 builds; r84 buildB486.sha
  d6e27c97ced21673...; band touches no aae sources per numstat:
  rgramc.c + rgram.py + test_rgram.sh + PINS only).
- RGRAMC-PYID 11235/11235 covered=11235/11235 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 22470/22470 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 22470/22470 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 22470/22470).
- PINS-RGRAM cells set-eq 22470/22470 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 11235/11235 xor 0;
  PINS 22472 rows (2 hdr + 22470 = PASS lines, +58 vs base
  22414).
  For-list union 11206->11235 +29 (148281 148282
  148283 148284 148290 148291 148297 148298 148299 148300
  148303 148304 148307 148308 148309 148324 148325 148340
  148351 148352 148372 148373 148479 148480 148544 148607
  148608 148609 148628),
  0 removed, range 148281..148628 exact. Each for-N yields
  2 PASS lines (g-zN + g-zN-closed). 29x2 = 58 = 22470-22412.
  The 29 = S0/S1 (2) + A head-pair/mid-pair/tail-pair (6:
  head pair 148283/148284 off0/1, mid pair 148290/148291
  off7/8, tail pair 148297/148298 off14/15; b5 const 86
  range-emergent NO step, PLAIN tier) +
  C head/mid/tail pairs (6: 148299/148300 off0/1,
  mid pair 148303/148304 off4/5, tail pair 148307/148308
  off8/9; b5 const 86 NO step) +
  Q head/mid-pair/mid/edge-pair/tail (7: head 148309 off0,
  mid pair 148324/148325 off15/16, mid 148340 off31,
  edge pair 148351/148352 off42/43 (B5EDGE 86->87),
  tail 148372 off63) +
  R head/edge-pair/mid/edge-triple/tail
  (8: head 148373 off0, edge pair 148479/148480 off106/107
  (pre-edge+edge),
  mid 148544 off171,
  edge triple 148607/148608/148609 off234/235/236
  (pre-edge+edge+post-edge),
  tail 148628 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg a0fd3014; C-port leg e988dbb5 touched zero
  PINS rows + zero for-line); all 22470 rows
  test_rgram_fast.py-tagged; added 58 names == for-added
  closed+open pairs (29x2),
  sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P378 C-vs-py, script-compared, TABAUDIT-GREEN
  135 PASS 0 FAIL (tabaudit486.py rc=0, fresh first-hand,
  first run green, no script fix needed;
  coverage checks run pre-exit, no dead code):
  S0 168ch sig df017f24 NEW-sig (33/84 payload diff vs
  P377S0 df017f20 first-hand, NOT byte-equal) /
  S1 176ch sig 49000000 NEW-sig (46/88 payload diff vs P377S1
  41000000 first-hand, NOT byte-equal; 23/88 diff vs
  own-C10[0] assembled n148299 first-hand, NOT byte-equal;
  sig SAME-as-own-C10 49-vs-49),
  staged as full-payload singletons,
  AM 16/16 7ch distinct, CM 10/10 5ch distinct,
  M 16/16 8ch distinct, QR 4/4 1ch distinct, RM 16/16
  8ch distinct, RQ 16/16 8ch distinct, no QT (quad
  tails = R1 + consts b85/b86/b87) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; Q uses M b28,29,30,31,80-83 by COL m=off&15 vs R
  uses RQ b28,29,30,31,76-79 by ROW r=off>>4 first-hand;
  string-identical HOLDS this tier -- reported, not gated),
  AC 79, CC 81, QC 77, RC 70; C _N decls
  79/81/77/70 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b20 sig 9b040000 (b0 const 9b, b5 const
  86 range-emergent via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M7 b20,21,22,80-83; lencode
  b4=(0x77+2off)&FF raw) + vs P377PBA (b0 const d8;
  novelty = NEW-sig 9b, AM 0-overlap).
  C10-1SIG-88-M5b20 sig 49000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 5ch b20,84,85,86,87; b5 CONST 86 range-emergent via
  raw lencode NO step; M5 5B lane) + NEW-sig-vs-P377C10
  (49-vs-41 first-hand).
  QUAD88-1SIG-QM8/R1-B5EDGE 1-sig 9a040000
  DIFFERS-from-PBA-sig (b0 const 9a in QC; b5 STEPS 86->87
  edge 148351->148352 via raw lencode tier-designed;
  QM8 b28,29,30,31,80-83 M 16/16 8ch NO frags, m = off&15
  first-hand; b84 R1 lane rows + b85 const 31 +
  b86 const bd + b87 const 4d quad-wide) +
  r1 b84 R1 4/4 UNPAIRED BY-ROW (q = off>>4 first-hand;
  rows 2b/4b/6b/8b 2-char exact);
  tails = R1 + 31bd4d 8ch quad-wide,
  full-tail suffix-lcs 3/3/3/3/3/3 + R1 all-distinct).
  Ring T88-STANDARD-TM8/TR8 1-sig ab4f0000 x256
  (b0 const ab in RC, STANDARD frame;
  code-TM8 b19,27,34,35,80-83 by COL RM 16/16 + code-TR8
  b28,29,30,31,76-79 by ROW RQ 16/16 UNPAIRED
  (SPLIT tails b80-83 col / b76-79 row; positions staged
  P322R/P346R + P346R/P370R);
  b84-87 const ab31bd4d ring-wide; b4=(0x2b+2off)&FF +
  b5=0x87+(off>=107)+(off>=235) (C literals
  43/135/107/235 verified == 0x2b/0x87/107/235)).
  VPOS partitions re-derived from code: PBA 8
  (b4 + M7 b20,21,22,80-83; b5 range-const in lencode) /
  C10 6 (b4 + M5 b20,84,85,86,87; b5 const via lencode range) /
  quad 11 (b4,b5 + QM8 8 + R1 1) / T 18
  (b4,b5 + TM8 8 + TR8 8)
  -- all match q1126/A-961 census geometry.
  Code-consts vs census excl (PBA 79 / C10 81 /
  quad 77 / T88 70): impl 79/81/77/70 =
  exact all four, NO writer lag: committed tables match
  the census excl values exactly; geometry exact, PORT stands;
  memo PRESENT-CONFIRM this tier (39th even band running,
  no-lag this tier).
  QUAD 1SIG 9a DIFFERS-sig-from-PBA-sig this tier;
  PBA sig 9b NEW-vs-P377 (b0 d8);
  C10 sig 49 SAME-as-own-PB1 + NEW-vs-P377C10;
  AC-QC both=74 sameval=35 (tables differ).
  No extra _T10P378 tables (12 symbols only: S0/S1/AM/AC/
  CM/CC/M/QR/QC/RM/RQ/RC; no pre-existing collision this tier).
  M-tails 16/16 ALL NEW vs P377RM col-led tails
  (zero overlap first-hand) AND 16/16 ALL NEW vs P377RQ
  row-led tails (zero overlap first-hand).
  AM/CM/M/RM/RQ/QR 0-overlap vs P377 (widths P378 vs
  P377: AM 7B vs 9B, CM 5B vs 5B, M 8B vs 8B, RM 8B vs 6B,
  RQ 8B vs 8B, QR 1B vs 1B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=148281 (PB0 sig df017f24 NEW-sig 33/84,
  payB 84, embed b4/b5 73/86 == raw),
  S1 n=148282 (fat PB1 sig 49000000 NEW-sig,
  46/88 diff vs P377S1, 23/88 diff vs C10[0]
  n148299, SAME-as-own-C10, payB 88, embed b4/b5 75/86),
  A 148283-298 PBA88-PLAIN-M7b20 (sig 9b040000 via AC
  b0-b3, b0 const 9b, mtab b20,21,22,80-83,
  lencode b4=(0x77+2off)&FF b5 range-const 86 NO edge),
  C 148299-308 C10-1SIG-88-M5b20 (49000000 x10
  SAME-as-PB1-sig via CC b0-3 + CM tab, CM 10/10
  b20,84,85,86,87, b5 const 86 NO step raw lencode),
  Q 148309-372 QUAD88-1SIG-QM8/R1-B5EDGE (QM8
  b28,29,30,31,80-83 M 16/16 8ch NO-frags + R1
  b84 rows 2b/4b/6b/8b (4/4 UNPAIRED, BY-ROW const) +
  tails R1+31bd4d above, b5 STEPS 86->87 edge
  148351->148352 raw lencode tier-designed),
  R 148373-148628 T88-ring STANDARD (sig ab4f0000 x256
  b0 const ab, code-TM8 b19,27,34,35,80-83 by COL RM 16/16,
  code-TR8 b28,29,30,31,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b84-87 const ab31bd4d ring-wide,
  b4=(0x2b+2off)&FF + b5=0x87+(off>=107)+(off>=235) (C literals
  43/135/107/235 verified == 0x2b/0x87/107/235)),
  temps _t7501-7516 (base max _t7500, no reuse) +
  _i4557/4559/4562/4565 (base max _i4555, no reuse) +
  _b4556/4558/4560/4561/4563/4564 (base max _b4554,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P377R close
  (C "T10P3780 singleton" after "CLOSED T10P377R"; py
  return 0 + S0 guard 99527), at dispatch tail
  (N-out-of-scope fallthrough follows; plateau guards
  at C T34753 / py NOTE-w2s7-11 are the T4 plateau,
  unrelated scope).
  Matches census geometry (PB0 NEW-sig 33/84;
  PB1 NEW-sig 46/88 SAME-as-own-C10 23/88; PBA88-PLAIN-M7b20
  VPOS 8 sig-9b b5-const M7 16/16 distinct; C10-1SIG-88-M5b20
  VPOS 6 SAME-as-PB1-sig b5-const M5 10/10 +
  NEW-vs-P377C10; QUAD88-1SIG-QM8/R1-B5EDGE VPOS 11 +
  R1 4/4 UNPAIRED 2b/4b/6b/8b + suffix-lcs-3/3/3/3/3/3 +
  R1-distinct + NO frags + M-tails NEW;
  T88-STANDARD-TM8/TR8 VPOS 18 + TM8-by-COL/TR8-by-ROW +
  SPLIT-tails + b84-87 ab31bd4d + 1-sig-const-b0 +
  counter 2b/87/107/235; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R1 rows +
  tails + LCS + B5EDGE-quad + consts stand;
  M==RQ 16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 77/86
  tail 95/86; 0 ff in 16 (PLAIN tier, b5 range-const);
  C head 97/86 tail a9/86; 0 ff in 10 (b5 const tier);
  Q pre-edge off42 (ff/86), edge off43 (01/87);
  exactly 1 ff in 64; Q head ab/86 tail 29/87;
  ring pre-edge off106 (ff/87), edge off107 (01/88);
  pre-edge off234 (ff/88) -> edge off235 (01/89);
  exactly 2 ff in 256; R head 2b/87 tail 29/89; formulas
  re-derived from T10P378R code text (2b/87/107/235) +
  T10P378A/C/Q text (raw lencode + b5 step/const);
  all edge pins + mid pins + tail 148628 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (73/86 +
  75/86) match raw lencode. Ring b5==raw-lencode
  256/256 + b4==raw 256/256 (tier-designed) +
  Q b5-formula 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges486.py EDGES-GREEN 47 PASS 0 FAIL,
  first run green -- PLAIN PBA + M5-C10 + B5EDGE-quad +
  STANDARD ring verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB485base.nums subset forB486.nums,
  removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons `^    if n == ` 778->780 (+2) /
  ranges `^    if N <= n <= ` 942->946 (+4; C singletons
  783->785 +2 / ranges 964->968 +4, same 6 P378 blocks both
  sides; py file-wide elif 50 both (0 added), C else-if 0 both;
  deltas agree every side),
  CLOSED T10P prints 2156->2162 +6 both sides, seal
  2250->2256 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence: memo A-sheet PRESENT for P378
  (A-961-q1126-P378 CONFIRM 51/51 CLEAN: Q1 geometry
  1x(100,84)+347x(104,88) EXACT + PB1 49000000 + PBA
  9b/M7/b5-86 + C10 49/M20,84-87/b5-86 + QUAD 1-sig-9a
  DIFFERS-PBA + T 1-sig-ab4f0000 STD; Q2 QM/R1 tails +
  suffix-lcs 3/3/3/3/3/3 + M-tails NEW + TM-by-COL/TR-by-ROW +
  ab31bd4d; Q3 lencode 348/348 + consts 79/81/77/70 +
  0 stragglers NO D dips -- memo present).
  Substitute first-hand (standing rule): writer census Q-1126
  (consts PBA 79 / C10 81 / quad 77 / T88 70; committed tables
  match excl exactly 79/81/77/70 -- no writer lag this tier,
  geometry exact, PORT verdict stands) + cport commit msg ev
  (PYID 11235, RGRAM 22470) + py-merge commit msg
  (RGRAM 22470) + own full battery above.
  Agrees with cport commit msg (PYID 11235, RGRAM 22470)
  and py-merge commit msg (RGRAM 22470).
- FWD-check first-hand: b487 T10P379 bank 67bdb25e ancestor-verified
  on lanes/encode-writer2b (T10P379 pins 148629..148976 per bank
  commit msg; b487 C port status TBD at takeover, odd sweep turf,
  base-use only for NEXT round). P378 head details verified exact
  against lane code during this gate (PB0 @148281 sig df017f24 pay84
  NEW-sig 33/84 + PB1 49000000 pay88 @148282 NEW-sig 46/88 +
  PBA88 sig 9b040000 x16 @148283-298 + C10-region 49000000
  x10 @148299-308 SAME-PB1 -- all exact).
- Quiz: no conflicting CLAIM/GATE/FLAG on b486 (adjacent
  odds b485 = ac53e2c4 C port + b487 C port TBD, base-use
  only, no verdict on odds).
  Activity polled (no b486 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above: S0 df017f24 / S1 49000000 / PBA 9b040000 /
  C10 49000000 / QUAD 9a040000 / T ab4f0000 /
  R1 2b/4b/6b/8b / tails 31bd4d / b84-87 ab31bd4d /
  counter 2b/87/107/235 / embeds 73/86 + 75/86).
- Logs: NVME ws tmp/encode-sweep2/r84/ (buildB486.sha info,
  pyidB486.log, rgramB486py/c.log, cmp sets (passB486py/c.names,
  passB486pyo/co.txt), for-B485base/B486.nums, forB486.added/.removed,
  smokeB486.log, unitsB486.log, tablesB486.log, tabaudit486.py,
  edges486.py, edgesB486.log, bandB486.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
