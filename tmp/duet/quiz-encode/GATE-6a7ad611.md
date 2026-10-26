# GATE 6a7ad611 b479 T10P371 pins 145845..146192 (348 pins) PASS-functional

Seat sweep-r81, first-hand, WT tmp/wt-encode-sweep @6a7ad611,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r81.
Band = 26469ef3 (py merge w2b@17479fd4baede106fde1b334d65ad286da10270a, +6 tiers
+58 pins) + 6a7ad611 (C port). Base 09b93c5d (b478 tip,
2208 tiers sealed).

- Build: make -C src/c BUILDDIR=r81/build479 aae rgramc
  (absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 2
  mkdir/cc command echoes only), build479/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: bit-identical to r81 b477 build first-hand;
  band touches no aae sources), rgramc
  sha1 9086fb8d / sha256 ab91cec1 (new value: band
  touches C sources, recorded first-hand).
- RGRAMC-PYID 11032/11032 covered=11032/11032 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 22064/22064 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME;
  11032 pins x2 open+closed).
- RGRAM C 22064/22064 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (22064/22064, sorted, cmp-equal first-hand).
- PINS-RGRAM cells set-eq 11032/11032 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 22066 lines (2 hdr + 22064 rows, +58 vs base 22008).
  For-list union 11003->11032 +29/-0 (python sets,
  trailing-';' strip, never comm).
  29 = 2 sing (145845 145846; offs 0,1) +
  A 6 (head pair 145847 + 145848 + mid pair 145854 +
  145855 + tail pair 145861 + 145862; offs 0,1,7,8,
  14,15; offs 2-6,9-13 unsampled:
  145849-145853, 145856-145860; NO mid-single;
  b5 const 73 NO step NO edge, first-hand) +
  C 6 (head pair 145863 + 145864 + mid pair 145867 +
  145868 + tail pair 145871 + 145872; offs 0,1,4,5,
  8,9; offs 2,3,6,7 unsampled: 145865, 145866,
  145869, 145870; b5 const 73 NO step NO edge,
  first-hand) +
  Q 7 (head 145873 + row-boundary pair 145888/145889 +
  offs 15,16 + mid off31 single 145904 +
  B5EDGE pair 145919/145920 + offs 46,47 (b5 steps
  73->74 @off47) + tail 145936; offs 0,15,16,31,46,
  47,63; boundary @16 pair-covered, boundary @32
  single-sided (mate off32 145905 unsampled),
  B5EDGE @47 pair-covered; first-hand) +
  R 8 (head 145937 + edge pair 146047/146048 +
  offs 110,111 + mid off175 146112 + edge pair
  146175/146176 + offs 238,239 + mate off240
  146177 + tail 146192; offs 0,110,111,175,238,239,
  240,255; both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58
  = 22064-22006.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P371 C-vs-py, 12-table A-PBA88-PLAIN-
  M6b40/C10-1SIG-88-TAIL-M2/QUAD88-1SIG-QM6/R5-
  B5EDGE/T88-STANDARD-split-TM9/TR8 layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs ef17960c NEW-sig / 18000000 NEW-sig;
  S0 diff vs P370S0 29/84 @ 1,2,4-11,13,15-19,24,
  56-63,80-83 (sig b1,2 IN diff, b0,b3 same-sig NOT
  in diff, NOT byte-equal) +
  S1 diff vs P370S1 50/88 @ 0,4,5,9-11,16-43,60-71,
  84-87 (sig b0 IN diff, b1-3 same-sig NOT in diff,
  NOT byte-equal) +
  S1 diff vs own C10 cells [10x26] TRUE-UNIFORM
  all 10 (cell diff 26 @ 4,19,26,27,34-47,72-75,
  84-87; sig b0-3 same-sig NOT in diff, SIG-EQ own
  C10; 26/88 == census predicted EXACT;
  26th TRUE-uniform case: b477 25th -> this TRUE;
  sweep accounting owns the uniform count per
  viewer-vs-sweep convention) +
  S1 vs P370C10[0] 41/88 (P370C10 sig 19000000
  SIG-DIFFERS own S1; m-tab b20,84-87 mapping
  verified from P370C dispatch first-hand;
  S1 SIG-EQ own C10 18000000 both; S1 SIG-DIFFERS
  own PB0 + PBA sig));
  AM 16/16 (6B), CM 10/10 (2B M2), M 16/16 (6B
  QM6), QR 4/4 (5B R5), RM 16/16 (9B), RQ
  16/16 (8B) EXACT;
  AC 80/80, CC 84/84, QC 75/75, RC 69/69 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 80/84/75/69 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit479.py 455 PASS 0 FAIL;
  inventory = 12 rgram-tier tables + 1 pre-existing
  early-tier _T10P371C (P-head row n<=29614, in base
  at same line 7740 -- name collision, band did NOT
  introduce it; C side same split _T10P371C early /
  _T10P371CC rgram)).
  12 rgram tables = exactly the 12 (S0,S1,AM,AC,CM,
  CC,M,QR,QC,RM,RQ,RC);
  NO F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R5 carries b40,84-87 in-row, no const
  trailer); table inventory exactly the 12+1.
  Missing-sets first-hand EXACT: AC-8 [4,5,40,41,
  80,81,82,83] = b4,b5+PLAIN-M6 (b40,41,80-83;
  full sig b0-3 in AC = c9,01,00,00 ->
  c9010000 x16, b0 const c9);
  CC-4 [4,5,84,85] = b4,b5+M2 (b84,85;
  full sig b0-3 in CC = 18,00,00,00 -> 18000000
  x10 SAME-as-PB1-sig first-hand; b86 const a3 +
  b87 const ed quad-wide per CC table);
  QC-13 [4,5,39,40,47,80,81,82,83,84,85,86,87] =
  b4,b5+QM6 (b39,47,80-83)+R5 (b40,84-87;
  b0-3 const c9,01,00,00 -> c9010000 x64 1SIG
  SAME-sig-as-PBA);
  RC-19 [4,5,40,41,46,47,50,52,53,54,55,76,77,
  78,79,80,81,82,83] = b4,b5+TR8 (b40,41,46,47,
  76-79)+TM9 (b50,52,53,54,55,80-83).
  PLAIN-M6b40: m-tab b40,41,80-83, positions
  STAGED P363A per code comment (no FIRST
  claimed beyond code-stated); b5 CONST 73 NO
  step NO edge;
  TAIL-M2 shape filed (no FIRST claimed);
  QM6 shape + lanes FIRST this lane per code
  comment; R5 filed (4/4 UNPAIRED exact rows
  7fa0b0a3ed/80712873aa/80477654f7/80677654f7,
  full tuples pairwise unequal, distinct 4; R5 no
  FIRST claimed beyond code-stated);
  TM9 shape + lanes FIRST this lane per code
  comment; TR8 shape + lanes FIRST this lane per
  code comment.
  B5EDGE quad shape filed (R5-B5EDGE: b5 steps
  73->74 @off46/47 edge pair 145919->145920
  ff/73->01/74 pair-covered; R5 has no const
  trailer (in-row b40,84-87 only), so full-tail
  = rows first-hand).
  Code AC80/CC84/QC75/RC69 = census consts
  80/84/75/69 EXACT (+0 all four: PBA 88-7 with
  -1 b5-const, C10 88-3 with -1 b5-const, quad
  88-13, T88 88-19 per A-773; census script
  agrees first-hand).
  VPOS 7/3/13/19 derived first-hand (VPOS =
  varying-of-{b4,b5} + mtab + rtab: A 1+6+0
  (b4+M6, b5 const); C 1+2+0 (b4+M2, b5 const);
  Q 2+6+5 (b4,b5+QM6+R5); T 2+9+8
  (b4,b5+TM9+TR8)).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3710 n==145845 /
  P3711 n==145846 singleton-const (offs 0/1; 84B/88B;
  T97907/T97912 py-line mirrors);
  P371A 145847..145862 off=n-145847 PBA88-PLAIN-
  M6b40 (m-tab 6B b40,41,80-83, sig c9010000,
  b0 const c9, raw lencode b4=(0x6f+2off)&FF
  b5 const 73 NO step; T97917);
  P371C 145863..145872 off=n-145863 C10-1SIG-88-
  TAIL-M2 (m-tab 2B b84,85, full sig b0-3 in CC
  = 18000000, raw lencode b4=(0x8f+2off)&FF b5
  const 73 NO step; T97932);
  P371Q 145873..145936
  off=n-145873 m=off&15 q=off>>4 QUAD88-1SIG-
  QM6/R5-B5EDGE 1-sig c9010000 (b0-3 const
  c9,01,00,00 in QC = SAME-sig-as-PBA)
  (M 6B b39,47,80-83 QM6 16/16 distinct
  + R5 b40,84-87 rows 4/4 UNPAIRED exact;
  full-tail trailing 0/0/0/0/0/3 rest 0 (pair
  (2,3)=3 per lane trailing-lcs convention, cf
  P370Q six-pair form); TSHARE 0/0/0/1/1/3 +
  subseq 0/0/0/1/1/4 (pairs among rows 1-3 share
  head byte 0x80; NOT all-3 agree this tier --
  first R5 tier, no const trailer to dominate;
  stated, not glossed);
  raw lencode b4=(0xa3+2off)&FF b5=0x73+(off>=47)
  + 1 ff->01 B5EDGE (145919->145920); T97947);
  P371R(T88-ring) 145937..146192 off=n-145937
  c=off&15 r=off>>4 STANDARD-split sig c9180000
  (TM9 9B b50,52,53,54,55,80-83 by COL + TR8 8B
  b40,41,46,47,76-79 by ROW SPLIT tails UNPAIRED
  16/16, b0 const c9, b84-87 const 877654f7
  ring-wide; T97967);
  A paylen 88, C paylen 88, Q paylen 88, R paylen 88 +
  counter b4=(0x23+2*off)&FF b5=0x74+(off>=111)+
  (off>=239).
  C blocks carry T97907/T97912/T97917/T97932/
  T97947/T97967 py-line mirrors (exact: py guard
  lines verified at those numbers first-hand);
  guards `if ((n) == (145845))` / `if ((n) == (145846))`
  + 4 ranges `(145847)<=(n)<=(145862)` /
  `(145863)<=(n)<=(145872)` /
  `(145873)<=(n)<=(145936)` /
  `(145937)<=(n)<=(146192)` exact; ring
  counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 111/239 identical first-hand
  arithmetic, per-off values in values log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  A 16/16 + C 10/10 counter match 0 mismatches.
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (b84,85 M2 TAIL mid-body M);
  M 16/16 distinct (6B);
  QR 4/4 distinct UNPAIRED;
  QR full-tail shares: trailing 0/0/0/0/0/3,
  TSHARE 0/0/0/1/1/3, subseq 0/0/0/1/1/4
  (trailing matches lane "(2,3,3) rest 0";
  TSHARE/subseq pick up shared head 0x80 across
  rows 1-3; full tuples pairwise unequal,
  distinct 4);
  RQ==M DISJOINT-full + TAIL-IDENTITY (code M 6B
  lanes [39,47,80-83] vs RQ8 8B lanes [40,41,46,
  47,76-79]: widths differ 6B vs 8B, rows 0/16;
  shared lane b47 overlap 0/16 (M-uniq 15,
  RQ-uniq 6); TAIL-IDENTITY M-tail(b80-83)==
  RQ-tail(b76-79) ordered 16/16 + set-eq 16/16) --
  57th odd-band RQ==M instance (odds 56->57);
  P365-pattern (DISJOINT-full + TAIL-IDENTITY,
  cf GATE-6922336f + VERIFY-6922336f);
  lanewise heads differ, tails identical values;
  ordered per lesson (d);
  FULL-identity degree unchanged (b477 12th stands;
  this tier is not full-identity);
  AM-vs-RQ cross-check SKIPPED (widths differ 6B
  vs 8B, no same-width crosscheck applicable);
  width predictor dead, never cited;
  tails SPLIT (TM9 b50,52-55,80-83 by COL
  c=off&15, TR8 b40,41,46,47,76-79 by ROW
  r=off>>4, 16/16 distinct each, sequences
  UNPAIRED);
  M-tails (b80-83) 16/16 ALL NEW vs P370T
  col-led tails (ref: P370T 2SIG-COLSPLIT, b80-83
  COL-led via RM10; overlap 0) AND vs P370T
  row-led tails (overlap 0);
  RQ-tails (b76-79) 16/16 ALL NEW vs P370T
  row-led AND col-led tails (overlap 0 both);
  RM-tails (b80-83) 16/16 ALL NEW vs P370T
  col-led AND row-led tails (overlap 0 both);
  S0 29/84 NEW-sig (b1,2 IN diff, b0,b3 same) +
  S1 50/88 NEW-sig (b0 IN diff, b1-3 same-sig
  NOT in diff) +
  S1-vs-own-C10 26/88 UNIFORM +
  S1-vs-P370C10[0] 41/88 SIG-DIFFERS +
  S1 SIG-EQ own C10 (18000000 both) +
  S1 SIG-DIFFERS own PB0 (18 vs ef) and PBA sig
  (18 vs c9);
  P371 actuals (S0 ef17960c/S1 18000000/PBA88
  sig c9010000 x16 b0 const c9 + PB0-vs-P370PB0
  29/84 NEW-sig + PB1-vs-P370PB1 50/88 NEW-sig
  + S1-vs-own-C10 26/88 + SAMESIG-as-PB1 C10,
  PBA88-PLAIN-M6b40 VPOS 7 b5 const 73,
  C10-1SIG-88-TAIL-M2 VPOS 3 b4 varies b5 const
  73 + b86 const a3 + b87 const ed, QUAD88-1SIG-
  QM6/R5-B5EDGE VPOS 13 = b4,b5+QM6+R5 + R5 4/4
  UNPAIRED exact rows + trailing 0/0/0/0/0/3 +
  TSHARE/subseq head-share noted + NO const
  trailer + M-tails ALL NEW 16/16, T88-STANDARD-
  split-TM9/TR8 sig c9180000 TM9 by COL + TR8 by
  ROW UNPAIRED 16/16 + SPLIT tails + b84-87
  const 877654f7 ring-wide, ring edges +
  thresholds 111/239, B5EDGE @47 pair-covered,
  NO D dips) == w2b-r33 qTBD-p371 census
  predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 6f/73 (145847)
  tail 8d/73 (145862), b5set {115} (decimal =
  0x73) NO step NO edge;
  C head 8f/73 (145863) tail a1/73 (145872),
  b5set {115} (decimal = 0x73) NO edge;
  Q head a3/73 (145873) + off15/16 (145888->
  145889) c1/73->c3/73 + mid off31 e1/73
  (145904) + B5EDGE off46/47 (145919->145920)
  ff/73->01/74 + tail off63 21/74 (145936),
  b5set {115,116} (decimal = 0x73,0x74) 1 edge;
  T head 23/74 (145937) + off110/111 (146047->
  146048) ff/74->01/75 + mid off175 81/75
  (146112) + off238/239 (146175->146176)
  ff/75->01/76 + mate off240 03/76 (146177) +
  tail off255 21/76 (146192).
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 146192 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  d033bd0f8ccfcd0118307db9041a90be037de0f6
  65d9703631df4160b383e0e6 matches PINS rawlen
  104; PASS g-z146192 + g-z146192-closed in BOTH
  legs, sorted cmp-equal).
  Ring counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 111/239 identical first-hand
  arithmetic, per-off values in values log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  A 16/16 + C 10/10 counter match 0 mismatches;
  band 29/348 pins in for-list, all PASSx2 both
  legs; full-tier 348/348 CLOSED via writer bed
  (w2b-r33 qTBD-p371: 145845..146192 bounds-
  verified, 1x(100,84)+347x(104,88) framing =
  code dispatch 1+1+16+10+64+256 = 348 pins;
  N-start 145845 = 83553+(371-192)*348 arithmetic
  first-hand) + RGRAM py+C 22064/22064 GREEN +
  tail rav byte-identical to PINS sha first-hand.
