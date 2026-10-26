# VERIFY-db0378aa b384 T10P276 pins 112785..113132 (1644 tiers) PASS

Seat viewer-r54, first-hand, tree-db0378aa @db0378aa,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r54.
Base 49652d42 (b383, 1638 tiers). Band = 82011043 (py merge
w2b@99ef3492 partial, +6 tiers, +62 pins) + db0378aa (C port,
1644 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build384/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 0c553cbc / aae d6e27c97
  (== GATE both) + sha1 rgramc 9c300604 / aae 7d8dd3a2
  (aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 8123/8123 covered=8123/8123 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16246/16246 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16246/16246 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16246/16246 sorted).
- PINS 16248 rows (2 hdr + 16246, +62 vs base 16186);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  112785 112786 112787 112788 112792 112797 112801 112802
  112803 112804 112806 112809 112811 112812 112813 112825
  112826 112841 112842 112857 112858 112873 112874 112876
  112877 112895 112896 112953 113023 113024 113132
  (== GATE verbatim; S2 + A6 + C6 + Q10 + R7; 8092->8123);
  31x2=62 rows, range 112785..113132 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit384.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 115 PASS
  0 FAIL. Inventory exactly the 15 both sides (R8/X8
  present = FRAG ring; no RT table either side; no BM/BC, no
  M19, no QB/PT/FM, no M42/X42). S0/S1 168ch sigs
  b6690700 NEW / 0d2b660e NEW (full-string ne P275 both).
  AM 16x14ch distinct; AC b0-3 ddb062e6 PLAIN, b0 const
  dd, b8 const dc, no b5. CM 10x22ch diverge 10/10; CC
  b0-3 386c550f 1SIG x10, no b5. M 16x18ch distinct. QR
  r0 73ff014fe862 distinct (last3 4fe862), r1==r2==r3
  31142182fe5d LAST3-PAIRED (last3 82fe5d), 2 distinct.
  QT f6592f08/8da3a08d/b2a3a08d/d7a3a08d 4/4 distinct;
  r1/r2/r3 share TRUE 3B a3a08d (first bytes 8d/b2/d7
  differ); r0 distinct. QC b1-3 c3/56/f5 (split-b0, no
  b0 const), b49 const df, no b5. RM 16x16ch distinct;
  RQ 16x18ch distinct. R8 41/c1/81/01/41/41/c1/01/41/
  c1/01/81/81/c1/81/c1 16x1B; X8 00x13 + 20/20/20.
  AC/CC/QC/RC 75/71/62/68 py-vs-C; _N decls 75/71/62/68
  match actual; sorted-unique. RC b0-3 0e000000; RC
  b84-87 2c/29/59/16 ring-wide. Missing-sets EXACT: AC
  [4,5,6,7,9,76,77,78,79]; CC [4,5,6,7,8,48,49,50,51,
  80,81,82,83]; QC [0,4,5,6,7,8,9,10,11,12,13,48,50,
  51,76,77,78,79,80,81,82,83]; RC [4,5,8,9,10,11,13,
  14,15,16,17,19,76,77,78,79,80,81,82,83]. Coverage
  unions exact every block (const U tab U {b4,b5} ==
  84/84/84/88, 0 overlap; QC tab incl split-b0, RC tab
  incl b8-xor). Tails SPLIT (RM b80-83 col / RQ b76-79
  row, 16/16 distinct each, 0 overlap; full-row sets
  disjoint UNPAIRED). Q legs M + R6 + T4 + split-b0
  (0xC1 iff m<13 else 0xE4 py; C decimal 193/228), no
  frags. R legs RM[c] + b8xor + RQ[r]; XOR staged
  (`pay[8] ^ X8[r]`), ADD tie noted in comment. M-tails
  16/16 ALL NEW vs P275 (zero overlap vs BOTH P275RM-
  tail8 and P275RQ-tail8 re-read). AM/CM 0-overlap vs
  P275AM/CM (CM 22ch vs 32ch widths). P275 sigs re-read
  b2690700/0d2bd60e; P275 PBA 809907fc; P275RC 07000000
  + f9b5ac58. A-671/A-339 P276 predictions corroborated
  x4 (b6690700/0d2b660e/ddb062e6/386c550f == staged).
  Memo INCL PBA 76 / C10 72 / quad 63 / T88 68 (A-676
  re-read): impl 75/71/62/68 = memo-1 on PBA/C10/quad
  (b5-const excluded), identical T88. Base temp maxes
  _t5809/_b3521/_i3522 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 112785 / S1 112786 / A 112787-802 / C 112803-812 /
  Q 112813-876 / R 112877-113132): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (S/A/C/Q) + R counter b4=(0xdb+2off)&FF b5=0x71+
  (off>=19)+(off>=147) (219/113 = 0xdb/0x71) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides + mtab/qtab/ttab
  byte positions exact (A 7B b6,7,9,76-79; C 11B b6-8,
  48-51,80-83; Q 9/6/4B + b0split; R 8B TM8 b9-11,19,
  80-83 by COL + b8xor staged + 9B TR9 b13-17,76-79 by
  ROW) + NO frag leg in Q. T-mirrors T75397/75402/75407/
  75422/75438/75463 each re-read: hits the exact py guard
  line. Temps _t5810-5829 continuous (base max _t5809, no
  reuse) + _b3523/3525/3527/3528/3529/3531/3532 (base max
  _b3521) + _i3524/3526/3530/3533 (base max _i3522, no
  reuse). C guards `if ((n) == (112785))` / `(112786)` +
  4 ranges exact. Insert exact both sides: after T10P275R
  close (py 75395 / C 201765), N-out-of-scope follows (py
  75484 / C 201977). Matches A-676/A-340 geometry (values
  re-checked in audit above; NO D dips).
