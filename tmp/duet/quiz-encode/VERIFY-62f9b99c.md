# VERIFY-62f9b99c b395 T10P287 pins 116613..116960 (1710 tiers) PASS

Seat viewer-r56, first-hand, tree-62f9b99c @62f9b99c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r56.
Base c28c6aa1 (b394, 1704 tiers). Band = 191490f1 (py merge
w2b@05f163cf partial, +6 tiers, +62 pins) + 62f9b99c (C port,
1710 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build395/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc b3aba7fc355a0cae / aae
  7d8dd3a2d118e0db + sha256 rgramc 745936b21151bc25 / aae
  d6e27c97ced21673 (== GATE all 4; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 8468/8468 covered=8468/8468 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16936/16936 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16936/16936 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 16936/16936).
- PINS 16938 rows (2 hdr + 16936, +62 vs base 16876);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  116613 116614 116615 116616 116622 116623 116629 116630
  116631 116632 116635 116636 116639 116640 116641 116648
  116656 116657 116665 116673 116681 116689 116696 116704
  116705 116735 116736 116833 116863 116864 116960
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 116633/116634/
  116637/116638 unsampled) + Q10 offs 0,7,15,16,24,32,
  40,48,55,63 (b5 const, NO step) + R7 offs 0,30/31,128,
  158/159,255; 8437->8468); 31x2=62 rows, range
  116613..116960 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit395.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 128 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/1SIG/QUAD88-4R/STANDARD ring; no QT/RT/TT; no
  BM/BC, no M19/XA19, no QB/PT/FM, no M42/X42/H42/L42);
  C==py 12/12. S0/S1 168ch sigs 85620b00 NEW / 4c0ac516
  NEW (full-string NEW vs BOTH P286 strings; S0-vs-P286S0
  32/84 @ b0-2,4,5,30-43,48,56-59,76-83 EXACT +
  cross-P286S1 39, S1-vs-P286S1 75/84 EXACT, agree-pos
  exactly b20,21,32,33,52-55,63 + cross-P286S0 79). AM
  16x20ch distinct; AC 76, b0-3 01/00/00/00 (b0 const
  01), no b4/b5, PBA sig 01000000 x16 PLAIN. CM 10x22ch
  10/10 diverge (rows span 3 distinct 4B heads 01bcf1bb/
  2c7c107b/d6bc70fb); CC 71, b0-3 86148a2d full-sig in
  consts, no b4/b5 (C10-1SIG x10). M 16x18ch distinct.
  QR 4x22ch 4-distinct UNPAIRED; r0 19318ff00a8d07849bb33d
  distinct; r123 share 7B d9171fcdeadc53; tails b84-87
  849bb33d/d4685f45/f9685f45/ac8d4aa8 4/4 distinct;
  r1r2 TRUE 3B 685f45; suffix-LCS (1,2)=3, (1,3)=(2,3)=
  0, r0-vs-rest 0. QC 66, b0-3 02000000 (NEW quad sig),
  no b4/b5. RM 16x16ch distinct; RQ 16x16ch distinct;
  RC 70, b0-3 2d/00/00/00, b84-87 1a/50/9e/70 ring-wide.
  RQ==M HEAD3+SHIFT FIRST (M 9B vs RQ 8B: RQ[1:4]==M[1:4]
  16/16 + RQ[4:8]==M[5:9] 16/16; 8x9 agree matrix clean
  head3+shifted-tail block at (1,1),(2,2),(3,3),(4,5),
  (5,6),(6,7),(7,8) all 16; RQ0 own max agree 1/16,
  16-distinct; incidental off-diag (2,0)=3, (5,4)=2 --
  NEW degree, P279 HEAD1+SHIFT and P283 HEAD0+SHIFT both
  differ). RM-vs-RQ UNPAIRED (sets disjoint). Tails
  STANDARD-SPLIT (RM b80-83 by COL, RQ b76-79 by ROW,
  16/16 distinct each, 0 overlap). Sorted-unique + _N
  decls 76/71/66/70 match actual. Missing-sets EXACT: AC
  [4,5,8,13,14,15,16,17,80,81,82,83]; CC [4,5,13,14,15,
  16,17,18,19,80,81,82,83]; QC [4,5,8,9,10,11,16,17,18,
  19,20,21,22,23,80,81,82,83,84,85,86,87]; RC [4,5,20,
  21,22,23,28,29,30,31,76,77,78,79,80,81,82,83].
  Coverage unions exact every block (const U tab U {b4,
  b5} == 88/84/88/88, 0 overlap). Q legs M[m] + QR[q],
  no frags. R legs RM[c] + RQ[r] STANDARD. P286 refs
  re-read: S0 1df80a00 / S1 cd23fd15 / PBA 01000000 /
  C10 cd236d10 / QUAD 01000000 (== P286 preds EXACT).
  P287 preds (A-710/A-350 Next-P287: 85620b00/4c0ac516/
  01000000/86148a2d) x4 corroborated staged. PBA REPEAT
  vs P286 (01000000 == 01000000). C10 NEW vs P286
  (86148a2d vs cd236d10). QUAD sig NEW vs P286 (02000000
  vs 01000000). QR 0-overlap vs P286QR. M-tails 16/16
  ALL NEW vs P286 RQ row-led tails (overlap 0); RM-tails
  ALL NEW vs P286 RM-tail8 + P286 RQ-tail8 (overlap 0
  x2); RQ-tails ALL NEW vs P286 RM-tail8 + P286 RQ-tail8
  (overlap 0 x2). Memo INCL PBA88 77 / C10 72 / quad88
  67 / T88 70 (A-713 re-read): impl 76/71/66/70 =
  memo-1 on PBA/C10/quad (b5-const excluded), identical
  T88. Base temp maxes _t6011/_b3641/_i3642 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 116613 / S1 116614 / A 116615-630 / C 116631-640 /
  Q 116641-704 / R 116705-960): bounds + paylens (12x84
  + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q both
  sides (b5-consts emerge from raw lencode) + R counter
  b4=(0xc3+2off)&FF b5=0x8f+(off>=31)+(off>=159) (py
  hex; C stages decimal 195/143/31/159, re-derived from
  code text both sides) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions exact
  (A 10B b8,13-17,80-83; C 11B b13-19,80-83; Q QM9
  b16-19,23,80-83 + R11 b8-11,20-22,84-87; R TM8
  b28-31,80-83 by COL + TR8 b20-23,76-79 by ROW) + NO
  frag leg in Q. T-mirrors T78050/78055/78060/78076/
  78092/78113 each re-read: hits the exact py guard
  line. C guards `if ((n) == (116613))` / `(116614)` +
  4 range guards exact. C byte-index lists match py per
  block (A 10B, C 11B, Q 9B/11B, R 8/8B). Temps
  _t6012-6027 continuous (base max _t6011) + _b3643/
  3645/3647/3648/3650/3651 (base max _b3641) + _i3644/
  3646/3649/3652 (base max _i3642): added-lines-only
  refs (base tree zero refs to new temps) prove no
  reuse. Insert exact both sides: after T10P286R close,
  at dispatch tail (N-out-of-scope fallthrough follows;
  C 2 scope hits, py 2 scope hits). Matches A-713/A-351
  geometry (values re-checked in audit above; NO D dips:
  ownloop tags exactly the 6 P287 blocks).
- Edges own-loop ownloop395.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P287R N=116960 off=255.
  edges395.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 0b/8f, 0d/8f == raw lencode
  0x8F0B/0x8F0D) + aform 16/16 (A 88B head 0f/8f tail
  2d/8f b5set {8f} NO step, 0 ff) + cform 10/10 (C head
  2f/8f tail 41/8f b5set {8f} NO step, 0 ff) + qform
  64/64 (Q head 43/8f tail c1/8f b5set {8f} NO step NO
  edge, quad formula == raw-lencode 64/64, 0 ff); ring
  counter 256/256 + ringraw 256/256 (head c3/8f; 116735
  off30 ff/8f -> 116736 off31 01/90; mid off128 c3/90;
  116863 off158 ff/90 -> 116864 off159 01/91; tail
  off255 c1/91; exactly 2 ff in 256 at o30/o158);
  odd-lencode 348/348. Ring edges + tail 116960 in
  for-list + 2 PASS lines each py+C. Tail 116960:
  oracle sha 0ee07be62583cf05... matches PINS; py+C
  CLOSED T10P287R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf395.py (cache path) + secf395b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (116613 +
  116265 + 116614 + 116266); S0: oracle116613-vs-116265
  32/84, codeS0-vs-P286S0 32/84, positions identical;
  DIRECT tool 32/84 with identical agree-pos 52
  positions. S1: oracle 75/84, code 75/84, positions
  identical; DIRECT 75/84 identical agree-pos 9
  positions. 0 miss (ownloop pre-warmed). Twice-derived
  both pairs. No byte-equal wording in A-713/A-351 this
  band (both stage NEW sigs, consistent with 32/75
  diffs) -- byte-diff discipline observed, nothing to
  refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 230
  content / 0 del. Normalized ([0-9]+ -> N recipe):
  py del-uniq 0 add-uniq 187 missing 0 == GATE EXACT.
  C add-uniq: stated recipe gives 168 first-hand (python
  + BSD shell, twice-derived); sweep-script
  reconstruction (lstrip + keep-empty) gives 165 ==
  GATE EXACT (see NOTE-viewer-r56-norm-resolution: same
  reconstruction reproduces b393's 166; +/- line sets
  byte-identical to sweep's cdiffs; sweep's r60 logs
  carry no norm script). del-uniq 0 + del-subset-add 0
  missing hold under EVERY variant (integrity property
  intact). Recipe-description imprecision only (GATE
  prose omits the lstrip step); numbers are genuine
  script outputs. Code unaffected.
