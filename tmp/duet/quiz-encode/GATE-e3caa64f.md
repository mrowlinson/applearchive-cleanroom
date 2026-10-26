# GATE e3caa64f b386 T10P278 pins 113481..113828 (1656 tiers) PASS-functional

Seat sweep2-r59 (recovery instance), first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r59/w386 @e3caa64f.
Band = ccdc6b7b (py merge w2b@ba53806f partial, +6 tiers, +64 pins)
+ e3caa64f (C port). Base a33e4c8f (b385 tip, 1650 tiers sealed).
Trees diff-identical to tips (w386 +__pycache__ battery byproduct only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build386/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 1875a2a6 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r59
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8185/8185 covered=8185/8185 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 16370/16370 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 16370/16370 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 16370/16370).
- PINS-RGRAM cells set-eq 16370/16370 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8185/8185 xor 0;
  PINS 16372 rows (2 hdr + 16370 = PASS lines, +64 vs base
  16308). For-list union 8153->8185 +32 (113481 113482
  113483 113484 113488 113493 113497 113498 113499 113500
  113502 113505 113507 113508 113509 113524 113525 113535
  113536 113540 113541 113556 113557 113572 113573 113663
  113664 113675 113691 113791 113792 113828),
  0 removed, range 113481..113828 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 32x2 = 64 = 16370-16306.
  The 32 = S0/S1 (2) + A head/mids/tail (6) + C head/mids/
  tail (6) + Q head/mids/step-pair/mids/tail (10) +
  ring head/edge-pairs/mids/tail (8).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P278 C-vs-py, script-compared, TABAUDIT-GREEN
  90 PASS 0 FAIL (tabaudit278.py rc=0): S0/S1 168ch
  EXACT sigs b0aa0700 NEW / f5f4570f (sig == P277C10,
  full-string NEW vs BOTH P277S0/S1),
  AM 16/16 8B distinct, CM 10/10 13B distinct, M 16/16
  6B distinct, QR 4/4 7B, QT 4/4 4B, RM 16/16 8B
  distinct, RQ 16/16 2B 15/16 (r6==r7 f1d5 PAIRED),
  RT 16/16 4B distinct (r6 != r7, tails disambiguate),
  AC 74, CC 69, QC 65, RC 72; C _N decls 74/69/65/72
  match actual; byte-coverage unions exact every block
  (84/84/84/88, 0 overlap, b4/b5 computed).
  PBA16-PLAIN sig e09a1ffa HELD (P277 e09a1ffa
  per P277AC code-verified), b0 const e0; AC
  has no b5 (b5-const memo-1).
  C10-1SIG f5f4570f x10 via CC b0-b3 == PB1 sig
  INTRA-tier repeat (staged: S1-vs-own-C10 diffs
  47x8/46x2, NOT byte-repeat) + HELD vs P277C10
  (cross-tier, P277C10 f5f4570f code-verified);
  CM 10/10 diverge; CC has no b5.
  QUAD1s single-sig e09a1ffa x64 == PBA sig
  INTRA-tier repeat (staged: AC-QC shared-pos 65,
  same-val 34, NOT const-repeat) + HELD vs P277QUAD
  (cross-tier, P277QUAD e09a1ffa code-verified);
  QC b47 const 96 (b47-skipped); QC has no b5
  (b5 step o>=27 computed).
  R7 LAST3-PAIRED r1==r2==r3 333104ef5407a6 x3,
  r0 a551220fd42f94 distinct; tails row-shared
  4/4 distinct 18e71aa7/1eef163c/8eae4f3c/b3ae4f3c,
  r2/r3 share TRUE 3B ae4f3c (r0/r1 do not);
  QM6 shared 16/16 x3 NO frags.
  Ring ROWTAIL (4th row-led T88): TM8 b6,7,12,13,
  76-79 by COL RM 16/16 8B, TR2 b52,53 by ROW
  RQ 15/16 (r6==r7 f1d5 PAIRED, RT tails
  disambiguate), TT4 b80-83 ROW-led by r;
  RC b0-3 0f000000 NEW (P277 sig 08000000),
  b84-87 7f5fc217 ring-wide NEW (P277 sig
  2783811e, both per P277RC code-verified).
  Code-consts vs A-683 INCL (PBA 75 / C10 70 /
  quad 65 / T88 72): impl 74/69/65/72 = memo-1
  on PBA/C10 (b5-const excluded), identical
  on quad/T88 (standing bookkeeping).
  M-tails 16/16 ALL NEW vs P277 (zero overlap vs
  BOTH P277RM-tail8 and P277RQ-tail8; P277 RM/RQ
  16x8B/16x3B rows re-read first-hand). AM/CM 0-overlap
  vs P277AM/CM (CM 26ch vs P277 24ch widths).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=113481 (PB0 sig b0aa0700 NEW, lenB 84), S1
  n=113482 (fat PB1 sig f5f4570f ==P277C10sig, lenB 84),
  A 113483-113498 PBA16-PLAIN (sig e09a1ffa HELD via
  AC b0-b3, b0 const e0, AM 16/16 distinct 8B, mtab
  b34,35,42,43,76-79, b5 const 76 raw lencode),
  C 113499-113508 C10-1SIG (f5f4570f x10 via CC
  b0-b3 == PB1 sig, CM 10/10 distinct 13B diverge 10/10,
  mtab b34,35,41-47,80-83, b5 const 76 raw lencode),
  Q 113509-113572 QUAD1s single-sig e09a1ffa x64
  (QM6 b48,49,76-79 M 16/16 6B shared x3 + R7
  b34,35,42-46 LAST3-PAIRED above + QT tails above,
  NO frags, raw lencode b5 step o>=27),
  R 113573-113828 T88-ROWTAIL (sig 0f000000, TM8
  b6,7,12,13,76-79 by COL RM 16/16 8B, TR2 b52,53
  by ROW RQ 15/16 PAIRED, TT4 b80-83 ROW-led by r,
  b84-87 const 7f5fc217 ring-wide,
  b4=(0x4b+2off)&FF, b5=0x77+(off>=91)+(off>=219)).
  C blocks carry T75913/75918/75923/75938/75954/75977
  py-line mirrors (each re-read: hits the exact py guard
  line), bounds + byte positions exact (A 8B, C 13B, Q
  6/7/4B, R 8/2/4B), counter b4=(0x4b+2off)&FF +
  (off>=91)+(off>=219), temps _t5850-5869 (base max
  _t5849, no reuse) + _b3546/3548/3550/3551/3552/3554/
  3555/3556 (base max _b3544, no reuse) + _i3547/3549/
  3553/3557 (base max _i3545, no reuse), all 6 verified.
  Insert position exact both sides: after T10P277R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-683/A-342 geometry (PB0 NEW, PB1 ==P277C10sig
  with 56/84 payload diff settled first-hand (own n113151
  reconstruction: 56 differ/28 agree), PBA16 PLAIN VPOS 9 b5
  const 76 16/16 distinct NO pair, C10-1SIG VPOS 14 b5
  const 76 10/10 diverge head-sig==PB1, QUAD1s VPOS 19
  + R7 LAST3-PAIRED + QT r23 TRUE-3B + b5 step o>=27 +
  M-tails NEW, T88-ROWTAIL VPOS 16 + TR2 15/16 r67-paired
  + b84-87 7f5fc217, lencode 348/348 whole-tier, Q edge
  113535->113536 + ring edges 113663->113664 +
  113791->113792, NO D dips) incl exact values (PBA/C10
  sigs, R7 values, QT tails, ring TM8/TR2/TT4 + consts
  stand).
