# GATE 3c2b2e00 b400 T10P292 pins 118353..118700 (1740 tiers) PASS-functional

Seat sweep2-r63, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r63/w400 @3c2b2e00.
Band = 2dbda75a (py merge w2b@439c8c3a partial, +6 tiers, +62 pins)
+ 3c2b2e00 (C port). Base d5de4afe (b399 tip, 1734 tiers sealed).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical); w400 +__pycache__
battery byproduct after runs, w399base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build400/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ded22093 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r63
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8624/8624 covered=8624/8624 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 17248/17248 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 17248/17248 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 17248/17248).
- PINS-RGRAM cells set-eq 17248/17248 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8624/8624 xor 0;
  PINS 17250 rows (2 hdr + 17248 = PASS lines, +62 vs base
  17188). For-list union 8593->8624 +31 (118353 118354
  118355 118356 118362 118363 118369 118370 118371 118372
  118377 118378 118379 118380 118381 118396 118397 118399
  118400 118413 118421 118429 118437 118444 118445 118527
  118528 118573 118655 118656 118700),
  0 removed, range 118353..118700 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 17248-17186.
  The 31 = S0/S1 (2) + A head/mids/tail (6) +
  C head/mids/tail (6) + Q head/mids/edge-pair/mids/tail (10) +
  ring head/edge-pairs/mid/tail (7). PINS-new-N == for-added
  31/31 (4th set-eq way), PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P292 C-vs-py, script-compared, TABAUDIT-GREEN
  96 PASS 0 FAIL (tabaudit292.py rc=0): S0/S1 168ch
  EXACT sigs 436f1300 NEW / 2b81e720 NEW (S diffs vs P291:
  S0 34/84 + 35/84, S1 73/84 + 56/84; P291 sigs
  5f6f1300 / 2b81c726),
  AM 16/16 6B distinct, CM 10/10 17B distinct, M 16/16
  7B distinct, QR 4/4 10B distinct, RM 16/16 8B
  distinct, RQ 16/16 7B distinct UNPAIRED, no QT
  (tails live in R10) + no RT (STANDARD SPLIT),
  M==RQ 16/16 identical INTRA-tier,
  AC 80, CC 65, QC 69, RC 71; C _N decls 80/65/69/71
  match actual; byte-coverage unions exact every block
  (88/84/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN sig 02000000 (b0 const 02; AC
  has no b5, b5 const 9c via lencode) + REPEAT vs
  P291PBA 02000000 (88B-pay PBA sig persists P291->P292;
  novelty = AM rows 0-overlap + M6 geometry
  b6,7,80-83 vs P291 M8 b40-43,80-83).
  C10-2SIG ORDERED 7+3 (08075220 x7 @118371-77 +
  84032910 x3 @118378-80, map order code-verified
  from CM rows; full sig b0-3 in tab, b9-skipped
  const 00; CM 10/10 diverge; CC has no b5,
  b5 const 9c via lencode).
  QUAD88-4R single-sig 01000000 x64 (QC b0-3;
  QC has no b5, b5 stepped 0x9c+(o>=19) full-block
  lencode, edge o18->19) +
  rows NEW vs P291 QUAD (R10 width 20ch vs P291
  24ch FRAG, 0-overlap code-verified; staged: AC-QC
  shared-pos 69, same-val 27, NOT const-repeat;
  11 AConly + 0 QConly).
  R10 rows r0 c36f025c86d5 distinct vs
  r123 share-6B 8b87eb584b65, differ at byte 6
  (9a/bf/e4); tails b84-87 4/4 distinct
  04c20dca/9a03613a/bf03613a/e403613a, r123 TRUE
  3B 03613a;
  byte-LCS (0,*)=0, (1,2)=(1,3)=(2,3)=3
  (own code-table LCS, memo/py-comment value
  re-derived exact).
  Ring STANDARD-split: TM8 b8,9,10,19,80-83 by COL
  RM 16/16 8B (M carries b80-83 col), TR7
  b13,14,15,76-79 by ROW RQ 16/16 UNPAIRED (R carries
  b76-79 row); RC b0-3 11000000 NEW (P291 sig
  23000000), b84-87 bea6f6d3 ring-wide NEW (P291
  1537fc9a, per P291RC code-verified).
  Code-consts vs A-733 INCL (PBA88 81 / C10 66 /
  quad88 69 / T88 71): impl 80/65/69/71 = memo-1
  on PBA/C10 (b5-const excluded), identical
  on quad/T88 (standing bookkeeping).
  M-tails 16/16 ALL NEW vs P291 (zero overlap vs
  P291 M AND P291RM-tail8 AND P291RQ-tail8; P291
  M/RM/RQ rows re-read first-hand). AM/CM/M/QR/
  RM/RQ 0-overlap vs P291 (widths differ M 14ch
  vs 8ch, AM 12ch vs 16ch, CM 34ch vs 32ch,
  QR 20ch vs 24ch, RQ 14ch vs 16ch; RM 16ch
  vs 18ch).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=118353 (PB0 sig 436f1300 NEW, lenB 84), S1
  n=118354 (fat PB1 sig 2b81e720 NEW, lenB 84),
  A 118355-370 PBA88-PLAIN (sig 02000000 via AC
  b0-b3, b0 const 02, AM 16/16 distinct 6B, mtab
  b6,7,80-83, b5 const 9c raw lencode),
  C 118371-380 C10-2SIG 7+3 (sigs above via CM
  b0-3 + b9-skipped const 00, CM 10/10 distinct 17B
  diverge 10/10, mtab b0-3,6-8,10,11,48-51,80-83, b5
  const 9c raw lencode),
  Q 118381-444 QUAD88-4R single-sig 01000000 x64
  (QM7 b13-15,80-83 M 16/16 7B shared x3 + R10
  b6,7,52-55,84-87 rows above (r0 distinct,
  r123 share 6B) + tails above, NO frags, raw
  lencode b5 0x9c+(o>=19) step o18->19),
  R 118445-700 T88-STANDARD (sig 11000000, TM8
  b8,9,10,19,80-83 by COL RM 16/16 8B, TR7
  b13,14,15,76-79 by ROW RQ 16/16 UNPAIRED,
  b84-87 const bea6f6d3 ring-wide,
  b4=(0x5b+2off)&FF, b5=0x9d+(off>=83)+(off>=211)).
  C blocks carry T79244/79249/79254/79269/79286/
  79307 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 6B,
  C 17B, Q 7/10B, R 8/7B), Q raw-lencode equiv counter
  b4=(0xdb+2off)&FF + b5=0x9c+(o>=19) verified 64/64,
  R counter b4=(0x5b+2off)&FF + (off>=83)+(off>=211)
  (C literals 91/157 verified == 0x5b/0x9d),
  temps _t6095-6110 (base max _t6094, no reuse) +
  _b3694/3696/3698/3699/3701/3702 (base max _b3692,
  no reuse) + _i3695/3697/3700/3703 (base max _i3693,
  no reuse), all 6 verified.
  Insert position exact both sides: after T10P291R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-733/A-356 geometry (PB0/PB1 NEW,
  PBA88 PLAIN VPOS 7 b5 const 9c 16/16 distinct NO pair,
  C10-2SIG VPOS 18 b5 const 9c 10/10 diverge 7+3,
  QUAD88-4R VPOS 19 + R10 4/4 UNPAIRED + r123 share-6B +
  r123-TRUE-3B + r0-lcs0 + b5 step + M-tails NEW,
  T88-STANDARD VPOS 17 + TR7 16/16 UNPAIRED +
  b84-87 bea6f6d3 + counter 5b/9d/83/211,
  lencode 348/348 whole-tier, Q edge
  118399->118400 + ring edges
  118527->118528 + 118655->118656, NO D
  dips) incl exact values (PBA/C10 sigs + map, R10
  rows + tails + LCS, ring TM8/TR7 + consts stand).
