# GATE f9bb207b b356 T10P248 pins 103041..103388 (1476 tiers) PASS-functional

Seat sweep2-r52, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r52/w356 @f9bb207b.
Band = 129832ad (py merge w2b@63cb0926 partial, +6 tiers, +62 pins)
+ f9bb207b (C port). Base 4b8d0444 (b355 tip, 1470 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build356/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4438b124 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value; band touches
  no aae sources per numstat).
- RGRAMC-PYID 7246/7246 covered=7246/7246 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14492/14492 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 14492/14492 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 14492/14492).
- PINS-RGRAM cells set-eq 7246/7246 (xor 0, PINS base-N
  set vs for-list); PINS 14494 rows (2 hdr + 14492 =
  PASS lines). For-list union +31 (103041 103042 103043
  103044 103050 103054 103057 103058 103059 103062 103063
  103065 103067 103068 103069 103077 103085 103093 103101
  103109 103117 103125 103131 103132 103133 103167 103168
  103261 103295 103296 103388), 0 removed, range
  103041..103388 exact. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 31x2 = 62 = 14492-14430.
  The 31 = S0/S1 (2) + A head/mids/tail (6) + C
  head/mids/tail (6) + Q head/mids/tail (10) +
  ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var).
- Tables audit P248 C-vs-py, script-compared, TABAUDIT-GREEN
  61 PASS 0 FAIL (tabaudit248.py rc=0): S0/S1 168ch
  EXACT sigs 1ce10200 NEW / c503ce05 NEW (both strings
  NEW vs P247), AM 16/16 8B distinct, CM 10/10 14B,
  M 16/16 7B distinct, QT 4/4 2B, RM 16/16 8B distinct,
  RQ 16/16 7B distinct, AC 74/74, CC 68/68, QC 73/73,
  RC 71/71; C _N decls 74/68/73/71 match actual;
  byte-coverage unions exact every block (84/84/84/88,
  0 overlap, b4/b5 in no const set).
  CM sig-map exact order: ce05 x4 @103059-62 +
  ee02 x6 @103063-68 (b2b3 prefix; CC b0,b1 const
  c5,03 sig-head -> full sigs c503ce05 x4 ==PB1 /
  c503ee02 x6, first 4/6 split).
  QT values 6936/9336/30ea/5aea (r0/r1 share 2nd-B 36,
  r2/r3 share 2nd-B ea); b82,83 const 3664 quad-wide.
  Code-consts vs A-596 INCL (PBA 75 / C10 69 / quad 74 /
  T88 71): impl 74/68/73 = memo-1 on PBA/C10/quad
  (b5 const 25 all three, standing incl/excl
  bookkeeping — A-596 §3 explicitly no-finding);
  T88 71 identical. P248 M rows == P248 RQ rows 16/16
  (staged identical strings at different byte positions,
  harmless); M-tails 16/16 ALL NEW vs P247T (P247 RQ
  byte order re-read first-hand, b76-79 last).
  RM/RQ UNPAIRED, tails SPLIT (RM b80-83 by COL 16/16,
  RQ b76-79 by ROW 16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=103041 (PB0 sig 1ce10200 NEW, lenB 84), S1
  n=103042 (fat PB1 sig c503ce05 NEW, lenB 84),
  A 103043-103058 PBA16 single-sig (sig 809a1f4a NEW
  via AC b0-b3, AM 16/16 distinct 8B, mtab
  b21-23,31,76-79, b5 const 25 raw lencode),
  C 103059-103068 C10 2-SIG 4+6 (sig map exact order
  above, CM 10/10 distinct 14B diverge 10/10, mtab
  b2,3,22,23,30-35,80-83 sig-bytes-in-tab, b5 const
  25), Q 103069-103132 QUAD-2T single-sig 809a1f2a
  (PBA-adjacent 4a->2a via QC b0-b3, QM7 b36-38,76-79
  M 16/16 distinct 7B, QT 2B tails above, NO R-block
  first R-less quad, b5 const 25 whole-range raw
  lencode), R 103133-103388 T88-ring STANDARD
  (sig 02000000 ==P247T re-read first-hand, TM8
  b19,39,46,47,80-83 by COL RM 16/16 distinct, TR7
  b40-42,76-79 by ROW RQ 16/16 distinct UNPAIRED
  b42 in T-R, tails SPLIT, b84-87 const fd74651e
  ring-wide, b4=(0xbb+2off)&FF, b5=0x25+(off>=35)+
  (off>=163)). C blocks carry T68066/68071/68076/
  68091/68108/68127 py-line mirrors (each re-read:
  hits the exact py guard line), bounds + byte
  positions exact, temps _t5264-5279 (base max _t5263,
  no reuse) + _b3215-3223 + _i3216-3224, all 6
  verified. Insert position exact both sides: after
  T10P247R close, at dispatch tail (N-out-of-scope
  fallthrough follows). Matches A-596/A-318 geometry
  (PB0/PB1 NEW, PBA16 VPOS 9 b5 const 25, C10-2SIG
  4+6 VPOS 15 b5 const 25 10/10 diverge NO pair,
  QUAD-2T VPOS 10 b5 const 25 NO R-block, T88 VPOS 17,
  lencode 348/348 whole-tier, ring edges 103167->103168
  + 103295->103296, NO D dips) incl exact values (CM
  sig-map, QT 2B tails, b82,83 3664, M-tails NEW,
  ring TM8/TR7 16/16 UNPAIRED, tails SPLIT, b84-87
  fd74651e, consts stand).
- Edges via counter formula first-hand: 103167 (off34,
  ff/25) -> 103168 (off35, 01/26); 103295 (off162,
  ff/26) -> 103296 (off163, 01/27); all four pins in
  for-list + 2 PASS lines each py+C. Q b5set {25},
  head b5set {25} (no carry anywhere). Ring counter ==
  raw lencode 256/256, 0 mismatch. Odd-lencode 348/348.
  No DISSENT: cut bytes verify.
- C diff purely additive: numstat 596 add / 0 del
  (rgramc.c) + 230/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 591 content + 5 blank-only
  `+` lines (verified bare) / 0 del; fine-norm
  (rgramc.c scope, TNP/_tN/_iN/_bN, BSD tools,
  empty-excluding) del-subset-add 0 missing (del-uniq
  0, add-uniq 402).
- Wall on band diff added lines (scope 4b8d0444..
  f9bb207b, 889 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim 0 hits, shebang 0 hits.
  Files touched: rgramc.c 596/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 528->530 +2 / ranges 444->448 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep), CLOSED T10P prints 1376->1382 +6, C singletons
  523->525 +2 (C-vs-py 5-offset pre-existing, unchanged),
  seal 1470->1476 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-596-q760-
  t10p248 verdict CONFIRM (34/34 = 11/11 shape +
  14/14 quad/ring + 9/9 counters; file present,
  counts verified; exact-value corroboration incl
  CM sig-map, QT tails, b82,83 const, M-tails NEW,
  ring edges + consts re-checked above) + A-318
  viewer corroboration (all 3 legs CONFIRM). No
  CONFIRM-P248.md file; A-596 suffices per rule.
  Agrees with cport commit msg (PYID 7246, RGRAM
  14492).
- Quiz: no conflicting CLAIM/GATE/FLAG on b356. Newest
  PARENT-* is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r52/ (build356.log,
  pyid356.log, rgram356py/c.log, cmp356.py/.c,
  for356-old/-new.nums, pins356.basen, smoke356.log,
  tables356.log, tabaudit248.py, edges356.log,
  numstat356.txt, added356.txt, add/delnorm356.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
