# VERIFY-31cd8b98 b407 T10P299 pins 120789..121136 (1782 tiers) PASS

Seat viewer-r59, first-hand, tree-31cd8b98 @31cd8b98,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r59.
Base 596f0e16 (b406, 1776 tiers). Band = e538588a (py merge
w2b@f0d2976a partial, +6 tiers, +62 pins) + 31cd8b98 (C port,
1782 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build407/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 8d381fa5455384a8 / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  9d7b1b0b36d3338e / aae 7d8dd3a2d118e0db (== GATE both).
- RGRAMC-PYID 8842/8842 covered=8842/8842 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17684/17684 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17684/17684 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17684/17684).
- PINS 17686 rows (2 hdr + 17684, +62 vs base 17624);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  120789 120790 120791 120792 120798 120799 120805 120806
  120807 120808 120811 120812 120815 120816 120817 120825
  120831 120832 120833 120841 120849 120857 120865 120880
  120881 120959 120960 121009 121087 121088 121136
  (== GATE decomposition: S0/S1 (2) + A6 offs 0,1,7,8,14,
  15 + C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 120809/120810/
  120813/120814 unsampled) + Q10 offs 0,8,14/15,16,24,32,
  40,48,63 (b5 step o14->o15 straddled: 120831+120832 both
  pinned) + R7 offs 0,78/79,128,206/207,255 (both counter
  edges straddled + mid 121009); 8811->8842); 31x2=62 rows,
  range 120789..121136 exact. PINS-new-N == for-added
  31/31 (4th set-eq way), PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit407.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 144 PASS
  0 FAIL. Inventory exactly the 13 both sides (PBA88-
  PLAIN/C10-1SIG/QUAD88-4R-FRAG/STANDARD ring + single-F
  coltab; no F0/F1 rowpair, no QT/RT/TT; no BM/BC, no
  M19/XA19, no QB/PT/FM, no M42/X42/H42/L42); C==py
  13/13. S0/S1 168ch sigs 36721e00 SIG-EQ-P298PB0 /
  5b49f53c NEW-own-C10 (S0 31/84 vs P298S0 @ 4-10,13-18,
  20-25,64-75 EXACT + cross-P298S1 36, S1 48/84 vs
  P298S1 @ 0-2,4,5,13-39,52-55,68-75,80-83 EXACT +
  cross-P298S0 63). AM 16x14ch distinct; AC 79, b0-3
  03/00/00/00 (b0 const 03), no b4/b5, PBA sig 03000000
  x16 PLAIN. CM 10x22ch 10/10 diverge; CC 71, b0-3
  5b49f53c full sig, no b4/b5 (C10-1SIG SAME-as-PB1-sig,
  b5 const af via lencode). M 16x14ch distinct. QR 4x20ch
  4-distinct UNPAIRED; r0 6b5ba2e612e8c76cd27c distinct;
  r123 share 6B d6da1e17928d (lcpre 6); tails b84-87
  c76cd27c/78bcf792/9dbcf792/c2bcf792 4/4 distinct;
  r123 TRUE 3B bcf792; full-row lcsuf r123 pairs 3,
  r0-vs-rest 0; lcpre r0-vs-rest 0 (computed first-hand).
  F 16x1B uniq 2 (86 x7 rows 0,1,2,3,5,6,9 / 06 x9 rows
  4,7,8,10-15). QC 68, b0-3 02000000, no b4/b5. RM
  16x16ch distinct; RQ 16x16ch distinct; RC 70, b0-3
  2a/00/00/00, b84-87 5e/a8/1c/06 ring-wide. M-ne-RQ;
  EMBED7 all 16 (RQ[i] = M[i][:2] + X[i] + M[i][2:];
  heads b38,39 same-pos + b47 same-pos value + tails
  cross-position value-equal); X uniq 8e x7 / 0e x9;
  X[i]==F[i]+8 mod 256 all 16 same indices (GATE-
  flagged memo observation CONFIRMED first-hand; stands
  as positional coincidence unless memo rules otherwise).
  RM-vs-RQ UNPAIRED (sets disjoint). Tails STANDARD-SPLIT
  (RM b80-83 by COL, RQ b76-79 by ROW, 16/16 distinct
  each, 0 overlap). Sorted-unique + _N decls 79/71/68/70
  match actual. Missing-sets EXACT: AC [4,5,40,41,42,80,
  81,82,83]; CC [4,5,36,37,38,39,40,41,42,80,81,82,83];
  QC [4,5,38,39,40,41,42,43,44,45,46,47,80,81,82,83,84,
  85,86,87]; RC [4,5,38,39,46,47,52,53,54,55,76,77,78,
  79,80,81,82,83]. Coverage unions exact every block
  (const U tab U {b4,b5} == 88/84/88/88, 0 overlap).
  Q legs M[m] + QR[q] + FRAG F[m] legs both sides
  (ftab/fadd4), no F0/F1 rowpair. R legs RM[c] + RQ[r]
  STANDARD. AC-QC shared-pos 68, same-val 31, AConly 11,
  QConly 0 (computed first-hand; NOT const-repeat). P298
  refs re-read: S0 36721e00 / S1 d46ce43c / PBA 03000000
  / C10-3SIG heads cb56e4 x8 + 0b2cfa + 2b8be4 (==
  A-753 Next-P298 preds EXACT x4). P299 preds (A-753
  Next-P299: 36721e00 sig-eq 31/84 / 5b49f53c NEW /
  03000000 x16 / C10-1SIG 5b49f53c x10) x4 corroborated.
  PBA REPEAT vs P298 (03000000 == 03000000). QUAD sig
  02000000 x64. QR/AM/CM/M/RM/RQ 0-overlap vs P298
  (widths differ AM 14ch vs 18ch, CM 22ch vs 26ch, QR
  20ch vs 24ch, RM 16ch vs 20ch; M/RQ 14ch same width,
  0-overlap by content; base widths re-read first-hand).
  M-tails 16/16 ALL NEW vs P298 M-tail8 + P298 RM-tail8
  + P298 RQ-tail8 (overlap 0 x3); RM-tails NEW vs P298
  RM tails + RQ-tails NEW vs P298 RQ tails + cross
  overlaps 0. Memo INCL PBA88 80 / C10 72 / quad88 68 /
  T88 70 (A-759 re-read): impl 79/71/68/70 = memo-1 on
  PBA/C10 (b5-const excluded), identical quad/T88 --
  standing +1 rule coherent (A/C single-const b5 -> +1,
  Q-step +0 like C-STEP P295, T counter -> +0). Base
  temp maxes _t6208/_b3762/_i3763 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 120789 / S1 120790 / A 120791-806 / C 120807-816 /
  Q 120817-880 / R 120881-121136): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-consts/step emerge from raw lencode) +
  R counter b4=(0x63+2off)&FF b5=0xb0+(off>=79)+
  (off>=207) (py hex; C staged decimal 99/176,
  re-derived from code text both sides) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides + mtab/rtab
  byte positions exact (A 7B b40-42,80-83; C 11B
  b36-42,80-83; Q QM7 b38,39,47,80-83 + R10 b40-45,
  84-87 + FRAG b46 coltab+ADD4: q==0 F[m] else F[m]+4
  mod 256, fail-tags ftab/fadd4 both sides; R TM8
  b52-55,80-83 by COL + TR8 b38,39,46,47,76-79 by ROW)
  + NO F0/F1 rowpair legs. T-mirrors T80898/80903/80908/
  80923/80939/80965 each re-read: hits the exact py guard
  line. C guards `if ((n) == (120789))` / `(120790)` +
  4 range guards exact. C byte-index lists match py per
  block (A 7B, C 11B, Q 7B/10B/1B, R 8B/8B). Temps
  _t6209-6226 continuous (base max _t6208) + _b3764/
  3766/3768/3769/3771/3772 (base max _b3762) + _i3765/
  3767/3770/3773 (base max _i3763): base-tree zero refs
  to new temps prove no reuse. Insert exact both sides:
  after T10P298R close, at dispatch tail (N-out-of-scope
  fallthrough follows). Code comments carry 31/84 +
  25/84 NOT-byte-equal discipline. Matches A-759 geometry
  (values re-checked in audit above; NO D dips: ownloop
  tags exactly the 6 P299 blocks).
