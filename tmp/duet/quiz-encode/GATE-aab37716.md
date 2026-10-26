# GATE aab37716 b445 T10P337 pins 134013..134360 (348 pins) PASS-functional

Seat sweep-r73, first-hand, WT tmp/wt-encode-sweep @aab37716,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r73.
Band = 7d6a7d43 (py merge w2b@4f9b6df4 partial, +6 tiers
+62 pins) + aab37716 (C port). Base 97803743 (b444 tip,
2004 tiers sealed).

- Build: make -C src/c BUILDDIR=r73/build445 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build445/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r73, sha256 matches b354-b445
  pinned value; band touches no aae sources), rgramc
  sha1 480f7de6 / sha256 b7e51fa7.
- RGRAMC-PYID 10032/10032 covered=10032/10032 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 20064/20064 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME).
- RGRAM C 20064/20064 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (20064/20064, sorted).
- PINS-RGRAM cells set-eq 10032/10032 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 20066 lines (2 hdr + 20064 rows, +62 vs base 20004).
  For-list union 10001->10032 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (134013 134014) +
  A 6 (head 134015 + 134016 + 134022 + 134023 +
  134029 + tail 134030; offs 0,1,7,8,14,15) +
  C 6 (head 134031 + 134032 + 134035 + 134036 +
  134039 + tail 134040; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 134033, 134034, 134037,
  134038) +
  Q 10 (head 134041 + row0-mid 134048 + boundary
  pairs 134056/134057 + 134072/134073 +
  134088/134089 + row3-mid 134096 + tail 134104;
  offs 0,7,15,16,31,32,47,48,55,63; dual-mid
  off7+off55, precedented P333, first-hand) +
  R 7 (head 134105 + edge pair 134143/134144 +
  mid 134207 + edge pair 134271/134272 + tail
  134360; offs 0,38/39,102,166/167,255; 1-mid
  shape off102 NEW, both counter edges pair-covered,
  first-hand).
  PINS adds = same 31 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 31x2 = 62
  = 20064-20002.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P337 C-vs-py, 12-table A-PBA88-STEP-
  M7b52/C10-1SIG-88-TAIL-M4/QUAD88-1SIG-4R-NOFRAG-
  C87+T88-RING-STANDARD layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs aefd4106 NEW-family / 0c000000 NEW;
  S0 diff vs P336S0 32/84 @ b0-2,4,5,19-31,36,37,
  60-71 incl NEW-sig b0-2 NOT byte-equal +
  S1 diff vs P336S1 58/88 @ b0,4,5,19,26-75,84-87
  incl sig b0 NOT byte-equal +
  S1 diff vs own C10 cells [43,43,43,43,43,43,
  43,43,43,43] TRUE UNIFORM all 10 (cell0 @ b4,
  5,38,39,45-79,84-87; sig b0-3 same-sig NOT
  in diff), NOT byte-equal);
  AM 16/16 (7B), CM 10/10 (4B), M 16/16 (8B),
  QR 4/4 (3B), RM 16/16 (6B), RQ 16/16 (8B)
  EXACT;
  AC 79/79, CC 82/82, QC 75/75, RC 72/72 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 79/82/75/72 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit445.py 412 PASS 0 FAIL).
  NO F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R3 carries b84-86 inside QR); table
  inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-9 [4,5,52,53,
  54,80,81,82,83] = b4,b5+M7 (b52-54,80-83);
  CC-6 [4,5,84,85,86,87] = b4,b5+M4 (b84-87
  tails-only, full sig b0-3 in CC = 0c,00,00,00 ->
  0c000000 x10 SAME-as-PB1-sig; b86,87 NOT const
  in CC);
  QC-13 [4,5,6,7,8,9,80,81,82,83,84,85,86]
  = b4,b5+QM8 (b6-9,80-83)+R3 (b84-86; b0 const
  c3 in QC = 1SIG, b1-3 const 00; b87 const d1
  quad-wide in QC);
  RC-16 [4,5,6,7,8,9,13,14,76,77,78,79,80,81,
  82,83] = b4,b5+TR8 (b6-9,76-79)+TM6
  (b13,14,80-83).
  STEP first-hand: AC b0..b3 = 8d,00,00,00 ->
  sig 8d000000 x16, b0 const 8d; AM 16/16
  distinct; b5 STEP 16->17 @off0/1 (NOT const).
  TAIL-M4 first-hand (precedented: TAIL-M4 on file
  per GATE-3c686253, no FIRST claimed): CC b0-3
  full sig 0c000000 x10 SAME-as-PB1-sig (S1
  sig-eq own C10); CM 10/10 diverge; b5
  const 17.
  Code AC79/CC82/QC75/RC72; incl = +0/+1/+1/+0
  (A b5 STEP 16->17 vary, C b5 const 17, Q b5
  const 17, T counter) = 79/83/76/72; lane
  consts = A-895 INCL EXACT (deduct-b5-only-
  when-b5vary rule holds; A-1049 excl 79/82/75/
  72 = code EXACT).
  VPOS 9/5/12/16 = memo EXACT (A b4,b5+M7 b5-STEP
  varies; C b4+M4; Q b4+QM8+R3; T b4,b5+TM6+TR8).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3370 n==134013 / P3371
  n==134014 singleton-const (offs 0/1; 84B/88B);
  P337A 134015..134030 off=n-134015 PBA88-STEP-
  M7b52 (m-tab 7B b52-54,80-83, sig 8d000000,
  b0 const 8d, b5 STEP 16->17 @off0/1);
  P337C 134031..134040 off=n-134031 C10-1SIG-88-
  TAIL-M4 (m-tab 4B b84-87, full sig b0-3
  in CC = 0c000000, b5 const 17);
  P337Q 134041..134104 off=n-134041 m=off&15
  q=off>>4 QUAD88-1SIG-4R-NOFRAG-C87
  1-sig c3000000 x64 (b0 const c3 in QC)
  (M 8B b6-9,80-83 QM8 shared NO frags +
  R3 b84-86 r0 3ed720 / r1 372e21 / r2 572e21
  / r3 772e21 exact tuples, r0 TRUE 1B d1 vs
  all + r123 TRUE 3B 2e21d1 + b87 CONST d1
  quad-wide (precedented: C87-const on file in
  6 GATEs incl b440/b442 evens, no FIRST
  claimed), full-tail b84-87 (R3-C87 rule per
  GATE-a69ef1d1: tails = row + const b87)
  TAIL4-substr = TSHARE = subseq = 1/1/1/3/3/3
  (= A-1049 suffix-lcs at all 3 metrics),
  b5 const 17 NO edge, b4 0x33+2off range
  33..b1, NO frags);
  P337R(T88-ring) 134105..134360 off=n-134105
  c=off&15 r=off>>4 STANDARD-split sig 1b0c0000
  (TM 6B b13,14,80-83 by COL + TR 8B b6-9,
  76-79 by ROW SPLIT tails UNPAIRED 16/16,
  b0 const 1b, b84-87 const 972e21d1);
  A/C paylen 88 / raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (A b5
  STEP emerges from raw lencode; C b5 const
  emerges from raw lencode);
  Q paylen 88 / raw lencode (b5 const emerges
  from raw lencode 64/64);
  R paylen 88 +
  counter b4=(0xb3+2off)&FF b5=0x17+(off>=39)+
  (off>=167).
  C blocks carry T90031/90036/90041/90056/90071/
  90090 py-line mirrors (exact); guards
  `if ((n) == (134013))` / `if ((n) == (134014))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; ring counter 179+2*off + 23+(off>=39)+
  (off>=167); temps _t6845.._t6860 appended
  (base max _t6844, no reuse);
  _i band 4147,4149,4152,4155 (base max _i4145),
  _b band 4146,4148,4150,4151,4153,4154 (base
  max _b4144), union 4146-4155 contiguous, no
  reuse; C byte-index lists match py per block
  (A 7B, C 4B, Q 8B/3B, R 6B/8B STANDARD
  tails-split); insert position exact (P336R
  block precedes, P337R immediately precedes
  LAST scope-hit; C has 2 scope hits; py has 2
  scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0 3ed720; r1
  372e21; r2 572e21; r3 772e21);
  QR full-tail shares: r0 TRUE 1B d1 (b87) +
  r123 TRUE 3B 2e21d1 (@b84,85,86) (memo
  substance confirmed);
  RQ==M FULL8-diagonal (M 8B vs RQ 8B same-lanes
  b6-9: agree all 8 columns 16/16 each; full-row
  sets EQUAL; +2 one-byte off-diagonal strays
  (3,6):1 (6,3):1; NOT full-identity, tabs
  differ) -- 40th odd-band RQ==M instance, 6th
  FULL8-diagonal agreement (5 FULL8 on file, all
  full-identity per GATE-a60294b6; sweep column-
  agreement FULL8 + same-lanes => ordered per
  cport-r57 lesson (d); width predictor
  REWRITTEN round r57, no width rule cited);
  tails STANDARD-split (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P336T-STANDARD RM
  col-led tails (overlap 0; P336T STANDARD frame
  first-hand from code, ref = RM col-led 8B rows,
  position-aware tails last-4B);
  RM-tails (b80-83) ALL NEW vs P336T RM col-led
  tails (overlap 0);
  S0 string 32/84 differ vs P336S0 (NEW-family
  incl sig b0-2; @ b0-2,4,5,19-31,36,37,60-71)
  +
  S1 string 58/88 differ vs P336S1 (incl sig b0;
  @ b0,4,5,19,26-75,84-87; [43x10] vs own C10
  TRUE UNIFORM -- 14th TRUE-uniform case, first
  43-wide: no [43x10] on file);
  S1 NOT sig-EQ P336C10 (0c000000 vs 0e000000
  DIFFSIG-kept, 53 diff vs P336C10[0]; per
  cport-r57 lesson (h) nothing to assert);
  P337 actuals (S0 aefd4106/S1 0c000000/PBA88
  8d000000/C10 0c000000 x10 SAME-as-PB1-sig +
  PB0-vs-P336PB0 32/84 + PB1-vs-P336PB1 58/88)
  == A-890 + A-1048 predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head ff/16 (134015)
  STEP->01/17 (134016) tail 1d/17 (134030),
  b5set {16,17}; C head 1f/17 (134031) tail
  31/17 (134040), b5set {17};
  Q head 33/17 (134041) tail b1/17 (134104),
  b5set {17};
  quad b4=(0x33+2off) 64/64 contig+2 range
  33..b1 + b5 const 64/64;
  T head b3/17 (134105) + off38/39 (134143->
  134144) ff/17->01/18 + mid off102 7f/18
  (134207) + off166/167 (134271->134272)
  ff/18->01/19 + tail off255 b1/19 (134360).
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 134360 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  f72df124968d743a matches PINS rawlen 104,
  py+C CLOSED T10P337R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand (346 + S0/S1
  embedded b4/b5 fb/16 + fd/16).
  Matches A-895 geometry (framing 1x84+347x88 pay =
  code dispatch 1+1+16+10+64+256 = 348 pins,
  PB0 aefd4106 NEW-family 32/84 + PB1 0c000000
  NEW 58/88 + SAME-as-own-C10 43/88 + differs-
  vs-own-PB0,
  PBA88-STEP-M7b52 VPOS 9 b5 STEP 16->17,
  C10-1SIG-88-TAIL-M4 VPOS 5 b5 const 17,
  QUAD88-1SIG-4R-NOFRAG-C87 VPOS 12 =
  b4,b5+QM8+R3 + R3 4/4 UNPAIRED exact tuples +
  r0-TRUE1/r123-TRUE3 + b0 const in QC + b87
  const d1 quad-wide + b5 const NO edge + M-tails
  ALL NEW 16/16,
  T88-RING-STANDARD sig 1b0c0000 TM6 by COL +
  TR8 by ROW UNPAIRED 16/16 + SPLIT tails +
  b84-87 const 972e21d1, ring edges + thresholds
  39/167, NO D dips) + A-1049 (suffix-lcs
  1/1/1/3/3/3 = TAIL4 full-tail b84-87 all 3
  metrics first-hand; consts excl 79/82/75/72
  = code EXACT).
- C diff pure-add: numstat 608/0 rgramc.c + 231/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 608
  content + 5 blank-only `+` lines / 0 del; raw py
  231 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 144, py del-uniq
  0 add-uniq 167). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 97803743..
  aab37716, 902 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 608/0, rgram.py 231/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1910->1916 +6, singletons
  `if n == ` 706->708 +2, range-guards `<= n <=`
  800->804 +4, CLOSED T10P prints
  1910->1916 +6, seal 2004->2010
  +6 (cport msgs; offset +94 vs CLOSED-T10P stable
  b401-b445): all agree (stated literal methods,
  first-hand).
  C guards: singleton `if ((n) == (` 701->703 +2,
  range 800->804 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b443 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-895-q1049
  memo CONFIRM 59/59 CLEAN (Verifier v281.py 59/59
  PASS; tier GATED PORT; novelty gated b87 CONST
  d1 quad-wide (R3 tails + const b87); w2b-r29
  6/8, cited from body read first-hand) +
  A-1049-q1049 memo CONFIRM 46/46 CLEAN (Verifier
  v600f3.py 46/46 PASS; tier GATED PORT;
  w2b-r29 6/8, cited from body read first-hand).
  Viewer: NO P337 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P337 (3 DISSENT files on file are
  T10P923/924/926 far-future, withdrawn Qs, checked
  not applicable). Agrees with cport commit msg
  (py/C 20064, PYID 10032).
- Quiz: no conflicting CLAIM/GATE/FLAG on b445/
  aab37716 (quiz poll + filename grep first-hand).
  b444/b446 EVEN = sweep2 turf, used b444 tip as
  diff-base only, NOT gated.
  Newest PARENT-* is 081-remount2-resume (read) +
  QNUM-25 (w2e Q-block refill only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r73/ (build445.log,
  b445-pyid.log, b445-py/c.log, pass445py/c.txt,
  seteq445.py/log, b445-smoke.log, b445-units.log,
  tabaudit445.py/log, values445.py/log, edges445.py/
  log, banddiff445.txt, added445.txt, numstat445.txt,
  diffwall445.py/log, build445/ binaries,
  tail-134360.rav, for445-base.sh, pins445-base.csv,
  c445-base.c, py445-base.py).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
