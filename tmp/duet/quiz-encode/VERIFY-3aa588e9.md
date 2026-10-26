# VERIFY-3aa588e9 b449 T10P341 pins 135405..135752 (348 pins) PASS

Seat viewer-r70, first-hand, tree @3aa588e9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r70.
Base 0065610e (b448 tip, 2028 tiers sealed; this
seat's VERIFY-0065610e PASS-filed same round,
base-use only, respected). Band = 8840ae78 (py
merge w2b@d303d68b partial, +6 tiers, +58 pins;
commit msg verified via git log) + 3aa588e9 (C
port; parent == 8840ae78 verified). Trees via git
archive to TMPDIR tree-sha dirs; tests run from
NVME workdirs (no WT src/__pycache__).

Banked Next-P341 shape (VERIFY-0065610e §Next-
P341: A-914 Q1 + A-1052 Q1 agree) CONSUMED FIRST
and VERIFIED first-hand EXACT: PB0 ee4a0a07
@135405 (S0 head; SAME-as-P340PB0) + PB1
0e000000 @135406 (S1 head; NEW) + PBA ea000000
x16 @135407-422 (AC b0-3 = ea/00/00/00) +
C10-region 0e000000 x10 @135423-432 (CC b0-3 =
0e/00/00/00, SAME-as-PB1-sig) -- all
corroborated against lane code before any
battery step (no bank-miss).

- Build: make -C tree/src/c BUILDDIR=$R/build449
  aae rgramc, rc=0, 0 warnings, build449/{aae,
  rgramc}. aae sha256 d6e27c97... (pinned stable
  continues). rgramc sha256 42c06ee9... == GATE.
- RGRAMC-PYID 10154/10154 covered=10154/10154
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, CT_CACHE_DIR set).
- RGRAM py 20308/20308 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set, NVME workdir).
- RGRAM C 20308/20308 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 20308/20308; cmp449.py; GATE claims
  sorted only, raw corroborated too).
