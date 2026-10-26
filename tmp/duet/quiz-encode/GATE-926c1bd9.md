# GATE 926c1bd9 b365 T10P257 pins 106173..106520 (348 pins) PASS-functional

Seat sweep-r53, first-hand, WT tmp/wt-encode-sweep @926c1bd9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r53.
Band = 99d41bb0 (py merge w2b@5240fbf7 partial, +6 tiers
+62 pins) + 926c1bd9 (C port). Base bd37fe85 (b364 tip,
1524 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build365/{aae,rgramc}, rc=0,
  0 warnings. aae sha1 7d8dd3a2 / sha256 d6e27c97
  (pinned stable continues: sha1 r39-r53, sha256 matches
  b354-b363 pinned value; band touches no aae sources),
  rgramc sha1 2b96810f / sha256 b813309f.
- RGRAMC-PYID 7525/7525 covered=7525/7525 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 15050/15050 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 15050/15050 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (15050/15050, sorted).
- PINS-RGRAM cells set-eq 7525/7525 (xor 0 all 3 ways:
  for^pass for^pins pass^pins; py^C 0).
  PINS 15052 rows (2 hdr + 15050, +62 vs base 14990).
  For-list union 7494->7525 +31/-0 (python sets, never
  comm).
  31 = 2 sing (106173 106174) +
  A 6 (head 106175 + 106176 + 106181 + 106185 + 106189 +
  tail 106190) +
  C 8 (head 106191 + 106194 + 106195 + 106196 + 106197 +
  106198 + 106199 + tail 106200; offs 1,2 unsampled:
  106192, 106193) +
  Q 8 (head 106201 + 106217 + 106233 + carry pair
  106239/106240 + 106248 + 106249 + tail 106264) +
  R 7 (head 106265 + edge pair 106367/106368 + mid
  106393 + edge pair 106495/106496 + tail 106520).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 31x2 = 62 = 15050-14988.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var).
