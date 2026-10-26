# GATE b9db70db b379 T10P271 pins 111045..111392 (348 pins) PASS-functional

Seat sweep-r56, first-hand, WT tmp/wt-encode-sweep @b9db70db,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r56.
Band = 876cc8fd (py merge w2b@e643e014 partial, +6 tiers
+66 pins) + b9db70db (C port). Base 9b8d6052 (b378 tip,
1608 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 (direct invocation,
  flags per r55 build373.log), build379/{aae,rgramc}, rc=0,
  0 warnings (empty build log). aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r56,
  sha256 matches b354-b379 pinned value; band touches no
  aae sources), rgramc sha1 0d53f79a / sha256 c4b6695e.
- RGRAMC-PYID 7965/7965 covered=7965/7965 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 15930/15930 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 15930/15930 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (15930/15930, sorted).
- PINS-RGRAM cells set-eq 7965/7965 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 15932 rows (2 hdr + 15930, +66 vs base 15866).
  For-list union 7932->7965 +33/-0 (python sets,
  trailing-';' stripped, never comm).
  33 = 2 sing (111045 111046) +
  A 8 split-aware (10-side head 111047 + 111048 +
  111055 + 111056 + 6-side head 111057 + 111058 +
  111061 + tail 111062; offs 0,1,8,9,10,11,14,15) +
  C 6 (head 111063 + 111064 + 111066 + 111069 +
  111071 + tail 111072; offs 0,1,3,6,8,9; offs
  2,4,5,7 unsampled: 111065, 111067, 111068,
  111070) +
  Q 10 (head 111073 + row-split pair 111088/111089 +
  row1-mid 111096 + step triple 111103/111104/111105
  + edge pair 111120/111121 + tail 111136; offs 0,
  15/16,23,30/31/32,47/48,63; b5 step off>=31) +
  R 7 (head 111137 + edge pair 111231/111232 + mid
  111280 + edge pair 111359/111360 + tail 111392;
  offs 0,94/95,143,222/223,255).
  PINS adds = same 33 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 33x2 = 66 = 15930-15864.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var).
