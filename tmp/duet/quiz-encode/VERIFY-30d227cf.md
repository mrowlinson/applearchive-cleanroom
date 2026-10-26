# VERIFY-30d227cf b447 T10P339 pins 134709..135056 (348 pins) PASS

Seat viewer-r69, first-hand, tree @30d227cf,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r69.
Base 2de6d522 (b446 tip, 2016 tiers sealed; this
seat's VERIFY-2de6d522 PASS-filed same round,
base-use only, respected). Band = 1a1af327 (py
merge w2b@68994a7a partial, +6 tiers, +62 pins;
commit msg verified via git log) + 30d227cf (C
port; parent == 1a1af327 verified). Trees via git
archive to TMPDIR tree-sha dirs; tests run from
NVME workdirs (no WT src/__pycache__).

Banked Next-P339 shape (b446 VERIFY: A-896 FWD +
A-1050 Q1 agree) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 ee4a0a06 NEW-sig 29/84
@134709 + PB1 0d000000 NEW 51/88 @134710 +
PBA88 86000000 x16 @134711-726 + C10-region
0d000000 x10 SAME-as-PB1-sig @134727-736
(memo-derived; lane-code verified at CONSUME
time per bank-miss lesson).

- Build: make -C tree/src/c BUILDDIR=$R/build447
  aae rgramc, rc=0, 0 warnings, build447/{aae,
  rgramc}. aae sha256 d6e27c97 (pinned stable
  continues), rgramc sha256 7d89d116 (== GATE).
- RGRAMC-PYID 10094/10094 covered=10094/10094
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, CT_CACHE_DIR default NVME, NVME
  workdir).
- RGRAM py 20188/20188 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 20188/20188 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 20188/20188; cmp447.py; GATE claims
  sorted only, raw corroborated too).
