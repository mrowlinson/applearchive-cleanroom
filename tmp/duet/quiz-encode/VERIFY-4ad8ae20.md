# VERIFY-4ad8ae20 b422 T10P314 pins 126009..126356 (1872 tiers) PASS

Seat viewer-r63, first-hand, tree422 @4ad8ae20,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r63.
Base 75aa70e6 (b421, 1866 tiers). Band = 49dcf348 (py merge
w2b@881c672c partial, +6 tiers, +64 pins) + 4ad8ae20 (C port,
1872 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117/117).

- Build: make -C src/c BUILDDIR=build422 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc c690cd6667bfc1492 / aae
  d6e27c97ced21673 + sha1 rgramc 1c98959fb1d59af6 / aae
  7d8dd3a2d118e0db (== GATE prefixes; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 9309/9309 covered=9309/9309 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18618/18618 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18618/18618 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18618/18618;
  GATE claims both, both corroborated).
- PINS 18620 rows (2 hdr + 18618, +64 vs base 18556);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq). For-list delta vs base
  +32/-0 (9277->9309):
  126009 126010 126011 126012 126018 126019 126025 126026
  126027 126028 126031 126032 126035 126036 126037 126044
  126053 126060 126069 126079 126080 126085 126092 126100
  126101 126113 126114 126207 126208 126335 126336 126356
  (== GATE list EXACT; decomposition first-hand: 2 sing +
  A6 offs 0,1,7,8,14,15 + C6 offs 0,1,4,5,8,9 + Q10 offs
  0,7,16,23,32,42,43,48,55,63 (head + 8 mids + tail,
  b5-step edge pair off42->43 pinned) + R8 offs 0,12,13,
  106,107,234,235,255 (head/colsplit-pair/edge-pair/
  edge-pair/tail)); 32x2=64 rows, range 126009..126356
  exact. PINS-new-N == for-added 32/32, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60-r63); band
  diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit422.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 142 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-1SIG-88-NOTPB1/QUAD88-4R-STEP/RING-STANDARD-
  COLSPLIT; no F/F0/F1, no QT/RT/TT, no BM/BC, no M19/
  X19, no QB/PT/FM, no M42/X42/H42/L42); C==py 12/12.
  S0 168ch sig 97016d01 sig-eq-P313S0 (32/84 vs P313S0,
  NOT byte-equal) / S1 176ch sig 01000000 NEW-sig
  (59/88 vs P313S1, NOT byte-equal; 29/88 vs own-C10[0]
  assembled, NOT byte-equal; sig NOT-SAME-as-own-C10).
  S1-vs-own-C10 staged per-cell (each cell own lencode)
  [29]x10 TRUE-UNIFORM count+position (cell0 29 @ 0,4,
  9-11,16-31,68-71,84-87 EXACT; positions identical all
  10 staged; sig 01-vs-02 DIVERGE yet uniform pattern
  -- 10th TRUE-uniform case on record, 9th excluding
  unverified P299; beyond GATE's cell0-only claim,
  oracle leg below agrees). AM 16x12ch distinct; AC 80,
  b0-3 16000000 (b0 const 16), no b4/b5, PBA sig
  16000000 x16 PLAIN (NEW sig 16; M6 b20,21,80-83). CM
  10x10ch 10/10 diverge (78e029db6a/78002adb6a/
  78202adb6a/78402adb6a/787f2adb6a/789f2adb6a/
  78bf2adb6a/80c6b23522/80e6b23522/8081730b5c EXACT);
  CC 81, b0-3 02000000 NOT-PB1-sig, no b4/b5 (b5 const
  d8 via lencode; M5 b22,84-87). M 16x12ch distinct
  (QM6 b28,29,80-83, shared NO frags). QR 4x22ch
  4-distinct UNPAIRED (r0 53db210bb393ad70e9aabd fully
  distinct; r123 share 14ch 295d712a13bf8a + tails
  7e308796/33ad7b9b/58ad7b9b EXACT; tails r0,r1,r2,r3
  = 70e9aabd/7e308796/33ad7b9b/58ad7b9b 4/4 distinct;
  r2r3 TRUE-3B ad7b9b differ b84 33/58 + r2r3-lcs3 +
  r0-vs-all lcs0 + r1-vs-all lcs0 programmatic EXACT).
  QC 69, b0-3 2c000000, no b4/b5 (QUAD single-sig x64;
  b27 const in QC, correctly excluded from VPOS). RM
  16x20ch distinct; colsplit 13+3 first-hand (RM[0..12]
  lead 2b, RM[13..15] lead 2c; cols0-12 sig 2b020000
  13x16=208 cells + cols13-15 sig 2c020000 3x16=48
  cells, arith verified); RQ 16x12ch distinct;
  RM-vs-RQ UNPAIRED (sets disjoint); RC 70, NO b0
  (col-led in tab), b1 const 02, b84-87 f4728f80
  ring-wide NEW. M==RQ lists 16/16 string-identical,
  agree pure diagonal (ALL off-diagonal 0/16), RQ
  distinctness 15/2/16/16/15/16 -- even-band
  string-identity BUT byte positions differ (QM6
  b28,29,80-83 vs TR6 b28,29,76-79, re-derived from
  dispatch code both sides; no ordinal per even/odd
  convention; running pattern b414-full/b416-tail/
  b418-full/b420-strdiff/b422-strdiff coherent).
  Tails SPLIT (RM b80-83 by COL c=off&15, RQ b76-79 by
  ROW r=off>>4 -- subscripts verified py+C; 16/16
  distinct each, 0 overlap). Sorted-unique + _N decls
  80/81/69/70 match actual. Missing-sets EXACT: AC
  [4,5,20,21,80-83]; CC [4,5,22,84-87]; QC [4,5,20-26,
  28,29,80-87] (19); RC [0,4,5,11,19,27,28,29,34,35,
  76-83] (18, b0 in tab). VPOS 7/6/19/18 == A-812
  EXACT (PBA M6+b4 / C10 {4,22,84-87} / quad
  b4,b5+QM6+R11 / T b0+TM10+TR6+b4+b5, b5-const
  excluded except quad/T). Coverage unions exact every
  block (const U tab U {b4,b5} == 88 x4, 0 overlap). Q
  legs M[m] + QR[q] both sides, NO F-legs either side.
  R legs RM[c] + RQ[r] both sides, NO F-legs. P313 refs
  re-read: S0 97016d01 / S1 02000000 / PBA 26000000 /
  C10 02000000 / RC 38020000+cbed6982 (1-sig STANDARD).
  Next-P314 preds (banked-from-r63 CONSUMED): PB0
  97016d01 sig-eq 32/84 / PB1 01000000 NEW-sig 59/88 /
  PBA88 16000000 x16 / C10-region 02000000 pay88 x10
  -- x4 corroborated. PBA NEW vs P313 (16000000 !=
  26000000); QUAD single-sig 2c vs P313 2SIG. AM/CM/M/
  QR/RM/RQ 0-overlap vs P313 (widths P314 AM12/CM10/
  M12/QR22/RM20/RQ12 vs P313 AM14/CM12/M12/QR24/RM14/
  RQ12 chars, base widths re-read first-hand). M-tails
  16/16 ALL NEW vs P313M AND vs P313RM-tail8 AND vs
  P313RQ-tail8 (overlap 0 x3; P313 widths M12/RM14/
  RQ12 re-read). AC-QC both=69 sameval=37 (tables
  differ) == GATE EXACT. Memo INCL PBA88 81 / C10 82
  / quad88 69 / T88 70 (A-812 re-read): impl 80/81/69/
  70 = memo-1 on PBA/C10 (b5-const excluded), identical
  quad (b5 step)/T88 (counter) -- standing +1 rule
  coherent, +1/+1/+0/+0. Base temp maxes _t6456/_b3913/
  _i3914 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 126009 / S1 126010 / A 126011-026 / C 126027-036 /
  Q 126037-100 / R 126101-356): bounds + paylens
  (1x84 + 347x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (QUAD-STEP edge off42->43 emerges from
  raw lencode) + R counter b4=(0x2b+2off)&FF b5=0xd9+
  (off>=107)+(off>=235) (py hex 0x2B/0xD9/107/235; C
  staged decimal 43/217, re-derived: 43==0x2b,
  217==0xd9) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A 6B b20,21,
  80-83; C 5B b22,84-87; Q QM6 b28,29,80-83 + R11
  b20-26,84-87, NO frags; R TM10 b0,11,19,27,34,35,
  80-83 by COL + TR6 b28,29,76-79 by ROW, SPLIT tails)
  + C guards `if ((n) == (126009))` / `(126010)` + 4
  range guards exact + C byte-index lists match py per
  block (A 6B, C 5B, Q 6B/11B union 17+b4/b5, R 10B/6B
  union 16+b4/b5). T-mirrors T84454/84459/84464/84479/
  84494/84515 each re-read: hits the exact py guard
  line. Temps _t6457-6472 continuous-16 (base max
  _t6456) + _b3915/3917/3919/3920/3922/3923 (base max
  _b3913) + _i3916/3918/3921/3924 (base max _i3914):
  added-only, no reuse. Insert exact both sides: P313R
  block precedes (py 84452-53, C 225119-21; P3140 at py
  84454, C 225122), at dispatch tail (N-out-of-scope
  follows; 84535 py + 225307 C). Matches A-812 geometry
  (values re-checked in audit above; NO D dips: ownloop
  tags exactly the 6 P314 blocks).
