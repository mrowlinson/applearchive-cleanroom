# VERIFY-307c9f53 b420 T10P312 pins 125313..125660 (1860 tiers) PASS

Seat viewer-r63, first-hand, tree420 @307c9f53,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r63.
Base adf40836 (b419, 1854 tiers). Band = 81601e3c (py merge
w2b@e67649f1 partial, +6 tiers, +62 pins) + 307c9f53 (C port,
1860 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117/117).

- Build: make -C src/c BUILDDIR=build420 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc 8a6fd088e3791836 / aae
  d6e27c97ced21673 + sha1 rgramc 29704b9c26b12443 / aae
  7d8dd3a2d118e0db (== GATE prefixes all four; aae pinned,
  band touches no aae sources per numstat).
- RGRAMC-PYID 9246/9246 covered=9246/9246 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18492/18492 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18492/18492 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18492/18492;
  GATE claims both, both corroborated).
- PINS 18494 rows (2 hdr + 18492, +62 vs base 18432);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq). For-list delta vs base
  +31/-0 (9215->9246):
  125313 125314 125315 125316 125322 125323 125329 125330
  125331 125332 125335 125336 125339 125340 125341 125348
  125357 125364 125373 125380 125389 125396 125403 125404
  125405 125439 125440 125500 125567 125568 125660
  (== GATE list EXACT; decomposition first-hand: 2 sing +
  A6 offs 0,1,7,8,14,15 + C6 offs 0,1,4,5,8,9 + Q10 offs
  0,7,16,23,32,39,48,55,62,63 (head + 8 mids + tail, NO
  step, quad b5 const) + R7 offs 0,34,35,95,162,163,255
  (head/edge-pair/mid/edge-pair/tail)); 31x2=62 rows,
  range 125313..125660 exact. PINS-new-N == for-added
  31/31, PINS removed 0. (Near-miss: first extraction
  dropped the `NNNN;` tail token -> 9245/9214 + shifted
  added-set; re-extracted stripping `;`, verbatim match.)
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60-r63); band
  diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit420.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 137 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-1SIG-88-TAILTAB/QUAD88-4R/RING-STANDARD; no F/
  F0/F1, no QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42); C==py 12/12. S0 168ch sig
  d7fb4f01 NEW / S1 176ch sig 02000000 NEW-sig (83/88 vs
  P311S1, agree-pos 1,2,3,13,33 EXACT, NOT byte-equal).
  S1-vs-own-C10 staged per-cell (each cell own lencode)
  [45]x10 TRUE-UNIFORM count+position (cell0 45 @
  4,19,25-43,56-75,84-87 EXACT; positions identical all
  10 staged; sig 02000000 both, NOT byte-equal -- 9th
  TRUE-uniform case on record, 8th excluding unverified
  P299; beyond GATE's cell0-only claim, oracle leg
  below agrees). AM 16x14ch distinct; AC 79, b0-3
  39000000 (b0 const 39), no b4/b5, PBA sig 39000000
  x16 PLAIN (NEW sig 39; M7 b29,34,35,80-83). CM 10x8ch
  10/10 diverge (108e1c28/308e1c28/508e1c28/708e1c28/
  908e1c28/b08e1c28/d08e1c28/f08e1c28/3c8f1c28/e7ca4681
  EXACT); CC 82, b0-3 02000000 SAME-as-PB1-sig, b80-83
  0a76879d, no b4/b5 (b5 const d3 via lencode; M4
  b84-87). M 16x12ch distinct (QM6 b40,41,80-83, shared
  NO frags). QR 4x22ch 4-distinct UNPAIRED (r0
  648f9d20fded89038a8269 fully distinct; r123 share 14ch
  e41f4b3cf3c455 + tails ac55f32f/d155f32f/f655f32f
  EXACT; tails 038a8269/ac55f32f/d155f32f/f655f32f 4/4
  distinct; r123 TRUE-3B 55f32f + pairwise-lcs3 +
  r0-vs-all lcs0 programmatic EXACT). QC 69, b0-3
  14000000, no b4/b5 (QUAD single-sig x64). RM 16x16ch
  distinct; RQ 16x12ch distinct; RM-vs-RQ UNPAIRED
  (sets disjoint); RC 72, b0-3 46010000, b84-87
  968a8269 ring-wide NEW. M==RQ lists 16/16 string-
  identical, agree pure diagonal (ALL off-diagonal
  0/16), RQ distinctness 16/4/16/13/16/14 -- even-band
  string-identity BUT byte positions differ (QM6
  b40,41,80-83 vs TR6 b40,41,76-79, re-derived from
  dispatch code both sides; no ordinal per even/odd
  convention). Tails SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4 -- subscripts verified
  py+C; 16/16 distinct each, 0 overlap). Sorted-unique
  + _N decls 79/82/69/72 match actual. Missing-sets
  EXACT: AC [4,5,29,34,35,80-83]; CC [4,5,84-87]; QC
  [4,5,25-27,34,35,37,38,40,41,80-87] (19); RC
  [4,5,30,39,40,41,46,47,76-83] (16). VPOS 8/5/18/16 ==
  A-806 EXACT (PBA M7+b4 / C10 {4,84-87} / quad
  b4+QM6+R11 / T TM8+TR6+b4+b5, b5-const excluded
  except T). Coverage unions exact every block (const U
  tab U {b4,b5} == 88 x4, 0 overlap). Q legs M[m] +
  QR[q] both sides, NO F-legs either side. R legs RM[c]
  + RQ[r] both sides, NO F-legs. P311 refs re-read: S0
  ebfda700 / S1 01000000 / PBA 14000000 / C10 01000000
  / QUAD 15000000 / RC 58010000+1d6a0d86. Next-P312
  preds (banked-from-r62 CONSUMED): PB0 d7fb4f01 NEW /
  PB1 02000000 83/88 / PBA88 39000000 x16 / C10-region
  02000000 pay88 x10 -- x4 corroborated. PBA NEW vs
  P311 (39000000 != 14000000); QUAD single-sig 14 vs
  P311 15. AM/CM/M/QR/RM/RQ 0-overlap vs P311 (widths
  P312 AM14/CM8/M12/QR22/RM16/RQ12 vs P311 AM20/CM10/
  M12/QR6/RM14/RQ12 chars, base widths re-read
  first-hand). M-tails 16/16 ALL NEW vs P311M AND vs
  P311RM-tail8 AND vs P311RQ-tail8 (overlap 0 x3;
  P311 SWAPPED so RQ row-led tails = memo's comparison
  set). AC-QC both=68 sameval=25 (tables differ) ==
  GATE EXACT. Memo INCL PBA88 80 / C10 83 / quad88 70
  / T88 72 (A-806 re-read): impl 79/82/69/72 = memo-1
  on PBA/C10/quad (b5-const excluded), identical T88
  (counter) -- standing +1 rule coherent, +1/+1/+1/+0.
  Base temp maxes _t6424/_b3893/_i3894 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 125313 / S1 125314 / A 125315-330 / C 125331-340 /
  Q 125341-404 / R 125405-660): bounds + paylens
  (1x84 + 347x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides + R counter b4=(0xbb+2off)&FF b5=0xd3+
  (off>=35)+(off>=163) (py hex 0xbb/0xd3/35/163; C
  staged decimal 187/211, re-derived: 187==0xbb,
  211==0xd3) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A 7B
  b29,34,35,80-83; C 4B b84-87; Q QM6 b40,41,80-83 +
  R11 b25-27,34,35,37,38,84-87, NO frags; R TM8
  b30,39,46,47,80-83 by COL + TR6 b40,41,76-79 by ROW,
  SPLIT tails) + C guards `if ((n) == (125313))` /
  `(125314)` + 4 range guards exact + C byte-index
  lists match py per block (A 7B, C 4B, Q 6B/11B union
  17+b4/b5, R 8B/6B union 14+b4/b5). T-mirrors
  T83989/83994/83999/84014/84029/84050 each re-read:
  hits the exact py guard line. Temps _t6425-6440
  continuous-16 (base max _t6424) + _b3895/3897/3899/
  3900/3902/3903 (base max _b3893) + _i3896/3898/3901/
  3904 (base max _i3894): added-only, no reuse. Insert
  exact both sides: P311R block precedes (py 83987, C
  223905-07; P3120 at py 83989, C 223908), at dispatch
  tail (N-out-of-scope follows; 84069 py + 224091 C).
  Matches A-806 geometry (values re-checked in audit
  above; NO D dips: ownloop tags exactly the 6 P312
  blocks).
