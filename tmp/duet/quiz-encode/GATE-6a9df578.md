# GATE 6a9df578 b475 T10P367 pins 144453..144800 (348 pins) PASS-functional

Seat sweep-r80, first-hand, WT tmp/wt-encode-sweep @6a9df578,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r80.
Band = df52359f (py merge w2b@1cb13bd6, +6 tiers
+58 pins) + 6a9df578 (C port). Base 69e06615 (b474 tip,
2184 tiers sealed).

- Build: make -C src/c BUILDDIR=r80/build475 aae rgramc
  (absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 2
  mkdir/cc command echoes only), build475/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r79 seatings, sha256 = b354-b461 pinned
  value, verified this band; band touches no aae
  sources), rgramc
  sha1 e2b1dfbb / sha256 681dbf6e (new value: band
  touches C sources, recorded first-hand).
- RGRAMC-PYID 10916/10916 covered=10916/10916 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 21832/21832 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME;
  10916 pins x2 open+closed).
- RGRAM C 21832/21832 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (21832/21832, sorted, cmp-equal first-hand).
- PINS-RGRAM cells set-eq 10916/10916 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 21834 lines (2 hdr + 21832 rows, +58 vs base 21776).
  For-list union 10887->10916 +29/-0 (python sets,
  trailing-';' strip, never comm).
  29 = 2 sing (144453 144454; offs 0,1) +
  A 6 (head pair 144455 + 144456 + mid pair 144462 +
  144463 + tail pair 144469 + 144470; offs 0,1,7,8,
  14,15; offs 2-6,9-13 unsampled:
  144457-144461, 144465-144468; NO mid-single,
  b5 const NO edge, first-hand) +
  C 6 (head pair 144471 + 144472 + mid pair 144475 +
  144476 + tail pair 144479 + 144480; offs 0,1,4,5,
  8,9; offs 2,3,6,7 unsampled: 144473, 144474,
  144477, 144478; b5 const NO edge, first-hand) +
  Q 8 (head 144481 + edge pair 144496/144497 +
  offs 15,16 + edge pair 144511/144512 +
  offs 30,31 (B5EDGE pair) + boundary-single off47
  144528 + tail 144544;
  offs 0,15,16,30,31,47,63; both counter edges
  pair-covered, off47 covered (R1 shape);
  b5 step off31 pair-covered, first-hand) +
  R 7 (head 144545 + edge pair 144639/144640 +
  mid 144704 + edge pair 144767/144768 + mate
  144769 + tail 144800; offs 0,94,95,159,222,223,
  224,255; 1-mid shape off159 NEW, both counter edges
  pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58
  = 21832-21774.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P367 C-vs-py, 12-table A-PBA88-PLAIN-
  M6b10/C10-1SIG-88-TAIL-M3/QUAD88-1SIG-QM7/R1-
  B5EDGE/T88-SWAPPED-split-RM8/RQ7 layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs 2f9a600e NEW-sig / 1c000000 sig-REPEAT;
  S0 diff vs P366S0 33/84 @ 2-5,22,23,30,31,
  33-43,48,49,52-55,68-75 (sig b0-3 IN diff,
  b0,b1 differ, NOT byte-equal) +
  S1 diff vs P366S1 65/88 @ 4-59,76-87 (sig b0-3
  NOT in diff, b1-3 same-sig NOT in diff, NOT
  byte-equal) +
  S1 diff vs own C10 cells [10x79] TRUE-UNIFORM
  all 10 (cell diff 79 @ 4,6-55,60-87;
  sig b0-3 same-sig NOT in diff, SIG-EQ own C10;
  79/88 == A-954 predicted EXACT; 24th
  TRUE-uniform case: b473 23rd -> this TRUE;
  sweep accounting owns the uniform count per
  viewer-vs-sweep convention) +
  S1 vs P366C10[0] 81/88 (P366C10 sig 1e000000
  SIG-DIFFERS own S1, payload differs));
  AM 16/16 (6B), CM 10/10 (3B M3), M 16/16 (7B
  QM7), QR 4/4 (1B R1), RM 16/16 (8B), RQ
  16/16 (7B) EXACT;
  AC 80/80, CC 83/83, QC 78/78, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 80/83/78/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit475.py 457 PASS 0 FAIL).
  12 py symbols = exactly the 12 tables (no _C probe:
  no numeric-head probe range covers N=144453+;
  table + probe precedent: band29/81c73cb3 only).
  NO F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R1 carries b84 in-row + b85/b86/b87
  consts); table inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-8 [4,5,10,11,
  80,81,82,83] = b4,b5+M6 (b10,11,80-83;
  full sig b0-3 in AC = b6,01,00,00 ->
  b6010000 x16, b0 const b6);
  CC-5 [4,5,84,85,86] = b4,b5+M3 (b84-86;
  full sig b0-3 in CC = 1c,00,00,00 -> 1c000000
  x10 SAME-as-PB1-sig first-hand);
  QC-10 [4,5,20,21,22,80,81,82,83,84] =
  b4,b5+QM7 (b20,21,22,80-83)+R1 (b84;
  b0-3 const cf,01,00,00 -> cf010000 x64 1SIG
  DIFFERS-from-PBA-sig; b85 const 0x9b +
  b86 const 0xed + b87 const 0x86 quad-wide);
  RC-17 [4,5,20,21,22,28,29,30,31,76,77,78,79,
  80,81,82,83] = b4,b5+RQ7 (b20-22,80-83)+RM8
  (b28-31,76-79).
  PLAIN-M6b10: m-tab b10,11,80-83, positions FIRST
  this lane per code comment (no A-side filed
  precedent; no FIRST claimed beyond code-stated);
  TAIL-M3 shape filed (b87 const 86 quad-wide
  entry; no FIRST claimed); QM7 shape filed (b467/
  b469/b471/b473 lane-sets differ; here lanes b20-
  22, lane-set differs, shape filed, no FIRST
  claimed); R1 filed (P360/P364 pattern, single-byte
  rows); RM8/RQ7 shapes + lanes FIRST this lane per
  code comment (SWAPPED-split; staged refs P359R/
  P343/P351R/P359R; no FIRST claimed beyond
  code-stated); B5EDGE quad shape filed (b461 R3-
  B5EDGE; Q-steps vary here, deduct-only-when-
  vary holds).
  Code AC80/CC83/QC78/RC71 = A-954 EXCL 80/83/78/71
  EXACT (+0 all four; memo notes incl +2 for the
  two b5-const regions A/C -- Q b5 steps once,
  T counter varies, no deduction).
  VPOS 7/4/10/17 derived first-hand (VPOS =
  varying-of-{b4,b5} + mtab + rtab: A 1+6+0
  (b4+M6, b5 const); C 1+3+0 (b4+M3, b5 const);
  Q 2+7+1 (b4,b5-step+QM7+R1); T 2+8+7
  (b4,b5+RM8+RQ7)).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3670 n==144453 /
  P3671 n==144454 singleton-const (offs 0/1; 84B/88B;
  T96983/T96988 py-line mirrors);
  P367A 144455..144470 off=n-144455 PBA88-PLAIN-
  M6b10 (m-tab 6B b10,11,80-83, sig b6010000,
  b0 const b6, raw lencode b4=(0x8f+2off)&FF
  b5 const 68 NO step NO edge; T96993);
  P367C 144471..144480 off=n-144471 C10-1SIG-88-
  TAIL-M3 (m-tab 3B b84-86, full sig b0-3 in CC
  = 1c000000, raw lencode b5 const 68 NO step
  NO edge; T97008);
  P367Q 144481..144544
  off=n-144481 m=off&15 q=off>>4 QUAD88-1SIG-
  QM7/R1-B5EDGE 1-sig cf010000 (b0-3 const
  cf,01,00,00 in QC = DIFFERS-from-PBA-sig)
  (M 7B b20,21,22,80-83 QM7
  shared + R1 b84 r0 59 / r1 79 / r2 99 / r3
  b9 exact single-byte rows 4/4 UNPAIRED + b85
  const 0x9b + b86 const 0xed + b87 const 0x86
  quad-wide (TAIL4 trailing = TSHARE = subseq =
  3/3/3/3/3/3, all-3 agree, pairs share consts
  9b/ed/86, full tuples pairwise unequal,
  distinct 4, first-hand),
  raw lencode b4=(0xc3+2off) b5=0x68+(off>=31)
  edge 144511->144512 ff/68->01/69; T97023);
  P367R(T88-ring) 144545..144800 off=n-144545
  c=off&15 r=off>>4 SWAPPED-split sig f31c0000
  (RM8 8B b28,29,30,31,76-79 by COL + RQ7 7B
  b20,21,22,80-83 by ROW SWAPPED tails UNPAIRED
  16/16, b0 const f3, b84-87 const d99bed86
  ring-wide; T97042);
  A/C paylen 88 / raw lencode b4=(0x8f+2off)
  b5 const 68 (A) / raw lencode b5 const
  68 (C);
  Q paylen 88 / raw lencode b4=(0xc3+2off)
  b5=0x68+(off>=31) (step emerges from raw
  lencode 64/64);
  R paylen 88 +
  counter b4=(0x43+2*off)&FF b5=0x69+(off>=95)+
  (off>=223).
  C blocks carry T96983/T96988/T96993/T97008/
  T97023/T97042 py-line mirrors (exact); guards
  `if ((n) == (144453))` / `if ((n) == (144454))`
  + 4 ranges `(144455)<=(n)<=(144470)` /
  `(144471)<=(n)<=(144480)` /
  `(144481)<=(n)<=(144544)` /
  `(144545)<=(n)<=(144800)` exact; ring
  counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 95/223 identical first-hand
  arithmetic, per-off values in edges log);
  quad counter==raw-lencode 64/64 b4 mismatches 0.
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (b84-86 M3 TAIL mid-body M);
  M 16/16 distinct (7B);
  QR 4/4 distinct UNPAIRED (r0 59; r1
  79; r2 99; r3 b9);
  QR full-tail shares: trailing-suffix = TSHARE =
  subseq = 3/3/3/3/3/3, all-3 agree (pairs
  share consts 9b/ed/86; full tuples pairwise
  unequal, distinct 4);
  RQ==M FULL-IDENTITY (code M 7B lanes
  [20,21,22,80-83] vs RQ7 7B lanes [20,21,22,
  80-83]: rows 16/16 (same width, same lanes);
  per-col position-exact all 7x16/16; col-set
  overlaps all-full (16/3/2/16/15/14/14);
  full-row sets EQUAL) --
  55th odd-band RQ==M instance (odds 54->55);
  11th FULL-identity degree (after b469 FULL8
  10th; P365 was the DISJOINT exception per
  GATE-6922336f + VERIFY-6922336f);
  ordered per lesson (d);
  AM-vs-RQ cross-check SKIPPED (widths differ 6B
  vs 7B, no same-width crosscheck applicable);
  width predictor dead, never cited;
  tails SWAPPED (RM8 b28-31,76-79 by COL
  c=off&15, RQ7 b20-22,80-83 by ROW
  r=off>>4, 16/16 distinct each, sequences
  UNPAIRED);
  M-tails (b80-83) 16/16 ALL NEW vs P366T
  col-led tails (overlap 0; P366T RM 16x8B frame
  first-hand from code, tails last-4B);
  RQ-tails (b80-83) 16/16 ALL NEW vs P366T
  col-led tails AND vs P366T row-led tails
  (overlap 0 both; P366T RQ 16x9B frame
  first-hand from code, tails last-4B);
  RM-tails (b76-79) 16/16 ALL NEW vs P366T
  col-led tails AND vs P366T row-led tails
  (overlap 0 both);
  S0 33/84 NEW-sig (b0-3 IN diff) + S1
  65/88 sig-REPEAT (b0-3 NOT in diff) +
  S1-vs-own-C10 79/88 UNIFORM +
  S1-vs-P366C10[0] 81/88 SIG-DIFFERS +
  S1 SIG-EQ own C10 (1c000000 both) +
  S1 SIG-DIFFERS own PB0 (1c vs 2f);
  P367 actuals (S0 2f9a600e/S1 1c000000/PBA88
  sig b6010000 x16 b0 const b6 + PB0-vs-P366PB0
  33/84 NEW-sig + PB1-vs-P366PB1 65/88 sig-REPEAT
  + S1-vs-own-C10 79/88 + SAMESIG-as-PB1 C10,
  PBA88-PLAIN-M6b10 VPOS 7 b5 const 68,
  C10-1SIG-88-TAIL-M3 VPOS 4 b5 const 68,
  QUAD88-1SIG-QM7/R1-B5EDGE VPOS 10 =
  b4,b5-step+QM7+R1 + R1 4/4 UNPAIRED exact
  single-byte rows + trailing 3/3/3/3/3/3 all-3
  agree + b85/b86/b87 consts 9b/ed/86 + M-tails
  ALL NEW 16/16, T88-SWAPPED-split-RM8/RQ7 sig
  f31c0000 RM8 by COL + RQ7 by ROW UNPAIRED 16/16
  + SWAPPED tails + b84-87 const d99bed86
  ring-wide, ring edges + thresholds 95/223, NO D
  dips) == A-954 predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head 8f/68 (144455)
  tail ad/68 (144470), b5set {104} (decimal =
  0x68) NO edge;
  C head af/68 (144471) tail c1/68 (144480),
  b5set {104} (decimal = 0x68) NO edge;
  Q head c3/68 (144481) + off30/31 (144511->
  144512) ff/68->01/69 + mid off47 21/69
  (144528) + tail off63 41/69 (144544),
  b5set {104,105} (decimal = 0x68,0x69) 1 edge, b4
  range c3..41 step+2 (64 distinct, 1 wrap);
  T head 43/69 (144545) + off94/95 (144639->
  144640) ff/69->01/6a + mid off159 81/6a
  (144704) + off222/223 (144767->144768)
  ff/6a->01/6b + off224 03/6b (144769) + tail
  off255 41/6b (144800).
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 144800 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  bd5be0159bfde8471b260b5b9e1fb13a279dd11964
  bc2fe557b40c6bb996015a matches PINS rawlen
  104; PASS g-z144800 + g-z144800-closed in BOTH
  legs, sorted cmp-equal).
  Ring counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 95/223 identical first-hand
  arithmetic, per-off values in edges log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  band 29/348 pins in for-list, all PASSx2 both
  legs; full-tier 348/348 CLOSED via A-954 (writer
  bed 144453..144828 BAD=0 + verifier v501 52/52 +
  direct-oracle 2/2 byte-match + T10P367 N-start
  144453 = 83553+(367-192)*348 arithmetic
  first-hand).
  Matches A-954 geometry (framing 1x84+347x88 pay =
  code dispatch 1+1+16+10+64+256 = 348 pins,
  PB0 2f9a600e NEW-sig 33/84 + PB1 1c000000
  sig-REPEAT 65/88 + SAME-as-own-C10 79/88 +
  differs-vs-own-PB0,
  PBA88-PLAIN-M6b10 VPOS 7 b5 const 68,
  C10-1SIG-88-TAIL-M3 VPOS 4 b5 const 68,
  QUAD88-1SIG-QM7/R1-B5EDGE VPOS 10 =
  b4,b5-step+QM7+R1 + R1 4/4 UNPAIRED exact
  single-byte rows + trailing 3/3/3/3/3/3 all-3
  agree + b85/b86/b87 consts 9b/ed/86 + M-tails
  ALL NEW 16/16, T88-SWAPPED-split-RM8/RQ7 sig
  f31c0000 RM8 by COL + RQ7 by ROW UNPAIRED 16/16
  + SWAPPED tails + b84-87 const d99bed86
  ring-wide, ring edges + thresholds 95/223, NO D
  dips) + A-954 (consts excl 80/83/78/71 = lane
  EXACT).
