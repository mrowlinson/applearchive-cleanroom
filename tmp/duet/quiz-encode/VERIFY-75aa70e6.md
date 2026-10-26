# VERIFY-75aa70e6 b421 T10P313 pins 125661..126008 (1866 tiers) PASS

Seat viewer-r63, first-hand, tree421 @75aa70e6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r63.
Base 307c9f53 (b420, 1860 tiers). Band = cc6d8b7a (py merge
w2b@6902f10c partial, +6 tiers, +62 pins) + 75aa70e6 (C port,
1866 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117/117).

- Build: make -C src/c BUILDDIR=build421 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc 80ca72fcae8a0e9d / aae
  d6e27c97ced21673 + sha1 rgramc f183794fe8be4879 / aae
  7d8dd3a2d118e0db (== GATE all four; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 9277/9277 covered=9277/9277 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18554/18554 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18554/18554 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18554/18554;
  GATE claims sorted only, raw corroborated too).
- PINS 18556 rows (2 hdr + 18554, +62 vs base 18494);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq). For-list delta vs base
  +31/-0 (9246->9277):
  125661 125662 125663 125664 125670 125671 125677 125678
  125679 125680 125683 125684 125687 125688 125689 125695
  125696 125705 125712 125721 125728 125737 125744 125752
  125753 125823 125824 125850 125951 125952 126008
  (== GATE list EXACT; decomposition first-hand: 2 sing +
  A6 offs 0,1,7,8,14,15 + C6 offs 0,1,4,5,8,9 (offs
  2,3,6,7 = 125681/125682/125685/125686 unsampled,
  absence verified) + Q10 offs 0,6,7,16,23,32,39,48,55,
  63 (EARLY step edge off6->7 pair-covered, tail single
  off63) + R7 offs 0,70/71,97,198/199,255 (1-mid shape:
  head/edge-pair/mid/edge-pair/tail, both counter edges
  pair-covered)); 31x2=62 rows, range 125661..126008
  exact. PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60-r63); band
  diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit421.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 142 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-1SIG-88/QUAD88-2SIG-STEP/RING-STANDARD; no F/
  F0/F1, no QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42); C==py 12/12. S0 168ch sig
  97016d01 NEW (33/84 vs P312S0 @ 0-2,4,5,11,19-31,36,
  37,52-55,68-75 EXACT) / S1 176ch sig 02000000 sig-eq-
  P312PB1 (47/88 vs P312S1 @ 4,5,19,26-35,37-44,46-59,
  72-79,84-87 EXACT, NOT byte-equal). S1-vs-own-C10
  staged per-cell (each cell own lencode) [20,21x9]
  NON-uniform (cell0 20 @ 4,38,39,46-55,60-63,84,85,86
  EXACT == GATE; counts AND positions differ across
  cells -- NO uniform entry, like P309). AM 16x14ch
  distinct; AC 79, b0-3 26000000 (b0 const 26), no
  b4/b5, PBA sig 26000000 x16 PLAIN (NEW sig 26; M7
  b52,53,54,80-83). CM 10x12ch 10/10 diverge; CC 80,
  b0-3 02000000 SAME-as-PB1-sig, no b4/b5 (b5 const d5
  via lencode, NO step; M6 b52,53,84-87). M 16x12ch
  distinct (QM6 b6,7,80-83, shared across sig boundary
  NO frags). QR 4x24ch 4-distinct UNPAIRED (r0
  242ba68df1e0ef616771577d fully distinct; r123 share
  16ch 20ad2a1e91b89fca + tails f46e6463/196f6463/
  3e6f6463 EXACT; b0 row-led split r0=24 r123=20;
  tails r0,r1,r2,r3 = 6771577d/f46e6463/196f6463/
  3e6f6463 4/4 distinct; r2r3 TRUE-3B 6f6463 differ
  b84 19/3e + r1-2B 6463 vs r2/r3 + r0-vs-all lcs0
  programmatic EXACT). QC 68, b1-3 const 00, b0 NOT
  const (in R12 tab), no b4/b5 (QUAD 2SIG: r0
  24000000 x16 + r123 20000000 x48). RM 16x14ch
  distinct; RQ 16x12ch distinct; RM-vs-RQ UNPAIRED
  (sets disjoint); RC 73, b0-3 38020000, b84-87
  cbed6982 ring-wide. RQ==M FULL6: M 6B vs RQ 6B agree
  (0,0),(1,1),(2,2),(3,3),(4,4),(5,5) 16/16 each;
  tabs byte-identical; agree pure diagonal (ALL
  off-diagonal 0/16); maxagree 16 all 6, distinct
  15,6,15,16,14,16 -- 28th odd-band RQ==M instance
  (viewer chain b419-27th/b421-28th sequential; b420
  even takes no ordinal); byte positions differ (QM6
  b6,7,80-83 vs TR6 b6,7,76-79, both stated in GATE;
  see prose note on the unscoped "2nd" ordinal).
  Tails STANDARD-SPLIT (RM b80-83 by COL c=off&15, RQ
  b76-79 by ROW r=off>>4 -- subscripts verified py+C;
  16/16 distinct each, 0 overlap). Sorted-unique + _N
  decls 79/80/68/73 match actual. Missing-sets EXACT:
  AC [4,5,52,53,54,80-83]; CC [4,5,52,53,84-87]; QC
  [0,4,5,6,7,19,50-55,80-87] (20, b0 in tab); RC
  [4,5,6,7,13,14,15,76-83] (15). VPOS 8/7/20/15 ==
  A-808 EXACT (quad {0,4,5,6,7,19,50-55,80-87}, b0 in
  tab + b5 varies in tab, correctly included).
  Coverage unions exact every block (const U tab U
  {b4,b5} == 88 x4, 0 overlap). Q legs M[m] + QR[q]
  both sides, NO F-legs either side. R legs RM[c] +
  RQ[r] both sides, NO F-legs. P312 refs re-read: S0
  d7fb4f01 / S1 02000000 / PBA 39000000 / C10 02000000
  / QUAD 14000000. Next-P313 preds (banked-from-r63
  CONSUMED): PB0 97016d01 NEW / PB1 02000000 47/88 /
  PBA88 26000000 x16 / C10-region 02000000 pay88 x10
  -- x4 corroborated (== A-806 predicted next EXACT).
  PBA NEW vs P312 (26000000 != 39000000); QUAD 2SIG
  24/20 vs P312 single-sig 14. AM/CM/M/QR/RM/RQ
  0-overlap vs P312 (widths P313 AM14/CM12/M12/QR24/
  RM14/RQ12 vs P312 AM14/CM8/M12/QR22/RM16/RQ12
  chars, base widths re-read first-hand). M-tails
  NEW vs P312RM col-led tails + RM-tails NEW vs
  P312RM col-led + RQ-tails NEW vs P312RQ row-led +
  cross overlaps 0 (P312T widths RM 8B/RQ 6B STANDARD
  re-read). Memo INCL PBA88 80 / C10 81 / quad88 68
  / T88 73 (A-808 re-read): impl 79/80/68/73 = memo-1
  on PBA/C10 (b5-const excluded), identical quad (b5
  step)/T88 (counter) -- standing +1 rule coherent,
  +1/+1/+0/+0. Base temp maxes _t6440/_b3903/_i3904
  (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 125661 / S1 125662 / A 125663-678 / C 125679-688 /
  Q 125689-752 / R 125753-126008): bounds + paylens
  (1x84 + 347x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (QUAD-STEP EARLY edge off6->7 emerges from
  raw lencode) + R counter b4=(0x73+2off)&FF b5=0xd6+
  (off>=71)+(off>=199) (py hex 0x73/0xD6/71/199; C
  staged decimal 115/214, re-derived: 115==0x73,
  214==0xd6) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A 7B b52,53,
  54,80-83; C 6B b52,53,84-87; Q QM6 b6,7,80-83 + R12
  b0,19,50-55,84-87, NO frags; R TM7 b13,14,15,80-83
  by COL + TR6 b6,7,76-79 by ROW, SPLIT tails) + C
  guards `if ((n) == (125661))` / `(125662)` + 4 range
  guards exact + C byte-index lists match py per block
  (A 7B, C 6B, Q 6B/12B union 18+b4/b5, R 7B/6B union
  13+b4/b5). T-mirrors T84222/84227/84232/84247/84262/
  84283 each re-read: hits the exact py guard line.
  Temps _t6441-6456 continuous-16 (base max _t6440) +
  _b3905/3907/3909/3910/3912/3913 (base max _b3903) +
  _i3906/3908/3911/3914 (base max _i3904): added-only,
  no reuse. Insert exact both sides: P312R block
  precedes (py 84220-21, C 224511; P3130 at py 84222,
  C 224514-15), at dispatch tail (N-out-of-scope
  follows; 84302 py + 224699 C; 2 scope hits py + 2
  scope hits C). Matches A-808 geometry (values
  re-checked in audit above; NO D dips: ownloop tags
  exactly the 6 P313 blocks).
