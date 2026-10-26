# VERIFY-3c2b2e00 b400 T10P292 pins 118353..118700 (1740 tiers) PASS

Seat viewer-r58, first-hand, tree-3c2b2e00 @3c2b2e00,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r58.
Base d5de4afe (b399, 1734 tiers). Band = 2dbda75a (py merge
w2b@439c8c3a partial, +6 tiers, +62 pins) + 3c2b2e00 (C port,
1740 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build400/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ded22093ff68c8c6 / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  e0664a177af19d72 / aae 7d8dd3a2d118e0db.
- RGRAMC-PYID 8624/8624 covered=8624/8624 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17248/17248 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17248/17248 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17248/17248).
- PINS 17250 rows (2 hdr + 17248, +62 vs base 17188);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  118353 118354 118355 118356 118362 118363 118369 118370
  118371 118372 118377 118378 118379 118380 118381 118396
  118397 118399 118400 118413 118421 118429 118437 118444
  118445 118527 118528 118573 118655 118656 118700
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,6,7,8,9 (offs 2,3,4,5 = 118373/118374/
  118375/118376 unsampled) + Q10 offs 0,15,16,18,19,32,
  40,48,56,63 (b5 step o18->o19 straddled: 118399+118400
  both pinned) + R7 offs 0,82/83,128,210/211,255 (both
  counter edges straddled); 8593->8624); 31x2=62 rows,
  range 118353..118700 exact. PINS-new-N == for-added
  31/31 (4th set-eq way), PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit400.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 124 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-2SIG/QUAD88-4R/STANDARD ring; no F0/F1, no
  QT/RT/TT; no BM/BC, no M19/XA19, no QB/PT/FM, no
  M42/X42/H42/L42); C==py 12/12. S0/S1 168ch sigs
  436f1300 NEW / 2b81e720 NEW (full-string NEW vs BOTH
  P291 strings; S0-vs-P291S0 34/84 @ b0,4,5,11,18,19,
  25-32,34-41,52-55,76-83 EXACT + cross-P291S1 35,
  S1-vs-P291S1 56/84 EXACT + cross-P291S0 73). AM
  16x12ch distinct; AC 80, b0-3 02/00/00/00 (b0 const
  02), no b4/b5, PBA sig 02000000 x16 PLAIN. CM 10x34ch
  10/10 diverge; CM sigs ORDERED 7+3 (08075220 x7 +
  84032910 x3, map order from CM rows); CC 65, b0-3 in
  tab, b9 const 00, no b4/b5 (C10-2SIG, b5 const 9c via
  lencode). M 16x14ch distinct. QR 4x20ch 4-distinct
  UNPAIRED; r0 c36f025c86d504c20dca distinct; r123 share
  6B 8b87eb584b65, byte6 9a/bf/e4; tails b84-87
  04c20dca/9a03613a/bf03613a/e403613a 4/4 distinct;
  r123 TRUE 3B 03613a; byte-LCS (0,*)=0, (1,2)=(1,3)=
  (2,3)=3 (computed first-hand). QC 69, b0-3 01000000,
  no b4/b5. RM 16x16ch distinct; RQ 16x14ch distinct;
  RC 71, b0-3 11/00/00/00, b84-87 be/a6/f6/d3 ring-wide.
  M==RQ EXACT 16/16 (lists identical). RM-vs-RQ UNPAIRED
  (sets disjoint). Tails STANDARD-SPLIT (RM b80-83 by
  COL, RQ b76-79 by ROW, 16/16 distinct each, 0 overlap).
  Sorted-unique + _N decls 80/65/69/71 match actual.
  Missing-sets EXACT: AC [4,5,6,7,80,81,82,83];
  CC [0,1,2,3,4,5,6,7,8,10,11,48,49,50,51,80,81,82,83];
  QC [4,5,6,7,13,14,15,52,53,54,55,80,81,82,83,84,85,86,
  87]; RC [4,5,8,9,10,13,14,15,19,76,77,78,79,80,81,82,
  83]. Coverage unions exact every block (const U tab U
  {b4,b5} == 88/84/88/88, 0 overlap). Q legs M[m] + QR[q],
  no frags. R legs RM[c] + RQ[r] STANDARD. AC-QC
  shared-pos 69, same-val 27, AConly 11, QConly 0 (==
  GATE, computed first-hand; NOT const-repeat). C-mtab
  M6 b6,7,80-83 parsed from code text vs P291 M8
  b40-43,80-83 (geometry change code-verified). P291 refs
  re-read: S0 5f6f1300 / S1 2b81c726 / PBA 02000000 (==
  P291 preds EXACT). P292 preds (A-730/A-355 Next-P292:
  436f1300/2b81e720/02000000/08075220x7+84032910x3)
  x4 corroborated. PBA REPEAT vs P291 (02000000 ==
  02000000). QUAD sig 01000000 (back to 01 after P291
  FRAG). QR 0-overlap vs P291QR. AM 0-overlap vs P291AM
  (true novelty). Widths differ (M 14ch vs 8ch, AM 12ch
  vs 16ch, CM 34ch vs 32ch, QR 20ch vs 24ch, RM 16ch vs
  18ch, RQ 14ch vs 16ch, base widths re-read first-hand).
  M-tails 16/16 ALL NEW vs P291 M-tail8 + P291 RM-tail8
  + P291 RQ-tail8 (overlap 0 x3). Memo INCL PBA88 81 /
  C10 66 / quad88 69 / T88 71 (A-733 re-read): impl
  80/65/69/71 = memo-1 on PBA/C10 (b5-const excluded),
  identical quad/T88. Base temp maxes _t6094/_b3692/
  _i3693 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 118353 / S1 118354 / A 118355-370 / C 118371-380 /
  Q 118381-444 / R 118445-700): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-consts emerge from raw lencode) + R
  counter b4=(0x5b+2off)&FF b5=0x9d+(off>=83)+(off>=211)
  (py hex; C stages decimal 91/157, re-derived from
  code text both sides) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions exact
  (A 6B b6,7,80-83; C 17B b0-3,6-8,10,11,48-51,80-83; Q
  QM7 b13-15,80-83 + R10 b6,7,52-55,84-87; R TM8
  b8,9,10,19,80-83 by COL + TR7 b13,14,15,76-79 by ROW)
  + NO frag leg in Q. T-mirrors T79244/79249/79254/
  79269/79286/79307 each re-read: hits the exact py guard
  line. C guards `if ((n) == (118353))` / `(118354)` +
  4 range guards exact. C byte-index lists match py per
  block (A 6B, C 17B, Q 7B/10B, R 8/7B). Temps
  _t6095-6110 continuous (base max _t6094) + _b3694/
  3696/3698/3699/3701/3702 (base max _b3692) + _i3695/
  3697/3700/3703 (base max _i3693): base-tree zero refs
  to new temps prove no reuse. Insert exact both sides:
  after T10P291R close, at dispatch tail (N-out-of-scope
  fallthrough follows). Matches A-733/A-356 geometry
  (values re-checked in audit above; NO D dips: ownloop
  tags exactly the 6 P292 blocks).