- PINS 20310 lines (2 hdr + 20308, +58 vs base
  20252; +58 = 29 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq449.py GREEN 16/16).
  For-list union delta vs base +29/-0 (10125->
  10154): 135405 135406 135407 135408 135414
  135415 135421 135422 135423 135424 135427
  135428 135431 135432 135433 135448 135449
  135464 135465 135480 135481 135496 135497
  135551 135552 135616 135679 135680 135752 (==
  GATE sampled list EXACT). Decomposition
  first-hand from the added set: 2 sing
  (135405/06) + A head 135407/08 off0/1 + pair
  135414/15 off7/8 + pair 135421/22 off14/15
  (6: offs 0,1,7,8,14,15; offs 2-6,9-13
  unsampled: 135409-413, 135416-420) + C head
  135423/24 off0/1 incl b5-edge + 135427/28
  off4/5 + 135431/32 off8/9 (6: offs 0,1,4,5,
  8,9; unsampled offs 2,3,6,7 = 135425/26/29/
  30) + Q head 135433 off0 + boundary pairs
  135448/49 off15/16 + 135464/65 off31/32 +
  135480/81 off47/48 + tail 135496 off63 (8:
  offs 0,15,16,31,32,47,48,63; NO mid -- b5
  const NO edge; all boundaries pair-covered)
  + R head 135497 off0 + edge pair 135551/52
  off54/55 + mid 135616 off119 + edge pair
  135679/80 off182/183 + tail 135752 off255 (7:
  offs 0,54/55,119,182/183,255; 1-mid off119
  NEW shape, both counter edges pair-covered).
  29x2=58 rows, range 135405..135752 exact.
  PINS-new-N == for-added 29/29, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit449.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 127 PASS 0 FAIL (second file version;
  first version had 3 seat-script bugs, all
  caught by runs, fixed+rerun, see scars;
  asserts derived from GATE shape throughout:
  no cloned-shape asserts). Inventory exactly
  the 12 both sides, C==py (S0/S1/AM/AC/CM/CC/
  M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1, no BM/
  BC, no M19/X19, no M42/X42/H42/L42, no QB/PT/
  FM, no RT/TT, no QT). S0 168ch sig ee4a0a07
  SAME-as-P340PB0 (32/84 diff @ b4-11,34,35,
  41-48,50-55,76-83 first-hand; sig b0-2 NOT
  in diff, SAME-sig kept; NOT byte-equal) / S1
  176ch sig 0e000000 NEW-sig (66/88 diff vs
  P340S1 @ b0,4-27,36-38,40-43,48-55,60-87
  first-hand incl sig b0, NOT byte-equal; vs
  own C10 cells NOT uniform: cell0 26/88 [diff
  @ b4,16-18,22-35,64-67,84-87] + cells1-9
  27/88 [same + b5], split exactly on b5 edge
  21->22; sig b0-3 same-sig NOT in diff;
  15-case TRUE-uniform streak ENDS first-hand;
  NOT byte-equal), staged as full-payload
  singletons. AM 16/16 8B distinct, CM 10/10 3B
  distinct, M 16/16 9B distinct, QR 4/4 4B
  distinct UNPAIRED (rows 56eab883/e0bfb6e2/
  90b0cef2/e675d4f2 exact; r23 trailing-suffix
  lcs 1, all other pairs 0; subseq lcs all 0
  except pair-23 = 1; b87 NOT const {83,e2,f2}
  = {131,226,242}), RM 16/16 7B distinct, RQ
  16/16 9B distinct, no QT (R4 b84-87 inside
  QR) + no RT (STANDARD-split tails) + no F (no
  frags). M-vs-RQ 8OF9 FIRST (M 9B b29-31,34,
  35,80-83 by COL vs RQ 9B b29-31,34,35,76-79
  by ROW; heads agree (29,29),(30,30),(34,34),
  (35,35) 16/16 each; b31 fully disjoint 0/16
  diag + 0 cross; tails (80,76),(81,77),(82,
  78),(83,79) 16/16 position-exact; full-row
  sets DISJOINT, zero full-row strays) -- 42nd
  odd-band RQ==M instance, FIRST 8OF9 degree
  (no 8OF9 on file; sweep column-agreement 8OF9
  + cport full-row DISJOINT same-width 9B/9B
  per lesson (d); width predictor dead, never
  cited). AC 78, CC 83, QC 73, RC 70; C _N
  decls 78/83/73/70 match actual; byte-coverage
  unions exact every block (88/88/88/88, 0
  overlap gap-free, computed). PBA88-PLAIN-
  M8b28 sig ea000000 (b0 const ea via AC b0-3;
  AM 16/16 distinct NO pair; M8 b28-31,80-83;
  A-b5set {0x21} const first-hand). C10-1SIG-
  88-TAIL-M3-B5EDGE sig 0e000000 x10 SAME-as-
  PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 3ch b84-86; CC has no b5, b5 EDGE
  21->22 @off0/1 ff->01 first-hand C-b5set
  {0x21,0x22}; b87 const 83). QUAD88-1SIG-QM9/
  R4-NOEDGE 1-sig f7000000 x64 DIFFERS-from-PBA
  (b0 const f7 in QC, b1-3 const 00; M9 b29-31,
  34,35,80-83 16/16 col-indexed (m = off&15
  both sides) shared-x3-vs-row0 48/48 oracle
  (see sharedx3.py) NO frags + R4 b84-87 rows
  above 4/4 NO pairing BY-ROW const (q = off>>4
  both sides); tails = full tuples 4/4
  distinct, r23 trailing-suffix lcs 1 vs all-0
  rest; b87 NOT const {83,e2,f2}; Q-b5set {0x22}
  const NO edge; b4 base 0x13 step2 64/64
  contig+2 range 13..91; NO frags). Ring
  STANDARD-split: sig 770d0000 x256; code-TM7
  b40,41,42,80-83 by COL RM 16/16 + code-TR9
  b29,30,31,34,35,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79
  row); b0 const 77 (256/256 oracle); b1 const
  0d (256/256 oracle); b84-87 const 25b7e6e7
  ring-wide NEW (256/256 oracle).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - deduct const-b5; b4+M8) / C10 5
  (missing 5 - 0, b5 EDGE-varies in VPOS;
  b4,b5-edge+M3) / quad 14 (missing 15 - 1;
  b4+QM9+R4, b5 const) / T 18 (missing 18 - 0;
  b4,b5+TM7+TR9, b5 counter-varies, in VPOS) --
  all match A-920 (missing sets AC-10 [4,5,
  28-31,80-83] / CC-5 [4,5,84-86] / QC-15 [4,5,
  29-31,34,35,80-87] / RC-18 [4,5,29-31,34,35,
  40-42,76-83] first-hand EXACT;
  deduct-const-b5 convention holds; b5 variance
  checked from oracle bytes: A {21}, C {21,22},
  Q {22}).
  Code-consts vs A-920 INCL (PBA 79 / C10 83 /
  quad 74 / T88 70): impl 78/83/73/70 = writer
  +1/+0/+1/+0 (A b5 const 21 -- in VPOS? no:
  b5 const DEDUCTED so +1; C b5 EDGE varies no
  deduction +0; Q b5 const 22 deducted +1; T
  counter +0) = 79/83/74/70; lane consts =
  A-920 INCL EXACT (deduct-b5-only-when-b5vary
  rule holds; A-1053 excl 78/83/73/70 = code
  EXACT -- no lag on odd band). VPOS 9/5/14/18
  = memo EXACT.
  M-tails 16/16 ALL NEW vs P340T RM col-led
  tails (overlap 0; P340T TM8 frame first-hand
  from code, ref = TM8 col-led 8B rows,
  position-aware tails last-4B) + RQ-tails
  (b76-79) 16/16 ALL NEW vs P340T TR7 row-led
  tails (overlap 0). AM/CM/M/QR/RM/RQ full-row
  0-overlap vs P340 (all 0/16; widths P341 vs
  P340: AM 8B vs 7B, CM 3B vs 4B, M 9B vs 7B,
  QR 4B vs 4B, RM 7B vs 8B, RQ 9B vs 7B).
  S1 SIG-EQ P340C10 (0e000000 both) record-only
  per lesson (h), no assert.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 135405 / S1 135406 / A 135407-422 /
  C 135423-432 / Q 135433-496 / R 135497-752):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C/Q b5 emerges from
  raw lencode; C b5 edge 21->22 emerges @off0/1
  ff->01; Q b5 const 22 emerges 64/64) + R
  explicit counter (b4=(0x93+2off)&FF b5=0x22+
  (off>=55)+(off>=183); py hex 0x93/0x22; C
  staged literals 147/34/55/183 re-derived:
  147==0x93, 34==0x22) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/rtab byte
  positions exact (A 8B b28-31,80-83; C 3B
  b84-86; Q 9B/4B; R 7B/9B STANDARD-split). C
  blocks carry T90956/90961/90966/90981/90996/
  91017 py-line mirrors (each re-read: hits the
  exact py guard line, C comment text matches
  py, all 6 present; bounds + byte positions
  exact). Insert exact both sides: after
  T10P340R close (py guard 90956; C block
  follows T10P340R close), at dispatch tail
  (N-out-of-scope fallthrough follows: C 2 scope
  hits (plateau + dispatch tail), py 2 scope
  hits; early same-text guards at C 163202 / py
  plateau are the n<=1077 check, unrelated
  scope). Matches A-920 geometry (values
  re-checked in audit above; NO D dips:
  ownloop tags exactly the 6 P341 blocks).
