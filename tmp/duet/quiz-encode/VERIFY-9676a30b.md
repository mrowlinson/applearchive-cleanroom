# VERIFY-9676a30b b450 T10P342 pins 135753..136100 (348 pins) PASS

Seat viewer-r70, first-hand, tree @9676a30b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r70.
Base 3aa588e9 (b449 tip, 2034 tiers sealed; this
seat's VERIFY-3aa588e9 PASS-filed same round,
base-use only, respected). Band = 165affb1 (py
merge w2b@eb5f1ddc partial, +6 tiers, +62 pins;
commit msg verified via git log) + 9676a30b (C
port; parent == 165affb1 verified). Trees via git
archive to TMPDIR tree-sha dirs; tests run from
NVME workdirs (no WT src/__pycache__).

Banked Next-P342 shape (VERIFY-3aa588e9 §Next-
P342: A-920 Q1 + A-1053 Q1 agree) CONSUMED FIRST
and VERIFIED first-hand EXACT: PB0 aec45307
@135753 (S0 head; NEW-sig NEW family) + PB1
0d000000 @135754 (S1 head; NEW-sig) + PBA
a1000000 x16 @135755-770 (AC b0-3 = a1/00/00/
00) + C10-region 0c000000 x10 @135771-780 (CC
b0-3 = 0c/00/00/00, DIFFERS-from-PB1-sig 0d) --
all corroborated against lane code before any
battery step (no bank-miss).

- Build: make -C tree/src/c BUILDDIR=$R/build450
  aae rgramc, rc=0, 0 warnings, build450/{aae,
  rgramc}. aae sha256 d6e27c97... (pinned stable
  continues). rgramc sha256 318d3816... == GATE.
- RGRAMC-PYID 10185/10185 covered=10185/10185
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, CT_CACHE_DIR set).
- RGRAM py 20370/20370 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set, NVME workdir).
- RGRAM C 20370/20370 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 20370/20370; cmp450.py; GATE claims
  sorted only, raw corroborated too).
