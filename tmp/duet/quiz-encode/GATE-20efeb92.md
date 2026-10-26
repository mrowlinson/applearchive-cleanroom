# GATE 20efeb92 b350 T10P242 pins 100953..101300 (1440 tiers) PASS-functional

Seat sweep2-r49, first-hand, WT tmp/wt-encode-sweep2 @20efeb92,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r49.
Band = 46f669c0 (py merge w2b@2acda95a partial, +6 tiers, +62 pins)
+ 20efeb92 (C port). Base b3b974d6 (b349 tip, 1434 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build350/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 9ed948a1 / aae d6e27c97
  (aae identical to b288-b349 builds: aae.c untouched).
- RGRAMC-PYID 7060/7060 covered=7060/7060 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14120/14120 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 14120/14120 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 14120/14120).
- PINS-RGRAM cells set-eq 7060/7060 (diff 0, PINS base-N
  set vs for-list); PINS 14122 rows (2 hdr + 14120 =
  PASS lines). For-list union +31 (100953 100954 100955
  100962 100970 100971 100972 100973 100974 100975 100978
  100980 100981 100991 100992 100996 100997 101004 101012
  101013 101020 101028 101029 101036 101044 101045 101119
  101120 101247 101248 101300), 0 removed, range
  100953..101300 exact. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 31x2 = 62 = 14120-14058.
  The 31 = S0/S1 (2) + A head/mid/tail (3) + C
  head/mids/tail (7) + Q head/carry-pair/mids/tail
  (13) + ring head/edge-pairs/tail (6).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P242 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, CM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 73/73, CC 69/69,
  QC 63/63, RC 69/69; C _N decls 73/69/63/69
  match actual (tabc242.py rc=0, 6-block PBA/
  C10-MS/quad/T88-ring, nothing else).
  Code-consts vs A-568 (PBA 74 / C10 70 /
  quad 63 / T88 69 INCL): impl -1 on PBA/C10
  is the standing incl/excl bookkeeping (writer
  dual-accounts, excl 73/69 — A-568 §3 explicitly
  no-finding; quad 63 + T88 69 identical since
  b5-varying); byte-coverage proven A 73+11,
  C 69+15, Q 63+21, R 69+19 (unions 84/84/84/88
  exact, 0 overlap anywhere; b4/b5 in no const
  set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=100953 (PB0 sig 4b620100 NEW, b4/b5 b3/14 ==
  lencode), S1 n=100954 (fat PB1 sig 6197c402 NEW,
  b4/b5 b5/14 == lencode), A 100955-100970 PBA16
  single-sig (sig 608fd732, AM 16/16 distinct 9B,
  mtab b12,13,14,15,19,76,77,78,79, b5 const 14
  raw lencode), C 100971-100980 C10-MS 6-SIG (sig
  map exact order: bd7dc602 x3 @100971-73 +
  f5c1ce02/6517cb02/1dfac902/f5c1ce02/c5f9cd02/
  9d6fcf02/1dfac902 @100974-80 with repeats @977
  ==974 and @980 ==976, CM 10/10 distinct 13B
  diverge 10/10, mtab b0,1,2,11,18,19,20,21,22,
  80,81,82,83, sig-bytes-in-tab CC b0/b1/b2 VAR
  b3 const 02, b5 const 14), Q 100981-101044
  single-sig quad (sig 0080773c NEW, M8 b24,25,26,
  27,76,77,78,79 M16 16/16 distinct 8B, R7 b12,13,
  14,18,19,21,22 b20-SKIPPED verified first-hand
  (b20 const f2 via consts), r2==r3 PAIRED
  b20f76d47c32b9 x2 r0 32ce7f3478c7b0 distinct
  r1 b20f76d07c32b9 1B-off d0-vs-d4, tails 4/4
  049680e9/2930e3e7/45bd1e06/6fbd1e06, M-tails 16/16
  NEW vs P241M (0/16 vs P241T), QT overlap 0/4 vs
  P241T, b5-carry 14->15 @100991->100992 ff->01
  edge raw lencode), R 101045-101300 T88-ring
  STANDARD (sig 02000000 ==P234/235T NOT P241T per
  A-312 correction, M9 b18,19,27,34,35,80-83 by
  COL RM 16/16 distinct, R8 b28,29,30,31,76-79
  by ROW RQ 16/16 distinct UNPAIRED, tails SPLIT,
  b84-87 const 2771a8dd ring-wide, b4=(0x6b+2off)
  &FF, b5=0x15+(off>=75)+(off>=203)). C blocks carry
  T66453/458/463/T66478/494/T66517 py-line mirrors,
  bounds + byte positions exact, ring consts
  107/21/75/203, all 6 verified. Insert position
  exact both sides: after T10P241R close, at dispatch
  tail (N-out-of-scope fallthrough follows). Matches
  A-568 geometry (PB0/PB1 NEW, PBA16 VPOS 10 b5
  const 14, C10-MS 6-sig map VPOS 14 b5 const 14
  10/10 diverge, QUAD64 VPOS 21 b5-carry, T88 VPOS
  19, lencode 348/348 whole-tier, ring edges 101119->
  101120 + 101247->101248, NO D dips) incl exact
  values (QR r2==r3 pair, tails 4/4, M-tails 16/16
  NEW, ring M9/R8 16/16 UNPAIRED, tails SPLIT,
  b84-87 2771a8dd, consts stand).
- Tail-share figure: QT r2/r3 = 45bd1e06/6fbd1e06,
  byte0 0x45 vs 0x6f differ, common suffix 3B bd1e06
  — confirms A-568 §2 (TRUE 3B, memo re-verified
  programmatically; descriptive only, cut SAFE,
  no DISSENT; exact tail values CONFIRMED, pins PASS).
- Edges via counter formula first-hand: 101119 (off74,
  ff/15) -> 101120 (off75, 01/16); 101247 (off202,
  ff/16) -> 101248 (off203, 01/17); all four pins
  PASS. Q b5-carry pair 100991 (ff/14) -> 100992
  (01/15) both PASS. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del; raw
  grep 605 content + 5 blank-only `+` lines (verified
  bare) / 0 del; fine-norm (rgramc.c scope, TNP/_tN/
  _iN/_bN, BSD tools, empty-excluding) del-subset-add
  0 missing (del-uniq 0, add-uniq 397).
- Wall on band diff added lines (scope b3b974d6..
  20efeb92, 910 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/CT-shim/shebang/
  /usr/bin/aa/nominated 0 hits. Files touched: rgramc.c
  610/0, rgram.py +237/+0 purely additive,
  test_rgram.sh 1/1 (for-line extension), PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 516->518 +2 / ranges 420->424 +4 = +6
  (stated method, plain `if n ==` for BSD grep),
  seal 1434->1440 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-568-q634-
  t10p242 verdict CONFIRM (33/33 = 15/15 shape +
  10/10 quad/ring + 8/8 counters; file present,
  counts verified; exact-value corroboration incl
  QR pair, tails 4/4, M-tails NEW, ring edges +
  consts re-checked above; A-312 correction on ring
  sig corroborates). No CONFIRM-P242.md file; A-568
  suffices per rule. Agrees with cport commit msg
  (PYID 7060, RGRAM 14120).
- Quiz: no conflicting CLAIM/GATE/FLAG on b350. Newest
  PARENT-* is QNUM-11 (w2f Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r49/ (build350.log,
  pyid350.log, rgram350py/c.log, cmp350.py/.c, for350-
  20efeb92/b3b974d6, for350-added, pins350.basen,
  smoke350.log, tables350.log, tabc242.py, bycov242.py,
  bycov350.log, sig242.py/.log, numstat350,
  added350, add/delnorm350).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
