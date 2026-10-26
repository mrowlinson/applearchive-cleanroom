# VERIFY-9cac7b4f b393 T10P285 pins 115917..116264 (1698 tiers) PASS

Seat viewer-r56, first-hand, tree-9cac7b4f @9cac7b4f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r56.
Base 4ea39e1c (b392, 1692 tiers). Band = b82c0c66 (py merge
w2b@b39d81f0 partial, +6 tiers, +62 pins) + 9cac7b4f (C port,
1698 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build393/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 457b9614295d0cf6 / aae
  7d8dd3a2d118e0db + sha256 rgramc 43e46a0777b94e4b / aae
  d6e27c97ced21673 (== GATE all 4; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 8406/8406 covered=8406/8406 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16812/16812 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16812/16812 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 16812/16812).
- PINS 16814 rows (2 hdr + 16812, +62 vs base 16752);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  115917 115918 115919 115920 115926 115927 115933 115934
  115935 115936 115939 115940 115943 115944 115945 115960
  115961 115967 115968 115977 115985 115993 116000 116008
  116009 116095 116096 116137 116223 116224 116264
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 115937/115938/
  115941/115942 unsampled) + Q10 offs 0,15/16,22/23,32,
  40,48,55,63 + R7 offs 0,86/87,128,214/215,255;
  8375->8406); 31x2=62 rows, range 115917..116264 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit393.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 122 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/1SIG/QUAD88-4R/SWAPPED ring; no QT/RT/TT; no
  BM/BC, no M19/XA19, no QB/PT/FM, no M42/X42/H42/L42);
  C==py 12/12. S0/S1 168ch sigs 19f80a00 NEW / ddbef415
  NEW (full-string NEW vs BOTH P284 strings; S0-vs-P284S0
  34/84 @ b0-2,4-11,41-51,56-67 EXACT + cross-P284S1 62,
  S1-vs-P284S1 55/84 @ b0-11,13-17,19-23,30-39,45-51,60-
  71,80-83 EXACT + cross-P284S0 65). AM 16x18ch distinct;
  AC 77, b0-3 01/00/00/00 (b0 const 01), no b4/b5, PBA
  sig 01000000 x16 PLAIN. CM 10x24ch 10/10 diverge
  (rows0-5 share 8B head 913cb87bb5cbe01a; rows6-9 heads
  da7ca5b2/b07c1209/9cfcf300/9cfcf300); CC 70, b0-3
  cd23fd15 full-sig in consts, no b4/b5 (C10-1SIG x10).
  M 16x16ch distinct. QR 4x22ch 4-distinct UNPAIRED; r0
  413c512d95c6ca7c4d8899 distinct; r123 share 7B prefix
  fdbce3ce75d9f2 + last byte 5f; tails b84-87 7c4d8899/
  a28eab5f/1719ad5f/eab0da5f 4/4 distinct; suffix-LCS
  (1,2)=(1,3)=(2,3)=1, r0-vs-rest 0. QC 67, b0-3
  01000000, no b4/b5. RM 16x14ch distinct; RQ 16x14ch
  distinct; RC 72, b0-3 16/00/00/00, b84-87 e4/65/4e/71
  ring-wide. RQ==M TAILS-only FIRST (M 8B vs RQ 7B:
  RQ[3:7]==M[4:8] 16/16; 7x8 agree matrix clean tail
  block at (3,4),(4,5),(5,6),(6,7) all 16; RQ[0:3] own
  max agree 1/16; RQ0 3-distinct 0f/1e/1f counts 9/6/1;
  RQ1 7-distinct 10/30/50/70/90/b0/d0 lo-nibble 0;
  RQ2 16-distinct). RM-vs-RQ UNPAIRED (sets disjoint).
  Tails SWAPPED-SPLIT (RM b76-79 by COL, RQ b80-83 by
  ROW, 16/16 distinct each, 0 overlap). Sorted-unique +
  _N decls 77/70/67/72 match actual. Missing-sets EXACT:
  AC [4,5,28,29,30,31,32,80,81,82,83]; CC [4,5,24,25,26,
  27,28,29,30,31,80,81,82,83]; QC [4,5,25,26,27,28,29,
  30,31,32,33,34,35,80,81,82,83,84,85,86,87]; RC [4,5,
  29,34,35,40,41,42,76,77,78,79,80,81,82,83]. Coverage
  unions exact every block (const U tab U {b4,b5} ==
  88/84/88/88, 0 overlap). Q legs M[m] + QR[q], no
  frags. R legs RM[c] + RQ[r] SWAPPED. P284 refs
  re-read: S0 99f00700 / S1 4513630f / PBA 5d3431f6 /
  C10 c432f015 (== r55 P284 preds EXACT). P285 preds
  (A-705/A-348 Next-P285: 19f80a00/ddbef415/01000000/
  cd23fd15) x4 corroborated staged. PBA NEW vs P284;
  C10 NEW vs P284. M-tails 16/16 ALL NEW vs P284 RM
  col-led tails (overlap 0); RM-tails ALL NEW vs P284
  RM-tail8 + P284 RQ-tail8 (overlap 0 x2). Memo INCL
  PBA88 78 / C10 71 / quad88 67 / T88 72 (A-709
  re-read): impl 77/70/67/72 = memo-1 on PBA/C10
  (b5-const excluded), identical quad/T88. Base temp
  maxes _t5979/_b3621/_i3622 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 115917 / S1 115918 / A 115919-934 / C 115935-944 /
  Q 115945-116008 / R 116009-264): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-const/step emerge from raw lencode) +
  R counter b4=(0x53+2off)&FF b5=0x8a+(off>=87)+
  (off>=215) (py hex; C stages decimal 83/138/87/215,
  re-derived from code text both sides) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides + mtab/rtab
  byte positions exact (A 9B b28-32,80-83; C 12B b24-31,
  80-83; Q QM8 b25-27,35,80-83 + R11 b28-34,84-87; R TM7
  b40-42,76-79 by COL + TR7 b29,34,35,80-83 by ROW) +
  NO frag leg in Q. T-mirrors T77591/77596/77601/77616/
  77632/77653 each re-read: hits the exact py guard
  line. C guards `if ((n) == (115917))` / `(115918)` +
  4 range guards exact. C byte-index lists match py per
  block (A 9B, C 12B, Q 8B/11B, R 7/7B). Temps
  _t5980-5995 continuous (base max _t5979) + _b3623/
  3625/3627/3628/3630/3631 (base max _b3621) + _i3624/
  3626/3629/3632 (base max _i3622): added-lines-only
  refs (base tree zero refs to new temps) prove no
  reuse. Insert exact both sides: after T10P284R close,
  at dispatch tail (N-out-of-scope fallthrough follows;
  C 2 scope hits, py 2 scope hits). Matches A-709/A-349
  geometry (values re-checked in audit above; NO D dips:
  ownloop tags exactly the 6 P285 blocks).
