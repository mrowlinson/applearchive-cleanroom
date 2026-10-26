# GATE 9cac7b4f b393 T10P285 pins 115917..116264 (348 pins) PASS-functional

Seat sweep-r60, first-hand, WT tmp/wt-encode-sweep @9cac7b4f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r60.
Band = b82c0c66 (py merge w2b@b39d81f0 partial, +6 tiers
+62 pins) + 9cac7b4f (C port). Base 4ea39e1c (b392 tip,
1692 tiers sealed).

- Build: make -C src/c BUILDDIR=r60/build393 aae rgramc
  (flags -O2 -Wall -Wextra -std=c11 per Makefile), rc=0,
  0 warnings (log = make/cc command echoes only),
  build393/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r60,
  sha256 matches b354-b393 pinned value; band touches no
  aae sources), rgramc sha1 457b9614 / sha256 43e46a07.
- RGRAMC-PYID 8406/8406 covered=8406/8406 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 16812/16812 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 16812/16812 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (16812/16812, sorted).
- PINS-RGRAM cells set-eq 8406/8406 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 16814 rows (2 hdr + 16812, +62 vs base 16752).
  For-list union 8375->8406 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (115917 115918) +
  A 6 (head 115919 + 115920 + 115926 + 115927 +
  115933 + tail 115934; offs 0,1,7,8,14,15) +
  C 6 (head 115935 + 115936 + 115939 + 115940 +
  115943 + tail 115944; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 115937, 115938, 115941,
  115942) +
  Q 10 (head 115945 + off15/16 pair 115960/115961 +
  edge pair 115967/115968 + off32 115977 + off40
  115985 + off48 115993 + off55 116000 + tail
  116008; offs 0,15/16,22/23,32,40,48,55,63;
  b5 step, edge o22->23) +
  R 7 (head 116009 + edge pair 116095/116096 + mid
  116137 + edge pair 116223/116224 + tail 116264;
  offs 0,86/87,128,214/215,255).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines; 31x2 = 62 = 16812-16750.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P285 C-vs-py, 12-table A-PBA88-PLAIN/
  C10-1SIG/QUAD88-4R+T88-SWAPPED layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 19f80a00 / ddbef415 NEW, both NEW strings;
  diff vs P284S0/S1 34/84 @ b0-2,4-11,41-51,56-67 +
  55/84 @ b0-11,13-17,19-23,30-39,45-51,60-71,
  80-83);
  AM 16/16 (9B), CM 10/10 (12B), M 16/16 (8B),
  QR 4/4 (11B), RM 16/16 (7B), RQ 16/16 (7B)
  EXACT;
  AC 77/77, CC 70/70, QC 67/67, RC 72/72 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 77/70/67/72 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit393.py 98 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42/H42/L42 (no b42), no QB/PT/FM,
  no RT/TT (SWAPPED ring, not ROWTAIL), no QT
  (R11 carries b84-87 inside QR); table inventory
  exactly the 12.
  Missing-sets first-hand EXACT: AC-11 [4,5,28,29,
  30,31,32,80,81,82,83] = b4,b5+M9 (b28-32,
  80-83);
  CC-14 [4,5,24,25,26,27,28,29,30,31,80,81,82,
  83] = b4,b5+M12 (b24-31,80-83);
  QC-21 [4,5,25,26,27,28,29,30,31,32,33,34,35,
  80,81,82,83,84,85,86,87] = b4,b5+QM8 (b25-27,
  35,80-83)+R11 (b28-34,84-87);
  RC-16 [4,5,29,34,35,40,41,42,76,77,78,79,80,
  81,82,83] = b4,b5+TR7 (b29,34,35,80-83)+
  TM7 (b40-42,76-79).
  PLAIN first-hand: AC b0..b3 = 01,00,00,00 ->
  sig 01000000 x16; AM 16/16 distinct.
  1SIG first-hand: CC b0..b3 = cd,23,fd,15 const
  -> cd23fd15 x10; CM 10/10 diverge (rows0-5
  share 8B head 913cb87bb5cbe01a, rows6-9 own
  heads da7ca5b2/b07c1209/9cfcf300).
  Code AC77/CC70/QC67/RC72; incl = +1/+1/+0/+0
  (A/C b5 const 89, Q b5-step, T counter) =
  78/71/67/72;
  lane consts = A-709/A-349 INCL EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2850 n==115917 / P2851
  n==115918 singleton-const (offs 0/1);
  P285A 115919..115934 off=n-115919 PBA88-PLAIN
  (m-tab 9B b28-32,80-83, sig 01000000, b0 const
  01, b5 const 89);
  P285C 115935..115944 off=n-115935 C10-1SIG
  (m-tab 12B b24-31,80-83, full sig b0-3 in
  consts, b5 const 89);
  P285Q 115945..116008 off=n-115945 m=off&15
  q=off>>4 QUAD88-4R single-sig 01000000 x64 (M 8B
  b25-27,35,80-83 NO frags + R11 b28-34,84-87
  r0 413c512d95c6ca7c4d8899 distinct + r123 share
  7B prefix fdbce3ce75d9f2 + last byte 5f, tails
  b84-87 4 distinct 7c4d8899/a28eab5f/1719ad5f/
  eab0da5f, b5 0x89+(o>=23) step o22->23);
  P285R(T88-ring) 116009..116264 off=n-116009
  c=off&15 r=off>>4 SWAPPED sig 16000000 (TM 7B
  b40,41,42,76-79 by COL + TR 7B b29,34,35,
  80-83 by ROW SPLIT tails UNPAIRED, b84-87 const
  e4/65/4e/71);
  A paylen 88 / C paylen 84 / Q paylen 88 + raw
  lencode l16=((n<<1)|1) &0xFFFF pay4=l16&0xFF
  pay5=l16>>8 (b5-consts emerge from raw lencode);
  R paylen 88 +
  counter b4=(0x53+2off)&FF b5=0x8a+(off>=87)+
  (off>=215).
  C blocks carry T77591/77596/77601/77616/77632/
  77653 py-line mirrors (exact); guards
  `if ((n) == (115917))` / `if ((n) == (115918))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 83+2*off + 138+(off>=87)+
  (off>=215); temps _t5980.._t5995 appended (base
  max _t5979, no reuse); _i max 3622->3632 (band
  3624,3626,3629,3632), _b max 3621->3631 (band
  3623,3625,3627,3628,3630,3631), no reuse;
  C byte-index lists match py per block (A 9B,
  C 12B, Q 8B/11B, R 7/7B); insert
  position exact (dispatch tail, N out-of-scope
  follows; C has 2 scope hits, rfind-used; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0
  413c512d95c6ca7c4d8899; r123
  fdbce3ce75d9f2a28eab5f/
  fdbce3ce75d9f21719ad5f/
  fdbce3ce75d9f2eab0da5f);
  QR all-pairs lcsuf (1,2)=(1,3)=(2,3)=1,
  r0-vs-rest 0; r123 last byte 5f;
  RQ==M TAILS-only (M 8B vs RQ 7B: RQ[3:7]==
  M[4:8] 16/16, agree matrix clean tail block
  at (3,4),(4,5),(5,6),(6,7), RQ[0:3] own (max
  agree 1/16, RQ0 3-distinct 0f/1e/1f, RQ1
  7-distinct 10/30/50/70/90/b0/d0 lo-nibble 0,
  RQ2 16-distinct)) -- tails-only degree (joins
  P255/P263/P267 group); 14th odd-band RQ==M
  instance;
  tails SWAPPED-SPLIT (RM b76-79 by COL c=off&15,
  RQ b80-83 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P284T RM col-led tails
  (overlap 0); RM-tails ALL NEW vs P284T tails
  (overlap 0);
  S0 NEW string (34/84 differ @ b0-2,4-11,41-51,
  56-67) + S1 NEW string (55/84 differ @ b0-11,
  13-17,19-23,30-39,45-51,60-71,80-83);
  P284S0 sig 99f00700 == A-699/A-347 predicted
  next PB0; P284S1/PBA/C10 4513630f/5d3431f6/
  c432f015 == predicted EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 9f/89 (115919)
  tail bd/89 (115934), b5set {89}; C head bf/89
  (115935) tail d1/89 (115944), b5set {89};
  Q head d3/89 (115945) tail 51/8a (116008),
  b5set {89,8a} step + edge o22->23 (115967->
  115968) ff/89->01/8a;
  quad formula == raw-lencode 64/64 mismatches 0.
  T head 53/8a (116009) + off86/87 (116095->
  116096) ff/8a->01/8b + mid off128 53/8b
  (116137) + off214/215 (116223->116224)
  ff/8b->01/8c + tail off255 51/8c (116264).
  All edge pins in for-list + PASS (batteries
  GREEN); 116264 tail pinned + in for-list +
  PASS (direct first-hand: oracle sha
  eb239b51ba87fa53... matches PINS, py+C CLOSED
  T10P285R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (9b/89, 9d/89) match raw
  lencode.
  Matches A-709/A-349 geometry (12x84B+336x88B,
  PB0 19f80a00 NEW + PB1 ddbef415 NEW, PBA88-PLAIN
  VPOS 10 b5 const 89 NO pair, C10-1SIG VPOS 13
  b5 const 89 10/10 diverge, QUAD88-4R VPOS 21
  QM8+R11 NO frags + R11 4/4 UNPAIRED + tails
  b84-87 4 distinct + M-tails ALL NEW 16/16,
  T88-ring SWAPPED sig 16000000 TM7 by COL + TR7
  by ROW UNPAIRED 16/16 + SPLIT tails + b84-87
  const e4654e71, quad b5-step + edge o22->23 +
  ring edges + thresholds 87/215, NO D dips).
- C diff pure-add: numstat 604/0 rgramc.c + 230/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 599
  content + 5 blank-only `+` lines / 0 del; raw py
  230 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 166, py del-uniq
  0 add-uniq 183). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 4ea39e1c..
  9cac7b4f, 897 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 604/0, rgram.py 230/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1598->1604 +6, singletons
  `if n == ` 602->604 +2, range-guards `<= n <=`
  592->596 +4, CLOSED T10P prints 1598->1604 +6,
  seal 1692->1698
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 597->599 +2,
  range 592->596 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b391 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-709-q797
  memo CONFIRM 36/36 (section heads shape 13/13 +
  quad+T-ring 11/11 + counters 12/12 quoted
  verbatim; tier cut SAFE; w2b-r23 2/8 new 12+336
  shape gated)
  + A-349-q349 viewer corroborates same tier (all
  legs CONFIRM, consts 78/71/67/72 INCL).
  No DISSENT on P285. Agrees with cport commit msg
  (py/C 16812, PYID 8406).
- Quiz: no conflicting CLAIM/GATE/FLAG on b393/
  9cac7b4f. b392 EVEN = sweep2 turf, used b392 tip
  as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-19 (w2d Q-block
  only, read, no gate impact); PROSE-01 re-read
  before filing.
- Logs: NVME ws tmp/encode-sweep/r60/ (build393.log,
  pyid393.log, rgram393py/c.log, pass393py/c.txt,
  for392-old.nums/for393-new.nums, seteq393.py/log,
  smoke393.log, tables393.log,
  tabaudit393.py, edges393.py, edges393.log,
  cdiff393.txt, pydiff393.txt, banddiff393.txt,
  added393.txt, numstat393.txt, build393/ binaries,
  tail-116264.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
