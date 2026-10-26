# GATE 256db28a b390 T10P282 pins 114873..115220 (1680 tiers) PASS-functional

Seat sweep2-r60, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r60/w390 @256db28a.
Band = 3640ef6d (py merge w2b@db0be62c partial, +6 tiers, +64 pins)
+ 256db28a (C port). Base 4ef44f6f (b389 tip, 1674 tiers sealed).
Trees diff-identical to tips at archive time (verified via git
ls-tree vs find); w390 +__pycache__ battery byproduct after runs,
w389base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build390/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 8a15c93b / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r60
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8311/8311 covered=8311/8311 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 16622/16622 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 16622/16622 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 16622/16622).
- PINS-RGRAM cells set-eq 16622/16622 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8311/8311 xor 0;
  PINS 16624 rows (2 hdr + 16622 = PASS lines, +64 vs base
  16560). For-list union 8279->8311 +32 (114873 114874
  114875 114876 114880 114885 114889 114890 114891 114892
  114896 114897 114898 114899 114900 114901 114916 114917
  114932 114933 114943 114944 114948 114949 114964 114965
  115071 115072 115136 115199 115200 115220),
  0 removed, range 114873..115220 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 32x2 = 64 = 16622-16558.
  The 32 = S0/S1 (2) + A head/mids/tail (6) + C head/mids/
  tail (7) + Q head/mids/edge-pair/mids/tail (10) +
  ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P282 C-vs-py, script-compared, TABAUDIT-GREEN
  91 PASS 0 FAIL (tabaudit282.py rc=0): S0/S1 168ch
  EXACT sigs 9ef00700 NEW / cb3de10f NEW (full-string NEW
  vs BOTH P281S0/S1, diffs S0 31/65 + S1 60/60),
  AM 16/16 8B distinct, CM 10/10 13B distinct, M 16/16
  7B distinct, QR 4/4 7B, QT 4/4 4B, RM 16/16 9B
  distinct, RQ 16/16 7B distinct UNPAIRED, no RT
  (STANDARD SPLIT), M==RQ 16/16 identical INTRA-tier,
  AC 74, CC 69, QC 64, RC 70; C _N decls 74/69/64/70
  match actual; byte-coverage unions exact every block
  (84/84/84/88, 0 overlap, b4/b5 computed).
  PBA16-PLAIN sig e0857ffe (b0 const e0; AC
  has no b5, b5-const memo-1) + NEW vs P281PBA c09417fb
  (cross-tier, P281PBA code-verified).
  C10-4SIG ORDERED map 3582e40f x6 @114891-96 + 4dffe70f
  @114897 + 8d59ea0f @114898 + ad85e10f x2 @114899-900
  via CM b0-2 + CC b3=0f (full sig b0-2 in tab, b0-2
  varpos, b3 const; staged: CM-sigs 3582e4 x6/4dffe7/
  8d59ea/ad85e1 x2 ORDERED) + NEW vs P281 C10-4SIG
  (different sigs, partial-b2,3-tab vs full-b0-2-tab
  geometry change code-verified);
  CM 10/10 diverge; CC has no b5.
  QUAD1s single-sig c09b7fe2 x64 (b20 const 93 via QC;
  QC has no b5, b5 step o>=43) + NEW vs P281 QUAD
  (1-sig vs SPLIT geometry, QR/QT 0-overlap
  code-verified; staged: AC-QC shared-pos 64,
  same-val 36, NOT const-repeat).
  R7 LAST3-PAIRED r1==r2==r3 72fabf3a6f842e x3,
  r0 b280ae92788e26 distinct; tails row-shared
  4/4 distinct dd6e42df/e1a9fa40/06aafa40/227a1141,
  r1/r2 share 2B fa40 (r0/r3 do not);
  QM7 shared 16/16 x3 NO frags; byte-LCS (1,2)=2
  rest 0 (own code-table LCS, memo value re-derived
  exact).
  Ring STANDARD (STANDARD, not ROWTAIL): TM9 b18,19,
  27,34,35,80-83 by COL RM 16/16 9B, TR7 b28-30,
  76-79 by ROW RQ 16/16 UNPAIRED, tails SPLIT
  b80-83 col / b76-79 row;
  RC b0-3 0f000000 NEW (P281 sig 0c000000),
  b84-87 63fa9206 ring-wide NEW (P281 sig
  af7cecbc, both per P281RC code-verified).
  Code-consts vs A-696 INCL (PBA 75 / C10 70 /
  quad 64 / T88 70): impl 74/69/64/70 = memo-1
  on PBA/C10 (b5-const excluded), identical
  on quad/T88 (standing bookkeeping).
  M-tails 16/16 ALL NEW vs P281 (zero overlap vs
  P281 M AND P281RM-tail8 AND P281RQ-tail8; P281
  M/RM/RQ rows re-read first-hand). AM/CM/M/RM/RQ/
  QT/QR 0-overlap vs P281 (widths differ AM 16ch
  vs 12ch, CM 26ch vs 24ch, M 14ch vs 16ch, RM 18ch
  vs 16ch, RQ 14ch vs 16ch; QR/QT same widths 14ch/
  8ch but 0-overlap).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=114873 (PB0 sig 9ef00700 NEW, lenB 84), S1
  n=114874 (fat PB1 sig cb3de10f NEW, lenB 84),
  A 114875-890 PBA16-PLAIN (sig e0857ffe via AC
  b0-b3, b0 const e0, AM 16/16 distinct 8B, mtab
  b12-14,19,76-79, b5 const 81 raw lencode),
  C 114891-900 C10-4SIG (map above via CM b0-2 +
  CC b3=0f, CM 10/10 distinct 13B diverge 10/10,
  mtab b0-2,11,18-22,80-83, b5 const 81 raw lencode),
  Q 114901-964 QUAD1s single-sig c09b7fe2 x64
  (QM7 b24-26,76-79 M 16/16 7B shared x3 + R7
  b12-14,18,19,21,22 LAST3-PAIRED above (b20 const
  93) + QT tails above, NO frags, raw lencode b5
  step o>=43),
  R 114965-115220 T88-STANDARD (sig 0f000000, TM9
  b18,19,27,34,35,80-83 by COL RM 16/16 9B, TR7
  b28-30,76-79 by ROW RQ 16/16 UNPAIRED, tails
  SPLIT, b84-87 const 63fa9206 ring-wide,
  b4=(0x2b+2off)&FF, b5=0x82+(off>=107)+(off>=235)).
  C blocks carry T76863/76868/76873/76888/76904/
  76927 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 8B,
  C 13B, Q 7/7/4B, R 9/7B), counter b4=(0x2b+2off)
  &FF + (off>=107)+(off>=235), temps _t5924-5941
  (base max _t5923, no reuse) + _b3591/3593/3595/
  3596/3597/3599/3600 (base max _b3589, no reuse) +
  _i3592/3594/3598/3601 (base max _i3590, no reuse),
  all 6 verified.
  Insert position exact both sides: after T10P281R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-696/A-346 geometry (PB0/PB1 NEW, PBA16
  PLAIN VPOS 9 b5 const 81 16/16 distinct NO pair,
  C10-4SIG VPOS 14 b5 const 81 10/10 diverge ORDERED
  map, QUAD1s VPOS 20 + R7 LAST3-PAIRED + QT r12
  share-2B + b20-93 + b5 step o>=43 + M-tails NEW,
  T88-STANDARD VPOS 18 + TR7 16/16 UNPAIRED + b84-87
  63fa9206, lencode 348/348 whole-tier, Q edge
  114943->114944 + ring edges 115071->115072 +
  115199->115200, NO D dips) incl exact values
  (PBA/C10 sigs+map, R7 values, QT tails + LCS, ring
  TM9/TR7 + consts stand).