- PINS 20190 lines (2 hdr + 20188, +62 vs base
  20128; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq447.py). For-list
  union delta vs base +31/-0 (10063->10094):
  134709 134710 134711 134712 134718 134719
  134725 134726 134727 134728 134731 134732
  134735 134736 134737 134752 134753 134768
  134769 134783 134784 134785 134792 134800
  134801 134911 134912 134975 135039 135040
  135056 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (134709/10) + A head 134711/12 off0/1 +
  134718/19 off7/8 + tail 134725/26 off14/15
  (6: offs 0,1,7,8,14,15) + C head 134727/28
  off0/1 + 134731/32 off4/5 + tail 134735/36
  off8/9 (6: offs 0,1,4,5,8,9; unsampled offs
  2,3,6,7 = 134729/30/33/34) + Q head 134737
  off0 + boundary pair 134752/53 off15/16 +
  boundary pair 134768/69 off31/32 + B5EDGE
  pair 134783/84 off46/47 + boundary 134785
  off48 + row3-mid 134792 off55 + tail 134800
  off63 (10: offs 0,15,16,31,32,46,47,48,55,63;
  edge-carry @46/47 + off55-mid) + R head
  134801 off0 + edge pair 134911/12 off110/111
  + mid 134975 off174 + edge pair 135039/40
  off238/239 + tail 135056 off255 (7: offs
  0,110/111,174,238/239,255; 1-mid off174 NEW
  shape, both counter edges pair-covered).
  31x2=62 rows, range 134709..135056 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit447.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 127 PASS 0 FAIL first full-green run
  (first file version; asserts derived from
  GATE shape: TAILS4 matrix diag asserted +
  strays printed, no cloned-shape asserts).
  Inventory exactly the 12 both sides, C==py
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42, no RT/TT, no QT). S0
  168ch sig ee4a0a06 NEW-sig (29/84 payload
  diff vs P338S0 @ 0-2,4-8,10,11,13-15,17-19,
  24,56-63,80-83 first-hand incl NEW-sig b0-2,
  NOT byte-equal; differs vs P338 heads
  aefd4106/0c000000-side) / S1 176ch sig
  0d000000 NEW (51/88 payload diff vs P338S1
  @ 0,4,5,8-11,16-43,60-71,84-87 first-hand
  incl sig b0, NOT byte-equal; 25/88 diff vs
  own C10[0] staged cell0 @ 4,19,26,27,34,
  36-47,72-75,84-87; sig SAME-as-own-C10;
  differs vs own PB0), staged as full-payload
  singletons. AM 16/16 16ch distinct, CM 10/10
  8ch distinct, M 16/16 20ch distinct, QR 4/4
  8ch distinct, RM 16/16 16ch distinct, RQ
  16/16 18ch distinct, no QT (R4 b84-87 inside
  QR) + no RT (SPLIT tails) + no F (no frags).
  M-vs-RQ TAILS4-ONLY (M 10B vs RQ 9B: agree
  (6,5),(7,6),(8,7),(9,8) 16/16 each = tails
  b80-83 cross-lane b76-79 position-exact
  monotone (tail-row order preserved); heads
  isolated (same-lanes b46,47 column-disagree
  0-byte: agree[4][3]==agree[5][4]==0; all
  other entries 1-byte max, zero entries >1);
  full-row sets disjoint -- widths differ 10B/
  9B) -- tails STANDARD-split (RM b80-83 by COL
  c=off&15, RQ b76-79 by ROW r=off>>4, 16/16
  distinct each, 0 overlap UNPAIRED). AC 78,
  CC 82, QC 72, RC 69; C _N decls 78/82/72/69
  match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap gap-free,
  mtab/r-tab computed). PBA88-PLAIN-M8b40 sig
  86000000 (b0 const 86, AM 16/16 distinct NO
  pair; M8 b40-43,80-83; b5 const 1c NO step).
  C10-1SIG-88-TAIL-M4 sig 0d000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM
  10/10 diverge 8ch b84-87; CC has no b4/b5, b5
  const 1c full block via lencode). QUAD88-
  1SIG-4R-NOFRAG-B5EDGE 1-sig 86000000 x64
  SAME-sig-as-PBA (b0 const 86 in QC, b1-3
  const 00; b87 NOT const {2b,88} -- b87 not
  in QC table; b5 edge 1c->1d exact @off46/47
  emergent from raw lencode, edge 134783->
  134784 r2c14/c15; b4 base 0xa3 step2 64/64
  contig+2 range a3..ff,01..21; QM10 b30,31,38,
  39,46,47,80-83 M 16/16 shared x3 vs row0 (M
  indexed by col off&15 first-hand) NO frags +
  R4 b84-87 rows 8333612b/a333612b/c333612b/
  f5f75f88 4/4 NO pairing BY-ROW const (QR
  indexed by row off>>4 first-hand); tails =
  full tuples 4/4 distinct, r012 TRUE 3B
  33612b @b85,86,87 (all 48 cells) + r3
  trailing-suffix lcs 0 vs all, TAIL4-substr =
  TSHARE = subseq = 3/3/0/3/0/0 (computed all
  three first-hand; == A-1051 suffix-lcs at all
  3 metrics); b87 NOT const {2b,88}; NO frags).
  Ring STANDARD-split 1-sig: sig 860c0000 x256;
  code-TM8 b52-55,80-83 by COL RM 16/16 + code-
  TR9 b40,41,42,46,47,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79
  row); b0 const 86; b1 const 0c; b84-87 const
  15f85f88 ring-wide NEW.
  VPOS partitions re-derived from code: PBA 9
  (b4+M8; b5 const 1c excluded) / C10 5 (b4+M4;
  b5 const excluded) / quad 16 (b4,b5+QM10+R4;
  b5 edge-varies, in VPOS) / T 19
  (b4,b5+TM8+TR9; b5 counter-varies, in VPOS)
  -- all match A-901/A-1051 (missing sets AC-10
  [4,5,40-43,80-83] / CC-6 [4,5,84-87] / QC-16
  [4,5,30,31,38,39,46,47,80-87] / RC-19
  [4,5,40-42,46,47,52-55,76-83] first-hand
  EXACT; deduct-const-b5 convention uniform
  P335-P339).
  Code-consts vs A-901 INCL (PBA 79 / C10 83 /
  quad 72 / T88 69): impl 78/82/72/69 = writer
  +1/+1/+0/+0 (A b5 const 1c, C b5 const 1c, Q
  b5 EDGE 1c->1d exact, T counter) = 79/83/72/
  69; lane consts = A-901 INCL EXACT (deduct-b5-
  only-when-b5vary rule holds; A-1051 excl
  78/82/72/69 = code EXACT -- no lag on odd
  band). VPOS 9/5/16/19 = memo EXACT.
  M-tails 16/16 ALL NEW vs P338T-COLSIG TM10
  col-led tails (overlap 0; P338T COLSIG frame
  first-hand from code, ref = TM10 col-led 10B
  rows, position-aware tails last-4B) + RQ-tails
  (b76-79) ALL NEW vs P338T TM10 col-led tails
  (overlap 0). AM/CM/M/QR/RM/RQ full-row
  0-overlap vs P338 (all 0/16 printed; widths
  P339 vs P338: AM 8B vs 6B, CM 4B vs 3B, M 10B
  vs 8B, QR 4B vs 4B, RM 8B vs 10B, RQ 9B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 134709 / S1 134710 / A 134711-726 /
  C 134727-736 / Q 134737-800 / R 134801-135056):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C b5 const emerges
  from raw lencode; Q b5 edge emerges from raw
  lencode 64/64) + R explicit counter (b4=(0x23+
  2off)&FF b5=0x1d+(off>=111)+(off>=239); py hex
  0x23/0x1d; C staged literals 35/29, re-derived:
  35==0x23, 29==0x1d) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/rtab byte
  positions exact (A 16ch b40-43,80-83; C 8ch
  b84-87; Q 20/8ch; R 16/18ch). C blocks carry
  T90492/90497/90502/90517/90532/90553 py-line
  mirrors (each re-read: hits the exact py guard
  line, C comment text matches py, all 6
  present; bounds + byte positions exact).
  Insert exact both sides: after T10P338R close
  (C 240664 comment, S0 guard `if ((n) ==
  (134709))`; py guard 90492), at dispatch tail
  (N-out-of-scope fallthrough follows: C 2 scope
  hits, py 2 scope hits per GATE). Matches A-901
  geometry (values re-checked in audit above; NO
  D dips: ownloop tags exactly the 6 P339 blocks).
