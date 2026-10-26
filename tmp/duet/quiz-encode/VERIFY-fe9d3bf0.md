# VERIFY-fe9d3bf0 b424 T10P316 pins 126705..127052 (1884 tiers) PASS

Seat viewer-r64, first-hand, tree @fe9d3bf0,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r64.
Base 5321f012 (b423, 1878 tiers). Band = b1e113f1 (py merge
w2b@1b619914 partial, +6 tiers, +74 pins) + fe9d3bf0 (C port,
1884 sealed). Trees manifest-identical to tips (git ls-tree
vs git ls-files identical both, 117/117; the initial find-based
diff also listed pre-existing untracked tmp/scratch-verify/,
my method error, corrected -- tracked files identical).

Banked Next-P316 shape (r63, from A-816) CONSUMED FIRST and
corroborated below: PB0 57a75201 pay84 sig-eq-P315PB0 33/84
@126705 / PB1 02000000 pay88 sig-eq-P315PB1 53/88 @126706 /
PBA88 28000000 x16 @126707-22 / C10-region 02000000 pay88
x10 @126723-32 -- double head repeat, all exact.

- Build: make -C src/c BUILDDIR=build424 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc 216f8d294a7e89f264e877a4654
  caf2bb4fb90f1ea189b707b01669cd9dc0a33 / aae d6e27c97ced2
  1673cc73eee061ffdbd7f0358a87e482056c222a867202110785
  + sha1 rgramc 484080a5ab0f9a2cc813563724bccd830ae620 /
  aae 7d8dd3a2d118e0db8cf84a7d1d3916c77e3c65ac (== GATE
  sha256 both; aae pinned, band touches no aae sources per
  numstat).
- RGRAMC-PYID 9377/9377 covered=9377/9377 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir).
- RGRAM py 18754/18754 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18754/18754 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18754/18754;
  GATE claims sorted only, raw corroborated too).
- PINS 18756 rows (2 hdr + 18754, +74 vs base 18680);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq). For-list delta vs base
  +37/-0 (9340->9377):
  126705 126706 126707 126708 126713 126714 126719 126720
  126721 126722 126723 126724 126727 126728 126731 126732
  126733 126740 126749 126756 126765 126772 126781 126788
  126795 126796 126797 126828 126829 126844 126845 126847
  126848 126900 126975 126976 127052
  (== GATE list EXACT, verified programmatically; for-list
  trap hit once: for-line ends `127052; do` -- fixed with
  split(';')[0], same class as r63 b420). Decomposition
  first-hand from the added set: 2 sing (126705/06) +
  A head/mid/edge/tail pairs (8: 07/08 + 13/14 + edge-pair
  19/20 b5-STEP pinned + 21/22) + C head/mid/tail pairs
  (6) + Q head/7-mids/tail-pair (10, NO step this tier,
  quad b5 const) + R head 126797 / mid-pairs 126828/29 +
  126844/45 / edge-pairs 126847/48 + 126975/76 / mid
  126900 / tail 127052 (11); 37x2=74 rows, range
  126705..127052 exact. PINS-new-N == for-added 37/37,
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked first-hand (`import lz4` Traceback, same as
  r60-r63 record); band diffs touch no proto/ sources
  (numstat proves), NO verdict impact.
