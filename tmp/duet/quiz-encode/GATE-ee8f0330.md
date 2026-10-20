# GATE ee8f0330 b337 T10P229 pins 96429..96776 (348 pins) PASS-functional

Seat sweep-r45, first-hand, WT tmp/wt-encode-sweep @ee8f0330,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r45.
Band = 6c4c75bd (py merge w2b@0461e11b partial, +7 tiers
+58 pins) + ee8f0330 (C port). Base 3cb4aae3 (b336 tip,
1353 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build337/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r45), rgramc 37aa9f09.
- RGRAMC-PYID 6659/6659 covered=6659/6659 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 13318/13318 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 13318/13318 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (13318/13318, version-sorted).
- PINS-RGRAM cells set-eq 13318/13318 (cmp-equal).
  PINS base-N vs for-list 6659/6659 exact.
- PINS 13320 rows (2 hdr + 13318, +58 vs base 13262). py diff
  +58/-0 (pure P229 addition); test_rgram.sh 1/1 (for-line).
  For-list union +29 (96429 96430 96431 96438 96446 96447
  96448 96449 96452 96456 96457 96464 96472 96473 96480
  96488 96489 96496 96504 96505 96511 96512 96520 96521
  96639 96640 96767 96768 96776), 0 removed: 2 sing +
  A 3 (head 96431 + mid 96438 + tail 96446) + P 2 (both
  96447/96448) + C 3 (head 96449 + mid 96452 + tail 96456) +
  Q 13 (all 4 rows: q0 off0/7/15, q1 off16/23/31,
  q2 off32/39/47, q3 off48/54/55(carry pair)/63) + R 6
  (head 96521 +
  edge pairs 96639/96640 + 96767/96768 + tail 96776).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P229 C-vs-py, 17-table PAIR/C8 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 994e0000 / e6969900);
  AM 16/16, PT 2/2, CM 8/8, M 16/16, M31 16/16, XA 4/4,
  QR 4/4, QT 4/4, RM 16/16, RQ 16/16 EXACT;
  AC 76/76, PC 79/79, CC 69/69, QC 63/63, RC 66/66 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/79/69/63/66 match actual;
  TABAUDIT-GREEN rc=0. No BM/BC/FM/FS/FO/FC/X42/M42
  (B replaced by PAIR+C8, no FRAG), grep-verified 0/0
  both sides; table inventory exactly the 17.
  Excl-b4/b5 accounting: b4/b5 in no const table (False x5).
  Missing-sets first-hand EXACT: AC-8 [4,5,24,25,76,77,
  78,79] = b4+b5-const+M6 (b24,25,76-79) = VPOS 7;
  PC-5 [4,5,80,81,82] = b4+b5-const+PAIR (b80-82)
  = VPOS 4 (b83 const 0x60 in-table, verified);
  CC-15 [4,5,20,21,25,26,27,28,29,30,31,80,81,82,83]
  = b4+b5-const+M13 (b20,21,25-31,80-83) = VPOS 14;
  QC-21 [4,5,21,22,23,24,25,26,27,28,29,30,31,76,77,78,
  79,80,81,82,83] = b4,b5+M7 (b21-23,76-79)+R7 (b24-30)
  +b31+T4 (b80-83) = VPOS 21;
  RC-18 [4,5,21,22,23,31,32,33,38,39,72,73,74,75,76,77,
  78,79] = VPOS 18 (b4,b5+M8 b32,33,38,39,72-75 + R8
  b21-23,31,76-79).
  b0-3 first-hand: AC e696d109, PC 32f79900, CC 32f74900,
  QC 32f7c107, RC e096d758.
  Code AC76/PC79/CC69/QC63/RC66; incl = +1/+1/+1/+0/+0
  (A/P/C b5 const f1, Q b5 varies carry, T counter)
  = 77/80/70/63/66; lane consts 77/70/63/66 = A-521/
  A-299 EXACT (pair PC informally 80, P219 analog).
  Dispatch verified by eye both sides, all 7 blocks
  (2 sing + A/P/C/Q/R): P2290 n==96429 / P2291 n==96430
  singleton-const (offs 0/1);
  P229A 96431..96446 off=n-96431 sig e696d109 NEW
  (m-tab 6B b24,25,76-79);
  P229P 96447..96448 off=n-96447 PAIR-3T sig 32f79900 NEW
  (ttab 3B b80-82 + consts incl b83=0x60);
  P229C 96449..96456 off=n-96449 PBC8 sig 32f74900 NEW
  (m-tab 13B b20,21,25-31,80-83);
  P229Q 96457..96520 off=n-96457 m=off&15 q=off>>4
  single-sig quad 32f7c107 r0==r2 (M 7B b21-23,76-79 +
  b31 row-add A=[0,1,0,0] vs M31[m] + R7 7B b24-30
  + QT b80-83);
  P229R(T-ring) 96521..96776 off=n-96521 c=off&15
  r=off>>4 STANDARD sig e096d758 NEW (RM 8B b32,33,38,39,
  72-75 by COL + RQ 8B b21-23,31,76-79 by ROW);
  all paylen 84; A/P/C/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0x13+2off)&FF
  b5=0xf2+(off>=119)+(off>=247).
  C blocks carry T63215/63220/63225/63240/63254/63270/
  63295 py-line mirrors (exact); guards
  `if ((n) == (96429))` / `if ((n) == (96430))` + 5 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; b31add via
  snprintf %02lx (pay[31]-hexval(XA[q]))&0xFF; counter
  19/242+(off>=119)+(off>=247); temps _t4896.._t4917
  appended (base max _t4895, no reuse);
  C byte-index lists match py per block; insert position
  exact (dispatch tail, N out-of-scope follows).
  Value checks first-hand: PT 2/2 distinct (5c640f/
  ed0d10); CM 8/8 distinct; M 16/16; M31 16/16
  distinct; XA 00,01,00,00; row-add 32/32 distinct
  values over 64 cells;
  QR r0==r2 EVEN-PAIRED 3/4 (fabc851eb404f9 x2; r1
  883c9428f4411d, r3 da7c90ed7471c8 distinct);
  QT 4/4 distinct exact (d08feaa6/29215901/2690eaa6/
  26d52267); QT r0/r2 common suffix eaa6 2B (byte1 8f
  vs 90) = A-521 §F correction, confirmed first-hand
  from table values (over A-299 3B note);
  RM 16/16 + RQ 16/16 UNPAIRED distinct;
  M-tails 0/16 vs P228RM ALL NEW (QT 0/4 vs P228QT).
  Counter edges computed first-hand (never trusted
  from comments): head b5 f1 x83 (96429..96511) then
  f2 x9 (96512..96520); Q carry 96511 ff/f1 ->
  96512 01/f2; T off118 ff/f2 -> off119 01/f3
  (96639->96640) + off246 ff/f3 -> off247 01/f4
  (96767->96768). All edge pins in for-list + PASS
  (batteries GREEN).
  Matches A-521/A-299 geometry (PB0 994e0000 NEW, PB1
  e6969900 NEW, PBA e696d109 VPOS 7 b5 const f1,
  PAIR-3T 32f79900 VPOS {b4,b80-82} + b83 0x60,
  PBC8 32f74900 VPOS 14 b5 const f1, QUAD single-sig
  32f7c107 VPOS 21 + row-add A=[0,1,0,0] 32 distinct +
  R7 r0==r2 EVEN-PAIRED 3/4 + tails 4/4 + carry f1->f2,
  T-ring STANDARD M8 by COL + R8 by ROW UNPAIRED 16/16
  + tails SPLIT + b80-83 const + M-tails ALL NEW 0/16,
  ring edges + thresholds 119/247, NO D dips).
