# VERIFY-f278bdf0 b426 T10P318 pins 127401..127748 (1896 tiers) PASS

Seat viewer-r64, first-hand, tree @f278bdf0,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r64.
Base d1c18b6c (b425 tip, 1890 tiers sealed; odd-seat GATE-filed
PASS-functional, even base-use only, respected). Band =
dbcef7b4 (py merge w2b@76bf89ba partial, +6 tiers, +62 pins)
+ f278bdf0 (C port, 1896 sealed). Trees manifest-identical
to tips (git ls-tree vs git ls-files identical both;
WT detached at band, will return to lanes/encode-viewer
at round end).

Banked Next-P318 shape (r63 from A-816, refined by A-823)
CONSUMED FIRST and corroborated below: PB0 36ac6c01 pay84
NEW-sig (repeat era ENDS) @127401 / PB1 02000000 pay88
sig-eq-P317PB1 58/88 @127402 / PBA88 27000000 x16 @127403-18 /
C10-region 02000000 pay88 x10 @127419-28 -- all exact.

- Build: make -C src/c BUILDDIR=build426 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc 3cdda4dc3206cedc2e7f
  247f585baaad905a0bd2aff9e8d18688989efee43976 / aae
  d6e27c97ced21673cc73eee061ffdbd7f0358a87e482056c222a
  867202110785 (== GATE sha256 both; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 9439/9439 covered=9439/9439 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir; first attempt failed
  rc=2 with RGRAMC pointed at the build directory
  instead of the binary -- invocation error, fixed,
  re-ran GREEN).
- RGRAM py 18878/18878 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18878/18878 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18878/18878;
  GATE claims ordered+raw, both corroborated).
- PINS 18880 rows (2 hdr + 18878, +62 vs base 18818);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq). For-list union delta
  vs base +31/-0 (9408->9439):
  127401 127402 127403 127404 127410 127411 127417
  127418 127419 127420 127423 127424 127427 127428
  127429 127436 127444 127445 127461 127477 127487
  127488 127491 127492 127493 127600 127615 127616
  127743 127744 127748
  (== GATE list EXACT, verified programmatically).
  Decomposition first-hand from the added set: 2 sing
  (127401/02) + A head/mid/tail pairs (6: 03/04 +
  10/11 + 17/18; offs 0,1,7,8,14,15) + C head/mid/tail
  pairs (6: 19/20 + 23/24 + 27/28; offs 0,1,4,5,8,9)
  + Q head 29/mids 36/44/45/61/77/edge-pair 87/88/
  tail-pair 91/92 (10: offs 0,7,15,16,32,48,58,59,62,
  63; step@59 edge pair pinned + tail pair, first-hand)
  + R head 93/mid 600/edge-pairs 615/616 + 743/744/
  tail 748 (7: offs 0,107,122/123,250/251,255; 1-mid
  shape, both counter edges pair-covered, first-hand).
  31x2=62 rows, range 127401..127748 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked first-hand (`import lz4` Traceback, same
  as r60-r64 record); band touches no proto/ sources
  (numstat proves), NO verdict impact.
