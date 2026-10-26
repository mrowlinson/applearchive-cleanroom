# GATE 376bc6a9 b377 T10P269 pins 110349..110696 (348 pins) PASS-functional

Seat sweep-r56, first-hand, WT tmp/wt-encode-sweep @376bc6a9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r56.
Band = 5ccbc0a1 (py merge w2b@155cdd49 partial, +6 tiers
+64 pins) + 376bc6a9 (C port). Base 42e6be18 (b376 tip,
1596 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 (direct invocation,
  flags per r55 build373.log), build377/{aae,rgramc}, rc=0,
  0 warnings (empty build log). aae sha1 7d8dd3a2 /
  sha256 d6e27c97 (pinned stable continues: sha1 r39-r56,
  sha256 matches b354-b377 pinned value; band touches no
  aae sources), rgramc sha1 c05ac326 / sha256 26edbfc6.
- RGRAMC-PYID 7899/7899 covered=7899/7899 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 15798/15798 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 15798/15798 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (15798/15798, sorted).
- PINS-RGRAM cells set-eq 7899/7899 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 15800 rows (2 hdr + 15798, +64 vs base 15736).
  For-list union 7867->7899 +32/-0 (python sets,
  trailing-';' stripped, never comm).
  32 = 2 sing (110349 110350) +
  A 6 (head 110351 + 110352 + 110356 + 110361 + 110365
  + tail 110366; offs 0,1,5,10,14,15) +
  C 6 (head 110367 + 110368 + 110370 + 110373 + 110375
  + tail 110376; offs 0,1,3,6,8,9; offs 2,4,5,7
  unsampled: 110369, 110371, 110372, 110374) +
  Q 10 (head 110377 + off7 110384 + triple
  110391/110392/110393 + edge pair 110408/110409 +
  edge pair 110424/110425 + tail 110440; offs 0,7,
  14/15/16,31/32,47/48,63; b5 const 5e, NO step) +
  R 8 (head 110441 + edge pair 110463/110464 + mid
  110584 + edge pair 110591/110592 + 110665 + tail
  110696; offs 0,22/23,143,150/151,224,255).
  PINS adds = same 32 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 32x2 = 64 = 15798-15734.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var).