- Edges own-loop ownloop407.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P299R N=121136 off=255.
  edges407.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 ab/af, ad/af == raw lencode) +
  aform 16/16 (A 88B head af/af tail cd/af b5set {af} NO
  step, 0 ff) + cform 10/10 (C head cf/af tail e1/af
  b5set {af} NO step, 0 ff) + qform 64/64 + qb5step 64/
  64 (Q head e3/af tail 61/b0 b5set {af,b0} step o14->o15:
  120831 o14 ff/af -> 120832 o15 01/b0, exactly 1 ff in
  64 at o14; quad b4 base e3 step2 == raw-lencode 64/64);
  ring counter 256/256 + ringraw 256/256 (head 63/b0;
  120959 off78 ff/b0 -> 120960 off79 01/b1; mid off128
  63/b1 at 121009; 121087 off206 ff/b1 -> 121088 off207
  01/b2; tail off255 61/b2; exactly 2 ff in 256 at
  o78/o206); odd-lencode 348/348. Ring edges + tail
  121136 in for-list + 2 PASS lines each py+C. Tail
  121136: oracle sha ea22ab1f0c254880... matches PINS
  (rawlen 104 re-checked: paylen 88 + 12 + 4); py+C
  CLOSED T10P299R off=255 agree. No DISSENT: cut bytes
  verify.
