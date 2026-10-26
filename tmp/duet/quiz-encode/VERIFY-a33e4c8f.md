# VERIFY-a33e4c8f b385 T10P277 pins 113133..113480 (1650 tiers) PASS

Seat viewer-r54, first-hand, tree-a33e4c8f @a33e4c8f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r54.
Base db0378aa (b384, 1644 tiers). Band = 9f1aa46d (py merge
w2b@e2008f5b partial, +6 tiers, +60 pins) + a33e4c8f (C port,
1650 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build385/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 3befc1e6 / aae 7d8dd3a2
  + sha256 rgramc 3552fba3 / aae d6e27c97 (== GATE all 4;
  aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 8153/8153 covered=8153/8153 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16306/16306 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16306/16306 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16306/16306 sorted).
- PINS 16308 rows (2 hdr + 16306, +60 vs base 16248);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +30/-0:
  113133 113134 113135 113136 113140 113145 113149 113150
  113151 113152 113154 113156 113158 113160 113161 113176
  113177 113192 113193 113208 113209 113224 113225 113279
  113280 113327 113407 113408 113455 113480
  (== GATE verbatim; S2 + A6 offs 0,1,5,10,14,15 + C6 offs
  0,1,3,5,7,9 (offs 2,4,6,8 unsampled) + Q8 offs 0,15/16,
  31/32,47/48,63 + R8 offs 0,54/55,102,182/183,230,255;
  8123->8153); 30x2=60 rows, range 113133..113480 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit385.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 115 PASS
  0 FAIL. Inventory exactly the 14 both sides (RT present
  = ROWTAIL TT tab; no BM/BC, no M19, no QB/PT/FM, no
  M42/X42, no R8/X8). S0/S1 168ch sigs b6aa0700 NEW /
  d505540f NEW (both NEW strings: 30/84 + 59/84 differ vs
  P276; S0 diff @ b1,4-11,42-48,50,51,56-67 EXACT). AM
  16x16ch distinct; AC b0-3 e09a1ffa PLAIN, b0 const e0.
  CM 10x24ch diverge 10/10 CARRY (rows 0-5 share 8B head
  3fbcb44875f06ba6 + distinct 4B tails 45f14707/65f14707/
  05004807/25004807/a5516907/c5516907; rows 6-9 all-
  distinct); CC b0-3 f5f4570f 1SIG x10. M 16x16ch
  distinct. QR r0 acbca4ea955e68 distinct (last3 955e68),
  r1==r2==r3 cb3c329115c98d LAST3-PAIRED (last3 15c98d),
  2 distinct. QT 0b6db88f/b3dff5e9/246311ea/8a1ff0ea 4/4
  distinct; last-2B b88f/f5e9/11ea/f0ea all distinct;
  all-pairs shared suffix max 1B (2 hex chars, only r2/r3
  share last 1B ea). RM 16x16ch distinct; RQ 16x6ch
  14/16 PAIRED (r6==r7 fe4de6 + r14==r15 ff6d87, tails
  disambiguate: RT[6]!=RT[7], RT[14]!=RT[15]); RT 16x8ch
  distinct. RT==M-tails 16/16 same-index + set-eq (RT[r]
  == M bytes 4-7; ROWTAIL degree; RQ 3B has no M
  containment). AC/CC/QC/RC 74/70/63/71 py-vs-C; _N decls
  74/70/63/71 match actual; sorted-unique. RC b0-3
  08000000; RC b84-87 27/83/81/1e ring-wide. Missing-sets
  EXACT: AC [4,5,24,25,26,27,76,77,78,79]; CC [4,5,24,25,
  26,27,28,29,30,31,80,81,82,83]; QC [4,5,21,22,23,24,25,
  26,27,28,29,30,31,76,77,78,79,80,81,82,83]; RC [4,5,29,
  34,35,40,41,42,43,76,77,78,79,80,81,82,83]. Coverage
  unions exact every block (const U tab U {b4,b5} ==
  84/84/84/88, 0 overlap). Q legs M + R7 + T4, no frags,
  no split. R legs RM[c] + RQ[r] + RT[r] ROW-led. M-tails
  16/16 ALL NEW vs P276T row-0; M-full ALL NEW vs P276RQ;
  QT 4/4 ALL NEW vs P276QT; RM ALL NEW vs P276RM. P276
  sigs re-read b6690700/0d2b660e/ddb062e6/386c550f (==
  A-671/A-339 predicted). A-676/A-340 P277 predictions
  corroborated x4 (b6aa0700/d505540f/e09a1ffa/f5f4570f ==
  staged). Memo INCL PBA 75 / C10 70 / quad 64 / T88 71
  (A-682 re-read): impl 74/70/63/71 = memo-1 on PBA/quad
  (b5-const excluded), identical C10/T88. Base temp maxes
  _t5829/_b3532/_i3533 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 113133 / S1 113134 / A 113135-150 / C 113151-160 /
  Q 113161-224 / R 113225-480): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (S/A/C/Q; b5-consts + carry edge emerge from raw
  lencode) + R counter b4=(0x93+2off)&FF b5=0x74+
  (off>=55)+(off>=183) (147/116 = 0x93/0x74, C stages
  decimal) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/qtab/ttab byte positions exact (A 8B
  b24-27,76-79; C 12B b24-31,80-83; Q 8/7/4B QM8 b21-23,
  31,76-79 + R7 b24-30 + T4 b80-83; R 8B TM8 b40-43,
  76-79 by COL + 3B TR3 b29,34,35 by ROW + 4B TT b80-83
  ROW-led by r) + NO frag leg in Q. T-mirrors T75656/
  75661/75666/75681/75697/75720 each re-read: hits the
  exact py guard line. Temps _t5830-5849 continuous (base
  max _t5829, no reuse) + _b3534/3536/3538/3539/3540/
  3542/3543/3544 (base max _b3532) + _i3535/3537/3541/
  3545 (base max _i3533, no reuse). C guards `if ((n) ==
  (113133))` / `(113134)` + 4 ranges exact. Insert exact
  both sides: after T10P276R close (py 75654 / C 202403),
  N-out-of-scope follows (py 75741 / C 202613; C has 2
  scope hits, rfind-used). Matches A-682/A-341 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop385.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (318 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. edges385.py: paylens 92 x84 + 256 x88;
  lencode 92/92 + cform 10/10 + qform 64/64 (A head
  df/73 tail fd/73 b5set {73} NO carry; C head ff/73
  (113151) -> 01/74 (113152) FIRST-CELL CARRY o=0->1,
  tail 11/74 (113160), b5set {73,74}, b4=(0xff+2off)&FF
  b5=0x73+(off>=1) 10/10; Q head 13/74 tail 91/74, b4=
  (0x13+2off)&FF b5=0x74 64/64, NO ff edge (b4 range
  0x13..0x91); Q b5set {74}; S0/S1 db/73 + dd/73 match
  raw lencode); ring counter 256/256 (head 93/74; 113279
  (off54, ff/74) -> 113280 (off55, 01/75); 113407
  (off182, ff/75) -> 113408 (off183, 01/76); mid off102
  (113327) 5f/75; off230 (113455) 5f/76; tail 113480
  (off255) 91/76); counter==raw-lencode 256/256;
  odd-b4 348/348. Carry edge + ring edges + tail 113480
  in for-list + 2 PASS lines each py+C. Tail 113480:
  oracle sha fdaa0c42882cb62c... matches PINS. No
  DISSENT: cut bytes verify.
- C diff pure-add: numstat 636/0 (rgramc.c) + 257/0
  (rgram.py) + 1/1 (for-line) + 60/0 (PINS) == GATE;
  raw C 631 content + 5 bare-blank / 0 del; raw py 257
  content / 0 del. Fine-norm sweep (keep-empty, [0-9]+
  -> N, sign/';' strip, python sets): C del-uniq 0
  add-uniq 184, py del-uniq 0 add-uniq 208, 0 missing
  EXACT (== GATE).
- Wall on band diff added lines (scope db0378aa..
  a33e4c8f, 954 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression//usr/bin/aa/shim 0
  hits, shebang 0 hits. Files: rgramc.c 636/0,
  rgram.py 257/0 purely additive, test_rgram.sh 1/1,
  PINS +60/+0.
- Tiers: merge-msg +6/+60, code 6 blocks, tier-comments
  1550->1556 +6, singletons 586->588 +2 / ranges
  560->564 +4 (stated method, plain `if n ==` /
  `<= n <=` BSD grep), CLOSED T10P prints 1550->1556
  +6, C singletons 581->583 +2 (5-count C-vs-py offset
  pre-existing, unchanged) + C ranges 560->564 +4,
  seal 1644->1650 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-682-q789-
  t10p277 verdict CONFIRM 39/39 as-filed (section heads
  13/13 + 14/14 + 12/12 = 39/39 sums exact; file re-read;
  exact-value corroboration incl PBA/C10-carry sigs,
  QUAD1s + R7 last3-pair + QT tails, M-tails NEW, ring
  ROWTAIL + PAIRED TR3 + edges + consts re-checked above)
  + A-341 viewer corroboration (all 3 legs CONFIRM,
  consts 75/70/64/71 INCL). Agrees with cport commit msg
  (PYID 8153, RGRAM 16306).
- Quiz: no conflicting CLAIM/GATE/FLAG on b385. Newest
  PARENT-* is QNUM-19 (w2d Q-block refill, read, no
  gate impact) -- GATE cites QNUM-18: 1 immaterial
  staleness (standing pattern). PROSE-01: all hex/counts
  above copied from own run output.
- Own near-misses caught pre-filing (scripts fixed, code
  never impugned): ownloop385 sed-carried sample-N list
  (replaced with P277 Ns pre-run).

Verdict: PASS. No RED. GATE CORRECT on code + prose (1
immaterial QNUM staleness, QNUM-18 vs -19).
