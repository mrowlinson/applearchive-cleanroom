# GATE 0dd1dddf b414 T10P306 pins 123225..123572 (1824 tiers) PASS-functional

Seat sweep2-r66, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r66/w414 @0dd1dddf.
Band = efb485e3 (py merge w2b@c5db4c86 partial, +6 tiers, +62 pins)
+ 0dd1dddf (C port). Base f539e0c8 (b413 tip, 1818 tiers sealed).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 = 113 non-tmp
+ 4 tmp); w414 +__pycache__ battery byproduct after runs,
w413base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build414/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc fa194b13 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r66
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9060/9060 covered=9060/9060 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 18120/18120 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 18120/18120 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 18120/18120).
- PINS-RGRAM cells set-eq 18120/18120 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9060/9060 xor 0;
  PINS 18122 rows (2 hdr + 18120 = PASS lines, +62 vs base
  18060). For-list union 9029->9060 +31 (123225 123226
  123227 123228 123234 123235 123241 123242 123243 123244
  123247 123248 123251 123252 123253 123261 123263 123264
  123269 123277 123285 123293 123301 123316 123317 123391
  123392 123445 123519 123520 123572),
  0 removed, range 123225..123572 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 18120-18058.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid/tail pairs (6) + Q head/mid/edge-pair/
  5-mids/tail (10, b5-step edge pair 123263/123264 pinned) +
  ring head/edge-pair/mid/edge-pair/tail (7).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P306 C-vs-py, script-compared, TABAUDIT-GREEN
  113 PASS 0 FAIL (tabaudit306.py rc=0): S0/S1 168ch
  EXACT sigs db1b7900 sig-EQ-P305S0 / 80120ffa NEW (S0
  32/84 payload diff first-hand vs P305S0, NOT byte-equal,
  FIRST 32-diff; S1 NEW vs P305 heads db1b7900/80299f81
  AND own-C10 803b4fc4; staged as full-payload singleton
  consts),
  AM 16/16 8B distinct, CM 10/10 12B distinct, M 16/16
  8B distinct, QR 4/4 11B distinct, RM 16/16 9B
  distinct, RQ 16/16 8B distinct UNPAIRED, no QT
  (quad tails live in R11) + no RT (SPLIT tails) +
  no RF (no frag this tier),
  M==RQ 16/16 identical INTRA-tier (STANDARD tier,
  3rd running P302/P304/P306),
  AC 78, CC 70, QC 67, RC 69; C _N decls 78/70/67/69
  match actual; byte-coverage unions exact every block
  (88/84/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN sig 0f000000 (b0 const 0f, b5 const
  c2 via lencode; AM 16/16 distinct NO pair; M8
  b20,21,22,23,80-83) + vs P305PBA 09000000 (novelty =
  new sig 0f + AM 0-overlap).
  C10-1SIG 803b4fc4 x10 NOT-PB1-sig (sig in CC
  b0-3 consts; CM 10/10 diverge 12B; rows 0-8 share
  16ch 721329877813b2ab, tails 0daaa4af/2daaa4af/
  4daaa4af/04311bbb/4c3351c3/6c3351c3/8c3351c3/
  ac3351c3/cc3351c3, row9 distinct head f20d0937
  tail 2db3ab3a; CC has no b5, b5 const c2 full
  block via lencode).
  QUAD88-4R single-sig 0f000000 x64 (QC b0-3;
  b5 step 0xc2+(o>=11), edge o10->11 @123263 ff/c2
  -> 123264 01/c3, exactly 1 ff in 64; QM8 16/16
  distinct NO frags + R11 rows r0 4d5cfce5 distinct
  vs r123 share-14B 8adb9da333e671 byte7-diverge
  ea/2e/53, tails b84-87 4/4 distinct 13f28f3f/
  ea331391/2e341391/53341391, r23 TRUE 3B 341391,
  r1 2B 1391; byte-LCS (2,3)=3, (1,2)=(1,3)=2,
  (0,1)=(0,2)=(0,3)=1 -- LCS-NOTE: py-comment +
  memo say "r0 lcs=0" but first-hand 1 via shared
  single byte 0x13 (r0 13.. vs r123 ..1391);
  prose shorthand only, tails still 4-distinct,
  TRUE-3B/2B stand, geometry unaffected, tier stands).
  Ring STANDARD-split: TM9 b18,19,27,34,35,80-83 by
  COL RM 16/16 + TR8 b28-31,76-79 by ROW RQ 16/16
  UNPAIRED (tails SPLIT b80-83 col / b76-79 row;
  b8 const 79, no frag); RC b0-3 b0000000, b84-87
  e46e4a40 ring-wide NEW (P305 c372802f).
  VPOS partitions re-derived from code: PBA 9
  (M8+b4, b5const excluded) / C10 13 (M12+b4,
  b5const excluded) / quad 21 (QM8+R11+b4+b5vary;
  b27 excluded const-ff in QC) / T 19 (TM9+TR8+
  b4+b5) -- all match A-782.
  Code-consts vs A-782 (PBA 79 / C10 71 /
  quad 67 / T88 69): impl 78/70/67/69 =
  memo-exact on quad/T88 (b5vary, no deduction),
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-898 sheet counts b5-iff-const (memo A-782
  confirms the sheet) -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  geometry exact, PORT verdict stands; FLAGGED for
  memo (2nd band running).
  QUAD single-sig 0f000000 vs P305 SPLIT; PBA sig
  0f NEW vs P305 09; QUAD-sig-EQ-PBA-sig this tier
  (same sig, different tables: AC-QC both=67
  sameval=39).
  M-tails 16/16 ALL NEW vs P305 (zero overlap vs
  P305RQ row-led AND vs P305M AND vs P305RM-tail8
  col-led -- P305T STANDARD). AM/CM/M/QR/RM/RQ
  0-overlap vs P305 (all widths differ: P306 AM16/
  CM24/M16/QR22/RM18/RQ16 vs P305 AM18/CM22/M14/
  QR24/RM14/RQ14).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=123225 (PB0 sig db1b7900 EQ-P305S0-sig, 32/84
  diff, lenB 84), S1 n=123226 (fat PB1 sig 80120ffa
  NEW, lenB 84),
  A 123227-242 PBA88-PLAIN (sig 0f000000 via AC
  b0-b3, b0 const 0f, AM 16/16 distinct 8B, mtab
  b20,21,22,23,80-83, raw lencode b4/b5 const c2),
  C 123243-252 C10-1SIG (803b4fc4 x10 NOT-PB1
  via CC b0-3 + CM tab, CM 10/10 distinct 12B
  diverge 10/10, mtab b12,13,14,18-22,80-83, b5
  const c2 raw lencode),
  Q 123253-316 QUAD88-4R single-sig 0f000000 x64
  (QM8 b28-31,80-83 M 16/16 8B + R11
  b20-26,84-87 rows above (r0 distinct, r123
  share 14B) + tails above, NO frags, raw lencode
  b5 step o10->11),
  R 123317-572 T88-RING-STANDARD (sig b0000000,
  TM9 b18,19,27,34,35,80-83 by COL RM 16/16, TR8
  b28-31,76-79 by ROW RQ 16/16 UNPAIRED,
  b84-87 const e46e4a40 ring-wide,
  b4=(0x6b+2off)&FF, b5=0xc3+(off>=75)+(off>=203)).
  C blocks carry T82539/82544/82549/82564/82580/
  82601 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 8B,
  C 12B, Q 8/11B, R 9/8B),
  R counter b4=(0x6b+2off)&FF + (off>=75)+(off>=203)
  (C literals 107/195 verified == 0x6b/0xc3),
  temps _t6325-6340 (base max _t6324, no reuse) +
  _b3834/3836/3838/3839/3841/3842 (base max _b3832,
  no reuse) + _i3835/3837/3840/3843 (base max _i3833,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P305R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-782 geometry (PB0 sig-eq-P305 + 32/84
  NOT-byte-equal FIRST; PB1 NEW; PBA88-PLAIN VPOS 9
  sig-0f b5 const c2 16/16 distinct NO pair,
  C10-1SIG VPOS 13 NOT-PB1-sig b5 const 10/10 diverge,
  QUAD88-4R VPOS 21 + R11 4/4 UNPAIRED + share-14B +
  r23-TRUE-3B + r1-2B + b5-step o10->11 + M-tails NEW,
  T88-RING-STANDARD VPOS 19 + TM9/TR8 + tails-split
  + b84-87 e46e4a40 + counter 6b/c3/75/203,
  lencode 348/348 whole-tier, Q step edge
  123263->123264, ring edges 123391->123392 +
  123519->123520, NO D dips) incl exact values (PBA/
  C10/QUAD/T88 sigs, R11 rows + tails + LCS, ring
  split + consts stand; sheet-vs-tables const-count
  note is S-F arithmetic in tables only per memo,
  geometry unaffected; LCS-NOTE above is the one
  prose imprecision found, cut bytes stand; M==RQ
  equality unmentioned by memo, batteries confirm,
  tier stands).
- Edges via counter formula first-hand: A head b7/c2
  tail d5/c2 b5set {c2} NO step, 0 ff;
  C head d7/c2 tail e9/c2 b5set {c2} NO step, 0 ff;
  Q head eb/c2 tail 69/c3 b5step o10->11 (123263
  ff/c2 -> 123264 01/c3), exactly 1 ff in 64
  (b4 base 0xeb step2 64/64);
  ring 123391 (off74, ff/c3) -> 123392 (off75, 01/c4);
  123519 (off202, ff/c4) -> 123520 (off203, 01/c5);
  exactly 2 ff in 256; R head 6b/c3 tail
  69/c5 (Q tail 69/c3 vs R tail 69/c5 differ in b5 --
  labeled apart); formulas re-derived from T10P306R
  code text (6b/c3/75/203) + T10P306Q text
  (c2/11/10/11); all edge pins + tail
  123572 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (b3/c2, b5/c2) match raw lencode.
  Odd-lencode 348/348. No DISSENT on cut bytes.
- C diff purely additive: numstat 604 add / 0 del
  (rgramc.c) + 230/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 599 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 389).