- Tables audit P257 C-vs-py, 13-table A-PBA/C10-MS/
  QUADms-row-led+T88 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 601a0300 NEW / e58c3506 ==P256PB1, both
  NEW strings);
  AM 16/16 (9B), CM 10/10 (13B), M 16/16 (8B),
  QR 4/4 (8B), QT 4/4 (4B), RM 16/16 (7B), RQ 16/16
  (7B) EXACT;
  AC 73/73, CC 69/69, QC 62/62, RC 72/72 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 73/69/62/72 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit365.py 47 PASS 0 FAIL).
  No QB (row-led quad, not pair-led), no BM/BC, no
  M42/X42, no PT/FM; table inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-11 [4,5,47,48,49,
  50,51,76,77,78,79] = b4,b5+M9 (b47-51,76-79);
  CC-15 [2,3,4,5,35,46,47,48,49,50,51,80,81,82,83]
  = b4,b5+M13 (b2,3,35,46-51,80-83; b0,b1 const
  e5,8c, sig b2,b3 in tab);
  QC-22 [3,4,5,6,7,8,9,35,46,47,48,49,50,51,76,
  77,78,79,80,81,82,83] = b4,b5+QM8 (b6-9,76-79)+
  R8 (b3,35,46-51)+T4 (b80-83);
  RC-16 [4,5,6,7,9,10,11,12,76,77,78,79,80,81,
  82,83] = VPOS 16 over 0..87 (b4,b5+TM7
  b9-11,80-83 + TR7 b6,7,12,76-79).
  b0-3 first-hand: AC b0-3 a0802f7c (==P256PBA);
  CM sig map e58c3506 x4 @rows0-3 + e58cd504/
  e58c9504/e58cb504/e58cd504 @rows4-7 + e58c1505
  x2 @rows8-9 (d504 repeats @106195+@106198, 5
  distinct);
  QR full-sig rows 53929c867196cfbd-r0 /
  55d2169151c42757-r1 / 4b9272aaf1b82f64-r2,r3
  (row-sigs 53/55/4b/4b);
  RC 05000000 (==P249/251T sig, re-read first-hand).
  Code AC73/CC69/QC62/RC72; incl = +1/+1/+0/+0
  (A/C b5 const 3d, Q b5-carry, T counter) =
  74/70/62/72; lane consts = A-611/A-321 INCL
  EXACT (writer PBA/C10 = memo-1, quad/T88
  identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2570 n==106173 / P2571
  n==106174 singleton-const (offs 0/1);
  P257A 106175..106190 off=n-106175 PBA16
  (m-tab 9B b47-51,76-79, sig a0802f7c ==P256PBA,
  b5 const 3d);
  P257C 106191..106200 off=n-106191 C10-MS
  5-sig (m-tab 13B b2,3,35,46-51,80-83, b0,b1
  const, b5 const 3d);
  P257Q 106201..106264 off=n-106201 m=off&15
  q=off>>4 3-sig row-led quad (M 8B b6-9,76-79 +
  R8 8B sig-led b3,35,46-51 + QT b80-83, b5-carry
  3d->3e @106239->106240);
  P257R(T88-ring) 106265..106520 off=n-106265
  c=off&15 r=off>>4 STANDARD sig 05000000 (TM 7B
  b9-11,80-83 by COL + TR 7B b6,7,12,76-79 by
  ROW SPLIT tails, b84-87 const dc/77/ac/14);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8; R paylen 88
  + counter b4=(0x33+2off)&FF b5=0x3e+(off>=103)+
  (off>=231).
  C blocks carry T70591/70596/70601/70617/70633/
  70656 py-line mirrors (exact); guards
  `if ((n) == (106173))` / `if ((n) == (106174))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 51/62 + (off>=103)+(off>=231);
  temps _t5446.._t5463 appended (base max _t5445,
  no reuse); _i max 3312->3323, _b max 3311->
  3322, no reuse; C byte-index lists match py per
  block (A 9B, C 13B, Q 8/8/4B, R 7/7B); insert
  position exact (dispatch tail, N out-of-scope
  follows).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (5-sig rows, all distinct);
  M 16/16 distinct;
  QR r2==r3 PAIRED (4b9272aaf1b82f64 x2; r0
  53929c867196cfbd + r1 55d2169151c42757
  distinct);
  QT 4/4 distinct exact (d777ee49/223c1151/
  d528f87f/ff28f87f); r2/r3 share last 3B ONLY
  (28f87f; 1st bytes d5/ff differ) TRUE-3B per
  A-611 (memo re-verified programmatically);
  M/RQ heads(b6,7) 16/16 + tails(b76-79) 16/16
  same-index (shared-slice prefix+suffix; middle
  M-b8,9 vs RQ-b12 differs; full-string impossible:
  RQ 7B vs M 8B);
  tails SPLIT (RM b80-83 by COL c=off&15, RQ
  b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P256T
  (P256RQ 7B tails, row-led via TR7);
  QT 4/4 NEW vs P256QT
  (10299170/36299170/6c301f67/87aa49cb).
  S0 NEW string (sig 601a0300 NEW; P256S0 sig
  641a0300); S1 NEW (sig e58c3506 ==P256PB1;
  P256S1 sig e58c3506).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 7f/3d (106175)
  tail 9d/3d (106190), b5set {3d}; C head 9f/3d
  (106191) tail b1/3d (106200), b5set {3d}; Q
  head b3/3d (106201) tail 31/3e (106264),
  b5set {3d,3e}, carry ff/3d->01/3e @106239->
  106240 (single flip, INTERNAL off38->39).
  T head 33/3e (106265) + off102/103 (106367->
  106368) ff/3e->01/3f + off230/231 (106495->
  106496) ff/3f->01/40 + mid off128 33/3f
  (106393) + tail off255 31/40 (106520). All
  edge pins in for-list + PASS (batteries GREEN);
  106520 tail pinned + in for-list + PASS.
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (7b/3d, 7d/3d) match raw
  lencode.
  Matches A-611/A-321 geometry (mixed-size 92x84B+
  256x88B, PB0 601a0300 NEW + PB1 e58c3506
  ==P256PB1, PBA16 VPOS 10 b5 const 3d 16/16
  distinct NO pair, C10-MS 5-sig VPOS 14 b5 const
  3d 10/10 diverge, QUAD row-led 3-sig VPOS 22
  QM8 shared + R8 r2==r3 + tails 4/4 TRUE-3B +
  M-tails ALL NEW 16/16, T88-ring STANDARD sig
  05000000 TM7 by COL + TR7 by ROW UNPAIRED 16/16
  + SPLIT tails + b84-87 const dc77ac14, ring
  edges + thresholds 103/231, NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 238/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 605
  content + 5 blank-only `+` lines / 0 del; raw py
  238 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 174, py del-uniq
  0 add-uniq 195). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope bd37fe85..
  926c1bd9, 911 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 610/0, rgram.py 238/0,
  test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1430->1436 +6, singletons
  `if n == ` 546->548 +2, range-guards `<= n <=`
  480->484 +4, CLOSED T10P prints 1430->1436 +6
  (bare-CLOSED 1948->1954 +6, same delta), seal
  1524->1530 +6: all agree (stated literal methods,
  first-hand). C guards: singleton `if ((n) == (`
  541->543 +2, range 480->484 +4; 5-count C-vs-py
  singleton offset pre-existing (same C-only dip
  guards as b357/b359/b361/b363), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-611-q769
  T10P257 memo CONFIRM 35/35 (shape 12/12 +
  quad+Tring 11/11 + counters 12/12; TRUE-3B tails
  28f87f memo re-verified programmatically, tier
  cut SAFE)
  + A-321-q321 viewer corroborates same tier (3/3
  legs CONFIRM, consts 74/70/62/72 INCL).
  No DISSENT on P257. Agrees with cport commit msg
  (py/C 15050, PYID 7525).
- Quiz: no conflicting CLAIM/GATE/FLAG on b365/
  926c1bd9. b364/b366 EVEN = sweep2 turf, used b364
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-12 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r53/ (build365.log,
  pyid365.log, rgram365py/c-full.log, pass365py/c.
  txt, pins364base.csv, for365-old/-new.nums,
  sh364/365.sh, smoke365.log, tables365.log,
  tabaudit365.py, edges365.log, numstat365.txt,
  cdiff365.txt, pydiff365.txt, banddiff365.txt,
  build365/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
