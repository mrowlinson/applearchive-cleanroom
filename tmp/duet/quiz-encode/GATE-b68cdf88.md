# GATE b68cdf88 b396 T10P288 pins 116961..117308 (1716 tiers) PASS-functional

Seat sweep2-r62, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r62/w396 @b68cdf88.
Band = a36a36d3 (py merge w2b@31527a73 partial, +6 tiers, +62 pins)
+ b68cdf88 (C port). Base 62f9b99c (b395 tip, 1710 tiers sealed).
Trees diff-identical to tips at archive time (verified via git
ls-tree vs find); w396 +__pycache__ battery byproduct after runs,
w395base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build396/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4f4c483d / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r62
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8499/8499 covered=8499/8499 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 16998/16998 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 16998/16998 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 16998/16998).
- PINS-RGRAM cells set-eq 16998/16998 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8499/8499 xor 0;
  PINS 17000 rows (2 hdr + 16998 = PASS lines, +62 vs base
  16938). For-list union 8468->8499 +31 (116961 116962
  116963 116964 116970 116971 116977 116978 116979 116980
  116983 116984 116987 116988 116989 116991 116992 117004
  117005 117013 117021 117029 117037 117052 117053 117119
  117120 117181 117247 117248 117308),
  0 removed, range 116961..117308 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 16998-16936.
  The 31 = S0/S1 (2) + A head/mids/tail (6) +
  C head/mids/tail (6) + Q head/step-edge/mids/tail (10) +
  ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P288 C-vs-py, script-compared, TABAUDIT-GREEN
  96 PASS 0 FAIL (tabaudit288.py rc=0): S0/S1 168ch
  EXACT sigs 0ac51600 NEW / 3bf3942d (S diffs vs P287:
  S0 32/84 + 72/84, S1 67/84 + 75/84; P287 sigs
  85620b00 / 4c0ac516),
  AM 16/16 8B distinct, CM 10/10 12B distinct, M 16/16
  6B distinct, QR 4/4 12B distinct, RM 16/16 7B
  distinct, RQ 16/16 6B distinct UNPAIRED, no QT
  (tails live in R12) + no RT (STANDARD SPLIT),
  M==RQ 16/16 identical INTRA-tier,
  AC 78, CC 70, QC 68, RC 73; C _N decls 78/70/68/73
  match actual; byte-coverage unions exact every block
  (88/84/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN sig 02000000 (b0 const 02; AC
  has no b5, b5 const 91 via lencode) + NEW vs
  P287PBA 01000000 (sig changes P287->P288).
  C10-1SIG 3bf3942d x10 SAME-as-PB1-sig (full sig b0-3
  in CC consts, CM 10/10 diverge; CC has no b5, b5
  const 91 via lencode) + NEW vs P287 C10-1SIG
  86148a2d (different sig, M12 geometry b22,23,30-35,
  80-83 vs P287 M11 b13-19,80-83 code-verified).
  QUAD88-4R single-sig 02000000 x64 (QC b0-3;
  QC has no b5, b5 step o>=3 varpos) + rows NEW vs
  P287 QUAD (R12 width 24ch vs P287 R11 22ch,
  0-overlap code-verified; staged: AC-QC shared-pos 67,
  same-val 29, NOT const-repeat; QC positions cover
  AC positions except 11 AConly + 1 QConly).
  R12 rows r0 2b022ff935b1da25 distinct vs
  r123 share-8B abe8237f75320326, differ at byte 8
  (41/66/8b); tails b84-87 4/4 distinct
  e032bd5c/416e5b06/666e5b06/8b6e5b06, r123 TRUE
  3B 6e5b06;
  byte-LCS (0,*)=0, (1,2)=(1,3)=(2,3)=3
  (own code-table LCS, memo/py-comment value
  re-derived exact).
  Ring STANDARD-split: TM7 b39,46,47,80-83 by COL
  RM 16/16 7B (M carries b80-83 col), TR6
  b40,41,76-79 by ROW RQ 16/16 UNPAIRED (R carries
  b76-79 row); RC b0-3 2f000000 NEW (P287 sig
  2d000000), b84-87 de75775e ring-wide NEW (P287
  1a509e70, both per P287RC code-verified).
  Code-consts vs A-727 INCL (PBA88 79 / C10 71 /
  quad88 68 / T88 73): impl 78/70/68/73 = memo-1
  on PBA/C10 (b5-const excluded), identical
  on quad/T88 (standing bookkeeping).
  M-tails 16/16 ALL NEW vs P287 (zero overlap vs
  P287 M AND P287RM-tail8 AND P287RQ-tail8; P287
  M/RM/RQ rows re-read first-hand). AM/CM/M/QR/
  RM/RQ 0-overlap vs P287 (widths differ M 12ch
  vs 18ch, AM 16ch vs 20ch, CM 24ch vs 22ch,
  RM 14ch vs 16ch, RQ 12ch vs 16ch, QR 24ch
  vs 22ch).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=116961 (PB0 sig 0ac51600 NEW, lenB 84), S1
  n=116962 (fat PB1 sig 3bf3942d NEW, sig-eq own-C10
  47/84 payload diff, lenB 84),
  A 116963-978 PBA88-PLAIN (sig 02000000 via AC
  b0-b3, b0 const 02, AM 16/16 distinct 8B, mtab
  b25-27,35,80-83, b5 const 91 raw lencode),
  C 116979-988 C10-1SIG (3bf3942d x10 via CC
  b0-3, CM 10/10 distinct 12B diverge 10/10,
  mtab b22,23,30-35,80-83, b5 const 91 raw lencode),
  Q 116989-117052 QUAD88-4R single-sig 02000000 x64
  (QM6 b40,41,80-83 M 16/16 6B shared x3 + R12
  b26,27,34-39,84-87 rows above (r0 distinct,
  r123 share 8B) + tails above, NO frags, raw
  lencode b5 0x91+(o>=3)),
  R 117053-117308 T88-STANDARD (sig 2f000000, TM7
  b39,46,47,80-83 by COL RM 16/16 7B, TR6
  b40,41,76-79 by ROW RQ 16/16 UNPAIRED,
  b84-87 const de75775e ring-wide,
  b4=(0x7b+2off)&FF, b5=0x92+(off>=67)+(off>=195)).
  C blocks carry T78282/78287/78292/78307/78323/
  78344 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 8B,
  C 12B, Q 6/12B, R 7/6B), Q raw-lencode b5 step
  (equiv counter b4=(0xfb+2off)&FF verified 64/64),
  R counter b4=(0x7b+2off)&FF + (off>=67)+(off>=195)
  (C literals 123/146 verified == 0x7b/0x92),
  temps _t6028-6043 (base max _t6027, no reuse) +
  _b3653/3655/3657/3658/3660/3661 (base max _b3651,
  no reuse) + _i3654/3656/3659/3662 (base max _i3652,
  no reuse), all 6 verified.
  Insert position exact both sides: after T10P287R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-727/A-352 geometry (PB0 NEW, PB1 NEW +
  sig-eq own-C10 + 47/84 payload diff,
  PBA88 PLAIN VPOS 9 b5 const 91 16/16 distinct NO pair,
  C10-1SIG VPOS 13 b5 const 91 10/10 diverge,
  QUAD88-4R VPOS 20 + R12 4/4 UNPAIRED + r123
  share-8B + TRUE-3B + b5 step o2->3 + edge
  116991->116992 + M-tails NEW,
  T88-STANDARD VPOS 15 + TR6 16/16 UNPAIRED +
  b84-87 de75775e + counter 7b/92/67/195,
  lencode 348/348 whole-tier, Q edge 116991->116992 +
  ring edges 117119->117120 + 117247->117248, NO D
  dips) incl exact values (PBA/C10 sigs, R12 rows +
  tails + LCS, ring TM7/TR6 + consts stand).