- Edges own-loop ownloop420.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P312R N=125660
  off=255. edges420.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 03/d3, 05/d3
  == raw lencode) + aform 16/16 (A head 07/d3 tail
  25/d3 b5set {d3} NO step, 0 ff) + cform 10/10 (C
  head 27/d3 tail 39/d3 b5set {d3} NO step, 0 ff) +
  qform 64/64 + qb5const 64/64 (Q head 3b/d3 tail
  b9/d3 b5set {d3} NO step, 0 ff; quad b4 base 0x3b
  step2 == raw-lencode 64/64 range 3b..b9 NO edge);
  ring counter 256/256 + ringraw 256/256 (head bb/d3;
  125439 off34 ff/d3 -> 125440 off35 01/d4; mid off95
  79/d4 at 125500; 125567 off162 ff/d4 -> 125568
  off163 01/d5; tail 125660 off255 b9/d5; exactly 2
  ff in 256 at o34/o162); ff total x2 (ring only).
  odd-lencode 92+256=348/348. Ring edges + tail
  125660 in for-list + 2 PASS lines each py+C. Tail
  125660: oracle sha 1021b2831c2237ca... matches PINS
  (GATE states no tail sha; recorded first-hand).
  py+C CLOSED T10P312R off=255 agree. No DISSENT: cut
  bytes verify.
