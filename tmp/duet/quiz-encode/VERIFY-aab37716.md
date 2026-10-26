# VERIFY-aab37716 b445 T10P337 pins 134013..134360 (348 pins) PASS

Seat viewer-r69, first-hand, tree @aab37716,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r69.
Base 97803743 (b444 tip, 2004 tiers sealed; this
seat's VERIFY-97803743 PASS-filed same round,
base-use only, respected). Band = 7d6a7d43 (py
merge w2b@4f9b6df4 partial, +6 tiers, +62 pins;
commit msg verified via git log) + aab37716 (C
port; parent == 7d6a7d43 verified). Trees via git
archive to TMPDIR tree-sha dirs; tests run from
NVME workdirs (no WT src/__pycache__).

Banked Next-P337 shape (b444 VERIFY: A-895 FWD +
A-1048 Q1 agree) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 aefd4106 NEW-family 32/84
@134013 + PB1 0c000000 NEW 58/88 @134014 +
PBA88 8d000000 x16 @134015-030 + C10-region
0c000000 x10 SAME-as-PB1-sig @134031-040
(memo-derived; lane-code verified at CONSUME
time per bank-miss lesson).

- Build: make -C tree/src/c BUILDDIR=$R/build445
  aae rgramc, rc=0, 0 warnings, build445/{aae,
  rgramc}. aae sha256 d6e27c97 (pinned stable
  continues), rgramc sha256 b7e51fa7 (== GATE).
- RGRAMC-PYID 10032/10032 covered=10032/10032
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, CT_CACHE_DIR default NVME, NVME
  workdir).
- RGRAM py 20064/20064 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 20064/20064 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 20064/20064; cmp445.py; GATE claims
  sorted only, raw corroborated too).
