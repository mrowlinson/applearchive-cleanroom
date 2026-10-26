# VERIFY-adf40836 b419 T10P311 pins 124965..125312 (1854 tiers) PASS

Seat viewer-r62, first-hand, tree419 @adf40836,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r62.
Base 85fc4505 (b418, 1848 tiers). Band = 91e2afc7 (py merge
w2b@32751af3 partial, +6 tiers, +62 pins) + adf40836 (C port,
1854 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117/117).

- Build: make -C src/c BUILDDIR=build419 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc 184d5ed471c98a84 / aae
  d6e27c97ced21673 + sha1 rgramc 3de9452d08e3c48f / aae
  7d8dd3a2d118e0db (== GATE all four; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 9215/9215 covered=9215/9215 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18430/18430 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18430/18430 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18430/18430;
  GATE claims sorted only, raw corroborated too).
- PINS 18432 rows (2 hdr + 18430, +62 vs base 18370);
  PASS-names vs PINS-names xor 0 py+C; py-vs-C xor 0;
  base-N vs for-list xor 0 (4-way set-eq). For-list
  delta vs base +31/-0:
  124965 124966 124967 124968 124974 124975 124981 124982
  124983 124984 124987 124988 124991 124992 124993 125000
  125009 125016 125025 125032 125041 125048 125055 125056
  125057 125120 125183 125184 125250 125311 125312
  (== GATE decomposition: 2 sing + A6 offs 0,1,7,8,14,15
  + C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 124985/124986/
  124989/124990 unsampled, absence verified) + Q10 offs
  0,7,16,23,32,39,48,55,62,63 (per-row m0/m7 + tail pair
  = P309 shape first-hand; tail pair covers STEP edge
  off62->63 LAST pair) + R7 offs 0,63,126/127,193,254/
  255 (2-mid shape: mid1 off63 125120 + mid2 off193
  125250; tail off255 inside edge2 pair = TIER-LAST
  edge, first-hand); 9184->9215); 31x2=62 rows, range
  124965..125312 exact. PINS-new-N == for-added 31/31,
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60-r62); band
  diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit419.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 141 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-1SIG-88/QUAD88-4R-STEP/RING-SWAPPED; no F/
  F0/F1, no QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42); C==py 12/12. S0 168ch sig
  ebfda700 NEW (33/84 vs P310S0 @ 2,4,5,21-23,30-43,
  48,56-59,76-83 EXACT) / S1 176ch sig 01000000 sig-eq-
  P310PB1 (80/88 vs P310S1 @ 4-55,60-87 EXACT, NOT
  byte-equal). S1-vs-own-C10 staged per-cell (each cell
  own lencode) [70]x10 TRUE-UNIFORM count+position
  (cell0 70 @ b4,6-12,14-55,68-87 EXACT; positions
  identical all 10 staged). AM 16x20ch distinct; AC 76,
  b0-3 14000000 (b0 const 14), no b4/b5, PBA sig
  14000000 x16 PLAIN (NEW sig 14; M10 b8,13-17,80-83).
  CM 10x10ch 10/10 diverge; CC 81, b0-3 01000000
  SAME-as-PB1-sig, no b4/b5 (b5 const d0 via lencode,
  NO step; M5 b8,84-87). M 16x12ch distinct (QM6
  b20,21,80-83, shared NO frags). QR 4x6ch 4-distinct
  UNPAIRED micro-quad (r0 f81296 / r1 1d1396 / r2
  421396 / r3 550297 EXACT; smallest R-tab this lane:
  3B, b87 const 5c excluded); tails+const b84-87
  f812965c/1d13965c/4213965c/5502975c 4/4 distinct;
  full 3/2/1 programmatic ladder byte-exact (r1r2 TRUE
  3B 13965c, differ b84 1d/42; r0 2B 965c vs r1/r2;
  r3-vs-all lcsuf 1 = b87 const only -- first of its
  kind, memo-agreed). QC 77, b0-3 15000000, b87 const
  5c quad-wide, no b4/b5 (QUAD single-sig x64). RM
  16x14ch distinct; RQ 16x12ch distinct; RM-vs-RQ
  UNPAIRED (sets disjoint); RC 73, b0-3 58010000,
  b84-87 1d/6a/0d/86 ring-wide. RQ==M FULL6: M 6B vs
  RQ 6B agree (0,0),(1,1),(2,2),(3,3),(4,4),(5,5)
  16/16 each; tabs byte-identical; agree pure diagonal
  (ALL off-diagonal 0/16); maxagree 16 all 6,
  distinct 16,2,16,12,16,16 -- NEW odd degree (first
  full-identity instance among ODD bands; same byte
  positions b20,21,80-83 both tabs; see prose note on
  the unscoped "first"); 27th odd-band RQ==M instance
  (viewer chain b413-24th/b415-25th/b417-26th/b419-27th
  sequential; evens take no ordinal). Tails SWAPPED
  (RM b76-79 by COL c=off&15, RQ b80-83 by ROW
  r=off>>4 -- subscripts verified py+C; 16/16
  distinct each, 0 overlap). Sorted-unique + _N decls
  76/81/77/73 match actual. Missing-sets EXACT: AC
  [4,5,8,13-17,80-83]; CC [4,5,8,84-87]; QC [4,5,20,
  21,80-86] (11, b87 const); RC [4,5,20,21,28-30,
  76-83] (15). VPOS 11/6/11/15 == A-802 EXACT (quad
  {4,5,20,21,80-86}, b87 correctly excluded).
  Coverage unions exact every block (const U tab U
  {b4,b5} == 88 x4, 0 overlap). Q legs M[m] + QR[q]
  both sides, NO F-legs either side. R legs RM[c] +
  RQ[r] both sides, NO F-legs. P310 refs re-read: S0
  ebfd8700 / S1 01000000 / PBA 15000000 / C10 01000000
  / QUAD 0a000000 x64. Next-P311 preds (A-798 re-read:
  PB0 ebfda700 NEW / PB1 01000000 80/88 / PBA88
  14000000 x16 / C10-region 01000000 pay88 x10) x4
  corroborated (banked-from-r62 CONSUMED). PBA NEW vs
  P310 (14000000 != 15000000); QUAD single-sig 15 vs
  P310 0a. AM/CM/M/QR/RM/RQ 0-overlap vs P310 (widths
  P311 AM20/CM10/M12/QR6/RM14/RQ12 vs P310 AM16/CM8/
  M18/QR24/RM16/RQ18 chars, base widths re-read
  first-hand). M-tails 16/16 ALL NEW vs P310 RQ row-
  led tails + RM-tails NEW vs P310 RM col-led tails
  + RQ-tails NEW vs P310 RQ row-led tails + cross
  overlaps 0 (P310T widths RM 8B/RQ 9B re-read).
  Memo INCL PBA88 77 / C10 82 / quad88 77 / T88 73
  (A-802 re-read): impl 76/81/77/73 = memo-1 on PBA/
  C10 (b5-const excluded), identical quad (b5 step)/
  T88 (counter) -- standing +1 rule coherent,
  +1/+1/+0/+0. Base temp maxes _t6408/_b3883/_i3884
  (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 124965 / S1 124966 / A 124967-982 / C 124983-992 /
  Q 124993-125056 / R 125057-312): bounds + paylens
  (1x84 + 347x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (QUAD-STEP LAST-pair o62->o63 emerges from
  raw lencode) + R counter b4=(0x03+2off)&FF b5=0xd1+
  (off>=127)+(off>=255) (py hex 0x03/0xD1/127/255; C
  staged decimal 3/209, re-derived: 3==0x03, 209==0xd1)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 10B b8,13-17,80-83;
  C 5B b8,84-87; Q QM6 b20,21,80-83 + R3 b84-86, NO
  frags; R TM7 b28-30,76-79 by COL + TR6 b20,21,80-83
  by ROW, SWAPPED tails-last) + C guards `if ((n) ==
  (124965))` / `(124966)` + 4 range guards exact + C
  byte-index lists match py per block (A 10B, C 5B, Q
  6B/3B union 9+b4/b5, R 7B/6B union 13+b4/b5). T-
  mirrors T83757/83762/83767/83783/83798/83818 each
  re-read: hits the exact py guard line. Temps
  _t6409-6424 continuous-16 (base max _t6408) +
  _b3885/3887/3889/3890/3892/3893 (base max _b3883) +
  _i3886/3888/3891/3894 (base max _i3884): added-only,
  no reuse. Insert exact both sides: P310R block
  precedes (py 83737, C 223256; P3110 at py 83757, C
  223305), at dispatch tail (N-out-of-scope follows;
  2 scope hits py + 2 scope hits C). Matches A-802
  geometry (values re-checked in audit above; NO D
  dips: ownloop tags exactly the 6 P311 blocks).
