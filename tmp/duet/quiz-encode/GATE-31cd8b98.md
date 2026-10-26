# GATE 31cd8b98 b407 T10P299 pins 120789..121136 (348 pins) PASS-functional

Seat sweep-r63, first-hand, WT tmp/wt-encode-sweep @31cd8b98,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r63.
Band = e538588a (py merge w2b@f0d2976a partial, +6 tiers
+62 pins) + 31cd8b98 (C port). Base 596f0e16 (b406 tip,
1776 tiers sealed).

- Build: make -C src/c BUILDDIR=r63/build407 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build407/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r63, sha256 matches b354-b407
  pinned value; band touches no aae sources), rgramc
  sha1 9d7b1b0b / sha256 8d381fa5.
- RGRAMC-PYID 8842/8842 covered=8842/8842 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 17684/17684 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 17684/17684 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (17684/17684, sorted).
- PINS-RGRAM cells set-eq 8842/8842 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 17686 rows (2 hdr + 17684, +62 vs base 17624).
  For-list union 8811->8842 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (120789 120790) +
  A 6 (head 120791 + 120792 + 120798 + 120799 +
  120805 + tail 120806; offs 0,1,7,8,14,15) +
  C 6 (head 120807 + 120808 + 120811 + 120812 +
  120815 + tail 120816; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 120809, 120810, 120813,
  120814) +
  Q 10 (head 120817 + off8 120825 + edge pair
  120831/120832 + off16 120833 + off24 120841 +
  off32 120849 + off40 120857 + off48 120865 +
  tail 120880; offs 0,8,14/15,16,24,32,40,48,63;
  b5 step o14->15, edge pair in for-list) +
  R 7 (head 120881 + edge pair 120959/120960 + mid
  121009 + edge pair 121087/121088 + tail 121136;
  offs 0,78/79,128,206/207,255).
  PINS adds = same 31 tier pins (2 rows each; base
  all 2x). Each for-N yields 2 PASS lines; 31x2 = 62
  = 17684-17622.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P299 C-vs-py, 13-table A-PBA88-PLAIN/
  C10-1SIG/QUAD88-4R-FRAG+T88-RING layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 36721e00 (sig-eq P298PB0) / 5b49f53c NEW;
  S0 diff vs P298S0 31/84 @ b4-10,13-18,20-25,64-75
  NOT byte-equal + S1 diff vs P298S1 48/84 @ b0-2,
  4,5,13-39,52-55,68-75,80-83 + S1 diff vs own
  C10 cells 25/84 UNIFORM all 10 ([0] @ b4,22,23,
  30-43,76-83), NOT byte-equal);
  AM 16/16 (7B), CM 10/10 (11B), M 16/16 (7B),
  QR 4/4 (10B), F 16/16 rows (1B, uniq 2: 86 x7 /
  06 x9), RM 16/16 (8B), RQ 16/16 (8B)
  EXACT;
  AC 79/79, CC 71/71, QC 68/68, RC 70/70 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 79/71/68/70 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit407.py 90 PASS 0 FAIL).
  No F0/F1 (single-F coltab, not rowpair-tabs), no
  BM/BC (C10, not B10), no M19/X19 (FRAG is
  single-F coltab+ADD4, not M19), no M42/X42/H42/
  L42 (no b42), no QB/PT/FM, no RT/TT (ring, not
  ROWTAIL), no QT (R10 carries b84-87 inside QR);
  table inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-9 [4,5,40,41,
  42,80,81,82,83] = b4,b5+M7 (b40-42,80-83);
  CC-13 [4,5,36,37,38,39,40,41,42,80,81,82,
  83] = b4,b5+M11 (b36-42,80-83);
  QC-20 [4,5,38,39,40,41,42,43,44,45,46,47,80,
  81,82,83,84,85,86,87] = b4,b5+QM7
  (b38,39,47,80-83)+R10 (b40-45,84-87)+F1
  (b46);
  RC-18 [4,5,38,39,46,47,52,53,54,55,76,77,78,
  79,80,81,82,83] = b4,b5+TR8 (b38,39,46,47,
  76-79)+TM8 (b52-55,80-83).
  PLAIN first-hand: AC b0..b3 = 03,00,00,00 ->
  sig 03000000 x16, b0 const 03; AM 16/16
  distinct.
  1SIG first-hand: CC b0..b3 = 5b,49,f5,3c ->
  5b49f53c x10 SAME-as-PB1-sig; CM 10/10 diverge;
  b5 const af, NO step.
  Code AC79/CC71/QC68/RC70; incl = +1/+1/+0/+0
  (A b5 const af, C b5 const af, Q b5-step, T
  counter) = 80/72/68/70; lane consts =
  A-759 INCL EXACT (deduct-b5-only-when-b5vary
  rule holds: Q-step +0 like C-STEP P295).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2990 n==120789 / P2991
  n==120790 singleton-const (offs 0/1);
  P299A 120791..120806 off=n-120791 PBA88-PLAIN
  (m-tab 7B b40-42,80-83, sig 03000000, b0
  const 03, b5 const af);
  P299C 120807..120816 off=n-120807 C10-1SIG
  (m-tab 11B b36-42,80-83 M11, full sig b0-3 in
  CC, b5 const af, NO step);
  P299Q 120817..120880 off=n-120817 m=off&15
  q=off>>4 QUAD88-4R-FRAG 1-sig 02000000 x64
  (M 7B b38,39,47,80-83 NO frags + R10
  b40-45,84-87 r0 6b5ba2e6 distinct + r123
  share 6B d6da1e17928d, tails b84-87 4
  distinct c76cd27c/78bcf792/9dbcf792/c2bcf792,
  r123 TRUE 3B bcf792, r0 lcsuf 0 vs rest, r123
  lcpre 6B d6da1e17928d + FRAG b46 coltab F +
  ADD4 r123==r0+4 mod256, b5 0xaf+(o>=15) step
  o14->15);
  P299R(T88-ring) 120881..121136 off=n-120881
  c=off&15 r=off>>4 STANDARD sig 2a000000 (TM 8B
  b52-55,80-83 by COL + TR 8B b38,39,46,47,
  76-79 by ROW SPLIT tails UNPAIRED 16/16,
  b84-87 const 5e/a8/1c/06);
  A paylen 88 / C paylen 84 / Q paylen 88 + raw
  lencode l16=((n<<1)|1) &0xFFFF pay4=l16&0xFF
  pay5=l16>>8 (b5-consts/step emerge from raw
  lencode);
  R paylen 88 +
  counter b4=(0x63+2off)&FF b5=0xb0+(off>=79)+
  (off>=207).
  C blocks carry T80898/80903/80908/80923/80939/
  80965 py-line mirrors (exact); guards
  `if ((n) == (120789))` / `if ((n) == (120790))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 99+2*off + 176+(off>=79)+
  (off>=207); ftab if (q)==(0) F else fadd4
  (hexval+4)&255; temps _t6209.._t6226 appended
  (base max _t6208, no reuse); _i band 3765,
  3767,3770,3773 (base max _i3763), _b band
  3764,3766,3768,3769,3771,3772 (base max
  _b3762), no reuse; C byte-index lists match py
  per block (A 7B, C 11B, Q 7B/10B/1B, R 8B/8B);
  insert position exact (P298R block precedes, N
  out-of-scope follows; C has 2 scope hits; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0
  6b5ba2e6...c76cd27c; r1
  d6da1e17928d...78bcf792; r2
  d6da1e17928d...9dbcf792; r3
  d6da1e17928d...c2bcf792);
  QR full-row lcsuf: r123 pairs 3, r0-vs-rest 0;
  r123 lcpre 6B d6da1e17928d;
  RQ==M EMBED7 (RQ[i] = M[i][:2] + X[i] +
  M[i][2:] all 16 rows: heads b38,39 same-pos +
  b47 same-pos value + tails cross-position
  b76-79 vs b80-83 value-equal; X = b46 insert,
  uniq 8e x7 / 0e x9) -- EMBED7 degree NEW (tab-
  subsequence equality);
  21st odd-band RQ==M instance;
  OBSERVED (not a gate criterion, flagged for
  memo): X[i]==F[i]+8 mod 256 all 16 same
  indices (86<->8e rows 0,1,2,3,5,6,9; 06<->0e
  rows 4,7,8,10-15) across row/col axes --
  positional coincidence unless memo rules
  otherwise;
  tails STANDARD-SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P298T RM col-led tails
  (overlap 0); RM-tails (b80-83) ALL NEW vs P298T
  RM tails (overlap 0); RQ-tails (b76-79) ALL NEW
  vs P298T RQ tails (overlap 0); cross overlaps 0;
  F coltab 16 rows uniq 2 (86 x7, 06 x9);
  ftab/fadd4 both sides (q==0 F[m] else F[m]+4
  mod 256);
  S0 sig-eq string (31/84 differ @ b4-10,13-18,
  20-25,64-75) + S1 NEW string (48/84 differ vs
  P298S1 @ b0-2,4,5,13-39,52-55,68-75,80-83;
  25/84 UNIFORM vs own C10 all 10, [0] @ b4,22,
  23,30-43,76-83);
  P299 actuals (S0 36721e00/S1 5b49f53c/PBA88
  03000000/C10-1SIG x10 + PB1-vs-C10 25/84) ==
  A-753 predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head af/af (120791)
  tail cd/af (120806), b5set {af}; C head cf/af
  (120807) tail e1/af (120816), b5set {af};
  Q head e3/af (120817) edge o14->15 (120831->
  120832) ff/af->01/b0 tail 61/b0 (120880);
  quad b4=(0xe3+2off) 64/64;
  T head 63/b0 (120881) + off78/79 (120959->
  120960) ff/b0->01/b1 + mid off128 63/b1
  (121009) + off206/207 (121087->121088)
  ff/b1->01/b2 + tail off255 61/b2 (121136).
  All edge pins in for-list + PASS (batteries
  GREEN); 121136 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  ea22ab1f0c254880... matches PINS rawlen 104,
  py+C CLOSED T10P299R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (ab/af, ad/af) match raw
  lencode.
  Matches A-759 geometry (12x84B+336x88B,
  PB0 36721e00 sig-eq P298PB0 + PB1 5b49f53c NEW
  sig-eq own-C10, PBA88-PLAIN VPOS 8 b5 const af
  NO pair, C10-1SIG VPOS 12 b5 const af 10/10
  diverge, QUAD88-4R-FRAG VPOS 20 QM7+R10+F1 +
  R10 4/4 UNPAIRED + tails b84-87 4 distinct
  r123-TRUE-3B + FRAG coltab+ADD4 + M-tails ALL
  NEW 16/16, T88-RING STANDARD sig 2a000000 TM8
  by COL + TR8 by ROW UNPAIRED 16/16 + SPLIT
  tails + b84-87 const 5ea81c06, ring edges +
  thresholds 79/207, NO D dips).
- C diff pure-add: numstat 634/0 rgramc.c + 254/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 629
  content + 5 blank-only `+` lines / 0 del; raw py
  254 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 173, py del-uniq
  0 add-uniq 199). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 596f0e16..
  31cd8b98, 951 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 634/0, rgram.py 254/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1682->1688 +6, singletons
  `if n == ` 630->632 +2, range-guards `<= n <=`
  648->652 +4, CLOSED T10P prints
  1682->1688 +6, seal 1776->1782
  +6 (cport msgs; offset +94 vs CLOSED-T10P stable
  b401-b407): all agree (stated literal methods,
  first-hand).
  C guards: singleton `if ((n) == (` 625->627 +2,
  range 648->652 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b405 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-759-q891
  memo CONFIRM 51/53 + section-F (section heads
  shape 25/25 + quad+T-ring 14/14 + counters 12/14
  quoted verbatim; the 2 non-confirm = const-count
  writer arithmetic, geometry exact; tier cut SAFE;
  w2b-r24 8/8 CAP; Port verdict).
  Viewer: NO P299 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P299. Agrees with cport commit msg
  (py/C 17684, PYID 8842).
- Quiz: no conflicting CLAIM/GATE/FLAG on b407/
  31cd8b98. b406/b408 EVEN = sweep2 turf, used b406
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-21 (w2b Q-block refill only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r63/ (build407.log,
  pyid407.log, rgram407py/c.log, pass407py/c.txt,
  seteq407.py/log, smoke407.log, tables407.log,
  tabaudit407.py, edges407.py, edges407.log,
  cdiff407.txt, pydiff407.txt, banddiff407.txt,
  added407.txt, numstat407.txt, diffwall407.py/log,
  build407/ binaries,
  tail-121136.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