- Tables audit own script tabaudit426.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 134 PASS
  0 FAIL. Inventory exactly the 12 both sides, C==py
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F anywhere --
  0 hits both sources; no F0/F1, no QT/RT/TT, no BM/BC,
  no M19/X19, no M42/X42/H42/L42, no QB/PT/FM).
  S0 168ch sig 36ac6c01 NEW-sig (differs first-hand vs
  P317 head sigs 57a75201/02000000; 37/84 payload diff
  vs P317S0, repeat era ENDS confirmed) / S1 176ch sig
  02000000 sig-eq-P317S1 (58/88 payload diff vs P317S1
  @ b4,5,11,16-19,22-28,30,31,33,34,36-47,56-79,84-87
  first-hand, NOT byte-equal; 49/88 diff vs own-C10[0]
  assembled, NOT byte-equal; sig SAME-as-own-C10;
  differs vs own PB0), staged as full-payload singletons.
  AM 16/16 16ch distinct, AC 78, b0-3 27000000 (b0
  const 27), no b4/b5. C10-1SIG-88-M5b45 sig 02000000
  x10 SAME-as-PB1 (sig in CC b0-3 consts; CM 10/10
  diverge 10ch heads 21x8+61,61 tails 1782/3782/5782/
  7782-e3d6 x4 + 3/5/7/9-ec7fcd6 x4 + 38ae7614 +
  1adb364d first-hand; CC has no b4/b5, b5 const e3
  full block via lencode).
  S1-vs-own-C10 staged per-cell (M5 b45,84-87, each cell
  own lencode) [49]x10 TRUE-UNIFORM count+position
  (cell0 49 @ 4,11,19,38-79,84-87 EXACT; positions
  identical all 10 staged AND oracle; sig 02000000 both,
  NOT byte-equal -- 14th TRUE-uniform case on record,
  13th excluding unverified P299; beyond-GATE values
  corroborated by oracle leg below; see prose note on
  the GATE's cell0 position list).
  QUAD88-2SIG-4R (row0 27000000 x16 SAME-sig-as-PBA +
  rows1-3 15000000 x48; QM7 b52-54,80-83 shared 16/16
  x3 vs row0, NO frags + R34 b0,8-15,19,25-35,38,39,
  45-51,84-87 rows 4/4 NO pairing pairwise-disjoint
  (r0 27-led fully distinct, r123 15-led, r2/r3 share
  60ch non-tail prefix, differ in tails) + tails b84-87
  4 distinct 3adb364d/392fd794/0d5f067f/325f067f, r2r3
  TRUE-3B 5f067f (differ b84 0d/32), r0/r1 lcs0 vs all
  rows, r2r3-lcs3; b0 row-led split r0=27/r123=15
  (b1-3 const 00 in QC).
  M==RQ 16/16 FULL string-identical INTRA-tier (list
  equality, not just sorted), SAME byte positions
  (QM7/TR7 b52-54,80-83 both sides; M 14ch vs RQ 14ch
  full strings identical; m=off&15 vs r=off>>4
  subscripts differ only in index direction; running
  pattern: b414 full-eq, b416 tail-eq, b418 full-eq,
  b420/b422 string-eq-positions-differ, b424 tail-eq-
  positions-differ, b426 full-eq). Even-band RQ==M
  takes no ordinal (viewer chain convention). Memo-
  silent on the relation (b426 unmentioned by memo).
  Ring SWAPPED: sig 55010000 x256; TM6 b6,7,76-79 by
  COL RM 16/16 + TR7 b52-54,80-83 by ROW RQ 16/16
  UNPAIRED (tails SWAPPED b76-79 col / b80-83 row;
  subscripts + tail positions verified in dispatch
  text both sides); RM 16/16 12ch + RQ 16/16 14ch
  distinct, sets disjoint; b0 const 55 b1 const 01;
  b84-87 535f6858 ring-wide NEW (P317 3f010000/
  bf2724fb single-sig era).
  Sorted-unique + _N decls 78/81/45/73 match actual.
  Missing-sets EXACT: AC-10 [4,5,38,39,46,47,80-83]
  (b4,b5+M8b38); CC-7 [4,5,45,84-87] (b4,b5+M5);
  QC-43 (b0,b4,b5+QM7+R34, table-verified count +
  coverage structure); RC-15 [4,5,6,7,52-54,76-83]
  (b4,b5+TM6+TR7). VPOS 9/6/43/15 == A-824 EXACT (PBA
  b4+M8 b5-const-excluded / C10 b4+M5 / quad
  b0,b4,b5+QM7+R34, b0 in tab / T b4,b5+TM6+TR7, b0
  const-excluded). Coverage unions exact every block
  (const U tab U {b4,b5} == 88 x4, 0 overlap).
  Q legs M[m] + QR[q] both sides, NO F-legs in Q;
  R legs RM[c] + RQ[r] both sides, NO F-legs in R
  (STANDARD RM-col / RQ-row verified in region text).
  P317 refs re-read: S0 57a75201 / S1 02000000 /
  PBA 28000000 / C10 02000000 / QUAD 2SIG 2a/13.
  PBA sig 27 NEW vs P317 28 (27000000 != 28000000);
  QUAD 2SIG 27/15 vs P317 2SIG 2a/13 (row0 keeps PBA
  sig, rows1-3 NEW 15 vs 13). AC-QC both=45 sameval=19
  (tables differ) -- recorded first-hand (no GATE
  claim). M-tails 16/16 ALL NEW vs P317 (zero overlap
  vs P317M AND vs P317RM-tail8 AND vs P317RQ-tail8 --
  P317 widths M8/RM16/RQ14 re-read first-hand).
  RM-tails NEW vs P317RM col-led + RQ-tails NEW vs
  P317RQ row-led + cross overlaps 0 (position-aware
  col-led/row-led).
  Memo INCL PBA88 79 / C10 82 / quad88 45 / T88 73
  (A-824 re-read): impl 78/81/45/73 = writer-1 on
  PBA/C10: impl tables still deduct const-b5 on PBA/
  C10 (b5 covered by lencode instead) while Q-910
  sheet counts b5 (memo A-824 confirms the sheet) --
  S-F arithmetic persists in committed tables though
  the sheet is FIXED; geometry exact, PORT verdict
  stands; memo-exact on quad (b5 STEP-varies, in tab)
  and T88 (b5 varies, no deduction). 21st consecutive
  tables-lag band (b426 pattern +1/+1/+0/+0: PBA/C10
  lag; running b412-b426 per GATE + r63/r64 records).
  Base temp maxes _t6536/_b3953/_i3954 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 127401 / S1 127402 / A 127403-18 / C 127419-28 /
  Q 127429-492 / R 127493-748): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C both sides (b5
  const e3 emerges from raw lencode, NO step) + Q/R
  explicit counters both sides (Q b4=(0x8b+2off)&FF
  b5=0xe3+(off>=59); R b4=(0x0b+2off)&FF b5=0xe4+
  (off>=123)+(off>=251); py hex 0x8B/0xE3/0x0B/0xE4;
  C staged literals 139/227 + 11/228, re-derived:
  139==0x8b, 227==0xe3, 11==0x0b, 228==0xe4) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 8B b38,39,46,47,
  80-83; C 5B b45,84-87; Q QM7 b52-54,80-83 + R34
  34B b0,8-15,19,25-35,38,39,45-51,84-87, NO frags;
  R TM6 b6,7,76-79 by COL + TR7 b52-54,80-83 by ROW,
  SWAPPED tails) + C guards `if ((n) == (127401))` /
  `(127402)` + 4 range guards exact + counter literals
  exact + C byte-index lists match py per block (A 8B,
  C 5B, Q 7B/34B, R 6B/7B). T-mirrors T85562/85567/
  85572/85587/85602/85627 each re-read: hits the exact
  py guard line (85562/85567/85572/85587/85602/85627);
  C mirrors identical numbers in comments. Temps
  _t6537.._t6552 continuous-16 (base max _t6536) +
  _b3955/3957/3959/3960/3962/3963 (base max _b3953) +
  _i3956/3958/3961/3964 (base max _i3954): added-only,
  no reuse.
  Insert exact both sides: after T10P317R close (py
  CLOSED 85560, guard 85562; C 227771-73, block 227774),
  at dispatch tail (N-out-of-scope fallthrough follows:
  py 85646 + C 227981; 2 scope hits py + 2 scope hits
  C). Matches A-824 geometry (values re-checked in
  audit above; NO D dips: ownloop tags exactly the 6
  P318 blocks).
