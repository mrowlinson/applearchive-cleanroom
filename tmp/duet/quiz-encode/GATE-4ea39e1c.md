# GATE 4ea39e1c b392 T10P284 pins 115569..115916 (1692 tiers) PASS-functional

Seat sweep2-r61, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r61/w392 @4ea39e1c.
Band = dc9bff5b (py merge w2b@c6a35346 partial, +6 tiers, +62 pins)
+ 4ea39e1c (C port). Base 2d5cbe97 (b391 tip, 1686 tiers sealed).
Trees diff-identical to tips at archive time (verified via git
ls-tree vs find); w392 +__pycache__ battery byproduct after runs,
w391base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build392/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 06b3de14 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r61
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8375/8375 covered=8375/8375 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 16750/16750 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 16750/16750 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 16750/16750).
- PINS-RGRAM cells set-eq 16750/16750 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8375/8375 xor 0;
  PINS 16752 rows (2 hdr + 16750 = PASS lines, +62 vs base
  16690). For-list union 8344->8375 +31 (115569 115570
  115571 115572 115582 115583 115584 115586 115587 115588
  115591 115592 115595 115596 115597 115604 115612 115613
  115621 115629 115637 115645 115652 115660 115661 115711
  115712 115789 115839 115840 115916),
  0 removed, range 115569..115916 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 16750-16688.
  The 31 = S0/S1 (2) + A head/mids/step-edge/tail (6) +
  C head/mids/tail (6) + Q head/mids/tail (10) +
  ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P284 C-vs-py, script-compared, TABAUDIT-GREEN
  91 PASS 0 FAIL (tabaudit284.py rc=0): S0/S1 168ch
  EXACT sigs 99f00700 NEW / 4513630f NEW (full-string NEW
  vs BOTH P283S0/S1, diffs S0 31/84 + 36/84, S1 73/84 +
  54/84),
  AM 16/16 9B distinct, CM 10/10 11B distinct, M 16/16
  7B distinct, QR 4/4 10B distinct, RM 16/16 8B
  distinct, RQ 16/16 7B distinct UNPAIRED, no QT
  (tails live in R10) + no RT (STANDARD SPLIT),
  M==RQ 16/16 identical INTRA-tier,
  AC 73, CC 71, QC 69, RC 71; C _N decls 73/71/69/71
  match actual; byte-coverage unions exact every block
  (84/84/88/88, 0 overlap, mtab/r-tab computed).
  PBA16-STEP sig 5d3431f6 (b0 const 5d; AC
  has no b5, b5 step o>=13 varpos) + NEW vs P283PBA
  c09b7fe2 (cross-tier, P283AC code-verified).
  C10-1SIG c432f015 x10 (full sig b0-3 in CC
  consts, CM 10/10 diverge; CC has no b5, b5
  const 87 via lencode) + NEW vs P283 C10-2SIG
  6+4 (staged partial-sig vs full-sig geometry
  change code-verified).
  QUAD88-4R single-sig 01000000 x64 (QC b0-3;
  QC has no b5, b5 const 87 via lencode) + NEW vs
  P283 QUAD (88B-pay 1-sig R10 vs 84B-pay SPLIT
  geometry, QR 0-overlap code-verified; staged:
  AC-QC shared-pos 62, same-val 7, NOT const-repeat).
  R10 rows r0 1b36beda5c674aa60eca distinct vs
  r123 share-6B 534c7bdbb26d; tails b84-87
  4/4 distinct 4aa60eca/e4e03671/e7843771/0c853771,
  r123 share 1B 71, r2r3 share 2B 3771 (r1
  last-2B 3671 differs);
  byte-LCS (0,*)=0, (1,2)=1, (1,3)=1, (2,3)=2
  (own code-table LCS, memo/py-comment value
  re-derived exact).
  Ring STANDARD (STANDARD, not ROWTAIL): TM8 b8,9,
  10,19,80-83 by COL RM 16/16 8B, TR7 b13,14,
  15,76-79 by ROW RQ 16/16 UNPAIRED, tails SPLIT
  b80-83 col / b76-79 row;
  RC b0-3 14000000 NEW (P283 sig 07000000),
  b84-87 309f7eaa ring-wide NEW (P283
  a8fd2c45, both per P283RC code-verified).
  Code-consts vs A-705 INCL (PBA 73 / C10 72 /
  quad88 70 / T88 71): impl 73/71/69/71 = memo
  identical on PBA/T88, memo-1 on C10/quad
  (b5-const excluded; standing bookkeeping).
  M-tails 16/16 ALL NEW vs P283 (zero overlap vs
  P283 M AND P283RM-tail8 AND P283RQ-tail8; P283
  M/RM/RQ rows re-read first-hand). AM/CM/M/QR/
  RM/RQ 0-overlap vs P283 (widths differ M 14ch
  vs 12ch, RM 16ch vs 12ch; RQ same width 14ch
  but 0-overlap).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=115569 (PB0 sig 99f00700 NEW, lenB 84), S1
  n=115570 (fat PB1 sig 4513630f NEW, lenB 84),
  A 115571-586 PBA16-STEP (sig 5d3431f6 via AC
  b0-b3, b0 const 5d, AM 16/16 distinct 9B, mtab
  b6-10,76-79, raw lencode b5 0x86+(o>=13)),
  C 115587-596 C10-1SIG (c432f015 x10 via CC
  b0-3, CM 10/10 distinct 11B diverge 10/10,
  mtab b6-8,48-51,80-83, b5 const 87 raw lencode),
  Q 115597-660 QUAD88-4R single-sig 01000000 x64
  (QM7 b13-15,80-83 M 16/16 7B shared x3 + R10
  b6,7,52-55,84-87 rows above (r0 distinct,
  r123 share 6B) + tails above, NO frags, raw
  lencode b5 const 87),
  R 115661-115916 T88-STANDARD (sig 14000000, TM8
  b8,9,10,19,80-83 by COL RM 16/16 8B, TR7
  b13,14,15,76-79 by ROW RQ 16/16 UNPAIRED, tails
  SPLIT, b84-87 const 309f7eaa ring-wide,
  b4=(0x9b+2off)&FF, b5=0x87+(off>=51)+(off>=179)).
  C blocks carry T77361/77366/77371/77386/77402/
  77423 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 9B,
  C 11B, Q 7/10B, R 8/7B), counter b4=(0x9b+2off)
  &FF + (off>=51)+(off>=179), temps _t5964-5979
  (base max _t5963, no reuse) + _b3613/3615/3617/
  3618/3620/3621 (base max _b3611, no reuse) +
  _i3614/3616/3619/3622 (base max _i3612, no reuse),
  all 6 verified.
  Insert position exact both sides: after T10P283R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-705/A-348 geometry (PB0/PB1 NEW, PBA16
  STEP VPOS 11 b5 step o12->13 + edge 115583->115584,
  C10-1SIG VPOS 12 b5 const 87 10/10 diverge,
  QUAD88-4R VPOS 18 + R10 4/4 UNPAIRED + tails
  r0-lcs0/r123-share-1B/r2r3-share-2B + b5 const 87 +
  M-tails NEW, T88-STANDARD VPOS 17 + TR7 16/16
  UNPAIRED + b84-87 309f7eaa + counter 9b/87/51/179,
  lencode 348/348 whole-tier, A edge 115583->115584 +
  ring edges 115711->115712 + 115839->115840, NO D
  dips) incl exact values (PBA/C10 sigs, R10 rows +
  tails + LCS, ring TM8/TR7 + consts stand).
