# GATE 69eaa7e9 b387 T10P279 pins 113829..114176 (348 pins) PASS-functional

Seat sweep-r58, first-hand, WT tmp/wt-encode-sweep @69eaa7e9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r58.
Band = bff93d36 (py merge w2b@3e774788 partial, +6 tiers
+66 pins) + 69eaa7e9 (C port). Base e3caa64f (b386 tip,
1656 tiers sealed).

- Build: make -C src/c BUILDDIR=r58/build387 aae rgramc
  (flags -O2 -Wall -Wextra -std=c11 per Makefile), rc=0,
  0 warnings (log = make/cc command echoes only),
  build387/{aae,rgramc}. aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r58,
  sha256 matches b354-b387 pinned value; band touches no
  aae sources), rgramc sha1 f785d34b / sha256 7d76c33d.
- RGRAMC-PYID 8218/8218 covered=8218/8218 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 16436/16436 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 16436/16436 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (16436/16436, sorted).
- PINS-RGRAM cells set-eq 8218/8218 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 16438 rows (2 hdr + 16436, +66 vs base 16372).
  For-list union 8185->8218 +33/-0 (python sets,
  trailing-';' stripped, never comm).
  33 = 2 sing (113829 113830) +
  A 8 (head 113831 + 113832 + 113841 + 113842 +
  113843 + 113844 + 113845 + tail 113846; offs
  0,1,10,11,12,13,14,15; SPLIT-dense: x12 tail
  pair + full x4 part) +
  C 6 (head 113847 + 113848 + 113850 + 113853 +
  113855 + tail 113856; offs 0,1,3,6,8,9; offs
  2,4,5,7 unsampled: 113849, 113851, 113852,
  113854) +
  Q 10 (head 113857 + off7 113864 + edge pair
  113872/113873 + mid pair 113888/113889 + mid
  pair 113904/113905 + LAST pair 113919/113920;
  offs 0,7,15/16,31/32,47/48,62/63; b5 step
  off>=63 LAST-CELL) +
  R 7 (head 113921 + off64 113985 + edge pair
  114047/114048 + mid 114112 + LAST pair
  114175/114176; offs 0,64,126/127,191,
  254/255).
  PINS adds = same 33 tier pins. Each for-N yields 2 PASS
  lines; 33x2 = 66 = 16436-16370.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P279 C-vs-py, 13-table A-PBA-SPLIT/
  C10-1SIG/QUAD2s+T88-STANDARD layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs b8aa0700 / 74b05c0f NEW, both NEW strings;
  diff vs P278S0/S1 32/84 @ b0,4,5,30-32,34-41,
  44-49,56-59,76-83 + 75/84);
  AM 16/16 (8B), CM 10/10 (11B), M 16/16 (7B),
  QR 4/4 (7B), QT 4/4 (4B), RM 16/16 (8B),
  RQ 16/16 (6B)
  EXACT;
  AC 74/74, CC 71/71, QC 64/64, RC 72/72 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 74/71/64/72 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit387.py 94 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42 (no b42 staging), no QB/PT/FM, no
  RT/TT (STANDARD ring, not ROWTAIL); table
  inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-10 [0,4,5,9,
  10,11,76,77,78,79] = b0,b4,b5+M7 (b9-11,
  76-79);
  CC-13 [4,5,13,14,15,16,17,18,19,80,81,82,
  83] = b4,b5+M11 (b13-19,80-83);
  QC-20 [0,1,2,3,4,5,12,13,16,17,18,19,76,
  77,78,79,80,81,82,83] = b4,b5+QM7
  (b12,13,19,76-79)+sig-led R7 (b0-3,16-18)
  +T4 (b80-83);
  RC-16 [4,5,20,21,28,29,30,31,76,77,78,79,
  80,81,82,83] = b4,b5+TR6 (b20,21,76-79)
  +TM8 (b28-31,80-83).
  SPLIT first-hand: AM b0 ORDERED c6 x12 (offs
  0-11) + c8 x4 (offs 12-15); AC b1-3 =
  05,cb,f5 -> sigs c605cbf5 x12 @113831-42 +
  c805cbf5 x4 @113843-46; AM 16/16 distinct.
  1SIG first-hand: CM rows 0-5 share 7B head
  ecbc91fba16787 + distinct 4B tails
  (56aa120f/76aa120f/b34f130f/37c9801d/
  76c9801d/96c9801d), rows 6-9 all-distinct;
  CC b0..b3 = 5e,b0,5c,0f -> sig 5eb05c0f x10;
  CM 10/10 diverge.
  Code AC74/CC71/QC64/RC72; incl = +1/+1/+0/+0
  (A/C b5 const 79, Q b5-step, T counter) =
  75/72/64/72;
  lane consts = A-690/A-343 INCL EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2790 n==113829 / P2791
  n==113830 singleton-const (offs 0/1);
  P279A 113831..113846 off=n-113831 PBA-SPLIT
  (m-tab 8B b0,9-11,76-79 covers split, sigs
  c605cbf5/c805cbf5, b5 const 79);
  P279C 113847..113856 off=n-113847 C10-1SIG
  (m-tab 11B b13-19,80-83, b5 const 79);
  P279Q 113857..113920 off=n-113857 m=off&15
  q=off>>4 QUAD2s row-split a09b0ff6 x16 (row0)
  + 00928ff4 x48 (rows1-3) (M 7B
  b12,13,19,76-79 NO frags + sig-led R7
  b0-3,16-18 r1==r2==r3 LAST3-PAIRED
  00928ff4c51894 x3 + QT b80-83 9aa19575/
  7f90f0d4/a490f0d4/c990f0d4 r1/r2/r3 share
  3B 90f0d4, b5 step off>=63 LAST-CELL);
  P279R(T88-ring) 113921..114176 off=n-113921
  c=off&15 r=off>>4 STANDARD sig 0f000000 (TM 8B
  b28-31,80-83 by COL + TR 6B b20,21,76-79
  by ROW SPLIT tails UNPAIRED, b84-87
  const 75/da/a8/0b);
  A/C paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (b5-consts
  emerge from raw lencode); Q paylen 84 + raw
  lencode (b5-step emerges from raw lencode);
  R paylen 88 + counter b4=(0x03+2off)&FF
  b5=0x7a+(off>=127)+(off>=255).
  C blocks carry T76152/76157/76162/76177/
  76193/76216 py-line mirrors (exact); guards
  `if ((n) == (113829))` / `if ((n) == (113830))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 3+2*off + 122+(off>=127)+
  (off>=255);
  temps _t5870.._t5887 appended (base max _t5869,
  no reuse); _i max 3557->3568 (band 3559,3561,
  3565,3568), _b max 3556->3567 (band 3558,3560,
  3562,3563,3564,3566,3567), no reuse;
  C byte-index lists match py per block (A 8B,
  C 11B, Q 7/7/4B, R 8/6B); insert position exact
  (dispatch tail, N out-of-scope follows; C has 2
  scope hits, rfind-used).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (1SIG rows, all distinct);
  M 16/16 distinct; QR r1==r2==r3 LAST3-PAIRED
  exact (00928ff4c51894 x3; r0 a09b0ff6f9d44c
  distinct); 2 distinct;
  QT 4/4 distinct exact (9aa19575/7f90f0d4/
  a490f0d4/c990f0d4); r1/r2/r3 share last 3B
  90f0d4 (tails echo the R last3-pairing; r0
  last-2B 9575 distinct);
  RQ==M HEAD1+SHIFT FIRST (M 7B vs RQ 6B:
  byte1 identical 16/16 + RQ[2:6]==M[3:7]
  16/16, same-index agree vector [0,16,0,0,0,0],
  RQ[0] own 16 distinct 6c/73/04/15/64/94/be/
  4f/52/70/9c/c0/02/12/88/e3 with no small
  formula over any M byte: xor/add/sub+const
  0/5376) -- new degree beyond the ten known
  instances (P253 DISJOINT, P255/P263/P267
  tails-only, P257/P259 prefix+suffix, P261/P265
  FULL-STRING, P269 HEAD-REMAP, P271
  MID+TAILS-SKIP, P273 HEAD2+TAILS, P275
  HEADS+SHIFT);
  tails SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P278T col-0 reference
  (overlap 0);
  QT 4/4 ALL NEW vs P278QT (overlap 0);
  RM ALL NEW vs P278RM.
  S0 NEW string (32/84 differ @ b0,4,5,30-32,
  34-41,44-49,56-59,76-83) + S1 NEW string
  (75/84 differ); P278S0 sig b0aa0700 ==
  A-682/A-341 predicted next PB0; P278S1/PBA/
  C10 f5f4570f/e09a1ffa/f5f4570f == predicted
  EXACT (PB1 == P277C10sig as predicted).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 4f/79 (113831)
  tail 6d/79 (113846), b5set {79}; C head 6f/79
  (113847) tail 81/79 (113856), b5set {79};
  Q head 83/79 (113857) step off62/63
  (113919->113920) ff/79->01/7a LAST-CELL +
  tail 01/7a (113920); quad formula ==raw-lencode
  64/64 mismatches 0.
  T head 03/7a (113921) + off64 83/7a (113985) +
  off126/127 (114047->114048) ff/7a->01/7b +
  mid off191 81/7b (114112) + LAST off254/255
  (114175->114176) ff/7b->01/7c.
  All edge pins in for-list + PASS (batteries
  GREEN); 114176 tail pinned + in for-list +
  PASS (direct first-hand: oracle sha
  12d03ff936fda249... matches PINS, py+C CLOSED
  T10P279R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (4b/79, 4d/79) match raw
  lencode.
  Matches A-690/A-343 geometry (mixed-size 92x84B+
  256x88B, PB0 b8aa0700 NEW + PB1 74b05c0f NEW,
  PBA16-SPLIT12/4 VPOS 9 b5 const 79 NO pair,
  C10-1SIG VPOS 12 b5 const 79 10/10 diverge,
  QUAD2s VPOS 20 QM7+R7+T4 NO frags + sig-led R7
  r1==r2==r3 LAST3-PAIRED + tails r1/r2/r3 3B
  90f0d4 + M-tails ALL NEW 16/16,
  T88-ring STANDARD sig 0f000000 TM8 by COL +
  TR6 by ROW UNPAIRED 16/16 + SPLIT tails +
  b84-87 const 75daa80b, quad LAST-CELL step +
  ring edges + thresholds 127/255, NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 237/0
  rgram.py (+1/-1 for-line, +66/0 PINS); raw C 605
  content + 5 blank-only `+` lines / 0 del; raw py
  237 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 171, py del-uniq
  0 add-uniq 192). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope e3caa64f..
  69eaa7e9, 914 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 610/0, rgram.py 237/0,
  test_rgram.sh 1/1 (for-line), PINS 66/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1562->1568 +6, singletons
  `if n == ` 590->592 +2, range-guards `<= n <=`
  568->572 +4, CLOSED T10P prints 1562->1568 +6,
  seal 1656->1662
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 585->587 +2,
  range 568->572 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b385 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-690-q791
  memo CONFIRM 37/37 (section heads shape 12/12 +
  quad+T-ring 13/13 + counters 12/12 quoted
  verbatim; tier cut SAFE)
  + A-343-q343 viewer corroborates same tier (all 3
  legs CONFIRM, consts 75/72/64/72 INCL).
  No DISSENT on P279. Agrees with cport commit msg
  (py/C 16436, PYID 8218).
- Quiz: no conflicting CLAIM/GATE/FLAG on b387/
  69eaa7e9. b386 EVEN = sweep2 turf (all evens are),
  used b386 tip as diff-base only, NOT gated. Newest
  PARENT-* is QNUM-18 (w2e/w2f Q-blocks only, read, no
  gate impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r58/ (build387.log,
  pyid387.log, rgram387py/c.log, pass387py/c.txt,
  for386-old.nums/for387-new.nums, seteq387.py/log,
  smoke387.log, tables387.log, tables387-RQ0.log,
  tabaudit387.py, edges387.log, edges387.py,
  cdiff387.txt, pydiff387.txt, banddiff387.txt,
  added387.txt, build387/ binaries, tail-114176.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
