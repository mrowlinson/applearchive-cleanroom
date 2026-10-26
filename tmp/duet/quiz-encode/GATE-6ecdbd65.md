# GATE 6ecdbd65 b373 T10P265 pins 108957..109304 (348 pins) PASS-functional

Seat sweep-r55, first-hand, WT tmp/wt-encode-sweep @6ecdbd65,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r55.
Band = a079ddf3 (py merge w2b@d55b9220 partial, +6 tiers
+62 pins) + 6ecdbd65 (C port). Base 7ad92845 (b372 tip,
1572 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build373/{aae,rgramc}, rc=0,
  0 warnings. aae sha1 7d8dd3a2 / sha256 d6e27c97
  (pinned stable continues: sha1 r39-r55, sha256 matches
  b354-b373 pinned value; band touches no aae sources),
  rgramc sha1 71d713b3 / sha256 cc2beda7.
- RGRAMC-PYID 7773/7773 covered=7773/7773 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 15546/15546 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 15546/15546 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (15546/15546, sorted).
- PINS-RGRAM cells set-eq 7773/7773 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 15548 rows (2 hdr + 15546, +62 vs base 15486).
  For-list union 7742->7773 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (108957 108958) +
  A 6 (head 108959 + 108960 + 108964 + 108969 + 108973
  + tail 108974; offs 0,1,5,10,14,15) +
  C 8 (head 108975 + 108978 + 108979 + 108980 + 108981
  + 108982 + 108983 + tail 108984; offs 0,3,4,5,6,7,8,9;
  offs 1,2 unsampled: 108976, 108977; all 6 sigs
  covered) +
  Q 8 (head 108985 + row-edge pair 109000/109001 +
  row-edge pair 109016/109017 + row-edge pair
  109032/109033 + tail 109048; offs 0,15/16,31/32,
  47/48,63; no carry, b5 const) +
  R 7 (head 109049 + b0split-04-side 109052 + edge pair
  109055/109056 + edge pair 109183/109184 + tail 109304;
  offs 0,3,6/7,134/135,255; no mid).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 31x2 = 62 = 15546-15484.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var).