- Edges via counter formula first-hand: A head e7/86
  tail 05/87 b5set {86,87} step o12->13: 115583
  (o12, ff/86) -> 115584 (o13, 01/87) A-mid-row,
  exactly 1 ff in 16 (o12);
  C head 07/87 tail 19/87 b5set {87} NO step, 0 ff;
  Q head 1b/87 tail 99/87 b5set {87} 64/64, 0 ff;
  ring 115711 (off50, ff/87) -> 115712 (off51, 01/88);
  115839 (off178, ff/88) -> 115840 (off179, 01/89);
  exactly 2 ff in 256 (o50/o178); R head 9b/87 tail
  99/89; formula re-derived from T10P284R code text
  (9b/87/51/179); all edge pins + tail 115916 in
  for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (e3/86, e5/86) match raw lencode.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 600 add / 0 del
  (rgramc.c) + 230/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 595 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 415).
- Wall on band diff added lines (scope 2d5cbe97..
  4ea39e1c, 893 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 600/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 590->592 +2 (stated plain-method 600->602;
  10 inline non-guard `if n ==`) / ranges 588->592 +4
  = +6, C singletons 595->597 +2 / ranges 588->592 +4
  (C absolute +5 = pre-existing nested py guards
  11609/12909/13257/13605/14045, verified 8-space),
  CLOSED T10P prints 1592->1598 +6 both sides,
  seal 1686->1692 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-705-q796-
  t10p284 verdict CONFIRM (Q1 shape 14/14 + Q2 quad/ring
  12/12 + Q3 counters 12/12 = 38/38 as-filed; file
  present, counts verified; exact-value corroboration
  incl PBA-STEP + b5 step + edge, C10-1SIG, QUAD88-4R
  + R10 rows + tails + LCS + M-tails NEW, ring
  STANDARD + TR7 16/16 UNPAIRED + edges + consts, own
  P283C10-head n115239 reconstruction 49/84 vs P284S1
  NEW) + A-348 viewer corroboration (all legs
  CONFIRM, consts 73/72/70/71). No CONFIRM-P284.md
  file; A-705 suffices per rule. Agrees with cport
  commit msg (PYID 8375, RGRAM 16750).
- Quiz: no conflicting CLAIM/GATE/FLAG on b392 (adjacent
  odds b391 base-used, b393 beyond-cap acknowledged).
  Newest activity read (VERIFY-e3caa64f b386, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r61/ (build392.log,
  pyid392.log, rgram392py/c.log, cmp392.py/.c,
  for392-w392/-w391base.nums, smoke392.log, tables392.log,
  tabaudit284.py, edges284.py, edges392.log,
  numstat392.txt, add/delnorm392.txt, added392.txt,
  banddiff392.txt, pydiff284.txt, cdiff392.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
