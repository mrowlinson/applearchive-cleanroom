# GATE e59e5d25 b375 T10P267 pins 109653..110000 (348 pins) PASS-functional

Seat sweep-r55, first-hand, WT tmp/wt-encode-sweep @e59e5d25,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r55.
Band = 444de119 (py merge w2b@aa2a6a60 partial, +6 tiers
+62 pins) + e59e5d25 (C port). Base 26cd06b5 (b374 tip,
1584 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build375/{aae,rgramc}, rc=0,
  0 warnings. aae sha1 7d8dd3a2 / sha256 d6e27c97
  (pinned stable continues: sha1 r39-r55, sha256 matches
  b354-b375 pinned value; band touches no aae sources),
  rgramc sha1 1ea26863 / sha256 cc943172.
- RGRAMC-PYID 7835/7835 covered=7835/7835 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 15670/15670 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 15670/15670 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (15670/15670, sorted).
- PINS-RGRAM cells set-eq 7835/7835 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 15672 rows (2 hdr + 15670, +62 vs base 15610).
  For-list union 7804->7835 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (109653 109654) +
  A 6 (head 109655 + 109656 + 109660 + 109665 + 109669
  + tail 109670; offs 0,1,5,10,14,15) +
  C 6 (head 109671 + 109672 + 109674 + 109677 + 109679
  + tail 109680; offs 0,1,3,6,8,9; offs 2,4,5,7
  unsampled: 109673, 109675, 109676, 109678) +
  Q 10 (head 109681 + row0-mid 109688 + step triple
  109695/109696/109697 + row-edge pair 109712/109713 +
  row-edge pair 109728/109729 + tail 109744; offs 0,7,
  14/15/16,31/32,47/48,63; b5 step off>=15) +
  R 7 (head 109745 + edge pair 109823/109824 + mid
  109888 + edge pair 109951/109952 + tail 110000;
  offs 0,78/79,143,206/207,255).
  PINS adds = same 31 tier pins. Each for-N yields 2 PASS
  lines (g-zN-closed + g-zN); 31x2 = 62 = 15670-15608.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var).