- Edges via counter formula first-hand: A head 77/81
  tail 95/81 b5set {81} NO carry; C head 97/81 tail
  a9/81 b5set {81} NO carry; Q head ab/81 tail 29/82,
  formula b4=(0xab+2off)&FF b5=0x81+(off>=43) 64/64,
  edge 114943 (o42, ff/81) -> 114944 (o43, 01/82)
  mid-row2, exactly 1 ff in 64 (o42);
  ring 115071 (off106, ff/82) -> 115072 (off107, 01/83);
  115199 (off234, ff/83) -> 115200 (off235, 01/84);
  exactly 2 ff in 256 (o106/o234); R head 2b/82 tail
  29/84; formula re-derived from T10P282R code text
  (2B/82/107/235); all edge pins + tail 115220 in
  for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (73/81, 75/81) match raw lencode.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del
  (rgramc.c) + 237/0 (rgram.py) + 1/1 (for-line) +
  64/0 (PINS); raw C grep 605 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 393).
- Wall on band diff added lines (scope 4ef44f6f..
  256db28a, 912 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 610/0, rgram.py 237/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, dispatch-guards
  singletons 596->598 +2 / ranges 580->584 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep; C `(n) == (N)` / range form agrees absolute
  596->598/580->584), CLOSED T10P prints 1580->1586 +6,
  C CLOSED 1580->1586 +6 (deltas agree both
  sides), seal 1674->1680 +6
  (commit msgs): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-696-q794-
  t10p282 verdict CONFIRM (Q1 shape 13/13 + Q2 quad/ring
  12/12 + Q3 counters 12/12 = 37/37 as-filed; file
  present, counts verified; exact-value corroboration
  incl PBA/C10-4SIG map, QUAD1s + R7 last3-pair + QT
  tails + LCS + b20-93 + b5 step, M-tails NEW, ring
  STANDARD + TR7 16/16 UNPAIRED + edges + consts, own
  P281C10-head n114543 reconstruction 57/84 vs P282S1
  NEW) + A-346 viewer corroboration (all 3 legs
  CONFIRM). No CONFIRM-P282.md file; A-696 suffices per
  rule. Agrees with cport commit msg (PYID 8311, RGRAM
  16622).
- Quiz: no conflicting CLAIM/GATE/FLAG on b390 (adjacent
  odds b389 base-used, b391 beyond-cap acknowledged).
  Newest PARENT-* is QNUM-19 (w2d Q-block only, read, no
  gate impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r60/ (build390.log,
  pyid390.log, rgram390py/c.log, cmp390.py/.c,
  for390-old/-new.nums, smoke390.log, tables390.log,
  tabaudit282.py, edges282.py, edges390.log,
  numstat390.txt, add/delnorm390.txt, added390.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