- PINS 20066 lines (2 hdr + 20064, +62 vs base
  20004; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq445.py). For-list
  union delta vs base +31/-0 (10001->10032):
  134013 134014 134015 134016 134022 134023
  134029 134030 134031 134032 134035 134036
  134039 134040 134041 134048 134056 134057
  134072 134073 134088 134089 134096 134104
  134105 134143 134144 134207 134271 134272
  134360 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (134013/14) + A head 134015/16 off0/1 +
  134022/23 off7/8 + tail 134029/30 off14/15
  (6: offs 0,1,7,8,14,15) + C head 134031/32
  off0/1 + 134035/36 off4/5 + tail 134039/40
  off8/9 (6: offs 0,1,4,5,8,9; unsampled offs
  2,3,6,7 = 134033/34/37/38) + Q head 134041
  off0 + row0-mid 134048 off7 + boundary pairs
  134056/57 off15/16 + 134072/73 off31/32 +
  134088/89 off47/48 + row3-mid 134096 off55
  + tail 134104 off63 (10: offs 0,7,15,16,31,
  32,47,48,55,63; dual-mid off7+off55,
  precedented P333) + R head 134105 off0 + edge
  pair 134143/44 off38/39 + mid 134207 off102
  + edge pair 134271/72 off166/167 + tail
  134360 off255 (7: offs 0,38/39,102,166/167,
  255; 1-mid off102 NEW shape, both counter
  edges pair-covered). 31x2=62 rows, range
  134013..134360 exact. PINS-new-N == for-added
  31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit445.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 130 PASS 0 FAIL first full-green run
  (second file version; first run hit 1 cloned-
  shape over-assert M-RQ-NOT-full-identity --
  rows ARE ordered-identical, "NOT full-
  identity" refers to COL-vs-ROW tabs; fixed
  first-hand. Novelty lesson applied again).
  Inventory exactly the 12 both sides, C==py
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42, no RT/TT, no QT). S0
  168ch sig aefd4106 NEW-family (32/84 payload
  diff vs P336S0 @ 0-2,4,5,19-31,36,37,60-71
  first-hand incl NEW-sig b0-2, NOT byte-equal;
  differs vs P336 heads 2e01ac06/0d000000-side)
  / S1 176ch sig 0c000000 NEW (58/88 payload
  diff vs P336S1 @ 0,4,5,19,26-75,84-87 first-
  hand incl sig b0, NOT byte-equal; 43/88 diff
  vs own C10[0] staged cell0 @ 4,5,38,39,45-79,
  84-87; sig SAME-as-own-C10; differs vs own
  PB0), staged as full-payload singletons. AM
  16/16 14ch distinct, CM 10/10 8ch distinct,
  M 16/16 16ch distinct, QR 4/4 6ch distinct,
  RM 16/16 12ch distinct, RQ 16/16 16ch
  distinct, no QT (R3 b84-86 inside QR + b87
  const in QC) + no RT (SPLIT tails) + no F (no
  frags). M==RQ FULL8 16/16 ordered-identical
  INTRA-tier (M-ordered-equal-RQ True; diag-16
  all 8 lanes; symmetric 1-byte coincidental
  strays (3,6,1)/(6,3,1), zero other strays;
  full-row sets EQUAL) -- tabs DIFFER (M[m]
  m=off&15 vs RQ[r] r=off>>4, verified in legs
  + dispatch). AC 79, CC 82, QC 75, RC 72;
  C _N decls 79/82/75/72 match actual; byte-
  coverage unions exact every block (88/88/88/
  88, 0 overlap gap-free, mtab/r-tab computed).
  PBA88-STEP-M7b52 sig 8d000000 (b0 const 8d,
  AM 16/16 distinct NO pair; M7 b52-54,80-83;
  b5 STEP 16->17 @off0/1, in VPOS). C10-1SIG-
  88-TAIL-M4 sig 0c000000 x10 SAME-as-PB1-sig
  (sig in CC b0-3 consts; CM 10/10 diverge 8ch
  b84-87; CC has no b4/b5, b5 const 17 full
  block via lencode). QUAD88-1SIG-4R-NOFRAG-
  C87 1-sig c3000000 x64 (b0 const c3 in QC,
  b1-3 const 00; b87 const d1 quad-wide in QC;
  b5 const 17 NO edge; b4 base 0x33 step2 64/64
  range 33..b1; QM8 b6-9,80-83 M 16/16 shared
  x3 vs row0 (M indexed by col off&15 first-
  hand) NO frags + R3 b84-86 rows 3ed720/
  372e21/572e21/772e21 4/4 NO pairing BY-ROW
  const (QR indexed by row off>>4 first-hand);
  tails = row+const-b87 4/4, r0 TRUE 1B d1 vs
  all + r123 TRUE 3B 2e21d1, TAIL4-substr =
  TSHARE = subseq = 1/1/1/3/3/3 (computed all
  three first-hand; == A-1049 suffix-lcs at all
  3 metrics); b87 CONST d1 quad-wide
  (precedented C87-const, no FIRST claimed);
  NO frags). Ring STANDARD-split 1-sig: sig
  1b0c0000 x256; code-TM6 b13,14,80-83 by COL
  RM 16/16 + code-TR8 b6-9,76-79 by ROW RQ
  16/16 UNPAIRED (SPLIT tails b80-83 col /
  b76-79 row); b0 const 1b; b1 const 0c; b84-87
  const 972e21d1 ring-wide NEW.
  VPOS partitions re-derived from code: PBA 9
  (b4,b5+M7; b5 STEP varies, in VPOS) / C10 5
  (b4+M4; b5 const 17 excluded) / quad 12
  (b4+QM8+R3; b5 const 17 excluded) / T 16
  (b4,b5+TM6+TR8; b5 counter-varies, in VPOS)
  -- all match A-895/A-1049 (missing sets AC-9
  [4,5,52-54,80-83] / CC-6 [4,5,84-87] / QC-13
  [4,5,6-9,80-87] / RC-16 [4,5,6-9,13,14,76-
  83] first-hand EXACT; deduct-const-b5
  convention uniform P335/P336/P337).
  Code-consts vs A-895 INCL (PBA 79 / C10 83 /
  quad 76 / T88 72): impl 79/82/75/72 = writer
  +0/+1/+1/+0 (A b5 STEP varies in VPOS, C b5
  const 17, Q b5 const 17, T counter) = 79/83/
  76/72; lane consts = A-895 INCL EXACT
  (deduct-b5-only-when-b5vary rule holds;
  A-1049 excl 79/82/75/72 = code EXACT -- no
  lag on odd band). VPOS 9/5/12/16 = memo EXACT.
  M-tails 16/16 ALL NEW vs P336T-STANDARD RM
  col-led tails (overlap 0; P336T STANDARD frame
  first-hand from code, ref = RM col-led 8B
  rows, position-aware tails last-4B) + RM-tails
  ALL NEW vs P336T (overlap 0). AM/CM/M/QR/RM/
  RQ full-row 0-overlap vs P336 (all 0/16,
  printed; widths P337 vs P336: AM 7B vs 9B,
  CM 4B vs 4B, M 8B vs 8B, QR 3B vs 4B, RM 6B
  vs 8B, RQ 8B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 134013 / S1 134014 / A 134015-030 /
  C 134031-040 / Q 134041-104 / R 134105-360):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A b5 STEP emerges from
  raw lencode; C b5 const emerges from raw
  lencode; Q b5 const emerges from raw lencode
  64/64) + R explicit counter (b4=(0xb3+2off)
  &FF b5=0x17+(off>=39)+(off>=167); py hex
  0xb3/0x17; C staged literals 179/23, re-
  derived: 179==0xb3, 23==0x17) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 14ch b52-
  54,80-83; C 8ch b84-87; Q 16/6ch; R 12/16ch).
  C blocks carry T90031/90036/90041/90056/
  90071/90090 py-line mirrors (each re-read:
  hits the exact py guard line, C comment text
  matches py, all 6 present; bounds + byte
  positions exact). Insert position exact both
  sides: after T10P336R close (C 239454/239456
  comment/guard, S0 block; py CLOSED 90029,
  return, S0 guard 90031), at dispatch tail
  (N-out-of-scope fallthrough follows: C has 2
  scope hits, py has 2 scope hits per GATE).
  Matches A-895 geometry (values re-checked in
  audit above; NO D dips: ownloop tags exactly
  the 6 P337 blocks).