- Edges own-loop ownloop393.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P285R N=116264 off=255.
  edges393.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 9b/89, 9d/89 == raw lencode
  0x899B/0x899D) + aform 16/16 (A 88B head 9f/89 tail
  bd/89 b5set {89} NO step, 0 ff) + cform 10/10 (C head
  bf/89 tail d1/89 b5set {89} NO step, 0 ff) + qform
  64/64 (Q head d3/89 tail 51/8a b5set {89,8a} step
  o22->23: 115967 o22 ff/89 -> 115968 o23 01/8a,
  quad formula == raw-lencode 64/64, exactly 1 ff in
  64); ring counter 256/256 + ringraw 256/256 (head
  53/8a; 116095 off86 ff/8a -> 116096 off87 01/8b; mid
  off128 53/8b; 116223 off214 ff/8b -> 116224 off215
  01/8c; tail off255 51/8c; exactly 2 ff in 256 at
  o86/o214); odd-lencode 348/348. Ring edges + tail
  116264 in for-list + 2 PASS lines each py+C. Tail
  116264: oracle sha eb239b51ba87fa53... matches PINS;
  py+C CLOSED T10P285R off=255 agree. No DISSENT: cut
  bytes verify.
- PB-diff secf393.py (cache path) + secf393b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (115917 +
  115569 + 115918 + 115570); S0: oracle115917-vs-115569
  34/84, codeS0-vs-P284S0 34/84, positions identical;
  DIRECT tool 34/84 with identical agree-pos 50
  positions. S1: oracle 55/84, code 55/84, positions
  identical; DIRECT 55/84 identical agree-pos 29
  positions. 0 miss (ownloop pre-warmed). Twice-derived
  both pairs. No byte-equal wording in A-709/A-349 this
  band (both stage NEW sigs, consistent with 34/55
  diffs) -- byte-diff discipline observed, nothing to
  refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 230
  content / 0 del. Normalized ([0-9]+ -> N recipe):
  py del-uniq 0 add-uniq 183 missing 0 == GATE EXACT.
  FLAG -- C add-uniq: GATE claims 166, first-hand
  re-derivation gives 169 under the stated recipe,
  thrice-derived (python set-norm 169; variant norms
  168 empty-excluding / 165 lstripped / 169 rstrip-semi;
  BSD shell cut/sed/sort-u 169 with blanks, 168
  without). 166 is unreachable under any natural
  variant. del-uniq 0 + del-subset-add 0 missing hold
  under EVERY variant (integrity property intact); raw
  counts match. GATE C add-uniq 166 is a GATE-side
  prose/count slip (same class as b389 loose-aa
  parenthetical), corrected here: 169. Code unaffected.
