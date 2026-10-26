# VERIFY-d525fb04 b403 T10P295 pins 119397..119744 (1758 tiers) PASS

Seat viewer-r58, first-hand, tree-d525fb04 @d525fb04,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r58.
Base 84585207 (b402, 1752 tiers). Band = 28d94b61 (py merge
w2b@54679d02 partial, +6 tiers, +62 pins) + d525fb04 (C port,
1758 sealed). Tree manifest-identical to tip (git ls-tree
vs find identical); base tree-84585207 reused (verified
identical at b402).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build403/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 63639da3e0dac5cd / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  5dfa3ebc78119f29 / aae 7d8dd3a2d118e0db (== GATE both).
- RGRAMC-PYID 8717/8717 covered=8717/8717 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17434/17434 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17434/17434 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17434/17434).
- PINS 17436 rows (2 hdr + 17434, +62 vs base 17374);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0 (xor 0 all 4 ways incl py^C). For-list delta vs
  base +31/-0:
  119397 119398 119399 119400 119406 119407 119413 119414
  119415 119416 119419 119420 119423 119424 119425 119432
  119440 119441 119449 119457 119465 119473 119480 119488
  119489 119551 119552 119617 119679 119680 119744
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 119417/119418/
  119421/119422 unsampled; C-STEP edge o8->o9 straddled:
  119423+119424 both pinned) + Q10 offs 0,7,15,16,24,32,
  40,48,55,63 (b5 const, NO step) + R7 offs 0,62/63,128,
  190/191,255 (both counter edges straddled); 8686->8717);
  31x2=62 rows, range 119397..119744 exact. PINS-new-N ==
  for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit403.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 137 PASS
  0 FAIL. Inventory exactly the 13 both sides (PBA88-
  PLAIN/C10-STEP/QUAD88-4R-FRAG/STANDARD ring + single-F
  coltab; no F0/F1, no QT/RT/TT; no BM/BC, no M19/XA19,
  no QB/PT/FM, no M42/X42/H42/L42); C==py 13/13. S0/S1
  168ch sigs 63501000 NEW / f2c7a020 NEW (full-string
  NEW vs BOTH P294 strings; S0-vs-P294S0 30/84 @ b0,1,
  4,5,30-32,34-43,48,56-59,76-83 EXACT + cross-P294S1
  40, S1-vs-P294S1 75/84 EXACT + cross-P294S0 79). AM
  16x14ch distinct; AC 79, b0-3 02/00/00/00 (b0 const
  02), no b4/b5, PBA sig 02000000 x16 PLAIN. CM 10x22ch
  10/10 diverge; CC 71, b0-3 86/c7/a0/20 full-sig in
  consts, no b4/b5 (C10-STEP 86c7a020 x10 SINGLE-sig,
  b5 steps o8->o9 via lencode). M 16x16ch distinct. QR
  4x22ch 4-distinct UNPAIRED; r0 d9183f31c971cc84414a84
  distinct; r123 share 7B 99365f3c05131e (lcpre 7B);
  tails b84-87 84414a84/99a274c5/acc979c5/d1c979c5 4/4
  distinct; r2r3 TRUE 3B c979c5; tail-lcsuf (2,3)=3,
  (1,2)=(1,3)=1, r0-vs-rest 0 (computed first-hand;
  r1 lcs=1). F coltab 16x2ch uniq 11 (03/0b/1b/33/4b/
  73/a3/b3/d3/e3/f3). QC 66, b0-3 02000000, no b4/b5. RM
  16x12ch distinct; RQ 16x16ch distinct; RC 72, b0-3
  20/00/00/00, b84-87 21/e7/42/40 ring-wide. RQ==M
  SUFFIX7 (RQ[1:8]==M[1:8] 16/16, byte0 differs 16/16;
  agree-matrix diagonal bytes 1-7 = 16 x7, RQ0 row all
  0, incidentals (1,0)=(3,5)=(5,3)=(5,7)=(7,5)=1;
  same-pos RM[2:6]==M[4:8] 0/16; full 8x8 matrix
  computed first-hand) -- SUFFIX7 degree NEW, 19th
  odd-band instance. RM-vs-RQ UNPAIRED (sets disjoint).
  Tails STANDARD-SPLIT (RM b80-83 by COL, RQ b76-79 by
  ROW, 16/16 distinct each, 0 overlap). Sorted-unique +
  _N decls 79/71/66/72 match actual. Missing-sets EXACT:
  AC [4,5,13,14,15,80,81,82,83]; CC [4,5,13,14,15,16,17,
  18,19,80,81,82,83]; QC [4,5,8,9,10,11,16,17,18,19,20,
  21,22,23,80,81,82,83,84,85,86,87]; RC [4,5,20,21,22,
  23,28,29,76,77,78,79,80,81,82,83]. Coverage unions
  exact every block (const U tab U {b4,b5} == 88/84/88/
  88, 0 overlap). Q legs M[m] + QR[q] + FRAG F[m]/
  fadd1 both sides. R legs RM[c] + RQ[r] STANDARD. P294
  refs re-read: S0 03291000 / S1 2b8b4e20 / PBA 02000000
  (== P294 preds EXACT). P295 preds (A-741/A-358 Next-
  P295: 63501000/f2c7a020/02000000/86c7a020-STEP) x4
  corroborated. PBA REPEAT vs P294 (02000000 ==
  02000000). QUAD sig REPEAT vs P294 (02000000 ==
  02000000), rows NEW (R11 22ch vs P294 R13 26ch,
  0-overlap). AM/CM/M/QR/RM/RQ 0-overlap vs P294
  (widths differ AM 14ch vs 16ch, CM 22ch vs 26ch, QR
  22ch vs 26ch; M/RM/RQ same width 16/12/16ch,
  0-overlap by content; base widths re-read first-hand;
  P294 has no F tab). M-tails 16/16 ALL NEW vs P294 RQ
  row-led tails + RM-tails (b80-83) ALL NEW vs P294 RQ
  tails + RQ-tails (b76-79) ALL NEW vs P294 RM tails
  (overlap 0 x3) + cross overlaps 0 x3. Memo INCL PBA88
  80 / C10 71 / quad88 67 / T88 72 (A-748 re-read): impl
  79/71/66/72 = memo-1 on PBA/quad (b5-const excluded),
  identical C/T (C-STEP +0 extends the step-+0 rule --
  coherent: memo adds b5 iff single-const). Base temp
  maxes _t6142/_b3732/_i3733 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 119397 / S1 119398 / A 119399-414 / C 119415-424 /
  Q 119425-488 / R 119489-744): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5 const a4 A / step o8->o9 C / const a5
  Q emerge from raw lencode) + R counter b4=(0x83+2off)
  &FF b5=0xa5+(off>=63)+(off>=191) (py hex; C stages
  decimal 131/165, re-derived from code text both sides)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 7B b13-15,80-83; C
  11B b13-19,80-83; Q QM8 b16-19,80-83 + R11 b8-11,20-
  22,84-87 + FRAG b23 coltab F + ADD1 r123==r0+1
  mod256 (q==0 ftab else fadd1, fail-tags ftab/fadd1
  both sides); R TM6 b28,29,80-83 by COL + TR8 b20-23,
  76-79 by ROW). T-mirrors T79951/79956/79961/79976/
  79992/80018 each re-read: hits the exact py guard
  line. C guards `if ((n) == (119397))` / `(119398)` +
  4 range guards exact. C byte-index lists match py per
  block (A 7B, C 11B, Q 8B/11B/1B, R 6/8B). Temps
  _t6143-6160 continuous (base max _t6142) + _b3724/
  3726/3728/3729/3731/3732 (base max _b3722) + _i3725/
  3727/3730/3733 (base max _i3723): base-tree zero refs
  to new temps prove no reuse. Insert exact both sides:
  after T10P294R close,
  at dispatch tail (N-out-of-scope fallthrough follows;
  C 2 scope hits, py 2 scope hits). Matches A-748/A-359
  geometry (values re-checked in audit above; NO D dips:
  ownloop tags exactly the 6 P295 blocks).