- Tables audit P269 C-vs-py, 14-table A-PBA-PLAIN/
  C10-1SIG/QUAD1s+T88-ROWTAIL layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs a4930300 NEW / 3d502907 NEW, both NEW strings);
  AM 16/16 (6B), CM 10/10 (12B), M 16/16 (10B),
  QR 4/4 (7B), QT 4/4 (4B), RM 16/16 (7B), RQ 16/16
  (6B), RT 16/16 (4B) EXACT;
  AC 76/76, CC 70/70, QC 61/61, RC 69/69 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/70/61/69 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit377.py 129 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no frags),
  no M42/X42 (no b42 staging), no QB/PT/FM; table
  inventory exactly the 14.
  Missing-sets first-hand EXACT: AC-8 [4,5,24,25,76,
  77,78,79] = b4,b5+M6 (b24,25,76-79);
  CC-14 [4,5,24,25,26,27,28,29,30,31,80,81,82,83]
  = b4,b5+M12 (b24-31,80-83);
  QC-23 [4,5,14,15,21,22,23,24,25,26,27,28,29,30,
  31,76,77,78,79,80,81,82,83] = b4,b5+QM10
  (b14,15,21,22,23,31,76-79)+R7 (b24-30)+T4
  (b80-83);
  RC-19 [4,5,18,19,25,26,27,35,40,41,42,76,77,
  78,79,80,81,82,83] = b4,b5+TR6 (b18,19,25-27,
  35)+TM7 (b40-42,76-79)+TT4 (b80-83).
  1SIG first-hand: CC b0-3 const a5322507 (full sig
  const); CM 10/10 diverge.
  Code AC76/CC70/QC61/RC69; incl = +1/+1/+1/+0
  (A/C/Q b5 const 5e, T counter) = 77/71/62/69;
  lane consts = A-653/A-333 INCL EXACT (writer
  PBA/C10/quad = memo-1; T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2690 n==110349 / P2691
  n==110350 singleton-const (offs 0/1);
  P269A 110351..110366 off=n-110351 PBA-PLAIN
  (m-tab 6B b24,25,76-79, sig 208c277e b0 const 20,
  b5 const 5e);
  P269C 110367..110376 off=n-110367 C10-1SIG
  (m-tab 12B b24-31,80-83, b5 const 5e NO carry);
  P269Q 110377..110440 off=n-110377 m=off&15
  q=off>>4 QUAD1s single-sig 208c277e (M 10B
  b14,15,21-23,31,76-79 shared + R7 b24-30
  r1==r2==r3 LAST3-PAIRED + QT b80-83 r1/r2/r3
  TRUE-3B 559c98, b5 const 5e NO step);
  P269R(T88-ROWTAIL) 110441..110696 off=n-110441
  c=off&15 r=off>>4 FIRST row-led-tail sig
  07000000 (TM 7B b40-42,76-79 by COL + TR 6B
  b18,19,25-27,35 by ROW 15/16 r14==r15 PAIRED
  tails disambiguate + TT 4B b80-83 ROW-led by
  row, b84-87 const 1b/2a/63/22);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8; R paylen 88
  + counter b4=(0xd3+2off)&FF b5=0x5e+(off>=23)+
  (off>=151).
  C blocks carry T73662/73667/73672/73687/73703/
  73727 py-line mirrors (exact); guards
  `if ((n) == (110349))` / `if ((n) == (110350))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 211+2*off + 94+(off>=23)+
  (off>=151);
  temps _t5678.._t5697 appended (base max _t5677,
  no reuse); _i max 3443->3455 (band 3445,3447,
  3451,3455), _b max 3442->3454 (band 3444,3446,
  3448,3449,3450,3452,3453,3454), no reuse;
  C byte-index lists match py per block (A 6B,
  C 12B, Q 10/7/4B, R 7/6/4B); insert position
  exact (dispatch tail, N out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (1SIG rows, all distinct);
  M 16/16 distinct;
  QR r1==r2==r3 LAST3-PAIRED exact (23bc65c2d5c02d
  x3; r0 957c910d55dd0a distinct); 2 distinct;
  QT 4/4 distinct exact (86296322/7d559c98/
  a2559c98/c7559c98); r1/r2/r3 share TRUE 3B
  559c98 (first bytes 7d/a2/c7 differ, exactly
  3B); r0 last3B 296322 differs;
  RQ==M HEAD-REMAP FIRST (M 10B vs RQ 6B: bytes
  1-5 identical 16/16, full-eq 0/16, b0 remap
  M->RQ 29->36 / a9->b6) -- new degree beyond
  the six known instances (P253 DISJOINT,
  P255/P263/P267 tails-only, P257/P259
  prefix+suffix, P261/P265 FULL-STRING);
  RT==M-tails FIRST (row-led tail tab echoes quad
  col tails: same-index 16/16 + set-eq, RTuniq 16
  Muniq 16; staged as independent table in code);
  RM UNPAIRED 16/16 by COL; RQ 15/16 (r14==r15
  366722f9e715; tails disambiguate 607a9f8b vs
  91f773c3);
  M-tails 16/16 ALL NEW vs P268T (overlap 0 vs
  P268 RM/RQ tail union; M-full also ALL NEW vs
  P268RQ);
  QT 4/4 ALL NEW vs P268QT
  (452ed3b4/b7e31656/dce31656/01e41656);
  RM ALL NEW vs P268RM; RT ALL NEW vs P268T
  (overlap 0).
  S0 NEW string (sig a4930300 NEW; P268S0 sig
  a4740300); S1 NEW string (sig 3d502907 NEW;
  P268S1 sig 1d188406).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 1f/5e (110351)
  tail 3d/5e (110366), b5set {5e}; C head 3f/5e
  (110367) tail 51/5e (110376), b5set {5e} NO
  carry; Q b5set {5e} NO step: head 53/5e
  (110377 off0) + triple 6f/5e (110391 off14)
  71/5e (110392 off15) 73/5e (110393 off16) +
  tail d1/5e (110440 off63).
  T head d3/5e (110441) + off22/23 (110463->
  110464) ff/5e->01/5f + off150/151 (110591->
  110592) ff/5f->01/60 + mid off143 f1/5f
  (110584) + off224 93/60 (110665) + tail
  off255 d1/60 (110696). All edge pins in
  for-list + PASS (batteries GREEN);
  110696 tail pinned + in for-list + PASS
  (direct first-hand: oracle sha 1387d003459518a5...
  matches PINS, py+C CLOSED T10P269R off=255
  agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (1b/5e, 1d/5e) match raw
  lencode.
  Matches A-653/A-333 geometry (mixed-size 92x84B+
  256x88B, PB0 a4930300 NEW + PB1 3d502907 NEW,
  PBA16-PLAIN VPOS 7 b5 const 5e NO pair,
  C10-1SIG VPOS 13 b5 const 5e 10/10 diverge
  NO T10-pair, QUAD1s VPOS 22 QM10 shared + R7
  r1==r2==r3 LAST3-PAIRED + tails 4/4 r123
  TRUE-3B 559c98 + M-tails ALL NEW 16/16,
  T88-ROWTAIL sig 07000000 TM7 by COL + TR6 by
  ROW 15/16 r14==r15 + ROW-led tails + b84-87
  const 1b2a6322, ring edges + thresholds
  23/151, NO D dips). Name note: memo/A-333 "TT"
  = code "RT" (same row-led tail tab by row).
- C diff pure-add: numstat 636/0 rgramc.c + 259/0
  rgram.py (+1/-1 for-line, +64/0 PINS); raw C 631
  content + 5 blank-only `+` lines / 0 del; raw py
  259 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 188, py del-uniq
  0 add-uniq 208). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 42e6be18..
  376bc6a9, 960 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 636/0, rgram.py 259/0,
  test_rgram.sh 1/1 (for-line), PINS 64/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1502->1508 +6, singletons
  `if n == ` 570->572 +2, range-guards `<= n <=`
  528->532 +4, CLOSED T10P prints 1502->1508 +6,
  seal 1596->1602
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 565->567 +2,
  range 528->532 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b375 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-653-q781
  memo CONFIRM 39/39 (section heads shape 13/13 +
  quad+T-ring 14/14 + counters 12/12 quoted
  verbatim; tier cut SAFE)
  + A-333-q333 viewer corroborates same tier (all 3
  legs CONFIRM, consts 77/71/62/69 INCL).
  No DISSENT on P269. Agrees with cport commit msg
  (py/C 15798, PYID 7899).
- Quiz: no conflicting CLAIM/GATE/FLAG on b377/
  376bc6a9. b376 EVEN = sweep2 turf (all evens are),
  used b376 tip as diff-base only, NOT gated. Newest
  PARENT-* is QNUM-16 (w2d Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r56/ (build377.log,
  pyid377.log, rgram377py/c.log, pass377py/c.txt,
  for376-old.nums/for377-new.nums,
  smoke377.log, tables377.log, tabaudit377.py,
  edges377.log, edges377.py, cdiff377.txt,
  pydiff377.txt, banddiff377.txt, added377.txt,
  build377/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
