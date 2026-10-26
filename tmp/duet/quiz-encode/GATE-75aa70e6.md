# GATE 75aa70e6 b421 T10P313 pins 125661..126008 (348 pins) PASS-functional

Seat sweep-r67, first-hand, WT tmp/wt-encode-sweep @75aa70e6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r67.
Band = cc6d8b7a (py merge w2b@6902f10c partial, +6 tiers
+62 pins) + 75aa70e6 (C port). Base 307c9f53 (b420 tip,
1860 tiers sealed).

- Build: make -C src/c BUILDDIR=r67/build421 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build421/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r67, sha256 matches b354-b421
  pinned value; band touches no aae sources), rgramc
  sha1 f183794f / sha256 80ca72fc.
- RGRAMC-PYID 9277/9277 covered=9277/9277 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18554/18554 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18554/18554 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (18554/18554, sorted).
- PINS-RGRAM cells set-eq 9277/9277 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 18556 rows (2 hdr + 18554, +62 vs base 18494).
  For-list union 9246->9277 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (125661 125662) +
  A 6 (head 125663 + 125664 + 125670 + 125671 +
  125677 + tail 125678; offs 0,1,7,8,14,15) +
  C 6 (head 125679 + 125680 + 125683 + 125684 +
  125687 + tail 125688; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 125681, 125682, 125685,
  125686) +
  Q 10 (head 125689 + edge pair 125695/125696 +
  off16 125705 + off23 125712 + off32 125721 +
  off39 125728 + off48 125737 + off55 125744 +
  tail 125752; offs 0,6,7,16,23,32,39,48,55,63;
  EARLY step edge off6->7 pair-covered, tail
  single off63, first-hand) +
  R 7 (head 125753 + edge pair 125823/125824 +
  mid 125850 + edge pair 125951/125952 + tail
  126008; offs 0,70/71,97,198/199,255; 1-mid
  shape, both counter edges pair-covered,
  first-hand).
  PINS adds = same 31 tier pins (2 rows each).
  Each for-N yields 2 PASS lines; 31x2 = 62
  = 18554-18492.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P313 C-vs-py, 12-table A-PBA88-PLAIN/
  C10-1SIG-88/QUAD88-2SIG-STEP+T88-RING-STANDARD layout,
  all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs 97016d01 NEW / 02000000;
  S0 diff vs P312S0 33/84 @ b0-2,4,5,11,19-31,
  36,37,52-55,68-75 NOT byte-equal + S1 diff vs
  P312S1 47/88 @ b4,5,19,26-35,37-44,46-59,
  72-79,84-87 NOT byte-equal +
  S1 diff vs own C10 cells [20,21,21,21,21,21,
  21,21,21,21] NON-uniform (cell0 @ b4,38,39,
  46-55,60-63,84,85,86), NOT byte-equal);
  AM 16/16 (7B), CM 10/10 (6B), M 16/16 (6B),
  QR 4/4 (12B), RM 16/16 (7B), RQ 16/16 (6B)
  EXACT;
  AC 79/79, CC 80/80, QC 68/68, RC 73/73 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 79/80/68/73 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit421.py 105 PASS 0 FAIL).
  No F/F0/F1 (no frags), no BM/BC (C10, not B10),
  no M19/X19, no M42/X42/H42/L42, no QB/PT/FM,
  no RT/TT (ring, not ROWTAIL), no QT (R12 carries
  b84-87 inside QR); table inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-9 [4,5,52,53,
  54,80,81,82,83] = b4,b5+M7 (b52,53,54,
  80-83);
  CC-8 [4,5,52,53,84,85,86,87] = b4,b5+M6 (b52,
  53,84-87, full sig b0-3 in CC = 02,00,00,00 ->
  02000000 x10);
  QC-20 [0,4,5,6,7,19,50,51,52,53,54,55,80,81,
  82,83,84,85,86,87] = b0,b4,b5+QM6 (b6,7,
  80-83)+R12 (b0,19,50-55,84-87; b1,b2,b3
  const 00 in QC);
  RC-15 [4,5,6,7,13,14,15,76,77,78,79,80,81,
  82,83] = b4,b5+TR6 (b6,7,76-79)+TM7
  (b13,14,15,80-83).
  PLAIN first-hand: AC b0..b3 = 26,00,00,00 ->
  sig 26000000 x16, b0 const 26; AM 16/16
  distinct; b5 const d5.
  1SIG first-hand: CC b0-3 full sig 02000000
  x10 SAME-as-PB1-sig (S1 sig-eq own C10); CM
  10/10 diverge; b5 const d5, NO step; 10/10
  diverge.
  Code AC79/CC80/QC68/RC73; incl = +1/+1/+0/+0
  (A b5 const d5, C b5 const d5, Q b5 step, T
  counter) = 80/81/68/73; lane consts =
  A-808 INCL EXACT (deduct-b5-only-when-b5vary
  rule holds).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3130 n==125661 / P3131
  n==125662 singleton-const (offs 0/1; 84B/88B);
  P313A 125663..125678 off=n-125663 PBA88-PLAIN
  (m-tab 7B b52,53,54,80-83, sig 26000000, b0
  const 26, b5 const d5);
  P313C 125679..125688 off=n-125679 C10-1SIG-88
  (m-tab 6B b52,53,84-87 M6, full sig b0-3 in CC =
  02000000, b5 const d5, NO step);
  P313Q 125689..125752 off=n-125689 m=off&15
  q=off>>4 QUAD88-2SIG-STEP r0 24000000 x16 +
  r123 20000000 x48
  (M 6B b6,7,80-83 QM6 shared across sig boundary
  NO frags + R12 b0,19,50-55,84-87 r0
  242ba68df1e0ef616771577d distinct / r123 share
  8B 20ad2a1e91b89fca, tails b84-87 4 distinct
  f46e6463/196f6463/3e6f6463/6771577d, r2r3 TRUE
  3B 6f6463 (differ b84 19/3e), r1 2B 6463 vs
  r2/r3, r0 lcs=0 vs all, b0 row-led split
  r0=24 r123=20, b5 0xd5+(off>=7) EARLY step
  off6->7 ff/d5->01/d6, b4 0xf3+2off base
  0xf3 step2);
  P313R(T88-ring) 125753..126008 off=n-125753
  c=off&15 r=off>>4 STANDARD sig 38020000 (TM
  7B b13,14,15,80-83 by COL + TR 6B b6,7,76-79
  by ROW SPLIT tails UNPAIRED 16/16, b84-87
  const cb/ed/69/82);
  A/C/Q paylen 88 / raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (b5-step/
  const emerges from raw lencode);
  R paylen 88 +
  counter b4=(0x73+2off)&FF b5=0xd6+(off>=71)+
  (off>=199).
  C blocks carry T84222/84227/84232/84247/84262/
  84283 py-line mirrors (exact); guards
  `if ((n) == (125661))` / `if ((n) == (125662))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 115+2*off + 214+(off>=71)+
  (off>=199); temps _t6441.._t6456 appended
  (base max _t6440, no reuse); _i band 3906,
  3908,3911,3914 (base max _i3904), _b band
  3905,3907,3909,3910,3912,3913 (base max
  _b3903), no reuse; C byte-index lists match py
  per block (A 7B, C 6B, Q 6B/12B, R 7B/6B
  STANDARD tails-split); insert position exact
  (P312R block precedes, N out-of-scope follows;
  C has 2 scope hits; py has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0 242ba68df1e0ef61
  6771577d; r1 20ad2a1e91b89fcaf46e6463; r2
  20ad2a1e91b89fca196f6463; r3 20ad2a1e91b89fc
  a3e6f6463);
  QR tail-shares: r2r3 TRUE 3B 6f6463, r1 2B
  6463 suffix, r0 lcs 0 vs all;
  RQ==M FULL6 (M 6B vs RQ 6B: agree (0,0),(1,1),
  (2,2),(3,3),(4,4),(5,5) 16/16 each; tabs
  byte-identical; maxagree 16 all 6) -- 2nd
  full-identity instance (after P311; QM6 byte
  positions b6,7,80-83, TR6 positions b6,7,
  76-79);
  28th odd-band RQ==M instance;
  tails STANDARD-split (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P312T RM col-led tails
  (overlap 0); RM-tails (b80-83) ALL NEW vs P312T
  RM col-led tails (overlap 0); RQ-tails (b76-79)
  ALL NEW vs P312T RQ row-led tails (overlap 0);
  cross overlaps 0 (P312T widths RM 8B/RQ 6B
  STANDARD first-hand);
  S0 NEW string (33/84 differ vs P312S0 @ b0-2,4,5,
  11,19-31,36,37,52-55,68-75) + S1 NEW string
  (47/88 differ vs P312S1 @ b4,5,19,26-35,37-44,
  46-59,72-79,84-87; [20,21x9] NON-uniform vs
  own C10, cell0 @ b4,38,39,46-55,60-63,84,85,
  86; memo's PB1-vs-C10[0] 20/88 matches cell0);
  P313 actuals (S0 97016d01/S1 02000000/PBA88
  26000000/C10-1SIG 02000000 x10 SAME-as-PB1-sig
  + PB1-vs-P312PB1 47/88) == A-806 predicted next
  EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head bf/d5 (125663)
  tail dd/d5 (125678), b5set {d5}; C head
  df/d5 (125679) tail f1/d5 (125688), b5set
  {d5};
  Q head f3/d5 (125689) edge off6->7
  (125695->125696) ff/d5->01/d6 tail 71/d6
  (125752), b5set {d5,d6};
  quad b4=(0xf3+2off) 64/64;
  T head 73/d6 (125753) + off70/71 (125823->
  125824) ff/d6->01/d7 + mid off97 35/d7
  (125850) + off198/199 (125951->125952)
  ff/d7->01/d8 + tail off255 71/d8 (126008).
  All edge pins in for-list + PASS (batteries
  GREEN); 126008 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  43e0be68514dbb4d... matches PINS rawlen 104,
  py+C CLOSED T10P313R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand (346 + S0/S1
  embedded b4/b5 bb/d5 + bd/d5).
  Matches A-808 geometry (novel 1x84+347x88 framing
  PINS-sampled 100x1+104x30 + code paylens 84/88,
  PB0 97016d01 NEW + PB1 02000000 sig-eq-P312PB1
  47/88 + SAME-as-own-C10 20/88,
  PBA88-PLAIN VPOS 8 b5 const d5,
  C10-1SIG-88 VPOS 7 b5 const d5 10/10 diverge,
  QUAD88-2SIG-STEP VPOS 20 QM6+R12 + R12 4/4
  UNPAIRED + tails 4 distinct r2r3-TRUE3/r1-2B/
  r0-lcs0 + b0 row-led split + EARLY step edge +
  M-tails ALL NEW 16/16, T88-RING STANDARD sig
  38020000 TM7 by COL + TR6 by ROW UNPAIRED
  16/16 + SPLIT tails + b84-87 const
  cbed6982, ring edges + thresholds 71/199,
  NO D dips).
- C diff pure-add: numstat 608/0 rgramc.c + 233/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 608
  content + 5 blank-only `+` lines / 0 del; raw py
  233 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 149, py del-uniq
  0 add-uniq 180). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 307c9f53..
  75aa70e6, 904 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 608/0, rgram.py 233/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1766->1772 +6, singletons
  `if n == ` 658->660 +2, range-guards `<= n <=`
  704->708 +4, CLOSED T10P prints
  1766->1772 +6, seal 1860->1866
  +6 (cport msgs; offset +94 vs CLOSED-T10P stable
  b401-b421): all agree (stated literal methods,
  first-hand).
  C guards: singleton `if ((n) == (` 653->655 +2,
  range 704->708 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b419 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-808-q905
  memo CONFIRM 61/61 CLEAN (section heads shape
  30/30 + quad+T 17/17 + counters 14/14
  quoted verbatim; ZERO section-F; tier cut SAFE;
  w2b-r26 [6/8]; Port verdict: 10th straight fully
  clean w2b sheet).
  Viewer: NO P313 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P313. Agrees with cport commit msg
  (py/C 18554, PYID 9277).
- Quiz: no conflicting CLAIM/GATE/FLAG on b421/
  75aa70e6. b420/b422 EVEN = sweep2 turf, used b420
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-22 (w2e Q-block refill only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r67/ (build421.log,
  b421-pyid.log, b421-py/c.log, pass421py/c.txt,
  seteq421.py/log, b421-smoke.log, tables421.log,
  tabaudit421.py, edges421.py, edges421.log,
  cdiff421.txt, pydiff421.txt, banddiff421.txt,
  added421.txt, numstat421.txt, diffwall421.py/log,
  build421/ binaries, tail-126008.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
