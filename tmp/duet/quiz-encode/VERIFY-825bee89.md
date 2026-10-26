# VERIFY-825bee89 b440 T10P332 pins 132273..132620 (348 pins) PASS

Seat viewer-r68, first-hand, tree @825bee89,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r68.
Base a69ef1d1 (b439 tip, 1974 tiers sealed; this
seat's base-use only, respected). Band = bb7f912a (py
merge w2b@9c14a0a4 partial, +6 tiers, +64 pins;
commit msg verified via git log) + 825bee89 (C
port; parent == bb7f912a verified). Trees via git
archive to TMPDIR tree440/tree440base; WT detached
at band for git ops only, returned to
lanes/encode-viewer at round end; tests run from
NVME workdirs (no WT src/__pycache__).

Banked Next-P332 shape (r67 handoff, A-872 +
A-1043 agree) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 6db29604 NEW-sig 35/84
@132273 + PB1 0b000000 NEW-sig 44/88 vs
n131926 @132274 + PBA88 b3000000 x16 @132275-290
+ C10-region 0d000000 x10 @132291-300
DIFFERS-from-PB1-sig (0b-vs-0d) -- staged==oracle
0/0/0/0, sigs exact, counts+positions identical.
Bank-miss lesson applied: no trust without code.

- Build: make -C tree440/src/c BUILDDIR=$R/build440
  aae rgramc, rc=0, 0 warnings (log = mkdir/cc
  echoes only), build440/{aae,rgramc}. aae sha256
  d6e27c97 (pinned stable continues; band touches
  no aae sources), rgramc sha256 aee644f6 (==
  GATE both).
- RGRAMC-PYID 9877/9877 covered=9877/9877 GREEN
  rc=0 (tests/test_rgramc_fast.py, RGRAMC=seat
  binary, CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19754/19754 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 19754/19754 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 19754/19754; cmp440.py; GATE claims
  sorted only, raw corroborated too).
