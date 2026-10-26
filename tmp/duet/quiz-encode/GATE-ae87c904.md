# GATE ae87c904 b487 T10P379 pins 148629..148976 (348 pins) PASS-functional

Seat sweep-r83, first-hand, fresh-tree git-archive to NVME
(band487/ + base486/ file-list-verified 117/117 MATCH both),
WT tmp/wt-encode-sweep untouched @246d3408 detached clean,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r83.
Band = 673eb8e3 (py merge w2b@67bdb25e03a234c060fb4a0d61f51874fc058ff8,
+6 tiers +58 pins) + ae87c904 (C port). Base e988dbb5 (b486 tip,
2256 tiers sealed).

- Build: make -C src/c BUILDDIR=r83/build487 aae rgramc
  (absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (2
  mkdir/cc command echoes only), build487/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: bit-identical r39-r83 builds first-hand;
  band touches no aae sources), rgramc
  sha1 c18159a3 / sha256 bde8ed4c (new value: band
  touches C sources, recorded first-hand).
- RGRAMC-PYID 11264/11264 covered=11264/11264 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 22528/22528 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME;
  11264 pins x2 open+closed).
- RGRAM C 22528/22528 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (22528/22528, sorted, cmp-equal first-hand).
- PINS-RGRAM cells set-eq 11264/11264 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 22530 lines (2 hdr + 22528 rows, +58 vs base 22472).
  For-list union 11235->11264 +29/-0 (python sets over
  PINS g-z names).
  29 = 2 sing (148629 148630; offs 0,1) +
  A 6 (head pair 148631 + 148632 + mid pair 148638/
  148639 + offs 7,8 + tail pair 148645 + 148646;
  offs 0,1,7,8,14,15; offs 2-6,9-13 unsampled:
  148633-148637, 148640-148644; NO mid-single;
  b5 const 89 NO step NO edge, first-hand) +
  C 6 (head pair 148647 + 148648 + mid pair 148651 +
  148652 + tail pair 148655 + 148656; offs 0,1,4,5,
  8,9; offs 2,3,6,7 unsampled: 148649, 148650,
  148653, 148654; b5 const 89 NO edge,
  first-hand) +
  Q 7 (head 148657 + boundary pairs (15,16)+(31,32):
  148672/148673 + 148688/148689 + mid off47
  (148704) + tail off63 (148720); offs 0,15,16,31,
  32,47,63; b5 const 89 NO edge anywhere, first-hand) +
  R 8 (head 148721 + edge pair 148735/148736 +
  offs 14,15 + mid off79 (148800) + edge pair
  148863/148864 + offs 142,143 + mate off144
  (148865) + tail off255 (148976); offs 0,14,15,
  79,142,143,144,255; both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58
  = 22528-22470.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend,
  workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P379 C-vs-py, 12-table A-PBA88-PLAIN-
  M6b40/C10-1SIG-88-TAIL-M4/QUAD88-1SIG-QM7/R4-NOEDGE/
  T88-ring-STANDARD-split-TM8/TR9 layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs 5d6af624 NEW-sig / 4f000000 NEW-sig;
  S0 diff vs P378S0 29/84 @ 0,1,2,4,5,6,7,9,10,13,
  14,15,17,18,19,20,21,56,57,58,59,60,61,62,63,76,
  77,78,79 (sig b0,1,2 IN diff, b3 same, NOT
  byte-equal) +
  S1 diff vs P378S1 49/88 @ 0,4,5,14,15,16,17,18,
  19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,
  35,36,37,38,39,40,41,42,43,60,61,62,63,64,65,66,
  67,80,81,82,83,84,85,86,87 (sig b0 IN diff, b1-3
  same-sig NOT in diff, NOT byte-equal) +
  S1 diff vs own C10 cells 25/25 TRUE-UNIFORM
  all 10 (cell diff 25; sig b0-3 SAME 4f000000 NOT
  in diff; 29th TRUE-uniform case; sweep accounting
  owns the uniform count per viewer-vs-sweep
  convention) +
  S1 vs P378C10[0] 40/88 SIG-DIFFERS (4f vs 49;
  m-tab b20,84-87 TAIL-M4, b0 const 49);
  AM 16/16 (6B), CM 10/10 (4B TAIL M4), M 16/16 (7B
  QM7), QR 4/4 (4B R4), RM 16/16 (8B TM8), RQ
  16/16 (9B TR9) EXACT;
  AC 80/80, CC 82/82, QC 75/75, RC 69/69 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 80/82/75/69 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit487.py 452 PASS 0 FAIL;
  inventory = exactly the 12 rgram tables, no
  pre-existing early-tier _T10P379C name collision
  this tier; no _T10P379C probe: inventory-verified;
  table + probe precedent: band29/81c73cb only).
  12 rgram tables = exactly the 12 (S0,S1,AM,AC,CM,
  CC,M,QR,QC,RM,RQ,RC);
  NO F/FT (no frags), no F0/F1, no BM/BC
  (C10/TAIL, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R4 full b84-87, NO trailer);
  table inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-8 [4,5,40,41,
  80,81,82,83] = b4,b5 + M6 (b40,41,80-83; b5
  const 89, b0 const 4d);
  CC-6 [4,5,84,85,86,87] = b4,b5+M4 (b84-87;
  full sig b0-3 in CC = 4f000000 x10
  SAME-as-PB1-sig, b0 const 4f, first-hand);
  QC-13 [4,5,30,39,47,80,81,82,83,84,85,86,87] =
  b4,b5+QM7 (b30,39,47,80-83)+R4 (b84-87;
  NO trailer consts; b0-3 const 4d,04,00,00 ->
  4d040000 x64 1SIG SAME-sig-as-PBA);
  RC-19 [4,5,40,41,42,46,47,52,53,54,55,76,77,
  78,79,80,81,82,83] = b4,b5+TR9 (b40,41,42,46,
  47,76-79)+TM8 (b52,53,54,55,80-83).
  PLAIN-M6b40: sig 4d040000 b0 const 4d, m-tab 6B
  b40,41,80-83 (AM rows 6B 16/16 distinct; b40 col
  16 distinct values, no sig-step claim beyond code
  comment), positions staged P363A/P371A per code
  comment (no FIRST claimed beyond code-stated);
  b5 CONST 89 NO step NO edge;
  1SIG-TAIL-M4: C10 1SIG (4f000000 x10 SAME-as-PB1-sig),
  m-tab b84,85,86,87 (CM rows 4B 10/10 diverge),
  positions staged P364C/P365C per code comment (no
  FIRST claimed beyond code-stated);
  b5 const 89 NO edge;
  QM7 shape + R4 filed (4/4 exact rows e9371c43/
  09381c43/a77da495/e67da495, full tuples unequal,
  distinct 4; NO frags, NO trailer (R4 fills
  b84-87); full-tail(b84-87) metrics suffix-lcs=
  TSHARE=subseq 2/0/0/0/0/3 AGREE; stated,
  not glossed; positions staged P363Q per code
  comment);
  TM8 shape 8B + TR9 shape 9B (positions staged
  P355R/P363R + P339R/P363R per code comments, no
  FIRST claimed beyond code-stated).
  Code AC80/CC82/QC75/RC69 = census consts
  80/82/75/69 EXACT (+0 all four: PBA 88-8 (6 mtab
  + b4,b5), C10 88-6 (4 mtab + b4,b5), quad 88-13
  (7 mtab+rtab + b4,b5), T88 88-19 (8 mtab+rtab
  + b4,b5) per A-962 census pattern; census script
  agrees first-hand).
  VPOS 7/5/13/19 derived first-hand (VPOS =
  varying-of-{b4,b5} + mtab + rtab: A 1+6+0
  (b4+M6, b5 const 89); C 1+4+0 (b4+M4, b5 const
  89); Q 2+7+4 (b4,b5+QM7+R4, NO edge); T
  2+8+9 (b4,b5+TM8+TR9)).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3790 n==148629 singleton-const
  (84B; T99758 py-line mirror);
  P3791 n==148630 singleton-const (fat, 88B;
  T99763 py-line mirror);
  P379A 148631..148646 off=n-148631 PBA88-PLAIN-
  M6b40 (m-tab 6B b40,41,80-83, sig 4d040000 b0
  const 4d, b5 const 89 NO step; T99768);
  P379C 148647..148656 off=n-148647 C10-1SIG-
  88-TAIL-M4 (m-tab 4B b84-87, full sig
  b0-3 in CC = 4f000000 SAME-as-PB1-sig, b0 const
  4f, b5 const 89 NO edge; T99783);
  P379Q 148657..148720 off=n-148657 m=off&15
  q=off>>4 QUAD88-1SIG-QM7/R4-NOEDGE 1-sig
  4d040000 SAME-sig-as-PBA (b0-3 const in QC)
  (M 7B b30,39,47,80-83 QM7 16/16 distinct
  + R 4B b84-87 R4 4/4 exact rows e9371c43/
  09381c43/a77da495/e67da495;
  full-tail suffix-lcs=TSHARE=subseq 2/0/0/0/0/3
  agree (NO frags, NO trailer);
  b5 const 89 NO edge; T99798);
  P379R(T88-ring) 148721..148976 off=n-148721
  c=off&15 r=off>>4 STANDARD-split sig 4d4e0000
  (TM8 8B b52,53,54,55,80-83 by COL + TR9 9B
  b40,41,42,46,47,76-79 by ROW STANDARD tails
  UNPAIRED 16/16, b0 const 4d, b84-87 const
  c9311baa ring-wide per memo + code consts;
  T99818);
  A paylen 88, C paylen 88, Q paylen 88, R paylen 88 +
  counter b4=(0x2f/0x4f/0x63/0xe3+2*off)&FF
  (A/Q/R per code comment; C base 0x4f derived from
  off0 raw first-hand, NOT from comments) b5 =
  89 / 89 / 89 /
  0x89+(off>=15)+(off>=143).
  C blocks carry T99758/T99763/T99768/T99783/
  T99798/T99818 py-line mirrors (exact: py guard
  lines verified at those numbers first-hand);
  guards `if ((n) == (148629))` / `if ((n) ==
  (148630))` + 4 ranges `(148631)<=(n)<=(148646)` /
  `(148647)<=(n)<=(148656)` /
  `(148657)<=(n)<=(148720)` /
  `(148721)<=(n)<=(148976)` exact; ring
  counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 15/143 identical first-hand
  arithmetic, per-off values in values log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  A 16/16 + C 10/10 counter match 0 mismatches.
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (b84-87 TAIL M4 1SIG mid-body M);
  M 16/16 distinct (7B);
  QR 4/4 distinct;
  QR(R4,b84-87) full-tail shares: suffix-lcs
  2/0/0/0/0/3, TSHARE 2/0/0/0/0/3, subseq-lcs
  2/0/0/0/0/3 (full tuples unequal, distinct 4;
  per py-comment pair-values (0,1,2),(0,2,0),
  (0,3,0),(1,2,0),(1,3,0),(2,3,3) mapped EXACT to
  suffix-lcs 2/0/0/0/0/3 first-hand);
  RQ==M absent this tier (code M 7B lanes [30,39,47,
  80-83] vs RQ 9B lanes [40,41,42,46,47,76-79]
  vs RM 8B lanes [52,53,54,55,80-83]: widths differ,
  no same-width M-vs-R crosscheck in code) --
  odd tally stays 60/14 (b485 60th/14th stand);
  AM-vs-RQ cross-check SKIPPED (widths differ 6B
  vs 9B, no same-width crosscheck applicable);
  width predictor dead, never cited;
  tails STANDARD (TM8 b52,53,54,55,80-83 by COL
  c=off&15, TR9 b40,41,42,46,47,76-79 by ROW
  r=off>>4, 16/16 distinct each, sequences
  UNPAIRED);
  M-tails (b80-83 of QM7) 16/16 ALL NEW vs P378T
  col-led AND row-led tails (overlap 0 both);
  RQ-tails (b76-79 of TR9) 16/16 ALL NEW vs P378T
  col-led AND row-led tails (overlap 0 both);
  RM-tails (b80-83 of TM8) 16/16 ALL NEW vs P378T
  row-led AND col-led tails (overlap 0 both);
  S0 29/84 NEW-sig (b0,1,2 IN diff, b3 same) +
  S1 49/88 NEW-sig (b0 IN diff, b1-3 same-sig
  NOT in diff) +
  S1-vs-own-C10 25/88 UNIFORM +
  S1-vs-P378C10[0] 40/88 SIG-DIFFERS +
  S1 SIG-SAME own C10 (4f vs 4f) +
  S1 SIG-DIFFERS P378C10 (4f vs 49) and PBA sig
  (4f vs 4d);
  P379 actuals (S0 5d6af624/S1 4f000000/PBA88-
  PLAIN-M6b40 VPOS 7 b5 const 89,
  C10-1SIG-88-TAIL-M4 VPOS 5 b4 varies b5 const +
  b84-87 lane, QUAD88-1SIG-QM7/R4-NOEDGE VPOS 13 =
  b4,b5+QM7+R4 + R4 4/4 exact rows +
  full-tail 2/0/0/0/0/3 agree + NO frags + M-tails
  ALL NEW 16/16,
  T88-ring-STANDARD-split-TM8/TR9 sig 4d4e0000
  TM8 by COL + TR9 by ROW UNPAIRED 16/16 +
  STANDARD tails + b84-87 const c9311baa ring-wide,
  ring edges + thresholds 15/143, NO Q edge,
  NO D dips) == w2b-r34 q1127-p379 census
  predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 2f/89 (148631)
  tail 4d/89 (148646), b5set {137} NO step NO edge;
  C head 4f/89 (148647) tail 61/89 (148656),
  b5set {137} NO edge;
  Q head 63/89 (148657) + boundary pairs off15/16
  (148672->148673) 81/89->83/89 + off31/32
  (148688->148689) a1/89->a3/89 + mid off47
  (148704) c1/89 + tail off63 (148720) e1/89,
  b5set {137} NO edge;
  T head e3/89 (148721) + off14/15 (148735->148736)
  ff/89->01/8a + mid off79 81/8a (148800) +
  off142/143 (148863->148864) ff/8a->01/8b + mate
  off144 03/8b (148865) + tail off255 (148976)
  e1/8b pair-covered (tail), b5set {137,138,139}
  2 edges.
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 148976 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  bd2f7f6a75e6446ad771abf0d0ca96efc7293491da6df7087853cb6476132d65
  matches PINS rawlen 104 row; PASS g-z148976 +
  g-z148976-closed in BOTH legs, sorted cmp-equal).
  band 29/348 pins in for-list, all PASSx2 both
  legs; full-tier 348/348 CLOSED via writer bed
  (w2b@67bdb25e q1127-p379: 148629..148976 bounds-
  verified, 1x(100,84)+347x(104,88) framing =
  code dispatch 1+1+16+10+64+256 = 348 pins;
  N-start 148629 = 83553+(379-192)*348 arithmetic
  first-hand) + RGRAM py+C 22528/22528 GREEN +
  tail rav byte-identical to PINS sha first-hand.