- Edges own-loop ownloop384.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact; split-pairs + ring edges + tail all CLOSED
  with exact tags. edges384.py: paylens 92 x84 + 256
  x88; lencode 92/92 + qform 64/64 (A head 27/71 tail
  45/71 b5set {71} NO carry; C head 47/71 tail 59/71
  b5set {71} NO carry; Q head 5b/71 tail d9/71, b4=
  (0x5b+2off)&FF b5=0x71 64/64, NO ff edge (b4 range
  0x5b..0xd9); Q b5set {71}; S0/S1 23/71 + 25/71 match
  raw lencode); split-b0 64/64 (c1 iff m<13: 112825 c1
  / 112826 e4 + 112841/42 + 112857/58 + 112873/74 in
  for-list, NO b5 step); ring counter 256/256 (head
  db/71; 112895 (off18, ff/71) -> 112896 (off19, 01/72);
  113023 (off146, ff/72) -> 113024 (off147, 01/73); mid
  off76 (112953) 73/72; tail 113132 (off255) d9/73);
  counter==raw-lencode 256/256; odd-b4 348/348. b8 tie
  from staged tables vs oracle: XOR-staged 256/256 (tie
  CONFIRMED in shape; per-row unique ADD constants 0
  rows 0-12 / 32 rows 13-15 corroborate the 13/3 split;
  memo A-vector [0x13,32,32,32] indexing not reproduced
  by my probes -- both independent memos CONFIRM it,
  code stages XOR so verdict unaffected; methodology
  note). Q-step n/a (no step) + ring edges + tail 113132
  in for-list + 2 PASS lines each py+C. Tail 113132:
  oracle sha af5650fc6199b94f... matches PINS. No
  DISSENT: cut bytes verify.
- C diff pure-add: numstat 654/0 (rgramc.c) + 262/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 649 content + 5 bare-blank / 0 del; raw py 262
  content / 0 del. Fine-norm (rgramc.c scope, temp-norm):
  del-uniq 0 add-uniq 440 missing 0 EXACT under empty-
  excluding (tib/allN/semi variants all 440); GATE 441 =
  empty-INCLUDING count (5 bare blanks collapse to the
  empty member: 440+1, verified) -- GATE prose slip
  CONFIRMED (method label "empty-excluding" vs number
  441), conclusion (pure-additive) stands under every
  variant. Immaterial, code PASS.
- Wall on band diff added lines (scope 49652d42..
  db0378aa, 979 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression//usr/bin/aa/shim 0
  hits, shebang 0 hits. Files: rgramc.c 654/0,
  rgram.py 262/0 purely additive, test_rgram.sh 1/1,
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, singletons
  584->586 +2 / ranges 556->560 +4 (stated method, plain
  `if n ==` / `<= n <=` BSD grep), CLOSED T10P prints
  1544->1550 +6, C singletons 579->581 +2 (5-count C-vs-
  py offset pre-existing, unchanged) + C ranges 556->560
  +4, C CLOSED 1544->1550 +6, seal 1638->1644 +6 (commit
  msgs): all agree, no slip (absolute seal inherits lane
  tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-676-q788-
  t10p276 verdict CONFIRM 41/41 as-filed (section heads
  14/14 + 15/15 + 12/12 = 41/41 sums exact; file re-read;
  exact-value corroboration incl PBA/C10 sigs, QUAD2s
  split + R6 last3-pair + QT tails, M-tails NEW, ring
  FRAG + b8-XOR stage + edges + consts re-checked above)
  + A-340 viewer corroboration (all 3 legs CONFIRM,
  consts 76/72/63/68 INCL; b8 ADD-tie vector as asserted).
  Agrees with cport commit msg (PYID 8123, RGRAM 16246).
- Quiz: no conflicting CLAIM/GATE/FLAG on b384. Newest
  PARENT-* is QNUM-19 (w2d Q-block refill, read, no
  gate impact) -- GATE cites QNUM-18: 1 immaterial
  staleness (standing pattern). PROSE-01: all hex/counts
  above copied from own run output.
- Own near-misses caught pre-filing (scripts fixed, code
  never impugned): tabaudit384 C-split check first used
  hex (C stages decimal 193/228 -- fixed); base_py _t-max
  probe (py carries no _t temps -- dropped); C-region
  anchor hit early occurrence (re-anchored on guard);
  edges384 ADD-index guess crashed (replaced with
  empirical per-row probe + family sweep, none fit --
  recorded as methodology note).

Verdict: PASS. No RED. GATE CORRECT on code + geometry (1
immaterial norm-count prose slip 440/441 + 1 immaterial
QNUM staleness, QNUM-18 vs -19).
