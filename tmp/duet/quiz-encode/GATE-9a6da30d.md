# GATE 9a6da30d b332 T10P224 pins 94689..95036 (1328 tiers) PASS-functional

Seat sweep2-r45, first-hand, WT tmp/wt-encode-sweep2 @9a6da30d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r45.
Band = 4c741ebb (py merge w2b@21b18db2 partial, +6 tiers, +52 pins)
+ 9a6da30d (C port). Base 6be444ff (b331 tip, 1322 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build332/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4652e61d / aae d6e27c97
  (aae identical to b288-b330 builds: aae.c untouched).
- RGRAMC-PYID 6524/6524 covered=6524/6524 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13048/13048 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 13048/13048 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 13048/13048).
- PINS-RGRAM cells set-eq 6524/6524 (diff 0, PINS base-N
  set vs for-list); PINS 13050 rows (2 hdr + 13048 =
  PASS lines). For-list union +26 (94689 94690 94691
  94698 94706 94707 94711 94716 94717 94719 94720
  94732 94733 94741 94748 94749 94757 94764 94765
  94780 94781 94847 94848 94975 94976 95036),
  0 removed. Each for-N yields 2 PASS lines (g-zN-closed
  + g-zN). The 26 = PB0/PB1 (2) + PBA16 edges + mid
  94698 (3) + PBB10 edges + mid 94711 (3) + quad head
  + carry pair 94719/94720 + mids + tail 94780 (12) +
  ring head + edge pairs 94847/94848 + 94975/94976 +
  tail 95036 (6).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P224 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, BM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 75/75, BC 71/71,
  QC 65/65, RC 69/69; C _N decls 75/71/65/69
  match actual (tabc224.py rc=0, tabc222 label-only,
  nothing else). Code-consts vs A-294 (PBA 76 /
  PBB 72 / quad 65 / T 69): quad + T exact; PBA/PBB
  -1 each is bookkeeping (b5 const e3 but checked via
  lencode formula, not const pairs — verified: b5 in
  var sets, 0 overlap, S0/S1 b5 == lencode first-hand);
  byte-coverage proven 84/84 all 4 groups: A 75+9,
  B 71+13, Q 65+19, R 69+15 (0 overlap anywhere;
  b4/b5 in no const set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=94689 (PB0 sig 1f120000 NEW, b4/b5 c3/e3 ==
  lencode), S1 n=94690 (fat PB1 sig fe042600 NEW,
  b4/b5 c5/e3 == lencode), A 94691-94706 PBA16
  (sig fe044602 NEW, AM 16/16 distinct, mtab b32-34,
  76-79, b5 const e3 raw lencode), B 94707-94716
  PBB10 single-sig (sig fe044e00 NEW, BM 10/10
  distinct, m-tab b22,23,30,31,36-38,80-83, b5 const
  e3 raw lencode), Q 94717-94780 QUAD (sig fe048604
  NEW, M6 b36,37,76-79 by m=off&15 M16 16/16
  distinct, R7 b22,23,30-34 r0==r1+r2==r3
  DOUBLE-PAIRED 2/4 distinct 01aae8f8749ec7 x2 /
  89b8ccf914329a x2, tails 4/4 70ec9d9c/9cec9d9c/
  09ee0259/38ee0259 with r0/r1 sharing last 3B
  ec9d9c + r2/r3 sharing ee0259, tails b80-83 by
  q=off>>4, b5-carry e3->e4 @94719->94720 ff->01
  raw lencode),
  R 94781-95036 T-ring STANDARD (sig 409dff48 NEW,
  M7 b35,42,43,76-79 by COL off&15, R6 b36,37,72-75
  by ROW off>>4 UNPAIRED 16/16 distinct, QM-heads
  16-set == TR-heads 16-set verified True first-hand,
  M-tails 16/16 NEW vs P223T, tails const ring-wide,
  b4=(0x7b+2off)&FF, b5=0xe4+(off>=67)+(off>=195)).
  C blocks carry T61855/860/865/880/896/919 py-line
  mirrors, bounds exact, ring consts 123/228 +
  thresholds 67/195, all 6 verified. Insert position
  exact both sides: after T10P223R close, at dispatch
  tail (N-out-of-scope fallthrough follows). Matches
  A-502 geometry (PB0 1f120000 NEW, PB1 fe042600
  NEW, PBA16 NEW VPOS 8 b5 const e3, PBB10
  single-sig VPOS 12 b5 const e3 10/10 diverge,
  QUAD64 VPOS 19 double-paired + carry e3->e4,
  T-ring VPOS 15 STANDARD UNPAIRED, lencode 348/348
  whole-tier, ring edges 94847->94848 + 94975->94976,
  NO D dips) and A-294 (double-pair exact, tails
  exact, B10M/QR share 8/11 corrected, B-only 36-38
  + Q-only 32-34, M-tails 16/16 NEW, consts stand).
- Quad b5-carry sides confirmed first-hand via the
  lencode formula: 94719 (off2, ff/e3) -> 94720
  (off3, 01/e4); both pins PASS. Ring edges via the
  counter formula: 94847 (off66, ff/e4) -> 94848
  (off67, 01/e5); 94975 (off194, ff/e5) -> 94976
  (off195, 01/e6); all four pins PASS. No DISSENT:
  cut bytes verify.
- C diff purely additive: numstat 606 add / 0 del; raw
  grep 601 add + 5 blank-only `+` lines (verified
  bare) / 0 del; fine-norm (_t/_i/_b/T numbers,
  TNP/TN, BSD-sed, sign-strip, empty-excluding)
  del-subset-add 0 missing (del-uniq 0, add-uniq 377).
- Wall on band diff added lines (scope 6be444ff..
  9a6da30d, 891 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/CT-shim/shebang/
  /usr/bin/aa/nominated 0 hits. Files touched: rgramc.c
  606/0, rgram.py +237/+0 purely additive,
  test_rgram.sh 1/1, PINS +52/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 480->482 +2 / ranges 322->326 +4 = +6
  (stated method; note BSD grep -E backslash-paren does
  not match literal paren, used plain `if n ==`),
  seal 1322->1328 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-502-q616-
  t10p224 verdict CONFIRM (28/28 = 14/14 shape +
  10/10 quad/ring + 4/4 counters; file present,
  counts verified; A-294 corroborates incl-consts
  with -1 bookkeeping resolved + B10M/QR 8/11 share
  + carry/ring edges re-checked above). No
  CONFIRM-P224.md file; A-502 suffices per rule.
  Agrees with cport commit msg (PYID 6524,
  RGRAM 13048).
- Quiz: no conflicting CLAIM/GATE/FLAG on b332. Newest
  PARENT-* is QNUM-07 (w2d Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r45/ (build332.log,
  pyid332.log, rgram332py/c.log, cmp332.py/.c, for332-
  6be444ff/9a6da30d, for332-added, pins332.csv/.basen,
  smoke332.log, tables332.log, tabc224.py, bycov224.py,
  sig224.py/.log, cdiff332, add/delnorm332,
  cdiff332.miss, banddiff332, added332, numstat332).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
