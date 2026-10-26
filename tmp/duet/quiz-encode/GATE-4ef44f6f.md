# GATE 4ef44f6f b389 T10P281 pins 114525..114872 (348 pins) PASS-functional

Seat sweep-r59, first-hand, WT tmp/wt-encode-sweep @4ef44f6f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r59.
Band = 97be8410 (py merge w2b@396f58dc partial, +6 tiers
+64 pins) + 4ef44f6f (C port). Base 55198ed2 (b388 tip,
1668 tiers sealed).

- Build: make -C src/c BUILDDIR=r59/build389 aae rgramc
  (flags -O2 -Wall -Wextra -std=c11 per Makefile), rc=0,
  0 warnings (log = make/cc command echoes only),
  build389/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r59,
  sha256 matches b354-b389 pinned value; band touches no
  aae sources), rgramc sha1 14fe509b / sha256 6b0f4be9.
- RGRAMC-PYID 8279/8279 covered=8279/8279 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 16558/16558 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 16558/16558 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (16558/16558, sorted).
- PINS-RGRAM cells set-eq 8279/8279 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 16560 rows (2 hdr + 16558, +64 vs base 16496).
  For-list union 8247->8279 +32/-0 (python sets,
  trailing-';' stripped, never comm).
  32 = 2 sing (114525 114526) +
  A 6 (head 114527 + 114528 + 114532 + 114537 +
  114541 + tail 114542; offs 0,1,5,10,14,15) +
  C 7 (head 114543 + 114544 + 114548 + 114549 +
  114550 + 114551 + tail 114552; offs 0,1,5,6,7,8,9;
  offs 2,3,4 unsampled: 114545, 114546, 114547) +
  Q 10 (head 114553 + mid-row0 edge pair
  114559/114560 + edge pair 114568/114569 + mid pair
  114584/114585 + mid pair 114600/114601 + tail
  114616; offs 0,6/7,15/16,31/32,47/48,63; b5 step
  off>=7 MID-ROW0) +
  R 7 (head 114617 + edge pair 114687/114688 + mid
  114752 + edge pair 114815/114816 + tail 114872;
  offs 0,70/71,135,198/199,255).
  PINS adds = same 32 tier pins. Each for-N yields 2 PASS
  lines; 32x2 = 64 = 16558-16494.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P281 C-vs-py, 13-table A-PBA-PLAIN/
  C10-4SIG/QUAD2s+T88-STANDARD layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 5eae0700 / 2557520f NEW, both NEW strings;
  diff vs P280S0/S1 33/84 @ b0,4,5,11,18-24,26-29,
  32-37,52-55,72-79 + 47/84 @ b4,5,22-40,42-55,
  72-83);
  AM 16/16 (6B), CM 10/10 (12B), M 16/16 (8B),
  QR 4/4 (7B), QT 4/4 (4B), RM 16/16 (8B),
  RQ 16/16 (8B)
  EXACT;
  AC 76/76, CC 70/70, QC 63/63, RC 70/70 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/70/63/70 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit389.py 100 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42 (no b42 staging), no QB/PT/FM, no
  RT/TT (STANDARD ring, not ROWTAIL); table
  inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-8 [4,5,48,49,
  76,77,78,79] = b4,b5+M6 (b48,49,76-79);
  CC-14 [2,3,4,5,46,47,48,49,50,51,80,81,82,
  83] = b4,b5+M12 (b2,3,46-51,80-83);
  QC-21 [3,4,5,6,7,9,10,46,47,48,49,50,51,
  76,77,78,79,80,81,82,83] = b4,b5+QM8
  (b6,7,9,10,76-79)+R7 (b3,46-51)+T4 (b80-83);
  RC-18 [4,5,6,7,9,10,11,12,13,20,76,77,78,
  79,80,81,82,83] = b4,b5+TR8 (b6,7,12,13,
  76-79)+TM8 (b9-11,20,80-83).
  PLAIN first-hand: AC b0..b3 = c0,94,17,fb ->
  sig c09417fb x16; AM 16/16 distinct.
  4SIG first-hand: CC b0,b1 = 25,57 + CM b2,b3
  map ORDERED 520f x6 @114543-48 + e20c @114549
  + f20b @114550 + 920c x2 @114551-52 ->
  2557520f x6 + 2557e20c + 2557f20b + 2557920c
  x2 (FIRST 6+1+1+2 C10 map); CM rows 0-5 share
  8B head 520f769791c36744 + distinct 4B tails
  (d037d006/f037d006/bff7820e/f8fc2833/
  41762933/80762933); CM 10/10 diverge.
  Code AC76/CC70/QC63/RC70; incl = +1/+1/+0/+0
  (A/C b5 const 7e, Q b5-step, T counter) =
  77/71/63/70;
  lane consts = A-692/A-345 INCL EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2810 n==114525 / P2811
  n==114526 singleton-const (offs 0/1);
  P281A 114527..114542 off=n-114527 PBA-PLAIN
  (m-tab 6B b48,49,76-79, sig c09417fb, b0 const
  c0, b5 const 7e);
  P281C 114543..114552 off=n-114543 C10-4SIG
  (m-tab 12B b2,3,46-51,80-83, partial sig b2,3
  in tab, b5 const 7e);
  P281Q 114553..114616 off=n-114553 m=off&15
  q=off>>4 QUAD2s row-split 5d7225ce x16 (row0)
  + 5d7225d4 x48 (rows1-3) (M 8B
  b6,7,9,10,76-79 NO frags + b3-led R7
  b3,46-51 r1==r2==r3 LAST3-PAIRED
  d4052931b9cf38 x3 + QT b80-83 e86c5231/
  4134a70c/53ecad0c/78ecad0c r2/r3 TRUE 3B
  ecad0c, b5 step off>=7 MID-ROW0);
  P281R(T88-ring) 114617..114872 off=n-114617
  c=off&15 r=off>>4 STANDARD sig 0c000000 (TM 8B
  b9-11,20,80-83 by COL + TR 8B b6,7,12,13,
  76-79 by ROW SPLIT tails UNPAIRED, b84-87
  const af/7c/ec/bc);
  A/C paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (b5-consts
  emerge from raw lencode); Q paylen 84 + raw
  lencode (b5-step emerges from raw lencode);
  R paylen 88 + counter b4=(0x73+2off)&FF
  b5=0x7f+(off>=71)+(off>=199).
  C blocks carry T76626/76631/76636/76651/
  76667/76690 py-line mirrors (exact); guards
  `if ((n) == (114525))` / `if ((n) == (114526))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 115+2*off + 127+(off>=71)+
  (off>=199);
  temps _t5906.._t5923 appended (base max _t5905,
  no reuse); _i max 3579->3590 (band 3581,3583,
  3587,3590), _b max 3578->3589 (band 3580,3582,
  3584,3585,3586,3588,3589), no reuse;
  C byte-index lists match py per block (A 6B,
  C 12B, Q 8/7/4B, R 8/8B); insert position exact
  (dispatch tail, N out-of-scope follows; C has 2
  scope hits, rfind-used; py has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (4SIG rows, all distinct);
  M 16/16 distinct; QR r1==r2==r3 LAST3-PAIRED
  exact (d4052931b9cf38 x3; r0 ceb6f8d1f53ff9
  distinct); 2 distinct;
  QT 4/4 distinct exact (e86c5231/4134a70c/
  53ecad0c/78ecad0c); r2/r3 share last 3B
  ecad0c; full all-pairs LCS (2,3)=3, (1,2)=
  (1,3)=1 from trailing 0c, rest 0;
  RQ==M PREFIX2+SUFFIX4 (M 8B vs RQ 8B:
  RQ[0:2]==M[0:2] 16/16 + RQ[4:8]==M[4:8]
  16/16, same-index agree vector [16,16,0,0,
  16,16,16,16], off-diagonal agree <=1/16,
  mid RQ[2:4] vs M[2:4] all-differ 16/16,
  RQ-mid 1:1 remap of M-mid 0067->0538 /
  ed66->6d37 / ee66->7537) -- joins the
  P257/P259 prefix+suffix family (12th odd-band
  RQ==M instance; prefix+suffix group now
  P257/P259/P281);
  tails SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P280T reference
  (overlap 0);
  QT 4/4 ALL NEW vs P280QT (overlap 0);
  RM ALL NEW vs P280RM.
  S0 NEW string (33/84 differ @ b0,4,5,11,
  18-24,26-29,32-37,52-55,72-79) + S1 NEW
  string (47/84 differ @ b4,5,22-40,42-55,
  72-83); P280S0 sig 58ae0700 ==
  A-690/A-343 predicted next PB0; P280S1/PBA/
  C10 2557520f/c09417fb/2557520f == predicted
  EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head bf/7e (114527)
  tail dd/7e (114542), b5set {7e}; C head df/7e
  (114543) tail f1/7e (114552), b5set {7e};
  Q head f3/7e (114553) step off6/7
  (114559->114560) ff/7e->01/7f MID-ROW0 +
  tail 71/7f (114616); quad formula ==raw-lencode
  64/64 mismatches 0.
  T head 73/7f (114617) + off70/71 (114687->
  114688) ff/7f->01/80 + mid off135 81/80
  (114752) + off198/199 (114815->114816)
  ff/80->01/81 + tail off255 71/81 (114872).
  All edge pins in for-list + PASS (batteries
  GREEN); 114872 tail pinned + in for-list +
  PASS (direct first-hand: oracle sha
  5d9af54748cdbb2d... matches PINS, py+C CLOSED
  T10P281R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (bb/7e, bd/7e) match raw
  lencode.
  Matches A-692/A-345 geometry (mixed-size 92x84B+
  256x88B, PB0 5eae0700 NEW + PB1 2557520f
  sigeq-P280PB1 47/84 diff, PBA16-PLAIN VPOS 7
  b5 const 7e NO pair, C10-4SIG VPOS 13 b5 const
  7e 10/10 diverge FIRST 6+1+1+2 map, QUAD2s
  VPOS 21 QM8+R7+T4 NO frags + R7 r1==r2==r3
  LAST3-PAIRED + tails r2/r3 3B ecad0c + M-tails
  ALL NEW 16/16, T88-ring STANDARD sig 0c000000
  TM8 by COL + TR8 by ROW UNPAIRED 16/16 + SPLIT
  tails + b84-87 const af7cecbc, quad MID-ROW0
  step off>=7 + ring edges + thresholds 71/199,
  NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 237/0
  rgram.py (+1/-1 for-line, +64/0 PINS); raw C 605
  content + 5 blank-only `+` lines / 0 del; raw py
  237 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 169, py del-uniq
  0 add-uniq 191). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 55198ed2..
  4ef44f6f, 912 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits (4 loose-`aa` hits = hex pairs
  inside PINS shas, strict pattern 0), shebang 0
  hits. Files touched: rgramc.c 610/0, rgram.py
  237/0, test_rgram.sh 1/1, PINS 64/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1574->1580 +6, singletons
  `if n == ` 594->596 +2, range-guards `<= n <=`
  576->580 +4, CLOSED T10P prints 1574->1580 +6,
  seal 1668->1674
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 589->591 +2,
  range 576->580 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b387 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-692-q793
  memo CONFIRM 37/37 (section heads shape 13/13 +
  quad+T-ring 13/13 + counters 11/11 quoted
  verbatim; tier cut SAFE)
  + A-345-q345 viewer corroborates same tier (all 3
  legs CONFIRM, consts 77/71/63/70 INCL).
  No DISSENT on P281. Agrees with cport commit msg
  (py/C 16558, PYID 8279).
- Quiz: no conflicting CLAIM/GATE/FLAG on b389/
  4ef44f6f. b388 EVEN = sweep2 turf (sweep2-r60 live
  b388+b390), used b388 tip as diff-base only, NOT
  gated. Newest PARENT-* is QNUM-19 (w2d Q-block
  only, read, no gate impact); PROSE-01 re-read
  before filing.
- Logs: NVME ws tmp/encode-sweep/r59/ (build389.log,
  pyid389.log, rgram389py/c.log, pass389py/c.txt,
  for388-old.nums/for389-new.nums, seteq389.py/log,
  smoke389.log, tables389.log, tables389-RQmid.log,
  tabaudit389.py, edges389.py, edges389.log,
  cdiff389.txt, pydiff389.txt, banddiff389.txt,
  added389.txt, numstat389.txt, build389/ binaries,
  tail-114872.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