- Edges via counter formula first-hand: A head c7/91
  tail e5/91 b5set {91} NO step, 0 ff;
  C head e7/91 tail f9/91 b5set {91} NO step, 0 ff;
  Q head fb/91 tail 79/92 b5set {91,92} step
  o2->o3: 116991 (o2, ff/91) -> 116992 (o3,
  01/92) Q-row0, exactly 1 ff in 64 (o2);
  ring 117119 (off66, ff/92) -> 117120 (off67, 01/93);
  117247 (off194, ff/93) -> 117248 (off195, 01/94);
  exactly 2 ff in 256 (o66/o194); R head 7b/92 tail
  79/94; formula re-derived from T10P288R code text
  (7b/92/67/195); all edge pins + tail 117308 in
  for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (c3/91, c5/91) match raw lencode.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 604 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 599 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 409).
- Wall on band diff added lines (scope 62f9b99c..
  b68cdf88, 898 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 604/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 598->600 +2 / ranges 582->586 +4 = +6,
  C singletons 603->605 +2 / ranges 604->608 +4
  (C absolute +5 singletons = standing 5 pre-existing
  nested py guards; C-range absolute gap standing,
  deltas agree every side),
  CLOSED T10P prints 1616->1622 +6 both sides,
  seal 1710->1716 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-727-q880-
  t10p288 verdict CONFIRM (Q1 shape 15/15 + Q2 quad/ring
  11/11 + Q3 counters 12/12 = 38/38 as-filed; file
  present, counts verified; exact-value corroboration
  incl PB0 NEW + PB1 NEW + sig-eq own-C10 + 47/84 diff,
  PBA88-PLAIN, C10-1SIG, QUAD88-4R + R12 rows + 8B-share
  + TRUE-3B + b5 step + edge + M-tails NEW, ring
  STANDARD + TR6 16/16 UNPAIRED + edges + consts,
  own C10-head n116979 reconstruction 47/84 vs S1
  (sig-eq, py-comment figure re-derived exact) AND
  separate P287C10-head n116631 reconstruction 47/84
  vs S1 (DIFFERENT comparison, coincident count))
  + A-352 corroboration (all legs CONFIRM, no geometry
  correction). No CONFIRM-P288.md file; A-727 suffices
  per rule. Agrees with cport commit msg (PYID 8499,
  RGRAM 16998).
- Quiz: no conflicting CLAIM/GATE/FLAG on b396 (adjacent
  odds b395 base-used, b397 beyond-cap acknowledged).
  Activity polled (no b396 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r62/ (build396.log,
  pyid396.log, rgram396py/c.log, cmp396.py/.c,
  for396-w396/-w395base.nums, smoke396.log, tables396.log,
  tabaudit288.py, edges288.py, edges396.log,
  numstat396.txt, add/delnorm396.txt, added396.txt,
  banddiff396.txt, pydiff288.txt, cdiff396.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