- Edges via counter formula first-hand: A head 97/76
  tail b5/76 b5set {76} NO carry; C head b7/76 tail
  c9/76 b5set {76} NO carry; Q head cb/76 tail 49/77,
  formula b4=(0xcb+2off)&FF b5=0x76+(off>=27) 64/64,
  edge 113535 (o26, ff/76) -> 113536 (o27, 01/77)
  mid-row1;
  ring 113663 (off90, ff/77) -> 113664 (off91, 01/78);
  113791 (off218, ff/78) -> 113792 (off219, 01/79);
  exactly 2 ff in 256 (o90/o218); R head 4b/77 tail
  49/79; formula re-derived from T10P278R code text
  (4B/77/91/219); all edge pins + tail 113828 in
  for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (93/76, 95/76) match raw lencode.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 636 add / 0 del
  (rgramc.c) + 257/0 (rgram.py) + 1/1 (for-line) +
  64/0 (PINS); raw C grep 631 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 430).
- Wall on band diff added lines (scope a33e4c8f..
  e3caa64f, 958 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 636/0, rgram.py 257/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, dispatch-guards
  singletons 588->590 +2 / ranges 564->568 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep; C `(n) == (N)` / range form agrees absolute
  588->590/564->568), CLOSED T10P prints 1556->1562 +6,
  C CLOSED 1556->1562 +6 (deltas agree both
  sides), seal 1650->1656 +6
  (commit msgs): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-683-q790-
  t10p278 verdict CONFIRM (Q1 shape 13/13 + Q2 quad/ring
  14/14 + Q3 counters 12/12 = 39/39 as-filed; file
  present, counts verified; exact-value corroboration
  incl PBA/C10 sigs, PB1-vs-n113151 56/84 payload diff
  (memo value re-derived first-hand, exact),
  QUAD1s + R7 last3-pair + QT tails + b5 step, M-tails
  NEW, ring ROWTAIL + TR2 15/16 + edges
  + consts) + A-342 viewer corroboration (all 3 legs
  CONFIRM). No CONFIRM-P278.md file; A-683 suffices per
  rule. Agrees with cport commit msg (PYID 8185, RGRAM
  16370).
- Quiz: no conflicting CLAIM/GATE/FLAG on b386 (adjacent
  odds b385 base-used, b387 GATED-by-sweep turf acknowledged).
  Newest PARENT-* is QNUM-19 (w2d Q-block only, read, no
  gate impact); PROSE-01 re-read before filing (all hex/counts
  copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r59/ (build386.log,
  pyid386.log, rgram386py/c.log, cmp386.py/.c,
  for386-old/-new.nums, smoke386.log, tables386.log,
  tabaudit278.py, edges278r.py, edges386r.log,
  numstat386.txt, add/delnorm386.txt, added386.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