- PINS 20372 lines (2 hdr + 20370, +62 vs base
  20310; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq450.py GREEN 16/16).
  For-list union delta vs base +31/-0 (10154->
  10185): 135753 135754 135755 135756 135762
  135763 135769 135770 135771 135772 135775
  135776 135779 135780 135781 135796 135797
  135807 135808 135812 135813 135828 135829
  135844 135845 135935 135936 136000 136063
  136064 136100 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (135753/54) + A head pair 135755/56 off0/
  1 + 135762/63 off7/8 + tail pair 135769/70
  off14/15 (6: offs 0,1,7,8,14,15) + C head
  135771/72 off0/1 + mid pair 135775/76 off4/5
  + tail pair 135779/80 off8/9 (6: offs
  0,1,4,5,8,9) + Q head 135781 off0 + 135796
  off15 + 135797 off16 + edge pair 135807/08
  off26/27 (b5 edge r1c10/c11) + pair 135812/13
  off31/32 + pair 135828/29 off47/48 + tail
  135844 off63 (10: offs 0,15,16,26/27-edge,
  31,32,47,48,63) + R head 135845 off0 + edge
  pair 135935/36 off90/91 + mid 136000 off155 +
  edge pair 136063/64 off218/219 + tail 136100
  off255 (7: offs 0,90/91,155,218/219,255;
  1-mid off155 NEW shape, both counter edges
  pair-covered). 31x2=62 rows, range
  135753..136100 exact. PINS-new-N == for-added
  31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit450.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 125 PASS 0 FAIL (second file version;
  first version had 2 seat-script bugs, both
  caught by runs, fixed+rerun, see scars;
  asserts derived from GATE shape throughout:
  no cloned-shape asserts). Inventory exactly
  the 12 both sides, C==py (S0/S1/AM/AC/CM/CC/
  M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1, no BM/
  BC, no M19/X19, no QB/PT/FM, no M42/X42/H42/
  L42, no RT/TT, no QT). S0 168ch sig aec45307
  NEW-sig NEW family (31/84 payload diff vs
  P341S0 first-hand, NOT byte-equal) / S1 176ch
  sig 0d000000 NEW-sig (49/88 payload diff vs
  P341S1 first-hand, NOT byte-equal; 46/88
  diff vs own C10[0] staged cell0 @ b4-87
  assembled first-hand (CC b0-3 + CM b45,84-87
  + lencode b4/b5); sig DIFFERS-from-own-C10
  (0d vs 0c); differs vs own PB0), staged as
  full-payload singletons. AM 16/16 16ch
  distinct, CM 10/10 10ch distinct, M 16/16 18ch
  distinct, QR 4/4 10ch distinct (R5 rows
  7412049f71/f4c56e46bb/f4e56e46bb/f4056f46bb
  4/4 exact; b45-paired r123 still unequal full
  tuples first-hand), RM 16/16 14ch distinct,
  RQ 16/16 18ch distinct, no QT (R5 b45,84-87
  inside QR) + no RT (ROW-led tails) + no F (no
  frags). M-vs-RQ FULL 16/16 string-identical
  INTRA-tier, SAME-lanes-ordered-identical-but-
  indexed-differ (M QM9 b51-55,80-83 by COL
  off&15 vs RQ9 b51-55,80-83 by ROW off>>4
  first-hand code-text both sides; string-eq
  RETURNS after the b448 lanes-differ break;
  running pattern b442/b444/b446 string-eq,
  b448 break, b450 string-eq again) -- 42nd
  even-band RQ==M instance, FULL degree
  (ordered-identical, diag-16; viewer full-row
  sets+ordered EQUAL, sweep diag-16; twin
  conventions reconcile first-hand). AC 78, CC
  81, QC 72, RC 70; C _N decls 78/81/72/70
  match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap gap-free,
  computed). PBA88-PLAIN-M8b38 sig a1000000 (b0
  const a1, b5 const 24 via raw lencode NOT in
  AC; AM 16/16 distinct NO pair; M8 b38,39,46,
  47,80-83). C10-DIFFSIG-M5b45 sig 0c000000
  x10 DIFFERS-from-PB1-sig (sig in CC b0-3
  consts; CM 10/10 diverge 10ch b45,84-87; CC
  has no b45/b84-87 (all in CM lane) and no b5,
  b5 const 24 full block via lencode). QUAD88-
  1SIG-QM9/R5-B5EDGE 1-sig a1000000 x64 SAME-
  sig-as-PBA (QC b0 const a1; b5 edge 24->25
  @off26/27 in raw lencode emergent, NOT in QC
  const table (deducted, in VPOS); b4 base 0xcb
  step2 64/64 range cb..ff,01..49; QM9 b51-55,
  80-83 16/16 col-indexed (m = off&15 both
  sides) shared-x3-vs-row0 48/48 oracle (see
  sharedx3.py) NO frags + R5 b45,84-87 rows
  above 4/4 NO pairing BY-ROW const (q = off>>4
  both sides; b45-paired r123 still unequal
  full tuples); tails = full tuples 4/4
  distinct, r12 TRUE-3B 6e46bb (b85,86,87 all
  cells, b84 differs c5/e5) + r13/r23
  trailing-suffix lcs=2 (anchored) + r0
  trailing-suffix lcs=0 vs all (tuple
  0/0/0/3/2/2 == A-1054 Q2 at all 3 metrics);
  b87 NOT-const {71,bb}; NO frags). Ring
  SWAPPED: sig 140a0000 x256; code-RM7 b6,7,9,
  76-79 by COL RM 16/16 + code-RQ9 b51-55,
  80-83 by ROW RQ 16/16 UNPAIRED (SWAPPED
  tails b80-83 row / b76-79 col); b0 const 14
  (256/256 oracle); b1 const 0a (256/256
  oracle); b84-87 const 256f46bb ring-wide NEW
  (256/256 oracle); R5 b45-carrying rowband
  (QR[q] at b45,84-87 in Q block).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - deduct const-b5; b4+M8) / C10 6
  (missing 7 - 1; b4+M5) / quad 16 (missing 16
  - 0, b5 edge-varies in VPOS; b4,b5+QM9+R5) /
  T 18 (missing 18 - 0; b0,b1,b4,b5+RM7+RQ9) --
  all match A-921 (missing sets AC-10 [4,5,38,
  39,46,47,80-83] / CC-7 [4,5,45,84-87] / QC-16
  [4,5,45,51-55,80-87] / RC-18 [4,5,6,7,9,51-
  55,76-83] first-hand EXACT;
  deduct-const-b5 convention holds; b5 variance
  checked from oracle bytes first-hand: A {24},
  C {24}, Q {24,25}).
  Code-consts vs A-921 INCL (PBA 79 / C10 82 /
  quad 72 / T88 70): impl 78/81/72/70 =
  writer-1 on PBA/C10 (impl tables still deduct
  const-b5 while sheet counts b5; memo confirms
  the sheet INCL values) = 79/82/72/70; T88
  exact (b5 counter-varies, no deduction).
  38th consecutive even-band S-F tables-lag
  (b412-b450 evens running; GATE sub-count 20th
  even (PBA/C10 lag; quad exact this tier);
  odds sheet==code, no lag on odds).
  Memo-exact every band on edge/counter/var
  tables (in VPOS, no deduction); memos confirm
  sheet values.
  M-tails 16/16 ALL NEW vs P341T RM col-led
  tails (zero overlap vs P341T tails first-hand)
  + RM7-tails (b76-79) 16/16 ALL NEW vs P341T
  RQ row-led tails + RQ9-tails (b80-83 row-led)
  16/16 ALL NEW vs P341T RM col-led tails.
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P341
  (all 0/16; widths P342 vs P341: AM 8B vs 8B,
  CM 5B vs 3B, M 9B vs 9B, QR 5B vs 4B, RM 7B
  vs 7B, RQ 9B vs 9B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 135753 / S1 135754 / A 135755-770 /
  C 135771-780 / Q 135781-844 / R 135845-100):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C b5 const 24 emerges
  from raw lencode; Q b5 edge 24->25 emerges
  64/64) + R explicit counter (b4=(0x4b+2off)&
  FF b5=0x25+(off>=91)+(off>=219); py hex
  0x4b/0x25; C staged literals 75/37/91/219
  re-derived: 75==0x4b, 37==0x25) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides + mtab/
  rtab byte positions exact (A 16ch b38,39,46,
  47,80-83; C 10ch b45,84-87; Q 18ch+10ch b51-
  55,80-83/b45,84-87; R 14ch/18ch SWAPPED:
  RM b6,7,9,76-79 by COL / RQ b51-55,80-83 by
  ROW). C blocks carry T91187/91192/91197/
  91212/91227/91248 py-line mirrors (each
  re-read: hits the exact py guard line, C
  comment text matches py, all 6 present;
  bounds + byte positions exact). Insert exact
  both sides: after T10P341R close (py guard
  91187; C block follows T10P341R close), at
  dispatch tail (N-out-of-scope fallthrough
  follows: C 2 scope hits (plateau + dispatch
  tail), py 2 scope hits; early same-text
  plateau guard unrelated). Matches A-921
  geometry (values re-checked in audit above;
  NO D dips: ownloop tags exactly the 6 P342
  blocks).