- Tables audit own script tabaudit424.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 147 PASS
  0 FAIL. Inventory exactly the 12 both sides, C==py
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F anywhere --
  0 hits both sources; no F0/F1, no QT/RT/TT, no BM/BC,
  no M19/X19, no QB/PT/FM, no M42/X42/H42/L42).
  S0 168ch sig 57a75201 sig-eq-P315S0 (33/84 payload
  diff vs P315S0 first-hand, NOT byte-equal) / S1 176ch
  sig 02000000 sig-eq-P315PB1 (53/88 payload diff vs
  P315S1, NOT byte-equal; 76/88 diff vs own-C10[0]
  assembled, NOT byte-equal; sig SAME-as-own-C10), staged
  as full-payload singletons.
  AM 16/16 16ch distinct (rows vary, NOT sig-carriers --
  sig lives in AC b0-3), AC 78, b0-3 28000000 (b0 const
  28), no b4/b5. C10-1SIG-88-TAIL sig 02000000 x10
  SAME-as-PB1 (sig in CC b0-3 consts; CM 10/10 diverge
  8ch; CC b80-83 const 73fd0265; CC has no b4/b5, b5
  const de full block via lencode). QUAD88-4R single-sig
  2a000000 x64 (QC b0-3; b5 const de full 64, NO step,
  0 ff; b4 base 0x1b step2 64/64 range 1b..99 NO edge;
  QM8 b13,14,15,16,80-83 16/16 distinct NO frags + R10
  b6,7,52-55,84-87 rows r0 99f80c5d1333846906a7 distinct
  vs r123 share-10ch 9f4c6adc58, tails b84-87 4/4
  distinct 846906a7/d3672f03/f8672f03/1d682f03, r1r2
  TRUE-3B 672f03 b84 d3/f8, r3 2B 2f03 (suffix of
  672f03), r0-lcs0 vs all, r1r2-lcs3, r1r3/r2r3-lcs2).
  Ring 3SIG row-led: RQ b0s f1/f1/bb/c9x13 first-hand;
  b1 const 02; b84-87 cae7888d ring-wide NEW (P315
  b1020000/fb2f2a18 single-sig era); TM10
  b12,13,14,15,18,19,80-83 by COL RM 16/16 + TR9
  b0,9,10,11,16,76-79 by ROW RQ 16/16 UNPAIRED
  (tails SPLIT b80-83 col / b76-79 row; subscripts
  verified in dispatch text: M[m] col, RQ[r]/RM[c]
  row/col; M-tail bytes map to pay b80-83, RQ-tail
  bytes to pay b76-79); RM 16/16 20ch + RQ 16/16 18ch
  distinct, sets disjoint; tails per-row 16/16 distinct
  each side.
  S1-vs-own-C10 staged per-cell (each cell own lencode)
  [76]x10 TRUE-UNIFORM count+position (cell0 76 @
  4-55,64-87 EXACT; positions identical all 10 staged;
  sig 02000000 both, NOT byte-equal -- 12th TRUE-uniform
  case on record, 11th excluding unverified P299; high-
  differ character noted: agrees only at 0-3 (sig) +
  56-63; beyond-GATE values corroborated by oracle leg
  below; even-band RQ==M takes no ordinal per viewer
  chain convention).
  M-tails == RQ-tails 16/16 string-equal INTRA-tier BUT
  byte positions differ (QM8 b80-83 col vs TR9 b76-79
  row; M 16ch vs RQ 18ch full strings differ; running
  pattern: b414 full-eq, b416 tail-eq, b418 full-eq,
  b420/b422 string-eq-positions-differ, b424
  tail-eq-positions-differ).
  AC-QC both=66 sameval=24 (tables differ) == GATE EXACT.
  Sorted-unique + _N decls 78/82/68/67 match actual.
  Missing-sets EXACT: AC [4,5,6,7,8,9,80-83] (M8);
  CC [4,5,84-87] (M4); QC [4,5,6,7,13-16,52-55,80-87]
  (R10+QM8, 20); RC [0,4,5,9-16,18,19,76-83] (TR9+TM10,
  21). VPOS 10/5/19/21 == A-819 EXACT (PBA full missing
  10 incl b5-STEP-varies; C10/quad minus b5; T full 21
  incl b0). Coverage unions exact every block
  (const U tab U {b4,b5} == 88 x4, 0 overlap).
  Q legs M[m] + QR[q] both sides, NO F-legs in Q;
  R legs RM[c] + RQ[r] both sides, NO F-legs in R
  (STANDARD RM-col / RQ-row verified in region text).
  P315 refs re-read: S0 57a75201 / S1 02000000 /
  PBA 31000000 / C10 02000000 / QUAD 31000000.
  PBA NEW vs P315 (28000000 != 31000000); QUAD single-sig
  2a vs P315 31. AM/CM/M/QR/RM/RQ 0-overlap vs P315
  (row-counts 16/10/16/4/16/16; string-lens P315
  16/10/14/18/14/14 vs P316 16/8/16/20/20/18, base
  widths re-read first-hand).
  M-tails 16/16 ALL NEW vs P315 (zero overlap vs
  P315M AND vs P315RM-tail8 AND vs P315RQ-tail8 --
  P315 widths M14/RM14/RQ14 re-read). RM-tails NEW vs
  P315RM col-led + RQ-tails NEW vs P315RQ row-led +
  cross overlaps 0 (position-aware col-led/row-led).
  Memo INCL PBA88 78 / C10 83 / quad88 69 / T88 67
  (A-819 re-read): impl 78/82/68/67 = memo-exact on PBA
  (b5 STEP-varies, in tab) and T88 (b5 varies, no
  deduction), writer-1 on C10/quad: impl tables still
  deduct const-b5 on C10/quad (b5 covered by lencode
  instead) while Q-908 sheet counts b5 (memo A-819
  confirms the sheet) -- S-F arithmetic persists in
  committed tables though the sheet is FIXED; geometry
  exact, PORT verdict stands. 19th consecutive
  tables-lag band (b424 pattern +0/+1/+1/+0: PBA exact,
  T88 exact, C10/quad lag; running b412/b414/b416/b418/
  b420/b422/b424 per GATE + r63 record).
  Base temp maxes _t6490/_b3933/_i3934 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 126705 / S1 126706 / A 126707-722 / C 126723-732 /
  Q 126733-796 / R 126797-127052): bounds + paylens
  (1x84 + 347x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5 const de emerges from raw lencode
  everywhere except PBA STEP b5 dd->de @off13, NO step
  elsewhere) + R counter b4=(0x9b+2off)&FF b5=0xde+
  (off>=51)+(off>=179) (py hex 0x9B/0xDE; C staged
  literals 155/222, re-derived: 155==0x9b, 222==0xde)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both sides
  + mtab/rtab byte positions exact (A 8B b6,7,8,9,
  80-83; C 8B b84-87; Q QM8 b13-16,80-83 + R10 b6,7,
  52-55,84-87; R TM10 b12-15,18,19,80-83 by COL + TR9
  b0,9-11,16,76-79 by ROW, SPLIT tails) + C guards
  `if ((n) == (126705))` / `(126706)` + 4 range guards
  exact + C byte-index lists match py per block.
  T-mirrors T84940/84945/84950/84965/84980/85001 each
  re-read: hits the exact py guard line; C mirrors
  identical numbers in comments. Temps _t6491-6506
  continuous-16 (base max _t6490) + _b3935/3937/3939/
  3940/3942/3943 (base max _b3933) + _i3936/3938/3941/
  3944 (base max _i3934): added-only, no reuse.
  Insert exact both sides: after T10P315R close (py
  CLOSED 84938, guard 84940; C 226360-62, block 226363),
  at dispatch tail (N-out-of-scope fallthrough follows:
  py 85022 + C 226553; 2 scope hits py + 2 scope hits
  C). Matches A-819 geometry (values re-checked in
  audit above; NO D dips: ownloop tags exactly the 6
  P316 blocks).