- Edges own-loop ownloop426.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (302 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P318R N=127748
  off=255. edges426.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 53/e3, 55/e3
  == raw lencode) + aform 16/16 (A head 57/e3 tail
  75/e3 b5set {e3} NO step, 0 ff) + cform 10/10 (C
  head 77/e3 tail 89/e3 b5set {e3} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head 8b/e3 edge
  off58->59 127487->127488 ff/e3->01/e4 tail 09/e4,
  b5set {e3,e4} STEP e3->e4 @off59; quad b4 base 0x8b
  step2 64/64 range 8b..09 NO edge, tail 09/e4 exact)
  + ring counter 256/256 + ringraw 256/256 (head
  0b/e4; 127615 off122 ff/e4 -> 127616 off123 01/e5;
  127743 off250 ff/e5 -> 127744 off251 01/e6; tail
  09/e6; exactly 2 ff in 256 at o122/o250); ff total
  x3 (Q-edge + 2 ring); ff-in-Q 1. odd-lencode
  92+256=348/348. Ring edges + tail 127748 in for-list
  + 2 PASS lines each py+C. Tail 127748: oracle full-
  rav sha 47a4c60d3c92262e... == PINS 64-hex FULL match
  (rawlen 104 re-checked: paylen 88 + 12 + 4); py+C
  CLOSED T10P318R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf426.py (cache path) + secf426b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (127401 +
  127053 + 127402 + 127054); S0: oracle127401-vs-127053
  37/84, codeS0-vs-P317S0 37/84, positions identical;
  DIRECT tool 37/84 with identical agree-pos 47
  positions. S1: oracle127402-vs-127054 58/88,
  codeS1-vs-P317S1 58/88, positions identical; DIRECT
  58/88 identical agree-pos 30 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf426c.py (oracle C10
  cells n127419-28): [49]x10 TRUE-UNIFORM counts AND
  positions identical all 10 (cell0 pos
  4,11,19,38-79,84-87 == staged EXACT; sig 02000000
  both, NOT byte-equal). Byte-diff discipline observed
  throughout, nothing to refute.
