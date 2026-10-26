# GATE d1c18b6c b425 T10P317 pins 127053..127400 (348 pins) PASS-functional

Seat sweep-r68, first-hand, WT tmp/wt-encode-sweep @d1c18b6c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r68.
Band = 54bca2c5 (py merge w2b@9de16d58 partial, +6 tiers
+62 pins) + d1c18b6c (C port). Base fe9d3bf0 (b424 tip,
1884 tiers sealed).

- Build: make -C src/c BUILDDIR=r68/build425 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build425/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r68, sha256 matches b354-b425
  pinned value; band touches no aae sources), rgramc
  sha1 8c56ceec / sha256 ff51e8b5.
- RGRAMC-PYID 9408/9408 covered=9408/9408 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18816/18816 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18816/18816 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (18816/18816, sorted).
- PINS-RGRAM cells set-eq 9408/9408 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 18818 rows (2 hdr + 18816, +62 vs base 18756).
  For-list union 9377->9408 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (127053 127054) +
  A 6 (head 127055 + 127056 + 127062 + 127063 +
  127069 + tail 127070; offs 0,1,7,8,14,15) +
  C 6 (head 127071 + 127072 + 127075 + 127076 +
  127079 + tail 127080; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 127073, 127074, 127077,
  127078) +
  Q 10 (head 127081 + off7 127088 + mid pair
  127096/127097 + edge pair 127103/127104 +
  off32 127113 + off48 127129 + tail pair
  127143/127144; offs 0,7,15,16,22,23,32,48,
  62,63; step@23 edge pair-covered + tail pair,
  first-hand) +
  R 7 (head 127145 + edge pair 127231/127232 +
  mid 127250 + edge pair 127359/127360 + tail
  127400; offs 0,86/87,105,214/215,255; 1-mid
  shape, both counter edges pair-covered,
  first-hand).
  PINS adds = same 31 tier pins (2 rows each).
  Each for-N yields 2 PASS lines; 31x2 = 62
  = 18816-18754.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P317 C-vs-py, 19-table A-PBA88-PLAIN/
  C10-1SIG-88-TAIL/QUAD88-2SIG-4R-FRAG6+T88-RING-
  STANDARD layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs 57a75201 sig-eq-P316PB0 / 02000000 sig-eq-
  P316PB1;
  S0 diff vs P316S0 31/84 @ b4-11,34,35,41-48,
  50,51,56-63,80,81,83 NOT byte-equal + S1 diff vs
  P316S1 52/88 @ b4-14,17-27,36-38,40-43,48-55,
  64-71,80,81,83-87 NOT byte-equal +
  S1 diff vs own C10 cells [37,37,37,37,37,37,
  37,37,37,37] TRUE UNIFORM all 10 (cell0 @ b4,
  16-18,22-26,28-35,56-71,84-87), NOT byte-equal);
  AM 16/16 (8B), CM 10/10 (4B), M 16/16 (4B),
  QR 4/4 (19B), FT25/FT26/FT27/FT29/FT34/FT35A/
  FT35B 16/16 each (1B), RM 16/16 (8B), RQ 16/16
  (7B) EXACT;
  AC 78/78, CC 82/82, QC 57/57, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 78/82/57/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit425.py 155 PASS 0 FAIL).
  No bare F, no F0/F1, no BM/BC (C10, not B10),
  no M19/X19, no M42/X42/H42/L42, no QB/PT/FM,
  no RT/TT (ring, not ROWTAIL), no QT (R19 carries
  b84-87 inside QR); table inventory exactly the 19.
  Missing-sets first-hand EXACT: AC-10 [4,5,28,29,
  30,31,80,81,82,83] = b4,b5+M8 (b28-31,
  80-83);
  CC-6 [4,5,84,85,86,87] = b4,b5+M4 (b84-87,
  full sig b0-3 in CC = 02,00,00,00 ->
  02000000 x10);
  QC-31 [0,4,5,8,9,10,11,12,13,14,15,19,25,26,
  27,28,29,30,31,32,33,34,35,80,81,82,83,84,
  85,86,87] = b0,b4,b5+QM4 (b80-83)+R19 (b0,
  8-15,19,28,30-33,84-87)+F6 (b25,26,27,29,
  34,35; b1,b2,b3 const 00 in QC);
  RC-17 [4,5,29,34,35,40,41,42,43,76,77,78,79,
  80,81,82,83] = b4,b5+TR7 (b29,34,35,76-79)+
  TM8 (b40-43,80-83).
  PLAIN first-hand: AC b0..b3 = 28,00,00,00 ->
  sig 28000000 x16, b0 const 28; AM 16/16
  distinct; b5 const e0.
  1SIG first-hand: CC b0-3 full sig 02000000
  x10 SAME-as-PB1-sig (S1 sig-eq own C10); CM
  10/10 diverge; b5 const e0, NO step; 10/10
  diverge.
  Code AC78/CC82/QC57/RC71; incl = +1/+1/+0/+0
  (A b5 const e0, C b5 const e0, Q b5 STEP
  e0->e1, T counter) = 79/83/57/71; lane consts
  = A-823 INCL EXACT (deduct-b5-only-when-b5vary
  rule holds).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3170 n==127053 / P3171
  n==127054 singleton-const (offs 0/1; 84B/88B);
  P317A 127055..127070 off=n-127055 PBA88-PLAIN-
  M8b28 (m-tab 8B b28-31,80-83, sig 28000000,
  b0 const 28, b5 const e0);
  P317C 127071..127080 off=n-127071 C10-1SIG-88-
  TAIL (m-tab 4B b84-87 M4, full sig b0-3 in CC =
  02000000, b5 const e0, NO step);
  P317Q 127081..127144 off=n-127081 m=off&15
  q=off>>4 QUAD88-2SIG-4R-FRAG6 r0 2a000000 x16 +
  r123 13000000 x48
  (M 4B b80-83 QM4 shared NO frags + R19 b0,
  8-15,19,28,30-33,84-87 r0
  2ab92c091200f97cf73af6343216b1d1ee8e61
  distinct / r123 share 10B 13593edf3d
  654990008d + r23 share 15B
  13593edf3d654990008d3722eb351e, tails b84-87 4
  distinct d1ee8e61/
  a8437798/3de4c0cb/62e4c0cb, r2r3 TRUE 3B
  e4c0cb (differ b84 3d/62), r0/r1 lcs 0 vs
  all, b0 in tab row-led split r0=2a r123=13
  (b1-3 const 00 in QC), b5 0xe0+(off>=23) step
  edge off22->23 ff/e0->01/e1, b4 0xd3+2off
  base 0xd3 step2 + FRAG6: b25 q0 const f2 /
  q123 FT25[m] {72,f2} + b26 q0 const 7a /
  FT26[m] {7e,7f,f8,f9,fa} + b27 q0 const 7e
  / FT27[m] {17,1f} + b29 q0 FT29[m] {5d,5f,
  7d,7f} / q1 const bc / q23 const fc + b34 q0
  FT34[m] {07,47,87,c7} / q1 const f7 / q23
  const c0 + b35 q0 FT35A[m] 15 distinct /
  q123 FT35B[m] 16 distinct; C consts 242/122/
  126/188/252/247/192 match py hex f2/7a/7e/
  bc/fc/f7/c0; NO ADD arithmetic -- FRAG6 =
  consts + coltabs only, FIRST of class);
  P317R(T88-ring) 127145..127400 off=n-127145
  c=off&15 r=off>>4 STANDARD sig 3f010000 (TM
  8B b40-43,80-83 by COL + TR 7B b29,34,35,
  76-79 by ROW SPLIT tails UNPAIRED 16/16,
  b84-87 const bf/27/24/fb);
  A/C paylen 88 / raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (b5 const
  emerges from raw lencode);
  Q paylen 88 / explicit counter b4=(0xd3+2off)
  &FF b5=0xe0+(off>=23) == raw lencode 64/64;
  R paylen 88 +
  counter b4=(0x53+2off)&FF b5=0xe1+(off>=87)+
  (off>=215).
  C blocks carry T85297/85302/85307/85322/85337/
  85395 py-line mirrors (exact); guards
  `if ((n) == (127053))` / `if ((n) == (127054))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 83+2*off + 225+(off>=87)+
  (off>=215); temps _t6507.._t6536 appended
  (base max _t6506, no reuse); _i band 3946,
  3948,3951,3954 (base max _i3944), _b band
  3945,3947,3949,3950,3952,3953 (base max
  _b3943), no reuse; C byte-index lists match py
  per block (A 8B, C 4B, Q 4B/19B/1Bx7, R 8B/7B
  STANDARD tails-split); insert position exact
  (P316R block precedes, P317R immediately
  precedes LAST scope-hit; C has 2 scope hits;
  py has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0 2ab92c091200f97c
  f73af6343216b1d1ee8e61; r1 13593edf3d6549900
  08d73a4fa753ba8437798; r2 13593edf3d6549900
  08d3722eb351e3de4c0cb; r3 13593edf3d6549900
  08d3722eb351e62e4c0cb);
  QR tail-shares: r2r3 TRUE 3B e4c0cb, r0/r1
  lcs 0 vs all;
  RQ==M TAILS4-ONLY (M 4B vs RQ 7B: agree (0,3),
  (1,4),(2,5),(3,6) 16/16 each; last-4 tails
  agree, 3 head cols isolated maxagree 0,0,0;
  tabs differ) -- 3rd TAILS4-ONLY degree instance
  (after P309 heads 0,1,5,1,0 + P315 heads 0,1,0);
  30th odd-band RQ==M instance;
  tails STANDARD-split (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P316T RM col-led tails
  (overlap 0); RM-tails (b80-83) ALL NEW vs P316T
  RM col-led tails (overlap 0); RQ-tails (b76-79)
  ALL NEW vs P316T RQ row-led tails (overlap 0);
  cross overlaps 0 (P316T widths RM 10B/RQ 9B
  3SIG STANDARD-split first-hand; tails compared
  position-aware against col-led/row-led sets);
  S0 string 31/84 differ vs P316S0 (sig-eq repeat)
  + S1 string 52/88 differ vs P316S1 (sig-eq
  repeat; 37/88 TRUE UNIFORM vs own C10 all 10,
  cell0 @ b4,16-18,22-26,28-35,56-71,84-87;
  6th TRUE-uniform case after P299 25/84 +
  P303 58/84 + P307 27/84 + P311 70/88 + P315
  26/88);
  P317 actuals (S0 57a75201/S1 02000000/PBA88
  28000000/C10-1SIG 02000000 x10 SAME-as-PB1-sig
  + PB1-vs-P316PB1 52/88) == A-819 predicted next
  EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 9f/e0 (127055)
  tail bd/e0 (127070), b5set {e0}; C head
  bf/e0 (127071) tail d1/e0 (127080), b5set
  {e0};
  Q head d3/e0 (127081) edge off22->23
  (127103->127104) ff/e0->01/e1 tail 51/e1
  (127144), b5set {e0,e1};
  quad b4=(0xd3+2off) 64/64 + b5 step 64/64;
  T head 53/e1 (127145) + off86/87 (127231->
  127232) ff/e1->01/e2 + mid off105 25/e2
  (127250) + off214/215 (127359->127360)
  ff/e2->01/e3 + tail off255 51/e3 (127400).
  All edge pins in for-list + PASS (batteries
  GREEN); 127400 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  498d852ce2cb06a7... matches PINS rawlen 104,
  py+C CLOSED T10P317R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand (346 + S0/S1
  embedded b4/b5 9b/e0 + 9d/e0).
  Matches A-823 geometry (novel 1x84+347x88 framing
  PINS-sampled 100x1+104x30 + code paylens 84/88,
  PB0 57a75201 sig-eq-P316PB0 31/84 + PB1
  02000000 sig-eq-P316PB1 52/88 + SAME-as-own-
  C10 37/88,
  PBA88-PLAIN VPOS 9 b5 const e0,
  C10-1SIG-88-TAIL VPOS 5 b5 const e0 10/10
  diverge,
  QUAD88-2SIG-4R-FRAG6 VPOS 31 = b0,b4,b5+QM4+
  R19+F6 (b0 shared) + R19 4/4 UNPAIRED
  pairwise-disjoint + FRAG6 exact (r123-tab
  2/5/2 + r0-tab 4/4/15 + r123-tab 16 distinct)
  + tails 4 distinct r2r3-TRUE3/r0r1-lcs0 + b0
  row-led split + step edge @23 + M-tails ALL
  NEW 16/16, T88-RING STANDARD sig 3f010000
  TM8 by COL + TR7 by ROW UNPAIRED 16/16 +
  SPLIT tails + b84-87 const bf2724fb, ring
  edges + thresholds 87/215, NO D dips).
- C diff pure-add: numstat 821/0 rgramc.c + 392/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 821
  content + 5 blank-only `+` lines / 0 del; raw py
  392 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 191, py del-uniq
  0 add-uniq 225). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope fe9d3bf0..
  d1c18b6c, 1276 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 821/0, rgram.py 392/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1790->1796 +6, singletons
  `if n == ` 666->668 +2, range-guards `<= n <=`
  720->724 +4, CLOSED T10P prints
  1790->1796 +6, seal 1884->1890
  +6 (cport msgs; offset +94 vs CLOSED-T10P stable
  b401-b425): all agree (stated literal methods,
  first-hand).
  C guards: singleton `if ((n) == (` 661->663 +2,
  range 720->724 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b423 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-823-q909
  memo CONFIRM 74/74 CLEAN (verifier v209.py 74/74
  PASS, tier GATED PORT, ZERO section-F, FRAG6
  tier; w2b-r27 [2/8], clean streak 14 straight,
  quoted verbatim).
  Viewer: NO P317 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P317. Agrees with cport commit msg
  (py/C 18816, PYID 9408).
- Quiz: no conflicting CLAIM/GATE/FLAG on b425/
  d1c18b6c. b424/b426 EVEN = sweep2 turf, used b424
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-23 (w2b Q-block refill only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r68/ (build425.log,
  b425-pyid.log, b425-py/c.log, pass425py/c.txt,
  seteq425.py/log, b425-smoke.log, b425-units.log,
  tables425.log, tabaudit425.py, edges425.py,
  edges425.log, cdiff425.txt, pydiff425.txt,
  banddiff425.txt, added425.txt, numstat425.txt,
  diffwall425.py/log, build425/ binaries,
  tail-127400.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
