# GATE 0bf51d2c b469 T10P361 pins 142365..142712 (348 pins) PASS-functional

Seat sweep-r79, first-hand, WT tmp/wt-encode-sweep @0bf51d2c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r79.
Band = 3226e14d (py merge w2b@902bea99, +6 tiers
+58 pins) + 0bf51d2c (C port). Base 97337e61 (b468 tip,
2148 tiers sealed).

- Build: make -C src/c BUILDDIR=r79/build469 aae rgramc
  (absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build469/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r79, sha256 = b354-b461 pinned
  value, verified this band; band touches no aae
  sources), rgramc
  sha1 9530fc99 / sha256 7546e4c2 (new value: band
  touches C sources, recorded first-hand).
- RGRAMC-PYID 10742/10742 covered=10742/10742 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 21484/21484 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME;
  10742 pins x2 open+closed).
- RGRAM C 21484/21484 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (21484/21484, sorted, cmp-equal first-hand).
- PINS-RGRAM cells set-eq 10742/10742 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 21486 lines (2 hdr + 21484 rows, +58 vs base 21428).
  For-list union 10713->10742 +29/-0 (python sets,
  trailing-';' strip, never comm).
  29 = 2 sing (142365 142366; offs 0,1) +
  A 6 (head pair 142367 + 142368 + mid pair 142374 +
  142375 + tail pair 142381 + 142382; offs 0,1,7,8,
  14,15; offs 2-6,9-13 unsampled:
  142369-142373, 142376-142380; NO mid-single,
  b5 const NO edge, first-hand) +
  C 6 (head pair 142383 + 142384 + mid pair 142387 +
  142388 + tail pair 142391 + 142392; offs 0,1,4,5,
  8,9; offs 2,3,6,7 unsampled: 142385, 142386,
  142389, 142390; b5 const NO edge, first-hand) +
  Q 8 (head 142393 + boundary pairs 142408/142409 +
  142424/142425 + 142440/142441 + tail 142456;
  offs 0,15,16,31,32,47,48,63; NO mid (b5 const
  58 NO edge), all boundaries pair-covered,
  first-hand) +
  R 7 (head 142457 + edge pair 142463/142464 +
  mid 142530 + edge pair 142591/142592 + tail
  142712; offs 0,6,7,73,134,135,255; 1-mid
  shape off73 NEW, both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58
  = 21484-21426.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P361 C-vs-py, 12-table A-PBA88-PLAIN-
  M8b52/C10-1SIG-88-M5b52/QUAD88-1SIG-QM8/R2-NOEDGE/
  T88-STANDARD-split-TM7/TR8 layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs ef9ea60c NEW-sigdiff-3 / 1d000000 NEW-sig;
  S0 diff vs P360S0 32/84 @ 0-2,4,5,19-31,36,37,
  60-71 (sig b0-2 IN diff, b3 same, NOT byte-equal) +
  S1 diff vs P360S1 58/88 @ 0,4,5,11,19,26-44,
  46-75,84-87 (sig b0 IN diff, b1-3 same-sig NOT
  in diff, NOT byte-equal) +
  S1 diff vs own C10 cells NOT-UNIFORM (cell 0 diff
  40 @ 4,19,38,39,46,48-51,53-79,84-87; cells 1-9
  diff 41, extra [52] = b52 2-valued mid-body M;
  sig b0-3 same-sig NOT in diff, SIG-EQ own C10;
  40/88 == A-948 predicted EXACT; S1[52]=0x92
  matches CM cell-0 b52 first-hand) +
  S1 vs P360C10[0] 52/88 (P360C10 sig 18000000
  DIFFERS-sig, payload differs));
  AM 16/16 (8B), CM 10/10 (5B M5), M 16/16 (8B
  QM8), QR 4/4 (2B R2), RM 16/16 (7B), RQ
  16/16 (8B) EXACT;
  AC 78/78, CC 81/81, QC 76/76, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 78/81/76/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit469.py 464 PASS 0 FAIL).
  13 py symbols = 12 tables + _T10P361C numeric-head
  probe (74 entries py = 74 C _T10P361C_N; table +
  probe pre-exist since band29/81c73cb3, precedent
  P360 _C on file, NOT a FIRST).
  NO F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R2 carries b84,85 in-row + b86/b87
  consts); table inventory exactly the 12 + _C.
  Missing-sets first-hand EXACT: AC-10 [4,5,52,53,
  54,55,80,81,82,83] = b4,b5+M8 (b52-55,80-83;
  full sig b0-3 in AC = ff,01,00,00 ->
  ff010000 x16, b0 const ff);
  CC-7 [4,5,52,84,85,86,87] = b4,b5+M5 (b52,84-87;
  b52 2-valued mid-body [0x92,0xb2] first-hand;
  full sig b0-3 in CC = 1d,00,00,00 -> 1d000000
  x10 SAME-as-PB1-sig);
  QC-12 [4,5,6,7,9,10,80,81,82,83,84,85] =
  b4,b5+QM8 (b6,7,9,10,80-83)+R2 (b84,85;
  b0-3 const d6,01,00,00 -> d6010000 x64 1SIG
  SAME-shape-as-PBA-family; b86 const 0xf9 +
  b87 const 0x5d quad-wide);
  RC-17 [4,5,6,7,9,10,13,14,15,76,77,78,79,80,
  81,82,83] = b4,b5+TR8 (b6,7,9,10,76-79)+TM7
  (b13,14,15,80-83).
  M8b52 shape filed (b461 T10P353 GATE-238ba34c,
  no FIRST claimed); M5b52 + b52-2-valued filed
  (b461, no FIRST claimed); QM8 shape filed (b461
  lanes b6-9; here lanes b6,7,9,10 -- lane-set
  differs, shape filed, no FIRST claimed); TM7/TR8
  shapes + STANDARD-split filed (b461; lanes differ
  here, no FIRST claimed).
  Code AC78/CC81/QC76/RC71 = A-948 EXCL 78/81/76/71
  EXACT (+0 all four; memo notes incl +3 for the
  three b5-const regions A/C/Q -- deduct-only-when-
  vary holds, T counter varies, no deduction; Q
  b5-const here vs Q-steps at b461).
  VPOS 9/6/11/17 derived first-hand (VPOS =
  varying-of-{b4,b5} + mtab + rtab: A 1+8+0
  (b4+M8, b5 const); C 1+5+0 (b4+M5, b5 const);
  Q 1+8+2 (b4+QM8+R2, b5 const); T 2+7+8
  (b4,b5+TM7+TR8)).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3610 n==142365 /
  P3611 n==142366 singleton-const (offs 0/1; 84B/88B;
  T95592/T95597 py-line mirrors);
  P361A 142367..142382 off=n-142367 PBA88-PLAIN-
  M8b52 (m-tab 8B b52-55,80-83, sig ff010000,
  b0 const ff, raw lencode b4=(0x3f+2off)&FF
  b5 const 58 NO step NO edge; T95602);
  P361C 142383..142392 off=n-142383 C10-1SIG-88-
  M5b52 (m-tab 5B b52,84-87, b52 2-valued
  mid-body, full sig b0-3 in CC = 1d000000,
  raw lencode b5 const 58 NO step NO edge; T95617);
  P361Q 142393..142456
  off=n-142393 m=off&15 q=off>>4 QUAD88-1SIG-
  QM8/R2-NOEDGE 1-sig d6010000 x64 (b0-3 const
  d6,01,00,00 in QC = SAME-shape-as-PBA-family)
  (M 8B b6,7,9,10,80-83 QM8
  shared + R2 b84,85 r0 a3ac / r1 c3ac / r2
  e3ac / r3 03ad exact tuples + b86 const 0xf9
  + b87 const 0x5d quad-wide (TAIL4 trailing =
  TSHARE = subseq = 3/3/2/3/2/2, all-3 agree,
  pairs (0,1)/(0,2)/(1,2) trailing 3 rest 2,
  full tuples pairwise unequal, first-hand),
  raw lencode b4=(0x73+2off) b5 const 58 NO
  edge; T95632);
  P361R(T88-ring) 142457..142712 off=n-142457
  c=off&15 r=off>>4 STANDARD-split sig 261d0000
  (TM7 7B b13,14,15,80-83 by COL + TR8 8B b6,7,
  9,10,76-79 by ROW SPLIT tails UNPAIRED 16/16,
  b0 const 26, b84-87 const 23adf95d ring-wide;
  T95652);
  A/C paylen 88 / raw lencode b4=(0x3f+2off)
  b5 const 58 (A) / raw lencode b5 const
  58 (C);
  Q paylen 88 / raw lencode b4=(0x73+2off)
  (b5 const 58 emerges from raw lencode 64/64);
  R paylen 88 +
  counter b4=(0xf3+2*off)&FF b5=0x58+(off>=7)+
  (off>=135).
  C blocks carry T95592/T95597/T95602/T95617/
  T95632/T95652 py-line mirrors (exact); guards
  `if ((n) == (142365))` / `if ((n) == (142366))`
  + 4 ranges `(142367)<=(n)<=(142382)` /
  `(142383)<=(n)<=(142392)` /
  `(142393)<=(n)<=(142456)` /
  `(142457)<=(n)<=(142712)` exact; ring
  counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 7/135 identical first-hand
  arithmetic, per-off values in edges log);
  quad counter==raw-lencode 64/64 b4 mismatches 0.
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (b52 2-valued [0x92,0xb2]
  mid-body M); M 16/16 distinct (8B);
  QR 4/4 distinct UNPAIRED (r0 a3ac; r1
  c3ac; r2 e3ac; r3 03ad);
  QR full-tail shares: trailing-suffix = TSHARE =
  subseq = 3/3/2/3/2/2, all-3 agree (pairs
  (0,1)/(0,2)/(1,2) trailing 3, rest 2;
  pairs share b86 const f9 + b87 const 5d;
  full tuples pairwise unequal, distinct 4);
  RQ==M FULL8 (code M 8B lanes [6,7,9,10,80-83]
  vs RQ 8B lanes [6,7,9,10,76-79]: rows 16/16
  EQUAL, all 8 cols 16/16 position-exact, col
  uniqs 14/12/3/2/16/16/16/15 both sides EQUAL,
  full-row sets EQUAL, sorted rows EQUAL) --
  52nd odd-band RQ==M instance, 10th FULL
  full-identity degree (FULL8-identity precedented,
  multiple on file; same-width 8B/8B, low lanes
  agree, tails b80-83 vs b76-79 differ); ordered
  per lesson (d);
  width predictor dead, never cited;
  tails STANDARD-split (TM7 b13,14,15,80-83 by COL
  c=off&15, TR8 b6,7,9,10,76-79 by ROW r=off>>4,
  16/16 distinct each, sequences UNPAIRED);
  M-tails (b80-83) 16/16 ALL NEW vs P360T RQ
  row-led tails (overlap 0; P360T RQ 16x6B frame
  first-hand from code, tails last-4B);
  RQ-tails (b76-79) 16/16 ALL NEW vs P360T RM
  col-led tails AND vs P360T RQ (overlap 0 both;
  P360T RM 16x9B frame first-hand from code,
  tails last-4B);
  RM-tails (b80-83) 16/16 ALL NEW vs P360T RM
  AND vs P360T RQ (overlap 0 both);
  S0 32/84 NEW-sigdiff-3 (b0-2 IN diff, b3 same) +
  S1 58/88 NEW-sig (b0 IN diff, b1-3 same) +
  S1-vs-own-C10 40/88 cell0 (41/88 cells 1-9 via
  b52) + S1-vs-P360C10[0] 52/88 DIFFERS-sig +
  S1 SIG-EQ own C10 (1d000000 both);
  P361 actuals (S0 ef9ea60c/S1 1d000000/PBA88
  sig ff010000 x16 b0 const ff + PB0-vs-P360PB0
  32/84 sigdiff-3 + PB1-vs-P360PB1 58/88 NEW-sig
  + S1-vs-own-C10 40/88 + M5-C10 1d000000 x10
  SAME-as-PB1-sig) == A-948 + Q-1073 predicted
  next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 3f/58 (142367)
  tail 5d/58 (142382), b5set {88} (decimal =
  0x58) NO edge;
  C head 5f/58 (142383) tail 71/58 (142392),
  b5set {88} (decimal = 0x58) NO edge;
  Q head 73/58 (142393) tail f1/58 (142456),
  b5set {88} (decimal = 0x58) NO edge, b4 range
  73..f1 contig+2 (no wrap, 64 distinct);
  T head f3/58 (142457) + off6/7 (142463->
  142464) ff/58->01/59 + mid off73 85/59
  (142530) + off134/135 (142591->142592)
  ff/59->01/5a + tail off255 f1/5a (142712).
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 142712 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  c3118d5e144a2757857d1e3d101446a9bca0fe62986
  cfdfff1bbe83d3ead1eee matches PINS rawlen
  104; PASS g-z142712 + g-z142712-closed in BOTH
  legs, sorted cmp-equal).
  Ring counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 7/135 identical first-hand
  arithmetic, per-off values in edges log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  band 29/348 pins in for-list, all PASSx2 both
  legs; full-tier 348/348 CLOSED via A-948 (writer
  bed 142365..142740 BAD=0 + verifier v501 50/50 +
  T10P361 N-start 142365 = 83553+(361-192)*348
  per Q-1073 first-hand).
  Matches A-948 geometry (framing 1x84+347x88 pay =
  code dispatch 1+1+16+10+64+256 = 348 pins,
  PB0 ef9ea60c NEW-sigdiff-3 32/84 + PB1 1d000000
  NEW-sig 58/88 + SAME-as-own-C10 40/88 +
  differs-vs-own-PB0,
  PBA88-PLAIN-M8b52 VPOS 9 b5 const 58,
  C10-1SIG-88-M5b52 VPOS 6 b5 const 58 b52
  2-valued,
  QUAD88-1SIG-QM8/R2-NOEDGE VPOS 11 =
  b4+QM8+R2 + R2 4/4 UNPAIRED exact tuples +
  trailing 3/3/2/3/2/2 all-3 agree + b86/b87
  consts f9/5d + M-tails ALL NEW 16/16,
  T88-STANDARD-split-TM7/TR8 sig 261d0000 TM7 by
  COL + TR8 by ROW UNPAIRED 16/16 + SPLIT tails +
  b84-87 const 23adf95d, ring edges + thresholds
  7/135, NO D dips) + A-948 (consts excl
  78/81/76/71 = lane EXACT).
