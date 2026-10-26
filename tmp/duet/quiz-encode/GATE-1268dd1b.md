# GATE 1268dd1b b369 T10P261 pins 107565..107912 (348 pins) PASS-functional

Seat sweep-r54, first-hand, WT tmp/wt-encode-sweep @1268dd1b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r54.
Band = 26a82bdb (py merge w2b@fd38b136 partial, +6 tiers
+62 pins) + 1268dd1b (C port). Base 8676784a (b368 tip,
1548 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build369/{aae,rgramc}, rc=0,
  0 warnings. aae sha1 7d8dd3a2 / sha256 d6e27c97
  (pinned stable continues: sha1 r39-r54, sha256 matches
  b354-b367 pinned value; band touches no aae sources),
  rgramc sha1 768e4574 / sha256 cb10fde2.
- RGRAMC-PYID 7649/7649 covered=7649/7649 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 15298/15298 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 15298/15298 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (15298/15298, sorted).
- PINS-RGRAM cells set-eq 7649/7649 (xor 0 all 3 ways:
  for^pass for^pins pass^pins; py^C 0).
  PINS 15300 rows (2 hdr + 15298, +62 vs base 15238).
  For-list union 7618->7649 +31/-0 (python sets, never
  comm).
  31 = 2 sing (107565 107566) +
  A 6 (head 107567 + 107568 + 107572 + 107577 +
  107581 + tail 107582) +
  B 6 (head 107583 + 107584 + 107586 + 107589 +
  107591 + tail 107592; offs 2,4,5,7 unsampled:
  107585, 107587, 107588, 107590) +
  Q 10 (head 107593 + row-edge pair 107608/107609 +
  row-edge pair 107624/107625 + row-edge pair
  107640/107641 + carry pair 107647/107648 + tail
  107656) +
  R 7 (head 107657 + edge pair 107775/107776 + mid
  107840 + edge pair 107903/107904 + tail 107912).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 31x2 = 62 = 15298-15236.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var).