- Edges own-loop ownloop447.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P339R N=135056 off=255.
  edges447.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  6b/1c, 6d/1c == raw lencode) + aform 16/16 (A
  head 6f/1c tail 8d/1c b5set {1c} NO step, 0
  ff) + cform 10/10 (C head 8f/1c tail a1/1c
  b5set {1c} NO step, 0 ff) + qform 64/64 +
  qb5edge 64/64 (Q head a3/1c, edge off46->47
  (134783->134784) ff/1c->01/1d, tail 21/1d
  @134800; b5set {1c,1d} (1c offs 0-46, 1d offs
  47-63); quad b4=(0xa3+2off) 64/64 contig+2
  range a3..ff,01..21) + ring counter 256/256 +
  ringraw 256/256 (head 23/1d; 134911 off110
  ff/1d -> 134912 off111 01/1e; mid off174 7f/1e
  @134975; 135039 off238 ff/1e -> 135040 off239
  01/1f; tail off255 21/1f @135056; exactly 3 ff
  in 348: Q-edge-ff + 2 ring-edge-ff).
  Odd-lencode 348/348 (346 + S0/S1 embedded b4/
  b5 6b/1c + 6d/1c). Ring edges + mid + tail
  135056 in for-list + 2 PASS lines each py+C.
  Tail 135056: oracle rav sha f497ff1cd6b69de3...
  == PINS (match True; rawlen 104 re-checked);
  py+C CLOSED T10P339R off=255 agree. No
  DISSENT: cut bytes verify.
- PB-diff secf447.py (cache path, 0 miss-warmed
  after ownloop) + secf447b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (134709 +
  134361 + 134710 + 134362); S0: oracle134709-
  vs-134361 29/84, codeS0-vs-P338S0 29/84,
  positions identical (differ-pos 0-2,4-8,10,
  11,13-15,17-19,24,56-63,80-83 listed); DIRECT
  29/84 agree. S1: oracle134710-vs-134362
  51/88, codeS1-vs-P338S1 51/88, positions
  identical (differ-pos 0,4,5,8-11,16-43,60-71,
  84-87 listed); DIRECT 51/88 agree. Triple-
  derived both pairs (same novel shape both
  tiers: 84/84/84/84 + 88/88/88/88). S1-vs-own-
  C10 secf447c.py (oracle C10 cells n134727-
  736): [25]x10 TRUE UNIFORM staged+oracle,
  cells0-9 positions identical (cell0 pos 4,19,
  26,27,34,36-47,72-75,84-87 == staged EXACT;
  sig b0-3 same-sig NOT in diff), sig 0d000000
  both, NOT byte-equal. UNIFORM -- 15th TRUE-
  uniform case in sweep accounting (after P299/
  P303/P307/P311/P315/P317/P319/P323/P325/P329/
  P331/P333/P335/P337); viewer record 27->28.
  FIRST 25-wide uniform (no [25x10] on file;
  NEW-sig S1 + odd band, consistent with the
  novelty/parity rule inferred at P338 -- P338
  SAME-sig/even excluded, P339 NEW/odd
  included; viewer defers to sweep accounting,
  evidence on file). S1 NOT sig-EQ P338C10
  (0d vs 0c DIFFSIG-kept, 42 diff vs P338C10[0]
  first-hand; per cport-r57 lesson (h) nothing
  to assert). Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  231/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw C
  608 total = 603 content + 5 bare-blank / 0
  del (verified bare `+` lines, 0 ws-only;
  GATE states "608 content + 5 blank-only"
  which sums 613 vs numstat 608?? -- first-hand:
  603 content + 5 bare-blank = 608 total ==
  numstat. 10th raw-C overcount-by-5 instance
  (b429/b431/b433/b435/b437/b439/b441/b443/
  b445/b447 odds); rgram.py raw 231 content /
  0 del == GATE; code GREEN since gated artifact
  == verified artifact).