- Tables audit P265 C-vs-py, 13-table A-PBA-PLAIN/
  C10-6SIG/QUAD-NOFRAG+T88-SPLITb0 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs a0560300 NEW / bdcfaa06 ==P264PB1, both NEW
  strings);
  AM 16/16 (6B), CM 10/10 (13B), M 16/16 (6B),
  QR 4/4 (8B), QT 4/4 (4B), RM 16/16 (8B), RQ 16/16
  (6B) EXACT;
  AC 76/76, CC 69/69, QC 64/64, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/69/64/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit373.py 107 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (no b19 frag),
  no QB/PT/FM/M42/X42; table inventory exactly the 13.
  Missing-sets first-hand EXACT: AC-8 [4,5,48,49,76,
  77,78,79] = b4,b5+M6 (b48,49,76-79);
  CC-15 [2,3,4,5,35,46,47,48,49,50,51,80,81,82,83]
  = b4,b5+M13 (b2,3,35,46-51,80-83, sig b2,b3
  in tab);
  QC-20 [3,4,5,6,7,35,46,47,48,49,50,51,76,77,78,
  79,80,81,82,83] = b4,b5+QM6 (b6,7,76-79)+R8
  (b3,35,46-51)+T4 (b80-83);
  RC-17 [0,4,5,6,7,9,10,11,20,76,77,78,79,80,81,
  82,83] = b0split+b4,b5+TM8 (b9-11,20,80-83)+
  TR6 (b6,7,76-79).
  6SIG map first-hand: CM full-sig bdcfaa06 x4 (offs
  0-3) + bdcf7a06 + bdcffa04 + bdcf1a05 + bdcf3a05 +
  bdcf7a05 x2 (offs 8-9); CC b0,b1 const bd,cf.
  Code AC76/CC69/QC64/RC71; incl = +1/+1/+1/+0
  (A/C/Q b5 const 53, T counter) = 77/70/65/71;
  lane consts = A-637/A-329 INCL EXACT (writer
  PBA/C10/quad = memo-1; T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2650 n==108957 / P2651
  n==108958 singleton-const (offs 0/1);
  P265A 108959..108974 off=n-108959 PBA-PLAIN
  (m-tab 6B b48,49,76-79, sig e0932f72 b0 const e0,
  b5 const 53);
  P265C 108975..108984 off=n-108975 C10-6SIG
  (m-tab 13B b2,3,35,46-51,80-83, b5 const 53
  NO carry);
  P265Q 108985..109048 off=n-108985 m=off&15
  q=off>>4 QUADms 3-sig row-led (dffbac59 x16 /
  dffbac5c x32 / dffbac57 x16 NEW; M 6B b6,7,76-79
  + R8 b3,35,46-51 r1==r2 MID-PAIRED + QT b80-83
  no shared suffix, NO frags, b5 const 53);
  P265R(T88-SPLIT-b0) 109049..109304 off=n-109049
  c=off&15 r=off>>4 FIRST split ring (b0 = 05 iff
  c<3 else 04, 48x05+208x04; b1-3 const 000000;
  TM 8B b9-11,20,80-83 by COL + TR 6B b6,7,76-79
  by ROW SPLIT tails UNPAIRED, b84-87 const
  20/32/be/d2);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8; R paylen 88
  + counter b4=(0xf3+2off)&FF b5=0x53+(off>=7)+
  (off>=135).
  C blocks carry T72668/72673/72678/72693/72709/
  72732 py-line mirrors (exact); guards
  `if ((n) == (108957))` / `if ((n) == (108958))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; b0split via ternary (((c) < (3)) ? (5) : (4))
  (matches py); counter 243+2*off + 83+(off>=7)+
  (off>=135);
  temps _t5604.._t5621 appended (base max _t5603,
  no reuse); _i max 3399->3410 (band 3401,3403,
  3407,3410), _b max 3398->3409 (band 3400,3402,
  3404,3405,3406,3408,3409), no reuse; C byte-index
  lists match py per block (A 6B, C 13B, Q 6/8/4B,
  R 8/6B); insert position exact (dispatch tail, N
  out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (6SIG rows, all distinct);
  M 16/16 distinct (heads 16-unique, tails
  16-unique);
  QR r1==r2 MID-PAIRED exact (5c52a392917ed792 x2;
  r0 59d2ffd8b1a56722 + r3 5792ce9eb1805f9a
  distinct); 3 distinct;
  QT 4/4 distinct exact (473b6a01/c2fac80f/
  756b3610/652f4ee8); max pairwise common suffix
  0 hex chars (last bytes 01/0f/10/e8 all differ)
  -- no shared suffix;
  RQ==M FULL-STRING 16/16 same-index+set-eq (6B
  identical in order; heads 16/16 + tails 16/16
  same-index) -- second FULL instance after P261
  (P253 DISJOINT, P255/P263 tails-only, P257/P259
  prefix+suffix);
  tails SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P264T (overlap 0 vs
  P264 RM/RQ tail union; M-full also ALL NEW vs
  P264RQ);
  QT 4/4 NEW vs P264QT
  (c37be99d/c0fadb1d/e5fadb1d/cb6a97b8);
  RM ALL NEW vs P264RM.
  S0 NEW string (sig a0560300 NEW; P264S0 sig
  a2560300); S1 NEW string (sig bdcfaa06 ==
  P264S1 sig repeat-forward).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 3f/53 (108959)
  tail 5d/53 (108974), b5set {53}; C head 5f/53
  (108975) tail 71/53 (108984), b5set {53} NO
  carry; Q head 73/53 (108985) tail f1/53
  (109048), b5set {53} NO carry.
  T head f3/53 (109049) + off6/7 (109055->
  109056) ff/53->01/54 + off134/135 (109183->
  109184) ff/54->01/55 + mid off127 f1/54
  (109176) + tail off255 f1/55 (109304). All
  edge pins in for-list + PASS (batteries GREEN);
  109304 tail pinned + in for-list + PASS
  (direct first-hand: oracle sha 393ae26963053f3e...
  matches PINS, py+C CLOSED T10P265R off=255
  agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand; b0split counts
  48x05+208x04 first-hand.
  S0/S1 embedded b4/b5 (3b/53, 3d/53) match raw
  lencode.
  Matches A-637/A-329 geometry (mixed-size 92x84B+
  256x88B, PB0 a0560300 NEW + PB1 bdcfaa06
  ==P264PB1, PBA16-PLAIN VPOS 7 b5 const 53 NO
  pair, C10-6SIG VPOS 14 b5 const 53 10/10 diverge
  NO T10-pair, QUADms 3-sig VPOS 19 QM6 shared +
  R8 r1==r2 MID-PAIRED + tails 4/4 no shared suffix
  + NO frags + M-tails ALL NEW 16/16, T88-SPLIT-b0
  FIRST VPOS 17 TM8 by COL + TR6 by ROW UNPAIRED
  16/16 + SPLIT tails + b84-87 const 2032bed2,
  ring edges + thresholds 7/135, NO D dips).
- C diff pure-add: numstat 612/0 rgramc.c + 239/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 607
  content + 5 blank-only `+` lines / 0 del; raw py
  239 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 156, py del-uniq
  0 add-uniq 177). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 7ad92845..
  6ecdbd65, 914 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 612/0, rgram.py 239/0,
  test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1478->1484 +6, singletons
  `if n == ` 562->564 +2, range-guards `<= n <=`
  512->516 +4, CLOSED T10P prints 1478->1484 +6,
  seal 1572->1578
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 557->559 +2,
  range 512->516 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357/b359/b361/b363/b365/b367/b369/b371),
  unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-637-q777
  memo CONFIRM 37/37 (section heads shape 12/12 +
  quad+Tring 13/13 + counters 12/12 quoted verbatim;
  tier cut SAFE)
  + A-329-q329 viewer corroborates same tier (3/3
  legs CONFIRM, consts 77/70/65/71 INCL).
  No DISSENT on P265. Agrees with cport commit msg
  (py/C 15546, PYID 7773).
- Quiz: no conflicting CLAIM/GATE/FLAG on b373/
  6ecdbd65. b372/b374 EVEN = sweep2 turf, used b372
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r55/ (build373.log,
  pyid373.log, rgram373py/c.log, pass373py/c.txt,
  pins372base.csv, for372-old.nums/for373-new.nums,
  smoke373.log, tables373.log, tabaudit373.py,
  edges373.log, edges373.py, cdiff373.txt,
  pydiff373.txt, banddiff373.txt, added373.txt,
  build373/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
