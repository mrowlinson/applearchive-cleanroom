# GATE e9c52e90 b477 T10P369 pins 145149..145496 (348 pins) PASS-functional

Seat sweep-r81, first-hand, WT tmp/wt-encode-sweep @e9c52e90,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r81.
Band = 9367008d (py merge w2b@e5a89b491924214343c83705269984fb8edc521a, +6 tiers
+58 pins) + e9c52e90 (C port). Base 0c29b70b (b476 tip,
2196 tiers sealed).

- Build: make -C src/c BUILDDIR=r81/build477 aae rgramc
  (absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 2
  mkdir/cc command echoes only), build477/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: prefixes match r39-r80 seatings first-hand;
  band touches no aae sources), rgramc
  sha1 0039e844 / sha256 968a39a6 (new value: band
  touches C sources, recorded first-hand).
- RGRAMC-PYID 10974/10974 covered=10974/10974 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 21948/21948 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME;
  10974 pins x2 open+closed).
- RGRAM C 21948/21948 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (21948/21948, sorted, cmp-equal first-hand).
- PINS-RGRAM cells set-eq 10974/10974 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 21950 lines (2 hdr + 21948 rows, +58 vs base 21892).
  For-list union 10945->10974 +29/-0 (python sets,
  trailing-';' strip, never comm).
  29 = 2 sing (145149 145150; offs 0,1) +
  A 6 (head pair 145151 + 145152 + mid pair 145158 +
  145159 + tail pair 145165 + 145166; offs 0,1,7,8,
  14,15; offs 2-6,9-13 unsampled:
  145153-145157, 145160-145164; NO mid-single;
  A b5 STEP 6d->6e @off0/1 edge pair-covered,
  first-hand) +
  C 6 (head pair 145167 + 145168 + mid pair 145171 +
  145172 + tail pair 145175 + 145176; offs 0,1,4,5,
  8,9; off 2,3,6,7 unsampled: 145169, 145170,
  145173, 145174; b5 const 6e NO edge, first-hand) +
  Q 7 (head 145177 + row-boundary pair 145192/145193 +
  offs 15,16 + row-boundary pair 145208/145209 +
  offs 31,32 + boundary-single off48 145225 +
  tail 145240; offs 0,15,16,31,32,48,63; row
  boundaries (16,32) pair-covered, third boundary
  off48 single-sided (mate off47 unsampled);
  b5 const 6e NO edge, first-hand) +
  R 8 (head 145241 + edge pair 145279/145280 +
  offs 38,39 + mid off103 145344 + edge pair
  145407/145408 + offs 166,167 + mate off168
  145409 + tail 145496; offs 0,38,39,103,166,167,
  168,255; both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58
  = 21948-21890.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P369 C-vs-py, 12-table A-PBA88-STEP-
  M8b52/C10-1SIG-88-TAIL-M4/QUAD88-1SIG-QM7/R4-
  NOEDGE/T88-STANDARD-split-TM7/TR7 layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs ef928b0e NEW-sig / 1e000000 NEW-sig;
  S0 diff vs P368S0 33/84 @ 0-2,4,5,11,19-31,36,
  37,60-71 (sig b0-2 IN diff, b3 same-sig NOT in
  diff, NOT byte-equal) +
  S1 diff vs P368S1 56/88 @ 0,4,5,19,26-44,46-54,
  56-75,84-87 (sig b0 IN diff, b1-3 same-sig NOT
  in diff, NOT byte-equal) +
  S1 diff vs own C10 cells [10x40] TRUE-UNIFORM
  all 10 (cell diff 40 @ 4,5,19,38,39,45,46,48-50,
  53-75,77-79,84-87; sig b0-3 same-sig NOT in diff,
  SIG-EQ own C10; 40/88 == census predicted EXACT;
  25th TRUE-uniform case: b475 24th -> this TRUE;
  sweep accounting owns the uniform count per
  viewer-vs-sweep convention) +
  S1 vs P368C10[0] 50/88 (P368C10 sig 1f000000
  SIG-DIFFERS own S1; S1 SIG-EQ own C10 1e000000
  both; S1 SIG-DIFFERS own PB0 + PBA sig));
  AM 16/16 (8B), CM 10/10 (4B M4), M 16/16 (7B
  QM7), QR 4/4 (4B R4), RM 16/16 (7B), RQ
  16/16 (7B) EXACT;
  AC 78/78, CC 82/82, QC 75/75, RC 72/72 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 78/82/75/72 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit477.py 452 PASS 0 FAIL).
  12 py symbols = exactly the 12 tables;
  NO F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R4 carries b84-87 in-row, no const
  trailer); table inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-10 [4,5,52,53,
  54,55,80,81,82,83] = b4,b5+STEP-M8 (b52-55,
  80-83; full sig b0-3 in AC = e5,01,00,00 ->
  e5010000 x16, b0 const e5);
  CC-6 [4,5,84,85,86,87] = b4,b5+M4 (b84-87;
  full sig b0-3 in CC = 1e,00,00,00 -> 1e000000
  x10 SAME-as-PB1-sig first-hand);
  QC-13 [4,5,6,7,8,80,81,82,83,84,85,86,87] =
  b4,b5+QM7 (b6,7,8,80-83)+R4 (b84-87;
  b0-3 const ef,01,00,00 -> ef010000 x64 1SIG
  DIFFERS-from-PBA-sig);
  RC-16 [4,5,6,7,8,13,14,15,76,77,78,79,
  80,81,82,83] = b4,b5+TR7 (b6,7,8,76-79)+TM7
  (b13,14,15,80-83).
  STEP-M8b52: m-tab b52-55,80-83, positions
  STAGED P353A/P361A per code comment (no FIRST
  claimed beyond code-stated); b5 STEPS 6d->6e
  @off0/1 edge pair-covered (145151->145152);
  TAIL-M4 shape filed (no FIRST claimed);
  QM7 shape filed (staged P321Q per comment; no
  FIRST claimed); R4 filed (4/4 UNPAIRED exact
  rows 8e9e54d5/ae9e54d5/234c14d7/434c14d7,
  full tuples pairwise unequal, distinct 4);
  TM7 shape filed (staged P313R per comment);
  TR7 shape + lanes FIRST this lane per code
  comment; no FIRST claimed beyond code-stated.
  NO B5EDGE this tier (A b5 step is lencode @off0/1
  pair-covered, not quad-edge; Q b5 const 6e NO
  edge; R b5 steps are ring-counter thresholds
  39/167 pair-covered).
  Code AC78/CC82/QC75/RC72 = census consts
  78/82/75/72 EXACT (+0 all four: PBA 88-10, C10
  88-6 with -1 b5-const, quad 88-13 with -1
  b5-const, T88 88-16 per A-773; census script
  agrees first-hand).
  VPOS 10/5/12/16 derived first-hand (VPOS =
  varying-of-{b4,b5} + mtab + rtab: A 2+8+0
  (b4,b5-step+STEP-M8); C 1+4+0 (b4+M4, b5 const);
  Q 1+7+4 (b4+QM7+R4, b5 const); T 2+7+7
  (b4,b5+TM7+TR7)).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3690 n==145149 /
  P3691 n==145150 singleton-const (offs 0/1; 84B/88B;
  T97443/T97448 py-line mirrors);
  P369A 145151..145166 off=n-145151 PBA88-STEP-
  M8b52 (m-tab 8B b52-55,80-83, sig e5010000,
  b0 const e5, raw lencode b4=(0xff+2off)&FF
  b5=0x6d+(off>=1); T97453);
  P369C 145167..145176 off=n-145167 C10-1SIG-88-
  TAIL-M4 (m-tab 4B b84-87, full sig b0-3 in CC
  = 1e000000, raw lencode b4=(0x1f+2off)&FF b5
  const 6e NO step; T97468);
  P369Q 145177..145240
  off=n-145177 m=off&15 q=off>>4 QUAD88-1SIG-
  QM7/R4-NOEDGE 1-sig ef010000 (b0-3 const
  ef,01,00,00 in QC = DIFFERS-from-PBA-sig)
  (M 7B b6,7,8,80-83 QM7 shared 16/16 distinct
  + R4 b84-87 rows 4/4 UNPAIRED exact;
  full-tail pairs trailing=TSHARE=subseq 3/0/0/
  0/0/3, all-3 agree: pairs (0,1),(2,3) share
  trailing 3, rest 0, no const trailer;
  raw lencode b4=(0x33+2off)&FF b5 const 6e
  NO edge; T97483);
  P369R(T88-ring) 145241..145496 off=n-145241
  c=off&15 r=off>>4 STANDARD-split sig ff1e0000
  (TM7 7B b13,14,15,80-83 by COL + TR7 7B
  b6,7,8,76-79 by ROW SPLIT tails UNPAIRED
  16/16, b0 const ff, b84-87 const 824c14d7
  ring-wide; T97503);
  A paylen 88, C paylen 88, Q paylen 88, R paylen 88 +
  counter b4=(0xb3+2*off)&FF b5=0x6e+(off>=39)+
  (off>=167).
  C blocks carry T97443/T97448/T97453/T97468/
  T97483/T97503 py-line mirrors (exact: py guard
  lines verified at those numbers first-hand);
  guards `if ((n) == (145149))` / `if ((n) == (145150))`
  + 4 ranges `(145151)<=(n)<=(145166)` /
  `(145167)<=(n)<=(145176)` /
  `(145177)<=(n)<=(145240)` /
  `(145241)<=(n)<=(145496)` exact; ring
  counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 39/167 identical first-hand
  arithmetic, per-off values in values log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  A 16/16 + C 10/10 counter match 0 mismatches.
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (b84-87 M4 TAIL mid-body M);
  M 16/16 distinct (7B);
  QR 4/4 distinct UNPAIRED;
  QR full-tail shares: trailing = TSHARE = subseq
  = 3/0/0/0/0/3, all-3 agree (pairs (0,1),(2,3)
  share trailing 3; no trailer consts; full tuples
  pairwise unequal, distinct 4);
  RQ==M FULL-IDENTITY (code M 7B lanes
  [6,7,8,80-83] vs RQ7 7B lanes [6,7,8,76-79]:
  rows 16/16 (same width, same values); per-col
  position-exact all 7x16/16; col-set overlaps
  all-full (13/13, 8/8, 2/2, 14/14, 13/13, 16/16,
  15/15); full-row sets EQUAL) --
  56th odd-band RQ==M instance (odds 55->56);
  12th FULL-identity degree (after b475 FULL 11th;
  b473 was the DISJOINT exception per
  GATE-6922336f + VERIFY-6922336f);
  lanewise the tail columns differ (M b80-83 vs
  RQ b76-79) with identical values: TAIL-IDENTITY
  ordered 16/16 + set-eq;
  ordered per lesson (d);
  AM-vs-RQ cross-check SKIPPED (widths differ 8B
  vs 7B, no same-width crosscheck applicable);
  width predictor dead, never cited;
  tails SPLIT (TM7 b13-15,80-83 by COL
  c=off&15, TR7 b6-8,76-79 by ROW
  r=off>>4, 16/16 distinct each, sequences
  UNPAIRED);
  M-tails (b80-83) 16/16 ALL NEW vs P368T
  row-led tails (ref: P368T SWAPPED, b80-83
  ROW-led via RQ8; overlap 0) AND vs P368T
  col-led tails (overlap 0);
  RQ-tails (b76-79) 16/16 ALL NEW vs P368T
  row-led AND col-led tails (overlap 0 both);
  RM-tails (b80-83) 16/16 ALL NEW vs P368T
  row-led AND col-led tails (overlap 0 both);
  S0 33/84 NEW-sig (b0-2 IN diff, b3 same) + S1
  56/88 NEW-sig (b0 IN diff, b1-3 same-sig NOT
  in diff) +
  S1-vs-own-C10 40/88 UNIFORM +
  S1-vs-P368C10[0] 50/88 SIG-DIFFERS +
  S1 SIG-EQ own C10 (1e000000 both) +
  S1 SIG-DIFFERS own PB0 (1e vs ef) and PBA sig
  (1e vs e5);
  P369 actuals (S0 ef928b0e/S1 1e000000/PBA88
  sig e5010000 x16 b0 const e5 + PB0-vs-P368PB0
  33/84 NEW-sig + PB1-vs-P368PB1 56/88 NEW-sig
  + S1-vs-own-C10 40/88 + SAMESIG-as-PB1 C10,
  PBA88-STEP-M8b52 VPOS 10 b5 step 6d->6e,
  C10-1SIG-88-TAIL-M4 VPOS 5 b4 varies b5 const
  6e, QUAD88-1SIG-QM7/R4-NOEDGE VPOS 12 =
  b4+QM7+R4 + R4 4/4 UNPAIRED exact rows +
  trailing 3/0/0/0/0/3 all-3 agree + NO const
  trailer + M-tails ALL NEW 16/16, T88-STANDARD-
  split-TM7/TR7 sig ff1e0000 TM7 by COL + TR7 by
  ROW UNPAIRED 16/16 + SPLIT tails + b84-87
  const 824c14d7 ring-wide, ring edges +
  thresholds 39/167, NO D dips) == w2b-r33
  qTBD-p369 census predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head ff/6d (145151)
  step 01/6e (145152), b5set {109,110} (decimal =
  0x6d,0x6e) 1 step;
  C head 1f/6e (145167) tail 31/6e (145176),
  b5set {110} (decimal = 0x6e) NO edge;
  Q head 33/6e (145177) + off15/16 (145192->
  145193) 51/6e->53/6e + off31/32 (145208->
  145209) 71/6e->73/6e + mid off48 93/6e
  (145225) + tail off63 b1/6e (145240),
  b5set {110} (decimal = 0x6e) NO edge;
  T head b3/6e (145241) + off38/39 (145279->
  145280) ff/6e->01/6f + mid off103 81/6f
  (145344) + off166/167 (145407->145408)
  ff/6f->01/70 + mate off168 03/70 (145409) +
  tail off255 b1/70 (145496).
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 145496 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  e44381975fcfe325ed082f58aa54290e29a066377c
  279ecdb035a4fa71c0cf1c matches PINS rawlen
  104; PASS g-z145496 + g-z145496-closed in BOTH
  legs, sorted cmp-equal).
  Ring counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 39/167 identical first-hand
  arithmetic, per-off values in values log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  A 16/16 + C 10/10 counter match 0 mismatches;
  band 29/348 pins in for-list, all PASSx2 both
  legs; full-tier 348/348 CLOSED via writer bed
  (w2b-r33 qTBD-p369: 145149..145496 bounds-
  verified, 1x(100,84)+347x(104,88) framing =
  code dispatch 1+1+16+10+64+256 = 348 pins;
  N-start 145149 = 83553+(369-192)*348 arithmetic
  first-hand) + RGRAM py+C 21948/21948 GREEN +
  tail rav byte-identical to PINS sha first-hand.
