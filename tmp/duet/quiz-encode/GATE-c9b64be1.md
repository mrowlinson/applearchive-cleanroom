# GATE c9b64be1 b415 T10P307 pins 123573..123920 (348 pins) PASS-functional

Seat sweep-r65, first-hand, WT tmp/wt-encode-sweep @c9b64be1,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r65.
Band = a694751f (py merge w2b@dae68b44 partial, +6 tiers
+62 pins) + c9b64be1 (C port). Base 0dd1dddf (b414 tip,
1824 tiers sealed).

- Build: make -C src/c BUILDDIR=r65/build415 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build415/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r65, sha256 matches b354-b415
  pinned value; band touches no aae sources), rgramc
  sha1 8f4c2da1 / sha256 0abce382.
- RGRAMC-PYID 9091/9091 covered=9091/9091 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18182/18182 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18182/18182 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (18182/18182, sorted).
- PINS-RGRAM cells set-eq 9091/9091 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 18184 rows (2 hdr + 18182, +62 vs base 18122).
  For-list union 9060->9091 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (123573 123574) +
  A 6 (head 123575 + 123576 + 123582 + 123583 +
  123589 + tail 123590; offs 0,1,7,8,14,15) +
  C 6 (head 123591 + 123592 + 123595 + 123596 +
  123599 + tail 123600; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 123593, 123594, 123597,
  123598) +
  Q 10 (head 123601 + off8 123609 + off16 123617 +
  off24 123625 + off32 123633 + off40 123641 +
  edge pair 123647/123648 + off48 123649 + tail
  123664; offs 0,8,16,24,32,40,46/47,48,63;
  b5 step o46->47, edge pair + off48 in for-list) +
  R 7 (head 123665 + edge pair 123775/123776 +
  mid 123793 + edge pair 123903/123904 + tail
  123920; offs 0,110/111,128,238/239,255).
  PINS adds = same 31 tier pins (2 rows each).
  Each for-N yields 2 PASS lines; 31x2 = 62
  = 18182-18120.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P307 C-vs-py, 13-table A-PBA88-PLAIN/
  C10-1SIG/QUAD88-4R-FRAG+T88-RING-STANDARD layout,
  all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs ab687400 NEW / 803b4f44 NEW NOT-PB1-sig
  (own C10 803b4f84);
  S0 diff vs P306S0 30/84 @ b0-2,4-10,13-19,24,
  64-75 NOT byte-equal + S1 diff vs P306S1 49/84
  @ b1-5,12-39,52-55,68-75,80-83 NOT byte-equal +
  S1 diff vs own C10 cells 27/84 TRUE UNIFORM all
  10 (cell0 @ b3,4,14,15,22,23,30,32-43,76-83),
  NOT byte-equal);
  AM 16/16 (8B), CM 10/10 (11B), M 16/16 (6B),
  QR 4/4 (10B), F 16/16 (1B), RM 16/16 (10B),
  RQ 16/16 (7B) EXACT;
  AC 78/78, CC 71/71, QC 69/69, RC 69/69 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 78/71/69/69 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit415.py 90 PASS 0 FAIL).
  No F0/F1 (single-F ADD, not rowpair), no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/L42,
  no QB/PT/FM, no RT/TT (ring, not ROWTAIL), no QT
  (R10 carries b84-87 inside QR); table inventory
  exactly the 13.
  Missing-sets first-hand EXACT: AC-10 [4,5,40,41,
  42,43,80,81,82,83] = b4,b5+M8 (b40-43,
  80-83);
  CC-13 [4,5,36,37,38,39,40,41,42,80,81,82,83] =
  b4,b5+M11 (b36-42,80-83, full sig b0-3 in
  CC = 80,3b,4f,84 -> 803b4f84 x10);
  QC-19 [4,5,38,40,41,42,43,44,45,46,47,80,81,
  82,83,84,85,86,87] = b4,b5+QM6
  (b38,47,80-83)+R10 (b40-45,84-87)+F1 (b46);
  RC-19 [4,5,38,46,47,50,51,52,53,54,55,76,77,
  78,79,80,81,82,83] = b4,b5+TR7
  (b38,46,47,76-79)+TM10 (b50-55,80-83).
  PLAIN first-hand: AC b0..b3 = 05,00,00,00 ->
  sig 05000000 x16, b0 const 05; AM 16/16
  distinct; b5 const c5, NO step.
  1SIG first-hand: CC b0-3 full sig 803b4f84 x10
  NOT-PB1-sig (S1 803b4f44 differs); CM 10/10
  diverge; b5 const c5, NO step; 10/10 diverge.
  FRAG first-hand: F 16 entries 2 distinct
  {10,90}, sequence 90 10 90 10 90 90 10 90 90
  10 90 90 10 10 90 10 EXACT == memo; dispatch
  q==0 ftab (pay[46] hex == F[m]) else fadd3
  (pay[46] == (F[m]+3)&FF) BOTH sides (py + C
  hexval+3); ADD constant 3 derived from dispatch
  first-hand (FIRST ADD3; 4th FRAG shape: single-F
  +ADD3, prior were rowpair F0/F1 vs single-F
  +ADD1 vs single-F +ADD4).
  Code AC78/CC71/QC69/RC69; incl = +1/+1/+0/+0
  (A b5 const c5, C b5 const c5, Q b5-step, T
  counter) = 79/72/69/69; lane consts =
  A-787 INCL EXACT (deduct-b5-only-when-b5vary
  rule holds; Q-step +0 like Q-step P303).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3070 n==123573 / P3071
  n==123574 singleton-const (offs 0/1);
  P307A 123575..123590 off=n-123575 PBA88-PLAIN
  (m-tab 8B b40-43,80-83, sig 05000000, b0
  const 05, b5 const c5);
  P307C 123591..123600 off=n-123591 C10-1SIG
  (m-tab 11B b36-42,80-83 M11, full sig b0-3
  in CC = 803b4f84, b5 const c5, NO step);
  P307Q 123601..123664 off=n-123601 m=off&15
  q=off>>4 QUAD88-4R-FRAG 1-sig 09000000 x64
  (M 6B b38,47,80-83 QM6 NO frags + R10
  b40-45,84-87 r0 5c5c471c distinct +
  r123 share 6B 42dc42e872fd, tails b84-87 4
  distinct 4c3c8f8d/63696b0a/88696b0a/ad696b0a,
  r123 ALL TRUE 3B 696b0a, r0 lcs 0 vs all,
  r123 lcpre 6, full-row lcsuf r123 pairs 3,
  b5 0xc5+(o>=47) step o46->47, b4 base 0xa3
  step2);
  P307R(T88-ring) 123665..123920 off=n-123665
  c=off&15 r=off>>4 STANDARD sig 93000000 (TM
  10B b50-55,80-83 by COL + TR 7B b38,46,47,
  76-79 by ROW SPLIT tails UNPAIRED 16/16,
  b84-87 const 1f/f2/0e/c5);
  A paylen 88 / C paylen 84 / Q paylen 88 + raw
  lencode l16=((n<<1)|1) &0xFFFF pay4=l16&0xFF
  pay5=l16>>8 (b5-const/step emerges from raw
  lencode);
  R paylen 88 +
  counter b4=(0x23+2off)&FF b5=0xc6+(off>=111)+
  (off>=239).
  C blocks carry T82787/82792/82797/82812/82828/
  82854 py-line mirrors (exact); guards
  `if ((n) == (123573))` / `if ((n) == (123574))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 35+2*off + 198+(off>=111)+
  (off>=239); temps _t6341.._t6358 appended
  (base max _t6340, no reuse); _i band 3845,
  3847,3850,3853 (base max _i3843), _b band
  3844,3846,3848,3849,3851,3852 (base max
  _b3842), no reuse; C byte-index lists match py
  per block (A 8B, C 11B, Q 6B/10B, R 10B/7B);
  insert position exact (P306R block precedes, N
  out-of-scope follows; C has 2 scope hits; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0
  5c5c471c...4c3c8f8d; r1
  42dc42e8...63696b0a; r2
  42dc42e8...88696b0a; r3
  42dc42e8...ad696b0a);
  QR full-row lcsuf: r123 pairs 3, r0-vs-rest 0;
  r123 lcpre 6B 42dc42e872fd;
  RQ==M SHIFT (M 6B vs RQ 7B: agree (0,0),
  (1,2),(2,3),(3,4),(4,5),(5,6) 16/16 each,
  RQ[1] isolated maxagree 0/16 2-distinct
  18/98, RQ[0] maxagree 16 distinct 2 (78/f8),
  RQ[2] maxagree 16 distinct 13, zero
  off-pattern incidentals) -- SHIFT degree (RQ
  carries extra b46 byte at idx1; M[1:6]==
  RQ[2:7]; NEW variant, joins neither prior
  group);
  25th odd-band RQ==M instance;
  tails STANDARD-SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P306T RM col-led tails
  (overlap 0); RM-tails (b80-83) ALL NEW vs P306T
  RM col-led tails (overlap 0); RQ-tails (b76-79)
  ALL NEW vs P306T RQ row-led tails (overlap 0);
  cross overlaps 0 (P306T widths RM 9B/RQ 8B
  first-hand);
  S0 NEW string (30/84 differ vs P306S0 @ b0-2,4-10,
  13-19,24,64-75) + S1 NEW string (49/84 differ
  vs P306S1 @ b1-5,12-39,52-55,68-75,80-83;
  27/84 TRUE UNIFORM vs own C10 all 10, cell0 @
  b3,4,14,15,22,23,30,32-43,76-83; third
  TRUE-uniform case after P299 25/84 + P303
  58/84);
  P307 actuals (S0 ab687400/S1 803b4f44/PBA88
  05000000/C10-1SIG 803b4f84 x10 NOT-PB1-sig)
  == A-782 predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 6f/c5 (123575)
  tail 8d/c5 (123590), b5set {c5}; C head 8f/c5
  (123591) tail a1/c5 (123600), b5set {c5};
  Q head a3/c5 (123601) edge o46->47 (123647->
  123648) ff/c5->01/c6 tail 21/c6 (123664);
  quad b4=(0xa3+2off) 64/64;
  T head 23/c6 (123665) + off110/111 (123775->
  123776) ff/c6->01/c7 + mid off128 23/c7
  (123793) + off238/239 (123903->123904)
  ff/c7->01/c8 + tail off255 21/c8 (123920).
  All edge pins in for-list + PASS (batteries
  GREEN); 123920 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  d48ee749c97cc315... matches PINS rawlen 104,
  py+C CLOSED T10P307R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand (346 + S0/S1
  embedded b4/b5 6b/c5 + 6d/c5).
  Matches A-787 geometry (12x84B+336x88B framing
  PINS-confirmed 100x16+104x46, PB0 ab687400 NEW
  + PB1 803b4f44 NEW diff-own-C10, PBA88-PLAIN
  VPOS 9 b5 const c5 NO pair, C10-1SIG VPOS 12
  b5 const c5 10/10 diverge, QUAD88-4R-FRAG
  VPOS 19 QM6+R10+F1 + R10 4/4 UNPAIRED +
  tails b84-87 4 distinct r123-TRUE-3B + F-seq
  exact + M-tails ALL NEW 16/16, T88-RING
  STANDARD sig 93000000 TM10 by COL + TR7 by ROW
  UNPAIRED 16/16 + SPLIT tails + b84-87 const
  1ff20ec5, ring edges + thresholds 111/239,
  NO D dips).
- C diff pure-add: numstat 634/0 rgramc.c + 254/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 634
  content + 5 blank-only `+` lines / 0 del; raw py
  254 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 151, py del-uniq
  0 add-uniq 176). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 0dd1dddf..
  c9b64be1, 951 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 634/0, rgram.py 254/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1730->1736 +6, singletons
  `if n == ` 646->648 +2, range-guards `<= n <=`
  680->684 +4, CLOSED T10P prints
  1730->1736 +6, seal 1824->1830
  +6 (cport msgs; offset +94 vs CLOSED-T10P stable
  b401-b415): all agree (stated literal methods,
  first-hand).
  C guards: singleton `if ((n) == (` 641->643 +2,
  range 680->684 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b413 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-787-q899
  memo CONFIRM 58/58 CLEAN (section heads shape
  27/27 + quad+T-ring 17/17 + counters 14/14
  quoted verbatim; ZERO section-F; tier cut SAFE;
  w2b-r25 [8/8 CAP]; Port verdict: 4th straight
  fully clean w2b sheet).
  Viewer: NO P307 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P307. Agrees with cport commit msg
  (py/C 18182, PYID 9091).
- Quiz: no conflicting CLAIM/GATE/FLAG on b415/
  c9b64be1. b414/b416 EVEN = sweep2 turf, used b414
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-22 (w2e Q-block refill only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r65/ (build415.log,
  b415-pyid.log, b415-py/c.log, pass415py/c.txt,
  seteq415.py/log, b415-smoke.log, tables415.log,
  tabaudit415.py, edges415.py, edges415.log,
  cdiff415.txt, pydiff415.txt, banddiff415.txt,
  added415.txt, numstat415.txt, diffwall415.py/log,
  build415/ binaries,
  tail-123920.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
