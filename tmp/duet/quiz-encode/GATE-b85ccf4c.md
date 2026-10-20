# GATE b85ccf4c b335 T10P227 pins 95733..96080 (348 pins) PASS-functional

Seat sweep-r45, first-hand, WT tmp/wt-encode-sweep @b85ccf4c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r45.
Band = 9af40a73 (py merge w2b@953bd5e5 partial, +6 tiers
+52 pins) + b85ccf4c (C port). Base 45854a24 (b334 tip,
1340 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build335/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r45), rgramc 08a003c4.
- RGRAMC-PYID 6602/6602 covered=6602/6602 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 13204/13204 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 13204/13204 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (13204/13204, version-sorted).
- PINS-RGRAM cells set-eq 13204/13204 (cmp-equal).
  PINS base-N vs for-list 6602/6602 exact.
- PINS 13206 rows (2 hdr + 13204, +52 vs base 13154). py diff
  +52/-0 (pure P227 addition); test_rgram.sh 1/1 (for-line).
  For-list union +26 (95733 95734 95735 95743 95744 95750
  95751 95753 95754 95760 95761 95771 95772 95777 95788
  95793 95804 95809 95820 95824 95825 95871 95872 95999
  96000 96080), 0 removed: 2 sing + A 4 (head 95735 +
  carry pair 95743/95744 + tail 95750) + B 4 (96-head
  95751 + 96-tail 95753 + 4e-head 95754 + tail 95760) +
  Q 10 (all 4 rows q0-q3: off0/10/11, off16/27, off32/43,
  off48/59/63) + R 6 (head 95825 + edge pairs 95871/95872
  + 95999/96000 + tail 96080).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P227 C-vs-py, 15-table classic-B layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs bf250000 / 8e634e00);
  AM 16/16, BM 10/10, M 16/16, X42 4/4, M42 16/16,
  QR 4/4, QT 4/4, RM 16/16, RQ 16/16 EXACT;
  AC 76/76, BC 64/64, QC 63/63, RC 65/65 EXACT (py-hex vs
  C-decimal normalized);
  C _N decls 76/64/63/65 match actual;
  TABAUDIT-GREEN rc=0. No PT/PC/CM/CC/FS/FO/FM/FC
  (NO PAIR/C8/FRAG), grep-verified 0/0 both sides;
  table inventory exactly the 15.
  Excl-b4/b5 accounting: b4/b5 in no const table (False x4).
  Missing-sets first-hand EXACT: AC-8 [4,5,36,37,76,77,
  78,79] = VPOS 8 (b4,b5+M6 b36,37,76-79);
  BC-20 [2,4,5,23,32,33,34,35,36,37,38,39,40,41,42,43,
  80,81,82,83] = {b4}+b5-const+M18 (b2,23,32-43,80-83)
  = VPOS 19 joint;
  QC-21 [2,4,5,34,35,36,37,38,39,40,41,42,43,76,77,78,
  79,80,81,82,83] = b4+b5-const+M8 (b2,34,35,43,76-79)
  +R6 (b36-41)+b42+T4 (b80-83) = VPOS 20 ex-b5;
  RC-19 [4,5,14,34,35,42,43,48,49,50,51,72,73,74,75,76,
  77,78,79] = VPOS 19 (b4,b5+M8 b48-51,76-79 + R9 b14,
  34,35,42,43,72-75).
  b0-3 first-hand: AC 8e63b604, BC 8e63??00 (b2 sig byte
  in tab), QC 8e63??04 (b2 sig-led col), RC a0990745.
  Code AC76/BC64/QC63/RC65; incl = +0/+1/+1/+0
  (A b5 varies carry, B/Q b5 const ec, T counter)
  = 76/65/64/65 = A-297 consts EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/B/Q/R): P2270 n==95733 / P2271 n==95734
  singleton-const (offs 0/1);
  P227A 95735..95750 off=n-95735 sig 8e63b604 NEW
  (m-tab 6B b36,37,76-79, b5-carry via raw lencode);
  P227B 95751..95760 off=n-95751 PBB10 2-sig (m-tab 18B
  b2,23,32-43,80-83, sig byte in tab);
  P227Q 95761..95824 off=n-95761 m=off&15 q=off>>4
  QUADmotif 2-sig ee04/f604 (M 8B b2,34,35,43,76-79 +
  b42 row-xor X=[00,03,05,04] vs M42[m] + R6 6B b36-41
  + QT b80-83);
  P227R(T-ring) 95825..96080 off=n-95825 c=off&15
  r=off>>4 STANDARD sig a0990745 (RM 8B b48-51,76-79
  by COL + RQ 9B b14,34,35,42,43,72-75 by ROW);
  all paylen 84; A/B/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0xa3+2off)&FF
  b5=0xec+(off>=47)+(off>=175).
  C blocks carry T62661/62666/62671/62686/62703/62728
  py-line mirrors (exact); guards `if ((n) == (95733))` /
  `if ((n) == (95734))` + 4 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; b42xor via
  snprintf %02lx pay[42]^hexval(X42[q]); counter
  163/236+(off>=47)+(off>=175); temps _t4854.._t4873
  appended (base max _t4853, no reuse);
  C byte-index lists match py per block; insert position
  exact (dispatch tail, N out-of-scope follows).
  Value checks first-hand: BM 10/10 distinct, order 96x3
  @95751,52,53 + 4ex7 @95754..95760 (4e group ==PB1);
  M 16/16, sig-led col b2 ee x11 (cols 0-10) / f6 x5
  (cols 11-15); X42 00,03,05,04; M42 16/16, lows set 7
  (1c/3c/5c/7c/9c/bc/dc); row-xor 16/16 cols
  all-4-distinct (c,c^3,c^5,c^4);
  QR UNPAIRED 4/4 exact (cb5bae95f046/9b5a58ebb025/
  dddb554c10a8/46de61cff06d); QT 4/4 distinct exact
  (4b696cac/f3c5f3b1/bd589836/5c9fa7af);
  RM 16/16 + RQ 16/16 UNPAIRED distinct;
  M-tails 0/16 vs P226RM ALL NEW (QT 0/4 vs P226QT).
  Counter edges computed first-hand (never trusted
  from comments): head b5 eb x11 (95733..95743) then
  ec x81 (95744..95824); A carry 95743 ff/eb ->
  95744 01/ec; T off46 ff/ec -> off47 01/ed
  (95871->95872) + off174 ff/ed -> off175 01/ee
  (95999->96000). All edge pins in for-list + PASS
  (batteries GREEN).
  Matches A-508/A-297 geometry (PB0 bf250000 REPEAT
  ==P226PB0, PB1 8e634e00 NEW, PBA 8e63b604 VPOS 8 +
  carry eb->ec, PBB10 2-sig exact map 96x3+4ex7 VPOS 19
  joint b5 const ec NO PAIR/C8/FRAG, QUADmotif 2-sig
  ee04/f604 VPOS 20 ex-b5 + row-xor + R6 UNPAIRED 4/4 +
  tails 4/4 + carry NONE (b5 const), T-ring STANDARD M8
  by COL + R9 by ROW UNPAIRED 16/16, M-tails ALL NEW
  0/16, ring edges + thresholds 47/175, NO D dips).
