# GATE b5516b9b b398 T10P290 pins 117657..118004 (1728 tiers) PASS-functional

Seat sweep2-r62, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r62/w398 @b5516b9b.
Band = aecb8331 (py merge w2b@d0220e2e partial, +6 tiers, +62 pins)
+ b5516b9b (C port). Base 7e4dcf66 (b397 tip, 1722 tiers sealed).
Trees diff-identical to tips at archive time (verified via git
ls-tree vs find); w398 +__pycache__ battery byproduct after runs,
w397base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build398/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 6c3c3aa3 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r62
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8562/8562 covered=8562/8562 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 17124/17124 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 17124/17124 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 17124/17124).
- PINS-RGRAM cells set-eq 17124/17124 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8562/8562 xor 0;
  PINS 17126 rows (2 hdr + 17124 = PASS lines, +62 vs base
  17064). For-list union 8531->8562 +31 (117657 117658
  117659 117660 117666 117667 117673 117674 117675 117676
  117681 117682 117683 117684 117685 117692 117700 117701
  117709 117717 117725 117733 117740 117748 117749 117759
  117760 117877 117887 117888 118004),
  0 removed, range 117657..118004 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 17124-17062.
  The 31 = S0/S1 (2) + A head/mids/tail (6) +
  C head/mids/tail (6) + Q head/mids/tail (10, no step edge) +
  ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P290 C-vs-py, script-compared, TABAUDIT-GREEN
  99 PASS 0 FAIL (tabaudit290.py rc=0): S0/S1 168ch
  EXACT sigs 5f6f1300 NEW / ccbede26 NEW (S diffs vs P289:
  S0 31/84 + 65/84, S1 61/84 + 62/84; P289 sigs
  0fc51600 / 3bf3f420),
  AM 16/16 9B distinct, CM 10/10 13B distinct, M 16/16
  7B distinct, QR 4/4 12B distinct, RM 16/16 9B
  distinct, RQ 16/16 7B distinct UNPAIRED, no QT
  (tails live in R12) + no RT (STANDARD SPLIT),
  M==RQ 16/16 identical INTRA-tier,
  AC 77, CC 69, QC 67, RC 70; C _N decls 77/69/67/70
  match actual; byte-coverage unions exact every block
  (88/84/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN sig 02000000 (b0 const 02; AC
  has no b5, b5 const 97 via lencode) + REPEAT vs
  P289PBA 02000000 (88B-pay PBA sig persists P289->P290;
  novelty = AM rows 0-overlap + M9 geometry
  b16-19,23,80-83 vs P289 M7).
  C10-3SIG ORDERED 7+1+2 (1b19db26 x7 @117675-81 +
  bb9cdb26 x1 @117682 + 8bf4d626 x2 @117683-84, map
  order code-verified from CM rows; 3 sig bytes b0-2
  in tab, b3 const 26; CM 10/10 diverge; CC has no b5,
  b5 const 97 via lencode).
  QUAD88-4R single-sig 02000000 x64 (QC b0-3;
  b27-skipped const 55 code-verified; QC has no b5,
  b5 const 97 full odd lencode, NO step, NO ff) +
  rows NEW vs P289 QUAD (R12 width 24ch vs P289
  20ch, 0-overlap code-verified; staged: AC-QC
  shared-pos 66, same-val 38, NOT const-repeat;
  11 AConly + 1 QConly).
  R12 rows r0 f272eec66e934b3 distinct vs
  r123 share-8B 328fc02e7833d143, differ at byte 8
  (eb/c9/ee); tails b84-87 4/4 distinct
  93fc9b25/eb2b0327/c9af0327/eeaf0327, r23 TRUE
  3B af0327, r1 shares 2B 0327;
  byte-LCS (0,*)=0, (1,2)=(1,3)=2, (2,3)=3
  (own code-table LCS, memo/py-comment value
  re-derived exact).
  Ring STANDARD-split: TM9 b18,19,27,34,35,80-83 by COL
  RM 16/16 9B (M carries b80-83 col), TR7
  b28-30,76-79 by ROW RQ 16/16 UNPAIRED (R carries
  b76-79 row); RC b0-3 24000000 NEW (P289 sig
  SPLIT), b84-87 fcaa79e0 ring-wide NEW (P289
  8536000f, per P289RC code-verified).
  Code-consts vs A-729 INCL (PBA88 78 / C10 70 /
  quad88 68 / T88 70): impl 77/69/67/70 = memo-1
  on PBA/C10/quad (b5-const excluded), identical
  on T88 (standing bookkeeping).
  M-tails 16/16 ALL NEW vs P289 (zero overlap vs
  P289 M AND P289RM-tail8 AND P289RQ-tail8; P289
  M/RM/RQ rows re-read first-hand). AM/CM/M/QR/
  RM/RQ 0-overlap vs P289 (widths differ M 14ch
  vs 12ch, AM 18ch vs 14ch, CM 26ch vs 24ch,
  QR 24ch vs 20ch, RQ 14ch vs 12ch; RM same
  width 18ch but 0-overlap).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=117657 (PB0 sig 5f6f1300 NEW, lenB 84), S1
  n=117658 (fat PB1 sig ccbede26 NEW, lenB 84),
  A 117659-674 PBA88-PLAIN (sig 02000000 via AC
  b0-b3, b0 const 02, AM 16/16 distinct 9B, mtab
  b16-19,23,80-83, b5 const 97 raw lencode),
  C 117675-684 C10-3SIG 7+1+2 (sigs above via CM
  b0-2 + CC b3 const 26, CM 10/10 distinct 13B
  diverge 10/10, mtab b0-2,11,18-22,80-83, b5
  const 97 raw lencode),
  Q 117685-748 QUAD88-4R single-sig 02000000 x64
  (QM7 b28-30,80-83 M 16/16 7B shared x3 + R12
  b16-18,22-26,84-87 rows above (r0 distinct,
  r123 share 8B) + tails above, NO frags, raw
  lencode b5 const 97),
  R 117749-118004 T88-STANDARD (sig 24000000, TM9
  b18,19,27,34,35,80-83 by COL RM 16/16 9B, TR7
  b28-30,76-79 by ROW RQ 16/16 UNPAIRED,
  b84-87 const fcaa79e0 ring-wide,
  b4=(0xeb+2off)&FF, b5=0x97+(off>=11)+(off>=139)).
  C blocks carry T78745/78750/78755/78770/78786/
  78807 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 9B,
  C 13B, Q 7/12B, R 9/7B), Q raw-lencode b5 const
  (equiv counter b4=(0x6b+2off)&FF verified 64/64),
  R counter b4=(0xeb+2off)&FF + (off>=11)+(off>=139)
  (C literals 235/151 verified == 0xeb/0x97),
  temps _t6060-6075 (base max _t6059, no reuse) +
  _b3673/3675/3677/3678/3680/3681 (base max _b3671,
  no reuse) + _i3674/3676/3679/3682 (base max _i3672,
  no reuse), all 6 verified.
  Insert position exact both sides: after T10P289R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-729/A-354 geometry (PB0/PB1 NEW,
  PBA88 PLAIN VPOS 10 b5 const 97 16/16 distinct NO pair,
  C10-3SIG VPOS 14 b5 const 97 10/10 diverge 7+1+2,
  QUAD88-4R VPOS 20 + R12 4/4 UNPAIRED + b27-55 +
  r123 share-8B + r23-TRUE-3B + r1-2B + b5 const +
  M-tails NEW,
  T88-STANDARD VPOS 18 + TR7 16/16 UNPAIRED +
  b84-87 fcaa79e0 + counter eb/97/11/139,
  lencode 348/348 whole-tier, ring edges
  117759->117760 + 117887->117888, NO D
  dips) incl exact values (PBA/C10 sigs + map, R12
  rows + tails + LCS, ring TM9/TR7 + consts stand).