- Wall on band diff added lines (scope c28c6aa1..
  62f9b99c, 897 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (191490f1), code 6 blocks,
  tier-comments `# T10P` 1610->1616 +6, singletons
  606->608 +2 / ranges 600->604 +4, CLOSED T10P prints
  1610->1616 +6 py + 1610->1616 +6 C, C singleton
  `if ((n) == (` 601->603 +2 / C ranges 600->604 +4,
  seal 1704->1710 +6 (commit msgs): all agree, no slip.
  5-count C-vs-py singleton offset pre-existing +
  unchanged (gap 5 at base AND new under GATEPAT).
- CONFIRM evidence (CONVERT-01 rule b): A-713-q799-
  t10p287 verdict CONFIRM, tallies 14/14 + 12/12 + 11/11
  = 37/37 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 16 total vs 37, counting unit irreproducible;
  methodology note, NO verdict impact) + exact-value
  corroboration incl PBA88-PLAIN + b5 const, C10-1SIG,
  QUAD88-4R + R11 rows + tails + lcsuf + M-tails NEW,
  ring STANDARD + TR8/TM8 16/16 UNPAIRED + edges +
  consts (all re-checked above) + A-351 viewer
  corroboration (CONFIRM all legs, consts 77/72/67/70
  INCL). No CONFIRM-P287.md file (absence verified);
  A-713 suffices per rule. Agrees with cport commit msg
  (PYID 8468, RGRAM 16936).
- Quiz: no conflicting CLAIM/GATE/FLAG on b395 (own seat
  CLAIM only). Newest PARENT-* is QNUM-21 (w2b block) +
  QNUM-20 (w2f block): pure Q-block grants, read, no gate
  impact -- GATE cites QNUM-19: 1 immaterial staleness
  (standing pattern). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 immaterial GATE prose notes (QNUM-19 vs -21
staleness; norm recipe prose omits lstrip step --
numbers 165/166 verified genuine via reconstruction,
integrity intact).
Next-P288 predictions banked for r57+ (A-713/A-351: PB0
0ac51600 / PB1 3bf3942d / PBA88 02000000 x16 == P287QUAD
sig / C10 3bf3942d == P288PB1 sig with 47/84 byte-diff
noted).
