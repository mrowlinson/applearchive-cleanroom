# GATE 6be444ff b331 T10P223 pins 94341..94688 (348 pins) PASS-functional

Seat sweep-r44, first-hand, WT tmp/wt-encode-sweep @6be444ff,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r44.
Band = c9fcc2fb (py merge w2b@f8d57674 partial, +6 tiers
+52 pins) + 6be444ff (C port). Base ae8c351d (b330 tip,
1316 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build331/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r44), rgramc f78eeb25.
- RGRAMC-PYID 6498/6498 covered=6498/6498 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12996/12996 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12996/12996 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12996/12996, version-sorted).
- PINS-RGRAM cells set-eq 12996/12996 (cmp-equal).
  PINS base-N vs for-list 6498/6498 exact.
- PINS 12998 rows (2 hdr + 12996, +52 vs base 12946). py diff
  +52/-0 (pure P223 addition); test_rgram.sh 1/1 (for-line).
  For-list union +26 (94341 94342 94343 94344 94351 94358
  94359 94363 94368 94369 94377 94384 94385 94393 94400
  94401 94416 94417 94425 94432 94433 94463 94464 94591
  94592 94688), 0 removed: 2 sing + A 4 + B 3 + Q 11 +
  R 6 (ring edges 94463/94464 + 94591/94592 + tail 94688).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P223 C-vs-py, 13-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 17120000 / 5c1f1200);
  AM 16/16, BM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16 EXACT;
  AC 73/73, BC 71/71, QC 64/64,
  RC 65/65 EXACT (py-hex vs C-decimal
  normalized);
  C _N decls 73/71/64/65 match actual;
  TABAUDIT-GREEN rc=0. No _T10P223PT/PC/CM/CC/FM/FC/FS/FO/H/TC*
  symbols either side (split-sig A + classic single-sig B,
  NO PAIR/C8/FRAG, grep-verified inventory).
  Excl-b4/b5 accounting: b4/b5 in no const table (False x4).
  Missing-sets first-hand EXACT: AC-11 [0,4,5,9,10,11,12,
  76,77,78,79] = VPOS 10 (b4+M9 b0,9-12,76-79) + b5-const;
  BC-13 [4,5,13,14,15,16,17,18,19,80,81,82,83] = VPOS 12
  (b4+M11 b13-19,80-83) + b5-const;
  QC-20 [4,5,13-22,76-83] = VPOS 19 (b4+M7 b20-22,76-79
  + R11 b13-19,80-83) + b5-const;
  RC-19 [4,5,12,13,14,19,20,21,25,26,27,72-79] = VPOS 19
  (b4,b5+M9 b20,21,25-27,76-79 + R8 b12-14,19,72-75).
  Code 73/71/64/65; incl = +1/+1/+1/+0 (b5 const e1
  verified first-hand over all 92 head cells 94341..94432,
  T +0 counter) = 74/72/65/65 = A-293 consts EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + 4 tiers): P2230 n==94341 / P2231 n==94342
  singleton-const (offs 0/1);
  P223A 94343..94358 off=n-94343 split-sig (cell0 1ef42101
  + 00f42101 x15, m-tab 9B b0,9-12,76-79 covers split);
  P223B 94359..94368 off=n-94359 single-sig 813e2400
  (m-tab 11B b13-19,80-83);
  P223Q 94369..94432 off=n-94369 m=off&15 q=off>>4
  single-sig 1de84302 r2==r3 paired (M 7B b20-22,76-79
  + QR 7B b13-19 + QT b80-83);
  P223R(T-ring) 94433..94688 off=n-94433 c=off&15
  r=off>>4 STANDARD sig 20827f28 (RM 9B b20,21,25-27,
  76-79 by COL + RQ 8B b12-14,19,72-75 by ROW);
  all paylen 84; A/B/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0xc3+2off)&FF
  b5=0xe1+(off>=31)+(off>=159).
  C blocks carry T61618/623/628/643/659/682 py-line
  mirrors (exact); C byte-index lists match py per
  block; insert position exact (dispatch
  tail, N out-of-scope follows).
  Value checks first-hand: AM0 1ea08657957a2f9bd3
  (b0=1e b12=95) vs rest b0=00 b12=b5, AM 16 distinct;
  BM 10/10 distinct; M 16/16; QR r2==r3 PAIRED
  e6fc877a5b8d9c x2, 3/4 distinct (r0 11fc431add39a7,
  r1 cc7c22fa9282a3); QT 4/4 distinct 7f7a1c5f/
  5dfc677c/d8397426/073a7426, r2/r3 share last 2B 7426;
  RM 16/16 + RQ 16/16 UNPAIRED distinct;
  M-tails 0/16 vs P222RM ALL NEW (QT 0/4 vs P222QT).
  Counter edges computed first-hand (never trusted
  from comments): head b5 const e1 (n=94341 0b/e1,
  n=94432 c1/e1, no carry in range);
  T off30 ff/e1 -> off31 01/e2 (94463->94464) +
  off158 ff/e2 -> off159 01/e3 (94591->94592).
  All edge pins PASS (batteries GREEN).
  Matches A-501/A-293 geometry (PB0 17120000 REPEAT,
  PB1 5c1f1200 NEW, PBA split-sig cell0 1ef42101 +
  00f42101 x15 VPOS 10 b0/b12 cell0-only 1e/95 vs
  00/b5 b5 const e1, PBB10 single-sig 813e2400 VPOS 12
  == quad-R positions 10/10 diverge NO PAIR/C8,
  QUAD64 M7 shared + R7 r2==r3 PAIRED 3/4 +
  tails 4/4 r2/r3 share 7426, T-ring STANDARD M9 by COL
  + R8 by ROW UNPAIRED 16/16, M-tails ALL NEW 0/16,
  ring edges + thresholds 31/159, NO D dips).