- Tables audit P271 C-vs-py, 13-table A-PBA-SPLIT10/6/
  C10-1SIG/QUAD2s+T88 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 76270700 NEW 7627-family / fcec550e NEW, both
  NEW strings);
  AM 16/16 (9B), CM 10/10 (11B), M 16/16 (8B),
  QR 4/4 (6B), QT 4/4 (4B), RM 16/16 (6B), RQ 16/16
  (7B) EXACT;
  AC 73/73, CC 71/71, QC 64/64, RC 73/73 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 73/71/64/73 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit379.py 126 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42 (no b42 staging), no RT (STANDARD ring,
  not ROWTAIL), no QB/PT/FM; table inventory exactly
  the 13.
  Missing-sets first-hand EXACT: AC-11 [0,4,5,9,10,
  11,12,76,77,78,79] = b0,b4,b5+M8 (b9-12,76-79,
  split b0 in tab);
  CC-13 [4,5,13,14,15,16,17,18,19,80,81,82,83]
  = b4,b5+M11 (b13-19,80-83);
  QC-20 [0,1,2,4,5,12,13,14,16,17,18,19,76,77,
  78,79,80,81,82,83] = b4,b5+QM8 (b12-14,19,
  76-79)+R6 sig-led (b0-2,16-18)+T4 (b80-83);
  RC-15 [4,5,20,21,22,28,29,76,77,78,79,80,81,
  82,83] = b4,b5+TR7 (b20-22,76-79)+TM6
  (b28,29,80-83).
  SPLIT first-hand: AM b0 34 x10 (rows 0-9) + 20 x6
  (rows 10-15) ORDERED; AC b1-3 const cc5ee5 ->
  sigs 34cc5ee5 x10 / 20cc5ee5 x6; AM 16/16
  distinct.
  1SIG first-hand: CC b0-3 const c3ec550e (full sig
  const); CM 10/10 diverge.
  Code AC73/CC71/QC64/RC73; incl = +1/+1/+0/+0
  (A/C b5 const 63, Q b5-step, T counter) =
  74/72/64/73;
  lane consts = A-659/A-335 INCL EXACT (writer
  PBA/C10 = memo-1; quad/T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2710 n==111045 / P2711
  n==111046 singleton-const (offs 0/1);
  P271A 111047..111062 off=n-111047 PBA-SPLIT10/6
  (m-tab 9B b0,9-12,76-79 covers split, sigs
  34cc5ee5/20cc5ee5, b5 const 63);
  P271C 111063..111072 off=n-111063 C10-1SIG
  (m-tab 11B b13-19,80-83, b5 const 63
  NO carry);
  P271Q 111073..111136 off=n-111073 m=off&15
  q=off>>4 QUAD2s row-split c09ba7f8 x16 (row0) +
  009d17f8 x48 (rows1-3) (M 8B b12-14,19,76-79
  shared + R6 sig-led b0-2,16-18 r1==r2==r3
  LAST3-PAIRED + QT b80-83 r1/r2/r3 TRUE-3B
  d84934, b5 step off>=31);
  P271R(T88-ring) 111137..111392 off=n-111137
  c=off&15 r=off>>4 STANDARD sig 0e000000 (TM 6B
  b28,29,80-83 by COL + TR 7B b20-22,76-79 by
  ROW SPLIT tails UNPAIRED, b84-87 const
  f7/61/b2/5f);
  A/C paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (Q b5-step
  emerges from raw lencode); R paylen 88
  + counter b4=(0x43+2off)&FF b5=0x64+(off>=95)+
  (off>=223).
  C blocks carry T74163/74168/74173/74189/74205/
  74228 py-line mirrors (exact); guards
  `if ((n) == (111045))` / `if ((n) == (111046))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 67+2*off + 100+(off>=95)+
  (off>=223);
  temps _t5718.._t5735 appended (base max _t5717,
  no reuse); _i max 3467->3478 (band 3469,3471,
  3475,3478), _b max 3466->3477 (band 3468,3470,
  3472,3473,3474,3476,3477), no reuse;
  C byte-index lists match py per block (A 9B,
  C 11B, Q 8/6/4B, R 6/7B); insert position
  exact (dispatch tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (1SIG rows, all distinct);
  M 16/16 distinct;
  QR r1==r2==r3 LAST3-PAIRED exact (009d17da74de
  x3; r0 c09ba7a8f99b distinct); 2 distinct;
  QR sig-led (r0 head c09ba7 = row0 sig head,
  r123 head 009d17 = rows1-3 sig head);
  QT 4/4 distinct exact (d45a1a47/81d84934/
  a6d84934/cbd84934); r1/r2/r3 share TRUE 3B
  d84934 (first bytes 81/a6/cb differ, exactly
  3B); r0 last3B 5a1a47 differs;
  RQ==M MID+TAILS-SKIP FIRST (M 8B vs RQ 7B:
  bytes 1-2 identical 16/16 + tails RQ[3:7]==
  M[4:8] same-index 16/16 + set-eq, M byte 3
  dropped, b0 own all 16 with no small formula
  over (M0,M3): xor/add/sub+const brute force
  0/1536) -- new degree beyond the seven known
  instances (P253 DISJOINT, P255/P263/P267
  tails-only, P257/P259 prefix+suffix, P261/P265
  FULL-STRING, P269 HEAD-REMAP);
  tails SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P270T (overlap 0 vs
  P270 RM/RQ tail union; M-full also ALL NEW vs
  P270RQ, widths 16 vs 10 hex);
  QT 4/4 ALL NEW vs P270QT
  (ea14f78d/4e664444/73664444/98664444);
  RM ALL NEW vs P270RM.
  S0 NEW string (sig 76270700 NEW 7627-family;
  P270S0 sig a6930300 == A-653 predicted next
  PB0); S1 NEW string (sig fcec550e NEW; P270S1
  sig a5322507 == P269 C10 sig carried forward).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 8f/63 (111047)
  tail ad/63 (111062), b5set {63}; C head af/63
  (111063) tail c1/63 (111072), b5set {63} NO
  carry; Q head c3/63 (111073) step off30/31
  (111103->111104) ff/63->01/64 + off32 03/64
  (111105) + tail 41/64 (111136); quad formula
  ==raw-lencode 64/64 mismatches 0.
  T head 43/64 (111137) + off94/95 (111231->
  111232) ff/64->01/65 + off222/223 (111359->
  111360) ff/65->01/66 + mid off143 61/65
  (111280) + tail off255 41/66 (111392). All
  edge pins in for-list + PASS (batteries GREEN);
  111392 tail pinned + in for-list + PASS
  (direct first-hand: oracle sha 2dd0e7ad51b16b78...
  matches PINS, py+C CLOSED T10P271R off=255
  agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (8b/63, 8d/63) match raw
  lencode.
  Matches A-659/A-335 geometry (mixed-size 92x84B+
  256x88B, PB0 76270700 NEW 7627-family + PB1
  fcec550e NEW, PBA16-SPLIT10/6 VPOS 10 b5 const
  63 NO pair, C10-1SIG VPOS 12 b5 const 63 10/10
  diverge NO pair, QUAD2s VPOS 20 QM8 shared +
  2-sig row-split + R6 sig-led r1==r2==r3
  LAST3-PAIRED + tails 4/4 r123 TRUE-3B d84934
  + M-tails ALL NEW 16/16, T88-ring STANDARD sig
  0e000000 TM6 by COL + TR7 by ROW UNPAIRED
  16/16 + SPLIT tails + b84-87 const f761b25f,
  quad step + ring edges + thresholds 95/223,
  NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 239/0
  rgram.py (+1/-1 for-line, +66/0 PINS); raw C 605
  content + 5 blank-only `+` lines / 0 del; raw py
  239 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 172, py del-uniq
  0 add-uniq 196). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 9b8d6052..
  b9db70db, 916 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 610/0, rgram.py 239/0,
  test_rgram.sh 1/1 (for-line), PINS 66/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1514->1520 +6, singletons
  `if n == ` 574->576 +2, range-guards `<= n <=`
  536->540 +4, CLOSED T10P prints 1514->1520 +6,
  seal 1608->1614
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 569->571 +2,
  range 536->540 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b377 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-659-q783
  memo CONFIRM 37/37 (section heads shape 12/12 +
  quad+T-ring 13/13 + counters 12/12 quoted
  verbatim; tier cut SAFE)
  + A-335-q335 viewer corroborates same tier (all 3
  legs CONFIRM, consts 74/72/64/73 INCL).
  No DISSENT on P271. Agrees with cport commit msg
  (py/C 15930, PYID 7965).
- Quiz: no conflicting CLAIM/GATE/FLAG on b379/
  b9db70db. b378 EVEN = sweep2 turf (all evens are),
  used b378 tip as diff-base only, NOT gated. Newest
  PARENT-* is QNUM-16 (w2d Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r56/ (build379.log,
  pyid379.log, rgram379py/c.log, pass379py/c.txt,
  for378-old.nums/for379-new.nums,
  smoke379.log, tables379.log, tabaudit379.py,
  edges379.log, edges379.py, cdiff379.txt,
  pydiff379.txt, banddiff379.txt, added379.txt,
  build379/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
