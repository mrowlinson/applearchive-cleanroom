# VERIFY-676b823c b409 T10P301 pins 121485..121832 (1794 tiers) PASS

Seat viewer-r60, first-hand, tree409 @676b823c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r60.
Base 09789412 (b408, 1788 tiers). Band = 4da27742 (py merge
w2b@533ad57e partial, +6 tiers, +62 pins) + 676b823c (C port,
1794 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical non-tmp both; 117 = 113 non-tmp + 4 tmp).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build409/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc c82391f53cd1356e / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  2d89dbb505d4e950 / aae 7d8dd3a2d118e0db (== GATE both).
- RGRAMC-PYID 8905/8905 covered=8905/8905 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17810/17810 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17810/17810 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp equal + raw-order identical, 17810/17810).
- PINS 17812 rows (2 hdr + 17810, +62 vs base 17750);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  121485 121486 121487 121488 121494 121495 121501 121502
  121503 121504 121507 121508 121511 121512 121513 121521
  121529 121537 121545 121553 121561 121569 121575 121576
  121577 121599 121600 121705 121727 121728 121832
  (== GATE decomposition: S0/S1 (2) + A6 offs 0,1,7,8,14,
  15 + C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 121505/121506/
  121509/121510 unsampled, absence verified) + Q10 offs
  0,8,16,24,32,40,48,56,62,63 (tail pair 121575/121576) +
  R7 offs 0,22/23,128,150/151,255 (both counter edges
  straddled + mid 121705); 8874->8905); 31x2=62 rows,
  range 121485..121832 exact. PINS-new-N == for-added
  31/31 (4th set-eq way), PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r59/b408); band
  diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit409.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 147 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-1SIG/QUAD88-4R/RING-SWAPPED; no F/F0/F1, no
  QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM, no
  M42/X42/H42/L42); C==py 12/12. S0/S1 168ch sigs
  2ab31200 NEW / 0b887b25 NEW (S0 32/84 vs P300S0 @ 1,2,
  4-11,41,42,44-51,56-67 EXACT + cross-P300S1 64, S1
  55/84 vs P300S1 @ 0-11,13-15,17,19-23,30-39,44-51,
  60-71,80-83 EXACT + cross-P300S0 64). AM 16x16ch
  distinct; AC 78, b0-3 02/00/00/00 (b0 const 02), no
  b4/b5, PBA sig 02000000 x16 PLAIN. CM 10x24ch 10/10
  diverge; CC 70, b0-3 0b/91/71/25 (C10-1SIG x10
  NOT-PB1-sig: 0b917125 != 0b887b25), no b4/b5 (b5
  const b5 via lencode). M 16x20ch distinct. QR 4x22ch
  4-distinct UNPAIRED; r0 e17ce7bdb5ec9f0b8e54bf
  distinct; r123 share 7B 8afce24675c2cd (lcpre 7);
  tails b84-87 0b8e54bf/ccca8588/f1ca8588/16cb8588 4/4
  distinct; r12 TRUE 3B ca8588; r3 2B 8588 (== memo
  fixed value); full-row lcsuf (1,2)=3 (1,3)=(2,3)=2
  (0,*)=0; lcpre r0-vs-rest 0. QC 65, b0-3 02000000, no
  b4/b5 (QUAD single-sig x64). RM 16x16ch distinct; RQ
  16x16ch distinct; RM-vs-RQ UNPAIRED (sets disjoint);
  RC 70, b0-3 29/00/00/00, b84-87 1d/40/42/53 ring-wide.
  M-ne-RQ lists; TAILS all 16 (RQ[i][4:8] == M[i][6:10]
  byte-indexed, b80-83 tails); heads own (aligned-4B
  agree max 0 over all 256 pairs incl diagonal);
  RQ0 4-distinct (9e x4 / 9f x6 / ae x4 / ff x2), RQ1
  2-distinct (56 x14 / 68 x2), RQ2 7-distinct, RQ3
  13-distinct. Tails SWAPPED (RM b76-79 by COL, RQ
  b80-83 by ROW, 16/16 distinct each, 0 overlap).
  Sorted-unique + _N decls 78/70/65/70 match actual.
  Missing-sets EXACT: AC [4,5,28,29,30,31,80,81,82,83];
  CC [4,5,24,25,26,27,28,29,30,31,80,81,82,83]; QC
  [4,5,18,19,25,26,27,28,29,30,31,32,33,34,35,80,81,82,
  83,84,85,86,87]; RC [4,5,29,30,34,35,40,41,42,43,76,
  77,78,79,80,81,82,83]. Coverage unions exact every
  block (const U tab U {b4,b5} == 88/84/88/88, 0
  overlap). Q legs M[m] + QR[q] both sides, NO F-legs
  either region both sides. R legs RM[c] + RQ[r] both
  sides. AC-QC shared-pos 65, same-val 49, AConly 13,
  QConly 0 (computed first-hand; NOT const-repeat).
  P300 refs re-read: S0 2a721e00 / S1 5b493523 / PBA
  02000000 / C10-2SIG 9b546625 x8 + 4d2ab312 x2 /
  QUAD 01000000 x64. Next-P301 preds (A-763 re-read:
  PB0 2ab31200 NEW / PB1 0b887b25 NEW / PBA88 02000000
  x16 / C10-1SIG 0b917125 x10) x4 corroborated. PBA
  REPEAT vs P300 (02000000 == 02000000). AM/CM/M/QR/RM/
  RQ 0-overlap vs P300 (widths P301 AM16/CM24/M20/QR22/
  RM16/RQ16 vs P300 AM14/CM32/M20/QR20/RM16/RQ18;
  same-width pairs 0-overlap by content; base widths
  re-read first-hand). M-tails 16/16 ALL NEW vs P300
  M-tail8 + P300 RM-tail8 + P300 RQ-tail8 (overlap 0
  x3, incl col-led); RM-tails NEW vs P300 RM tails +
  RQ-tails NEW vs P300 RQ tails + cross overlaps 0.
  Memo INCL PBA88 79 / C10 71 / quad88 66 / T88 70
  (A-768 re-read): impl 78/70/65/70 = memo-1 on
  PBA/C10/quad (b5-const excluded), identical T88 --
  standing +1 rule coherent, FIRST +1/+1/+1/+0 case (A/
  C/Q single-const b5 -> +1, T counter -> +0). Base
  temp maxes _t6244/_b3782/_i3783 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 121485 / S1 121486 / A 121487-502 / C 121503-512 /
  Q 121513-576 / R 121577-832): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-consts emerge from raw lencode) + R
  counter b4=(0xd3+2off)&FF b5=0xb5+(off>=23)+
  (off>=151) (py hex; C staged decimal 211/181,
  re-derived from code text both sides: 211==0xd3,
  181==0xb5) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A 8B b28-31,
  80-83; C 12B b24-31,80-83; Q QM10 b18,19,25-27,35,
  80-83 + R11 b28-34,84-87, NO frags; R TM8 b40-43,
  76-79 by COL + TR8 b29,30,34,35,80-83 by ROW) + C
  guards `if ((n) == (121485))` / `(121486)` + 4 range
  guards exact + C byte-index lists match py per block
  (A 8B, C 12B, Q 10B/11B, R 8B/8B). T-mirrors T81386/
  81391/81396/81411/81427/81449 each re-read: hits the
  exact py guard line. Temps _t6245-6260 continuous
  (base max _t6244) + _b3784/3786/3788/3789/3791/3792
  (base max _b3782) + _i3785/3787/3790/3793 (base max
  _i3783): combined 3784-3793 added-only, no reuse.
  Insert exact both sides: P300R block precedes, at
  dispatch tail (N-out-of-scope fallthrough follows; 2
  scope hits py + 2 scope hits C). Code comments carry
  32/84 + 55/84 NOT-byte-equal discipline (sigs NEW).
  Matches A-768 geometry (values re-checked in audit
  above; NO D dips: ownloop tags exactly the 6 P301
  blocks).