- Tables audit P267 C-vs-py, 15-table A-PBA-PLAIN/
  C10-1SIG/QUAD1s-b42+T88 layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs a0740300 ==P266PB0 REPEAT / 1d18e406 NEW, both
  NEW strings);
  AM 16/16 (6B), CM 10/10 (11B), M 16/16 (7B),
  M42 16/16 (1B), X42 4/4 (1B), QR 4/4 (6B),
  QT 4/4 (4B), RM 16/16 (8B), RQ 16/16 (8B) EXACT;
  AC 76/76, CC 71/71, QC 64/64, RC 70/70 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 76/71/64/70 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit375.py 112 PASS 0 FAIL).
  No BM/BC (C10, not B10), no M19/XA19 (b42, not b19),
  no QB/PT/FM; table inventory exactly the 15.
  Missing-sets first-hand EXACT: AC-8 [4,5,36,37,76,
  77,78,79] = b4,b5+M6 (b36,37,76-79);
  CC-13 [4,5,36,37,38,39,40,41,42,80,81,82,83]
  = b4,b5+M11 (b36-42,80-83, full sig const);
  QC-20 [4,5,34,35,36,37,38,39,40,41,42,43,76,
  77,78,79,80,81,82,83] = b4,b5+QM7
  (b34,35,43,76-79)+b42+R6 (b36-41)+T4 (b80-83);
  RC-18 [4,5,38,39,46,47,52,53,54,55,76,77,78,
  79,80,81,82,83] = b4,b5+TM8 (b52-55,80-83)+
  TR8 (b38,39,46,47,76-79).
  1SIG first-hand: CC b0-3 const 1d18e406 (full sig
  const, ==PB1/S1 sig); CM 10/10 diverge.
  Code AC76/CC71/QC64/RC70; incl = +1/+1/+0/+0
  (A/C b5 const 58, Q b5-step, T counter) =
  77/72/64/70;
  lane consts = A-644/A-331 INCL EXACT (writer
  PBA/C10 = memo-1; quad/T88 identical).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P2670 n==109653 / P2671
  n==109654 singleton-const (offs 0/1);
  P267A 109655..109670 off=n-109655 PBA-PLAIN
  (m-tab 6B b36,37,76-79, sig c0822772 b0 const c0,
  b5 const 58);
  P267C 109671..109680 off=n-109671 C10-1SIG
  (m-tab 11B b36-42,80-83, b5 const 58
  NO carry);
  P267Q 109681..109744 off=n-109681 m=off&15
  q=off>>4 QUAD1s single-sig c0822772 (M 7B
  b34,35,43,76-79 + b42 row-XOR X=[00,0f,0f,0f]
  staged, ADD tie A=[0,3,3,3] also fits flagged +
  R6 b36-41 r1==r2==r3 LAST3-PAIRED first + QT
  b80-83 r1/r2/r3 TRUE-3B, b5 step off>=15);
  P267R(T88-ring) 109745..110000 off=n-109745
  c=off&15 r=off>>4 STANDARD sig 06000000 (TM 8B
  b52-55,80-83 by COL + TR 8B b38,39,46,47,76-79
  by ROW SPLIT tails UNPAIRED, b84-87 const
  de/93/ee/f2);
  A/C/Q paylen 84 + raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8 (Q b5-step
  emerges from raw lencode); R paylen 88
  + counter b4=(0x63+2off)&FF b5=0x59+(off>=79)+
  (off>=207).
  C blocks carry T73166/73171/73176/73191/73207/
  73232 py-line mirrors (exact); guards
  `if ((n) == (109653))` / `if ((n) == (109654))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; b42xor via snprintf %02lx of (pay[42]^
  hexval(X42[q])) vs M42[m] (matches py XOR
  staging); counter 99+2*off + 89+(off>=79)+
  (off>=207);
  temps _t5640.._t5659 appended (base max _t5639,
  no reuse); _i max 3421->3432 (band 3423,3425,
  3429,3432), _b max 3420->3431 (band 3422,3424,
  3426,3427,3428,3430,3431), no reuse; C byte-index
  lists match py per block (A 6B, C 11B, Q 7/1/6/4B,
  R 8/8B); insert position exact (dispatch tail, N
  out-of-scope follows).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (1SIG rows, all distinct);
  M 16/16 distinct;
  M42 values exact (66/e6/66/e6/66/66/66/e6/66/
  66/26/e6/66/e6/66/26, 3 distinct);
  X42 [00,0f,0f,0f] EXACT;
  b42 tie first-hand: code stages XOR (formula +
  X42 values match memo X=[00,0f,0f,0f]); ADD tie
  A=[0,3,3,3] flagged in Q-block comment both
  sides; memo A-644 + viewer A-331 both
  first-hand confirm XOR/ADD 64/64 TIE; staging
  follows X42-family precedent (P243/P251 shape,
  P211-P259);
  QR r1==r2==r3 LAST3-PAIRED exact (bfdd8c6dd153
  x3; r0 24dfb205518e distinct); 2 distinct;
  FIRST last-three-paired quad;
  QT 4/4 distinct exact (9e2c5289/71bf4a51/
  96bf4a51/bbbf4a51); r1/r2/r3 share TRUE 3B
  bf4a51 (first bytes 71/96/bb differ, exactly
  3B); r0 last3B 2c5289 differs;
  RQ==M tails-only family (b76-79 same-index 16/16
  + set-eq; M 7B vs RQ 8B widths differ) --
  third tails-only instance after P255/P263
  (P253 DISJOINT, P257/P259 prefix+suffix, P261/
  P265 FULL);
  tails SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P266T (overlap 0 vs
  P266 RM/RQ tail union; M-full also ALL NEW vs
  P266RQ);
  QT 4/4 NEW vs P266QT
  (b3327d33/ceb7d61f/f3b7d61f/23337d33);
  RM ALL NEW vs P266RM.
  S0 NEW string (sig a0740300 ==P266S0 sig
  repeat-forward; P266S1 sig 2a40e906); S1 NEW
  string (sig 1d18e406 NEW == C10 head-sig).
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head af/58 (109655)
  tail cd/58 (109670), b5set {58}; C head cf/58
  (109671) tail e1/58 (109680), b5set {58} NO
  carry; Q head e3/58 (109681) step off14/15
  (109695->109696) ff/58->01/59 + off16 03/59
  (109697) + tail 61/59 (109744); quad formula
  ==raw-lencode 64/64 mismatches 0.
  T head 63/59 (109745) + off78/79 (109823->
  109824) ff/59->01/5a + off206/207 (109951->
  109952) ff/5a->01/5b + mid off143 81/5a
  (109888) + tail off255 61/5b (110000). All
  edge pins in for-list + PASS (batteries GREEN);
  110000 tail pinned + in for-list + PASS
  (direct first-hand: oracle sha c740e727a2eeba6c...
  matches PINS, py+C CLOSED T10P267R off=255
  agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand.
  S0/S1 embedded b4/b5 (ab/58, ad/58) match raw
  lencode.
  Matches A-644/A-331 geometry (mixed-size 92x84B+
  256x88B, PB0 a0740300 ==P266PB0 + PB1 1d18e406
  NEW, PBA16-PLAIN VPOS 7 b5 const 58 NO pair,
  C10-1SIG VPOS 12 b5 const 58 10/10 diverge
  NO T10-pair, QUAD1s VPOS 20 QM7 shared +
  b42 XOR/ADD 64/64 tie staged XOR + R6
  r1==r2==r3 LAST3-PAIRED first + tails 4/4
  r123 TRUE-3B + M-tails ALL NEW 16/16, T88-ring
  STANDARD sig 06000000 TM8 by COL + TR8 by ROW
  UNPAIRED 16/16 + SPLIT tails + b84-87 const
  de93eef2, quad step + ring edges + thresholds
  79/207, NO D dips).
- C diff pure-add: numstat 640/0 rgramc.c + 260/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 635
  content + 5 blank-only `+` lines / 0 del; raw py
  260 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 169, py del-uniq
  0 add-uniq 187). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 26cd06b5..
  e59e5d25, 963 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa/shim 0 hits, shebang 0 hits. Files
  touched: rgramc.c 640/0, rgram.py 260/0,
  test_rgram.sh 1/1 (for-line), PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1490->1496 +6, singletons
  `if n == ` 566->568 +2, range-guards `<= n <=`
  520->524 +4, CLOSED T10P prints 1490->1496 +6,
  seal 1584->1590
  +6: all agree (stated literal methods, first-hand).
  C guards: singleton `if ((n) == (` 561->563 +2,
  range 520->524 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357/b359/b361/b363/b365/b367/b369/b371/b373),
  unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-644-q779
  memo CONFIRM 39/39 (section heads shape 13/13 +
  quad+Tring 12/12 + counters 14/14 quoted verbatim;
  tier cut SAFE)
  + A-331-q331 viewer corroborates same tier (3/3
  legs CONFIRM, consts 77/72/64/70 INCL).
  No DISSENT on P267. Agrees with cport commit msg
  (py/C 15670, PYID 7835).
- Quiz: no conflicting CLAIM/GATE/FLAG on b375/
  e59e5d25. b374 EVEN = sweep2 turf (all evens are),
  used b374 tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r55/ (build375.log,
  pyid375.log, rgram375py/c.log, pass375py/c.txt,
  pins374base.csv, for374-old.nums/for375-new.nums,
  smoke375.log, tables375.log, tabaudit375.py,
  edges375.log, edges375.py, cdiff375.txt,
  pydiff375.txt, banddiff375.txt, added375.txt,
  build375/ binaries).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
