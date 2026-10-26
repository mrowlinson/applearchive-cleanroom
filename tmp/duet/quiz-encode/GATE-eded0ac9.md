# GATE eded0ac9 b367 T10P259 pins 106869..107216 (348 pins) PASS-functional

Seat sweep-r53, first-hand, WT tmp/wt-encode-sweep @eded0ac9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r53.
Band = 01e51667 (py merge w2b@cf984c9f partial, +6 tiers
+62 pins) + eded0ac9 (C port). Base a961bc67 (b366 tip,
1536 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build367/{aae,rgramc}, rc=0,
  0 warnings. aae sha1 7d8dd3a2 / sha256 d6e27c97
  (pinned stable continues: sha1 r39-r53, sha256 matches
  b354-b363 pinned value; band touches no aae sources),
  rgramc sha1 c828c131 / sha256 e2a5d825.
- RGRAMC-PYID 7587/7587 covered=7587/7587 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 15174/15174 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 15174/15174 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (15174/15174, sorted).
- PINS-RGRAM cells set-eq 7587/7587 (xor 0 all 3 ways:
  for^pass for^pins pass^pins; py^C 0).
  PINS 15176 rows (2 hdr + 15174, +62 vs base 15114).
  For-list union 7556->7587 +31/-0 (python sets, never
  comm).
  31 = 2 sing (106869 106870) +
  A 6 (head 106871 + 106872 + 106877 + carry pair
  106879/106880 + tail 106886) +
  B 6 (head 106887 + 106888 + 106891 + 106893 + 106895 +
  tail 106896; offs 2,3,5,7 unsampled: 106889, 106890,
  106892, 106894) +
  Q 10 (head 106897 + 106905 + row-edge pair
  106912/106913 + row-edge pair 106928/106929 + 106937 +
  row-edge pair 106944/106945 + tail 106960) +
  R 7 (head 106961 + edge pair 107007/107008 + mid
  107089 + edge pair 107135/107136 + tail 107216).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 31x2 = 62 = 15174-15112.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var).