- Edges own-loop ownloop419.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (303 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P311R N=125312
  off=255. edges419.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 4b/d0, 4d/d0
  == raw lencode) + aform 16/16 (A head 4f/d0 tail
  6d/d0 b5set {d0} NO step, 0 ff) + cform 10/10 (C
  head 6f/d0 tail 81/d0 b5set {d0} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head 83/d0, edge
  off62->63 125055->125056 ff/d0->01/d1 LAST pair,
  tail 01/d1, b5set {d0,d1}, exactly 1 ff in 64 at
  o62; quad b4 base 0x83 step2 == raw-lencode 64/64);
  ring counter 256/256 + ringraw 256/256 (head 03/d1;
  mid1 off63 81/d1 at 125120; 125183 off126 ff/d1 ->
  125184 off127 01/d2; mid2 off193 85/d2 at 125250;
  125311 off254 ff/d2 -> 125312 off255 01/d3 TIER-
  LAST; tail off255 01/d3; exactly 2 ff in 256 at
  o126/o254); ff total x3 (Q-step o62 + 2 ring).
  odd-lencode 92+256=348/348. Ring edges + tail
  125312 in for-list + 2 PASS lines each py+C. Tail
  125312: oracle sha f160772a7901f11a... matches
  PINS (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P311R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf419.py (cache path) + secf419b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (124965 +
  124617 + 124966 + 124618); S0: oracle124965-vs-124617
  33/84, codeS0-vs-P310S0 33/84, positions identical;
  DIRECT tool 33/84 with identical agree-pos 51
  positions. S1: oracle124966-vs-124618 80/88,
  codeS1-vs-P310S1 80/88, positions identical; DIRECT
  80/88 identical agree-pos 8 positions (0-3,56-59).
  0 miss (ownloop pre-warmed). Triple-derived both
  pairs (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf419c.py (oracle C10
  cells n124983-992): 70/88 TRUE-UNIFORM all 10 ([0]
  n124983 70/88 @ b4,6-12,14-55,68-87 == GATE EXACT;
  counts [70]x10 AND positions identical all 10 --
  verified beyond GATE's cell0, staged+oracle agree;
  sig 01000000 both, NOT byte-equal). P311 is the 8th
  TRUE-uniform case on record (7th excluding
  unverified P299) -- see prose note on the GATE's
  "4th" ordinal. Byte-diff discipline observed
  throughout, nothing to refute.
- C diff pure-add: numstat 608/0 (rgramc.c) + 233/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 603 content + 5 bare-blank / 0 del (see prose
  note: GATE writes "608 content"); raw py 233 content
  / 0 del. Full-digit norm ([0-9]+ -> N): C del-uniq 0
  add-uniq 150 missing 0 under the recipe AS STATED
  (diff-sign strip + trailing-';' strip, NO whitespace
  handling stated); GATE's 146 reproduces iff leading-
  whitespace-stripped AND empty-excluded (strip+
  dropempty 146, strip-only 147, dropempty-only 149 --
  recipe variant gap, same class as b405/b407/b409/b411/
  b413/b415/b417; see prose note); py del-uniq 0
  add-uniq 177 missing 0 == GATE EXACT (variant-
  insensitive: 177 all four variants). del-subset-add 0
  missing holds every variant (integrity intact).
  C-tempnorm 401 / py-tempnorm 192 recorded (no GATE
  claim).
- Wall on band diff added lines (scope 85fc4505..
  adf40836, 904 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 608/0,
  rgram.py 233/0 purely additive, test_rgram.sh 1/1,
  PINS +62/+0.
- Tiers: merge-msg +6/+62 (91e2afc7), code 6 blocks,
  tier-comments `# T10P` 1754->1760 +6 == GATE stated-
  method EXACT, singletons `if n == ` 654->656 +2 ==
  GATE EXACT, range-guards `<= n <=` 696->700 +4 ==
  GATE EXACT, CLOSED T10P prints 1754->1760 +6 py +
  1754->1760 +6 C == GATE EXACT, C singleton
  `if ((n) == (` 649->651 +2 == GATE EXACT (5-count
  C-vs-py offset pre-existing, unchanged: 654-649 =
  656-651 = 5), C ranges 696->700 +4 == GATE EXACT,
  seal 1848->1854 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1854-1760 = 94, stable b401-b419): all
  agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-802-q903-P311
  verdict CONFIRM, tallies 29/29 + 16/16 + 14/14 =
  59/59 arith-consistent as-filed + exact-value
  corroboration incl PB0 NEW + PB1 sig-eq-P310PB1
  80/88 NOT-byte-equal SAME-as-own-C10 70/88,
  PBA88-PLAIN sig-14 M10, C10-1SIG-88 b5-const NO-step
  M5, QUAD88-4R-STEP + R3 micro-quad + 3/2/1 ladder +
  b87-const-5c + QM6 + NO frags + b5-step LAST-pair +
  M-tails NEW, T88-RING-SWAPPED + TM7/TR6 16/16
  UNPAIRED + SWAPPED tails + b84-87 1d6a0d86 + edges
  + consts 03/d1/127/255 + lencode 348/348 + VPOS
  11/6/11/15 (all re-checked above). Sheet-vs-
  tables const-count note: Q-903 sheet rule 77/82/
  77/73 memo-exact (8th straight fully clean w2b
  sheet per memo; w2b-r26 [4/8]), committed tables
  76/81/77/73 still deduct const-b5 in PBA/C10 --
  14th consecutive tables-lag band (geometry exact,
  PORT verdict stands). No viewer P311 geometry
  answer on file at gate time (memo-only recon; this
  VERIFY is the viewer record). No CONFIRM-P311.md
  file (absence verified); A-802 suffices per rule.
  Agrees with cport commit msg (PYID 9215, RGRAM
  18430).
- Quiz: no conflicting CLAIM/GATE/FLAG on b419 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites
  QNUM-22 newest -- TRUE at filing time (GATE 14:26,
  QNUM-23/24 postdate it): NO staleness. PROSE-01:
  all hex/counts above copied from own run output;
  GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 4 prose-level notes ("raw C 608 content + 5
blank-only" reads 608+5=613 vs numstat 608 -- first-hand
is 603 content + 5 bare-blank = 608 (4th instance after
b413/b415/b417, same sweep-r66 token); norm-146 recipe
variant gap: stated recipe yields 150, strip+dropempty
yields the claimed 146 -- integrity holds every variant,
same class as b405/b407/b409/b411/b413/b415/b417 (8th
instance); "4th TRUE-uniform case after P299 + P303 +
P307": P300 56/84 (r60 filed record) + P306 28/84 (r61
count+position uniform) + P308 59/88 (r62 count+position
uniform) + P310 49/88 (r62 count+position uniform) are
all on record, making P311 EIGHTH on record (7th
excluding unverified P299) -- the ordinal holds only
under a narrower scope the GATE doesn't state, same
class as b415's flagged ordinal; "first full-identity
instance": b414 (even full-eq per r61 record) + b418
(even M==RQ lists-identical, verified this round)
precede -- holds only under odd-band scope, unstated;
code GREEN since gated artifact == verified artifact).
27th odd-band RQ==M instance corroborated as FULL6
(pure-diagonal agree + RQ distinctness 16/2/16/12/16/16;
NEW odd degree joining neither prior group; memo-silent
on the relation; even/odd convention holds: b418 even
takes no ordinal). Next-P312 SHAPE banked (A-802
re-read: PB0 d7fb4f01 NEW pay84 @125313 / PB1 02000000
pay88 @125314 NEW-sig 83/88 / PBA88 39000000 x16
@125315-30 / C10-region 02000000 pay88 x10 @125331-40
-- PB1/C10 sig rotation 01->02).
