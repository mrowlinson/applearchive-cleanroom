# GATE 648dd0de b482 T10P374 pins 146889..147236 (2232 tiers) PASS-functional

Seat sweep2-r83, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r83/wB482 @648dd0de.
Band = 83dbd944 (py merge w2b@635e3941 partial, +6 tiers, +58 pins)
+ 648dd0de (C port). Base 940d5f26 (b481 tip, 2226 tiers sealed,
odd-seat turf, used as diff-base only).
Band number from lane commit msg first-hand
(C port: "band482 T10P374 (pins 146889..147236, 2232 tiers sealed)";
py merge: "rgram T10P374 (pins 146889..147236, +6 tiers, +58 pins)").
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB482/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced2...
  (aae d6e27c97 = b288-b354 pinned + r52-r83 builds; r83 buildB482.sha
  d6e27c97ced21673...; band touches no aae sources per numstat:
  rgramc.c + rgram.py + test_rgram.sh + PINS only).
- RGRAMC-PYID 11119/11119 covered=11119/11119 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 22238/22238 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 22238/22238 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 22238/22238).
- PINS-RGRAM cells set-eq 22238/22238 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 11119/11119 xor 0;
  PINS 22240 rows (2 hdr + 22238 = PASS lines, +58 vs base
  22182).
  For-list union 11090->11119 +29 (146889 146890
  146891 146892 146898 146899 146905 146906 146907 146908
  146911 146912 146915 146916 146917 146932 146943 146944
  146949 146964 146980 146981 147071 147072 147136 147199
  147200 147201 147236),
  0 removed, range 146889..147236 exact. Each for-N yields
  2 PASS lines (g-zN + g-zN-closed). 29x2 = 58 = 22238-22180.
  The 29 = S0/S1 (2) + A head-pair/mid-pair/tail-pair (6:
  head pair 146891/146892 off0/1, mid pair 146898/146899
  off7/8, tail pair 146905/146906 off14/15; b5 const 7b
  range-emergent NO step, PLAIN tier) +
  C head/mid/tail pairs (6: 146907/146908 off0/1,
  mid pair 146911/146912 off4/5, tail pair 146915/146916
  off8/9; b5 const 7b NO step) +
  Q head/mid/edge-pair/mid/mid/tail (7: head 146917 off0,
  mid 146932 off15, edge pair 146943/146944 off26/27 (B5EDGE
  7b->7c), mid 146949 off32, mid 146964 off47,
  tail 146980 off63) +
  R head/edge-pair/mid/edge-triple/tail
  (8: head 146981 off0, edge pair 147071/147072 off90/91,
  mid 147136 off155,
  edge triple 147199/147200/147201 off218/219/220
  (pre-edge+edge+post-edge),
  tail 147236 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg 83dbd944; C-port leg 648dd0de touched zero
  PINS rows + zero for-line); all 22238 rows
  test_rgram_fast.py-tagged; added 58 names == for-added
  closed+open pairs (29x2),
  sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P374 C-vs-py, script-compared, TABAUDIT-GREEN
  133 PASS 0 FAIL (tabaudit482.py rc=0, fresh first-hand;
  coverage checks run pre-exit, no dead code;
  1 pre-run script fix: RC-missing dropped b0 (b0 const ef
  lives in RC, caught pre-run; tree untouched) +
  1 post-run script fix: QC-missing dropped b0 (b0 const 5e
  lives in QC, first run caught it; tree untouched)):
  S0 168ch sig 6e586913 NEW-sig (33/84 payload diff vs
  P373S0 first-hand, NOT byte-equal) /
  S1 176ch sig 26000000 sig-REPEAT (same sig as P373PB1;
  48/88 payload diff vs P373S1 first-hand, NOT byte-equal;
  45/88 diff vs own-C10[0] assembled n146907 first-hand,
  NOT byte-equal; sig DIFFERS-from-own-C10 26-vs-20),
  staged as full-payload singletons,
  AM 16/16 7ch distinct, CM 10/10 6ch distinct,
  M 16/16 7ch distinct, QR 4/4 4ch distinct, RM 16/16
  9ch distinct, RQ 16/16 7ch distinct, no QT (quad
  tails = R2 + consts b86/b87) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; Q uses M b52,53,54,80-83 by COL m=off&15 vs R
  uses RQ b52,53,54,76-79 by ROW r=off>>4 first-hand;
  string-identical HOLDS this tier -- reported, not gated),
  AC 79, CC 83, QC 77, RC 70; C _N decls
  79/83/77/70 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b30 sig 5e020000 (b0 const 5e, b5 const
  7b range-emergent via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M7 b30,39,47,80-83; lencode b4=(0x97+2off)
  &FF raw) + vs P373PBA sig 62 (novelty = NEW-sig 5e,
  AM 0-overlap).
  C10-1SIG-88-TAIL-M3 sig 20000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 3ch b84,85,86; CC HAS b87 const b8 (differs from
  P372 CC which had b86+b87 consts); b5 CONST 7b range-emergent via
  raw lencode NO step; M3 3B lane: CM 6ch rows).
  QUAD88-1SIG-QM7/R2-B5EDGE 1-sig 5e020000
  SAME-sig-as-PBA (b0 const 5e in QC; b5 STEPS 7b->7c
  edge 146943->146944 via raw lencode tier-designed;
  QM7 b52,53,54,80-83 M 16/16 7ch NO frags, m = off&15
  first-hand; b84,85 R2 lane rows + b86 const b2 +
  b87 const b8 quad-wide) +
  r2 b84,85 R2 4/4 UNPAIRED BY-ROW (q = off>>4 first-hand;
  rows ec37/0c38/2c38/4c38 4-char exact);
  tails = R2 + b2b8 8ch quad-wide,
  full-tail suffix-lcs 2/2/2/3/3/3 + R2 all-distinct).
  Ring T88-STANDARD-TM9/TR7 1-sig ef250000 x256
  (b0 const ef in RC, STANDARD frame -- differs from P372
  ring whose b0 lives in the TR lane;
  code-TM9 b6,7,8,9,10,80-83 by COL RM 16/16 (RM rows
  9ch FIRST this lane) + code-TR7 b52,53,54,76-79 by ROW
  RQ 16/16 UNPAIRED (SPLIT tails b80-83 col / b76-79 row);
  b84-87 const 6c38b2b8 ring-wide; b4=(0x4b+2off)&FF +
  b5=0x7c+(off>=91)+(off>=219) (C literals
  75/124/91/219 verified == 0x4b/0x7c/91/219)).
  VPOS partitions re-derived from code: PBA 8
  (b4 + M7 b30,39,47,80-83; b5 range-const in lencode) / C10 4
  (b4 + M3 b84,85,86; b5 const via lencode range) /
  quad 11 (b4,b5 + QM7 7 + R2 2) / T 18
  (b4,b5 + TM9 9 + TR7 7)
  -- all match q1122/A-957 census geometry.
  Code-consts vs census excl (PBA 79 / C10 83 /
  quad 77 / T88 70): impl 79/83/77/70 =
  exact all four, NO writer lag: committed tables match
  the census excl values exactly; geometry exact, PORT stands;
  memo PRESENT-CONFIRM this tier (37th even band running,
  no-lag this tier).
  QUAD 1SIG 5e SAME-sig-as-PBA-sig this tier;
  PBA sig 5e NEW-vs-P373 (62->5e);
  AC-QC both=74 sameval=54 (tables differ).
  No extra _T10P374 tables (12 symbols only: S0/S1/AM/AC/
  CM/CC/M/QR/QC/RM/RQ/RC; no pre-existing collision this tier).
  M-tails 16/16 ALL NEW vs P373RM col-led tails
  (zero overlap first-hand) AND 16/16 ALL NEW vs P373RQ
  row-led tails (zero overlap first-hand; P373T is STANDARD-split
  with col-led tails per Q-1122, both refs novel).
  AM/CM/M/RM/RQ/QR 0-overlap vs P373 (widths P374 vs
  P373: AM 7B vs 8B, CM 3B vs 4B, M 7B vs 7B, RM 9B vs 7B,
  RQ 7B vs 6B, QR 2B vs 2B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=146889 (PB0 sig 6e586913 NEW-sig 33/84,
  payB 84, embed b4/b5 93/7b == raw),
  S1 n=146890 (fat PB1 sig 26000000 sig-REPEAT,
  48/88 diff vs P373S1, 45/88 diff vs C10[0]
  n146907, DIFFERS-own-C10, payB 88, embed b4/b5 95/7b),
  A 146891-906 PBA88-PLAIN-M7b30 (sig 5e020000 via AC
  b0-b3, b0 const 5e, mtab b30,39,47,80-83,
  lencode b4=(0x97+2off)&FF b5 range-const 7b NO edge),
  C 146907-916 C10-1SIG-88-TAIL-M3 (20000000 x10
  DIFFERS-from-PB1-sig via CC b0-3 + CM tab, CM 10/10
  b84,85,86, b5 const 7b NO step raw lencode),
  Q 146917-980 QUAD88-1SIG-QM7/R2-B5EDGE (QM7
  b52,53,54,80-83 M 16/16 7ch NO-frags + R2
  b84,85 rows ec37/0c38/2c38/4c38 (4/4 UNPAIRED, BY-ROW const) +
  tails R2+b2b8 above, b5 STEPS 7b->7c edge
  146943->146944 raw lencode tier-designed),
  R 146981-147236 T88-ring STANDARD (sig ef250000 x256
  b0 const ef, code-TM9 b6,7,8,9,10,80-83 by COL RM 16/16 FIRST,
  code-TR7 b52,53,54,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b84-87 const 6c38b2b8 ring-wide,
  b4=(0x4b+2off)&FF + b5=0x7c+(off>=91)+(off>=219) (C literals
  75/124/91/219 verified == 0x4b/0x7c/91/219)),
  temps _t7437-7452 (base max _t7436, no reuse) +
  _i4517/4519/4522/4525 (base max _i4515, no reuse) +
  _b4516/4518/4520/4521/4523/4524 (base max _b4514,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P373R close
  (C "T10P3740 singleton" after "CLOSED T10P373R"; py
  return 0 + S0 guard 98603), at dispatch tail
  (N-out-of-scope fallthrough follows; plateau guards
  at C T34753 / py NOTE-w2s7-11 are the T4 plateau,
  unrelated scope).
  Matches census geometry (PB0 NEW-sig 33/84;
  PB1 sig-REPEAT 48/88 DIFFERS-own-C10 45/88; PBA88-PLAIN-M7b30
  VPOS 8 sig-5e b5-const M7 16/16 distinct; C10-1SIG-88-TAIL-M3
  VPOS 4 DIFFERS-from-PB1-sig b5-const M3 10/10;
  QUAD88-1SIG-QM7/R2-B5EDGE VPOS 11 + R2 4/4 UNPAIRED
  ec37/0c38/2c38/4c38 + suffix-lcs-2/2/2/3/3/3 +
  R2-distinct + NO frags + M-tails NEW;
  T88-STANDARD-TM9/TR7 VPOS 18 + TM9-by-COL/TR7-by-ROW +
  SPLIT-tails + b84-87 6c38b2b8 + 1-sig-const-b0 +
  counter 4b/7c/91/219; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + LCS + B5EDGE frame + consts stand;
  M==RQ 16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 97/7b
  tail b5/7b; 0 ff in 16 (PLAIN tier, b5 range-const);
  C head b7/7b tail c9/7b; 0 ff in 10 (b5 const tier);
  Q pre-edge off26 (ff/7b), edge off27 (01/7c);
  exactly 1 ff in 64; Q head cb/7b tail 49/7c;
  ring pre-edge off90 (ff/7c), edge off91 (01/7d);
  pre-edge off218 (ff/7d) -> edge off219 (01/7e);
  exactly 2 ff in 256; R head 4b/7c tail 49/7e; formulas
  re-derived from T10P374R code text (4b/7c/91/219) +
  T10P374A/C/Q text (raw lencode + b5 step/const);
  all edge pins + mid pins + tail 147236 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (93/7b +
  95/7b) match raw lencode. Ring b5==raw-lencode
  256/256 (b4 independent, tier-designed) +
  Q b5-formula 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges482.py EDGES-GREEN 45 PASS 0 FAIL,
  first run -- PLAIN PBA + M3-C10 + B5EDGE-quad + STANDARD
  ring verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB481base.nums subset forB482.nums,
  removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons `^    if n == ` 770->772 (+2) /
  ranges `^    if N <= n <= ` 926->930 (+4; C singletons
  775->777 +2 / ranges 948->952 +4, same 6 P374 blocks both
  sides; py file-wide elif 50 both (0 added), C else-if 0 both;
  deltas agree every side),
  CLOSED T10P prints 2132->2138 +6 both sides, seal
  2226->2232 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence: memo A-sheet PRESENT for P374
  (A-957-q1122-P374 CONFIRM 50/50 CLEAN: Q1 geometry
  1x(100,84)+347x(104,88) EXACT + PB1 sig-repeat + PBA
  5e/M7/b5-7b + C10 20/M84-86/b5-7b + QUAD 1-sig-5e
  SAME-PBA + T 1-sig-ef250000 STANDARD; Q2 QM/R2 tails +
  suffix-lcs 2/2/2/3/3/3 + M-tails NEW + TM-by-COL/TR-by-ROW +
  6c38b2b8; Q3 lencode 348/348 + consts 79/83/77/70 +
  0 stragglers NO D dips -- memo present both tiers this round).
  Substitute first-hand (standing rule): writer census Q-1122
  (consts PBA 79 / C10 83 / quad 77 / T88 70; committed tables
  match excl exactly 79/83/77/70 -- no writer lag this tier,
  geometry exact, PORT verdict stands) + cport commit msg ev
  (PYID 11119, RGRAM 22238) + py-merge commit msg
  (RGRAM 22238) + own full battery above.
  Agrees with cport commit msg (PYID 11119, RGRAM 22238)
  and py-merge commit msg (RGRAM 22238).
- FWD-check first-hand: b483 T10P375 bank 40ce87a2 ancestor-verified
  on lanes/encode-writer2b (T10P375 pins 147237..147584 per bank
  commit msg; b483 C port 246d3408 live odd sweep turf, base-use
  only for NEXT round). P374 head details verified exact against
  lane code during this gate (PB0 @146889 sig 6e586913 pay84
  NEW-sig 33/84 + PB1 26000000 pay88 @146890 sig-REPEAT 48/88 +
  PBA88 sig 5e020000 x16 @146891-906 + C10-region 20000000
  x10 @146907-916 DIFFERS-PB1 -- all exact).
- Quiz: no conflicting CLAIM/GATE/FLAG on b482 (adjacent
  odds b481 = 940d5f26 C port + b483 = 246d3408 C port, base-use
  only, no verdict on odds).
  Activity polled (no b482 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above: S0 6e586913 / S1 26000000 / PBA 5e020000 /
  C10 20000000 / QUAD 5e020000 / T ef250000 /
  R2 ec37/0c38/2c38/4c38 / tails b2b8 / b84-87 6c38b2b8 /
  counter 4b/7c/91/219 / embeds 93/7b + 95/7b).
- Logs: NVME ws tmp/encode-sweep2/r83/ (buildB482.sha info,
  pyidB482.log, rgramB482py/c.log, cmp sets (passB482py/c.names,
  passB482pyo/co.txt), for-B481base/B482.nums, forB482.added/.removed,
  smokeB482.log, unitsB482.log, tablesB482.log, tabaudit482.py,
  edges482.py, edgesB482.log, bandB482.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
