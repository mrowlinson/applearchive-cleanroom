# GATE 3cb4aae3 b336 T10P228 pins 96081..96428 (1353 tiers) PASS-functional

Seat sweep2-r46, first-hand, WT tmp/wt-encode-sweep2 @3cb4aae3,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r46.
Band = 39638d99 (py merge w2b@e62c259e partial, +7 tiers, +56 pins)
+ 3cb4aae3 (C port). Base b85ccf4c (b335 tip, 1346 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build336/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 68eb1ff2 / aae d6e27c97
  (aae identical to b288-b334 builds: aae.c untouched).
- RGRAMC-PYID 6630/6630 covered=6630/6630 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13260/13260 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 13260/13260 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 13260/13260).
- PINS-RGRAM cells set-eq 6630/6630 (diff 0, PINS base-N
  set vs for-list); PINS 13262 rows (2 hdr + 13260 =
  PASS lines). For-list union +28 (96081 96082 96083
  96090 96098 96099 96100 96101 96104 96108 96109
  96116 96117 96124 96125 96127 96128 96140 96141
  96172 96173 96255 96256 96300 96301 96383 96384
  96428), 0 removed. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 28x2 = 56 = 13260-13204. The
  28 = PB0/PB1 (2) + PBA head/mid/tail (3) + PAIR (2)
  + PBC head/mid/tail (3) + QUADhalf head/mids/
  carry-edge/mids/tail (10) + ring head/edge-pairs/
  flip-edge/tail (8).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P228 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, CM 8/8, M 16/16, PT 2/2,
  QR 4/4, QT 4/4, RF 2/2, RM 16/16, RQ 16/16,
  AC 74/74, CC 72/72, PC 81/81, QC 63/63,
  RC 65/65; C _N decls 74/72/81/63/65
  match actual (tabc228.py rc=0, tabc226 + CM/PT/RF
  tuples + CC/PC pair lists for the novel PBC/PAIR
  tier, nothing else). Code-consts vs
  A-298 (PBA 75 / PBC 73 / PAIR 82): impl -1 each
  is bookkeeping (b5 const ee but checked via lencode
  formula, not const pairs — verified: b5 in var
  sets, 0 overlap, S0/S1 b5 == lencode ee
  first-hand, lencode b5 const ee across A/P/C
  ranges); byte-coverage proven 84/84 all 5 groups:
  A 74+10, P 81+3, C 72+12, Q 63+21,
  R 65+19 (0 overlap anywhere; b4/b5 in no const
  set).
- Dispatch eye-verified both sides, 7 blocks in order:
  S0 n=96081 (PB0 sig 794b0000 NEW, b4/b5 a3/ee ==
  lencode), S1 n=96082 (fat PB1 sig 8e638e00 NEW,
  b4/b5 a5/ee == lencode), A 96083-96098 PBA16
  (sig ee38e608, AM 16/16 distinct, mtab b6-9,
  76-79, b5 const ee raw lencode), P 96099-96100
  PAIR (sig 4a329d00 NEW, PT 2/2 distinct 94/b4,
  1B b80 tab), C 96101-96108 PBC8 (sig 25994e00
  NEW, CM 8/8 distinct 10B, mtab b6,7,48-51,
  80-83, b5 const ee raw lencode),
  Q 96109-96172 QUADhalf (row sigs 3093e904/
  2693e904 via b0 half-split m0-7 0x30 x8 /
  m8-15 0x26 x8 all 4 rows, M9 b0,9-12,76-79
  M16 16/16 distinct, R6 b6,7,48-51 UNPAIRED
  4/4 distinct 22a57cd8a949/30b9545da42e/
  c69b71dfe16f/408a7c587091, tails 4/4
  4168ea6b/62116d6a/8bedcfaf/2a97368f max-common-
  suffix 0B, b5-carry @96127->96128),
  R 96173-96428 T-ring DUAL (sigs f032994e/
  e632994e, RF 2/2 f035/e655 flips b0 f0/e6 +
  b12 35/55 @off128 = 96300->96301, M8 b16-19,
  72-75 by COL RM 16/16 distinct, R7 b9-11,
  76-79 by ROW RQ 16/16 distinct UNPAIRED,
  M-tails 16/16 NEW vs P227M, QT overlap 0/4
  vs P227T, tails SPLIT b72-75 col + b76-79
  row NOT const, b80-83 const ring-wide,
  b4=(0x5b+2off)&FF,
  b5=0xef+(off>=83)+(off>=211)).
  C blocks carry T62922/927/932/947/961/977/001 py-line
  mirrors, bounds + byte positions exact, ring consts
  91/239 + thresholds 83/211, all 7 verified. Insert
  position exact both sides: after T10P227R close, at
  dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-518 geometry (PB0 794b0000 NEW, PB1
  8e638e00 NEW, PBA16 VPOS 9 b5 const ee, PAIR VPOS
  {b4,b80}, PBC8 VPOS 11 b5 const ee, QUADhalf VPOS
  21 b0 half-split + b5-carry edge, T-ring DUAL VPOS
  19 half-flips @off128, lencode 348/348 whole-tier,
  ring edges 96255->96256 + 96383->96384, NO D dips)
  and A-298 (R6 4/4 exact values, tails 4/4 exact,
  M-tails 16/16 NEW, ring M8/R7 16/16 UNPAIRED,
  tails SPLIT, b80-83 const, consts stand).
- Edges via formulas first-hand: Q carry 96127
  (ff/ee) -> 96128 (01/ef); ring 96255 (off82,
  ff/ef) -> 96256 (off83, 01/f0); 96383 (off210,
  ff/f0) -> 96384 (off211, 01/f1); all six pins
  PASS. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 733 add / 0 del; raw
  grep 727 add + 6 blank-only `+` lines (verified
  bare) / 0 del; fine-norm (_t/_i/_b/T numbers,
  BSD-sed, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 426).
- Wall on band diff added lines (scope b85ccf4c..
  3cb4aae3, 1060 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/CT-shim/shebang/
  /usr/bin/aa/nominated 0 hits. Files touched: rgramc.c
  733/0, rgram.py +276/+0 purely additive,
  test_rgram.sh 1/1, PINS +56/+0.
- Tiers: merge-msg +7, code 7 blocks, dispatch-guards
  singletons 488->490 +2 / ranges 360->365 +5 = +7
  (stated method, plain `if n ==` for BSD grep),
  seal 1346->1353 +7: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-518-q620-
  t10p228 verdict CONFIRM (30/30 = 15/15 shape +
  11/11 quad/ring + 4/4 counters; file present,
  counts verified; A-298 corroborates incl-consts
  with -1 x3 bookkeeping resolved + R6/tails exact
  values + ring edges re-checked above). No
  CONFIRM-P228.md file; A-518 suffices per rule.
  Agrees with cport commit msg (PYID 6630,
  RGRAM 13260).
- Quiz: no conflicting CLAIM/GATE/FLAG on b336. Newest
  PARENT-* is QNUM-09 (w2e Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r46/ (build336.log,
  pyid336.log, rgram336py/c.log, cmp336.py/.c, for336-
  b85ccf4c/3cb4aae3, for336-added, pins336.csv/.basen,
  smoke336.log, tables336.log, tabc228.py, bycov228.py,
  bycov336.log, sig228.py/.log, banddiff336, added336,
  numstat336, add/delnorm336).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
