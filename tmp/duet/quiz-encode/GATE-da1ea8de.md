# GATE da1ea8de b480 T10P372 pins 146193..146540 (2220 tiers) PASS-functional

Seat sweep2-r83, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r83/wB480 @da1ea8de.
Band = 7779190f (py merge w2b@f6cdd371 partial, +6 tiers, +58 pins)
+ da1ea8de (C port). Base 6a7ad611 (b479 tip, 2214 tiers sealed,
odd-seat turf, used as diff-base only).
Band number from lane commit msg first-hand
(C port: "band480 T10P372 (pins 146193..146540, 2220 tiers sealed)";
py merge: "rgram T10P372 (pins 146193..146540, +6 tiers, +58 pins)").
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB480/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced2...
  (aae d6e27c97 = b288-b354 pinned + r52-r83 builds; r83 buildB480.sha
  d6e27c97ced21673...; band touches no aae sources per numstat:
  rgramc.c + rgram.py + test_rgram.sh + PINS only).
- RGRAMC-PYID 11061/11061 covered=11061/11061 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 22122/22122 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 22122/22122 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 22122/22122).
- PINS-RGRAM cells set-eq 22122/22122 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 11061/11061 xor 0;
  PINS 22124 rows (2 hdr + 22122 = PASS lines, +58 vs base
  22066).
  For-list union 11032->11061 +29 (146193 146194
  146195 146196 146202 146203 146209 146210 146211 146212
  146215 146216 146219 146220 146221 146227 146228 146244
  146260 146276 146284 146285 146303 146304 146396 146397
  146431 146432 146540),
  0 removed, range 146193..146540 exact. Each for-N yields
  2 PASS lines (g-zN + g-zN-closed). 29x2 = 58 = 22122-22064.
  The 29 = S0/S1 (2) + A head-pair/mid-pair/tail-pair (6:
  head pair 146195/146196 off0/1, mid pair 146202/146203
  off7/8, tail pair 146209/146210 off14/15; b5 const 76
  range-emergent NO step, PLAIN tier) +
  C head/mid/tail pairs (6: 146211/146212 off0/1,
  mid pair 146215/146216 off4/5, tail pair 146219/146220
  off8/9; b5 const 76 NO step) +
  Q head/colsplit-pair/mid/mid/mid/tail (7: head 146221 off0,
  colsplit pair 146227/146228 off6/7 (b0 31-iff-col<7 frame
  boundary), mid 146244 off23, mid 146260 off39,
  mid 146276 off55, tail 146284 off63; b5 const 76 NO edge) +
  R head/edge-pair/mid-pair/edge-pair/tail
  (8: head 146285 off0, edge pair 146303/146304 off18/19,
  mid pair 146396/146397 off111/112,
  edge pair 146431/146432 off146/147,
  tail 146540 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg 7779190f; C-port leg da1ea8de touched zero
  PINS rows + zero for-line); all 22122 rows
  test_rgram_fast.py-tagged; added 58 names == for-added
  closed+open pairs (29x2),
  sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P372 C-vs-py, script-compared, TABAUDIT-GREEN
  137 PASS 0 FAIL (tabaudit480.py rc=0, fresh first-hand;
  coverage checks run pre-exit, no dead code;
  0 pre-run script fixes; 1 post-run script fix: 2 Q-edge
  expectations corrected (hand-arithmetic slips, b4 base 0x5b
  not 0xbb; tree untouched)):
  S0 168ch sig ef17160d NEW-sig (33/84 payload diff vs
  P371S0 first-hand, NOT byte-equal) /
  S1 176ch sig 1f000000 NEW-sig (44/88 payload diff vs
  P371S1 first-hand, NOT byte-equal;
  57/88 diff vs own-C10[0] assembled n146211 first-hand,
  NOT byte-equal; sig DIFFERS-from-own-C10 1f-vs-26),
  staged as full-payload singletons,
  AM 16/16 7ch distinct, CM 10/10 4ch distinct,
  M 16/16 7ch distinct, QR 4/4 4ch distinct, RM 16/16
  8ch distinct, RQ 16/16 7ch distinct, no QT (quad
  tails = R2 + consts b86/b87) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; Q uses M b0,10,11,80-83 by COL m=off&15 vs R
  uses RQ b0,10,11,76-79 by ROW r=off>>4 first-hand;
  string-identical HOLDS this tier -- reported, not gated),
  AC 79, CC 84, QC 77, RC 71; C _N decls
  79/84/77/71 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b6 sig ff010000 (b0 const ff, b5 const
  76 range-emergent via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M7 b6,7,9,80-83; lencode b4=(0x27+2off)
  &FF raw) + vs P371PBA sig c9 (novelty = NEW-sig ff,
  AM 0-overlap).
  C10-1SIG-88-TAIL-M2 sig 26000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 2ch b84,85; CC HAS b20 const (differs from P370
  CC which had no b20); b5 CONST 76 range-emergent via raw
  lencode NO step; M2 2B lane: CM 4ch rows).
  QUAD88-2SIG-QM7/R2-COLSPLIT 2-sig 31020000/46020000
  DIFFERS-from-PBA (b0=31 iff col<7: 28+36; QM7 b0,10,11,80-83
  M 16/16 7ch NO frags, m = off&15 first-hand;
  b84,85 R2 lane rows + b86 const 90 + b87 const 79 quad-wide) +
  r2 b84,85 R2 4/4 UNPAIRED BY-ROW (q = off>>4 first-hand;
  rows d82f/457b/657b/857b 4-char exact);
  tails = R2 + 9079 8ch quad-wide,
  full-tail suffix-lcs 2/2/2/3/3/3 + R2 all-distinct).
  Ring T88-2SIG-TM8/TR7-ROWSPLIT
  (sigs 31260000 x112 (rows0-6) + 46260000 x144 (rows7-15);
  b0 row-led rows0-6 iff 31;
  code-TM8 b16,17,18,19,80-83 by COL RM 16/16 (RM rows
  8ch FIRST this lane) + code-TR7 b0,10,11,76-79 by ROW
  RQ 16/16 UNPAIRED (SPLIT tails b80-83 col / b76-79 row);
  b84-87 const a57b9079 ring-wide; b4=(0xdb+2off)&FF +
  b5=0x76+(off>=19)+(off>=147) (C literals
  219/118/19/147 verified == 0xdb/0x76/19/147)).
  VPOS partitions re-derived from code: PBA 8
  (b4 + M7 b6,7,9,80-83; b5 range-const in lencode) / C10 4
  (b4,b5 + M2 b84,85; b5 const via lencode range) /
  quad 10 (b4 + QM7 7 + R2 2) / T 17
  (b4,b5 + TM8 8 + TR7 7)
  -- all match q1120/A-955 census geometry.
  Code-consts vs census excl (PBA 79 / C10 84 /
  quad 77 / T88 71): impl 79/84/77/71 =
  exact all four, NO writer lag: committed tables match
  the census excl values exactly; geometry exact, PORT stands;
  memo PRESENT-CONFIRM this tier (36th even band running,
  no-lag this tier).
  QUAD 2SIG 31/46 DIFFERS-from-PBA-sig this tier;
  PBA sig ff NEW-vs-P371 (c9->ff);
  AC-QC both=74 sameval=6 (tables differ).
  No extra _T10P372 tables (12 symbols only: S0/S1/AM/AC/
  CM/CC/M/QR/QC/RM/RQ/RC; no pre-existing collision this tier).
  M-tails 16/16 ALL NEW vs P371RM col-led tails
  (zero overlap first-hand) AND 16/16 ALL NEW vs P371RQ
  row-led tails (zero overlap first-hand; P371T is STANDARD-split
  with col-led tails per Q-1120, both refs novel).
  AM/CM/M/RM/RQ/QR 0-overlap vs P371 (widths P372 vs
  P371: AM 7B vs 6B, CM 2B vs 2B, M 7B vs 6B, RM 8B vs 9B,
  RQ 7B vs 8B, QR 2B vs 5B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=146193 (PB0 sig ef17160d NEW-sig 33/84,
  payB 84, embed b4/b5 23/76 == raw),
  S1 n=146194 (fat PB1 sig 1f000000 NEW-sig,
  44/88 diff vs P371S1, 57/88 diff vs C10[0]
  n146211, DIFFERS-own-C10, payB 88, embed b4/b5 25/76),
  A 146195-210 PBA88-PLAIN-M7b6 (sig ff010000 via AC
  b0-b3, b0 const ff, mtab b6,7,9,80-83,
  lencode b4=(0x27+2off)&FF b5 range-const 76 NO edge),
  C 146211-220 C10-1SIG-88-TAIL-M2 (26000000 x10
  DIFFERS-from-PB1-sig via CC b0-3 + CM tab, CM 10/10
  b84,85, b5 const 76 NO step raw lencode),
  Q 146221-284 QUAD88-2SIG-QM7/R2-COLSPLIT (QM7
  b0,10,11,80-83 M 16/16 7ch NO-frags + R2
  b84,85 rows d82f/457b/657b/857b (4/4 UNPAIRED, BY-ROW const) +
  tails R2+9079 above, b5 CONST 76 NO edge raw lencode),
  R 146285-540 T88-ring 2SIG-ROWSPLIT (sig 31260000 x112
  row-led b0=31 rows0-6 + sig 46260000 x144,
  code-TM8 b16,17,18,19,80-83 by COL RM 16/16 FIRST,
  code-TR7 b0,10,11,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b84-87 const a57b9079 ring-wide,
  b4=(0xdb+2off)&FF + b5=0x76+(off>=19)+(off>=147) (C literals
  219/118/19/147 verified == 0xdb/0x76/19/147)),
  temps _t7405-7420 (base max _t7404, no reuse) +
  _i4497/4499/4502/4505 (base max _i4495, no reuse) +
  _b4496/4498/4500/4501/4503/4504 (base max _b4494,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P371R close
  (C "T10P3720 singleton" after "CLOSED T10P371R"; py
  return 0 + S0 guard 98139), at dispatch tail
  (N-out-of-scope fallthrough follows; plateau guards
  at C T34753 / py NOTE-w2s7-11 are the T4 plateau,
  unrelated scope).
  Matches census geometry (PB0 NEW-sig 33/84;
  PB1 NEW-sig 44/88 DIFFERS-own-C10 57/88; PBA88-PLAIN-M7b6
  VPOS 8 sig-ff b5-const M7 16/16 distinct; C10-1SIG-88-TAIL-M2
  VPOS 4 DIFFERS-from-PB1-sig b5-const M2 10/10;
  QUAD88-2SIG-QM7/R2-COLSPLIT VPOS 10 + R2 4/4 UNPAIRED
  d82f/457b/657b/857b + suffix-lcs-2/2/2/3/3/3 +
  R2-distinct + NO frags + M-tails NEW;
  T88-2SIG-TM8/TR7-ROWSPLIT VPOS 17 + TM8-by-COL/TR7-by-ROW +
  SPLIT-tails + b84-87 a57b9079 + 112/144 split +
  counter db/76/19/147; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + LCS + COLSPLIT frame + consts stand;
  M==RQ 16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 27/76
  tail 45/76; 0 ff in 16 (PLAIN tier, b5 range-const);
  C head 47/76 tail 59/76; 0 ff in 10 (b5 const tier);
  Q 0 ff in 64 (b5 const 76 NO edge; head 5b/76
  tail d9/76);
  ring pre-edge off18 (ff/76), edge off19 (01/77);
  pre-edge off146 (ff/77) -> edge off147 (01/78);
  exactly 2 ff in 256; R head db/76 tail d9/78; formulas
  re-derived from T10P372R code text (db/76/19/147) +
  T10P372A/C/Q text (raw lencode + b5 const);
  all edge pins + mid pins + tail 146540 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (23/76 +
  25/76) match raw lencode. Ring b5==raw-lencode
  256/256 (b4 independent: db vs raw-1b, tier-designed) +
  Q b5-const 64/64 + A 16/16 + C 10/10.
  Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges480.py EDGES-GREEN 43 PASS 0 FAIL,
  second run after 1 post-run script fix -- 2 Q-edge
  expectations hand-corrected pre-reason (b4 base 0x5b);
  Q-const + M2-C10 + COLSPLIT-quad + ROWSPLIT
  ring verified first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB479base.nums subset forB480.nums,
  removed 0; C-scope del 0).
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons `^    if n == ` 766->768 (+2) /
  ranges `^    if N <= n <= ` 918->922 (+4; C singletons
  771->773 +2 / ranges 940->944 +4, same 6 P372 blocks both
  sides; py file-wide elif 50 both (0 added), C else-if 0 both;
  deltas agree every side),
  CLOSED T10P prints 2120->2126 +6 both sides, seal
  2214->2220 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence: memo A-sheet PRESENT for P372
  (A-955-q1120-P372 CONFIRM 50/50 CLEAN: Q1 geometry
  1x(100,84)+347x(104,88) EXACT + PBA ff/M7/b5-76 +
  C10 26/M84-85/b5-76 + QUAD 31/46 COLSPLIT 28+36 +
  T 31260000/46260000 ROWSPLIT 112+144; Q2 QM/R2 tails +
  suffix-lcs 2/2/2/3/3/3 + M-tails NEW + TM-by-COL/TR-by-ROW +
  a57b9079; Q3 lencode 348/348 + consts 79/84/77/71 +
  0 stragglers NO D dips -- breaks the r82 absent-streak,
  first memo-present tier this note series).
  Substitute first-hand (standing rule): writer census Q-1120
  (consts PBA 79 / C10 84 / quad 77 / T88 71; committed tables
  match excl exactly 79/84/77/71 -- no writer lag this tier,
  geometry exact, PORT verdict stands) + cport commit msg ev
  (PYID 11061, RGRAM 22122) + py-merge commit msg
  (RGRAM 22122) + own full battery above.
  Agrees with cport commit msg (PYID 11061, RGRAM 22122)
  and py-merge commit msg (RGRAM 22122).
- FWD-check first-hand: b481 T10P373 bank bbedd165 rev-parse
  verified on lanes/encode-writer2b (T10P373 pins 146541..146888
  per bank commit msg; NEXT for b482 base). P372 head details
  verified exact against lane code during this
  gate (PB0 @146193 sig ef17160d pay84 NEW-sig 33/84 +
  PB1 1f000000 pay88 @146194 NEW-sig 44/88 +
  PBA88 sig ff010000 x16 @146195-210 + C10-region 26000000
  x10 @146211-220 DIFFERS-PB1 -- all exact).
- Quiz: no conflicting CLAIM/GATE/FLAG on b480 (adjacent
  odds b479 = 6a7ad611 C port + b481 bank bbedd165, base-use only,
  no verdict on odds).
  Activity polled (no b480 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above: S0 ef17160d / S1 1f000000 / PBA ff010000 /
  C10 26000000 / QUAD 31020000+46020000 / T 31260000+46260000 /
  R2 d82f/457b/657b/857b / tails 9079 / b84-87 a57b9079 /
  counter db/76/19/147 / embeds 23/76 + 25/76).
- Logs: NVME ws tmp/encode-sweep2/r83/ (buildB480.sha info,
  pyidB480.log, rgramB480py/c.log, cmp sets (passB480py/c.names,
  passB480pyo/co.txt), for-B479base/B480.nums, forB480.added/.removed,
  smokeB480.log, unitsB480.log, tablesB480.log, tabaudit480.py,
  edges480.py, edgesB480.log, bandB480.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