- Edges own-loop ownloop422.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (316 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P314R N=126356
  off=255. edges422.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 73/d8, 75/d8
  == raw lencode) + aform 16/16 (A head 77/d8 tail
  95/d8 b5set {d8} NO step, 0 ff) + cform 10/10 (C
  head 97/d8 tail a9/d8 b5set {d8} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head ab/d8, edge
  off42->43 126079->126080 ff/d8->01/d9, tail 29/d9,
  b5set {d8,d9}, exactly 1 ff in 64 at o42; quad b4
  base 0xab step2 == raw-lencode 64/64); ring counter
  256/256 + ringraw 256/256 (head 2b/d9; colsplit pair
  off12/13 43/d9+45/d9 at 126113/126114 NOT a counter
  edge; 126207 off106 ff/d9 -> 126208 off107 01/da;
  126335 off234 ff/da -> 126336 off235 01/db; tail
  off255 29/db; exactly 2 ff in 256 at o106/o234); ff
  total x3 (Q-step o42 + 2 ring). odd-lencode
  92+256=348/348. Ring edges + quad edge + colsplit
  pair + tail 126356 in for-list + 2 PASS lines each
  py+C. Tail 126356: oracle sha 0ea9f877b521efa6...
  matches PINS (GATE states no tail sha; recorded
  first-hand; rawlen 104 re-checked). py+C CLOSED
  T10P314R off=255 agree. No DISSENT: cut bytes verify.