- C diff pure-add: numstat 636/0 rgramc.c + 262/0 rgram.py
  (+1/-1 for-line, +52/0 PINS); raw C 636 add / 0 del
  (637 incl +++ header); normalized ([0-9]+ -> N,
  cut-c2 strip, for-line trailing-';' strip, sort -u)
  del-subset-add 0 missing (del-uniq 0, add-uniq 184).
- Wall on band diff added lines (scope 45854a24..b85ccf4c,
  951 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 636/0,
  rgram.py 262/0, test_rgram.sh 1/1 (for-line), PINS 52/0.
- Tiers: merge-msg +6, code 6 blocks, tier-tags +6/0rm
  (1244->1250), singletons `if n == ` 486->488 +2/0rm,
  range-guards 356->360 +4/0rm, CLOSED prints 1246->1252
  +6: all agree (stated literal methods, first-hand).
- CONFIRM evidence (CONVERT-01 rule b): A-508-q619
  T10P227 predictive reproduces 31/31 (shape 15/15 +
  quad+Tring 12/12 + counters 4/4 CONFIRM) + A-297-q291
  corroborates same tier (shape + quad/ring + counters +
  consts 76/65/64/65 CONFIRM, 2 Q-prose labels fixed
  with counts standing; GATE uses corrected versions).
  No DISSENT on P227. Agrees with cport commit
  msg (py/C 13204, PYID 6602).
- Quiz: no conflicting CLAIM/GATE/FLAG on b335/b85ccf4c.
  b334 EVEN = sweep2 turf (tip 45854a24), used as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-08
  (w2f Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r45/ (*335* files:
  build335.log, pyid335, rgram335py/c, pass335py/c,
  cells335-battery, pins334base/pins335-cells/-nums,
  -baseN, for335-old/-new.nums, tiers334/335, smoke335.log,
  tables335.log, tabaudit335.py, sigcheck335.py/.log,
  verify335.py/.log, cdiff335.txt/-del-norm/
  -add-norm/-missing, banddiff335.txt, added335.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