- C diff pure-add: numstat 608/0 rgramc.c + 231/0
  rgram.py (+1/-1 for-line, +58/0 PINS); raw C 608
  = 603 content + 5 blank-only `+` lines / 0 del;
  raw py 231 content / 0 del (bank VARIES 231 vs
  232 route; measured, never carried); C legs touch
  ZERO PINS rows + ZERO for-line (add-only; sole del =
  old for-line churn, for-line 1/1).
  Normalized ([0-9]+ -> N, diff-sign strip) del-uniq
  0 (0 true `-` lines in C+py diffs).
- Wall on band diff added lines (scope 69e06615..
  6a9df578, 898 added lines: 893 content + 5 blank):
  vendor/disasm 0 hits, depload (dylib/CDLL/dlopen/
  ctypes/LoadLibrary/System.load) 0 hits,
  libcompression//usr/bin/aa 0 hits, shebang 0 hits,
  aea-invoke 0 hits (0 `aea' substrings, 0
  invocations). Files touched:
  rgramc.c 608/0, rgram.py 231/0, test_rgram.sh 1/1,
  PINS 58/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 2090->2096 +6, singletons
  `if n == ` 766->768 +2, range-guards `<= n <=`
  920->924 +4, CLOSED T10P prints
  2090->2096 +6, seal 2184->2190
  +6 (cport msgs; offset +94 (base 2184-2090 and
  band 2190-2096 both +94 first-hand)).
  C guards: singleton `if ((n) == (` 761->763 +2,
  range `) <= (n)` 920->924 +4; 5-count C-vs-py
  singleton offset pre-existing (same C-only dip
  guards as b357-b469 odds + b452-b474 evens),
  unchanged by band.
  C byte-index lists match py per block
  (A 6B, C 3B, Q 7B/1B, R 8B/7B SWAPPED
  tails-split); insert position exact (P366R
  block precedes, P367R last block immediately
  precedes N-out-of-scope fallthrough; both sides).
  Temps _t7325.._t7340 appended
  (base max use _t7324, 16 contiguous, no reuse);
  _i band 4447,4449,4452,4455, _b band 4446,4448,
  4450,4451,4453,4454 (base max _i4445/_b4444,
  union 4446-4455 contiguous, no reuse).
- CONFIRM evidence: A-954-q1079 memo CONFIRM 52/52
  CLEAN (Verifier v501.py 52/52 PASS; direct-oracle
  2/2 byte-match; tier GATED PORT; novelty M-tails
  16/16 ALL NEW vs P366T col-led tails; w2b-r33
  [4/8]; cited from body read first-hand).
  Q-1079 answered/drained by A-954; no 2nd
  (r6-side) CONFIRM for q1079 on file at gate
  time (filename survey first-hand).
  Viewer: NO P367 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P367 (DISSENT files on file are
  T10P923/924/926 far-future, withdrawn Qs, checked
  not applicable); no FLAG names P367/b475/6a9df578
  (filename + body-grep survey first-hand). Agrees
  with cport commit msg (py/C 21832, PYID 10916).
- Quiz: no conflicting CLAIM/GATE/FLAG on b475/
  6a9df578 (quiz poll + filename grep first-hand;
  GATE-6a9df578 absent before filing).
  Newest PARENT-* QNUM-36 (grants only, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r80/ (all *475* +
  builds, tail-144800 via ct-cache hit bd5be015).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