- Edges own-loop ownloop424.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (298 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P316R N=127052
  off=255. edges424.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 e3/dd, e5/dd
  == raw lencode) + aform 16/16 (A head e7/dd tail
  05/de b5set {dd,de} STEP dd->de @off13, exactly 1 ff
  in 16 at 126719) + cform 10/10 (C head 07/de tail
  19/de b5set {de} NO step, 0 ff) + qform 64/64 +
  qb5const 64/64 (Q head 1b/de tail 99/de NO edge,
  b5set {de} NO step, 0 ff; quad b4 base 0x1b step2
  64/64 range 1b..99 NO edge); ring counter 256/256 +
  ringraw 256/256 (head 9b/de; 126847 off50 ff/de ->
  126848 off51 01/df; 126975 off178 ff/df -> 126976
  off179 01/e0; tail 99/e0; exactly 2 ff in 256 at
  o50/o178); ff total x3 (A-edge + 2 ring).
  odd-lencode 92+256=348/348. Q tail 99/de vs R tail
  99/e0 differ in b5 (labeled apart). Ring edges +
  tail 127052 in for-list + 2 PASS lines each py+C.
  Tail 127052: oracle sha 62cc6a52c365096f... matches
  PINS (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P316R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf424.py (cache path) + secf424b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (126705 +
  126357 + 126706 + 126358); S0: oracle126705-vs-126357
  33/84, codeS0-vs-P315S0 33/84, positions identical;
  DIRECT tool 33/84 with identical agree-pos 51
  positions. S1: oracle126706-vs-126358 53/88,
  codeS1-vs-P315S1 53/88, positions identical; DIRECT
  53/88 identical agree-pos 35 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf424c.py (oracle C10
  cells n126723-732): [76]x10 TRUE-UNIFORM counts AND
  positions identical all 10 (cell0 pos 4-55,64-87 ==
  staged EXACT; sig 02000000 both, NOT byte-equal).
  Byte-diff discipline observed throughout, nothing to
  refute.
- C diff pure-add: numstat 608/0 (rgramc.c) + 233/0
  (rgram.py) + 1/1 (for-line) + 74/0 (PINS) == GATE;
  raw C 603 content + 5 bare-blank / 0 del (verified
  bare, no whitespace); full-digit norm ([0-9]+ -> N):
  C del-uniq 0 add-uniq 163/160/162/159 across the 4
  strip/dropempty variants, missing 0 every variant
  (integrity intact); py del-uniq 0 add-uniq 185 all
  four variants, missing 0. C-tempnorm 411 / py-tempnorm
  203 recorded (C-tempnorm del-uniq 0 add-uniq 411
  missing 0 == GATE EXACT).
- Wall on band diff added lines (scope 5321f012..
  fe9d3bf0, 916 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 608/0,
  rgram.py 233/0 purely additive, test_rgram.sh 1/1
  (for-line), PINS +74/+0.
- Tiers: merge-msg +6/+74 (b1e113f1), code 6 blocks,
  dispatch-guards (4-space dispatch-exact) singletons
  654->656 +2 / ranges 694->698 +4 = +6, C identical
  deltas 654->656 +2 / 694->698 +4 (py=C dispatch-exact;
  no else-if either side, deltas agree every side;
  naive unindented greps over-count nested guards --
  stated method resolves it), CLOSED T10P prints
  1784->1790 +6 py + 1784->1790 +6 C (5-count C-vs-py
  offset pre-existing, unchanged: 664-659 = 666-661
  = 5), seal 1878->1884 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1884-1790 = 94, stable b401-b424): all
  agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-819-q908-P316
  verdict CONFIRM 64/64 CLEAN (b1 shape 30/30 + b2
  quad+T 17/17 + b3 counters 17/17; file present,
  counts verified; exact-value corroboration incl
  PB0 sig-eq-P315PB0 33/84 NOT-byte-equal, PB1
  sig-eq-P315PB1 53/88 NOT-byte-equal SAME-as-own-C10
  76/88, PBA88-STEP-M8 sig-28 M8 b5-STEP dd->de @off13,
  C10-TAIL SAME-as-PB1-sig b5-const M4 10/10 diverge
  8ch, QUAD88-4R 1-sig-2a + R10 4/4 UNPAIRED +
  share-10ch + r1r2-TRUE-3B + r3-2B + r0-lcs0 +
  r1r2-lcs3 + r1r3/r2r3-lcs2 + QM8 + NO frags + b5-const
  M-tails NEW, T88-RING-3SIG + TM10/TR9 + row-led-b0 +
  tails-split + b84-87 cae7888d + counter 9b/de/51/179
  + lencode 348/348 (all re-checked above); plus
  sheet-vs-tables const-count note: Q-908 sheet
  78/83/69/67 memo-exact, committed tables 78/82/68/67
  still deduct const-b5 on C10/quad -- 19th consecutive
  tables-lag band, geometry exact, PORT verdict
  stands). Agrees with cport commit msg (PYID 9377,
  RGRAM 18754). No CONFIRM-P316.md file (absence
  verified); A-819 suffices per rule. No viewer P316
  geometry answer on file at gate time (memo-only
  recon; this VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b424 (own seat
  CLAIM only; exactly 1 GATE-fe9d3bf0; zero FLAG hits
  on b424/fe9d3bf0/T10P316/126705; adjacent odds b423/
  b425 GATED PASS by odd seat acknowledged). GATE
  cites QNUM-22 newest -- TRUE at filing time (QNUM-23/
  24/25 postdate it): NO staleness. PROSE-01:
  all hex/counts above copied from own run output;
  GATE re-read in FULL before filing (twice for tiers/
  norms/middle sections).
- RQ==M chain: b424 even TAILS-positions-differ (M-tails
  == RQ-tails 16/16 string-eq, byte positions differ,
  full strings differ; per-M-row vs per-RQ-col
  conventions reconciled first-hand in tabaudit).
  Even band takes no ordinal. Memo-silent on the
  relation (A-819 notes only cell-[0] 76/88). Running
  even pattern now b414-full/b416-tail/b418-full/
  b420-strdiff/b422-strdiff/b424-tail-pos-differ.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 prose-level note ("Inventory exactly the 13
both sides incl F coltab" -- first-hand inventory is
12/12 both sides, 0 F definitions in either source;
the GATE's own substance line "no F (no frag this
tier)" is correct, code GREEN since gated artifact ==
verified artifact). Next-P317 SHAPE banked (A-819
re-read: PB0 57a75201 pay84 sig-eq-P316PB0 31/84 @127053
/ PB1 02000000 pay88 sig-eq-P316PB1 52/88 @127054 /
PBA88 28000000 x16 @127055-70 / C10-region 02000000
pay88 x10 @127071-80 -- triple head repeat).
