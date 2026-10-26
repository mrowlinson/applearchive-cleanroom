# GATE 5dcf81a8 b471 T10P363 pins 143061..143408 (348 pins) PASS-functional

Seat sweep-r79, first-hand, WT tmp/wt-encode-sweep @5dcf81a8,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r79.
Band = 3c030696 (py merge w2b@027a0ffce, +6 tiers
+58 pins) + 5dcf81a8 (C port). Base 2ded9376 (b470 tip,
2160 tiers sealed).

- Build: make -C src/c BUILDDIR=r79/build471 aae rgramc
  (absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build471/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r79, sha256 = b354-b461 pinned
  value, verified this band; band touches no aae
  sources), rgramc
  sha1 ef45016b / sha256 0b6c47fd (new value: band
  touches C sources, recorded first-hand).
- RGRAMC-PYID 10800/10800 covered=10800/10800 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 21600/21600 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME;
  10800 pins x2 open+closed).
- RGRAM C 21600/21600 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (21600/21600, sorted, cmp-equal first-hand).
- PINS-RGRAM cells set-eq 10800/10800 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 21602 lines (2 hdr + 21600 rows, +58 vs base 21544).
  For-list union 10771->10800 +29/-0 (python sets,
  trailing-';' strip, never comm).
  29 = 2 sing (143061 143062; offs 0,1) +
  A 6 (head pair 143063 + 143064 + mid pair 143070 +
  143071 + tail pair 143077 + 143078; offs 0,1,7,8,
  14,15; offs 2-6,9-13 unsampled:
  143065-143069, 143072-143076; NO mid-single,
  b5 const NO edge, first-hand) +
  C 6 (head pair 143079 + 143080 + mid pair 143083 +
  143084 + tail pair 143087 + 143088; offs 0,1,4,5,
  8,9; offs 2,3,6,7 unsampled: 143081, 143082,
  143085, 143086; b5 const NO edge, first-hand) +
  Q 8 (head 143089 + edge pair 143103/143104 +
  off16 143105 + boundary pair 143120/143121 +
  boundary-single off48 143137 + tail 143152;
  offs 0,14,15,16,31,32,48,63; edge pair-covered,
  boundaries pair-covered except off47 mate
  unsampled (143136); b5 B5EDGE off14->15
  pair-covered, first-hand) +
  R 7 (head 143153 + edge pair 143231/143232 +
  mid 143290 + edge pair 143359/143360 + tail
  143408; offs 0,78,79,137,206,207,255; 1-mid
  shape off137 NEW, both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58
  = 21600-21542.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P363 C-vs-py, 12-table A-PBA88-PLAIN-
  M6b40/C10-1SIG-88-TAIL-M5b40/QUAD88-1SIG-QM7/R2-
  B5EDGE/T88-STANDARD-split-TM8/TR9 layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs ef0da90e NEW-sigdiff-2 / 1c000000 NEW-sig;
  S0 diff vs P362S0 30/84 @ 1,2,4-11,13-19,24,
  56-63,80-83 (sig b1-2 IN diff, b0,b3 same,
  NOT byte-equal) +
  S1 diff vs P362S1 50/88 @ 0,4,5,9-11,16-43,
  60-71,84-87 (sig b0 IN diff, b1-3 same-sig NOT
  in diff, NOT byte-equal) +
  S1 diff vs own C10 cells [10x26] TRUE-UNIFORM
  all 10 (cell diff 26 @ 4,19,26,27,34-47,72-75,
  84-87; sig b0-3 same-sig NOT in diff, SIG-EQ own
  C10; 26/88 == A-950 predicted EXACT; 22nd
  TRUE-uniform case: b463 20th -> b465 21st ->
  b467/b469 NOT-uniform -> this TRUE) +
  S1 vs P362C10[0] 40/88 (P362C10 sig 1d000000
  DIFFERS-sig, payload differs));
  AM 16/16 (6B), CM 10/10 (5B M5), M 16/16 (7B
  QM7), QR 4/4 (2B R2), RM 16/16 (8B), RQ
  16/16 (9B) EXACT;
  AC 80/80, CC 81/81, QC 77/77, RC 69/69 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 80/81/77/69 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit471.py 452 PASS 0 FAIL).
  12 py symbols = exactly the 12 tables (no _C probe:
  no numeric-head probe range covers N=143061+;
  table + probe precedent: band29/81c73cb3 only).
  NO F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R2 carries b84,85 in-row + b86/b87
  consts); table inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-8 [4,5,40,41,
  80,81,82,83] = b4,b5+M6 (b40,41,80-83;
  full sig b0-3 in AC = 96,01,00,00 ->
  96010000 x16, b0 const 96; AC b84-87 const
  fc,85,b6,29 A-lane);
  CC-7 [4,5,40,84,85,86,87] = b4,b5+M5 (b40,84-87;
  b40 2-valued mid-body [0xa8,0xa9] first-hand
  (7xa8+3xa9; no filed b40-2-valued precedent,
  shape M5 filed, no FIRST claimed);
  full sig b0-3 in CC = 1c,00,00,00 -> 1c000000
  x10 SAME-as-PB1-sig; CC b52 const 0xb9 const-entry
  first-hand);
  QC-11 [4,5,30,39,47,80,81,82,83,84,85] =
  b4,b5+QM7 (b30,39,47,80-83)+R2 (b84,85;
  b0-3 const 96,01,00,00 -> 96010000 x64 1SIG
  SAME-sig-as-PBA; b86 const 0xbc + b87
  const 0x37 quad-wide);
  RC-19 [4,5,40,41,42,46,47,52,53,54,55,76,77,
  78,79,80,81,82,83] = b4,b5+TR9 (b40,41,42,46,
  47,76-79)+TM8 (b52-55,80-83).
  PLAIN-M6b40: m-tab b40,41,80-83, positions FIRST
  this lane per code comment (QM6 same lanes filed
  Q-side b468 GATE-97337e61; no A-side filed
  precedent found; no FIRST claimed); M5b40 shape
  filed (GATE-a69ef1d1 TAIL-M5b40, same m-tab
  lanes; no FIRST claimed); QM7 shape filed (b467
  lanes b20-22; here lanes b30,39,47 -- lane-set
  differs, shape filed, no FIRST claimed); R2 filed
  (b465/b467/b469); TM8+TR9 shapes + lanes filed
  (GATE-30d227cf RC-19 identical missing-set and
  lanes; STANDARD-split; no FIRST claimed); B5EDGE
  quad shape filed (b461 R3-B5EDGE; Q-steps vary
  here, deduct-only-when-vary holds).
  Code AC80/CC81/QC77/RC69 = A-950 EXCL 80/81/77/69
  EXACT (+0 all four; memo notes incl +2 for the
  two b5-const regions A/C -- Q steps, T counter
  varies, no deduction).
  VPOS 7/6/11/19 derived first-hand (VPOS =
  varying-of-{b4,b5} + mtab + rtab: A 1+6+0
  (b4+M6, b5 const); C 1+5+0 (b4+M5, b5 const);
  Q 2+7+2 (b4,b5-step+QM7+R2); T 2+8+9
  (b4,b5+TM8+TR9)).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3630 n==143061 /
  P3631 n==143062 singleton-const (offs 0/1; 84B/88B;
  T96056/T96061 py-line mirrors);
  P363A 143063..143078 off=n-143063 PBA88-PLAIN-
  M6b40 (m-tab 6B b40,41,80-83, sig 96010000,
  b0 const 96, raw lencode b4=(0xaf+2off)&FF
  b5 const 5d NO step NO edge; T96066);
  P363C 143079..143088 off=n-143079 C10-1SIG-88-
  TAIL-M5b40 (m-tab 5B b40,84-87, b40 2-valued
  mid-body, full sig b0-3 in CC = 1c000000,
  raw lencode b5 const 5d NO step NO edge; T96081);
  P363Q 143089..143152
  off=n-143089 m=off&15 q=off>>4 QUAD88-1SIG-
  QM7/R2-B5EDGE 1-sig 96010000 x64 (b0-3 const
  96,01,00,00 in QC = SAME-sig-as-PBA)
  (M 7B b30,39,47,80-83 QM7
  shared + R2 b84,85 r0 4131 / r1 6131 / r2
  0732 / r3 2732 exact tuples + b86 const 0xbc
  + b87 const 0x37 quad-wide (TAIL4 trailing =
  TSHARE = subseq = 3/2/2/2/2/3, all-3 agree,
  pairs share b86 const bc + b87 const 37,
  full tuples pairwise unequal, first-hand),
  raw lencode b4=(0xe3+2off) b5=0x5d+(off>=15)
  edge 143103->143104 ff/5d->01/5e; T96096);
  P363R(T88-ring) 143153..143408 off=n-143153
  c=off&15 r=off>>4 STANDARD-split sig 961d0000
  (TM8 8B b52-55,80-83 by COL + TR9 9B b40,41,
  42,46,47,76-79 by ROW SPLIT tails UNPAIRED
  16/16, b0 const 96, b84-87 const 4732bc37
  ring-wide; T96116);
  A/C paylen 88 / raw lencode b4=(0xaf+2off)
  b5 const 5d (A) / raw lencode b5 const
  5d (C);
  Q paylen 88 / raw lencode b4=(0xe3+2off)
  b5=0x5d+(off>=15) (step emerges from raw
  lencode 64/64);
  R paylen 88 +
  counter b4=(0x63+2*off)&FF b5=0x5e+(off>=79)+
  (off>=207).
  C blocks carry T96056/T96061/T96066/T96081/
  T96096/T96116 py-line mirrors (exact); guards
  `if ((n) == (143061))` / `if ((n) == (143062))`
  + 4 ranges `(143063)<=(n)<=(143078)` /
  `(143079)<=(n)<=(143088)` /
  `(143089)<=(n)<=(143152)` /
  `(143153)<=(n)<=(143408)` exact; ring
  counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 79/207 identical first-hand
  arithmetic, per-off values in edges log);
  quad counter==raw-lencode 64/64 b4 mismatches 0.
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge (b40 2-valued [0xa8,0xa9]
  mid-body M); M 16/16 distinct (7B);
  QR 4/4 distinct UNPAIRED (r0 4131; r1
  6131; r2 0732; r3 2732);
  QR full-tail shares: trailing-suffix = TSHARE =
  subseq = 3/2/2/2/2/3, all-3 agree (pairs
  share b86 const bc + b87 const 37; full
  tuples pairwise unequal, distinct 4);
  RQ==M 0OF7 (code M 7B lanes [30,39,47,80-83]
  vs RQ 9B lanes [40,41,42,46,47,76-79]:
  rows 0/16 (widths differ); first-7 per-col
  position-exact all 0/16; col-set overlaps
  0/0/0/0/0/3/0 (only c5 shares 3 values);
  full-row sets DISJOINT) --
  53rd odd-band RQ==M instance, 2nd fully-disjoint
  degree (after b465's 0OF8 FIRST-disjoint);
  ordered per lesson (d);
  AM-vs-RQ cross-check (6B/6B prefix): rows 0/16,
  per-col all 0/16, col-set overlaps 0/0/0/0/1/1
  (agrees: disjoint);
  width predictor dead, never cited;
  tails STANDARD-split (TM8 b52-55,80-83 by COL
  c=off&15, TR9 b40,41,42,46,47,76-79 by ROW
  r=off>>4, 16/16 distinct each, sequences
  UNPAIRED);
  M-tails (b80-83) 16/16 ALL NEW vs P362T
  col-led tails (overlap 0; P362T RM 16x9B frame
  first-hand from code, tails last-4B);
  RQ-tails (b76-79) 16/16 ALL NEW vs P362T TR7
  row-led tails AND vs P362T col-led tails
  (overlap 0 both; P362T RQ 16x7B frame
  first-hand from code, tails last-4B);
  RM-tails (b80-83) 16/16 ALL NEW vs P362T
  col-led tails AND vs P362T TR7 tails
  (overlap 0 both);
  S0 30/84 NEW-sigdiff-2 (b1-2 IN diff, b0,b3
  same) + S1 50/88 NEW-sig (b0 IN diff, b1-3
  same) + S1-vs-own-C10 26/88 UNIFORM +
  S1-vs-P362C10[0] 40/88 DIFFERS-sig +
  S1 SIG-EQ own C10 (1c000000 both);
  P363 actuals (S0 ef0da90e/S1 1c000000/PBA88
  sig 96010000 x16 b0 const 96 + PB0-vs-P362PB0
  30/84 sigdiff-2 + PB1-vs-P362PB1 50/88 NEW-sig
  + S1-vs-own-C10 26/88 + M5-C10 1c000000 x10
  SAME-as-PB1-sig) == A-950 predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head af/5d (143063)
  tail cd/5d (143078), b5set {93} (decimal =
  0x5d) NO edge;
  C head cf/5d (143079) tail e1/5d (143088),
  b5set {93} (decimal = 0x5d) NO edge;
  Q head e3/5d (143089) + edge off14/15 (143103->
  143104) ff/5d->01/5e + tail off63 61/5e (143152),
  b5set {93,94} (decimal = 0x5d,0x5e) 1 edge, b4
  range e3..61 wrap+2 (64 distinct);
  T head 63/5e (143153) + off78/79 (143231->
  143232) ff/5e->01/5f + mid off137 75/5f
  (143290) + off206/207 (143359->143360)
  ff/5f->01/60 + tail off255 61/60 (143408).
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 143408 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  9eb9466c54982f168c4ce23b084517b645dfc2ec98
  df6e9013a9943e7330a755 matches PINS rawlen
  104; PASS g-z143408 + g-z143408-closed in BOTH
  legs, sorted cmp-equal).
  Ring counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 79/207 identical first-hand
  arithmetic, per-off values in edges log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  band 29/348 pins in for-list, all PASSx2 both
  legs; full-tier 348/348 CLOSED via A-950 (writer
  bed 143061..143436 BAD=0 + verifier v501 50/50 +
  T10P363 N-start 143061 = 83553+(363-192)*348
  arithmetic first-hand).
  Matches A-950 geometry (framing 1x84+347x88 pay =
  code dispatch 1+1+16+10+64+256 = 348 pins,
  PB0 ef0da90e NEW-sigdiff-2 30/84 + PB1 1c000000
  NEW-sig 50/88 + SAME-as-own-C10 26/88 +
  differs-vs-own-PB0,
  PBA88-PLAIN-M6b40 VPOS 7 b5 const 5d,
  C10-1SIG-88-TAIL-M5b40 VPOS 6 b5 const 5d b40
  2-valued,
  QUAD88-1SIG-QM7/R2-B5EDGE VPOS 11 =
  b4,b5-step+QM7+R2 + R2 4/4 UNPAIRED exact
  tuples + trailing 3/2/2/2/2/3 all-3 agree +
  b86/b87 consts bc/37 + M-tails ALL NEW 16/16,
  T88-STANDARD-split-TM8/TR9 sig 961d0000 TM8 by
  COL + TR9 by ROW UNPAIRED 16/16 + SPLIT tails +
  b84-87 const 4732bc37, ring edges + thresholds
  79/207, NO D dips) + A-950 (consts excl
  80/81/77/69 = lane EXACT).