- Edges own-loop ownloop450.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P342R N=136100 off=255.
  edges450.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  93/24, 95/24 == raw lencode) + aform 16/16
  (A head 97/24 tail b5/24 b5set {24} NO step,
  0 ff) + cform 10/10 (C head b7/24 tail c9/24
  b5set {24} NO step, 0 ff) + qform 64/64 +
  qb5edge 64/64 (Q head cb/24, edge off26->27
  (135807->135808) ff/24->01/25, tail 49/25
  @135844; b5set {24,25} (24 offs 0-26, 25
  offs 27-63); quad b4=(0xcb+2off) 64/64
  contig+2 range cb..ff,01..49) + ring counter
  256/256 + ringraw 256/256 (head 4b/25;
  135935 off90 ff/25 -> 135936 off91 01/26;
  mid off155 81/26 @136000; 136063 off218
  ff/26 -> 136064 off219 01/27; tail off255
  49/27 @136100; exactly 3 ff in 348: Q-edge-ff
  + 2 ring-edge-ff) + b0 const 14 256/256 + b1
  const 0a 256/256 + b84-87 const 256f46bb
  256/256 (all from oracle bytes first-hand).
  Odd-lencode 348/348 (346 + S0/S1 embedded).
  Ring edges + mid + tail 136100 in for-list +
  2 PASS lines each py+C. Tail 136100: oracle
  rav sha f727e25f... == PINS (match True;
  rawlen 104); py+C CLOSED T10P342R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf450.py (cache path, 0 miss-warmed
  after ownloop) + secf450b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (135753 +
  135405 + 135754 + 135406); S0: oracle135753-
  vs-135405 31/84, codeS0-vs-P341S0 31/84,
  positions identical; DIRECT 31/84 agree. S1:
  oracle135754-vs-135406 49/88, codeS1-vs-
  P341S1 49/88, positions identical; DIRECT
  49/88 agree. Triple-derived both pairs.
  S1-vs-own-C10 secf450c.py (oracle C10 cells
  n135771-780): [46x10] DIFFERS, sig 0d vs 0c;
  NOT uniform -- record stays 28 (15 cases);
  no new SAMESIG-same-sig even case arises
  (P342 S1 is DIFFSIG vs own C10). S1 NOT
  sig-EQ P341C10 (0d vs 0e DIFFSIG-kept; per
  cport-r57 lesson (h) nothing to assert).
  Byte-diff discipline observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  231/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw band
  902 added = 897 content + 5 bare-blank / 0
  del (verified bare `^+$` lines, 0 ws-only;
  per-file: rgramc.c 603+5=608, rgram.py
  231+0=231, for-line 1, PINS 62). GATE states
  the band split correctly -- ZERO prose notes
  (evens-correct per odds-overcount pattern
  b440-b450).