- Edges own-loop ownloop449.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P341R N=135752 off=255.
  edges449.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  db/21, dd/21 == raw lencode) + aform 16/16 (A
  head df/21 tail fd/21 b5set {21} NO step, 0
  ff) + cform 10/10 (C head ff/21 edge off0->1
  (135423->135424) ff/21->01/22, tail 11/22
  @135432; b5set {21,22}) + qform 64/64
  (Q head 13/22 tail 91/22 @135496; b5set {22}
  (22 all 64)) + qb5const 64/64 + ring counter
  256/256 + ringraw 256/256 (head 93/22;
  135551 off54/55 ff/22 -> 135552 off55 01/23;
  mid off119 81/23 @135616; 135679 off182/183
  ff/23 -> 135680 off183 01/24; tail off255
  91/24 @135752; exactly 3 ff in 348: C-edge-ff
  + 2 ring-edge-ff; Q/A zero ff) + b0 const 77
  256/256 + b1 const 0d 256/256 + b84-87 const
  25b7e6e7 256/256 (all from oracle bytes
  first-hand). Odd-lencode 348/348 (346 +
  S0/S1 embedded). Ring edges + mid + tail
  135752 in for-list + 2 PASS lines each py+C.
  Tail 135752: oracle rav sha a93e4e8b... ==
  PINS (match True; rawlen 104); py+C CLOSED
  T10P341R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf449.py (cache path, 0 miss-warmed
  after ownloop) + secf449b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (135405 +
  135057 + 135406 + 135058); S0: oracle135405-
  vs-135057 32/84, codeS0-vs-P340S0 32/84,
  positions identical (differ-pos b4-11,34,35,
  41-48,50-55,76-83); DIRECT 32/84 agree. S1:
  oracle135406-vs-135058 66/88, codeS1-vs-
  P340S1 66/88, positions identical; DIRECT
  66/88 agree. Triple-derived both pairs.
  S1-vs-own-C10 secf449c.py (oracle C10 cells
  n135423-432): [26,27x9] NOT uniform,
  cells1-9 diff-pos identical, split exactly on
  b5 (b5 is the ONLY differing position between
  cell0 and cell1 diff-pos sets); sig b0-3
  same-sig 0e NOT in diff. NOT uniform --
  15-case TRUE-uniform streak ENDS first-hand
  (record stays 28). S1 SIG-EQ P340C10
  record-only per lesson (h). Byte-diff
  discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  232/0 (rgram.py) + 1/1 (for-line) + PINS +58/
  +0 (clean append, 29 Ns x2) == GATE; raw band
  899 added = 894 content + 5 bare-blank / 0
  del (verified bare `^+$` lines, 0 ws-only;
  per-file: rgramc.c 603+5=608, rgram.py
  232+0=232, for-line 1, PINS 58). GATE states
  "608 content + 5 blank" (sums 613 vs numstat
  608 -- overcounts by 5: first-hand 603
  content + 5 bare-blank = 608 == numstat;
  11th raw-C overcount-by-5 instance, odds
  pattern b429-b449) + GATE states "raw py 231
  content" vs first-hand 232 == numstat (off by
  one, minor). Code GREEN since gated artifact
  == verified artifact.