- C diff pure-add: numstat 608/0 rgramc.c + 232/0
  rgram.py (+1/-1 for-line, +58/0 PINS); raw C 608
  = 603 content + 5 blank-only `+` lines / 0 del;
  raw py 232 content / 0 del; C legs touch ZERO
  PINS rows + ZERO for-line (add-only; sole del =
  old for-line churn, for-line 1/1).
  Normalized ([0-9]+ -> N, diff-sign strip) del-uniq
  0 (0 true `-` lines in C+py diffs).
- Wall on band diff added lines (scope 2ded9376..
  5dcf81a8, 899 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits, aea-invoke 0
  hits (1 `aea' substring: 1 PINS sha hex-literal
  fragment, 0 invocations). Files touched:
  rgramc.c 608/0, rgram.py 232/0, test_rgram.sh 1/1,
  PINS 58/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 2066->2072 +6, singletons
  `if n == ` 758->760 +2, range-guards `<= n <=`
  904->908 +4, CLOSED T10P prints
  2066->2072 +6, seal 2160->2166
  +6 (cport msgs; offset +94 (base 2160-2066 and
  band 2166-2072 both +94 first-hand)).
  C guards: singleton `if ((n) == (` 753->755 +2,
  range `) <= (n)` 904->908 +4; 5-count C-vs-py
  singleton offset pre-existing (same C-only dip
  guards as b357-b469 odds + b452-b470 evens),
  unchanged by band.
  C byte-index lists match py per block
  (A 6B, C 5B, Q 7B/2B, R 8B/9B STANDARD
  tails-split); insert position exact (P362R
  block precedes, P363R immediately precedes
  LAST scope-hit; C has 2 scope hits; py has 2
  scope hits).
  Temps _t7261.._t7276 appended
  (base max use _t7260, 16 contiguous, no reuse);
  _i band 4407,4409,4412,4415 (base max _i4405),
  _b band 4406,4408,4410,4411,4413,4414 (base
  max _b4404), union 4406-4415 contiguous, no
  reuse.
- CONFIRM evidence: A-950-q1075 memo CONFIRM 50/50
  CLEAN (Verifier v501.py 50/50 PASS; tier GATED
  PORT; novelty M-tails 16/16 ALL NEW vs P362T
  col-led tails; w2b-r32 8/8 CAP; cited from body
  read first-hand).
  Q-1075 answered/drained by A-950; no 2nd
  (r6-side) CONFIRM for q1075 on file at gate
  time (viewer-r69 live @b444-b447, ~20 bands
  behind; filename survey first-hand).
  Viewer: NO P363 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P363 (DISSENT files on file are
  T10P923/924/926 far-future, withdrawn Qs, checked
  not applicable); no FLAG names P363/b471/5dcf81a8
  (filename + body-grep survey first-hand). Agrees
  with cport commit msg (py/C 21600, PYID 10800).
- Quiz: no conflicting CLAIM/GATE/FLAG on b471/
  5dcf81a8 (quiz poll + filename grep first-hand;
  GATE-5dcf81a8 absent before filing).
  Newest PARENT-* QNUM-27 + 081-remount2-resume (no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r79/ (all *471* +
  builds, tail-143408 via ct-cache hit 9eb9466c).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