- Edges own-loop ownloop445.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P337R N=134360 off=255.
  edges445.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  fb/16, fd/16 == raw lencode) + aform 16/16 +
  a5step 16/16 (A head ff/16 STEP->01/17 tail
  1d/17, b5set {16,17}) + cform 10/10 (C head
  1f/17 tail 31/17 b5set {17}) + qform 64/64 +
  qb5const 64/64 (Q head 33/17 tail b1/17 b5set
  {17}; b4 base 0x33 step2 64/64 contig+2 range
  33..b1) + ring counter 256/256 + ringraw
  256/256 (head b3/17; 134143 off38 ff/17 ->
  134144 off39 01/18; mid off102 7f/18 @134207;
  134271 off166 ff/18 -> 134272 off167 01/19;
  tail off255 b1/19; exactly 3 ff in 348: A-
  head-STEP-ff + 2 ring edges). Odd-lencode
  348/348 (346 + S0/S1 embedded b4/b5 fb/16 +
  fd/16). Ring edges + mid + tail 134360 in
  for-list + 2 PASS lines each py+C. Tail
  134360: oracle rav sha f72df124968d743a...
  == PINS (match True; rawlen 104 re-checked);
  py+C CLOSED T10P337R off=255 agree. No
  DISSENT: cut bytes verify.
- PB-diff secf445.py (cache path, 0 miss-warmed
  after ownloop) + secf445b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (134013 +
  133665 + 134014 + 133666); S0: oracle134013-
  vs-133665 32/84, codeS0-vs-P336S0 32/84,
  positions identical (differ-pos 0-2,4,5,19-
  31,36,37,60-71 listed); DIRECT 32/84 agree.
  S1: oracle134014-vs-133666 58/88, codeS1-vs-
  P336S1 58/88, positions identical (differ-pos
  0,4,5,19,26-75,84-87 listed); DIRECT 58/88
  agree. Triple-derived both pairs (same novel
  shape both tiers: 84/84/84/84 + 88/88/88/88).
  S1-vs-own-C10 secf445c.py (oracle C10 cells
  n134031-040): [43]x10 TRUE UNIFORM staged+
  oracle, cells0-9 positions identical (cell0
  pos 4,5,38,39,45-79,84-87 == staged EXACT;
  sig b0-3 same-sig NOT in diff), sig 0c000000
  both, NOT byte-equal. UNIFORM -- 14th TRUE-
  uniform case in sweep accounting (after P299/
  P303/P307/P311/P315/P317/P319/P323/P325/P329/
  P331/P333/P335); viewer record 26->27. FIRST
  43-wide uniform (no [43x10] on file).
  Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  231/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw C
  608 total = 603 content + 5 bare-blank / 0
  del (verified bare `+` lines, 0 ws-only;
  GATE states "608 content + 5 blank-only"
  which sums 613 vs numstat 608?? -- first-hand:
  603 content + 5 bare-blank = 608 total ==
  numstat. 9th raw-C overcount-by-5 instance
  (b429/b431/b433/b435/b437/b439/b441/b443/
  b445); rgram.py raw 231 content / 0 del ==
  GATE; code GREEN since gated artifact ==
  verified artifact).