- PINS 19756 rows (2 hdr + 19754, +64 vs base
  19690; +64 = 32 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq440.py). For-list
  union delta vs base +32/-0 (9845->9877):
  132273 132274 132275 132276 132282 132283
  132289 132290 132291 132292 132295 132296
  132299 132300 132301 132317 132332 132333
  132348 132349 132351 132352 132353 132364
  132365 132479 132480 132524 132525 132607
  132608 132620 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (132273/74) + A head pair 275/276 off0/1
  + 282/283 off7/8 + tail pair 289/290 off14/15
  (6: offs 0,1,7,8,14,15) + C head pair
  291/292 off0/1 + 295/296 off4/5 + 299/300
  off8/9 (6) + Q head 301 off0 + 317 off16 +
  pairs 332/333 off31/32 + 348/349 off47/48 +
  B5EDGE pair 351/352 off50/51 + 353 off52 +
  tail 364 off63 (10: offs 0,16,31,32,47,48,
  50,51,52,63) + R head 365 off0 + edge pair
  479/480 off114/115 + sigbnd pair 524/525
  off159/160 + edge pair 607/608 off242/243 +
  tail 620 off255 (8: ROWBND novelty carries the
  extra sig-boundary pair = +32nd pin vs usual
  31). 32x2=64 rows, range 132273..132620 exact.
  PINS-new-N == for-added 32/32, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit440.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 137 PASS 0 FAIL after 1 seat-script fix
  (M-vs-RQ byte-column over-assert: GATE "0/16
  identical" = 0 identical ROWS, sets disjoint
  holds; column matrix recorded exact instead;
  fixed, re-ran). Inventory exactly the 12 both
  sides, C==py (S0/S1/AM/AC/CM/CC/M/QR/QC/
  RM/RQ/RC; no F/FT, no F0/F1, no BM/BC, no M19/
  X19, no QB/PT/FM, no M42/X42/H42/L42, no
  RT/TT, no QT). S0 168ch sig 6db29604 NEW
  (35/84 payload diff vs P331S0 @ 3-5,20-23,
  25-34,36-41,64-75 first-hand incl NEW-sig
  b0-2, NOT byte-equal; differs vs P331 heads
  6db29605/09000000) / S1 176ch sig 0b000000
  NEW (44/88 payload diff vs P331S1 @ 0,4,5,19,
  26,27,34-59,72-79,84-87 first-hand incl sig
  b0, NOT byte-equal; 60/88 diff vs own C10[0]
  staged cell0; sig DIFFERS-from-own-C10
  0b-vs-0d; differs vs own PB0), staged as
  full-payload singletons. AM 16/16 18ch
  distinct (9B), CM 10/10 8ch distinct (4B:
  M4 b84-87), M 16/16 14ch distinct (7B: M9
  b6-10,80-83), QR 4/4 2ch distinct (1B R1
  rows 59/79/99/b9) UNPAIRED, RM 16/16 12ch
  distinct (6B TM6), RQ 16/16 14ch distinct (7B
  TR7) UNPAIRED, no QT (R1 b84 + consts) + no
  RT (ROWBND tails) + no F (no frags). AC 77,
  b0-3 b3000000 (b0 const b3), no b4/b5.
  C10-1SIG-88-DIFFSIG sig 0d000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts;
  CM 10/10 diverge; CC has no b4/b5, b5 const
  09 full block via raw lencode). S1-vs-own-C10
  staged per-cell (M4 b84-87 + b0-3 CC sig +
  b4/b5 lencode, each cell own assembly)
  [60]x10 DIFFSIG, cells0-9 positions identical
  (cell0 @ 0,4,6-55,80-87 first-hand; oracle
  secf440c same vector), sig 0b-vs-0d, NOT
  byte-equal -- NOT uniform (record stays 24).
  QUAD88-1SIG-4R-NOFRAG-B5EDGE-C87 1-sig
  d2000000 x64 DIFFERS-from-PBA-sig b3: QM7
  b13-15,80-83 M 16/16 shared x3 vs row0 (M
  indexed by col off&15 first-hand) NO frags +
  R1 b84 rows 59/79/99/b9 4/4 NO pairing
  BY-ROW const (QR indexed by row off>>4
  first-hand); tails b84-87 = row+33fde9:
  5933fde9/7933fde9/9933fde9/b933fde9, r0123
  TRUE-3B 33fde9 ALL pairs, suffix = subseq =
  substr = 3/3/3/3/3/3 (computed all three
  first-hand; == A-1044 suffix-lcs 3x6); b87
  CONST e9 quad-wide; b0 const d2 in QC (1SIG,
  b5 edge 09->0a @off50/51 exact in VPOS, edge
  132351->132352 r3c2/c3 first-hand); b4 base
  0x9b step2 64/64 contig+2 range 9b..ff,01..19;
  NO frags.
  R legs M[m] + QR[q] both sides, NO F-row leg,
  NO F-scalar leg; Q region m=off&15/q=off>>4.
  P332R(T88-ring 2SIG-ROWBND) 132365..132620
  off=n-132365 sig d20d0000 x160 (off0-159) +
  d30d0000 x96 (off160-255); boundary off159/
  160 = N132524->132525 ROW-9/10 boundary; TM6
  b18,19,80-83 by COL + TR7 b0,10,11,76-79 by
  ROW UNPAIRED SPLIT (tails b80-83 col / b76-79
  row, 16/16 distinct each, 0 overlap
  UNPAIRED); b0 row-led (d2 rows0-9, d3
  rows10-15, RQ first bytes d2 x10 + d3 x6
  first-hand); b1 const 0d ring-wide; b84-87
  const 3bfd54d5 ring-wide NEW; counter b4=
  (0x1b+2off)&FF b5=0x0a+(off>=115)+(off>=243)
  (py hex 0x1b/0x0a; C staged literals 27/10,
  re-derived: 27==0x1b, 10==0x0a; edges
  off114/115 + off242/243 + sigbnd off159/160
  first-hand). R legs RM[c] + RQ[r] both sides,
  NO F anywhere in R. RM 16/16 distinct + RQ
  16/16 distinct.
  M-vs-RQ ROWS-DISJOINT (sets disjoint, 0/16
  identical rows -- GATE "0/16 identical" holds
  at row identity; lanes differ QM7 vs TR7, 0
  overlap; cross-band string-eq pattern b414-
  b438 N/A this tier, FIRST rows-disjoint even
  band; width-equality predictor vacuous: rows
  differ at equal 7B/7B width). Byte-column
  cross-agreement recorded first-hand (NOT row
  order): 3-cycle cols0-2 (M0==RQ1, M1==RQ2,
  M2==RQ0, 16/16 each) + identity cols3-6
  (16/16 each) + noise <=1 elsewhere; viewer-vs-
  sweep convention reconciled (sweep 0/16 =
  rows; columns share bytes permuted).
  Tails STANDARD-split (RM b80-83 by COL
  c=off&15, RQ b76-79 by ROW r=off>>4, 16/16
  distinct each, 0 overlap UNPAIRED); M-tails
  16/16 ALL NEW vs P331M/RM tails (overlap 0).
  S0 string 35/84 differ vs P331S0 (NEW-sig
  incl b0-2) + S1 string 44/88 differ vs P331S1
  (incl sig b0; [60x10] vs own C10 DIFFSIG --
  not a uniform case). P332 actuals (S0
  6db29604/S1 0b000000/PBA88 b3000000/C10
  0d000000 x10 DIFFERS-from-PB1 + PB0-vs-
  P331PB0 35/84 + PB1-vs-P331PB1 44/88) ==
  A-882 predicted next EXACT.
  Missing-sets first-hand EXACT: AC-11
  [4,5,6,7,8,9,10,80-83] = b4,b5+M9 (b5 const
  09 deducted from AC) / CC-6 [4,5,84-87] =
  b4,b5+M4 (full sig b0-3 in CC = 0d,00,00,00
  -> 0d000000 x10 DIFFERS-from-PB1-sig; b5
  const 09 deducted) / QC-10
  [4,5,13,14,15,80,81,82,83,84] = b4,b5+QM7
  (b13-15,80-83)+R1 (b84; b0 const d2 in QC =
  1SIG, b87 CONST e9 quad-wide) / RC-15
  [0,4,5,10,11,18,19,76-83] = b0,b4,b5+TR7
  (b0,10,11,76-79)+TM6 (b18,19,80-83; b0 in
  TR7, counted once). Code AC77/CC82/QC78/RC73;
  incl = +1/+1/+0/+0 (A b5 const 09, C b5 const
  09, Q b5 EDGE 09->0a exact, T counter) =
  78/83/78/73; lane consts = A-882 INCL EXACT
  on quad+T88, PBA/C10 writer-1 (deduct-b5-
  only-when-b5vary holds; A-1044 excl
  77/82/78/73 = code EXACT). AC-QC both=73
  sameval=8 == GATE. Sorted-unique + _N decls
  77/82/78/73 match actual. Coverage unions
  exact every block (const U tab U lencode ==
  88 x4, 0 overlap; each missing == region
  pay-index set minus lencode EXACT all 4).
  Base temp maxes _t6764/_b4094/_i4095 (no
  reuse: band adds _t6765-6780 continuous-16 +
  _i4097/99/4102/4105 + _b4096/98/4100/4101/
  4103/4104, whole-file max _t6780, all above
  base maxes).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 132273 / S1 132274 / A 132275-290 /
  C 132291-300 / Q 132301-364 / R 132365-620):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A b5 const 09, C b5
  const 09, Q b5=09+(off>=51); A/C/Q use raw
  lencode, no counter literals anywhere A/C/Q)
  + R explicit counter (b4=(0x1b+2off)&FF b5=
  0x0a+(off>=115)+(off>=243); py hex 0x1b/0x0a;
  C staged literals 27/10, re-derived:
  27==0x1b, 10==0x0a) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/rtab byte
  positions exact (A 18ch b6-10,80-83; C 8ch
  b84-87; Q 14/2ch; R 12/14ch). C blocks carry
  T88874/88879/88884/88900/88915/88934 py-line
  mirrors (all 6 present, bounds + byte positions
  exact). Insert exact both sides: after T10P331R
  close (py 88855-block then guards 88874+; C
  tables-then-dispatch in band order), at
  dispatch tail (N-out-of-scope fallthrough
  follows). Matches A-882 geometry (values re-
  checked in audit above; NO D dips: ownloop
  tags exactly the 6 P332 blocks).