- C diff pure-add: numstat 607/0 (rgramc.c) + 232/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 602 content + 5 bare-blank / 0 del (verified
  bare, no whitespace) == GATE; full-digit norm
  ([0-9]+ -> N): C del-uniq 0 add-uniq 149/146/148/145
  across the 4 strip/dropempty variants, missing 0
  every variant; py del-uniq 0 add-uniq 170 all four
  variants, missing 0 (integrity intact, no GATE
  claim). C-tempnorm del-uniq 0 add-uniq 398 missing 0
  == GATE EXACT. Band-level sole del = old for-line
  churn (1/1).
- Wall on band diff added lines (scope d1c18b6c..
  f278bdf0, 902 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 607/0,
  rgram.py 232/0 purely additive, test_rgram.sh 1/1
  (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62 (dbcef7b4), code 6 blocks,
  dispatch-guards (4-space dispatch-exact) singletons
  658->660 +2 / ranges 702->706 +4 = +6, C identical
  deltas 658->660 +2 / 702->706 +4 (py=C dispatch-exact;
  no else-if either side, deltas agree every side; the
  all-indent literal method gives py 668->670 +2 /
  724->728 +4 with 10 nested singletons + 22 nested
  ranges pre-existing both sides, C all-indent 663->
  665 +2 (5-count offset pre-existing, unchanged:
  668-663 = 670-665 = 5) -- deltas agree under every
  method, no slip), CLOSED T10P prints 1796->1802 +6
  py + 1796->1802 +6 C, seal 1890->1896 +6 (commit
  msgs; offset +94 vs CLOSED-T10P: 1896-1802 = 94,
  stable b401-b426): all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-824-q910-P318
  verdict CONFIRM 65/65 CLEAN (Q1 shape + Q2 quad+T +
  Q3 counters, verifier v210.py 65/65 PASS; file
  present; exact-value corroboration incl PB0 NEW-sig
  36ac6c01 (repeat era ENDS), PB1 sig-eq-P317PB1 58/88
  NOT-byte-equal SAME-as-C10 49/88, PBA88-PLAIN-M8b38
  sig-27 b0-const-27 b5-const-e3 16/16 distinct NO
  pair M8, C10-M5b45 SAME-as-PB1-sig b0-const-02
  b5-const-e3 10/10 diverge, QUAD88-2SIG-4R
  row0-same-as-PBA + R34 rows + share-60ch + r2r3-
  TRUE-3B + r0/r1-lcs0 + r2r3-lcs3 + QM7 b52-54 + NO
  frags + b5-step + M-tails NEW, T88-RING-SWAPPED +
  TM6/TR7 + swapped-split + b84-87 535f6858 + counter
  0b/e4/123/251 + lencode 348/348 (all re-checked
  above); plus sheet-vs-tables const-count note:
  Q-910 sheet 79/82/45/73 memo-exact, committed
  tables 78/81/45/73 still deduct const-b5 on PBA/C10
  -- 21st consecutive tables-lag band, geometry exact,
  PORT verdict stands). Agrees with cport commit msg
  (PYID 9439, RGRAM 18878). No viewer P318 geometry
  answer on file at gate time (memo-only recon; this
  VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b426 (own seat
  CLAIM only; exactly 1 GATE-f278bdf0; zero FLAG hits
  on b426/f278bdf0/T10P318/127401; next-band
  GATE-49f9f3e4 uses b426 as base = adjacency; older
  GATE-c72b0b57 references b426 tip = note, no verdict
  on b426; odd bases b425/b427 respected). PROSE-01:
  all hex/counts above copied from own run output;
  GATE re-read in FULL before filing.
- RQ==M chain: b426 even FULL-eq (M==RQ list-identical,
  same byte positions QM7/TR7 b52-54,80-83; M 14ch vs
  RQ 14ch). Even band takes no ordinal. Memo-silent on
  the relation. Running even pattern now b414-full/
  b416-tail/b418-full/b420-strdiff/b422-strdiff/
  b424-tail-pos-differ/b426-full.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 prose-level notes (tail-sha prefix "1a994922
580a5183" matches neither full-rav sha (47a4c60d3c
92262e == PINS 64-hex full) nor pay-only sha -- value
not from this band's run output; S1-vs-C10 cell0
position list "b4,9-14,20-43,57-65,80-87" is wrong --
first-hand staged AND oracle both give 49 @
4,11,19,38-79,84-87 with [49]x10 uniformity + identical
positions all 10; count + uniformity corroborated,
positions corrected). AC-QC both=45 sameval=19 recorded
first-hand (no GATE claim). Next-P319 SHAPE banked
(A-824 re-read: PB0 36ac2c01 pay84 NEW @127749 (30/84
diff vs P318PB0) / PB1 02000000 pay88 @127750 (68/88
diff vs P318PB1) / PBA88 25000000 x16 @127751-66 /
C10-region 02000000 pay88 x10 @127767-76).
