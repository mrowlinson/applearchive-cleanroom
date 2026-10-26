# GATE 49f9f3e4 b427 T10P319 pins 127749..128096 (348 pins) PASS-functional

Seat sweep-r68, first-hand, WT tmp/wt-encode-sweep @49f9f3e4,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r68.
Band = 38f56a72 (py merge w2b@78fbd03a partial, +6 tiers
+62 pins) + 49f9f3e4 (C port). Base f278bdf0 (b426 tip,
1896 tiers sealed).

- Build: make -C src/c BUILDDIR=r68/build427 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build427/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r68, sha256 matches b354-b427
  pinned value; band touches no aae sources), rgramc
  sha1 7fc5f96a / sha256 9c889da6.
- RGRAMC-PYID 9470/9470 covered=9470/9470 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18940/18940 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18940/18940 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (18940/18940, sorted).
- PINS-RGRAM cells set-eq 9470/9470 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 18942 rows (2 hdr + 18940, +62 vs base 18880).
  For-list union 9439->9470 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (127749 127750) +
  A 6 (head 127751 + 127752 + 127758 + 127759 +
  127765 + tail 127766; offs 0,1,7,8,14,15) +
  C 6 (head 127767 + 127768 + 127771 + 127772 +
  127775 + tail 127776; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 127769, 127770, 127773,
  127774) +
  Q 10 (head 127777 + off7 127784 + boundary pair
  127792/127793 + boundary pair 127808/127809 +
  off48 127825 + off55 127832 + tail pair
  127839/127840; offs 0,7,15,16,31,32,48,55,
  62,63; const-b5 NO step edge, first-hand) +
  R 7 (head 127841 + edge pair 127871/127872 +
  mid 127950 + edge pair 127999/128000 + tail
  128096; offs 0,30/31,109,158/159,255; 1-mid
  shape, both counter edges pair-covered,
  first-hand).
  PINS adds = same 31 tier pins (2 rows each).
  Each for-N yields 2 PASS lines; 31x2 = 62
  = 18940-18878.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P319 C-vs-py, 12-table A-PBA88-PLAIN/
  C10-1SIG-88-M5b8/QUAD88-2SIG-PAIRED-4R+T88-RING-
  SWAPPED layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs 36ac2c01 NEW / 02000000 sig-eq-P318PB1;
  S0 diff vs P318S0 30/84 @ b2,4,5,22,23,30,
  32-39,41-43,48,52-55,72-79 NOT byte-equal +
  S1 diff vs P318S1 68/88 @ b4-63,80-87 NOT
  byte-equal +
  S1 diff vs own C10 cells [75,75,75,75,75,75,
  75,75,75,75] TRUE UNIFORM all 10 (cell0 @ b4,
  6-55,64-87), NOT byte-equal);
  AM 16/16 (7B), CM 10/10 (5B), M 16/16 (6B),
  QR 4/4 (17B), RM 16/16 (7B), RQ 16/16 (6B)
  EXACT;
  AC 79/79, CC 81/81, QC 63/63, RC 73/73 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 79/81/63/73 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit427.py 107 PASS 0 FAIL).
  No F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R17 carries b84-87 inside QR); table
  inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-9 [4,5,13,14,
  15,80,81,82,83] = b4,b5+M7 (b13-15,
  80-83);
  CC-7 [4,5,8,84,85,86,87] = b4,b5+M5 (b8,
  84-87, full sig b0-3 in CC = 02,00,00,00 ->
  02000000 x10);
  QC-25 [0,4,5,8,9,10,11,12,13,14,15,16,17,18,
  19,20,21,80,81,82,83,84,85,86,87] = b0,b4,
  b5+QM6 (b20,21,80-83)+R17 (b0,8-19,84-87;
  b1,b2,b3 const 00 in QC);
  RC-15 [4,5,20,21,28,29,30,76,77,78,79,80,81,
  82,83] = b4,b5+TR6 (b20,21,80-83)+TM7
  (b28-30,76-79).
  PLAIN first-hand: AC b0..b3 = 25,00,00,00 ->
  sig 25000000 x16, b0 const 25; AM 16/16
  distinct; b5 const e6.
  1SIG first-hand: CC b0-3 full sig 02000000
  x10 SAME-as-PB1-sig (S1 sig-eq own C10); CM
  10/10 diverge; b5 const e6, NO step; 10/10
  diverge.
  Code AC79/CC81/QC63/RC73; incl = +1/+1/+1/+0
  (A b5 const e6, C b5 const e6, Q b5 const e6
  NO step, T counter) = 80/82/64/73; lane consts
  = A-829 INCL EXACT (deduct-b5-only-when-b5vary
  rule holds; Q-const +1 like PBA).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3190 n==127749 / P3191
  n==127750 singleton-const (offs 0/1; 84B/88B);
  P319A 127751..127766 off=n-127751 PBA88-PLAIN-
  M7 (m-tab 7B b13-15,80-83, sig 25000000, b0
  const 25, b5 const e6);
  P319C 127767..127776 off=n-127767 C10-1SIG-88-
  M5b8 (m-tab 5B b8,84-87 M5, full sig b0-3 in
  CC = 02000000, b5 const e6, NO step);
  P319Q 127777..127840 off=n-127777 m=off&15
  q=off>>4 QUAD88-2SIG-PAIRED-4R rows0-1
  21000000 x32 + rows2-3 10000000 x32
  (M 6B b20,21,80-83 QM6 shared NO frags +
  R17 b0,8-19,84-87 r0
  21f9e99c1400df3ca8fc668521f7aa564b / r1
  21f9e99c140052fc021c916e017d02882d share
  6B prefix 21f9e99c1400 (b0,b8-b12), differ
  b13 df/52, NOT 8B (A-829 section-F CONFIRMED
  first-hand: writer gloss corrected, b13 in
  R17 tab, no table impact) + r23 share 13B
  1019122f904fe7a400fb7dcdd7, tails b84-87 4
  distinct f7aa564b/7d02882d/d0457c1e/f5457c1e,
  r2r3 TRUE 3B 457c1e (differ b84 d0/f5),
  r0/r1 lcs 0 vs all, b0 in tab sig-paired
  r01=21 r23=10 (b1-3 const 00 in QC), b5 const
  e6 NO step, b4 0x43+2off range 43..c1 NO
  edge);
  P319R(T88-ring) 127841..128096 off=n-127841
  c=off&15 r=off>>4 SWAPPED sig 08010000 (TM
  7B b28-30,76-79 by COL + TR 6B b20,21,80-83
  by ROW SWAPPED tails UNPAIRED 16/16, b84-87
  const 11/2d/ac/b5);
  A/C/Q paylen 88 / raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (b5 const
  emerges from raw lencode);
  R paylen 88 +
  counter b4=(0xc3+2off)&FF b5=0xe6+(off>=31)+
  (off>=159).
  C blocks carry T85798/85803/85808/85823/85838/
  85860 py-line mirrors (exact); guards
  `if ((n) == (127749))` / `if ((n) == (127750))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 195+2*off + 230+(off>=31)+
  (off>=159); temps _t6553.._t6568 appended
  (base max _t6552, no reuse); _i band 3966,
  3968,3971,3974 (base max _i3964), _b band
  3965,3967,3969,3970,3972,3973 (base max
  _b3963), no reuse; C byte-index lists match py
  per block (A 7B, C 5B, Q 6B/17B, R 7B/6B
  SWAPPED tails-split); insert position exact
  (P318R block precedes, P319R immediately
  precedes LAST scope-hit; C has 2 scope hits;
  py has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0 21f9e99c1400df3c
  a8fc668521f7aa564b; r1 21f9e99c140052fc021c
  916e017d02882d; r2 1019122f904fe7a400fb7dcd
  d7d0457c1e; r3 1019122f904fe7a400fb7dcdd7f5
  457c1e);
  QR tail-shares: r2r3 TRUE 3B 457c1e, r0/r1
  lcs 0 vs all;
  RQ==M FULL6 (M 6B vs RQ 6B: agree (0,0),(1,1),
  (2,2),(3,3),(4,4),(5,5) 16/16 each; tabs
  byte-identical; maxagree 16 all 6) -- 3rd
  full-identity instance (after P311 + P313; QM6
  byte positions b20,21,80-83, TR6 positions
  b20,21,80-83);
  31st odd-band RQ==M instance;
  tails SWAPPED-split (RM b76-79 by COL c=off&15,
  RQ b80-83 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P318T RQ row-led tails
  (overlap 0); RM-tails (b76-79) ALL NEW vs P318T
  RM col-led tails (overlap 0); RQ-tails (b80-83)
  ALL NEW vs P318T RQ row-led tails (overlap 0);
  cross overlaps 0 (P318T widths RM 6B/RQ 7B
  SWAPPED first-hand; tails compared SWAPPED-
  aware against col-led/row-led sets);
  S0 NEW string (30/84 differ vs P318S0 @ b2,4,5,
  22,23,30,32-39,41-43,48,52-55,72-79) + S1 NEW
  string (68/88 differ vs P318S1 @ b4-63,80-87;
  75/88 TRUE UNIFORM vs own C10 all 10, cell0 @
  b4,6-55,64-87; 7th TRUE-uniform case after P299
  25/84 + P303 58/84 + P307 27/84 + P311 70/88 +
  P315 26/88 + P317 37/88);
  P319 actuals (S0 36ac2c01/S1 02000000/PBA88
  25000000/C10-1SIG 02000000 x10 SAME-as-PB1-sig
  + PB1-vs-P318PB1 68/88) == A-824 predicted next
  EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 0f/e6 (127751)
  tail 2d/e6 (127766), b5set {e6}; C head
  2f/e6 (127767) tail 41/e6 (127776), b5set
  {e6};
  Q head 43/e6 (127777) tail c1/e6 (127840)
  NO edge, b5set {e6};
  quad b4=(0x43+2off) 64/64 range 43..c1;
  T head c3/e6 (127841) + off30/31 (127871->
  127872) ff/e6->01/e7 + mid off109 9d/e7
  (127950) + off158/159 (127999->128000)
  ff/e7->01/e8 + tail off255 c1/e8 (128096).
  All edge pins in for-list + PASS (batteries
  GREEN); 128096 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  441a9d5964ac5b11... matches PINS rawlen 104,
  py+C CLOSED T10P319R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand (346 + S0/S1
  embedded b4/b5 0b/e6 + 0d/e6).
  Matches A-829 geometry (novel 1x84+347x88 framing
  PINS-sampled 100x1+104x30 + code paylens 84/88,
  PB0 36ac2c01 NEW + PB1 02000000 sig-eq-P318PB1
  68/88 + SAME-as-own-C10 75/88,
  PBA88-PLAIN VPOS 8 b5 const e6,
  C10-1SIG-88-M5b8 VPOS 6 b5 const e6 10/10
  diverge,
  QUAD88-2SIG-PAIRED-4R VPOS 24 = b0,b4+QM6+R17
  (b0 shared) + R17 4/4 UNPAIRED pairwise-
  disjoint sig-paired r01/r23 + section-F r01-
  6B-prefix (NOT 8B) + tails 4 distinct r2r3-
  TRUE3/r0r1-lcs0 + b0 sig-paired + NO step +
  M-tails ALL NEW 16/16, T88-RING SWAPPED sig
  08010000 TM7 by COL + TR6 by ROW UNPAIRED
  16/16 + SWAPPED tails + b84-87 const 112dacb5,
  ring edges + thresholds 31/159, NO D dips).
- C diff pure-add: numstat 608/0 rgramc.c + 233/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 608
  content + 5 blank-only `+` lines / 0 del; raw py
  233 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 145, py del-uniq
  0 add-uniq 169). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope f278bdf0..
  49f9f3e4, 904 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 608/0, rgram.py 233/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1802->1808 +6, singletons
  `if n == ` 670->672 +2, range-guards `<= n <=`
  728->732 +4, CLOSED T10P prints
  1802->1808 +6, seal 1896->1902
  +6 (cport msgs; offset +94 vs CLOSED-T10P stable
  b401-b427): all agree (stated literal methods,
  first-hand).
  C guards: singleton `if ((n) == (` 665->667 +2,
  range 728->732 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b425 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-829-q911
  memo CONFIRM 64/65 + section-F (Verifier v215.py
  64/65, single FAIL = Q-claim witness. Geometry
  GATED PORT; writer corrects the forensic gloss
  (no table impact); section-F r01-prefix 6B
  CONFIRMED first-hand this gate: r0/r1 share
  21f9e99c1400, differ b13 df/52, NOT 8B;
  w2b-r27 [4/8], quoted verbatim).
  Viewer: NO P319 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P319. Agrees with cport commit msg
  (py/C 18940, PYID 9470).
- Quiz: no conflicting CLAIM/GATE/FLAG on b427/
  49f9f3e4. b426/b428 EVEN = sweep2 turf, used b426
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-23 (w2b Q-block refill only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r68/ (build427.log,
  b427-pyid.log, b427-py/c.log, pass427py/c.txt,
  seteq427.py/log, b427-smoke.log, b427-units.log,
  tables427.log, tabaudit427.py, edges427.py,
  edges427.log, cdiff427.txt, pydiff427.txt,
  banddiff427.txt, added427.txt, numstat427.txt,
  diffwall427.py/log, build427/ binaries,
  tail-128096.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