- C diff pure-add: numstat 608/0 rgramc.c + 232/0
  rgram.py (+1/-1 for-line, +58/0 PINS); raw C 608
  = 608 content / 0 del (NO blank-only lines this
  band); raw py 232 content / 0 del (bank route 232
  this band, measured; C+py port/merge split clean:
  port commit C-only 608, merge commit py+sh+PINS);
  C legs touch ZERO PINS rows + ZERO for-line
  (add-only; sole del = old for-line churn, test_
  rgram.sh 1/1);
  Normalized ([0-9]+ -> N, diff-sign strip) del-uniq
  0 (0 true `-` lines in C+py diffs; the single
  normalized `-` line in full scope = old for-line).
- Wall on band diff added lines (scope e988dbb5..
  ae87c904, 894 added lines, all content, 0 blank):
  vendor/disasm 0 hits, depload (dylib/CDLL/dlopen/
  ctypes/LoadLibrary/System.load) 0 hits,
  libcompression//usr/bin/aa 0 hits, shebang 0 hits,
  aea 2 `aea' substrings, BOTH inside PINS sha-256
  hex (e714...aea14f..., 3c25...aea5367...),
  0 invocations. Files touched:
  rgramc.c 608/0, rgram.py 232/0, test_rgram.sh 1/1,
  PINS 58/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 2162->2168 +6, singletons
  `if n == ` 790->792 +2, range-guards
  `<= n <=` 968->972 +4, CLOSED T10P prints
  2162->2168 +6 (py + C both), seal 2256->2262
  +6 (cport msgs; offset +94 (base 2256-2162 and
  band 2262-2168 both +94 first-hand)).
  C guards: singleton `if ((n) == (` 785->787 +2,
  range `) <= (n)` 968->972 +4; 5-count C-vs-py
  singleton offset pre-existing (same C-only dip
  guards; offset 5 at base AND band, unchanged
  by band).
  C byte-index lists match py per block
  (A 6B, C 4B TAIL, Q 7B/4B, R 8B/9B STANDARD
  tails-not-swapped); insert position exact
  (P378R block precedes, P379R last block
  immediately precedes N-out-of-scope fallthrough;
  both sides).
  Temps _t7517..7532 appended
  (base max use _t7516, 16 contiguous, no reuse);
  _i band 4567,4569,4572,4575, _b band 4566,4568,
  4570,4571,4573,4574 (base max _i4565/_b4564,
  all band numbers absent from base, no reuse;
  generator-stride gaps unused anywhere:
  _i4566/4568/4570/4571/4573/4574 + _b4567/4569/
  4572/4575 absent whole tree).
- CONFIRM evidence: rgram memo CONFIRM A-962-q1127-
  P379 (w2b-r34 [8/8 CAP]) read first-hand (P-head
  geometry census: PB0 NEW-sig 29/84, PB1 NEW-sig
  49/88 + 25/88 vs own C10, PBA sig x16 M[40,41,
  80-83] b4=(0x2f+2off), C10 4f x10 SAME-as-PB1,
  QM[30,39,47,80-83] shared x3 NO frags R rows
  exact, full-tail suffix-lcs 2/0/0/0/0/3, M-tails
  NEW vs P378T col-led, TM8/TR9 STANDARD frame,
  counters + edges, consts 80/82/75/69,
  VPOS 7/5/13/19 -- all agree with this GATE's
  numbers first-hand). Q-1127 ANSWERED at gate time
  (no unanswered Q on P379; filename survey
  first-hand).
  Viewer: NO P379 geometry answer on file at gate
  time (filename survey first-hand; viewer VERIFY
  lands post-gate per pipeline order).
  No DISSENT/FLAG on P379 (filename + body-grep
  for P379/b487/ae87c904/148629 across DISSENT* +
  FLAG* = 0 hits first-hand);
  no FLAG names pins 148629..148976.
  Agrees with cport commit msg (py/C 22528,
  PYID 11264).
- Quiz: no conflicting CLAIM/GATE/FLAG on b487/
  ae87c904 (quiz poll + filename grep first-hand:
  sweep2 CLAIM names no b487 turf (even-band seat;
  b486 base-use per pipeline); viewer CLAIM-r80
  FRONTIER b485-b487 is post-gate turf per pipeline
  order; GATE-ae87c904 absent before filing).
  Newest PARENT-* QNUM-46 (w2b Q-block grant, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r83/ (all *487* +
  builds, tail-148976 via ct-cache hit bd2f7f6a).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.