- FRAG frag407.py oracle first-hand: F coltab 16 rows
  (86 x7 / 06 x9); ftab q==0 F[m] 16/16 + fadd4 q!=0
  F[m]+4 mod 256 48/48 (== memo A-759 48/48 EXACT).
- PB-diff secf407.py (cache path) + secf407b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (120789 +
  120441 + 120790 + 120442); S0: oracle120789-vs-120441
  31/84, codeS0-vs-P298S0 31/84, positions identical;
  DIRECT tool 31/84 with identical agree-pos 53
  positions. S1: oracle120790-vs-120442 48/84,
  codeS1-vs-P298S1 48/84, positions identical; DIRECT
  48/84 identical agree-pos 36 positions. 0 miss
  (ownloop pre-warmed). Twice-derived both pairs.
  S1-vs-own-C10 secf407c.py: 25/84 UNIFORM all 10
  C10 cells (counts [25]x10; [0] n120807 @ b4,22,23,
  30-43,76-83 == GATE EXACT; sig 5b49f53c vs 5b49f53c
  sig-eq, NOT byte-equal). Byte-diff discipline observed
  throughout, nothing to refute.
- C diff pure-add: numstat 634/0 (rgramc.c) + 254/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 629 content + 5 bare-blank / 0 del; raw py 254
  content / 0 del. Full-digit norm ([0-9]+ -> N): C
  del-uniq 0 add-uniq 178 missing 0 under the recipe AS
  STATED; GATE's 173 reproduces iff leading-whitespace-
  stripped AND empty-excluded (strip+dropempty 173,
  strip-only 174, dropempty-only 177 -- recipe variant
  gap, same class as b405; see prose note); py del-uniq
  0 add-uniq 199 missing 0 == GATE EXACT (variant-
  insensitive: 199 all four variants). del-subset-add 0
  missing holds every variant (integrity intact).
  C-tempnorm 449 / py-tempnorm 215 recorded (no GATE
  claim).
- Wall on band diff added lines (scope 596f0e16..
  31cd8b98, 951 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 634/0, rgram.py 254/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (e538588a), code 6 blocks,
  tier-comments `# T10P` 1682->1688 +6 == GATE stated-
  method EXACT, singletons `if n == ` 630->632 +2 ==
  GATE EXACT, range-guards `<= n <=` 648->652 +4 ==
  GATE EXACT, CLOSED T10P prints 1682->1688 +6 py +
  1682->1688 +6 C, C singleton `if ((n) == (` 625->627
  +2 == GATE EXACT (5-count C-vs-py offset pre-existing,
  unchanged), C ranges 648->652 +4 == GATE EXACT, seal
  1776->1782 +6 (commit msgs; offset +94 vs CLOSED-T10P:
  1782-1688 = 94): all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-759-q891-P299
  verdict PORT, tallies 25/25 + 14/14 + 12/14 = 51/53
  arith-consistent as-filed (the 2 short = §F const-count
  writer arithmetic on PBA/C10, geometry exact -- memo-
  internal methodology note, NO verdict impact; 3rd
  consecutive §F per memo, escalation noted) + exact-
  value corroboration incl PB0 sig-eq + 31/84 + PB1 NEW
  + 25/84, PBA88-PLAIN, C10-1SIG, QUAD88-4R-FRAG + R10
  rows + 6B-share + r123-TRUE-3B + FRAG coltab+ADD4 +
  M-tails NEW, ring STANDARD + TM8/TR8 16/16 UNPAIRED +
  edges + consts (all re-checked above). No viewer P299
  geometry answer on file at gate time (memo-only recon;
  this VERIFY is the viewer record). No CONFIRM-P299.md
  file (absence verified); A-759 suffices per rule. Agrees
  with cport commit msg (PYID 8842, RGRAM 17684).
- Quiz: no conflicting CLAIM/GATE/FLAG on b407 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites
  QNUM-21 newest; QNUM-22 + QNUM-23 both read FULL
  first-hand (pure w2e/w2b Q-block grants, no gate
  impact) -- standing-pattern staleness, immaterial.
  PROSE-01: all hex/counts above copied from own run
  output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 prose-level notes (norm-173 recipe variant gap:
stated recipe yields 178, strip+dropempty yields the
claimed 173 -- integrity holds every variant, same class
as b405; QNUM-21 staleness -- immaterial standing
pattern). 21st odd-band RQ==M instance corroborated as
EMBED7 NEW (tab-subsequence equality + X==F+8 positional
coincidence confirmed, memo-flag stands).
Next-P300 predictions banked (A-759: PB0 @121137 2a721e00
NEW + PB1 5b493523 NEW @121138 + PBA88 02000000 x16
@121139-54 + C10-2SIG @121155-64 = 9b546625 x8 THEN
4d2ab312 x2 trailing-2 pattern).
