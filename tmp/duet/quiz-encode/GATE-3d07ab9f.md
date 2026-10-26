# GATE 3d07ab9f b463 T10P355 pins 140277..140624 (348 pins) PASS-functional

Seat sweep-r77, first-hand, WT tmp/wt-encode-sweep @3d07ab9f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r77.
Band = 4b86c220 (py merge w2b@c20cad6d partial, +6 tiers
+58 pins) + 3d07ab9f (C port). Base 05398fc3 (b462 tip,
2112 tiers sealed).

- Build: make -C src/c BUILDDIR=r77/build463 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build463/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r77, sha256 = b354-b461 pinned
  value, verified this band; band touches no aae
  sources), rgramc
  sha1 274f60d7 / sha256 2b0eaff2.
- RGRAMC-PYID 10568/10568 covered=10568/10568 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR default NVME).
- RGRAM py 21136/21136 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR default NVME).
- RGRAM C 21136/21136 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (21136/21136, sorted).
- PINS-RGRAM cells set-eq 10568/10568 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 21138 lines (2 hdr + 21136 rows, +58 vs base 21080).
  For-list union 10539->10568 +29/-0 (python sets,
  trailing-';' strip, never comm).
  29 = 2 sing (140277 140278) +
  A 6 (head 140279 + 140280 + edge pair 140287/140288 +
  pair 140293/140294 tail; offs 0,1,8,9,14,15; offs
  2-7,10-13 unsampled: 140281-140286, 140289-140292) +
  C 6 (head 140295 + 140296 + 140299 + 140300 +
  140303 + tail 140304; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 140297, 140298, 140301,
  140302) +
  Q 8 (head 140305 + boundary pairs 140320/140321 +
  140336/140337 + 140352/140353 + tail 140368; offs
  0,15,16,31,32,47,48,63; NO mid (b5 const NO edge),
  all boundaries pair-covered, first-hand) +
  R 7 (head 140369 + edge pair 140415/140416 +
  mid 140480 + edge pair 140543/140544 + tail
  140624; offs 0,46/47,111,174/175,255; 1-mid
  shape off111 NEW, both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58
  = 21136-21078.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- UNITS-GREEN rc=0 (22/0: tests/test_units.py synthetic
  shape tests, no oracle).
- Tables audit P355 C-vs-py, 12-table A-PBA88-PLAIN-
  M8b40/C10-1SIG-88-TAIL-M3/QUAD88-1SIG-QM8/R2-NOEDGE+
  T88-RING-STANDARD-split layout, all EXACT:
  S0/S1 const strings EXACT (168/176 hex chars,
  sigs aefa6007 NEW-sig-3B-off / 0f000000 NEW-sig;
  S0 diff vs P354S0 31/84 @ b0-2,4-7,9-11,13-19,
  24,25,56-63,80-83 (sig b0-2 IN diff, b3 same,
  NEW-sig) +
  S1 diff vs P354S1 51/88 @ b0,4,5,8-11,16-43,
  60-71,84-87 (sig b0 IN diff vs P354S1 sig
  0e000000, NEW-sig) +
  S1 diff vs own C10 cells [10x27] TRUE UNIFORM all
  10 (cell @ b4,5,19,26,27,34-47,72-75,84-87; sig
  b0-3 same-sig NOT in diff), NOT byte-equal);
  AM 16/16 (8B), CM 10/10 (3B), M 16/16 (8B),
  QR 4/4 (2B), RM 16/16 (8B), RQ 16/16 (8B)
  EXACT;
  AC 78/78, CC 83/83, QC 76/76, RC 70/70 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 78/83/76/70 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit463.py 452 PASS 0 FAIL).
  NO F/FT tabs (no frags), no F0/F1, no BM/BC
  (C10, not B10), no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM, no RT/TT (ring, not ROWTAIL),
  no QT (R2 carries b84,85 inside QR + b86/b87
  const); table inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-10 [4,5,40,41,
  42,43,80,81,82,83] = b4,b5+M8 (b40-43,80-83);
  CC-5 [4,5,84,85,86] = b4,b5+M3 (b84-86 tails;
  full sig b0-3 in CC = 0f,00,00,00 ->
  0f000000 x10 SAME-as-PB1-sig; b87 const 0x41
  in CC);
  QC-12 [4,5,38,39,46,47,80,81,82,83,84,85] =
  b4,b5+QM8 (b38,39,46,47,80-83)+R2 (b84,85; b0
  const f5 in QC = 1SIG SAME-sig-as-PBA, b1-3
  const 00; b86 const 0x59 + b87 const 0x41
  quad-wide);
  RC-18 [4,5,40,41,46,47,52,53,54,55,76,77,78,
  79,80,81,82,83] = b4,b5+TR8 (b40,41,46,47,
  76-79)+TM8 (b52-55,80-83).
  PLAIN first-hand (M8b40 shape as filed per
  Q-1067/A-942; no FIRST claimed): AC b0..b3 =
  f5,00,00,00 -> sig f5000000 x16, b0 const f5;
  AM 16/16 distinct; b5 0x47+(off>=9) edge
  140287->140288 (A-b5set {71,72} decimal =
  0x47,0x48 first-hand).
  TAIL-M3 first-hand (M3 shape precedented: C10-M3
  on file per A-936 (CM b84-86 + b87 const +
  full sig + b5 const); no FIRST claimed): CC b0-3
  full sig 0f000000 x10 SAME-as-PB1-sig (S1 sig-eq
  own C10); CM 10/10 diverge; b5 const 48 NO edge
  (C-b5set {72} decimal = 0x48 first-hand).
  Code AC78/CC83/QC76/RC70; incl = +0/+1/+1/+0
  (A b5 STEPS 47->48 varies, C b5 const 48,
  Q b5 const 48, T counter) = 78/84/77/70; lane
  consts = A-942 EXCL 78/83/76/70 + rule (+2 for
  the two b5-const lanes; deduct-only-when-vary
  holds, 6th shape: A-steps deduct).
  VPOS 10/4/11/18 derived first-hand (VPOS =
  varying-of-{b4,b5} + mtab + rtab: A 2+8+0
  (b4,b5-step+M8); C 1+3+0 (b4+M3, b5 const);
  Q 1+8+2 (b4+QM8+R2, b5 const); T 2+8+8
  (b4,b5+TM8+TR8)).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3550 n==140277 /
  P3551 n==140278 singleton-const (offs 0/1; 84B/88B);
  P355A 140279..140294 off=n-140279 PBA88-PLAIN-
  M8b40 (m-tab 8B b40-43,80-83, sig f5000000,
  b0 const f5, b5 0x47+(off>=9) edge 140287->
  140288 off8->9);
  P355C 140295..140304 off=n-140295 C10-1SIG-88-
  TAIL-M3 (m-tab 3B b84-86, b87 const 0x41, full
  sig b0-3 in CC = 0f000000, b5 const 48 NO step
  NO edge);
  P355Q 140305..140368 off=n-140305 m=off&15
  q=off>>4 QUAD88-1SIG-QM8/R2-NOEDGE
  1-sig f5000000 x64 SAME-sig-as-PBA (b0 const
  f5 in QC)
  (M 8B b38,39,46,47,80-83 QM8 shared NO frags
  (16 rows x4, m=off&15) + R2 b84,85 r0
  456e / r1 e46e / r2 046f / r3 246f
  exact tuples + b86 const 0x59 + b87 const 0x41
  quad-wide (TAIL4 trailing = TSHARE = subseq =
  3/2/2/2/2/3, all-3 agree first-hand),
  b5 const 48 NO edge, b4 0x23+2off range 23..a1
  contig+2 (no wrap, 64 distinct), NO frags);
  P355R(T88-ring) 140369..140624 off=n-140369
  c=off&15 r=off>>4 STANDARD-split sig 750b0000
  (TM 8B b52-55,80-83 by COL + TR 8B b40,41,46,
  47,76-79 by ROW SPLIT tails UNPAIRED 16/16,
  b0 const 75, b1 const 0b, b84-87 const
  446f5941 ring-wide);
  A/C paylen 88 / raw lencode b4=(0xef+2off) b5
  0x47+(off>=9) (A) / b4=(0x0f+2off) b5 const
  48 (C, const emerges from raw lencode);
  Q paylen 88 / raw lencode b4=(0x23+2off) (b5
  const emerges from raw lencode 64/64);
  R paylen 88 +
  counter b4=(0xa3+2off)&FF b5=0x48+(off>=47)+
  (off>=175).
  C blocks carry T94205/T94210/T94215/T94230/
  T94245/T94265 py-line mirrors (exact); guards
  `if ((n) == (140277))` / `if ((n) == (140278))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; ring counter 163+2*off + 72+(off>=47)+
  (off>=175); temps _t7133.._t7148 appended
  (base max _t7132, 16 contiguous, no reuse);
  _i band 4327,4329,4332,4335 (base max _i4325),
  _b band 4326,4328,4330,4331,4333,4334 (base
  max _b4324), union 4326-4335 contiguous, no
  reuse; C byte-index lists match py per block
  (A 8B, C 3B, Q 8B/2B, R 8B/8B STANDARD
  tails-split); insert position exact (P354R
  block precedes, P355R immediately precedes
  LAST scope-hit; C has 2 scope hits; py has 2
  scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0 456e; r1
  e46e; r2 046f; r3 246f);
  QR full-tail shares: trailing-suffix = TSHARE =
  subseq = 3/2/2/2/2/3 (pairs share b86 const 59
  + b87 const 41; pairs (0,1)/(2,3) trailing 3,
  rest 2) (memo substance confirmed: suffix
  metric EXACT);
  RQ==M 4OF8 (M 8B lanes [38,39,46,47,80-83] vs
  RQ 8B lanes [40,41,46,47,76-79]: heads cols
  0-3 0/16 position-exact each, col-set overlaps
  0/0/0/0 (fully disjoint); tails cols 4-7
  16/16 position-exact each, tail-sets EQUAL
  (col overlaps 15/16/16/14, full); full-row sets
  DISJOINT (intersect 0)) -- 49th odd-band
  RQ==M instance, FIRST 4OF8 degree (no precedent
  on file); ordered per lesson (d) (tails
  position-exact + tail-sets EQUAL + rows
  DISJOINT same-width 8B/8B);
  width predictor dead, never cited;
  tails STANDARD-split (TM b52-55,80-83 by COL
  c=off&15, TR b40,41,46,47,76-79 by ROW
  r=off>>4, 16/16 distinct each, sequences
  UNPAIRED);
  M-tails 16/16 ALL NEW vs P354T RQ row-led tails
  (overlap 0; P354T RQ7 frame first-hand from
  code, ref = RQ7 7B rows, position-aware
  tails last-4B);
  RQ-tails (b76-79) 16/16 ALL NEW vs P354T RM
  (overlap 0; P354T RM9 frame first-hand from
  code);
  S0 string 31/84 NEW-sig-3B-off (b0-2 IN diff,
  b3 same; @ b0-2,4-7,9-11,13-19,24,25,56-63,
  80-83) +
  S1 string 51/88 NEW-sig (sig b0 IN diff vs
  P354S1 sig 0e000000; @ b0,4,5,8-11,16-43,
  60-71,84-87; vs own C10 [10x27] TRUE
  UNIFORM, sig b0-3 same-sig NOT in diff --
  20th TRUE-uniform case) +
  S1 SIG-EQ own C10 (0f000000 both);
  S1 vs P354C10[0] 41/88 (P354C10 sig 0e000000,
  DIFFERS-sig, payload differs);
  P355 actuals (S0 aefa6007/S1 0f000000/PBA88
  f5000000/C10 0f000000 x10 SAME-as-PB1-sig +
  PB0-vs-P354PB0 31/84 NEW-3B-off + PB1-vs-P354PB1
  51/88 NEW-sig) == A-942 + Q-1067 predicted
  next EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head ef/47 (140279)
  edge off8->9 (140287->140288) ff/47->01/48
  tail 0d/48 (140294), b5set {71,72} (decimal =
  0x47,0x48);
  C head 0f/48 (140295) tail 21/48 (140304),
  b5set {72} (decimal = 0x48);
  Q head 23/48 (140305) tail a1/48 (140368),
  b5set {72} (decimal = 0x48) NO edge;
  quad b4=(0x23+2off) 64/64 contig+2 range
  23..a1 + b5 const 64/64;
  T head a3/48 (140369) + off46/47 (140415->
  140416) ff/48->01/49 + mid off111 81/49
  (140480) + off174/175 (140543->140544)
  ff/49->01/4a + tail off255 a1/4a (140624).
  All edge pins in for-list + PASSx2 (batteries
  GREEN); 140624 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  34dbc6ed843e045acae9b632f62c46b62544ec7dc5
  74f57b0f2dad62adb1ae14 matches PINS rawlen 104;
  PASS g-z140624 + g-z140624-closed in BOTH legs,
  sorted cmp-equal).
  Ring counter==raw-lencode 256/256 b4 mismatches
  0 (b5 thresholds 47/175 identical first-hand
  arithmetic, per-off values in edges log);
  quad counter==raw-lencode 64/64 b4 mismatches 0;
  odd-lencode 348/348 first-hand (346 code-path +
  2 singleton-embedded: S0 b4/b5 eb/47 =
  l16(140277), S1 ed/47 = l16(140278)).
  Matches A-942 geometry (framing 1x84+347x88 pay =
  code dispatch 1+1+16+10+64+256 = 348 pins,
  PB0 aefa6007 NEW-3B-off 31/84 + PB1 0f000000
  NEW 51/88 + SAME-as-own-C10 27/88 +
  differs-vs-own-PB0,
  PBA88-PLAIN-M8b40 VPOS 10 b5 edge @8/9,
  C10-1SIG-88-TAIL-M3 VPOS 4 b5 const 48,
  QUAD88-1SIG-QM8/R2-NOEDGE VPOS 11 =
  b4+QM8+R2 (b5 const) + R2 4/4 UNPAIRED exact
  tuples + trailing 3/2/2/2/2/3 + b86/b87 const +
  b5 const NO edge + M-tails ALL NEW 16/16,
  T88-RING-STANDARD-split sig 750b0000 TM8 by COL +
  TR8 by ROW UNPAIRED 16/16 + SPLIT tails +
  b84-87 const 446f5941, ring edges + thresholds
  47/175, NO D dips) + A-942 (suffix-lcs
  3/2/2/2/2/3 = TAIL4 b84-87 all 3 metrics agree
  first-hand; consts excl 78/83/76/70 = lane
  EXACT).
- C diff pure-add: numstat 608/0 rgramc.c + 231/0
  rgram.py (+1/-1 for-line, +58/0 PINS); raw C 608
  content+blank (5 blank-only `+` lines) / 0 del;
  raw py 231 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C+py del-uniq 0 add-uniq 345). Band-level
  sole del = old for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 05398fc3..
  3d07ab9f, 898 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits, aea-invoke 0
  hits (10 `aea' substrings all hex-literal
  fragments, 0 invocations). Files touched:
  rgramc.c 608/0, rgram.py 231/0, test_rgram.sh
  1/1, PINS 58/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 2018->2024 +6, singletons
  `if n == ` 742->744 +2, range-guards `<= n <=`
  872->876 +4, CLOSED T10P prints
  2018->2024 +6, seal 2112->2118
  +6 (cport msgs; offset +94 (base 2112-2018 and
  band 2118-2024 both +94 first-hand; r75-r77
  priors on file)): all agree (stated literal
  methods, first-hand).
  C guards: singleton `if ((n) == (` 737->739 +2,
  range 872->876 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b461 odds + b452-b462 evens),
  unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-942-q1067
  memo CONFIRM 51/51 CLEAN (Verifier v501.py 51/51
  PASS; tier GATED PORT; novelty gated M-tails
  16/16 ALL NEW vs P354T col-led tails; w2b-r31
  8/8 CAP, cited from body read first-hand).
  No 2nd (r6-side) CONFIRM for q1067 on file at gate
  time (filename survey first-hand).
  Viewer: NO P355 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P355 (3 DISSENT files on file are
  T10P923/924/926 far-future, withdrawn Qs, checked
  not applicable); no FLAG names P355/b463/3d07ab9f
  (filename + body-grep survey first-hand). Agrees
  with cport commit msg (py/C 21136, PYID 10568).
- Quiz: no conflicting CLAIM/GATE/FLAG on b463/
  3d07ab9f (quiz poll + filename grep first-hand).
  Newest PARENT-* is QNUM-27 (w2d Q-block refill) +
  081-remount2-resume (both unchanged since r76);
  all writer-turf only, no gate impact; PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r77/ (build463.log,
  b463-pyid.log, b463-py/c.log, pass463py/c.txt,
  seteq463.py/log, b463-smoke.log, b463-units.log,
  tabaudit463.py/log, values463.py/log, edges463.py/
  log, banddiff = added463.txt, numstat463.txt,
  del463.txt, diffwall in shell (wall 0), build463/
  binaries, tail-140624 via ct-cache hit,
  for463-base/new-line, pins via
  vectors/rgram-PINS.csv).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