- Wall on band diff added lines (scope 3aa588e9..
  9676a30b, 902 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 231/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1940->1946 +6, dispatch
  singletons (4sp) 706->708 +2 / range-guards
  (4sp) 798->802 +4 = +6, C singletons 706->708
  +2 (4sp; file-wide 709->711 = py-filewide -
  5) / ranges 820->824 +4 = +6, CLOSED T10P
  prints 1940->1946 +6 both sides, seal
  2034->2040 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 2040-1946 = 94, stable
  b401-b450). All agree (stated literal methods
  first-hand; deltas agree every side; 5-count
  C-vs-py singleton offset pre-existing,
  unchanged: file-wide py 714->716 = C 709->711
  + 5). No elif either side (py elif 50->50, C
  else-if 0->0; A/C/Q use raw lencode, no
  counters).
- CONFIRM evidence (CONVERT-01 rule b): A-921-
  q1054-P342 verdict CONFIRM 51/51 CLEAN (own
  beds r4-P342 135753..136128 + r4-P341 cross-
  refs, BAD=0, direct-oracle spot 4/4 byte-match;
  verifier v306.py P342 51/51 PASS; file
  present, counts verified; tier GATED PORT;
  novelties gated SWAPPED T frame (RM7/RQ9) +
  R5 b45-carrying rowband + M-tails 16/16 ALL
  NEW vs P341T; w2b-r30 3/8, cited from body
  read first-hand) + A-1054-q1054-P342 verdict
  CONFIRM 45/45 CLEAN (own bed r6-P342
  135753..136128, 376 cells + r6-P341 cross-
  refs, BAD=0; verifier v600f3.py P342 45/45
  PASS; suffix-lcs 0/0/0/3/2/2 -- corroborated
  first-hand (0,0,0,3,2,2) + M-tails NEW + SWP
  frame + consts excl 78/81/72/70
  script-claimed corroborated; w2b-r30 3/8,
  cited from body read first-hand). Agrees with
  cport commit msg (PYID 10185, RGRAM 20370).
  No viewer P342 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record). No DISSENT on P342 (3 DISSENT
  files on file are T10P923/924/926 far-future,
  withdrawn Qs, checked not applicable per
  GATE).
- Quiz: no conflicting CLAIM/GATE/FLAG on b450/
  9676a30b (quiz poll + filename grep first-
  hand; own seat CLAIM only; exactly 1 GATE-
  9676a30b; zero FLAG hits; odd base b449
  respected; no future turf touched; CLAIM at
  brief path tmp/duet/). PROSE-01: all hex/
  counts above copied from own run output;
  GATE-9676a30b re-read in FULL before filing
  (zero GATE prose notes: raw-C stated
  correctly; temps exact; no slip).
- RQ==M chain: b450 even FULL ordered-identical
  16/16 (M QM9 by COL vs RQ9 by ROW; same lane
  values, different index vars; viewer
  full-row sets+ordered EQUAL, sweep diag-16)
  -- 42nd even-band RQ==M instance, FULL
  degree (string-eq run b442/b444/b446 resumes
  after b448 break; viewer-vs-sweep convention
  reconciled first-hand).
- TRUE-uniform chain: b450 NOT uniform (S1
  DIFFSIG vs own C10, 46/88). Record stays 28
  (15 cases). No SAMESIG-same-sig even case
  arises -- uniform-rule dispute NOT
  re-litigated (P339-15th consumed as banked).
- S-F tables-lag: b450 even band sheet-vs-code
  writer-1 on PBA/C10 (impl 78/81/72/70 vs
  A-921 INCL 79/82/72/70; quad+T exact) --
  38th consecutive even-band lag (b412-b450
  running; GATE sub-count 20th even PBA/C10
  lag; odds sheet==code, no lag on odds).
- Next-P343 banked (A-921 Q1 + A-1054 Q1 agree,
  for r70-next-band to CONSUME FIRST): PB0
  @136101 sig aec4d307 pay84 (1B-off vs
  P342PB0) + PB1 @136102 sig 0f000000 + PBA
  fa000000 x16 + C10-region 0f000000 x10
  SAME-as-PB1-sig (memo-derived; lane-code
  verify pending at CONSUME time per bank-miss
  lesson).
- Shared-x3 resolution (chain-level, extended
  this band): memo phrase "QM shared x3 16/16
  vs row0 NO frags" (A-921 Q2 + A-1054 Q1;
  same family as P340/P341) verified 48/48
  from oracle bytes for P342-QM9 (SHAREDX3
  144/144 GREEN all three tiers) -- proves
  col-only indexing + NO frags from oracle
  data. Memo phrase family resolved, NOT a
  slip.

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; ZERO GATE prose notes
(raw-C stated correctly; temps exact; VPOS
convention confirmed, no slip). Viewer scars (2
seat-script, both caught by runs, fixed+rerun):
QR-b84 slice ([6:8] hex-slice error, observed
c5/e5 at [2:4] per R5 5B layout) + M-vs-RQ
ordered-identical (my "indexed-differ"-as-order
assert wrong; same table values, different
index vars m=off&15 vs r=off>>4).