- Edges own-loop ownloop409.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed = 348-31). Census R256/Q64/A16/
  C10/S0/S1 exact. Tail line: CLOSED T10P301R N=121832
  off=255. edges409.py: paylens 12x84 + 336x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 1b/b5, 1d/b5 == raw
  lencode) + aform 16/16 (A 88B head 1f/b5 tail 3d/b5
  b5set {b5} NO step, 0 ff) + cform 10/10 (C head 3f/b5
  tail 51/b5 b5set {b5} NO step, 0 ff) + qform 64/64 +
  qb5const 64/64 (Q head 53/b5 tail d1/b5 b5set {b5} NO
  step, 0 ff in 64; quad b4 base 53 step2 == raw-lencode
  64/64); ring counter 256/256 + ringraw 256/256 (head
  d3/b5; 121599 off22 ff/b5 -> 121600 off23 01/b6; mid
  off128 d3/b6 at 121705; 121727 off150 ff/b6 -> 121728
  off151 01/b7; tail off255 d1/b7; exactly 2 ff in 256
  at o22/o150); odd-lencode 348/348. Ring edges + tail
  121832 in for-list + 2 PASS lines each py+C. Tail
  121832: oracle sha 93b3a589f52d2e8a... matches PINS
  (rawlen 104 re-checked: paylen 88 + 12 + 4); py+C
  CLOSED T10P301R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf409.py (cache path) + secf409b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (121485 +
  121137 + 121486 + 121138); S0: oracle121485-vs-121137
  32/84, codeS0-vs-P300S0 32/84, positions identical;
  DIRECT tool 32/84 with identical agree-pos 52
  positions. S1: oracle121486-vs-121138 55/84,
  codeS1-vs-P300S1 55/84, positions identical; DIRECT
  55/84 identical agree-pos 29 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs.
  S1-vs-own-C10 secf409c.py: 38/84 x9 + 37/84 x1
  (cell 8 n121511) NON-uniform ([0] n121503 @ b1,2,4,
  19-22,24-31,52-55,57-71,80-83 == GATE EXACT; sig
  0b887b25 vs 0b917125 differs, NOT byte-equal; cell 8
  agrees b25 where [0] differs). Byte-diff discipline
  observed throughout, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 230
  content / 0 del. Full-digit norm ([0-9]+ -> N): C
  del-uniq 0 add-uniq 165 missing 0 under the recipe AS
  STATED; GATE's 161 reproduces iff leading-whitespace-
  stripped AND empty-excluded (strip+dropempty 161,
  strip-only 162, dropempty-only 164 -- recipe variant
  gap, same class as b405/b407; see prose note); py
  del-uniq 0 add-uniq 186 missing 0 == GATE EXACT
  (variant-insensitive: 186 all four variants).
  del-subset-add 0 missing holds every variant
  (integrity intact). C-tempnorm 412 / py-tempnorm 205
  recorded (no GATE claim).
