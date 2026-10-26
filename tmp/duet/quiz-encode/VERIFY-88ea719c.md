# VERIFY-88ea719c b417 T10P309 pins 124269..124616 (1842 tiers) PASS

Seat viewer-r62, first-hand, tree417 @88ea719c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r62.
Base 19dbc5e1 (b416, 1836 tiers). Band = 4ed86711 (py merge
w2b@925a104b partial, +6 tiers, +62 pins) + 88ea719c (C port,
1842 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117/117).

- Build: make -C src/c BUILDDIR=build417 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc e5b0cc2fd084aa14 / aae
  d6e27c97ced21673 + sha1 rgramc 56ad0c5e885e8f7f / aae
  7d8dd3a2d118e0db (== GATE all four; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 9153/9153 covered=9153/9153 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18306/18306 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18306/18306 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18306/18306;
  GATE claims sorted only, raw corroborated too).
- PINS 18308 rows (2 hdr + 18306, +62 vs base 18246);
  PASS-names vs PINS-names xor 0 py+C; py-vs-C xor 0;
  base-N vs for-list xor 0 (4-way set-eq). For-list
  delta vs base +31/-0:
  124269 124270 124271 124272 124278 124279 124285 124286
  124287 124288 124291 124292 124295 124296 124297 124304
  124313 124320 124329 124336 124345 124352 124359 124360
  124361 124415 124416 124500 124543 124544 124616
  (== GATE decomposition: 2 sing + A6 offs 0,1,7,8,14,15
  + C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 124289/124290/
  124293/124294 unsampled, absence verified) + Q10 offs
  0,7,16,23,32,39,48,55,62,63 (per-row m0/m7 + tail pair
  -- first-hand from for-list; "NEW vs P305 m0/m8"
  beyond window, not disputed) + R7 offs 0,54/55,139,
  182/183,255 (mid off139 = 124500 first-hand; novel vs
  b415 off128 mid per VERIFY-c9b64be1 record);
  9122->9153); 31x2=62 rows, range 124269..124616 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60-r62); band
  diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit417.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 143 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-1SIG-88-STEP/QUAD88-4R/RING-SWAPPED; no F/
  F0/F1, no QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42); C==py 12/12. S0 168ch sig
  ab689400 NEW (33/84 vs P308S0 @ 2,4-11,34,35,41-51,
  56-60,62-67 EXACT) / S1 176ch sig 01000000 sig-eq-
  P308PB1 (53/88 vs P308S1 @ 4-7,9-14,16-27,36-38,
  40-43,48-55,64-75,84-87 EXACT, NOT byte-equal).
  S1-vs-own-C10 staged per-cell (each cell own lencode)
  [41,42,42,42,42,42,42,42,42,41] NON-uniform (cell0
  41 @ b4,16-18,22-26,28-35,56-75,84-87 EXACT).
  AM 16x12ch distinct; AC 80, b0-3 12000000 (b0 const
  12), no b4/b5, PBA sig 12000000 x16 PLAIN (NEW sig
  12; M6 b28,29,80-83). CM 10x20ch 10/10 diverge; CC
  76, b0-3 01000000 SAME-as-PB1-sig, b32 const gap
  0x56 (first C10 gap), no b4/b5 in CC (b5 step via
  lencode; M10 b28-31,33,34,84-87). M 16x20ch
  distinct (QM10 b18,19,25-27,35,80-83, shared NO
  frags). QR 4x22ch 4-distinct UNPAIRED; r0
  7dbc559c75fc127642375e distinct; r123 share 14ch
  823c06ca15ee43; tails b84-87 7642375e/c90c66f8/
  ee0c66f8/7825d7fd 4/4 distinct; r1r2 pair-only 3B
  0c66f8 (differ b84 c9/ee); full-row lcsuf r1r2=3
  else 0 (r0 lcs0 AND r3 lcs0, suffix sense) +
  lcpre r123 7, r0-vs-rest 0. QC 65, b0-3 08000000,
  no b4/b5 (QUAD single-sig x64). RM 16x14ch
  distinct; RQ 16x18ch distinct; RM-vs-RQ UNPAIRED
  (sets disjoint); RC 70, b0-3 8b000000, b84-87
  3d/cf/97/f7 ring-wide. RQ==M TAILS4-ONLY: M 10B vs
  RQ 9B agree (6,5),(7,6),(8,7),(9,8) 16/16 each
  (b80-83 tails position-exact); zero off-pattern
  FULL agrees (incidentals M0-RQ8 1, M1-RQ2 5,
  M5-RQ3 1, M9-RQ1 1); RQ[0..4] maxagree 0,1,5,1,0
  distinct 4,2,2,8,12; RQ[5..8] maxagree 16 distinct
  16,15,15,15 -- NEW degree (tails-only, heads
  differ; joins neither DIAG6/HEAD2+TAILS nor SHIFT
  group); 26th odd-band RQ==M instance (viewer chain
  b413-24th/b415-25th/b417-26th sequential; evens
  take no ordinal). Tails SWAPPED (RM b76-79 by COL
  c=off&15, RQ b80-83 by ROW r=off>>4 -- subscripts
  verified py+C; 16/16 distinct each, 0 overlap).
  Sorted-unique + _N decls 80/76/65/70 match actual.
  Missing-sets EXACT: AC [4,5,28,29,80-83]; CC [4,5,
  28-31,33,34,84-87]; QC [4,5,18,19,25-35,80-87]
  (23); RC [4,5,29-31,34,35,40-42,76-83] (18).
  VPOS 7/12/22/18 == A-796 EXACT (C10 b5 varies in
  tab; quad b5 correctly excluded). Coverage unions
  exact every block (const U tab U {b4,b5} == 88 x4,
  0 overlap). Q legs M[m] + QR[q] both sides, NO
  F-legs either side. R legs RM[c] + RQ[r] both
  sides, NO F-legs. P308 refs re-read: S0 ab685400 /
  S1 01000000 / PBA 10000000 / C10-1SIG 01000000.
  Next-P309 preds (A-793 re-read: PB0 ab689400 NEW /
  PB1 01000000 / PBA88 12000000 x16) x3 + C10
  SAME-as-PB1-sig corroborated (banked-from-r62
  CONSUMED). PBA NEW vs P308 (12000000 != 10000000).
  AM/CM/M/QR/RM/RQ 0-overlap vs P308 (widths P309
  AM12/CM20/M20/QR22/RM14/RQ18 vs P308 AM14/CM20/M8/
  QR32/RM18/RQ14 chars, base widths re-read
  first-hand). M-tails 16/16 ALL NEW vs P308 RM col-
  led tails + RM-tails NEW vs P308 RQ row-led tails
  + RQ-tails NEW vs P308 RM col-led tails + cross
  overlaps 0 (P308T widths RM 9B/RQ 7B re-read).
  Memo INCL PBA88 81 / C10 76 / quad88 66 / T88 70
  (A-796 re-read): impl 80/76/65/70 = memo-1 on PBA/
  quad (b5-const excluded), identical C10 (b5 step)/
  T88 (counter) -- standing +1 rule coherent,
  +1/+0/+1/+0. Base temp maxes _t6376/_b3863/_i3864
  (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 124269 / S1 124270 / A 124271-286 / C 124287-296 /
  Q 124297-360 / R 124361-616): bounds + paylens
  (1x84 + 347x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (C10-STEP o0->o1 emerges from raw lencode)
  + R counter b4=(0x93+2off)&FF b5=0xcb+(off>=55)+
  (off>=183) (py hex 0x93/0xCB/55/183; C staged
  decimal 147/203, re-derived: 147==0x93, 203==0xcb)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 6B b28,29,80-83;
  C 10B b28-31,33,34,84-87; Q QM10 b18,19,25-27,35,
  80-83 + R11 b28-34,84-87, NO frags; R TM7 b40-42,
  76-79 by COL + TR9 b29-31,34,35,80-83 by ROW,
  SWAPPED tails-last) + C guards `if ((n) ==
  (124269))` / `(124270)` + 4 range guards exact + C
  byte-index lists match py per block (A 6B, C 10B,
  Q 10B/11B union 21 disjoint+b4/b5, R 7B/9B union
  16+b4/b5). T-mirrors T83289/83294/83299/83314/83330/
  83352 each re-read: hits the exact py guard line.
  Temps _t6377-6392 continuous-16 (base max _t6376) +
  _b3865/3867/3869/3870/3872/3873 (base max _b3863)
  + _i3866/3868/3871/3874 (base max _i3864):
  added-only, no reuse. Insert exact both sides:
  P308R block precedes (py 83269, C 222025; P3090 at
  py 83289, C 222073), at dispatch tail (N-out-of-
  scope follows; 2 scope hits py + 2 scope hits C).
  Matches A-796 geometry (values re-checked in audit
  above; NO D dips: ownloop tags exactly the 6 P309
  blocks).