- C diff pure-add: numstat 608/0 rgramc.c + 231/0
  rgram.py (+1/-1 for-line, +58/0 PINS); raw C 608
  = 603 content + 5 blank-only lines / 0 del;
  raw py 231 content / 0 del (bank single-route 231
  this band, measured; C+py port/merge split clean:
  port commit C-only 608, merge commit py+sh+PINS);
  C legs touch ZERO PINS rows + ZERO for-line
  (add-only; sole del = old for-line churn, test_
  rgram.sh 1/1).
  Normalized ([0-9]+ -> N, diff-sign strip) del-uniq
  0 (0 true `-` lines in C+py diffs).
- Wall on band diff added lines (scope 0c29b70b..
  e9c52e90, 898 added lines: 893 content + 5 blank):
  vendor/disasm 0 hits, depload (dylib/CDLL/dlopen/
  ctypes/LoadLibrary/System.load) 0 hits,
  libcompression//usr/bin/aa 0 hits, shebang 0 hits,
  aea-invoke 0 hits (0 `aea' substrings, 0
  invocations). Files touched:
  rgramc.c 608/0, rgram.py 231/0, test_rgram.sh 1/1,
  PINS 58/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 2102->2108 +6, singletons
  `if n == ` 770->772 +2, range-guards
  `<= n <=` 928->932 +4, CLOSED T10P prints
  2102->2108 +6, seal 2196->2202
  +6 (cport msgs; offset +94 (base 2196-2102 and
  band 2202-2108 both +94 first-hand)).
  C guards: singleton `if ((n) == (` 765->767 +2,
  range `) <= (n)` 928->932 +4; 5-count C-vs-py
  singleton offset pre-existing (same C-only dip
  guards; offset 5 at base AND band, unchanged
  by band).
  C byte-index lists match py per block
  (A 8B, C 4B, Q 7B/4B, R 7B/7B SPLIT
  tails-split); insert position exact (P368R
  block precedes, P369R last block immediately
  precedes N-out-of-scope fallthrough; both sides).
  Temps _t7357.._t7372 appended
  (base max use _t7356, 16 contiguous, no reuse);
  _i band 4467,4469,4472,4475, _b band 4466,4468,
  4470,4471,4473,4474 (base max _i4465/_b4464,
  all band numbers absent from base, no reuse;
  generator-stride gaps unused anywhere:
  _i4466/_b4465/_b4467/_b4469/_b4472 + _i4468/
  4470/4471/4473/4474 absent whole tree).
- CONFIRM evidence: NO rgram memo CONFIRM for P369
  on file at gate time (A-956-q1081 absent;
  filename survey first-hand; memo answers P368/
  P369 pending). Writer-bed evidence w2b-r33
  qTBD-p369 read first-hand (P-head geometry
  census: PB0 NEW-sig 33/84, PB1 NEW-sig 56/88,
  PBA e5 x16, C10 1e x10 SAME-as-PB1, QM7/R4
  rows + tails, TM7/TR7 STANDARD frame, M-tails
  ALL NEW vs P368T RQ, counters + edges, consts
  78/82/75/72 -- all agree with this GATE's
  numbers first-hand).
  Q-1081 UNANSWERED at gate time (no CONFIRM of
  either side on file; filename survey first-hand).
  Viewer: NO P369 geometry answer on file at gate
  time (filename survey first-hand; viewer VERIFY
  lands post-gate per pipeline order).
  No DISSENT on P369 (DISSENT files on file are
  T10P923/924/926 far-future, withdrawn Qs, checked
  not applicable); no FLAG names P369/b477/e9c52e90
  (filename + body-grep survey first-hand). Agrees
  with cport commit msg (py/C 21948, PYID 10974).
- Quiz: no conflicting CLAIM/GATE/FLAG on b477/
  e9c52e90 (quiz poll + filename grep first-hand;
  GATE-e9c52e90 absent before filing).
  Newest PARENT-* QNUM-38 (w2d Q-block grant, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r81/ (all *477* +
  builds, tail-145496 via ct-cache hit e4438197).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