- Edges via counter formula first-hand: A head a7/9c
  tail c5/9c b5set {9c} NO step, 0 ff;
  C head c7/9c tail d9/9c b5set {9c} NO step, 0 ff;
  Q head db/9c tail 59/9d edge o18->19 (118399->118400)
  ff/9c->01/9d, exactly 1 ff in 64 (o18);
  ring 118527 (off82, ff/9d) -> 118528 (off83, 01/9e);
  118655 (off210, ff/9e) -> 118656 (off211, 01/9f);
  exactly 2 ff in 256 (o82/o210); R head 5b/9d tail
  59/9f (Q tail 59/9d vs R tail 59/9f differ in b5 --
  labeled apart); formula re-derived from T10P292R
  code text (5b/9d/83/211); all edge pins + tail
  118700 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (a3/9c, a5/9c) match raw lencode.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 604 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 599 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 418).
- Wall on band diff added lines (scope d5de4afe..
  3c2b2e00, 898 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 604/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 606->608 +2 /
  ranges 598->602 +4 = +6, C identical 606->608 +2 /
  598->602 +4 (nested 5 singleton + 22 range guards
  identical both sides; +5 py-only inline ternaries =
  standing bookkeeping, deltas agree every side),
  CLOSED T10P prints 1640->1646 +6 both sides,
  seal 1734->1740 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-733-q884-
  t10p292 verdict CONFIRM (Q1 shape 14/14 + Q2 quad/ring
  11/11 + Q3 counters 12/12 = 35/35 as-filed + TBD settled;
  file present, counts verified; exact-value corroboration
  incl PB0/PB1 NEW, PBA88-PLAIN, C10-2SIG 7+3 map,
  QUAD88-4R + R10 rows + 6B-share + r123-TRUE-3B +
  r0-lcs0 + b5 step + M-tails NEW, ring STANDARD +
  TR7 16/16 UNPAIRED + edges + consts, own P291C10-head
  n118023 reconstruction 50/84 vs S1 (sig 2b81c726,
  matches no P292 sig -- S1 2b81e720 NEW standalone))
  + A-356 corroboration (all legs CONFIRM, no geometry
  correction). No CONFIRM-P292.md file; A-733 suffices
  per rule. Agrees with cport commit msg (PYID 8624,
  RGRAM 17248).
- Quiz: no conflicting CLAIM/GATE/FLAG on b400 (adjacent
  odds b399 base-used, b401 sweep-GATED acknowledged).
  Activity polled (no b400 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r63/ (build400.log,
  pyid400.log, rgram400py/c.log, cmp400.py/.c,
  for400-w400/-w399base.nums, smoke400.log, tables400.log,
  tabaudit292.py, edges292.py, edges400.log,
  numstat400.txt, add/delnorm400.txt, added400.txt,
  banddiff400.txt, pydiff292.txt, cdiff400.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