- Edges own-loop ownloop400.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P292R N=118700 off=255.
  edges400.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 a3/9c, a5/9c == raw lencode) +
  aform 16/16 (A 88B head a7/9c tail c5/9c b5set {9c} NO
  step, 0 ff) + cform 10/10 (C head c7/9c tail d9/9c
  b5set {9c} NO step, 0 ff) + qform 64/64 + qb5step 64/
  64 (Q head db/9c tail 59/9d b5set {9c,9d} step o18->o19:
  118399 o18 ff/9c -> 118400 o19 01/9d, exactly 1 ff in
  64 at o18; quad b4 formula == raw-lencode 64/64); ring
  counter 256/256 + ringraw 256/256 (head 5b/9d; 118527
  off82 ff/9d -> 118528 off83 01/9e; mid off128 5b/9e;
  118655 off210 ff/9e -> 118656 off211 01/9f; tail
  off255 59/9f; exactly 2 ff in 256 at o82/o210; Q tail
  59/9d vs R tail 59/9f differ in b5 -- labeled apart);
  odd-lencode 348/348. Ring edges + tail 118700 in
  for-list + 2 PASS lines each py+C. Tail 118700:
  oracle sha fd1fd3760a110342... matches PINS; py+C
  CLOSED T10P292R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf400.py (cache path) + secf400b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (118353 +
  118005 + 118354 + 118006); S0: oracle118353-vs-118005
  34/84, codeS0-vs-P291S0 34/84, positions identical;
  DIRECT tool 34/84 with identical agree-pos 50
  positions. S1: oracle 56/84, code 56/84, positions
  identical; DIRECT 56/84 identical agree-pos 28
  positions. 0 miss (ownloop pre-warmed). Twice-derived
  both pairs. No byte-equal wording in A-733/A-356 this
  band (both stage NEW sigs) -- byte-diff discipline
  observed, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 231/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 231
  content / 0 del. Fine-norm (temp-norm, empty-
  excluding): del-uniq 0 add-uniq 418 missing 0 ==
  GATE EXACT (first-hand, no reconstruction needed;
  this GATE states the temp-norm recipe explicitly).
  del-subset-add 0 missing holds (integrity intact).