- C diff pure-add: numstat 606/0; raw 606 add / 0 del
  (607/1 incl diff headers; 5 blank-plus, 0 blank-minus);
  normalized ([0-9]+ -> N, cut-c2 strip, sort -u)
  del-subset-add 0 missing (del-uniq 0, add-uniq 175).
- Wall on band diff added lines (scope ae8c351d..6be444ff,
  895 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression/CT-shim/shebang//usr/bin/aa/
  nominated 0 hits. Files touched: rgramc.c 606/0,
  rgram.py 236/0, test_rgram.sh 1/1 (for-line), PINS 52/0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  786->792 +6/0rm (stated method, literal `if n ==` form;
  one scratch pattern slip self-caught pre-filing, never
  filed), seal 1316->1322 +6: all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-501-q617
  T10P223 predictive reproduces 30/30 (shape 16/16 +
  quad+Tring 10/10 + counters 4/4 CONFIRM) + A-293
  corroborates same tier (shape + quad/ring + tails
  + T-ring + edges CONFIRM, incl consts 74/72/65/65,
  NO D dips). No DISSENT on P223 (only P923/P924/P926,
  other turf, rebuttals filed). Agrees with cport commit
  msg (py/C 12996, PYID 6498).
- Quiz: no conflicting CLAIM/GATE/FLAG on b331/6be444ff.
  b330 EVEN = sweep2 turf (GATE-ae8c351d filed by
  sweep2-r44), used as diff-base only, NOT gated.
  Newest PARENT-* is QNUM-07 (w2d Q-block only, read,
  no gate impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r44/ (*331* files:
  build331.log, pyid331, rgram331py/c, pass331py/c,
  cells331-battery, pins330base/pins331-cells/-nums,
  for331-old/-new.nums, guards331-old/-new, smoke331.log,
  tables331.log, tabaudit331.py, sigcheck331.py/.log,
  verify331.py/.log, cdiff331.txt/-del-norm/
  -add-norm/-missing, banddiff331.txt, added331.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