- Edges own-loop ownloop417.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P309R N=124616
  off=255. edges417.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 db/ca, dd/ca
  == raw lencode) + aform 16/16 (A head df/ca tail
  fd/ca b5set {ca} NO step, 0 ff) + cform 10/10 +
  cstep 10/10 (C head ff/ca, edge o0->o1 124287->
  124288 ff/ca->01/cb, tail 11/cb, b5set {ca,cb}) +
  qform 64/64 + qb5flat 64/64 (Q head 13/cb tail
  91/cb b5set {cb} NO step, 0 ff in 64; quad b4 base
  0x13 step2 13..91 == raw-lencode 64/64, NO edge);
  ring counter 256/256 + ringraw 256/256 (head 93/cb;
  124415 off54 ff/cb -> 124416 off55 01/cc; mid
  off139 a9/cc at 124500; 124543 off182 ff/cc ->
  124544 off183 01/cd; tail off255 91/cd; exactly 2
  ff in 256 at o54/o182); ff total x3 (C-step o0 +
  2 ring). odd-lencode 92+256=348/348. Ring edges +
  tail 124616 in for-list + 2 PASS lines each py+C.
  Tail 124616: oracle sha af5e052c18a2e8e7... matches
  PINS (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P309R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf417.py (cache path) + secf417b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (124269 +
  123921 + 124270 + 123922); S0: oracle124269-vs-123921
  33/84, codeS0-vs-P308S0 33/84, positions identical;
  DIRECT tool 33/84 with identical agree-pos 51
  positions. S1: oracle124270-vs-123922 53/88,
  codeS1-vs-P308S1 53/88, positions identical; DIRECT
  53/88 identical agree-pos 35 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf417c.py (oracle C10
  cells n124287-296): [41,42,42,42,42,42,42,42,42,41]
  NON-uniform ([0] n124287 41/88 @ b4,16-18,22-26,
  28-35,56-75,84-87 == GATE EXACT; counts == staged
  per-cell assembly EXACT; positions differ across
  cells -- verified beyond GATE's cell0; sig
  01000000 both, NOT byte-equal). No TRUE-uniform
  ordinal impact (P309 NON-uniform). Byte-diff
  discipline observed throughout, nothing to refute.
- C diff pure-add: numstat 608/0 (rgramc.c) + 233/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 603 content + 5 bare-blank / 0 del (see prose
  note: GATE writes "608 content"); raw py 233 content
  / 0 del. Full-digit norm ([0-9]+ -> N): C del-uniq 0
  add-uniq 167 missing 0 under the recipe AS STATED
  (diff-sign strip + trailing-';' strip, NO whitespace
  handling stated); GATE's 163 reproduces iff leading-
  whitespace-stripped AND empty-excluded (strip+
  dropempty 163, strip-only 164, dropempty-only 166 --
  recipe variant gap, same class as b405/b407/b409/b411/
  b413/b415; see prose note); py del-uniq 0 add-uniq
  189 missing 0 == GATE EXACT (variant-insensitive:
  189 all four variants). del-subset-add 0 missing
  holds every variant (integrity intact). C-tempnorm
  378 / py-tempnorm 205 recorded (no GATE claim).
- Wall on band diff added lines (scope 19dbc5e1..
  88ea719c, 904 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 608/0,
  rgram.py 233/0 purely additive, test_rgram.sh 1/1,
  PINS +62/+0.
- Tiers: merge-msg +6/+62 (4ed86711), code 6 blocks,
  tier-comments `# T10P` 1742->1748 +6 == GATE stated-
  method EXACT, singletons `if n == ` 650->652 +2 ==
  GATE EXACT, range-guards `<= n <=` 688->692 +4 ==
  GATE EXACT, CLOSED T10P prints 1742->1748 +6 py +
  1742->1748 +6 C == GATE EXACT, C singleton
  `if ((n) == (` 645->647 +2 == GATE EXACT (5-count
  C-vs-py offset pre-existing, unchanged: 650-645 =
  652-647 = 5), C ranges 688->692 +4 == GATE EXACT,
  seal 1836->1842 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1842-1748 = 94, stable b401-b417): all
  agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-796-q901-P309
  verdict CONFIRM, tallies 29/29 + 19/19 + 15/15 =
  63/63 arith-consistent as-filed + exact-value
  corroboration incl PB0 NEW + PB1 sig-eq-P308PB1
  53/88 NOT-byte-equal SAME-as-own-C10 41/88,
  PBA88-PLAIN sig-12 M6, C10-1SIG-88-STEP b5-step
  o0->o1 b32-gap M10, QUAD88-4R + R11 rows + 7B-share
  + r1r2-pair-3B + r0+r3-lcs0 + QM10 + NO frags +
  M-tails NEW, T88-RING-SWAPPED + TM7/TR9 16/16
  UNPAIRED + SWAPPED tails + b84-87 3dcf97f7 + edges
  + consts 93/cb/55/183 + lencode 348/348 + VPOS
  7/12/22/18 (all re-checked above). Sheet-vs-
  tables const-count note: Q-901 sheet rule 81/76/
  66/70 memo-exact (6th straight fully clean w2b
  sheet per memo; w2b-r26 [2/8]), committed tables
  80/76/65/70 still deduct const-b5 in PBA/QUAD --
  12th consecutive tables-lag band (geometry exact,
  PORT verdict stands). No viewer P309 geometry
  answer on file at gate time (memo-only recon; this
  VERIFY is the viewer record). No CONFIRM-P309.md
  file (absence verified); A-796 suffices per rule.
  Agrees with cport commit msg (PYID 9153, RGRAM
  18306).
- Quiz: no conflicting CLAIM/GATE/FLAG on b417 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites
  QNUM-22 newest -- TRUE at filing time (GATE 14:20,
  QNUM-23/24 postdate it): NO staleness. PROSE-01:
  all hex/counts above copied from own run output;
  GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 prose-level notes ("raw C 608 content + 5
blank-only" reads 608+5=613 vs numstat 608 -- first-hand
is 603 content + 5 bare-blank = 608 (3rd instance after
b413/b415, same token now in sweep-r66); norm-163 recipe
variant gap: stated recipe yields 167, strip+dropempty
yields the claimed 163 -- integrity holds every variant,
same class as b405/b407/b409/b411/b413/b415 (7th
instance); code GREEN since gated artifact == verified
artifact). 26th odd-band RQ==M instance corroborated as
TAILS4-ONLY (tails position-exact + RQ-heads isolated
0/1/5/1/0 + distinctness 4/2/2/8/12 + tails 16/15/15/15;
NEW variant joining neither prior group; memo-silent on
the relation; even/odd convention holds: b416 even takes
no ordinal). Next-P310 SHAPE banked (A-796 re-read: PB0
ebfd8700 NEW pay84 @124617 / PB1 01000000 pay88 @124618
sig-repeat 48/88 / PBA88 15000000 x16 @124619-34 /
C10-region 01000000 pay88 x10 @124635-44 -- same novel
shape continues).