- Wall on band diff added lines (scope 97803743..
  aab37716, 902 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 231/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1910->1916 +6, singletons
  `if n == ` 706->708 +2, range-guards `<= n <=`
  800->804 +4, CLOSED T10P prints 1910->1916
  +6 both sides, seal 2004->2010 +6 (offset +94
  vs CLOSED-T10P stable b401-b445): all agree
  (stated literal methods first-hand; unanchored
  viewer == GATE-tier absolutes this odd band;
  no convention split to reconcile). C guards:
  singleton `if ((n) == (` 701->703 +2 / range
  800->804 +4; 5-count C-vs-py singleton offset
  pre-existing (same C-only dip guards as b357-
  b445 odds), unchanged by band. No elif either
  side (py elif 50->50, C else-if 0->0; A/C/Q
  use raw lencode, no counters).
- CONFIRM evidence (CONVERT-01 rule b): A-895-
  q1049 memo CONFIRM 59/59 CLEAN (Verifier
  v281.py 59/59 PASS; tier GATED PORT; novelty
  gated b87 CONST d1 quad-wide (R3 tails + const
  b87); exact-value corroboration per GATE;
  w2b-r29 6/8, cited from body read first-hand)
  + A-1049-q1049 memo CONFIRM 46/46 CLEAN
  (Verifier v600f3.py 46/46 PASS; tier GATED
  PORT; suffix-lcs 1/1/1/3/3/3 + M-tails NEW +
  consts excl 79/82/75/72 script-claimed
  corroborated; files present, counts verified;
  tier GATED PORT). Agrees with cport commit msg
  (PYID 10032, RGRAM 20064). No viewer P337
  geometry answer on file at gate time (memo-
  only recon; this VERIFY is the viewer record).
  No DISSENT on P337 (3 DISSENT files on file
  are T10P923/924/926 far-future, withdrawn Qs,
  checked not applicable per GATE).
- Quiz: no conflicting CLAIM/GATE/FLAG on b445/
  aab37716 (quiz poll + filename grep first-
  hand; own seat CLAIM only; exactly 1 GATE;
  b444/b446 EVEN = sweep2 turf, b444 tip used
  as diff-base only, NOT gated). PROSE-01 re-
  read before filing (all hex/counts copied from
  run output above; 1 mild GATE prose note
  above: raw-C "608 content + 5 blank" over-
  counts by 5, substance exact).
- RQ==M chain: b445 odd FULL8-diagonal (M 8B vs
  RQ 8B same-lanes diag-16, +2 one-byte off-
  diagonal strays (3,6):1 (6,3):1; full-row sets
  EQUAL, tabs differ COL-vs-ROW) -- 40th odd-
  band RQ==M instance, 6th FULL8-diagonal
  agreement (viewer chain b435-35th FULL8/b437-
  36th FULL6/b439-37th TAILS4-ONLY/b441-38th
  7OF8/b443-39th FULL6/b445-40th FULL8-diag
  sequential). Viewer-vs-sweep convention
  reconciled first-hand (sweep column-agreement
  FULL8 + same-lanes => ordered per cport-r57
  lesson (d); width predictor REWRITTEN round
  r57, no width rule cited).
- TRUE-uniform chain: b445 UNIFORM [43]x10
  SAMESIG (staged+oracle, positions identical).
  Record 26->27. 14th case, FIRST 43-wide
  uniform.
- S-F tables-lag: b445 odd band sheet==code
  (impl 79/82/75/72 vs A-895 INCL 79/83/76/72
  with +0/+1/+1/+0, A-1049 excl EXACT) -- no lag
  on odds (deduct-b5-only-when-b5vary holds);
  even sub-streak stays 17 (b444 last even).
- Next-P338 FWD (A-895 Q1 + A-1049 Q1 agree, for
  r69 b446 to CONSUME FIRST): PB0 @134361 sig
  aefd4106 SAME-sig + PB1 @134362 sig 0c000000
  sigeq + PBA cd000000 x16 @134363-378 + C10
  0c000000 x10 SAME-as-PB1 @134379-388
  (memo-derived; lane-code verify pending at
  CONSUME time per bank-miss lesson).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 1 mild GATE prose note (raw-C
"608 content + 5 blank" overcounts by 5: first-
hand 603 content + 5 bare-blank = 608 ==
numstat; 9th instance; code GREEN since gated
artifact == verified artifact).