- Wall on band diff added lines (scope 0065610e..
  3aa588e9, 899 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/
  ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 232/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks, tier-
  comments `# T10P` 1934->1940 +6, singletons
  (4sp) 704->706 +2 / range-guards 794->798 +4
  = +6, C singletons (4sp) 704->706 +2 / ranges
  816->820 +4 = +6 (deltas agree every side
  every method), CLOSED T10P prints 1934->1940
  +6 both sides, seal 2028->2034 +6 (commit
  msgs; offset +94 vs CLOSED-T10P: 2034-1940 =
  94, stable b401-b449). File-wide singletons
  py 714->716 +2 / C 709->711 +2 (10
  non-dispatch early-tier guards + 5-count
  C-vs-py dip-guard offset, both pre-existing,
  unchanged by band: 716-711 = 714-709 = 5).
  No elif either side (py elif 50->50, C else-if
  0->0; A/C/Q use raw lencode, no counters).
- CONFIRM evidence (CONVERT-01 rule b): A-920-
  q1053-P341 verdict CONFIRM 52/52 CLEAN (own
  beds r4-P341 135405..135780 + r4-P340
  cross-refs, BAD=0, direct-oracle spot 4/4
  byte-match; verifier v306.py 52/52 PASS; tier
  GATED PORT; novelty gated M-tails 16/16 ALL
  NEW vs P340T RM col-led tails; w2b-r30 2/8,
  cited from body read first-hand) +
  A-1053-q1053-P341 verdict CONFIRM 46/46 CLEAN
  (own bed r6-P341 135405..135780, 376 cells +
  r6-P340 cross-refs, BAD=0; verifier v600f3.py
  46/46 PASS; file present, counts verified;
  tier GATED PORT; suffix-lcs 0/0/0/0/0/1 +
  M-tails NEW + STD frame + consts excl
  78/83/73/70 script-claimed corroborated;
  w2b-r30 2/8, cited from body read
  first-hand). Agrees with cport commit msg
  (PYID 10154, RGRAM 20308). No viewer P341
  geometry answer on file at gate time
  (memo-only recon; this VERIFY is the viewer
  record). No DISSENT on P341 (3 DISSENT files
  on file are T10P923/924/926 far-future,
  withdrawn Qs, checked not applicable per
  GATE).
- Quiz: no conflicting CLAIM/GATE/FLAG on b449/
  3aa588e9 (quiz poll + filename grep first-
  hand; own seat CLAIM only; exactly 1 GATE-
  3aa588e9; zero FLAG hits; even base b448
  respected; no future turf touched; CLAIM at
  brief path tmp/duet/). PROSE-01: all hex/
  counts above copied from own run output;
  GATE-3aa588e9 re-read in FULL before filing
  (3 mild GATE prose notes below, substance
  exact).
- RQ==M chain: b449 odd 8OF9 FIRST (M 9B vs RQ
  9B: heads 4x16/16, b31 0-disjoint, tails
  4x16/16 position-exact; full-row sets
  DISJOINT same-width 9B/9B) -- 42nd odd-band
  RQ==M instance, FIRST 8OF9 degree (no 8OF9
  on file; sweep column-agreement 8OF9 +
  full-row DISJOINT same-width per lesson (d);
  viewer-vs-sweep convention reconciled
  first-hand).
- TRUE-uniform chain: b449 NOT uniform (S1 vs
  own C10 [26,27x9], b5-split; 15-case streak
  ENDS). Record stays 28 (15 cases). No
  SAMESIG-same-sig even case arises (b449 is
  odd; P341 S1 is SAME-sig-as-own-C10 but odd
  band -- consistent with the novelty/parity
  rule; dispute NOT re-litigated).
- S-F tables-lag: b449 odd band sheet==code
  (impl 78/83/73/70 == A-1053 excl; incl
  +1/+0/+1/+0 = 79/83/74/70 == A-920 INCL) --
  no lag on odds (deduct-b5-only-when-b5vary
  holds). Even sub-streak stays 37 (b448 last
  even).
- Next-P342 banked (A-920 Q1 + A-1053 Q1 agree,
  for r70-next-band to CONSUME FIRST): PB0
  @135753 sig aec45307 pay84 + PB1 @135754 sig
  0d000000 + PBA a1000000 x16 + C10-region
  0c000000 x10 DIFFERS-from-PB1-sig (memo-
  derived; lane-code verify pending at CONSUME
  time per bank-miss lesson).
- Shared-x3 resolution (chain-level, first-hand
  this band): memo phrase "QM shared x3 16/16
  vs row0 NO frags" (A-920 Q2 + A-1053 Q1;
  same family as A-914 Q2/A-1052 Q1 for P340)
  FORMALIZED as: 3 non-zero q-rows x 16 cells
  share M-lanes with row0 (col-only indexing).
  Verified from oracle bytes: P341-QM9 48/48 +
  P340-QM7 48/48 (sharedx3.py GREEN 96/96) --
  proves col-only indexing + NO frags from
  oracle data, complementing code-text checks.
  Memo phrase family resolved, NOT a slip
  (retroactively corroborates P340 too).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; 3 mild GATE prose notes (temps
_i/_b base-max stale by one band -- actual base
max _i4185/_b4184, band-new _i4187+/_b4186+
fresh contiguous, no reuse; raw py "231" vs
232 == numstat; raw-C overcount-by-5 11th odds
instance: 603 content + 5 bare-blank = 608 ==
numstat). Code GREEN since gated artifact ==
verified artifact. Viewer scars (3 seat-script,
all caught by runs, fixed+rerun): hex-char
widths (bytes vs hex chars); b448-cloned QR-
suffix pattern (observed r23-1-rest-0 exactly
per GATE -- lesson reinforced: novelty-first
bands need GATE-shape-derived asserts, never
cloned-shape asserts); temp scope (band-new vs
band-used); plus 2 cosmetic label slips
(secf449 tree path + diff labels, caught
pre-file).