- Tables audit P261 C-vs-py, 13-table A-PBA/B10/
  QUAD-r02+T88 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 0f550300 NEW / adecad06 NEW, both NEW strings);
  AM 16/16 (8B), BM 10/10 (12B), M 16/16 (8B),
  QR 4/4 (7B), QT 4/4 (4B), RM 16/16 (7B),
  RQ 16/16 (8B) EXACT;
  AC 74/74, BC 70/70, QC 63/63, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 74/70/63/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit369.py 100 PASS 0 FAIL).
  No CM/CC (B10, not C10), no QB (not pair-led), no
  PT/FM/M42/X42; table inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-10 [4,5,24,25,26,
  27,76,77,78,79] = b4,b5+M8 (b24-27,76-79);
  BC-14 [4,5,24,25,26,27,28,29,30,31,80,81,82,83]
  = b4,b5+M12 (b24-31,80-83);
  QC-21 [4,5,21,22,23,24,25,26,27,28,29,30,31,76,
  77,78,79,80,81,82,83] = b4,b5+QM8 (b21-23,31,
  76-79)+R7 (b24-30)+T4 (b80-83);
  RC-17 [4,5,25,26,27,35,40,41,42,76,77,78,79,80,
  81,82,83] = VPOS 17 over 0..87 (b4,b5+TM7
  b40-42,76-79 + TR8 b25-27,35,80-83).
  b0-3 first-hand: AC b0-3 e08ad76e (NEW);
  BC b0-3 35fda506 (single-sig B10);
  QC b0-3 e08ad76e (==PBA sig, single-sig quad);
  RC 06000000 (==P252/253/256/259T sig).
  Code AC74/BC70/QC63/RC71; incl = +1/+1/+0/+0
  (A/B b5 const 48, Q b5-carry, T counter) =
  75/71/63/71; lane consts = A-624/A-325 INCL
  EXACT (writer PBA/B10 = memo-1; quad/T88
  identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/B/Q/R): P2610 n==107565 / P2611
  n==107566 singleton-const (offs 0/1);
  P261A 107567..107582 off=n-107567 PBA16
  (m-tab 8B b24-27,76-79, sig e08ad76e NEW,
  b5 const 48);
  P261B 107583..107592 off=n-107583 B10 single-sig
  (m-tab 12B b24-31,80-83, b5 const 48);
  P261Q 107593..107656 off=n-107593 m=off&15
  q=off>>4 single-sig quad (M 8B b21-23,31,76-79
  + R7 7B b24-30 r0==r2 EVEN-PAIRED + QT b80-83
  r0/r2 TRUE-3B a0e666, b5-carry 48->49 @107647->
  107648);
  P261R(T88-ring) 107657..107912 off=n-107657
  c=off&15 r=off>>4 STANDARD sig 06000000 (TM 7B
  b40-42,76-79 by COL + TR 8B b25-27,35,80-83
  by ROW SPLIT tails, b84-87 const 22/ec/f4/2b);
  A/B/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8; R paylen 88
  + counter b4=(0x13+2off)&FF b5=0x49+(off>=119)+
  (off>=247).
  C blocks carry T71565/71570/71575/71590/71606/
  71629 py-line mirrors (exact); guards
  `if ((n) == (107565))` / `if ((n) == (107566))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 19+2*off + 73+(off>=119)+
  (off>=247);
  temps _t5520.._t5537 appended (base max _t5519,
  no reuse); _i max 3356->3367 (band 3358,3360,
  3364,3367), _b max 3355->3366 (band 3357,3359,
  3361,3362,3363,3365,3366), no reuse; C byte-index
  lists match py per block (A 8B, B 12B, Q 8/7/4B,
  R 7/8B); insert position exact (dispatch tail, N
  out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct;
  BM 10/10 diverge (single-sig rows, all distinct);
  M 16/16 distinct;
  QR r0==r2 EVEN-PAIRED exact (e53cf3d4b53eb1 x2;
  r1 5f3c623315b6d1 + r3 f6bcd40cf5d63e
  distinct -- first EVEN r02 pair);
  QT 4/4 distinct exact (7fa0e666/9517fb30/
  caa0e666/027177fa); r0/r2 share TRUE-3B a0e666
  (matching R-pair); last2B e666/fb30/e666/77fa
  (3-unique);
  RQ==M FULL-STRING 16/16 same-index + set-eq (8B
  rows identical in order -- FOURTH family after
  P253 DISJOINT + P255 tails-only + P257/P259
  prefix+suffix; oracle-true per GREEN batteries +
  memo TR8 16/16 UNPAIRED by-ROW CONFIRM);
  tails SPLIT (RM b76-79 by COL c=off&15, RQ
  b80-83 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P260T (P260 RM 9B
  b76-79 col-led via TM9, overlap 0; M-full also
  ALL NEW vs P260RQ);
  QT 4/4 NEW vs P260QT
  (fdc59ac8/f4840360/70affd40/12ee7121).
  S0 NEW string (sig 0f550300 NEW; P260S0 sig
  2f370300); S1 NEW (sig adecad06 NEW; P260S1
  sig 05010206).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 5f/48 (107567)
  tail 7d/48 (107582), b5set {48}; B head 7f/48
  (107583) tail 91/48 (107592), b5set {48}; Q
  head 93/48 (107593) tail 11/49 (107656), b5set
  {48,49}, carry ff/48->01/49 @107647->107648
  (single flip, off54->55).
  T head 13/49 (107657) + off118/119 (107775->
  107776) ff/49->01/4a + off246/247 (107903->
  107904) ff/4a->01/4b + mid off183 81/4a
  (107840) + tail off255 11/4b (107912). All
  edge pins in for-list + PASS (batteries GREEN);
  107912 tail pinned + in for-list + PASS.
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (5b/48, 5d/48) match raw
  lencode.
  Matches A-624/A-325 geometry (mixed-size 92x84B+
  256x88B, PB0 0f550300 NEW + PB1 adecad06
  NEW, PBA16 VPOS 9 b5 const
  48 16/16 distinct NO pair, B10 single-sig VPOS
  13 b5 const 48 10/10 diverge, QUAD single-sig
  VPOS 21 QM8 shared + R7 r0==r2 EVEN-PAIRED +
  tails 4/4 r0/r2 TRUE-3B + M-tails ALL NEW 16/16,
  T88-ring STANDARD sig 06000000 TM7 by COL + TR8
  by ROW UNPAIRED 16/16 + SPLIT tails + b84-87
  const 22ecf42b, ring edges + thresholds 119/247,
  NO D dips).
- C diff pure-add: numstat 610/0 rgramc.c + 237/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 605
  content + 5 blank-only `+` lines / 0 del; raw py
  237 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 159, py del-uniq
  0 add-uniq 183). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 8676784a..
  1268dd1b, 910 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 610/0, rgram.py 237/0,
  test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1454->1460 +6, singletons
  `if n == ` 554->556 +2, range-guards `<= n <=`
  496->500 +4, CLOSED T10P prints 1454->1460 +6,
  seal 1548->1554
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 549->551 +2,
  range 496->500 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357/b359/b361/b363/b365/b367), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-624-q773
  memo CONFIRM 34/34 verdict (shape 12/12 +
  quad+Tring 11/11 + counters 11/11 quoted verbatim;
  R7 r0==r2 EVEN-PAIRED first + tails r0/r2 TRUE-3B
  programmatic re-verify, tier cut SAFE)
  + A-325-q325 viewer corroborates same tier (3/3
  legs CONFIRM, consts 75/71/63/71 INCL).
  No DISSENT on P261. Agrees with cport commit msg
  (py/C 15298, PYID 7649).
- Quiz: no conflicting CLAIM/GATE/FLAG on b369/
  1268dd1b. b368/b370 EVEN = sweep2 turf, used b368
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-12 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r54/ (build369.log,
  pyid369.log, rgram369py/c.log, pass369py/c.txt,
  pins368base.csv, for368-old.nums/for369-new.nums,
  smoke369.log, tables369.log, tabaudit369.py,
  edges369.log, cdiff369.txt, pydiff369.txt,
  banddiff369.txt, build369/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