- C diff pure-add: numstat 608/0 rgramc.c + 231/0
  rgram.py (+1/-1 for-line, +58/0 PINS); raw C 608
  = 603 content + 5 blank-only `+` lines / 0 del;
  raw py 231 content / 0 del; C legs touch ZERO
  PINS rows + ZERO for-line (add-only; sole del =
  old for-line churn, for-line 1/1).
  Normalized ([0-9]+ -> N, diff-sign strip) del-uniq
  0 (0 true `-` lines in C+py diffs).
- Wall on band diff added lines (scope 97337e61..
  0bf51d2c, 898 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits, aea-invoke 0
  hits (0 `aea' substrings, 0 invocations). Files
  touched: rgramc.c 608/0, rgram.py 231/0,
  test_rgram.sh 1/1, PINS 58/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 2054->2060 +6, singletons
  `if n == ` 754->756 +2, range-guards `<= n <=`
  896->900 +4, CLOSED T10P prints
  2054->2060 +6, seal 2148->2154
  +6 (cport msgs; offset +94 (base 2148-2054 and
  band 2154-2060 both +94 first-hand)).
  C guards: singleton `if ((n) == (` 749->751 +2,
  range `) <= (n)` 896->900 +4; 5-count C-vs-py
  singleton offset pre-existing (same C-only dip
  guards as b357-b467 odds + b452-b468 evens),
  unchanged by band.
  C byte-index lists match py per block
  (A 8B, C 5B, Q 8B/2B, R 7B/8B STANDARD
  tails-split); insert position exact (P360R
  block precedes, P361R immediately precedes
  LAST scope-hit; C has 2 scope hits; py has 2
  scope hits).
  Temps _t7229.._t7244 appended
  (base max use _t7228, 16 contiguous, no reuse);
  _i band 4387,4389,4392,4395 (base max _i4385),
  _b band 4386,4388,4390,4391,4393,4394 (base
  max _b4384), union 4386-4395 contiguous, no
  reuse.
- CONFIRM evidence: A-948-q1073 memo CONFIRM 50/50
  CLEAN (Verifier v501.py 50/50 PASS; tier GATED
  PORT; novelty M-tails 16/16 ALL NEW vs P360T
  row-led tails; w2b-r32 6/8; cited from body
  read first-hand).
  Q-1073 answered/drained by A-948; no 2nd
  (r6-side) CONFIRM for q1073 on file at gate
  time (viewer-r69 live @b444-b447, ~20 bands
  behind; filename survey first-hand).
  Viewer: NO P361 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order; NOTE-1073-viewer-
  heartbeat names no P361).
  No DISSENT on P361 (DISSENT files on file are
  T10P923/924/926 far-future, withdrawn Qs, checked
  not applicable); no FLAG names P361/b469/0bf51d2c
  (filename + body-grep survey first-hand). Agrees
  with cport commit msg (py/C 21484, PYID 10742).
- Quiz: no conflicting CLAIM/GATE/FLAG on b469/
  0bf51d2c (quiz poll + filename grep first-hand;
  GATE-0bf51d2c absent before filing).
  Newest PARENT-* QNUM-27 + 081-remount2-resume (no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r79/ (all *469* +
  builds, tail-142712 via ct-cache hit c3118d5e).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
