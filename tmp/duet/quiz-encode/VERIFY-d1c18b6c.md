# VERIFY-d1c18b6c b425 T10P317 pins 127053..127400 (1890 tiers) PASS

Seat viewer-r64, first-hand, tree @d1c18b6c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r64.
Base fe9d3bf0 (b424, 1884 tiers). Band = 54bca2c5 (py merge
w2b@9de16d58 partial, +6 tiers, +62 pins) + d1c18b6c (C port,
1890 sealed). Trees manifest-identical to tips (git ls-tree
vs git ls-files identical both; WT detached at band, will
return to lanes/encode-viewer at round end).

Banked Next-P317 shape (r63 from A-816, refined by A-819)
CONSUMED FIRST and corroborated below: PB0 57a75201 pay84
sig-eq-P316PB0 31/84 @127053 / PB1 02000000 pay88
sig-eq-P316PB1 52/88 @127054 / PBA88 28000000 x16 @127055-70 /
C10-region 02000000 pay88 x10 @127071-80 -- triple head
repeat, all exact.

- Build: make -C src/c BUILDDIR=build425 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc ff51e8b553f8d3e646a24
  df8619a48b341443a0affe66817597a31805e30358d / aae
  d6e27c97ced21673cc73eee061ffdbd7f0358a87e482056c222a
  867202110785 (== GATE sha256 both; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 9408/9408 covered=9408/9408 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir).
- RGRAM py 18816/18816 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18816/18816 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18816/18816;
  GATE claims sorted only, raw corroborated too).
- PINS 18818 rows (2 hdr + 18816, +62 vs base 18756);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq). For-list delta vs base
  +31/-0 (9377->9408):
  127053 127054 127055 127056 127062 127063 127069
  127070 127071 127072 127075 127076 127079 127080
  127081 127088 127096 127097 127103 127104 127113
  127129 127143 127144 127145 127231 127232 127250
  127359 127360 127400
  (== GATE sampled list EXACT, verified programmatically;
  the 4 extra 127xxx numbers my first regex swept up are
  the explicitly-unsampled C offs 127073/74/77/78).
  Decomposition first-hand from the added set: 2 sing
  (127053/54) + A head/mid1/mid2/tail pairs (6: 55/56 +
  62/63 + 69/70; offs 0,1,7,8,14,15) + C head/mid/tail
  pairs (6: 71/72 + 75/76 + 79/80; offs 0,1,4,5,8,9;
  offs 2,3,6,7 = 73/74/77/78 unsampled, absence
  verified) + Q head 81/off7 88/mid-pair 96/97/edge-pair
  103/104/off32 113/off48 129/tail-pair 143/144 (10:
  offs 0,7,15,16,22,23,32,48,62,63; step@23 edge-pair
  covered + tail pair, first-hand) + R head 145/edge-pair
  231/232/mid 250/edge-pair 359/360/tail 400 (7: offs
  0,86/87,105,214/215,255; 1-mid shape, both counter
  edges pair-covered, first-hand). 31x2=62 rows, range
  127053..127400 exact. PINS-new-N == for-added 31/31,
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py; 22/0 per GATE
  method -- own run GREEN rc=0). AEAD env-blocked
  first-hand (`import lz4` Traceback, same as r60-r64
  record); band touches no proto/ sources (numstat
  proves), NO verdict impact.
