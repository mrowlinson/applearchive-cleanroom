# GATE ae8c351d b330 T10P222 pins 93993..94340 (1316 tiers) PASS-functional

Seat sweep2-r44, first-hand, WT tmp/wt-encode-sweep2 @ae8c351d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r44.
Band = da8f64ae (py merge w2b@0c767190 partial, +6 tiers, +52 pins)
+ ae8c351d (C port). Base 1c52e56f (b329 tip, 1310 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build330/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 16229ff1 / aae d6e27c97
  (aae identical to b288-b328 builds: aae.c untouched).
- RGRAMC-PYID 6472/6472 covered=6472/6472 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 12944/12944 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 12944/12944 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 12944/12944).
- PINS-RGRAM cells set-eq 6472/6472 (diff 0, PINS base-N
  set vs for-list); PINS 12946 rows (2 hdr + 12944 =
  PASS lines). For-list union +26 (93993 93994 93995
  94002 94010 94011 94015 94020 94021 94029 94036 94037
  94045 94052 94053 94068 94069 94079 94080 94084 94085
  94207 94208 94335 94336 94340),
  0 removed. Each for-N yields 2 PASS lines (g-zN-closed
  + g-zN). The 26 = PB0/PB1 both cells (2) + PBA16 edges
  + mid 94002 (3) + PBB10 edges + mid 94015 (3) + quad
  row edges + carry pair 94079/94080 (12) + ring start
  + edge pairs 94207/94208 + 94335/94336 + tail 94340
  (6).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P222 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, BM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 74/74, BC 70/70,
  QC 61/61, RC 67/67; C _N decls 74/70/61/67
  match actual (tabc222.py rc=0, tabc216 label-only,
  nothing else). Code-consts vs A-292 (PBA 75 /
  PBB 71 / quad 61 / T 67): quad + T exact; PBA/PBB
  -1 each is bookkeeping (b5 const but checked via
  lencode formula, not const pairs); byte-coverage
  proven 84/84 all 4 groups: A 74+10, B 70+14,
  Q 61+23, R 67+17 (0 overlap anywhere; b4/b5 in no
  const set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=93993 (PB0 sig 17120000 NEW, b4/b5 53/de ==
  lencode), S1 n=93994 (fat PB1 sig 3a822100 ==P221B10,
  b4/b5 55/de == lencode), A 93995-94010 PBA16
  (sig 3a820102 NEW, AM 16/16 distinct, mtab b34,35,
  42,43,76-79, b5 const de raw lencode), B 94011-94020
  PBB10 single-sig (sig 3a822100 ==PB1, BM 10/10
  distinct, m-tab b34,35,41-46,80-83 == quad-R
  set-exact BM12==QR8+tails verified True, b5 const
  de raw lencode), Q 94021-94084 QUAD (sig 3a824102
  ==P221Q, M9 b47-51,76-79 by m=off&15 shared 16/16
  x3, R8 b34,35,41-46 r2==r3 PAIRED 2e7b899abfd3e438
  x2 3/4 distinct, tails 4/4 09bb7378/d1f01af7/
  b6f9d055/472ce255 with r2/r3 sharing last 1B 55,
  tails b80-83 by q=off>>4, b5-carry de->df ff->01
  @94079->94080 raw lencode),
  R 94085-94340 T-ring STANDARD (sig ae231824 NEW,
  M6 b6,7,76-79 by COL off&15, R9 b47-51,72-75 by ROW
  off>>4 UNPAIRED 16/16 distinct, QM-heads 16-set ==
  TR 16-set verified True first-hand, M-tails 16/16
  NEW vs P221T, tails const ring-wide, b4=(0x0b+2off)
  &FF, b5=0xdf+(off>=123)+(off>=251)).
  C blocks carry T61382/387/392/407/423/446 py-line
  mirrors, bounds exact, ring consts 11/223 +
  thresholds 123/251, all 6 verified. Insert position
  exact both sides: after T10P221R close, at dispatch
  tail (N-out-of-scope fallthrough follows). Matches
  A-499 geometry (PB0 17120000 NEW, PB1 3a822100
  ==P221B10, PBA16 NEW VPOS 9 b5 const de, PBB10
  single-sig VPOS 13 b5 const de 10/10 diverge,
  QUAD64 VPOS 23 + carry de->df, T-ring VPOS 17
  STANDARD UNPAIRED, lencode 348/348 whole-tier, ring
  edges 94207->94208 + 94335->94336, NO D dips) and
  A-292 (M9 shared, R8 paired exact, tails exact,
  PBB positions == quad-R set-exact, M-tails 16/16
  NEW, consts stand).
- Quad b5-carry sides confirmed first-hand via the
  lencode formula: 94079 (off58, ff/de) -> 94080
  (off59, 01/df); both pins PASS. Ring edges via the
  counter formula: 94207 (off122, ff/df) -> 94208
  (off123, 01/e0); 94335 (off250, ff/e0) -> 94336
  (off251, 01/e1); all four pins PASS. No DISSENT:
  cut bytes verify.
- C diff purely additive: numstat 606 add / 0 del; raw
  grep 606 add / 0 del (5 blank-only `+` lines,
  verified bare; 0 del); fine-norm (_t/_i/_b/T
  numbers, BSD-sed, sign-strip, empty-excluding)
  del-subset-add 0 missing (del-uniq 0, add-uniq 371).
- Wall on band diff added lines (scope 1c52e56f..
  ae8c351d, 896 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/CT-shim/shebang/
  /usr/bin/aa/nominated 0 hits. Files touched: rgramc.c
  606/0, rgram.py +237/+0 purely additive,
  test_rgram.sh 1/1, PINS +52/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  780->786 +6 (stated method: ^    if (n == / N <= n
  in rgram.py), seal 1310->1316 +6: all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-499-q614-
  t10p222 verdict CONFIRM (28/28 = 14/14 shape +
  10/10 quad/ring + 4/4 counters; file present,
  counts verified; A-292 corroborates incl-consts
  with -1 bookkeeping resolved + PBB==quad-R set-claim
  + carry/ring edges re-checked above). No
  CONFIRM-P222.md file; A-499 suffices per rule.
  Agrees with cport commit msg (PYID 6472,
  RGRAM 12944).
- Quiz: no conflicting CLAIM/GATE/FLAG on b330. Newest
  PARENT-* is QNUM-06 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r44/ (build330.log,
  pyid330, rgram330py/c.log, cmp330.py/.c, for330-
  1c52e56f/ae8c351d, for330-added, pins330.csv/.basen,
  smoke330, tables330.log, tabc222.py, bycov222.py,
  sig222.py/.log, cdiff330, add/delnorm330,
  cdiff330.miss, banddiff330, added330, numstat330).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