- PB-diff secf420.py (cache path) + secf420b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (125313 +
  124965 + 125314 + 124966); S0: oracle125313-vs-124965
  47/84, codeS0-vs-P311S0 47/84, positions identical;
  DIRECT tool 47/84 with identical agree-pos 37
  positions. S1: oracle125314-vs-124966 83/88,
  codeS1-vs-P311S1 83/88, positions identical; DIRECT
  83/88 identical agree-pos 5 positions (1,2,3,13,33).
  0 miss (ownloop pre-warmed). Triple-derived both
  pairs (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf420c.py (oracle C10
  cells n125331-340): 45/88 TRUE-UNIFORM all 10 ([0]
  n125331 45/88 @ 4,19,25-43,56-75,84-87 == staged
  EXACT; counts [45]x10 AND positions identical all
  10 -- verified beyond GATE's cell0, staged+oracle
  agree; sig 02000000 both, NOT byte-equal). P312 is
  the 9th TRUE-uniform case on record (8th excluding
  unverified P299). Byte-diff discipline observed
  throughout, nothing to refute.
- C diff pure-add: numstat 608/0 (rgramc.c) + 232/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 603 content + 5 bare-blank / 0 del == GATE
  EXACT (no whitespace-suspect lines); raw py 232
  content / 0 del. Full-digit norm: C 150/147/149/146
  across the 4 strip/dropempty variants (recorded, no
  GATE claim); py 173 all four variants. C-tempnorm
  del-uniq 0 add-uniq 389 missing 0 == GATE EXACT
  (recipe as stated: temp-norm, empty-excluding);
  py-tempnorm 190. del-subset-add 0 missing holds
  every variant (integrity intact).
- Wall on band diff added lines (scope adf40836..
  307c9f53, 903 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 608/0,
  rgram.py 232/0 purely additive, test_rgram.sh 1/1,
  PINS +62/+0.
- Tiers: merge-msg +6/+62 (81601e3c), code 6 blocks,
  dispatch-guards (4-space dispatch-exact) singletons
  646->648 +2 == GATE EXACT / ranges 678->682 +4 ==
  GATE EXACT, C identical deltas 646->648 +2 /
  678->682 +4 == GATE EXACT (py=C dispatch-exact; no
  else-if either side, deltas agree every side),
  CLOSED T10P prints 1760->1766 +6 both sides,
  seal 1854->1860 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1860-1766 = 94, stable b401-b420): all
  agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-806-q904-P312
  verdict CONFIRM, tallies 27/27 + 15/15 + 14/14 =
  56/56 arith-consistent as-filed + exact-value
  corroboration incl PB0 NEW + PB1 NEW-sig 83/88
  NOT-byte-equal SAME-as-own-C10 45/88, PBA88-PLAIN
  sig-39 M7, C10-1SIG-88-TAILTAB SAME-as-PB1-sig M4,
  QUAD88-4R + R11 rows + share-14ch + r123-TRUE-3B +
  r0-lcs0 + r123-lcs3 + QM6 + NO frags + b5-const +
  M-tails NEW, T88-RING-STANDARD + TM8/TR6 16/16
  UNPAIRED + SPLIT tails + b84-87 968a8269 + edges +
  consts bb/d3/35/163 + lencode 348/348 + VPOS
  8/5/18/16 (all re-checked above). Sheet-vs-
  tables const-count note: Q-904 sheet rule 80/83/
  70/72 memo-exact (9th straight fully clean w2b
  sheet per memo; w2b-r26 [5/8]), committed tables
  79/82/69/72 still deduct const-b5 in PBA/C10/quad
  -- 15th consecutive tables-lag band (geometry exact,
  PORT verdict stands; even sub-sequence b412/b414/
  b416/b418/b420 membership re-verified from records:
  all tables-lag, quad signature alternates with quad
  b5 const-vs-step). No viewer P312 geometry answer
  on file at gate time (memo-only recon; this VERIFY
  is the viewer record). No CONFIRM-P312.md file
  (absence verified); A-806 suffices per rule.
  Agrees with cport commit msg (PYID 9246, RGRAM
  18492).
- Quiz: no conflicting CLAIM/GATE/FLAG on b420 (own seat
  CLAIM only; exactly 1 GATE-307c9f53; NO-FLAG greps
  first-hand). PROSE-01: all hex/counts above copied
  from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 0 prose notes (sweep2-r68 fully clean: raw-C
603+5 bare-blank EXACT, tempnorm-389 recipe reproduces
EXACT, P311-contrast 58010000/1d6a0d86 re-read EXACT,
AC-QC both=68 sameval=25 EXACT, even-pattern grouping
coherent). Even-band RQ==M string-identity corroborated
(lists-identical pure-diagonal + RQ distinctness
16/4/16/13/16/14 + byte-positions-differ QM6-80-83 vs
TR6-76-79; no ordinal; memo-silent on the relation;
even/odd convention holds). Next-P313 SHAPE banked
(A-806 re-read: PB0 97016d01 NEW pay84 @125661 / PB1
02000000 sig-eq-P312PB1 47/88 @125662 / PBA88 26000000
x16 @125663-78 / C10-region 02000000 pay88 x10
@125679-88 -- 02-sig era continues).
