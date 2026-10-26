# VERIFY-596f0e16 b406 T10P298 pins 120441..120788 (1776 tiers) PASS

Seat viewer-r59, first-hand, tree-596f0e16 @596f0e16,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r59.
Base 17287ff6 (b405, 1770 tiers). Band = f105d6b6 (py merge
w2b@de35d962 partial, +6 tiers, +64 pins) + 596f0e16 (C port,
1776 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build406/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 25999cfe215f09fa / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  8fece2c5d1591114 / aae 7d8dd3a2d118e0db.
- RGRAMC-PYID 8811/8811 covered=8811/8811 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17622/17622 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17622/17622 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17622/17622).
- PINS 17624 rows (2 hdr + 17622, +64 vs base 17560);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +32/-0:
  120441 120442 120443 120444 120447 120448 120457 120458
  120459 120460 120463 120466 120467 120468 120469 120476
  120484 120485 120493 120501 120509 120517 120524 120532
  120533 120539 120540 120575 120576 120703 120704 120788
  (== GATE verbatim; S0/S1 (2) + A6 120443/120444/120447/
  120448/120457/120458 (offs 0,1,4,5,14,15; b5 step o4->o5
  straddled: 120447+120448 both pinned) + C6 120459/120460/
  120463/120466/120467/120468 (offs 0,1,4,7,8,9) + Q10
  120469/120476/120484/120485/120493/120501/120509/120517/
  120524/120532 (offs 0,7,15/16,24,32,40,48,55,63; b5 const
  full block, NO step) + R8 120533/120539/120540/120575/
  120576/120703/120704/120788 (offs 0,6/7,42/43,170/171,
  255; both counter edges straddled; NO mid pin -- see
  prose note); 8779->8811); 32x2=64 rows, range
  120441..120788 exact. PINS-new-N == for-added 32/32
  (4th set-eq way), PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit406.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 139 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  STEP/C10-3SIG/QUAD88-4R/2SIG ring; no F0/F1, no
  QT/RT/TT; no BM/BC, no M19/XA19, no QB/PT/FM, no
  M42/X42/H42/L42); C==py 12/12. S0/S1 168ch sigs
  36721e00 NEW / d46ce43c NEW (S0 31/84 vs P297S0 @
  0-2,4,5,30,31,38-48,50,56-63,80-83 EXACT +
  cross-P297S1 63, S1 62/84 vs P297S1 @ 0-11,13,15-27,
  30-39,42-51,56-67,80-83 EXACT + cross-P297S0 60).
  AM 16x18ch distinct; AC 77, b0-3 03/00/00/00 (b0 const
  03), no b4/b5, PBA sig 03000000 x16 STEP (b5 stepped
  0xac+(o>=5) via lencode). CM 10x26ch 10/10 diverge;
  rows 0-6 share 18ch cb56e485ef1bf35e90 byte9 7-diverge
  (52/72/92/b2/d2/f2/12), row 7 head cb56e485 then
  diverges, rows 8-9 distinct heads 0b2cfa85/2b8be445;
  CC 69, b3 const 3c, no b0-2/b5 (C10-3SIG cb56e43c x8
  + 0b2cfa3c + 2b8be43c ORDERED 8+1+1, b5 const ad via
  lencode). M 16x14ch distinct. QR 4x24ch 4-distinct
  UNPAIRED; r0 b28a63bf7b73275140bbf05d distinct; r123
  share 8B 32b068fb7533445a, byte8 d4/b8/dd; tails
  b84-87 40bbf05d/d4bda4a6/b8e7a4a6/dde7a4a6 4/4
  distinct; r23 TRUE 3B e7a4a6 (r1 shares a4a6 pair);
  byte-LCS (0,*)=0, (1,2)=(1,3)=2, (2,3)=3 (computed
  first-hand). QC 67, b0-3 03000000, no b4/b5. RM
  16x20ch distinct, b0 col-split 3c cols 0-6 + 3d cols
  7-15 (112x3c + 144x3d arithmetic verified: 7x16 +
  9x16); RQ 16x14ch distinct; RC 69, no b0 (2SIG),
  b1-3 00/00/00 const, b84-87 50/6b/89/62 ring-wide.
  M==RQ EXACT 16/16 (lists identical). RM-vs-RQ UNPAIRED
  (sets disjoint). Tails SPLIT (RM b80-83 by COL, RQ
  b76-79 by ROW, 16/16 distinct each, 0 overlap).
  Sorted-unique + _N decls 77/69/67/69 match actual.
  Missing-sets EXACT: AC [4,5,16,17,18,19,23,80,81,82,
  83]; CC [0,1,2,4,5,11,18,19,20,21,22,80,81,82,83]; QC
  [4,5,16,17,18,22,23,24,25,26,28,29,30,80,81,82,83,84,
  85,86,87]; RC [0,4,5,11,19,27,28,29,30,34,35,76,77,78,
  79,80,81,82,83]. Coverage unions exact every block
  (const U tab U {b4,b5} == 88/84/88/88, 0 overlap).
  Q legs M[m] + QR[q], no frags. R legs RM[c] + RQ[r]
  2SIG. AC-QC shared-pos 66, same-val 39, AConly 11,
  QConly 1 (== GATE, computed first-hand; NOT const-
  repeat). P297 refs re-read: S0 66501000 / S1 7b802f23
  / PBA 02000000 / C10-3SIG heads 2f23 x8 + 8f1d + cf1c
  / RC 1e000000+be38e65b (== A-752/A-361 Next-P297 preds
  EXACT x4 + RC consts). P298 preds (A-752/A-361
  Next-P298: 36721e00 NEW / d46ce43c NEW / 03000000 x16
  / C10 cb56e43c x8 + 0b2cfa3c + 2b8be43c) x4
  corroborated. PBA NEW vs P297 (03000000 vs 02000000).
  QUAD sig 03000000 x64. QR/AM/CM/M/RM/RQ 0-overlap vs
  P297 (widths differ AM 18ch vs 14ch, RM 20ch vs 16ch;
  CM 26ch + M/RQ 14ch + QR 24ch same width, 0-overlap
  by content; base widths re-read first-hand). M-tails
  16/16 ALL NEW vs P297 M-tail8 + P297 RM-tail8 + P297
  RQ-tail8 (overlap 0 x3). Memo INCL PBA88 77 / C10 70
  / quad88 68 / T88 69 (A-753 re-read): impl 77/69/67/
  69 = memo identical on PBA/T88 (b5 varies/stepped,
  no deduction), memo-1 on C10/quad (writer deducted
  const-b5) -- standing +1 rule coherent (PBA-STEP +0
  new case: b5 varies -> no deduction, like C-STEP b403
  and Q-step cases). Base temp maxes _t6192/_b3752/
  _i3753 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 120441 / S1 120442 / A 120443-458 / C 120459-468 /
  Q 120469-532 / R 120533-788): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-step/consts emerge from raw lencode) +
  R counter b4=(0xab+2off)&FF b5=0xad+(off>=43)+
  (off>=171) (py hex; C staged decimal 171/173,
  re-derived from code text both sides) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides + mtab/rtab
  byte positions exact (A 9B b16-19,23,80-83; C 13B
  b0-2,11,18-22,80-83; Q QM7 b28-30,80-83 + R12
  b16-18,22-26,84-87; R TM10 b0,11,19,27,34,35,80-83
  by COL + TR7 b28-30,76-79 by ROW) + NO frag leg in Q.
  T-mirrors T80648/80653/80658/80673/80689/80710 each
  re-read: hits the exact py guard line. C guards
  `if ((n) == (120441))` / `(120442)` + 4 range guards
  exact. C byte-index lists match py per block (A 9B,
  C 13B, Q 7B/12B, R 10B/7B). Temps _t6193-6208
  continuous (base max _t6192) + _b3754/3756/3758/3759/
  3761/3762 (base max _b3752) + _i3755/3757/3760/3763
  (base max _i3753): base-tree zero refs to new temps
  prove no reuse. Insert exact both sides: after
  T10P297R close, at dispatch tail (N-out-of-scope
  fallthrough follows). Q comment 'r2r3 TRUE 3B e7a4a6,
  r1 lcs=2, r0 lcs=0' EXACT vs first-hand LCS (no
  comment staleness). Matches A-753 geometry (values
  re-checked in audit above; NO D dips: ownloop tags
  exactly the 6 P298 blocks).