- Wall on band diff added lines (scope 09789412..
  676b823c, 897 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (4da27742), code 6 blocks,
  tier-comments `# T10P` 1694->1700 +6 == GATE stated-
  method EXACT, singletons `if n == ` 634->636 +2 ==
  GATE EXACT, range-guards `<= n <=` 656->660 +4 ==
  GATE EXACT, CLOSED T10P prints 1694->1700 +6 py +
  1694->1700 +6 C, C singleton `if ((n) == (` 629->631
  +2 == GATE EXACT (5-count C-vs-py offset pre-existing,
  unchanged: 634-629 = 636-631 = 5), C ranges 656->660
  +4 == GATE EXACT, seal 1788->1794 +6 (commit msgs;
  offset +94 vs CLOSED-T10P: 1794-1700 = 94, stable):
  all agree, no slip. Dispatch-exact cross-check: py
  624->626 +2 / 634->638 +4, C identical 624->626 /
  634->638 (py=C, no offset at dispatch scope).
- CONFIRM evidence (CONVERT-01 rule b): A-768-q893-P301
  verdict PORT, tallies 25/25 + 17/17 + 11/14 = 53/56
  arith-consistent as-filed (the 3 short = §F const-count
  writer arithmetic on PBA/C10/quad, geometry exact --
  5th consecutive §F per memo, escalation noted; NO
  verdict impact) + exact-value corroboration incl PB0/
  PB1 NEW sigs, PBA88-PLAIN, C10-1SIG NOT-PB1-sig,
  QUAD88-4R + R11 rows + 7B-share + r12-TRUE-3B + r3-2B
  (memo-fixed value 8588) + M-tails NEW, T88-RING-
  SWAPPED + TM8/TR8 16/16 UNPAIRED + SWAPPED tails +
  b84-87 1d404253 + edges + consts (all re-checked
  above). No viewer P301 geometry answer on file at
  gate time (memo-only recon; this VERIFY is the viewer
  record). No CONFIRM-P301.md file (absence verified);
  A-768 suffices per rule. Agrees with cport commit msg
  (PYID 8905, RGRAM 17810).
- Quiz: no conflicting CLAIM/GATE/FLAG on b409 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites
  QNUM-21 newest; QNUM-22 + QNUM-23 both read FULL
  first-hand (pure w2e/w2b Q-block grants, no gate
  impact) -- standing-pattern staleness, immaterial.
  PROSE-01: all hex/counts above copied from own run
  output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 3 prose-level notes (norm-161 recipe variant gap:
stated recipe yields 165, strip+dropempty yields the
claimed 161 -- integrity holds every variant, same class
as b405/b407; PB1-vs-C10 38/37 attribution: values
CORRECT first-hand, but A-763 predicted sigs/patterns
only -- 38/37 are GATE-measured, and the "== predicted
EXACT" parenthetical overstates; QNUM-21 staleness --
immaterial standing pattern). 22nd odd-band RQ==M
instance corroborated as TAILS (tab-tail equality
RQ[4:8]==M[6:10] + heads-own max-agree 0 + RQ head
distinctness 4/2/7/13; joins P255/P263/P267/P285/P291/
P401 group; memo-silent).
Next-P302 predictions banked (A-768 re-read: PB0 @121833
0b913100 NEW + PB1 8031ff44 NEW @121834 + PBA88 04000000
x16 @121835-50 NEW sig 04 first + C10-1SIG 8031ff44 x10
@121851-60 SAME-as-PB1-sig).