- Tables audit own script tabaudit425.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 148 PASS
  0 FAIL. Inventory exactly the 19 both sides, C==py
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC + FT25/FT26/FT27/
  FT29/FT34/FT35A/FT35B; no bare F, no F0/F1, no BM/BC,
  no M19/X19, no M42/X42/H42/L42, no QB/PT/FM, no RT/TT
  (ring, not ROWTAIL), no QT (R19 carries b84-87 inside
  QR)).
  S0 168ch sig 57a75201 sig-eq-P316PB0 (31/84 payload
  diff vs P316S0 @ b4-11,34,35,41-48,50,51,56-63,80,81,
  83 first-hand, NOT byte-equal) / S1 176ch sig 02000000
  sig-eq-P316PB1 (52/88 payload diff vs P316S1 @ b4-14,
  17-27,36-38,40-43,48-55,64-71,80,81,83-87, NOT
  byte-equal; 37/88 diff vs own-C10[0] assembled, NOT
  byte-equal; sig SAME-as-own-C10), staged as
  full-payload singletons.
  AM 16/16 16ch (8B) distinct, AC 78, b0-3 28000000
  (b0 const 28), no b4/b5. C10-1SIG-88-TAIL sig 02000000
  x10 SAME-as-PB1 (sig in CC b0-3 consts, b0 const 02;
  CM 10/10 diverge 8ch; CC b80-83 const c6f29582
  first-hand; CC has no b4/b5, b5 const e0 full block
  via lencode).
  S1-vs-own-C10 staged per-cell (each cell own lencode)
  [37]x10 TRUE-UNIFORM count+position (cell0 37 @
  4,16-18,22-26,28-35,56-71,84-87 EXACT; positions
  identical all 10 staged; sig 02000000 both, NOT
  byte-equal -- 13th TRUE-uniform case on record, 12th
  excluding unverified P299; beyond-GATE values
  corroborated by oracle leg below; see prose note on
  the GATE's "6th" ordinal).
  QUAD88-2SIG-4R-FRAG6 (row0 2a000000 x16 + rows1-3
  13000000 x48; QM4 b80-83 shared 16/16 x3 vs row0, NO
  frags + R19 b0,8-15,19,28,30-33,84-87 rows 4/4
  distinct tuples UNPAIRED (r0 fully distinct vs all,
  r123 share 10B 13593edf3d654990008d, r23 share 15B
  13593edf3d654990008d3722eb351e) + tails b84-87 4
  distinct d1ee8e61/a8437798/3de4c0cb/62e4c0cb, r2r3
  TRUE-3B e4c0cb (differ b84 3d/62), r0/r1 lcs0 vs all
  rows (r1-lcs0 vs r2/r3 too), r2r3-lcs3; b0 row-led
  split r0=2a/r123=13 (b1-3 const 00 in QC).
  FRAG6 exact first-hand: b25 q0 const f2 / q123 FT25[m]
  {72,f2} + b26 q0 const 7a / q123 FT26[m]
  {7e,7f,f8,f9,fa} + b27 q0 const 7e / q123 FT27[m]
  {17,1f} + b29 q0 FT29[m] {5d,5f,7d,7f} / q1 const bc
  / q23 const fc + b34 q0 FT34[m] {07,47,87,c7} / q1
  const f7 / q23 const c0 + b35 q0 FT35A[m] 15 distinct
  / q123 FT35B[m] 16 distinct; C consts 242/122/126/
  188/252/247/192 == py hex f2/7a/7e/bc/fc/f7/c0; NO
  ADD arithmetic (fadd236 absent both sides) -- FRAG6 =
  consts + coltabs only, FIRST of class; r123-tab
  2/5/2 (FT25/26/27 distinct-counts) + r0-tab 4/4/15
  (FT29/FT34/FT35A) + r123-tab 16 distinct (FT35B).
  QC 57, b1-3 const 00, b0 in tab (row-led split), no
  b4/b5, b5 STEP e0->e1 @off23 (edge 127103->127104
  ff/e0->01/e1).
  RQ==M TAILS4-ONLY: M 4B vs RQ 7B agree (0,3),(1,4),
  (2,5),(3,6) 16/16 each; last-4 tails agree, 3 head
  cols isolated maxagree 0,0,0; tabs differ (M-tail-set
  vs RQ-tail-set position-mapped, zero off-pattern FULL
  agrees); RQ distinctness [4,7,14,16,14,16,16] (new
  data, no GATE claim). 30th odd-band RQ==M instance
  (viewer chain b421-28th/b423-29th/b425-30th
  sequential); 3rd TAILS4-ONLY degree instance (after
  P309 heads 0,1,5,1,0 + P315 heads 0,1,0, both
  re-verified vs r62/r63 records). Memo-silent on the
  relation (A-823 notes cell-[0] only).
  Tails STANDARD-SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each, 0
  overlap UNPAIRED; subscripts + tail positions
  verified in dispatch text both sides); RM 16/16 8ch
  + RQ 16/16 7ch distinct, sets disjoint.
  M-tails 16/16 ALL NEW vs P316T RM col-led tails
  (overlap 0); RM-tails (b80-83) ALL NEW vs P316T RM
  col-led tails (overlap 0); RQ-tails (b76-79) ALL NEW
  vs P316T RQ row-led tails (overlap 0); cross overlaps
  0 (P316T widths RM
  10B/RQ 9B 3SIG STANDARD-split first-hand; tails
  compared position-aware against col-led/row-led
  sets).
  Sorted-unique + _N decls 78/82/57/71 match actual.
  Missing-sets EXACT: AC-10 [4,5,28-31,80-83] = b4,b5+
  M8; CC-6 [4,5,84-87] = b4,b5+M4; QC-31
  [0,4,5,8-15,19,25-35,80-87] = b0,b4,b5+QM4(80-83)+
  R19(0,8-15,19,28,30-33,84-87)+F6(25,26,27,29,34,35);
  RC-17 [4,5,29,34,35,40-43,76-83] = b4,b5+TR7(29,34,
  35,76-79)+TM8(40-43,80-83). VPOS 9/5/31/17 == A-823
  EXACT (PBA b4+M8 b5-const-excluded / C10 b4+M4 /
  quad b0,b4,b5+QM4+R19+F6, b0 in tab / T b4,b5+TM8+
  TR7, b0 const-excluded). Coverage unions exact every
  block (const U tab U {b4,b5} == 88 x4, 0 overlap).
  Q legs M[m] + QR[q] + FRAG F-legs both sides; R legs
  RM[c] + RQ[r] both sides, NO F-legs in R
  (STANDARD RM-col / RQ-row verified in region text).
  P316 refs re-read: S0 57a75201 / S1 02000000 /
  PBA 28000000 / C10 02000000 / QUAD 2a000000.
  PBA sig 28 SAME-as-P316 (28000000, 2nd band at 28
  after b424 NEW); QUAD 2SIG 2a/13 NEW vs P316 1-sig
  2a (r0 keeps 2a, r123 NEW 13). M-tails true novelty
  vs P316T (position-aware 0 overlaps throughout).
  Memo INCL PBA88 79 / C10 83 / quad88 57 / T88 71
  (A-823 re-read): impl 78/82/57/71 = memo-exact on
  quad (b5 STEP-varies, in tab) and T88 (b5 varies, no
  deduction); writer-1 on PBA/C10: impl tables still
  deduct const-b5 on PBA/C10 (b5 covered by lencode
  instead) while Q-909 sheet counts b5 (memo A-823
  confirms the sheet) -- S-F arithmetic persists in
  committed tables though the sheet is FIXED; geometry
  exact, PORT verdict stands. 20th consecutive
  tables-lag band (b425 pattern +1/+1/+0/+0: PBA/C10
  lag, quad/T88 exact; running b412-b425 per GATE +
  r63/r64 records).
  Base temp maxes _t6506/_b3943/_i3944 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 127053 / S1 127054 / A 127055-70 / C 127071-80 /
  Q 127081-144 / R 127145-400): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C both sides (b5
  const e0 emerges from raw lencode, NO step) + Q/R
  explicit counters both sides (Q b4=(0xd3+2off)&FF
  b5=0xe0+(off>=23); R b4=(0x53+2off)&FF b5=0xe1+
  (off>=87)+(off>=215); py hex 0xD3/0xE0/0x53/0xE1;
  C staged literals 211/224 + 83/225, re-derived:
  211==0xd3, 224==0xe0, 83==0x53, 225==0xe1) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 8B b28-31,80-83;
  C 4B b84-87; Q QM4 b80-83 + R19 b0,8-15,19,28,30-33,
  84-87 + FRAG6 b25/26/27/29/34/35 per-row const/tab
  split above; R TM8 b40-43,80-83 by COL + TR7 b29,34,
  35,76-79 by ROW, SPLIT tails) + C guards
  `if ((n) == (127053))` / `(127054)` + 4 range guards
  exact + counter literals exact + C byte-index lists
  match py per block (A 8B, C 4B, Q 4B/19B/1Bx7,
  R 8B/7B). T-mirrors T85297/85302/85307/85322/85337/
  85395 each re-read: hits the exact py guard line
  (85297/85302/85307/85322/85337/85395); C mirrors
  identical numbers in comments. Temps _t6507.._t6536
  continuous-30 (base max _t6506) + _b3945/3947/3949/
  3950/3952/3953 (base max _b3943) + _i3946/3948/3951/
  3954 (base max _i3944): added-only, no reuse.
  Insert exact both sides: P316R block precedes (py
  guard 85297 follows P316R close; C block 227104
  follows P316R close), at dispatch tail (P317R
  immediately precedes LAST N-out-of-scope: py 85414
  + C 227374; 2 scope hits py + 2 scope hits C).
  Matches A-823 geometry (values re-checked in audit
  above; NO D dips: ownloop tags exactly the 6 P317
  blocks).