- Edges own-loop ownloop403.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P295R N=119744 off=255.
  edges403.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 cb/a4, cd/a4 == raw lencode) +
  aform 16/16 (A 88B head cf/a4 tail ed/a4 b5set {a4} NO
  step, 0 ff) + cform 10/10 + cb5step 10/10 (C head ef/
  a4 b5set {a4,a5} step o8->o9: 119423 o8 ff/a4 ->
  119424 o9 01/a5, exactly 1 ff in 10 at o8; C tail =
  01/a5 last cell) + qform 64/64 + qb5const 64/64 (Q
  head 03/a5 tail 81/a5 b5set {a5} NO step, 0 ff in 64;
  quad b4 formula == raw-lencode 64/64); ring counter
  256/256 + ringraw 256/256 (head 83/a5; 119551 off62
  ff/a5 -> 119552 off63 01/a6; mid off128 83/a6; 119679
  off190 ff/a6 -> 119680 off191 01/a7; tail off255 81/
  a7; exactly 2 ff in 256 at o62/o190; Q tail 81/a5 vs
  R tail 81/a7 differ in b5 -- labeled apart); odd-
  lencode 348/348. FRAG frag403.py: ftab 16/16 + ADD1
  48/48 over Q oracle bytes (== memo 48/48 first-hand).
  Ring edges + C-STEP edge + tail 119744 in for-list +
  2 PASS lines each py+C. Tail 119744: oracle sha
  8f62b763efd890f1... matches PINS; py+C CLOSED T10P295R
  off=255 agree. No DISSENT: cut bytes verify.