- Edges own-loop ownloop406.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (316 miss-warmed = 348 minus 32 for-Ns). Census
  R256/Q64/A16/C10/S0/S1 exact. Tail line: CLOSED
  T10P298R N=120788 off=255. edges406.py: paylens 12x84
  + 336x88; lencode 92/92 (S/A/C/Q raw l16; S0/S1 f3/ac,
  f5/ac == raw lencode) + aform 16/16 (A 88B head f7/ac
  tail 15/ad b5set {ac,ad} step o4->o5: 120447 o4 ff/ac
  -> 120448 o5 01/ad, exactly 1 ff in 16 at o4; A b4
  base f7 step2 == raw-lencode 16/16) + cform 10/10 (C
  head 17/ad tail 29/ad b5set {ad} NO step, 0 ff) +
  qform 64/64 + qb5const 64/64 (Q head 2b/ad tail a9/ad
  b5set {ad} NO step, 0 ff; quad b4 base 2b step2 ==
  raw-lencode 64/64); ring counter 256/256 + ringraw
  256/256 (head ab/ad; 120575 off42 ff/ad -> 120576
  off43 01/ae; 120703 off170 ff/ae -> 120704 off171
  01/af; tail off255 a9/af; exactly 2 ff in 256 at
  o42/o170; Q tail a9/ad vs R tail a9/af differ in b5
  -- labeled apart); odd-lencode 348/348. Ring edges +
  tail 120788 in for-list + 2 PASS lines each py+C.
  Tail 120788: oracle sha 7f0869e76738e7c5... matches
  PINS; py+C CLOSED T10P298R off=255 agree. No DISSENT:
  cut bytes verify.