- Edges own-loop ownloop421.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P313R N=126008
  off=255. edges421.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 bb/d5, bd/d5
  == raw lencode) + aform 16/16 (A head bf/d5 tail
  dd/d5 b5set {d5} NO step, 0 ff) + cform 10/10 (C
  head df/d5 tail f1/d5 b5set {d5} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head f3/d5, edge
  off6->7 125695->125696 ff/d5->01/d6 EARLY pair,
  tail 71/d6, b5set {d5,d6}, exactly 1 ff in 64 at
  o6; quad b4 base 0xf3 step2 == raw-lencode 64/64);
  ring counter 256/256 + ringraw 256/256 (head 73/d6;
  125823 off70 ff/d6 -> 125824 off71 01/d7; mid off97
  35/d7 at 125850; 125951 off198 ff/d7 -> 125952
  off199 01/d8; tail off255 71/d8; exactly 2 ff in
  256 at o70/o198); ff total x3 (Q-step o6 + 2 ring).
  odd-lencode 92+256=348/348. Ring edges + quad edge
  + tail 126008 in for-list + 2 PASS lines each py+C.
  Tail 126008: oracle sha 43e0be68514dbb4d... matches
  PINS (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P313R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf421.py (cache path) + secf421b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (125661 +
  125313 + 125662 + 125314); S0: oracle125661-vs-125313
  33/84, codeS0-vs-P312S0 33/84, positions identical;
  DIRECT tool 33/84 with identical agree-pos 51
  positions. S1: oracle125662-vs-125314 47/88,
  codeS1-vs-P312S1 47/88, positions identical; DIRECT
  47/88 identical agree-pos 41 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf421c.py (oracle C10
  cells n125679-688): [20,21x9] NON-uniform ([0]
  n125679 20/88 @ 4,38,39,46-55,60-63,84,85,86 ==
  staged EXACT; counts AND positions differ across
  cells; sig 02000000 both, NOT byte-equal; memo's
  PB1-vs-C10[0] 20/88 matches cell0). No uniform
  entry (like P309). Byte-diff discipline observed
  throughout, nothing to refute.
- C diff pure-add: numstat 608/0 (rgramc.c) + 233/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 603 content + 5 bare-blank / 0 del (see prose
  note: GATE writes "608 content"); raw py 233 content
  / 0 del. Full-digit norm ([0-9]+ -> N): C del-uniq 0
  add-uniq 153 missing 0 under the recipe AS STATED
  (diff-sign strip + trailing-';' strip, NO whitespace
  handling stated); GATE's 149 reproduces iff leading-
  whitespace-stripped AND empty-excluded (strip+
  dropempty 149, strip-only 150, dropempty-only 152 --
  recipe variant gap, same class as b405/b407/b409/b411/
  b413/b415/b417/b419; see prose note); py del-uniq 0
  add-uniq 180 missing 0 == GATE EXACT (variant-
  insensitive: 180 all four variants). del-subset-add 0
  missing holds every variant (integrity intact).
  C-tempnorm 361 / py-tempnorm 193 recorded (no GATE
  claim).
- Wall on band diff added lines (scope 307c9f53..
  75aa70e6, 904 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 608/0,
  rgram.py 233/0 purely additive, test_rgram.sh 1/1,
  PINS +62/+0.
- Tiers: merge-msg +6/+62 (cc6d8b7a), code 6 blocks,
  tier-comments `# T10P` 1766->1772 +6 == GATE stated-
  method EXACT, singletons `if n == ` 658->660 +2 ==
  GATE EXACT, range-guards `<= n <=` 704->708 +4 ==
  GATE EXACT, CLOSED T10P prints 1766->1772 +6 py +
  1766->1772 +6 C == GATE EXACT, C singleton
  `if ((n) == (` 653->655 +2 == GATE EXACT (5-count
  C-vs-py offset pre-existing, unchanged: 658-653 =
  660-655 = 5), C ranges 704->708 +4 == GATE EXACT
  (method `) <= (n)`; narrower 4-space dispatch-exact
  gives 682->686, same +4 delta), seal 1860->1866 +6
  (commit msgs; offset +94 vs CLOSED-T10P: 1866-1772
  = 94, stable b401-b421): all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-808-q905-P313
  verdict CONFIRM, tallies 30/30 + 17/17 + 14/14 =
  61/61 arith-consistent as-filed + exact-value
  corroboration incl PB0 NEW + PB1 sig-eq-P312PB1
  47/88 NOT-byte-equal SAME-as-own-C10 20/88,
  PBA88-PLAIN sig-26 M7, C10-1SIG-88 b5-const NO-step
  M6, QUAD88-2SIG-STEP r0-24/r123-20 + R12 4/4 +
  r2r3-TRUE-3B + r1-2B + r0-lcs0 + b0-split + QM6 +
  NO frags + b5-step EARLY edge + M-tails NEW,
  T88-RING-STANDARD + TM7/TR6 16/16 UNPAIRED + SPLIT
  tails + b84-87 cbed6982 + edges + consts 73/d6/71/
  199 + lencode 348/348 + VPOS 8/7/20/15 (all
  re-checked above). Sheet-vs-tables const-count note:
  Q-905 sheet rule 80/81/68/73 memo-exact (10th
  straight fully clean w2b sheet per memo; w2b-r26
  [6/8]), committed tables 79/80/68/73 still deduct
  const-b5 in PBA/C10 -- 16th consecutive tables-lag
  band (geometry exact, PORT verdict stands). No
  viewer P313 geometry answer on file at gate time
  (memo-only recon; this VERIFY is the viewer record).
  No CONFIRM-P313.md file (absence verified); A-808
  suffices per rule. Agrees with cport commit msg
  (PYID 9277, RGRAM 18554).
- Quiz: no conflicting CLAIM/GATE/FLAG on b421 (own seat
  CLAIM only; exactly 1 GATE-75aa70e6; NO-FLAG greps
  first-hand). GATE cites QNUM-22 newest -- TRUE at
  filing time (GATE 14:37, QNUM-23/24/25 postdate it
  at 14:51/16:04/23:35): NO staleness. PROSE-01:
  all hex/counts above copied from own run output;
  GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 3 prose-level notes ("raw C 608 content + 5
blank-only" reads 608+5=613 vs numstat 608 -- first-hand
is 603 content + 5 bare-blank = 608 (5th instance after
b413/b415/b417/b419, same sweep-odd-seat token);
norm-149 recipe variant gap: stated recipe yields 153,
strip+dropempty yields the claimed 149 -- integrity
holds every variant, same class as b405/b407/b409/b411/
b413/b415/b417/b419 (9th instance); "2nd full-identity
instance (after P311)": b418 (even FULL, r62 record
re-grepped) + b420 (even string-identical pure-diagonal
positions-differ, verified this round) precede -- holds
only under odd-band scope (P311 -> P313 = 2nd odd),
unstated, same class as b419's flagged ordinal; code
GREEN since gated artifact == verified artifact).
28th odd-band RQ==M instance corroborated as FULL6
(pure-diagonal agree + maxagree 16 + RQ distinctness
15/6/15/16/14/16; memo-silent on the relation; even/odd
convention holds: b420 even takes no ordinal).
Next-P314 SHAPE banked (A-808 re-read: PB0 97016d01
pay84 sig-eq-P313PB0 32/84 @126009 / PB1 01000000 pay88
NEW-sig 59/88 vs P313PB1 @126010 / PBA88 16000000 x16
@126011-26 / C10-region 02000000 pay88 x10 @126027-36
-- PB0 repeat + PB1/C10 sigs DIVERGE 01/02).