- Edges own-loop ownloop425.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (0 miss, cache pre-warmed). Census R256/Q64/
  A16/C10/S0/S1 exact. Tail line: CLOSED T10P317R
  N=127400 off=255. edges425.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 9b/e0, 9d/e0
  == raw lencode) + aform 16/16 (A head 9f/e0 tail
  bd/e0 b5set {e0} NO step, 0 ff) + cform 10/10 (C
  head bf/e0 tail d1/e0 b5set {e0} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head d3/e0 edge
  off22->23 127103->127104 ff/e0->01/e1 tail 51/e1,
  b5set {e0,e1} STEP e0->e1 @off23; quad b4 base 0xd3
  step2 64/64 range d3..51 NO edge, tail 51/e1 exact) +
  ring counter 256/256 + ringraw 256/256 (head
  53/e1; 127231 off86 ff/e1 -> 127232 off87 01/e2;
  mid off105 25/e2 at 127250; 127359 off214 ff/e2 ->
  127360 off215 01/e3; tail 51/e3; exactly 2 ff in
  256 at o86/o214); ff total x3 (Q-edge + 2 ring);
  ff-in-Q 1. odd-lencode 92+256=348/348 (346 + S0/S1
  embedded b4/b5 9b/e0 + 9d/e0). Ring edges + tail
  127400 in for-list + 2 PASS lines each py+C. Tail
  127400: oracle sha 498d852ce2cb06a7... matches PINS
  (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P317R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf425.py (cache path) + secf425b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (127053 +
  126705 + 127054 + 126706); S0: oracle127053-vs-126705
  31/84, codeS0-vs-P316S0 31/84, positions identical;
  DIRECT tool 31/84 with identical agree-pos 53
  positions. S1: oracle127054-vs-126706 52/88,
  codeS1-vs-P316S1 52/88, positions identical; DIRECT
  52/88 identical agree-pos 36 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf425c.py (oracle C10
  cells n127071-80): [37]x10 TRUE-UNIFORM counts AND
  positions identical all 10 (cell0 pos
  4,16-18,22-26,28-35,56-71,84-87 == staged EXACT;
  sig 02000000 both, NOT byte-equal). Byte-diff
  discipline observed throughout, nothing to refute.
- C diff pure-add: numstat 821/0 (rgramc.c) + 392/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 816 content + 5 bare-blank / 0 del (verified
  bare, no whitespace); full-digit norm ([0-9]+ -> N):
  C del-uniq 0 add-uniq 201/192/200/191 across the 4
  strip/dropempty variants, missing 0 every variant;
  py del-uniq 0 add-uniq 227/225/227/225, missing 0
  every variant (integrity intact). C-tempnorm 478 /
  py-tempnorm 287 recorded (no GATE claim).
  Band-level sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope fe9d3bf0..
  d1c18b6c, 1276 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 821/0,
  rgram.py 392/0 purely additive, test_rgram.sh 1/1
  (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62 (54bca2c5), code 6 blocks,
  tier-comments `# T10P` 1790->1796 +6, singletons
  `if n == ` 666->668 +2, range-guards `<= n <=`
  720->724 +4 = +6, CLOSED T10P prints 1790->1796 +6
  py + 1790->1796 +6 C (all-indent literal methods,
  first-hand; the 4-space dispatch-exact subset gives
  656->658 +2 / 698->702 +4 both sides identically --
  stated-method pluralism documented, deltas agree
  every side; no else-if either side), seal 1884->1890
  +6 (commit msgs; offset +94 vs CLOSED-T10P:
  1890-1796 = 94, stable b401-b425): all agree, no
  slip. C guards: singleton `if ((n) == (` 661->663
  +2 (5-count C-vs-py singleton offset pre-existing,
  unchanged: 666-661 = 668-663 = 5), range lower-bound
  `) <= (n)` 720->724 +4 (py=C dispatch-exact).
- CONFIRM evidence (CONVERT-01 rule b): A-823-q909-P317
  memo CONFIRM 74/74 CLEAN (verifier v209.py 74/74
  PASS, tier GATED PORT, ZERO section-F, FRAG6 tier;
  w2b-r27 [2/8], clean streak 14 straight, quoted
  verbatim; exact-value corroboration incl PB0
  sig-eq-P316PB0 31/84 NOT-byte-equal, PB1 sig-eq-
  P316PB1 52/88 NOT-byte-equal SAME-as-own-C10 37/88,
  PBA88-PLAIN-M8b28 sig-28 b0-const-28 b5-const-e0
  16/16 distinct NO pair, C10-1SIG-88-TAIL SAME-as-
  PB1-sig b0-const-02 b5-const-e0 10/10 diverge 8ch,
  QUAD88-2SIG-4R-FRAG6 r0-2a + r123-13 + R19 4/4
  UNPAIRED pairwise-distinct-rows + share-10B +
  r23-share-15B + r2r3-TRUE-3B + r0/r1-lcs0 +
  b0-row-led-split + b5-STEP-e0->e1-@off23 + QM4 +
  FRAG6 exact (r123-tab 2/5/2 + r0-tab 4/4/15 +
  r123-tab 16 distinct) + tails 4-distinct + M-tails
  ALL NEW, T88-RING-STANDARD sig-3f010000 + TM8 by COL
  + TR7 by ROW UNPAIRED + SPLIT tails + b84-87
  bf2724fb + ring counter 53/e1/87/215 + lencode
  348/348 (all re-checked above); plus sheet-vs-
  tables const-count note: Q-909 sheet 79/83/57/67
  memo-exact, committed tables 78/82/57/71 still
  deduct const-b5 on PBA/C10 -- 20th consecutive
  tables-lag band, geometry exact, PORT verdict
  stands). Agrees with cport commit msg (PYID 9408,
  RGRAM 18816). No CONFIRM-P317.md file on record
  (not claimed); A-823 suffices per rule. No viewer
  P317 geometry answer on file at gate time (memo-only
  recon; this VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b425 (own seat
  CLAIM only; exactly 1 GATE-d1c18b6c; zero FLAG hits
  on b425/d1c18b6c/T10P317/127053; even base b424 used
  as diff-base only, NOT gated (sweep2 turf respected);
  next-band GATE-f278bdf0 mentions d1c18b6c as base --
  adjacency, no verdict on b425). GATE cites QNUM-23
  newest -- TRUE at filing time (QNUM-24/25 postdate
  it at 16:04/23:35): NO staleness. PROSE-01:
  all hex/counts above copied from own run output;
  GATE re-read in FULL before filing.
- RQ==M chain: b425 odd TAILS4-ONLY (M 4B vs RQ 7B
  agree (0,3),(1,4),(2,5),(3,6) 16/16 each; last-4
  tails agree; heads per-RQ-col maxagree 0,0,0; RQ
  distinctness 4/7/14/16/14/16/16; tabs differ; zero
  off-pattern FULL agrees). 30th odd-band instance
  (viewer chain b421-28th FULL6/b423-29th TAILS4-ONLY/
  b425-30th TAILS4-ONLY sequential); 3rd TAILS4-ONLY
  degree (P309 heads 0,1,5,1,0 + P315 heads 0,1,0 +
  P317 heads 0,0,0). Memo-silent on the relation.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 3 prose-level notes (raw-C "821 content + 5
blank-only" reads 821+5 vs numstat 821 -- first-hand is
816 content + 5 bare-blank = 821, 7th instance after
b413/b415/b417/b419/b421/b423, same sweep-odd-seat
token; norm-191/225 recipe variant gap: stated recipe
yields C-201/py-227, strip+dropempty yields the claimed
C-191 (py-225 needs strip) -- integrity holds every
variant, 11th instance same class as b405/b407/b409/
b411/b413/b415/b417/b419/b421/b423; "6th TRUE-uniform
case after P299 + P303 + P307 + P311 + P315": P300
56/84 (r60 filed record) + P306 28/84 (r61 count+
position) + P308 59/88 (r62 count+position) + P310
49/88 (r62 count+position) + P312 45/88 (r63 count+
position) + P314 29/88 (r63 count+position) + P316
76/88 (r64 count+position, this round) are all on
record, making P317 THIRTEENTH on record (12th
excluding unverified P299) -- the ordinal holds only
under a narrower scope the GATE doesn't state, same
class as b419's flagged "4th"/b421/b423; code GREEN
since gated artifact == verified artifact). Next-P318
SHAPE banked (A-823 re-read: PB0 36ac6c01 pay84 NEW
@127401 (differs vs P317 heads, repeat era ENDS) / PB1
02000000 pay88 @127402 / PBA88 27000000 x16 @127403-18 /
C10-region 02000000 pay88 x10 @127419-28).