- Edges own-loop ownloop440.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P332R N=132620 off=255.
  edges440.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  63/09, 65/09 == raw lencode) + aform 16/16 (A
  head 67/09 tail 85/09 b5set {09} NO step, 0
  ff) + cform 10/10 (C head 87/09 tail 99/09
  b5set {09} NO step, 0 ff) + qform 64/64 +
  qb5edge 64/64 (Q head 9b/09 edge off50->51
  132351 ff/09 -> 132352 01/0a tail 19/0a b4
  base 0x9b step2 64/64 contig+2 range
  9b..ff,01..19 b5set {09,0a} (09 offs 0-50,
  0a offs 51-63), exactly 1 ff in 64) + ring
  counter 256/256 + ringraw 256/256 (head
  1b/0a; 132479 off114 ff/0a -> 132480 off115
  01/0b; sigbnd 132524 off159 59/0b ->
  132525 off160 5b/0b; 132607 off242 ff/0b ->
  132608 off243 01/0c; tail off255 19/0c;
  exactly 2 ff in 256). S0/S1 embedded b4/b5
  match raw lencode. Odd-lencode 348/348. Ring
  edges + sigbnd pair + tail 132620 in for-list
  + 2 PASS lines each py+C. Tail 132620:
  oracle rav sha 8ef8bef78e6be0b0... == PINS
  (match True; rawlen 104 re-checked); py+C
  CLOSED T10P332R off=255 agree. No DISSENT:
  cut bytes verify.