- PB-diff secf403.py (cache path) + secf403b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (119397 +
  119049 + 119398 + 119050); S0: oracle119397-vs-119049
  30/84, codeS0-vs-P294S0 30/84, positions identical;
  DIRECT tool 30/84 with identical agree-pos 54
  positions. S1: oracle 75/84, code 75/84, positions
  identical; DIRECT 75/84 identical agree-pos 9
  positions (b3,6,20,32,33,52-55). 0 miss (ownloop
  pre-warmed). Twice-derived both pairs. No byte-equal
  wording in A-748/A-359 P295-own geometry (both stage
  NEW sigs); A-748 Next-P296 sig-eq pairs explicitly
  settled NOT-byte-equal (31/84 + 46/84 first-hand) --
  byte-diff discipline observed, nothing to refute.
- C diff pure-add: numstat 634/0 (rgramc.c) + 253/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 629 content + 5 bare-blank / 0 del; raw py 253
  content / 0 del. Full-digit norm ([0-9]+ -> N, keep-
  empty): del-uniq 0 add-uniq 183 C / 201 py == GATE
  EXACT (first-hand, no reconstruction needed; this GATE
  states the norm recipe explicitly). del-subset-add 0
  missing holds (integrity intact; tempnorm C 427 / py
  221 also 0-missing).
- Wall on band diff added lines (scope 84585207..
  d525fb04, 950 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 634/0, rgram.py 253/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (28d94b61), code 6 blocks,
  py broad singletons (`if n == `) 622->624 +2 == GATE
  stated-literal EXACT / py broad ranges (`<= n <=`)
  632->636 +4 == GATE EXACT, py narrow top-level 612->
  614 +2 / 610->614 +4, CLOSED T10P prints 1658->1664
  +6 py + 1658->1664 +6 C, `# T10P` comments 1658->1664
  +6, C broad singleton 617->619 +2 == GATE EXACT / C
  broad ranges 632->636 +4 == GATE EXACT (5-count C-vs-
  py singleton offset pre-existing + unchanged), C
  narrow 612->614 +2 / 610->614 +4, seal 1752->1758 +6
  (commit msgs): all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-748-q887-
  t10p295 verdict CONFIRM, tallies 15/15 + 13/13 + 12/12
  = 40/40 as-filed (file present, read in full;
  arithmetic 15+13+12=40 consistent) + exact-value
  corroboration incl PB0 NEW + PB1 NEW, PBA88-PLAIN,
  C10-STEP + o8->9 edge, QUAD88-4R-FRAG + R11 rows +
  7B-share + r2r3-TRUE-3B + FRAG coltab+ADD1 48/48 +
  M-tails NEW, ring STANDARD + TM6/TR8 16/16 UNPAIRED +
  SPLIT tails + edges + consts (all re-checked above) +
  A-359 viewer corroboration (CONFIRM all legs, consts
  80/71/67/72 INCL). No CONFIRM-P295.md file (absence
  verified); A-748 suffices per rule. Agrees with cport
  commit msg (PYID 8717, RGRAM 17434).
- Quiz: no conflicting CLAIM/GATE/FLAG on b403 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites
  QNUM-21, newest is QNUM-22 (both read FULL first-hand
  at b401: pure Q-block grants w2b 1520-1559 / w2e
  1560-1599, no gate impact) -- staleness immaterial,
  standing pattern. PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 0 prose slips (norm recipe stated explicitly this
band, full-digit norm 183/201 reproduced EXACT with no
variant gap; tier recipes reproduced EXACT broad+narrow).
Next-P296 predictions banked (A-748/A-359: PB0 @119745
63501000 sig==P295PB0 NOT-byte-equal 31/84 / PB1 @119746
7b80af20 NEW / PBA88 02000000 x16 @119747-62 / C10-1SIG
7b80af20 x10 @119763-72 ==P296PB1-sig, PB1-vs-C10[0] 46/84
DIFFER never-assumed).