- Wall on band diff added lines (scope 2de6d522..
  30d227cf, 902 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 231/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1922->1928 +6, singletons
  `if n == ` 710->712 +2 (unanchored; 4sp
  700->702 +2) / range-guards `<= n <=` 808->
  812 +4 (unanch and 4sp) = +6 py (== GATE
  deltas 710->712 unanchored; deltas agree
  every literal method; viewer==GATE-tier
  absolutes this odd band, no convention split
  to reconcile) / CLOSED T10P prints 1922->1928
  +6 both sides (seal 2016->2022 +6; offset +94
  vs CLOSED-T10P: 2022-1928 = 94, stable
  b401-b447). All agree (stated literal methods
  first-hand; deltas agree every method;
  5-count C-vs-py singleton offset pre-existing,
  unchanged: 712-707 = 710-705 = 5; C guards:
  singleton `if ((n) == (` 705->707 +2 / range
  808->812 +4; C-closed 1928; no C-only offset
  this window). No elif either side (py elif
  50->50, C else-if 0->0; A/C/Q use raw
  lencode, no counters).
- CONFIRM evidence (CONVERT-01 rule b): A-901-
  q1051 memo CONFIRM 59/59 CLEAN (Verifier
  v287.py 59/59 PASS; tier GATED PORT; novelty
  gated QM10 (n=10) with r012 TRUE 3B tails;
  w2b-r29 8/8 CAP, cited from body read
  first-hand) + A-1051-q1051 memo CONFIRM 45/45
  CLEAN (Verifier v600f3.py 45/45 PASS; tier
  GATED PORT; w2b-r29 8/8 CAP, cited from body
  read first-hand). Agrees with cport commit
  msg (PYID 10094, RGRAM 20188). No viewer
  P339 geometry answer on file at gate time
  (memo-only recon; this VERIFY is the viewer
  record). No DISSENT on P339 (3 DISSENT files
  on file are T10P923/924/926 far-future,
  withdrawn Qs, checked not applicable per
  GATE).
- Quiz: no conflicting CLAIM/GATE/FLAG on b447/
  30d227cf (quiz poll + filename grep first-
  hand; own seat CLAIM only; exactly 1 GATE-
  30d227cf; zero FLAG hits; even base b446
  respected; no future turf touched; CLAIM at
  brief path tmp/duet/). PROSE-01: all hex/
  counts above copied from own run output;
  GATE-30d227cf re-read in FULL before filing
  (1 mild GATE prose note above: raw-C "608
  content + 5 blank" overcounts by 5, substance
  exact).
- RQ==M chain: b447 odd TAILS4-ONLY (M 10B vs
  RQ 9B: agree tails (6,5),(7,6),(8,7),(9,8)
  16/16 each; heads isolated same-lanes b46,47
  0-byte; other strays 1-byte max; full-row
  sets disjoint widths-differ 10B/9B) -- 41st
  odd-band RQ==M instance, 6th TAILS4-ONLY
  degree (viewer chain b435-35th FULL8/b437-36th
  FULL6/b439-37th TAILS4-ONLY/b441-38th 7OF8/
  b443-39th FULL6/b445-40th FULL8-diag/b447-41st
  TAILS4-ONLY sequential; sweep column-agreement
  TAILS4-ONLY + full-row sets disjoint widths-
  differ, twin to a69ef1d1-shape per GATE;
  width predictor REWRITTEN round r57, no width
  rule cited). Viewer-vs-sweep convention
  reconciled first-hand.
- TRUE-uniform chain: b447 UNIFORM [25]x10
  SAMESIG (staged+oracle, positions identical).
  Record 27->28. 15th case, FIRST 25-wide
  uniform (NEW-sig S1 + odd band).
- S-F tables-lag: b447 odd band sheet==code
  (impl 78/82/72/69 vs A-901 INCL 79/83/72/69
  with +1/+1/+0/+0, A-1051 excl EXACT) -- no
  lag on odds (deduct-b5-only-when-b5vary
  holds); even sub-streak stays 18 (b446 last
  even).
- Next-P340 banked (A-901 Q1 + A-1051 Q1 agree,
  for r70/next-viewer to CONSUME FIRST): PB0
  @135057 sig ee4a0a07 NEW-sig (differs 1B vs
  P339PB0; 33/84 vs P339PB0) + PB1 @135058 sig
  0c000000 NEW (43/88 vs P339PB1) + PBA c4000000
  x16 (sig c4) + C10-region 0e000000 x10
  DIFFERS-from-PB1 (memo-derived; lane-code
  verify pending at CONSUME time per bank-miss
  lesson).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 1 mild GATE prose note (raw-C
"608 content + 5 blank" overcounts by 5: first-
hand 603 content + 5 bare-blank = 608 ==
numstat; 10th instance; code GREEN since gated
artifact == verified artifact).
