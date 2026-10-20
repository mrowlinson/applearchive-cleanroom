# GATE bcc7d15a b339 T10P231 pins 97125..97472 (348 pins) PASS-functional

Seat sweep-r46, first-hand, WT tmp/wt-encode-sweep @bcc7d15a,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r46.
Band = d8dcb7f9 (py merge w2b@df48700e partial, +6 tiers
+54 pins) + bcc7d15a (C port). Base 69174c03 (b338 tip,
1366 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build339/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r46), rgramc 04b3c29c.
- RGRAMC-PYID 6712/6712 covered=6712/6712 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 13424/13424 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 13424/13424 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (13424/13424, version-sorted).
- PINS-RGRAM names set-eq 13424/13424 (cmp-equal both ways).
  PINS cells 6712 vs for-list 6711: for-list C cells
  6711/6711, cells-for = {97472} (tail pinned, not in
  battery for-list).
- PINS 13426 rows (2 hdr + 13424, +54 vs base 13372). py diff
  +54/-0 rows = +27/-0 cells (pure P231 addition);
  test_rgram.sh 1/1 (for-line).
  For-list union 6684->6711 +27/-0: 97124 (P230 tail
  boundary) + 26 tier pins: 2 sing (97125 97126) + A 3
  (head 97127 + mid 97134 + tail 97142) + B 4 (head 97143
  + mid 97147 + carry-pre 97151 + tail 97152) + Q 12 (all
  4 rows: q0 off0/7, q1 off15/16/23, q2 off31/32/39, q3
  off47/48/55/63) + R 5 (head 97217 + edge pairs
  97279/97280 + 97407/97408).
  PINS adds = same 26 tier pins + 97472 tail (no 97124).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P231 C-vs-py, 15-table mixed-size layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 329d0000 / f1053b01);
  AM 16/16, BM 10/10, M 16/16, M19 16/16, XA19 4/4,
  QR 4/4, QT 4/4, RM 16/16, RQ 16/16 EXACT;
  AC 75/75, BC 71/71, QC 63/63, RC 70/70 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 75/71/63/70 match actual;
  TABAUDIT-GREEN rc=0. No PT/CM/PT-pair/C8/FRAG
  (classic A/B + QUADms + T88-ring), table inventory
  exactly the 15.
  Missing-sets first-hand EXACT: AC-9 [4,5,9,10,11,76,
  77,78,79] = b4,b5+M7 (b9-11,76-79) = VPOS 8;
  BC-13 [4,5,13,14,15,16,17,18,19,80,81,82,83] =
  b4,b5+M11 (b13-19,80-83) = VPOS 13;
  QC-21 [0,1,2,4,5,11,13,14,15,16,17,18,19,76,77,78,
  79,80,81,82,83] = b4,b5+M8 (b0-2,11,76-79)+R6
  (b13-18)+b19+T4 (b80-83) = VPOS 20;
  RC-18 [4,5,16,17,18,19,23,29,30,31,76,77,78,79,80,
  81,82,83] = VPOS 18 over 0..87 (b4,b5+M7 b29-31,
  80-83 + R9 b16-19,23,76-79).
  b0-3 first-hand: AC 2d5eb013, BC e0053b01,
  RC 01000000, QC(3)=0x1e (b0-2 in m-tab).
  Code AC75/BC71/QC63/RC70; incl = +1/+0/+1/+0
  (A b5 const f6, B b5 varies carry, Q b5 const f7,
  T counter) = 76/71/64/70; lane consts 76/71/64/70
  = A-529/A-301 INCL EXACT (writer dual-accounts
  PBA/quad = memo-1, PBB/T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/B/Q/R): P2310 n==97125 / P2311 n==97126
  singleton-const (offs 0/1);
  P231A 97127..97142 off=n-97127 sig 2d5eb013
  (m-tab 7B b9-11,76-79);
  P231B 97143..97152 off=n-97143 single-sig e0053b01
  (m-tab 11B b13-19,80-83);
  P231Q 97153..97216 off=n-97153 m=off&15 q=off>>4
  QUADms 15-sig (M 8B b0-2,11,76-79 +
  b19 row-add A=[0,9,9,-11] vs M19[m] + R6 6B b13-18
  + QT b80-83);
  P231R(T88-ring) 97217..97472 off=n-97217 c=off&15
  r=off>>4 STANDARD sig 01000000 (RM 7B b29-31,80-83
  by COL + RQ 9B b16-19,23,76-79 by ROW, b84-87
  const d6/38/64/3c);
  A/B/Q paylen 84 + raw lencode l16=((n<<1)|1)&0xFFFF
  pay4=l16&0xFF pay5=l16>>8; R paylen 88 + counter
  b4=(0x83+2off)&FF b5=0xf7+(off>=63)+(off>=191).
  C blocks carry T63726/63731/63736/63751/63767/63792
  py-line mirrors (exact); guards
  `if ((n) == (97125))` / `if ((n) == (97126))` + 4 ranges
  `if ((lo) <= (n) && (n) <= (hi))` exact; b19add via
  snprintf %02lx (pay[19]-hexval(XA19[q]))&0xFF; counter
  131/247+(off>=63)+(off>=191); temps _t4936.._t4955
  appended (base max _t4935, no reuse);
  C byte-index lists match py per block; insert position
  exact (dispatch tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 + M 16/16 distinct;
  M19 2-valued {35,b5}; XA19 00/09/09/f5 (3 distinct);
  row-add 6/64 distinct values over 64 cells;
  QR r1==r2 PAIRED 3/4 (b2fc01da137e x2; r0
  df3c65fa69d5, r3 01bc573a353a distinct);
  M col0 15-sig order EXACT (d33d/d63d/d73d/dd3d x2/
  a895/aa95/ae95/b095/b295/b895/b78d/b88d/bd8d/
  be8d/c18d);
  QT 4/4 distinct exact (2738643c/d7ecaf3d/01edaf3d/
  4beeaca6; r1/r2 share last 2B af3d);
  RM 16/16 + RQ 16/16 UNPAIRED distinct, tails SPLIT
  (RM b80-83 part 16 distinct + RQ b76-79 part 16
  distinct);
  M-tails 16/16 ALL NEW vs P230RM + 16/16 vs P230RQ
  (QT 4/4 vs P230QT).
  Counter/lencode edges computed first-hand (never trusted
  from comments): A head cf/f6 (97127) -> tail ed/f6
  (97142, b5 const f6); B ef/f6 -> carry ff/f6 (97151)
  -> 01/f7 (97152); Q head 03/f7 (97153) -> tail 81/f7
  (97216, b5 const f7); T off62/63 (97279->97280) +
  off190/191 (97407->97408). All edge pins in for-list
  + PASS (batteries GREEN); 97472 tail pinned + PYID
  covered.
  Matches A-529/A-301 geometry (mixed-size 92x84B+256x88B,
  PB0 329d0000 NEW, PB1 f1053b01 NEW, PBA 2d5eb013 VPOS 8
  b5 const f6, PBB10 e0053b01 VPOS 13 b5-carry f6->f7
  @97151->97152, QUADms 15-sig VPOS 20 b5 const f7 +
  row-add A=[0,9,9,-11] (ADD staged per comment, XOR tie
  noted; memo adopts ADD per precedent) + R6 r1==r2
  PAIRED 3/4 + tails 4/4 + M-tails ALL NEW 16/16,
  T88-ring STANDARD M7 by COL + R9 by ROW UNPAIRED 16/16
  + tails SPLIT + b84-87 const + M-tails ALL NEW 16/16,
  ring edges + thresholds 63/191, NO D dips).
- C diff: numstat 642/1 rgramc.c + 261/1 rgram.py
  (+1/-1 for-line, +54/0 PINS); raw C 642 add / 1 del
  (643 incl +++ header); normalized ([0-9]+ -> N,
  cut-c2 strip, trailing-';' strip, sort -u)
  del-uniq 1, add-uniq 184, miss 1 = the OLD paylen-guard
  line only (allow-list extended +88 for first 88B tier;
  py guard same 1-line change with T10P231+ comment).
  No other del: all other 642 C + 261 py lines pure-add.
- Wall on band diff added lines (scope 69174c03..bcc7d15a,
  958 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression//usr/bin/aa/shim 0 hits,
  shebang 0 hits. Files touched: rgramc.c 642/1,
  rgram.py 261/1, test_rgram.sh 1/1 (for-line), PINS 54/0.
- Tiers: merge-msg +6, code 6 blocks, tier-tags +6/0rm
  (1272->1278), singletons `if n == ` 494->496 +2/0rm,
  range-guards 374->378 +4/0rm, CLOSED prints 1790->1796
  +6: all agree (stated literal methods, first-hand).
- CONFIRM evidence (CONVERT-01 rule b): A-529-q623
  T10P231 predictive reproduces 35/35 (shape 15/15 +
  quad+Tring 12/12 + counters 8/8 CONFIRM; XOR-tie flag
  adopted ADD per precedent, cut SAFE, states no
  DISSENT) + A-301-q295 corroborates same tier (shape +
  quad/ring + counters 3/3 legs CONFIRM, b19 tie proven
  undecidable arithmetically, staged ADD stands, consts
  76/71/64/70 INCL). No DISSENT on P231. Agrees with
  cport commit msg (py/C 13424, PYID 6712).
- Quiz: no conflicting CLAIM/GATE/FLAG on b339/bcc7d15a.
  b338 EVEN = sweep2 turf (tip 69174c03), used as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-09
  (w2e Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r46/ (*339* files:
  build339.log, pyid339.log, rgram339py/c.log,
  pass339py/c.txt, pins338base.csv, pins338/339-cells.nums,
  for339-old/-new/-add.nums, sh338.sh, smoke339.log,
  tables339.log, tabaudit339.py, cdiff339.txt/-del-norm/
  -add-norm/-missing, banddiff339.txt, added339.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