- PB-diff secf440.py (cache path, 0 miss-warmed
  after ownloop) + secf440b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (132273 +
  131925 + 132274 + 131926); S0: oracle132273-
  vs-131925 35/84, codeS0-vs-P331S0 35/84,
  positions identical (differ-pos 3-5,20-23,
  25-34,36-41,64-75 listed); DIRECT 35/84
  agree. S1: oracle132274-vs-131926 44/88,
  codeS1-vs-P331S1 44/88, positions identical
  (differ-pos 0,4,5,19,26,27,34-59,72-79,84-87
  listed); DIRECT 44/88 agree. Triple-derived
  both pairs (same novel shape both tiers:
  84/84/84/84 + 88/88/88/88). S1-vs-own-C10
  secf440c.py (oracle C10 cells n132291-300):
  [60]x10 DIFFSIG staged+oracle, cells0-9
  positions identical (cell0 pos 0,4,6-55,80-87
  == staged EXACT), sig 0b-vs-0d, NOT
  byte-equal. NOT uniform -- record stays 24.
  Byte-diff discipline observed throughout.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  232/0 (rgram.py) + 1/1 (for-line) + PINS +64/
  +0 (clean append, 32 Ns x2) == GATE; raw C
  608 total = 603 content + 5 bare-blank / 0
  del (verified bare `+` lines; GATE states
  "603 content + 5 bare-blank" EXACT -- stated
  correctly this band, no overcount). Band-level
  sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope a69ef1d1..
  825bee89): vendor 0 hits, disasm 0 hits,
  depload 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/
  ct-cache 0 hits, shebang 0 hits. Files:
  rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line), PINS
  +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, tier-
  comments `# T10P` 1880->1886 +6, singletons
  `if n == ` 696->698 +2 (unanchored; 4sp
  691->693 +2) / range-guards `<= n <=`
  780->784 +4 (unanch and 4sp 780->784 +4) = +6
  py (== GATE deltas); C guards: singleton `if
  ((n) == (` 691->693 +2 / CLOSED T10P prints
  1880->1886 +6 both sides (seal 1974->1980 +6;
  offset +94 vs CLOSED-T10P: 1980-1886 = 94,
  stable b401-b440). All agree (stated literal
  methods first-hand; deltas agree every method;
  5-count C-vs-py singleton offset pre-existing,
  unchanged: 698-693 = 696-691 = 5; viewer-vs-
  sweep absolute convention reconciled). No
  elif either side (py elif 50->50, C else-if
  0->0; A/C/Q use raw lencode, no counters).