- Edges via counter formula first-hand: A head 37/97
  tail 55/97 b5set {97} NO step, 0 ff;
  C head 57/97 tail 69/97 b5set {97} NO step, 0 ff;
  Q head 6b/97 tail e9/97 b5set {97} NO step, 0 ff
  in 64 (b5 const full block);
  ring 117759 (off10, ff/97) -> 117760 (off11, 01/98);
  117887 (off138, ff/98) -> 117888 (off139, 01/99);
  exactly 2 ff in 256 (o10/o138); R head eb/97 tail
  e9/99 (Q tail e9/97 vs R tail e9/99 differ in b5 --
  labeled apart); formula re-derived from T10P290R
  code text (eb/97/11/139); all edge pins + tail
  118004 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (33/97, 35/97) match raw lencode.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 604 add / 0 del
  (rgramc.c) + 230/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 599 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 387).
- Wall on band diff added lines (scope 7e4dcf66..
  b5516b9b, 897 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 602->604 +2 / ranges 590->594 +4 = +6,
  C singletons 607->609 +2 / ranges 612->616 +4
  (C absolute +5 singletons = standing 5 pre-existing
  nested py guards; C-range absolute gap standing,
  deltas agree every side),
  CLOSED T10P prints 1628->1634 +6 both sides,
  seal 1722->1728 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-729-q882-
  t10p290 verdict CONFIRM (Q1 shape 14/14 + Q2 quad/ring
  11/11 + Q3 counters 12/12 = 37/37 as-filed; file
  present, counts verified; exact-value corroboration
  incl PB0/PB1 NEW, PBA88-PLAIN, C10-3SIG 7+1+2 map,
  QUAD88-4R + R12 rows + 8B-share + r23-TRUE-3B +
  r1-2B + b5 const + M-tails NEW, ring STANDARD +
  TR7 16/16 UNPAIRED + edges + consts, own P289C10-head
  n117327 reconstruction 55/84 vs S1 (sig 3bf3f420,
  matches no P290 sig -- S1 ccbede26 NEW standalone))
  + A-354 corroboration (all legs CONFIRM, no geometry
  correction). No CONFIRM-P290.md file; A-729 suffices
  per rule. Agrees with cport commit msg (PYID 8562,
  RGRAM 17124).
- Quiz: no conflicting CLAIM/GATE/FLAG on b398 (adjacent
  odds b397 base-used, b399 beyond-cap acknowledged).
  Activity polled (no b398 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r62/ (build398.log,
  pyid398.log, rgram398py/c.log, cmp398.py/.c,
  for398-w398/-w397base.nums, smoke398.log, tables398.log,
  tabaudit290.py, edges290.py, edges398.log,
  numstat398.txt, add/delnorm398.txt, added398.txt,
  banddiff398.txt, pydiff290.txt, cdiff398.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
