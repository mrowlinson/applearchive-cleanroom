# GATE 2bc8d273 b455 T10P347 pins 137493..137840 (348 pins) PASS-functional

Seat sweep-r75, first-hand, WT tmp/wt-encode-sweep @2bc8d273,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r75.
Band = b94eec82 (py merge w2b@6ddee87a partial, +6 tiers
+58 pins) + 2bc8d273 (C port). Base b64b17b6 (b454 tip,
2064 tiers sealed).

- Build: make -C src/c BUILDDIR=r75/build455 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build455/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r75, sha256 = b354-b453 pinned
  value, verified this band; band touches no aae
  sources), rgramc
  sha1 08e5b33f / sha256 8bce9c44.
- RGRAMC-PYID 10336/10336 covered=10336/10336 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 20672/20672 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME).
- RGRAM C 20672/20672 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (20672/20672, sorted).
- PINS-RGRAM cells set-eq 10336/10336 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 20674 lines (2 hdr + 20672 rows, +60 vs base 20614).
  For-list union 10307->10336 +29/-0 (python sets,
  trailing-';' strip, never comm).
  29 = 2 sing (137493 137494) +
  A 6 (head 137495 + 137496 + pair 137502/137503 +
  pair 137509/137510 tail; offs 0,1,7,8,14,15; offs
  2-6,9-13 unsampled: 137497-137501, 137504-137508) +
  C 6 (head 137511 + 137512 + 137515 + 137516 +
  137519 + tail 137520; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 137513, 137514, 137517,
  137518) +
  Q 8 (head 137521 + boundary pairs 137536/137537 +
  137552/137553 + 137568/137569 + tail 137584; offs
  0,15,16,31,32,47,48,63; NO mid (b5 const NO edge),
  all boundaries pair-covered, first-hand) +
  R 7 (head 137585 + edge pair 137599/137600 +
  mid 137664 + edge pair 137727/137728 + tail
  137840; offs 0,14/15,79,142/143,255; 1-mid
  shape off79 NEW, both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58
  = 20672-20614.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P347 C-vs-py, 12-table A-PBA88-PLAIN-
  M8b40/C10-1SIG-88-TAIL-M4/QUAD88-1SIG-QM9/R4-NOEDGE+
  T88-RING-STANDARD-split layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs ef496f07 NEW-sig NEW family / 0d000000 NEW-sig
  vs P346PB1;
  S0 diff vs P346S0 31/84 @ b0-2,4-11,13-19,24,
  56-63,80-83 (sig b0-2 IN diff, NEW-sig NEW family) +
  S1 diff vs P346S1 51/88 @ b0,4,5,8-11,16-43,60-71,
  84-87 incl sig b0 NEW-sig, NOT byte-equal +
  S1 diff vs own C10 cells NOT UNIFORM (26x9 + 25x1:
  odd cell5 missing b84 from diff = m-lane
  coincidence CM[0]=0x9e==S1[84] in exactly one
  cell; sig b0-3 same-sig NOT in diff), NOT
  byte-equal);
  AM 16/16 (8B), CM 10/10 (4B), M 16/16 (9B),
  QR 4/4 (4B), RM 16/16 (7B), RQ 16/16 (8B)
  EXACT;
  AC 78/78, CC 82/82, QC 73/73, RC 71/71 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 78/82/73/71 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit455.py 449 PASS 0 FAIL).
  NO F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R4 carries b84-87 inside QR); table
  inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-10 [4,5,40,41,
  42,43,80,81,82,83] = b4,b5+M8 (b40-43,80-83);
  CC-6 [4,5,84,85,86,87] = b4,b5+M4 (b84-87 tails,
  full sig b0-3 in CC = 0d,00,00,00 ->
  0d000000 x10 SAME-as-PB1-sig; b84-87 all vary,
  NO b87 const);
  QC-15 [4,5,30,38,39,46,47,80,81,82,83,84,85,86,
  87] = b4,b5+QM9 (b30,38,39,46,47,80-83)+R4
  (b84-87; b0 const e8 in QC = 1SIG SAME-as-PBA,
  b1-3 const 00);
  RC-17 [4,5,40,41,46,47,52,53,54,76,77,78,79,80,
  81,82,83] = b4,b5+TR8 (b40,41,46,47,76-79)+
  TM7 (b52-54,80-83).
  PLAIN first-hand (M8 shape precedented: PLAIN-M8
  on file per PBA88-PLAIN-M8/M8b28; b40-43-lane
  variant precedented per memo; no FIRST claimed):
  AC b0..b3 = e8,00,00,00 -> sig e8000000 x16,
  b0 const e8; AM 16/16 distinct; b5 const 32
  NO step NO edge (A-b5set {50} first-hand).
  TAIL-M4 first-hand (M4 shape precedented:
  C10-M4 on file per A-1059/A-926 (CM b84-87 +
  full sig + b5 const); no FIRST claimed): CC b0-3
  full sig 0d000000 x10 SAME-as-PB1-sig (S1 sig-eq
  own C10); CM 10/10 diverge; b5 const 32 NO edge
  (C-b5set {50} first-hand).
  Code AC78/CC82/QC73/RC71; incl = +1/+1/+1/+0
  (A b5 const 32, C b5 const 32, Q b5 const 32,
  T counter) = 79/83/74/71; lane consts = A-926
  INCL EXACT (deduct-b5-only-when-b5vary rule holds;
  A-1059 excl 78/82/73/71 = code EXACT).
  VPOS 9/5/14/17 = A-926 EXACT, derived first-hand
  (VPOS = varying-of-{b4,b5} + mtab + rtab: A
  1+8+0 (b4+M8, b5 const); C 1+4+0 (b4+M4, b5
  const); Q 1+9+4 (b4+QM9+R4, b5 const); T 2+7+8
  (b4,b5+TM7+TR8)).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3470 n==137493 /
  P3471 n==137494 singleton-const (offs 0/1; 84B/88B);
  P347A 137495..137510 off=n-137495 PBA88-PLAIN-
  M8b40 (m-tab 8B b40-43,80-83, sig e8000000,
  b0 const e8, b5 const 32 NO step NO edge);
  P347C 137511..137520 off=n-137511 C10-1SIG-88-
  TAIL-M4 (m-tab 4B b84-87, full sig b0-3
  in CC = 0d000000, b5 const 32 NO step NO edge);
  P347Q 137521..137584 off=n-137521 m=off&15
  q=off>>4 QUAD88-1SIG-QM9/R4-NOEDGE
  1-sig e8000000 x64 SAME-sig-as-PBA (b0 const
  e8 in QC)
  (M 9B b30,38,39,46,47,80-83 QM9 shared NO frags
  (16 rows x4, m=off&15) + R4 b84-87 r0
  3e34f1c8 / r1 5e34f1c8 / r2 7e34f1c8 / r3
  3d6e3bca exact tuples, r012 TRUE 3B 34f1c8 +
  r3 trailing-suffix lcs 0 vs all (TAIL4-substr =
  TSHARE = subseq = 3/3/0/3/0/0, all-3 agree
  first-hand), b87 NOT const {c8,ca} = {0xc8,0xca},
  b5 const 32 NO edge, b4 0x63+2off range 63..e1
  contig+2 (no wrap, 64 distinct), NO frags);
  P347R(T88-ring) 137585..137840 off=n-137585
  c=off&15 r=off>>4 STANDARD-split sig 680d0000
  (TM 7B b52-54,80-83 by COL + TR 8B b40,41,46,
  47,76-79 by ROW SPLIT tails UNPAIRED 16/16,
  b0 const 68, b1 const 0d, b84-87 const
  5d6e3bca ring-wide);
  A/C paylen 88 / raw lencode b4=(0x2f+2off) b5
  const 32 (A) / b4=(0x4f+2off) b5 const 32 (C,
  both const emerge from raw lencode);
  Q paylen 88 / raw lencode (b5 const emerges
  from raw lencode 64/64);
  R paylen 88 +
  counter b4=(0xe3+2off)&FF b5=0x32+(off>=15)+
  (off>=143).
  C blocks carry T92345/T92350/T92355/T92370/
  T92385/T92406 py-line mirrors (exact); guards
  `if ((n) == (137493))` / `if ((n) == (137494))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; ring counter 227+2*off + 50+(off>=15)+
  (off>=143); temps _t7005.._t7020 appended
  (base max _t7004, 16 contiguous, no reuse);
  _i band 4247,4249,4252,4255 (base max _i4245),
  _b band 4246,4248,4250,4251,4253,4254 (base
  max _b4244), union 4246-4255 contiguous, no
  reuse; C byte-index lists match py per block
  (A 8B, C 4B, Q 9B/4B, R 7B/8B STANDARD
  tails-split); insert position exact (P346R
  block precedes, P347R immediately precedes
  LAST scope-hit; C has 2 scope hits; py has 2
  scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0 3e34f1c8; r1
  5e34f1c8; r2 7e34f1c8; r3 3d6e3bca);
  QR full-tail shares: r012 trailing-suffix lcs 3
  (TRUE 3B 34f1c8) + r3 lcs 0 vs all (TSHARE same,
  subseq same) (memo substance confirmed);
  RQ==M 4OF6 (M 9B vs RQ 8B: 6 comparable cols =
  2 shared + 4 tail-correspondent; tails (80,76),
  (81,77),(82,78),(83,79) 16/16 position-exact,
  tail SETS EQUAL (overlap 16/16); shared b46/b47
  0/16 each FULLY DISJOINT; M-only b30,38,39 /
  RQ-only b40,41 no counterpart) -- 45th odd-band
  RQ==M instance, FIRST 4OF6 degree (no 9B-vs-8B
  degree on file, full shape-name survey
  first-hand); ordered per lesson (d) (tails
  position-exact + tail-sets EQUAL, cf P341 8OF9);
  width predictor dead, never cited;
  tails STANDARD-split (TM b52-54,80-83 by COL
  c=off&15, TR b40,41,46,47,76-79 by ROW r=off>>4,
  16/16 distinct each, sequences UNPAIRED);
  M-tails 16/16 ALL NEW vs P346T RM col-led tails
  (overlap 0; P346T RM8 frame first-hand from
  code, ref = RM8 8B rows, position-aware
  tails last-4B);
  RQ-tails (b76-79) 16/16 ALL NEW vs P346T RQ
  row-led tails (overlap 0);
  S0 string 31/84 differ vs P346S0 (sig b0-2 IN
  diff, NEW-sig NEW family; @ b0-2,4-11,13-19,24,
  56-63,80-83) +
  S1 string 51/88 differ vs P346S1 (incl sig b0;
  @ b0,4,5,8-11,16-43,60-71,84-87; vs own C10
  NOT uniform (26x9+25x1, odd-cell5 b84 m-lane
  coincidence; sig b0-3 same-sig NOT in diff);
  uniformity stays ended per-band emergent, never
  assumed) +
  S1 SIG-EQ own C10 (0d000000 both);
  S1 vs P346C10[0] 40/88 (P346C10 sig 0e000000,
  NEW-sig vs prev C10 too);
  P347 actuals (S0 ef496f07/S1 0d000000/PBA88
  e8000000/C10 0d000000 x10 SAME-as-PB1-sig +
  PB0-vs-P346PB0 31/84 + PB1-vs-P346PB1 51/88)
  == A-1059 + A-926 predicted next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): S0 b4/b5 2b/32 = l16(137493),
  S1 b4/b5 2d/32 = l16(137494);
  A head 2f/32 (137495)
  tail 4d/32 (137510), b5set {32};
  C head 4f/32 (137511) tail 61/32 (137520),
  b5set {32};
  Q head 63/32 (137521) tail e1/32 (137584),
  b5set {32};
  quad b4=(0x63+2off) 64/64 contig+2 range
  63..e1 + b5 const 64/64;
  T head e3/32 (137585) + off14/15 (137599->
  137600) ff/32->01/33 + mid off79 81/33
  (137664) + off142/143 (137727->137728)
  ff/33->01/34 + tail off255 e1/34 (137840).
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 137840 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  4ab4a87a46b67074c118e74703d80d387dbe1e047cc
  2ec4e41476183f141432e matches PINS rawlen 104;
  PASS g-z137840 + g-z137840-closed in BOTH legs,
  sorted cmp-equal).
  Ring counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 15/143 identical first-hand
  arithmetic, per-off values in edges log);
  odd-lencode 348/348 first-hand (346 code-path +
  2 singleton-embedded: S0 b4/b5 2b/32 =
  l16(137493), S1 2d/32 = l16(137494)).
  Matches A-1059 geometry (framing 1x84+347x88 pay =
  code dispatch 1+1+16+10+64+256 = 348 pins,
  PB0 ef496f07 NEW-sig NEW family 31/84 + PB1
  0d000000 NEW 51/88 + SAME-as-own-C10 26/88 +
  differs-vs-own-PB0,
  PBA88-PLAIN-M8b40 VPOS 9 b5 const 32,
  C10-1SIG-88-TAIL-M4 VPOS 5 b5 const 32,
  QUAD88-1SIG-QM9/R4-NOEDGE VPOS 14 =
  b4+QM9+R4 (b5 const, SAME-sig-as-PBA) + R4 4/4
  UNPAIRED exact tuples + r012-3/r3-0 + b0 const
  in QC SAME-as-PBA + b87 NOT-const + b5 const
  NO edge + M-tails ALL NEW 16/16,
  T88-RING-STANDARD-split sig 680d0000 TM7 by COL +
  TR8 by ROW UNPAIRED 16/16 + SPLIT tails +
  b84-87 const 5d6e3bca, ring edges + thresholds
  15/143, NO D dips) + A-926 (suffix-lcs
  3/3/0/3/0/0 = TAIL4 b84-87 all 3 metrics
  first-hand; consts incl 79/83/74/71 = lane
  EXACT).
- C diff pure-add: numstat 608/0 rgramc.c + 232/0
  rgram.py (+1/-1 for-line, +58/0 PINS); raw C 608
  content + 5 blank-only `+` lines / 0 del; raw py
  232 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C+py del-uniq 0 add-uniq 351). Band-level
  sole del = old for-line churn (for-line 1/1).
- Wall on band diff added lines (scope b64b17b6..
  2bc8d273, 840 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits, aea-invoke 0
  hits. Files touched: rgramc.c 608/0, rgram.py
  232/0, test_rgram.sh 1/1, PINS 58/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1970->1976 +6, singletons
  `if n == ` 726->728 +2, range-guards `<= n <=`
  840->844 +4, CLOSED T10P prints
  1970->1976 +6, seal 2064->2070
  +6 (cport msgs; offset +94 (2070-1976; same +94 at
  b447 per r73 read + b448/b449/b451/b453 per counts
  verified this round)): all agree (stated literal
  methods, first-hand).
  C guards: singleton `if ((n) == (` 721->723 +2,
  range 840->844 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b453 odds + b448/b450/b452/b454 evens),
  unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-1059-q1059
  memo CONFIRM 45/45 CLEAN (Verifier v600f3.py 45/45
  PASS; tier GATED PORT; w2b-r30 8/8 CAP, cited from
  body read first-hand) +
  A-926-q1059 memo CONFIRM 50/50 CLEAN (Verifier
  v306.py 50/50 PASS; tier GATED PORT; novelty
  gated M-tails 16/16 ALL NEW vs P346T RM col-led
  tails; w2b-r30 8/8 CAP, cited from body read
  first-hand).
  Viewer: NO P347 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P347 (3 DISSENT files on file are
  T10P923/924/926 far-future, withdrawn Qs, checked
  not applicable). Agrees with cport commit msg
  (py/C 20672, PYID 10336).
- Quiz: no conflicting CLAIM/GATE/FLAG on b455/
  2bc8d273 (quiz poll + filename grep first-hand;
  FLAG-937c347 checked: superseded ancient hold,
  unrelated). Newest PARENT-* is QNUM-27 (w2d
  Q-block refill, read) + 081-remount2-resume
  (read); all writer-turf only, no gate impact;
  PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r75/ (build455.log,
  b455-pyid.log, b455-py/c.log, pass455py/c.txt,
  seteq455.py/log, b455-smoke.log, b455-units.log,
  tabaudit455.py/log, values455.py/log, edges455.py/
  log, banddiff = added455.txt, numstat455.txt,
  diffwall in diffwall455.log, build455/ binaries,
  tail-137840 via ct-cache hit, for455-base/new-line,
  pins via vectors/rgram-PINS.csv).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