- CONFIRM evidence (CONVERT-01 rule b): A-882-
  q1044 verdict CONFIRM 64/64 CLEAN (own bed
  r3-P332 132273..132652 BAD=0 + own r3-P331,
  verifier v268.py 64/64 PASS; tier GATED PORT;
  novelties FIRST-R1-quad + 2SIG-ROWBND T-ring
  gated; writer CORRECTION none this tier;
  exact-value corroboration incl PB0 NEW-sig
  35/84 + PB1 NEW-sig 44/88 DIFFERS-from-own-
  C10 60/88 + PBA88-PLAIN-M9b6 sig-b3 + C10-
  DIFFSIG + QUAD d2 + R1 59/79/99/b9 + TRUE-3B
  + b87-CONST-e9 + M-tails NEW + T88-ROWBND +
  counter + edges; sheet-vs-tables const-count
  note: Q-1044 sheet 78/83/78/73 memo-exact,
  committed tables 77/82/78/73 still deduct
  const-b5 on PBA/C10 -- S-F arithmetic in
  tables only, geometry exact, PORT stands) +
  A-1044-q1044 verdict CONFIRM 48/48 CLEAN
  (own bed r6-P332 132273..132648 + r6-P331,
  BAD=0 + direct-oracle 2/2 byte-match,
  verifier v600f3.py 48/48 PASS; suffix-lcs
  3x6 + M-tails NEW + b0-row-led-d2/d3 +
  consts excl 77/82/78/73 script-claimed
  corroborated; files present, counts verified;
  tier GATED PORT). Agrees with cport commit
  msg (PYID 9877, RGRAM 19754). No viewer P332
  geometry answer on file at gate time (memo-
  only recon; this VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b440
  (own seat CLAIM only; exactly 1 GATE-825bee89;
  zero FLAG hits; odd base b439 respected;
  b441+ = future turf, untouched, used as
  nothing here). PROSE-01: all hex/counts above
  copied from own run output; GATE-825bee89
  re-read in FULL before filing (no prose slip
  found; raw-C stated correctly).
- RQ==M chain: b440 even ROWS-DISJOINT (M 7B vs
  RQ 7B rows disjoint, 0/16 identical rows;
  byte-columns permuted-agree, not row order).
  FIRST rows-disjoint even-band instance (prior
  evens b436/b438 string-eq-positions-differ;
  odds chain unaffected). Memo-silent on the
  relation; batteries confirm; tier stands.
- TRUE-uniform chain: b440 NOT uniform (S1
  DIFFSIG vs own C10, 60/88). Record stays 24
  (23 excl P299).
- S-F tables-lag: b440 impl 77/82/78/73 vs
  A-882 sheet 78/83/78/73 (PBA/C10 writer-1,
  quad+T88 memo-exact) -- 15th even-band
  running per GATE count (b412..b440); odd-band
  rule (deduct-b5-only-when-b5vary) unaffected.

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; zero prose slips found.