- Wall on band diff added lines (scope f539e0c8..
  0dd1dddf, 897 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 634->636 +2 /
  ranges 654->658 +4 = +6, C identical 634->636 +2 /
  654->658 +4 (py=C dispatch-exact; nested 8-space extras
  outside dispatch scope, standing bookkeeping, deltas
  agree every side),
  CLOSED T10P prints 1724->1730 +6 both sides,
  seal 1818->1824 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-782-q898-P306
  verdict CONFIRM 54/54 CLEAN (b1 shape 25/25 + b2
  quad+T 15/15 + b3 counters 14/14; file present,
  counts verified; exact-value corroboration incl
  PB0 sig-eq-P305 + 32/84 NOT-byte-equal FIRST,
  PB1 NEW, PBA88-PLAIN sig-0f M8, C10-1SIG NOT-PB1-sig
  M12, QUAD88-4R + R11 rows + share-14B + r23-TRUE-3B +
  r1-2B + b5-step + M-tails NEW, T88-RING-STANDARD +
  TM9/TR8 + tails-split + b84-87 e46e4a40 + edges +
  consts; plus LCS-NOTE: "r0 lcs=0" shorthand
  imprecise first-hand ((0,1)=(0,2)=(0,3)=1 shared
  0x13), prose-only, tier stands; plus
  sheet-vs-tables const-count note: Q-898 sheet
  FIXED-rule 79/71/67/69 memo-exact, committed tables
  78/70/67/69 still deduct const-b5 -- S-F arithmetic
  in tables only, geometry exact, PORT verdict stands).
  Agrees with cport commit msg (PYID 9060, RGRAM 18120).
- Quiz: no conflicting CLAIM/GATE/FLAG on b414 (adjacent
  odds b413 base-used, b415 sweep-turf acknowledged).
  Activity polled (no b414 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r66/ (build414.log,
  pyid414.log, rgram414py/c.log, cmp414.py/.c/.pyo/.co,
  for414.nums/for413base.nums, smoke414.log, tables414.log,
  tabaudit306.py, edges306.py, edges414.log,
  numstat414.txt, add/delnorm414.txt, added414.txt,
  banddiff414.txt, pydiff306.txt, cdiff414.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
