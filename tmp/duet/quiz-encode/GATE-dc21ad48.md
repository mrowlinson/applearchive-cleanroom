# GATE dc21ad48 b492 T10P384 pins 150369..150716 (348) PASS-functional

Seat sweep2-r87g, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r87g/wB492 @dc21ad48 + wB491base @38e3a831.
Band = 70a5ce2c (py merge w2b@d8b9c892 partial, +6 tiers, +58 pins)
+ dc21ad48 (C port). Base 38e3a831 (b491 tip, 2286 tiers sealed,
odd-seat turf, used as diff-base only).
Band number from lane commit msg first-hand
(C port: "band492 T10P384 (pins 150369..150716, 2292 tiers sealed)";
py merge: "rgram T10P384 (pins 150369..150716, +6 tiers, +58 pins)").
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB492/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced21673
  (aae d6e27c97 = r52-r86 pinned + r87g buildB492.sha
  d6e27c97ced21673...; band touches no aae sources per numstat:
  rgramc.c + rgram.py + test_rgram.sh + PINS only).
- RGRAMC-PYID 11409/11409 covered=11409/11409 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, ct-cache).
- RGRAM py 22818/22818 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 22818/22818 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw identical, 22818/22818; 11409 unique).
- PINS-RGRAM cells set-eq 22818/22818 (PASS-N vs PINS-N);
  PINS N set vs for-list 11409/11409 xor 0;
  PINS 22820 lines (2 hdr + 22818 = PASS lines, +58 vs base
  22762).
  For-list union 11380->11409 +29 (150369 150370
  150371 150372 150378 150379 150385 150386 150387 150388
  150391 150392 150395 150396 150397 150399 150400 150412
  150413 150444 150460 150461 150527 150528 150591 150655
  150656 150657 150716),
  0 removed, added range 150369..150716 exact. Each for-N yields
  2 PASS lines (g-zN + g-zN-closed). 29x2 = 58 = 22818-22760.
  The 29 = S0/S1 (2: 150369 off0, 150370 off1) +
  A head-pair + mid-pair + tail-pair (6:
  head pair 150371/150372 off0/1, mid pair 150378/150379
  off7/8, tail pair 150385/150386 off14/15; A b5 const 96
  NO step this tier) +
  C head/mid/tail pairs (6: 150387/150388 off0/1,
  mid pair 150391/150392 off4/5, tail pair 150395/150396
  off8/9; b5 const 96 NO step) +
  Q head + edge-pair + mids + tail (7: head 150397 off0,
  edge pair 150399/150400 off2/3 (pre-edge + B5EDGE 96->97),
  mid pair 150412/150413 off15/16, mid 150444 off47,
  tail 150460 off63) +
  R head/edge-pair/mid/edge-triple/tail
  (8: head 150461 off0, edge pair 150527/150528 off66/67
  (pre-edge+edge),
  mid 150591 off130,
  edge triple 150655/150656/150657 off194/195/196
  (pre-edge+edge+post-edge),
  tail 150716 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0, PINS changed 0. PINS numstat 58/0 clean append
  (all in py-merge leg 70a5ce2c; C-port leg dc21ad48 touched zero
  PINS rows + zero for-line); all 22818 rows
  test_rgram_fast.py-tagged, added 58 names == for-added
  closed+open pairs (29x2),
  sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P384 C-vs-py, script-compared, TABAUDIT-GREEN
  138 PASS 0 FAIL (tabaudit492.py rc=0, fresh first-hand):
  S0 168ch sig 5f522926 sig-REPEAT (32/84 payload diff vs
  P383PB0 first-hand per memo, NOT byte-equal) /
  S1 176ch sig 4c000000 sig-REPEAT (67/88 payload diff vs P383PB1
  first-hand per memo, NOT byte-equal; 45/88 diff vs
  own-C10[0] assembled n150387 first-hand, NOT byte-equal;
  sig DIFFERS-from-own-C10 4c-vs-4f),
  staged as full-payload singletons,
  AM 16/16 7ch distinct, CM 10/10 2ch distinct,
  M 16/16 6ch distinct, QR 4/4 4ch distinct, RM 16/16
  7ch distinct, RQ 16/16 6ch distinct, no QT (quad
  tails = R2, no consts) + no RT (SWAPPED tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list first-hand; Q uses M b40,41,80-83 by COL m=off&15 vs R
  uses RQ b40,41,80-83 by ROW r=off>>4 first-hand;
  string-identical HOLDS this tier -- reported, not gated),
  AC 79, CC 84, QC 78, RC 73, NO tier-head C (absent P384
  py+C first-hand; 12 symbols only: S0/S1/AM/AC/
  CM/CC/M/QR/QC/RM/RQ/RC); C _N decls
  79/84/78/73 match actual; byte-coverage unions exact
  every block (m-tab/r-tab computed, 0 overlap).
  PBA88-PLAIN-M7b29 sig ff040000 (b0 const ff, b5 CONST 96
  NO step NO edge; AM 16/16 distinct NO pair; M7
  b29,34,35,80-83; lencode b4=(0xc7+2off)&FF raw) + vs
  P383PBA (novelty = NEW-sig ff, AM 0-overlap).
  C10-1SIG-88-TAIL-M2 sig 4f000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 2ch b84,85; b5 CONST 96 range-emergent via
  raw lencode NO step; M2 TAIL lane).
  QUAD88-1SIG-QM6/R2-B5EDGE 1-sig 6b040000
  DIFFERS-from-PBA-sig (b0 const 6b in QC; b5 0x96+(off>=3)
  via raw lencode + edge 150399->150400 tier-designed;
  QM6 b40,41,80-83 M 16/16 6ch NO frags, m = off&15
  first-hand; b84,85 R2 lane rows (NO consts --
  quad tails ARE the R2 rows) +
  r2 b84,85 R2 4/4 UNPAIRED BY-ROW (q = off>>4 first-hand;
  rows d308/f308/1309/3309 4ch exact);
  full-tail suffix-lcs 3/2/2/2/2/3 + R2 all-distinct +
  NO frags + M-tails NEW.
  Ring T88-SWAPPED-split 1-sig 6b460000 x256
  (b0 const 6b in RC, SWAPPED-split frame;
  code-TM7 b39,46,47,76-79 by COL RM 16/16 + code-TR6
  b40,41,80-83 by ROW RQ 16/16 UNPAIRED
  (SWAPPED tails b80-83 col / b76-79 row; positions staged
  P360R/P376R);
  b84-87 const 5309759b ring-wide;
  b4=(0x7b+2off)&FF +
  b5=0x97+(off>=67)+(off>=195) (C literals
  123/151/67/195 verified == 0x7b/0x97/67/195)).
  Code-consts vs census excl (PBA 79 / C10 84 /
  quad 78 / T88 73): impl 79/84/78/73 =
  exact all four, NO writer lag: committed tables match
  the census excl values exactly; geometry exact, PORT stands;
  memo PRESENT-CONFIRM this tier (42nd even band running,
  no-lag this tier).
  QUAD 1SIG 6b DIFFERS-sig-from-PBA-sig this tier;
  PBA sig ff NEW-vs-P383;
  C10 sig 4f DIFFERS-as-own-PB1;
  AC-QC both=75 sameval=38 (tables differ).
  M-tails 16/16 ALL NEW vs P383RM col-led tails
  (zero overlap first-hand) AND 16/16 ALL NEW vs P383RQ
  row-led tails (zero overlap first-hand).
  AM/CM/M/RM/RQ 0-overlap vs P383 (widths P384 vs
  P383: AM 7B vs 9B, CM 2B vs 2B, M 6B vs 7B, RM 7B vs 8B,
  RQ 6B vs 7B, QR 2B vs 1B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=150369 (PB0 sig 5f522926 sig-REPEAT 32/84,
  payB 84, embed b4/b5 c3/96 == raw),
  S1 n=150370 (fat PB1 sig 4c000000 sig-REPEAT,
  67/88 diff vs P383PB1, 45/88 diff vs C10[0]
  n150387, DIFFERS-from-own-C10, payB 88, embed b4/b5 c5/96),
  A 150371-386 PBA88-PLAIN-M7b29 (sig ff040000 via AC
  b0-b3, b0 const ff, mtab b29,34,35,80-83,
  lencode b4=(0xc7+2off)&FF b5 const 96 raw,
  NO step NO edge),
  C 150387-396 C10-1SIG-88-TAIL-M2 (4f000000 x10
  DIFFERS-from-PB1-sig via CC b0-3 + CM tab, CM 10/10
  b84,85, b5 const 96 NO step raw lencode),
  Q 150397-460 QUAD88-1SIG-QM6/R2-B5EDGE (QM6
  b40,41,80-83 M 16/16 6ch NO-frags + R2
  b84,85 rows d308/f308/1309/3309
  (4/4 UNPAIRED, BY-ROW const, rows ARE tails) +
  tails R2 above, b5 0x96+(off>=3) edge 150399->150400
  raw lencode),
  R 150461-716 T88-ring SWAPPED-split (sig 6b460000 x256
  b0 const 6b, code-TM7 b39,46,47,76-79 by COL RM 16/16,
  code-TR6 b40,41,80-83 by ROW RQ 16/16 UNPAIRED,
  SWAPPED tails, b84-87 const 5309759b ring-wide,
  b4=(0x7b+2off)&FF + b5=0x97+(off>=67)+(off>=195) (C literals
  123/151/67/195 verified == 0x7b/0x97/67/195)),
  temps _t7597-7612 (base max _t7596, no reuse) +
  _i4617/4619/4622/4625 (base max _i4615, no reuse) +
  _b4616/4618/4620/4621/4623/4624 (base max _b4615,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P383R close
  (C "T10P3840 singleton" after "CLOSED T10P383R" 268038;
  py return 0 + S0 guard 100916), at dispatch tail
  (N-out-of-scope fallthrough follows).
  Matches census geometry (PB0 sig-REPEAT 32/84;
  PB1 sig-REPEAT 67/88 DIFFERS-as-own-C10 45/88; PBA88-PLAIN-M7b29
  sig-ff b5-const M7 16/16 distinct; C10-1SIG-88-TAIL-M2
  DIFFERS-as-PB1-sig b5-const M2 10/10;
  QUAD88-1SIG-QM6/R2-B5EDGE + R2 4/4 UNPAIRED d308/f308/1309/3309 +
  suffix-lcs-3/2/2/2/2/3 + R2-distinct + NO frags + M-tails NEW;
  T88-SWAPPED TM7-by-COL/TR6-by-ROW +
  SWAPPED-tails + b84-87 5309759b + 1-sig-const-b0 +
  counter 7b/97/67/195; lencode 348/348 whole-tier,
  NO D dips).
- Edges via counter formula first-hand: A head c7/96
  tail e5/96; 0 ff in 16 (b5 const tier);
  C head e7/96 tail f9/96; 0 ff in 10 (b5 const tier);
  Q head fb/96 tail 79/97; 1 ff in 64 at off2 (pre-edge ff/96,
  edge off3 01/97 B5EDGE 96->97);
  ring pre-edge off66 (ff/97), edge off67 (01/98);
  pre-edge off194 (ff/98) -> edge off195 (01/99);
  exactly 2 ff in 256; R head 7b/97 tail 79/99; formulas
  re-derived from T10P384R code text (7b/97/67/195) +
  T10P384A/C/Q text (raw lencode + b5 step/const);
  all edge pins + mid pins + tail 150716 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (c3/96 +
  c5/96) match raw lencode. Ring b5==raw-lencode
  256/256 (tier-designed) +
  A b5-const 16/16 + C b5-const 10/10 + Q b5-formula 64/64.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges492.py EDGES-GREEN 47 PASS 0 FAIL,
  const-PBA + const-C10 + B5EDGE-quad +
  SWAPPED-split ring verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB491base.nums subset forB492.nums,
  removed 0; C-scope del 0).
  Leg attribution first-hand: C-port leg dc21ad48 =
  rgramc.c 608/0 only; py-merge leg 70a5ce2c = rgram.py
  231/0 + test_rgram.sh 1/1 + PINS 58/0 only.
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons `^    if n == ` 790->792 (+2) /
  ranges `^    if N <= n <= ` 966->970 (+4; py file-wide
  elif 50 both (0 added), C else-if 0 both;
  deltas agree every side),
  CLOSED T10P prints 2192->2198 +6 both sides, seal
  2286->2292 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence: memo A-sheet PRESENT for P384
  (A-967-q1132-P384 CONFIRM 50/50 CLEAN: Q1 geometry
  1x(100,84)+347x(104,88) EXACT + PB0 5f522926 pay84 +
  PB1 4c000000 + PBA ff/M7/b5-const + C10 4f/M84-85/b5-const +
  QUAD 1-sig-6b DIFFERS-PBA + T 1-sig-6b460000 SWP; Q2 QM/R
  tails + suffix-lcs 3/2/2/2/2/3 + M-tails NEW + TM-by-COL/
  TR-by-ROW + 5309759b; Q3 lencode 348/348 + consts 79/84/78/73 +
  0 stragglers NO D dips -- memo present).
  Substitute first-hand (standing rule): writer census Q-1132
  (consts PBA 79 / C10 84 / quad 78 / T88 73; committed tables
  match excl exactly 79/84/78/73 -- no writer lag this tier,
  geometry exact, PORT verdict stands) + cport commit msg ev
  (PYID 11409, RGRAM 22818) + py-merge commit msg
  (RGRAM 22818) + own full battery above.
  Agrees with cport commit msg (PYID 11409, RGRAM 22818)
  and py-merge commit msg (RGRAM 22818).
- FWD-check first-hand: b493 T10P385 bank 612fdc42 ancestor-verified
  on lanes/encode-writer2b (T10P385 pins 150717..151064 per bank
  commit msg; b493 C port 3158f991 committed, odd sweep turf,
  base-use only for NEXT round). P384 head details verified exact
  against lane code during this gate + P385 head exact per memo
  Next line (PB0 @150717 sig 5f943026 pay84 NEW-sig 31/84 +
  PB1 46000000 pay88 @150718 + PBA88 sig 6b040000 x16 @150719-734 +
  C10-region 46000000 x10 @150735-744 SAME-as-PB1 -- all exact).
- Quiz: no conflicting CLAIM/GATE/FLAG on b492 (adjacent
  odds b491 = 38e3a831 C port + b493 = 3158f991 C port, base-use
  only, no verdict on odds).
  Activity polled (no b492 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above: S0 5f522926 / S1 4c000000 / PBA ff040000 /
  C10 4f000000 / QUAD 6b040000 / T 6b460000 /
  R2 d308/f308/1309/3309 / b84-87 5309759b /
  counter 7b/97/67/195 / embeds c3/96 + c5/96).
- Logs: NVME ws tmp/encode-sweep2/r87g/ (buildB492.sha info,
  pyidB492.log, rgramB492py/c.log, cmp sets (passB492py/c.names,
  passB492pyo/co.txt), for-B491base/B492.nums, forB492.added/.removed,
  smokeB492.log, unitsB492.log, tablesB492.log, tabaudit492.py,
  edges492.py, edgesB492.log, band addedlines via git diff).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