- PB-diff secf406.py (cache path) + secf406b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (120441 +
  120093 + 120442 + 120094); S0: oracle120441-vs-120093
  31/84, codeS0-vs-P297S0 31/84, positions identical;
  DIRECT tool 31/84 with identical agree-pos 53
  positions. S1: oracle120442-vs-120094 62/84,
  codeS1-vs-P297S1 62/84, positions identical; DIRECT
  62/84 identical agree-pos 22 positions. 0 miss
  (ownloop pre-warmed). Twice-derived both pairs. Both
  NEW strings, no byte-equal wording anywhere this band
  -- byte-diff discipline observed, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 231/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 231
  content / 0 del. Fine-norm: C-tempnorm (temp-norm,
  empty-excluding) del-uniq 0 add-uniq 390 missing 0 ==
  GATE EXACT (this GATE states the temp-norm recipe
  explicitly). Full-digit norm C 151 / py 170 + py-
  tempnorm 185 recorded (no GATE claim). del-subset-add
  0 missing holds (integrity intact).
- Wall on band diff added lines (scope 17287ff6..
  596f0e16, 900 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1, PINS +64/+0.
- Tiers: merge-msg +6/+64 (f105d6b6), code 6 blocks,
  py top-level singletons (^4sp `if n == `) 618->620 +2
  == GATE stated-method EXACT, py T10P range guards
  622->626 +4 == GATE EXACT, CLOSED T10P prints 1676->
  1682 +6 py + 1676->1682 +6 C, C top-level singleton
  `if ((n) == (` 618->620 +2 == GATE EXACT / C top-level
  ranges `if ((N) <= (n)` 622->626 +4 == GATE EXACT,
  seal 1770->1776 +6 (commit msgs): all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-753-q890-P298
  verdict PORT, tallies 25/25 + 14/14 + 13/15 = 52/54
  arith-consistent as-filed (the 2 short = §F const-count
  writer arithmetic on C10/quad, geometry exact -- memo-
  internal methodology note, NO verdict impact; same
  systematic dispute as A-752 §F) + exact-value
  corroboration incl PB0/PB1 NEW sigs, PBA88-STEP + edge,
  C10-3SIG ORDERED 8/1/1, QUAD88-4R + R12 rows + 8B-share
  + r23-TRUE-3B + b5 const + M-tails NEW, ring 2SIG col-
  split + 112+144 + TR7 16/16 UNPAIRED + edges + consts
  (all re-checked above). No CONFIRM-P298.md file (absence
  verified); A-753 suffices per rule. Agrees with cport
  commit msg (PYID 8811, RGRAM 17622).
- Quiz: no conflicting CLAIM/GATE/FLAG on b406 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites no
  QNUM (no staleness). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 prose-level note (ring decomposition "mid" label:
no mid pin exists, extra pair is ring offs 6/7 --
enumerated 32 Ns exact, label looseness only; norm recipe
stated explicitly this band, temp-norm 390 reproduced
EXACT with no variant gap).
Next-P299 predictions banked (A-753: PB0 @120789 36721e00
sig-eq P298PB0 31/84 NOT byte-equal + PB1 5b49f53c NEW
@120790 + PBA88 03000000 x16 @120791-806 + C10 5b49f53c
x10 ==P299PB1 sig, PB1-vs-C10 25/84 uniform all 10).