- Wall on band diff added lines (scope 4ea39e1c..
  9cac7b4f, 897 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (b82c0c66), code 6 blocks,
  tier-comments `# T10P` 1598->1604 +6, singletons
  602->604 +2 / ranges 592->596 +4, CLOSED T10P prints
  1598->1604 +6 py + 1598->1604 +6 C, C singleton
  `if ((n) == (` 597->599 +2 / C ranges 592->596 +4,
  seal 1692->1698 +6 (commit msgs): all agree, no slip.
  5-count C-vs-py singleton offset pre-existing +
  unchanged (gap 5 at base AND new under GATEPAT).
- CONFIRM evidence (CONVERT-01 rule b): A-709-q797-
  t10p285 verdict CONFIRM, tallies 13/13 + 11/11 + 12/12
  = 36/36 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 17 total vs 36, counting unit irreproducible;
  methodology note, NO verdict impact) + exact-value
  corroboration incl PBA88-PLAIN + b5 const, C10-1SIG,
  QUAD88-4R + R11 rows + tails + lcsuf + M-tails NEW,
  ring SWAPPED + TR7/TM7 16/16 UNPAIRED + edges +
  consts (all re-checked above) + A-349 viewer
  corroboration (CONFIRM all legs, consts 78/71/67/72
  INCL). No CONFIRM-P285.md file (absence verified);
  A-709 suffices per rule. Agrees with cport commit msg
  (PYID 8406, RGRAM 16812).
- Quiz: no conflicting CLAIM/GATE/FLAG on b393 (own seat
  CLAIM only). Newest PARENT-* is QNUM-21 (w2b block) +
  QNUM-20 (w2f block): pure Q-block grants, read, no gate
  impact -- GATE cites QNUM-19: 1 immaterial staleness
  (standing pattern). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS on code. No RED. GATE CORRECT on code +
all behavior legs; 2 immaterial GATE prose slips
(QNUM-19 vs -21 staleness; C add-uniq 166 vs 169
thrice-derived, corrected above; integrity property
del-subset-add 0 missing intact).
Next-P286 predictions banked for r56+ (A-709/A-349: PB0
1df80a00 / PB1 cd23fd15 == P285C10sig with 57/84
byte-diff noted / PBA88 01000000 x16 / C10 cd236d10).
