# VERIFY-85fc4505 b418 T10P310 pins 124617..124964 (1848 tiers) PASS

Seat viewer-r62, first-hand, tree418 @85fc4505,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r62.
Base 88ea719c (b417, 1842 tiers). Band = 00b6e14c (py merge
w2b@fa0bb2c1 partial, +6 tiers, +62 pins) + 85fc4505 (C port,
1848 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117/117).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build418/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 048c2e3388dc631e / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  0d2fd6f2c2dc804a / aae 7d8dd3a2d118e0db (recorded, no
  GATE claim).
- RGRAMC-PYID 9184/9184 covered=9184/9184 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 18368/18368 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 18368/18368 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18368/18368).
- PINS 18370 rows (2 hdr + 18368, +62 vs base 18308);
  PASS-names vs PINS-names xor 0 py+C; py-vs-C xor 0;
  base-N vs for-list xor 0 (4-way set-eq). For-list
  delta vs base +31/-0:
  124617 124618 124619 124620 124626 124627 124633 124634
  124635 124636 124639 124640 124643 124644 124645 124652
  124661 124671 124672 124677 124684 124693 124700 124708
  124709 124799 124800 124850 124927 124928 124964
  (== GATE verbatim: S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,4,5,8,9 + Q10 offs 0,7,16,26,27,32,39,48,
  55,63 (head/8-mids/tail, b5-step edge pair 124671/
  124672 off26/27 pinned) + R7 offs 0,90/91,141,218/
  219,255 (head + both counter edges straddled + mid
  124850 + tail); 9153->9184); 31x2=62 rows, range
  124617..124964 exact. PINS-new-N == for-added 31/31,
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60-r62); band
  diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit418.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 143 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-TAILTAB/QUAD88-4R-STEP/RING-SWAPPED; no F/
  F0/F1, no QT/RT, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42); C==py 12/12. S0 168ch sig
  ebfd8700 NEW (33/84 vs P309S0 first-hand, positions
  in log; no GATE count claimed) / S1 176ch sig
  01000000 sig-eq-P309PB1 (48/88 vs P309S1 EXACT, NOT
  byte-equal). S1-vs-C10[0] staged assembly 49/88
  NOT-byte-equal (C10[0] own lencode b7/cd @124635
  re-derived). AM 16x16ch distinct; AC 78, b0-3
  15000000 (b0 const 15), no b4/b5, PBA sig 15000000
  x16 PLAIN (NEW sig 15; M8 b38,39,46,47,80-83). CM
  10x8ch 10/10 diverge, values 8cc2305a/9550325a/
  aec2375a/cec2375a/eec2375a/0ec3375a/2ec3375a/
  f9d6215d/38d7215d/58d7215d EXACT (M4 b84-87 tails-
  only); CC 82, b0-3 01000000 SAME-as-PB1-sig, b80-83
  const 55fc3237, no b4/b5 (b5 const cd via lencode).
  M 16x18ch distinct (QM9 b51-55,80-83, shared NO
  frags). QR 4x24ch 4-distinct UNPAIRED; r0
  640b9b270f74325f50eea792 distinct; r123 share 16ch
  94cddb021ff48676; tails b84-87 50eea792/bd5b21bb/
  e8b01dc8/0db11dc8 4/4 distinct; r2r3 2B pair-only
  1dc8 (heads e8b0/0db1 differ); full-row lcsuf
  (2,3)=2 else 0 (r0-vs-all 0 AND r1-vs-all 0 --
  r1 bd5b21bb joins r0 in isolation; first 2B-pair
  variant, memo-agreed) + lcpre r123 8, r0-vs-rest 0.
  QC 65, b0-3 0a000000, no b4/b5 (QUAD single-sig
  x64). RM 16x16ch distinct; RQ 16x18ch distinct;
  RM-vs-RQ UNPAIRED (sets disjoint); RC 69, b0-3
  a0000000, b84-87 b14ee351 ring-wide NEW. M==RQ
  lists identical 16/16 (same byte positions
  b51-55,80-83 QM9/TR9; agree-matrix diagonal 16/16
  all 9; even-band FULL identity, no ordinal per
  even/odd convention; GATE's running-pattern remark
  "b414 full-eq" beyond window, not disputed --
  b416 tail-eq corroborated this round). Tails
  SWAPPED (RM b76-79 by COL c=off&15, RQ b80-83 by
  ROW r=off>>4 -- subscripts verified py+C; 16/16
  distinct each, 0 overlap). Sorted-unique + _N
  decls 78/82/65/69 match actual. Missing-sets EXACT:
  AC [4,5,38,39,46,47,80-83]; CC [4,5,84-87] (M4
  tails-only); QC [4,5,38,39,45-55,80-87] (23); RC
  [4,5,6-9,51-55,76-83] (19). VPOS 9/5/23/19 ==
  A-798 EXACT (C10 {4,84-87}; quad b5 varies
  included). Coverage unions exact every block
  (const U tab U {b4,b5} == 88 x4, 0 overlap). Q
  legs M[m] + QR[q] both sides, NO F-legs either
  side. R legs RM[c] + RQ[r] both sides, NO F-legs.
  AC-QC shared-pos 65, same-val 27, AConly 13,
  QConly 0 (computed first-hand). P309 refs re-read:
  S0 ab689400 / S1 01000000 / PBA 12000000 / C10
  01000000 / QUAD 08000000 x64. Next-P310 preds
  (A-796 re-read: PB0 ebfd8700 NEW / PB1 01000000
  48/88 / PBA88 15000000 x16 / C10-region 01000000
  pay88 x10) x4 corroborated (banked-from-r62
  CONSUMED). PBA NEW vs P309 (15000000 != 12000000);
  QUAD single-sig 0a vs P309 08. AM/CM/M/QR/RM/RQ
  0-overlap vs P309 (widths P310 AM16/CM8/M18/QR24/
  RM16/RQ18 vs P309 AM12/CM20/M20/QR22/RM14/RQ18
  chars, base widths re-read first-hand). M-tails
  16/16 ALL NEW vs P309 M-tail8 + RM-tail8 + RQ-tail8
  (overlap 0 x3; P309 widths M20/RM14/RQ18 re-read).
  Memo INCL PBA88 79 / C10 83 / quad88 65 / T88 69
  (A-798 re-read): impl 78/82/65/69 = memo-1 on PBA/
  C10 (b5-const excluded), identical quad (b5 step)/
  T88 (counter) -- standing +1 rule coherent,
  +1/+1/+0/+0. Base temp maxes _t6392/_b3873/_i3874
  (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 124617 / S1 124618 / A 124619-634 / C 124635-644 /
  Q 124645-708 / R 124709-964): bounds + paylens
  (1x84 + 347x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (QUAD-STEP o26->o27 emerges from raw
  lencode; code text "b5 0xcd+(off>=27) step edge
  off26->27" re-read) + R counter b4=(0x4b+2off)&FF
  b5=0xce+(off>=91)+(off>=219) (py hex 0x4B/0xCE/91/
  219; C staged decimal 75/206, re-derived: 75==0x4b,
  206==0xce) + m=off&15/q=off>>4/c=off&15/r=off>>4
  both sides + mtab/rtab byte positions exact (A 8B
  b38,39,46,47,80-83; C 4B b84-87 tails-only; Q QM9
  b51-55,80-83 + R12 b38,39,45-50,84-87, NO frags; R
  TM8 b6-9,76-79 by COL + TR9 b51-55,80-83 by ROW,
  SWAPPED tails-last) + C guards `if ((n) ==
  (124617))` / `(124618)` + 4 range guards exact + C
  byte-index lists match py per block (A 8B, C 4B, Q
  9B/12B union 21 disjoint+b4/b5, R 8B/9B union 17+
  b4/b5). T-mirrors T83522/83527/83532/83547/83562/
  83584 each re-read: hits the exact py guard line.
  Temps _t6393-6408 continuous-16 (base max _t6392) +
  _b3875/3877/3879/3880/3882/3883 (base max _b3873)
  + _i3876/3878/3881/3884 (base max _i3874):
  added-only, no reuse. Insert exact both sides:
  P309R block precedes (C 222681-83, block 222684;
  py CLOSED 83520, guard 83522), at dispatch tail
  (N-out-of-scope fallthrough follows: C 222875, py
  83604). Matches A-798 geometry (values re-checked
  in audit above; NO D dips: ownloop tags exactly
  the 6 P310 blocks).
- Edges own-loop ownloop418.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (0 miss-warmed -- cache pre-warmed). Census
  R256/Q64/A16/C10/S0/S1 exact. Tail line: CLOSED
  T10P310R N=124964 off=255. edges418.py: paylens
  1x84 + 347x88; lencode 92/92 (S/A/C/Q raw l16;
  S0/S1 93/cd, 95/cd == raw lencode) + aform 16/16
  (A head 97/cd tail b5/cd b5set {cd} NO step, 0 ff)
  + cform 10/10 (C head b7/cd tail c9/cd b5set {cd}
  NO step, 0 ff) + qform 64/64 + qb5step 64/64 (Q
  head cb/cd, edge o26->o27 124671->124672 ff/cd->
  01/ce, tail 49/ce, b5set {cd,ce}, exactly 1 ff in
  64 at o26; quad b4 base 0xcb step2 == raw-lencode
  64/64); ring counter 256/256 + ringraw 256/256
  (head 4b/ce; 124799 off90 ff/ce -> 124800 off91
  01/cf; mid off141 65/cf at 124850; 124927 off218
  ff/cf -> 124928 off219 01/d0; tail off255 49/d0;
  exactly 2 ff in 256 at o90/o218; Q tail 49/ce vs
  R tail 49/d0 differ in b5 -- labeled apart); ff
  total x3 (Q-step o26 + 2 ring). odd-lencode
  92+256=348/348. Ring edges + tail 124964 in
  for-list + 2 PASS lines each py+C. Tail 124964:
  oracle sha d6aa36de2d921a2d... matches PINS (rawlen
  104 re-checked: paylen 88 + 12 + 4); py+C CLOSED
  T10P310R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf418.py (cache path) + secf418b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (124617 +
  124269 + 124618 + 124270); S0: oracle124617-vs-124269
  33/84, codeS0-vs-P309S0 33/84, positions identical;
  DIRECT tool 33/84 with identical agree-pos 51
  positions. S1: oracle124618-vs-124270 48/88,
  codeS1-vs-P309S1 48/88, positions identical; DIRECT
  48/88 identical agree-pos 40 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf418c.py (oracle C10
  cells n124635-644): 49/88 TRUE-UNIFORM all 10
  ([0] n124635 49/88 @ b4,11,19,38-55,60-87 ==
  GATE staged-assembly count EXACT; counts [49]x10
  AND positions identical all 10 -- verified beyond
  GATE's cell0 staged assembly; sig 01000000 both,
  NOT byte-equal). Byte-diff discipline observed
  throughout, nothing to refute.
- C diff pure-add: numstat 608/0 (rgramc.c) + 232/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 603 content + 5 bare-blank / 0 del == GATE
  EXACT; raw py 232 content / 0 del. C-tempnorm
  del-uniq 0 add-uniq 379 missing 0 == GATE EXACT
  (recipe stated explicitly: rgramc.c scope,
  _tN/_iN/_bN temp-norm, empty-excluding -- no
  variant gap, b412/b414/b416 family). Full-digit
  norm recorded (no GATE claim): C 151/148/150/147 +
  py 172 x4, del-uniq 0 missing 0 every variant
  (integrity intact). py-tempnorm 186 recorded.
- Wall on band diff added lines (scope 88ea719c..
  85fc4505, 903 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (00b6e14c), code 6 blocks,
  dispatch-exact (4-space) singletons 642->644 +2 /
  ranges 670->674 +4 py + C identical 642->644 +2 /
  670->674 +4 (C broad 647->649 +2 / 692->696 +4,
  deltas +2/+4 every series == GATE), CLOSED T10P
  prints 1748->1754 +6 py + C == GATE EXACT, seal
  1842->1848 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1848-1754 = 94, stable b401-b418):
  all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-798-q902-P310
  verdict CONFIRM, tallies 28/28 + 16/16 + 14/14 =
  58/58 arith-consistent as-filed + exact-value
  corroboration incl PB0 NEW + PB1 sig-eq-P309PB1
  48/88 NOT-byte-equal SAME-as-C10 49/88, PBA88-PLAIN
  sig-15 M8, C10-TAILTAB SAME-as-PB1-sig M4,
  QUAD88-4R-STEP + R12 rows + share-16ch + r2r3-2B-
  pair-only + r0+r1-lcs0 + QM9 + NO frags + b5-step
  o26->o27 + M-tails NEW, T88-RING-SWAPPED + TM8/TR9
  16/16 UNPAIRED + SWAPPED tails + b84-87 b14ee351 +
  edges + consts 4b/ce/91/219 + lencode 348/348 +
  VPOS 9/5/23/19 (all re-checked above). Sheet-vs-
  tables const-count note: Q-902 sheet rule 79/83/
  65/69 memo-exact (7th straight fully clean w2b
  sheet per memo; w2b-r26 [3/8]), committed tables
  78/82/65/69 still deduct const-b5 in PBA/C10 --
  13th consecutive tables-lag band (geometry exact,
  PORT verdict stands). No viewer P310 geometry
  answer on file at gate time (memo-only recon; this
  VERIFY is the viewer record). No CONFIRM-P310.md
  file (absence verified); A-798 suffices per rule.
  Agrees with cport commit msg (PYID 9184, RGRAM
  18368).
- Quiz: no conflicting CLAIM/GATE/FLAG on b418 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites no
  QNUM (no staleness). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE FULLY CORRECT on code +
behavior + prose legs; 0 prose notes (sweep2-r67's
"share-16ch" uses correct units; no token slip, no
norm gap -- C-tempnorm recipe stated explicitly and
reproduces EXACT). Even-band RQ==M instance
corroborated as FULL identity (M==RQ lists 16/16,
same positions b51-55,80-83; no ordinal per even/odd
convention; convention holds). Next-P311 SHAPE banked
(A-798 re-read: PB0 ebfda700 NEW pay84 @124965 / PB1
01000000 pay88 @124966 sig-repeat 80/88 / PBA88
14000000 x16 @124967-82 / C10-region 01000000 pay88
x10 @124983-92 -- same novel shape continues).