- C diff pure-add: numstat 752/0 rgramc.c + 291/0 rgram.py
  (+1/-1 for-line, +58/0 PINS); raw C 752 add / 0 del
  (753 incl +++ header); normalized ([0-9]+ -> N,
  cut-c2 strip, trailing-';' strip, sort -u)
  del-subset-add 0 missing (del-uniq 0, add-uniq 194).
- Wall on band diff added lines (scope 3cb4aae3..ee8f0330,
  1102 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 752/0,
  rgram.py 291/0, test_rgram.sh 1/1 (for-line), PINS 58/0.
- Tiers: merge-msg +7, code 7 blocks, tier-tags +7/0rm
  (1257->1264), singletons `if n == ` 490->492 +2/0rm,
  range-guards 365->370 +5/0rm, CLOSED prints 1259->1266
  +7: all agree (stated literal methods, first-hand).
- CONFIRM evidence (CONVERT-01 rule b): A-521-q621
  T10P229 predictive reproduces 33/34 + finding (shape
  15/15 + quad+Tring 10/11 + counters 8/8 CONFIRM; §F
  tail-share 2B descriptive, cut SAFE, states no
  DISSENT) + A-299-q293 corroborates same tier (shape +
  quad/ring + counters + consts 77/70/63/66 CONFIRM,
  b83 0x60 + PBA 77 + PBC 70 fixes; QT r0/r2 share taken
  as A-521's corrected 2B eaa6, verified first-hand).
  No DISSENT on P229. Agrees with cport commit
  msg (py/C 13318, PYID 6659).
- Quiz: no conflicting CLAIM/GATE/FLAG on b337/ee8f0330.
  b336 EVEN = sweep2 turf (tip 3cb4aae3), used as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-09
  (w2e Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r45/ (*337* files:
  build337.log, pyid337, rgram337py/c, pass337py/c,
  cells337-battery, pins336base/pins337-cells/-nums,
  -baseN, for337-old/-new.nums, tiers336/337, smoke337.log,
  tables337.log, tabaudit337.py, sigcheck337.py/.log,
  verify337.py/.log, cdiff337.txt/-del-norm/
  -add-norm/-missing, banddiff337.txt, added337.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