- PB-diff secf422.py (cache path) + secf422b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (126009 +
  125661 + 126010 + 125662); S0: oracle126009-vs-125661
  32/84, codeS0-vs-P313S0 32/84, positions identical;
  DIRECT tool 32/84 with identical agree-pos 52
  positions. S1: oracle126010-vs-125662 59/88,
  codeS1-vs-P313S1 59/88, positions identical; DIRECT
  59/88 identical agree-pos 29 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf422c.py (oracle C10
  cells n126027-036): 29/88 TRUE-UNIFORM all 10 ([0]
  n126027 29/88 @ 0,4,9-11,16-31,68-71,84-87 == staged
  EXACT; counts [29]x10 AND positions identical all
  10 -- verified beyond GATE's cell0, staged+oracle
  agree; sig 01-vs-02 DIVERGE, NOT byte-equal). P314
  is the 10th TRUE-uniform case on record (9th
  excluding unverified P299). Byte-diff discipline
  observed throughout, nothing to refute.
- C diff pure-add: numstat 608/0 (rgramc.c) + 233/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE;
  raw C 603 content + 5 bare-blank / 0 del == GATE
  EXACT (no whitespace-suspect lines); raw py 233
  content / 0 del. Full-digit norm: C 150/147/149/146
  across the 4 strip/dropempty variants (recorded, no
  GATE claim); py 174 all four variants. C-tempnorm
  del-uniq 0 add-uniq 374 missing 0 == GATE EXACT
  (recipe as stated: temp-norm, empty-excluding).
  del-subset-add 0 missing holds every variant
  (integrity intact). py-tempnorm 192 recorded.