- C diff pure-add: numstat 608/0 rgramc.c + 232/0
  rgram.py (+1/-1 for-line, +58/0 PINS); raw C 608
  = 603 content + 5 blank-only lines / 0 del;
  raw py 232 content / 0 del (bank route 232 this
  band, measured; C+py port/merge split clean:
  port commit C-only 608, merge commit py+sh+PINS);
  C legs touch ZERO PINS rows + ZERO for-line
  (add-only; sole del = old for-line churn, test_
  rgram.sh 1/1).
  Normalized ([0-9]+ -> N, diff-sign strip) del-uniq
  0 (0 true `-` lines in C+py diffs).
- Wall on band diff added lines (scope 09b93c5d..
  6a7ad611, 899 added lines: 894 content + 5 blank):
  vendor/disasm 0 hits, depload (dylib/CDLL/dlopen/
  ctypes/LoadLibrary/System.load) 0 hits,
  libcompression//usr/bin/aa 0 hits, shebang 0 hits,
  aea-invoke 0 hits (0 `aea' substrings, 0
  invocations). Files touched:
  rgramc.c 608/0, rgram.py 232/0, test_rgram.sh 1/1,
  PINS 58/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 2114->2120 +6, singletons
  `if n == ` 774->776 +2, range-guards
  `<= n <=` 936->940 +4, CLOSED T10P prints
  2114->2120 +6, seal 2208->2214
  +6 (cport msgs; offset +94 (base 2208-2114 and
  band 2214-2120 both +94 first-hand)).
  C guards: singleton `if ((n) == (` 769->771 +2,
  range `) <= (n)` 936->940 +4; 5-count C-vs-py
  singleton offset pre-existing (same C-only dip
  guards; offset 5 at base AND band, unchanged
  by band).
  C byte-index lists match py per block
  (A 6B, C 2B, Q 6B/5B, R 9B/8B SPLIT
  tails-split); insert position exact (P370R
  block precedes, P371R last block immediately
  precedes N-out-of-scope fallthrough; both sides).
  Temps _t7389.._t7404 appended
  (base max use _t7388, 16 contiguous, no reuse);
  _i band 4487,4489,4492,4495, _b band 4486,4488,
  4490,4491,4493,4494 (base max _i4485/_b4484,
  all band numbers absent from base, no reuse;
  generator-stride gaps unused anywhere:
  _i4486/4488/4490/4491/4493/4494 + _b4485/4487/
  4489/4492/4495 absent whole tree).
- CONFIRM evidence: NO rgram memo CONFIRM for P371
  on file at gate time (A-958-q1083 absent;
  filename survey first-hand; memo answers P370/
  P371 pending). Writer-bed evidence w2b-r33
  qTBD-p371 [8/8 CAP] read first-hand (P-head
  geometry census: PB0 NEW-sig 29/84, PB1 NEW-sig
  50/88, PBA c9 x16, C10 18 x10 SAME-as-PB1,
  QM6/R5 rows + tails, TM9/TR8 STANDARD frame,
  M-tails ALL NEW vs P370T RM, counters + edges,
  consts 80/84/75/69, VPOS 7/3/13/19 -- all agree
  with this GATE's numbers first-hand).
  Q-1083 UNANSWERED at gate time (no CONFIRM of
  either side on file; filename survey first-hand).
  Viewer: NO P371 geometry answer on file at gate
  time (filename survey first-hand; VERIFY-09b93c5d
  covers only the b478 base; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P371 (DISSENT files on file are
  T10P923/924/926 far-future, withdrawn Qs, checked
  not applicable); no FLAG names P371/b479/6a7ad611
  (filename + body-grep survey first-hand). Agrees
  with cport commit msg (py/C 22064, PYID 11032).
- Quiz: no conflicting CLAIM/GATE/FLAG on b479/
  6a7ad611 (quiz poll + filename grep first-hand;
  GATE-6a7ad611 absent before filing).
  Newest PARENT-* QNUM-38 (w2d Q-block grant, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r81/ (all *479* +
  builds, tail-146192 via ct-cache hit d033bd0f).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