- Tables audit P259 C-vs-py, 15-table A-PBA/B10/
  QUAD-b42+T88 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 20370300 ==P258PB0 REPEAT / 05016206 NEW, both
  NEW strings);
  AM 16/16 (8B), BM 10/10 (11B), M 16/16 (7B),
  M42 16/16 (1B), X42 4/4 (1B), QR 4/4 (6B),
  QT 4/4 (4B), RM 16/16 (8B), RQ 16/16 (8B) EXACT;
  AC 74/74, BC 71/71, QC 64/64, RC 70/70 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 74/71/64/70 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit367.py 52 PASS 0 FAIL).
  No CM/CC (B10, not C10), no QB (not pair-led), no
  PT/FM; table inventory exactly the 15.
  Missing-sets first-hand EXACT: AC-10 [4,5,36,37,38,
  39,76,77,78,79] = b4,b5+M8 (b36-39,76-79);
  BC-13 [4,5,36,37,38,39,40,41,42,80,81,82,83]
  = b4,b5+M11 (b36-42,80-83; b42 IN M-range);
  QC-20 [4,5,34,35,36,37,38,39,40,41,42,43,76,
  77,78,79,80,81,82,83] = b4,b5+QM7 (b34,35,43,
  76-79)+b42+R6 (b36-41)+T4 (b80-83);
  RC-18 [4,5,38,39,46,47,52,53,54,55,76,77,78,
  79,80,81,82,83] = VPOS 18 over 0..87 (b4,b5+TM8
  b52-55,80-83 + TR8 b38,39,46,47,76-79).
  b0-3 first-hand: AC b0-3 e0921f7a (NEW);
  BC b0-3 05016206 (==PB1 sig, single-sig: b0-3
  const over all 10 rows);
  QC b0-3 e0921f7a (==PBA sig, single-sig quad);
  RC 06000000 (==P252/253/256T sig, P253+P256
  re-read first-hand).
  Code AC74/BC71/QC64/RC70; incl = +0/+1/+1/+0
  (A b5-carry, B/Q b5 const 43, T counter) =
  74/72/65/70; lane consts = A-619/A-323 INCL
  EXACT (writer PBA/T88 identical; B10/quad =
  memo-1).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/B/Q/R): P2590 n==106869 / P2591
  n==106870 singleton-const (offs 0/1);
  P259A 106871..106886 off=n-106871 PBA16
  (m-tab 8B b36-39,76-79, sig e0921f7a NEW,
  b5-carry 42->43 @106879->106880);
  P259B 106887..106896 off=n-106887 B10 single-sig
  (m-tab 11B b36-42,80-83, b42 in M-range, b5
  const 43);
  P259Q 106897..106960 off=n-106897 m=off&15
  q=off>>4 single-sig quad (M 7B b34,35,43,76-79
  + b42 row-XOR X=[00,3e,05,09] staged, ADD tie
  documented + R6 6B b36-41 + QT b80-83, b5
  const 43);
  P259R(T88-ring) 106961..107216 off=n-106961
  c=off&15 r=off>>4 STANDARD sig 06000000 (TM 8B
  b52-55,80-83 by COL + TR 8B b38,39,46,47,76-79
  by ROW SPLIT tails, b84-87 const 37/63/4b/e0);
  A/B/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8; R paylen 88
  + counter b4=(0xa3+2off)&FF b5=0x43+(off>=47)+
  (off>=175).
  C blocks carry T71089/71094/71099/71114/71130/
  71155 py-line mirrors (exact); guards
  `if ((n) == (106869))` / `if ((n) == (106870))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; b42xor via snprintf %02lx of pay[42]^
  hexval(X42[q]) vs M42[m] (matches py); counter
  163/67 + (off>=47)+(off>=175);
  temps _t5482.._t5501 appended (base max _t5481,
  no reuse); _i max 3334->3345, _b max 3333->
  3344, no reuse; C byte-index lists match py per
  block (A 8B, B 11B, Q 7/1/6/4B, R 8/8B); insert
  position exact (dispatch tail, N out-of-scope
  follows).
  Value checks first-hand: AM 16/16 distinct;
  BM 10/10 diverge (single-sig rows, all distinct);
  M 16/16 distinct;
  M42 4-valued {5f,df,9f,1f} low-nibble const f;
  X42 [00,3e,05,09] EXACT;
  XOR-grid (M42[m]^X42[q]) 16 distinct = 4x4
  (16/1a/1f/21/56/5a/5f/61/96/9a/9f/a1/d6/da/
  df/e1);
  QR 4/4 UNPAIRED distinct exact (d7df932a3163/
  bc5c041831f7/8d5e1c80319e/605e2317914d);
  QT 4/4 distinct exact (5288342d/5ed4036f/
  fca81ac3/fa92adc7); no shared suffix (last2B
  2d/6f/c3/c7 all differ);
  M/RQ heads 16/16 + tails(b76-79) 16/16
  same-index (shared-slice prefix+suffix; middle
  M-b43 vs RQ-b46,47 differs; full-string
  impossible: RQ 8B vs M 7B);
  tails SPLIT (RM b80-83 by COL c=off&15, RQ
  b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P258T
  (P258RQ 6B tails, row-led via TR6);
  QT 4/4 NEW vs P258QT
  (f2bc5daa/49f3db15/dab7ba8e/1469107b).
  S0 NEW string (sig 20370300 ==P258PB0 REPEAT);
  S1 NEW (sig 05016206 NEW; P258S1 sig f8416e06).
  b42 tie first-hand: code stages XOR (formula +
  X values match memo X=[00,3e,05,09]); ADD tie
  A=[0,02,fb,f7] documented in Q-block comment
  both sides; memo A-619 + viewer A-323 both
  first-hand confirm XOR/ADD 64/64 TIE; staging
  follows b42-family precedent (P251 same XOR
  formula shape, rgram.py:70438).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head ef/42 (106871)
  tail 0d/43 (106886), b5set {42,43}, carry
  ff/42->01/43 @106879->106880 (single flip,
  off8->9, 9+7 split per memo correction); B head
  0f/43 (106887) tail 21/43 (106896), b5set {43};
  Q head 23/43 (106897) tail a1/43 (106960),
  b5set {43} NO carry.
  T head a3/43 (106961) + off46/47 (107007->
  107008) ff/43->01/44 + off174/175 (107135->
  107136) ff/44->01/45 + mid off128 a3/44
  (107089) + tail off255 a1/45 (107216). All
  edge pins in for-list + PASS (batteries GREEN);
  107216 tail pinned + in for-list + PASS.
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (eb/42, ed/42) match raw
  lencode.
  Matches A-619/A-323 geometry (mixed-size 92x84B+
  256x88B, PB0 20370300 ==P258PB0 + PB1 05016206
  NEW, PBA16 VPOS 10 b5-carry 16/16 distinct NO
  pair, B10 single-sig VPOS 12 b5 const 43 10/10
  diverge, QUAD single-sig VPOS 19 QM7 shared +
  b42 XOR-tie staged + R6 UNPAIRED + tails 4/4
  no-suffix + M-tails ALL NEW 16/16, T88-ring
  STANDARD sig 06000000 TM8 by COL + TR8 by ROW
  UNPAIRED 16/16 + SPLIT tails + b84-87 const
  37634be0, ring edges + thresholds 47/175, NO D
  dips).
- C diff pure-add: numstat 640/0 rgramc.c + 260/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 635
  content + 5 blank-only `+` lines / 0 del; raw py
  260 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 182, py del-uniq
  0 add-uniq 199). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope a961bc67..
  eded0ac9, 963 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 640/0, rgram.py 260/0,
  test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1442->1448 +6, singletons
  `if n == ` 550->552 +2, range-guards `<= n <=`
  488->492 +4, CLOSED T10P prints 1442->1448 +6,
  seal 1536->1542
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 545->547 +2,
  range 488->492 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357/b359/b361/b363/b365), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-619-q771
  T10P259 memo CONFIRM 37/37 verdict (section heads
  shape 12/12 + quad+Tring 12/12 + counters 12/12
  quoted verbatim; b42 XOR/ADD 64/64 tie staged XOR
  per b42-family precedent, PBA carry 9+7
  re-verified, tier cut SAFE)
  + A-323-q323 viewer corroborates same tier (3/3
  legs CONFIRM, consts 74/72/65/70 INCL).
  No DISSENT on P259. Agrees with cport commit msg
  (py/C 15174, PYID 7587).
- Quiz: no conflicting CLAIM/GATE/FLAG on b367/
  eded0ac9. b366/b368 EVEN = sweep2 turf, used b366
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-12 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r53/ (build367.log,
  pyid367.log, rgram367py/c-full.log, pass367py/c.
  txt, pins366base.csv, for367-old/-new.nums,
  sh366/367.sh, smoke367.log, tables367.log,
  tabaudit367.py, edges367.log, numstat367.txt,
  cdiff367.txt, pydiff367.txt, banddiff367.txt,
  build367/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