- Wall on band diff added lines (scope 75aa70e6..
  4ad8ae20, 906 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 608/0,
  rgram.py 233/0 purely additive, test_rgram.sh 1/1,
  PINS +64/+0.
- Tiers: merge-msg +6/+64 (49dcf348), code 6 blocks,
  dispatch-guards (4-space dispatch-exact) singletons
  650->652 +2 == GATE EXACT / ranges 686->690 +4 ==
  GATE EXACT, C identical deltas 650->652 +2 /
  686->690 +4 == GATE EXACT (py=C dispatch-exact; no
  else-if either side, deltas agree every side;
  continues b419-646/678 -> b420-648/682 -> b421-650/
  686 sequence), CLOSED T10P prints 1772->1778 +6 both
  sides, seal 1866->1872 +6 (commit msgs; offset +94
  vs CLOSED-T10P: 1872-1778 = 94, stable b401-b422):
  all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-812-q906-P314
  verdict CONFIRM, tallies 30/30 + 18/18 + 14/14 =
  62/62 arith-consistent as-filed + exact-value
  corroboration incl PB0 sig-eq-P313PB0 32/84
  NOT-byte-equal, PB1 NEW-sig 59/88 NOT-byte-equal
  NOT-SAME-as-C10 29/88, PBA88-PLAIN sig-16 M6,
  C10-NOTPB1 M5, QUAD88-4R-STEP + R11 rows + share-14ch
  + r2r3-TRUE-3B + r0+r1-lcs0 + r2r3-lcs3 + QM6 + NO
  frags + b5-step off42->43 + M-tails NEW,
  T88-RING-STANDARD-COLSPLIT + TM10/TR6 16/16 UNPAIRED
  + b0-colsplit-13+3 + tails-split + b84-87 f4728f80 +
  edges + consts 2b/d9/107/235 + lencode 348/348 +
  VPOS 7/6/19/18 (all re-checked above). Sheet-vs-
  tables const-count note: Q-906 sheet rule 81/82/
  69/70 memo-exact (11th straight fully clean w2b
  sheet per memo; w2b-r26 [7/8]), committed tables
  80/81/69/70 still deduct const-b5 in PBA/C10 --
  17th consecutive tables-lag band (geometry exact,
  PORT verdict stands; even sub-sequence b412/b414/
  b416/b418/b420/b422 all tables-lag). No viewer P314
  geometry answer on file at gate time (memo-only
  recon; this VERIFY is the viewer record). No
  CONFIRM-P314.md file (absence verified); A-812
  suffices per rule. Agrees with cport commit msg
  (PYID 9309, RGRAM 18618).
- Quiz: no conflicting CLAIM/GATE/FLAG on b422 (own seat
  CLAIM only; exactly 1 GATE-4ad8ae20; NO-FLAG greps
  first-hand; adjacent-odd-GATE adjacency notes carry
  no b422 verdict). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before
  filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 prose-level note ("second r2r3-pair variant
after b418's 2B, here 3B": b421 carries R12 r2r3-TRUE-3B
(GATE-75aa70e6 filed 14:37, acknowledged in this GATE;
verified first-hand this round) between b418's 2B and
this band -- b422 is the THIRD r2r3-pair band and the
second 3B; the ordinal holds only under even-band scope
(b418 -> b422), unstated, same ordinal-scope class as
the b419/b421 flags; code GREEN since gated artifact ==
verified artifact). Even-band RQ==M string-identity
corroborated (lists-identical pure-diagonal + RQ
distinctness 15/2/16/16/15/16 + byte-positions-differ
QM6-80-83 vs TR6-76-79; no ordinal; memo-silent on the
relation; even/odd convention holds). Next-P315 SHAPE
banked (A-812 re-read: PB0 57a75201 NEW pay84 @126357 /
PB1 02000000 pay88 NEW-sig 50/88 vs P314PB1 @126358 /
PBA88 31000000 x16 @126359-74 / C10-region 02000000
pay88 x10 @126375-84 -- PB1 rotates back 01->02).