- Wall on band diff added lines (scope d5de4afe..
  3c2b2e00, 898 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (2dbda75a), code 6 blocks,
  py top-level singletons (^4sp `if n == `) 606->608 +2
  == GATE stated-method EXACT, py T10P range guards
  598->602 +4 == GATE EXACT, CLOSED T10P prints 1640->
  1646 +6 py + 1640->1646 +6 C, C top-level singleton
  `if ((n) == (` 606->608 +2 == GATE EXACT / C top-level
  ranges 598->602 +4 == GATE EXACT (broad-C recipe 611->
  613 / 620->624, +5/+22 nested offset pre-existing +
  unchanged), seal 1734->1740 +6 (commit msgs): all agree,
  no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-733-q884-
  t10p292 verdict CONFIRM, tallies 14/14 + 11/11 + 12/12
  as-filed (file present, read in full; NOTE 14+11+12=37
  vs verdict line 35/35 -- memo-internal arithmetic
  irreproducible; methodology note, NO verdict impact) +
  exact-value corroboration incl PB0 NEW + PB1 NEW,
  PBA88-PLAIN, C10-2SIG 7+3 map, QUAD88-4R + R10 rows +
  6B-share + r123-TRUE-3B + r0-lcs0 + b5 step + edge +
  M-tails NEW, ring STANDARD + TM8/TR7 16/16 UNPAIRED +
  edges + consts (all re-checked above) + A-356 viewer
  corroboration (CONFIRM all legs, consts 81/66/69/71
  INCL). No CONFIRM-P292.md file (absence verified);
  A-733 suffices per rule. Agrees with cport commit msg
  (PYID 8624, RGRAM 17248).
- Quiz: no conflicting CLAIM/GATE/FLAG on b400 (own seat
  CLAIM only; NO-FLAG greps first-hand). Newest
  PARENT-QNUM-22 (w2e Q-block grant, read, no gate
  impact) -- GATE cites no QNUM (no staleness). PROSE-01:
  all hex/counts above copied from own run output; GATE
  re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 0 prose slips (norm recipe stated explicitly this
band, temp-norm 418 reproduced EXACT with no variant
gap; tier recipes reproduced EXACT via top-level-guard
reading).
Next-P293 predictions banked (A-733/A-356: PB0 @118701
03291000 NEW / PB1 @118702 3b635420 NEW / PBA88 02000000
x16 @118703-18 / C10-1SIG 2b8b4e20 x10 @118719-28
SINGLE-sig map TBD-settled).
