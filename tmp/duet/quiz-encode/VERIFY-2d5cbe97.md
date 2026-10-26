# VERIFY-2d5cbe97 b391 T10P283 pins 115221..115568 (1686 tiers) PASS

Seat viewer-r55, first-hand, tree-2d5cbe97 @2d5cbe97,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r55.
Base 256db28a (b390, 1680 tiers). Band = b67f7800 (py merge
w2b@cfefa1d0 partial, +6 tiers, +66 pins) + 2d5cbe97 (C port,
1686 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build391/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc d7c5de50e071c326 / aae
  7d8dd3a2d118e0db + sha256 rgramc 09d8ce9d8167b0e / aae
  d6e27c97ced21673 (== GATE all 4; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 8344/8344 covered=8344/8344 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16688/16688 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16688/16688 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16688/16688 sorted).
- PINS 16690 rows (2 hdr + 16688, +66 vs base 16624);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +33/-0:
  115221 115222 115223 115224 115228 115233 115237 115238
  115239 115240 115243 115244 115245 115246 115247 115248
  115249 115256 115264 115265 115280 115281 115288 115296
  115297 115312 115313 115327 115328 115392 115455 115456
  115568
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,5,10,14,15 +
  C8 offs 0,1,4,5,6,7,8,9 (offs 2,3 = 115241/242
  unsampled; sig-boundary dense: sig1 head pair 0,1 +
  sig1 tail pair 4,5 + full sig2 6,7,8,9) + Q10 offs 0,7,
  15/16,31/32,39,47/48,63 (b5 const, NO step) + R7 offs
  0,14/15,79,142/143,255; 8311->8344); 33x2=66 rows,
  range 115221..115568 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit391.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 131 PASS
  0 FAIL. Inventory exactly the 15 both sides (STANDARD
  ring + H42/L42 nib-tabs, no RT/TT; no BM/BC, no M19,
  no QB/PT/FM, no M42/X42, no R8/X8); C==py 15/15. S0/S1
  168ch sigs 9ef00700 NEW / 4513e30f NEW (full-string NEW
  vs BOTH P282 strings; S0-vs-P282S0 30/84 @ b4-7,9-11,
  13-18,20,22-25,64-75 EXACT + S1-vs-P282S1 48/84 @ b0-2,
  4,5,11,13,15-39,52-55,68-75,80-83 EXACT; cross S0-
  P282S1 34 + S1-P282S0 62). AM 16x14ch distinct; AC 75,
  b0-3 c0/9b/7f/e2 (b0 const c0), no b4/b5, PBA sig
  c09b7fe2 x16. CM 10x32ch 10/10 diverge; map bytes
  ORDERED e30f x6 + f307 x4; CC 66, b0,b1 = 45,13, full
  2SIG map 4513e30f x6 + 4513f307 x4 (ORDERED 6+4);
  partial sig b2,3 in tab (no CC b2/b3 consts), no b4/b5.
  M 16x12ch distinct. H42 16x1ch coltab 733f373777bff773
  EXACT (4-distinct); L42 [5,9,9,9] EXACT (r0->5,
  r123->9). QR r0 285f5f3c51e4 distinct (last3 3c51e4),
  r1==r2==r3 9d592674f113 LAST3-PAIRED (last3 74f113), 2
  distinct. QT 1ebc3c63/9a7d1825/bf7d1825/e47d1825 4/4
  distinct; r1/r2/r3 share last 3B 7d1825 (first bytes
  9a/bf/e4 differ); r0 last3 bc3c63 does not. QC 65,
  b0-3 c09b7f62 (QUAD1s single-sig x64); b42 in tab (no
  QC b42 const), no b4/b5. QC-sig vs PBA-sig share b0-2
  (c0,9b,7f), b3 differs 62-vs-e2 (viewer observation,
  first-hand). RM 16x12ch distinct; RQ 16x14ch 16/16
  distinct; RC 73, b0-3 07/00/00/00, b84-87 a8/fd/2c/45
  ring-wide. Sorted-unique + _N decls 75/66/65/73 match
  actual. Missing-sets EXACT: AC [4,5,36,37,38,76,77,78,
  79]; CC [2,3,4,5,34,35,36,37,38,39,40,41,42,43,80,81,
  82,83]; QC [4,5,34,36,37,38,39,40,41,42,43,76,77,78,79,
  80,81,82,83]; RC [4,5,38,46,47,52,53,76,77,78,79,80,81,
  82,83]. Coverage unions exact every block (const U tab
  U {b4,b5} == 84/84/84/88, 0 overlap). Q legs M[m] +
  H42[m] + L42[q] + QR[q] + QT[q] + NIBSPLIT (pay[42]>>4
  / pay[42]&0xF both sides), no frags. R legs RM[c] +
  RQ[r] STANDARD. RQ==M HEAD0+SHIFT FIRST (M 6B vs RQ
  7B: RQ[0]==M[0] 16/16 + RQ[2:7]==M[1:6] 16/16; 7x6
  agree matrix clean shift -- diagonal (0,0),(2,1),(3,2),
  (4,3),(5,4),(6,5) all 16, all other 36 cells <=1 with
  max 1 at (1,5); RQ[1] own: 4-distinct 3c/7c/bc/fc
  counts 5/7/1/3, lo-6 bits const 3c 16/16). RM-vs-RQ
  UNPAIRED (full-row sets disjoint; RM-tail4/RQ-tail4 16
  distinct each, SPLIT-disjoint). QT byte-LCS all-pairs:
  (1,2)=(1,3)=(2,3)=3, r0-vs-rest 0 (memo values exact).
  P282 refs re-read: S0 9ef00700 / S1 cb3de10f / PBA
  e0857ffe / C10-map 3582e40f x6 + 4dffe70f + 8d59ea0f +
  ad85e10f x2 (== A-692/A-345 preds EXACT). P283 preds
  (A-696/A-346 Next-P283) x4 corroborated (9ef00700/
  4513e30f/c09b7fe2/6+4 map == staged). M-tails 16/16 ALL
  NEW vs P282M-tail8 + P282RM-tail8 + P282RQ-tail8 (0
  overlap x3). QT 4/4 ALL NEW vs P282QT; RM ALL NEW vs
  P282RM. Memo INCL PBA 76 / C10 67 / quad 66 / T88 73
  (A-699 re-read): impl 75/66/65/73 = memo-1 on PBA/C10/
  quad (b5-const excluded), identical T88. Base temp
  maxes _t5941/_b3600/_i3601 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 115221 / S1 115222 / A 115223-238 / C 115239-248 /
  Q 115249-312 / R 115313-568): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (A/C/Q; b5-consts emerge from raw lencode) + R
  counter b4=(0xE3+2off)&FF b5=0x84+(off>=15)+(off>=143)
  (py hex; C stages decimal 227/132/15/143, re-derived
  from code text both sides) + m=off&15/q=off>>4/c=off&
  15/r=off>>4 both sides + mtab/qtab/ttab byte positions
  exact (A 7B b36-38,76-79; C 16B b2,3,34-43,80-83; Q
  6B QM6 b34,43,76-79 + b42 NIBSPLIT hi==H42[m]/lo==L42
  [q] (py "%x" idiom, C snprintf %lx idiom) + 6B R6 b36-
  41 + 4B T4 b80-83; R 6B TM6 b52,53,80-83 by COL + 7B
  TR7 b38,46,47,76-79 by ROW) + NO frag leg in Q. T-
  mirrors T77124/77129/77134/77149/77166/77193 each re-
  read: hits the exact py guard line. C guards `if ((n)
  == (115221))` / `(115222)` + 4 range guards exact.
  Temps _t5942-5963 continuous (base max _t5941) +
  _b3602/3604/3606/3607/3608/3610/3611 (base max _b3600)
  + _i3603/3605/3609/3612 (base max _i3601): added-lines-
  only refs prove no reuse. C byte-index lists match py
  per block (A 7B, C 16B, Q 6B+2nib/6B/4B, R 6/7B).
  Insert exact both sides: after T10P282R close (C
  206124), at dispatch tail (N-out-of-scope follows; C 2
  scope hits, py 2 scope hits). Matches A-699/A-347
  geometry (values re-checked in audit above; NO D dips:
  ownloop tags exactly the 6 P283 blocks).
- Edges own-loop ownloop391.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (315 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P283R N=115568 off=255.
  edges391.py: paylens 92 x84 + 256 x88; lencode 92/92
  (S0/S1 2b/84 + 2d/84 == raw lencode 0x842B/0x842D) +
  aform 16/16 (A head 2f/84 tail 4d/84 b5set {84} NO
  carry) + cform 10/10 (C head 4f/84 tail 61/84 b5set
  {84} NO carry) + qform 64/64 (Q head 63/84 tail e1/84
  b5set {84} NO step NO edge); ring counter 256/256 +
  ringraw 256/256 (head e3/84; 115327 off14 ff/84 ->
  115328 off15 01/85; mid 115392 off79 81/85; 115455
  off142 ff/85 -> 115456 off143 01/86; tail off255 e1/
  86; exactly 2 ff in 256 at o14/o142); odd-b4 348/348
  by formula construction (all 5 formulas odd-base + 2
  off, all conformance checks green). Ring edges + tail
  115568 in for-list + 2 PASS lines each py+C. Tail
  115568: oracle sha 996f684d281c44ad... matches PINS; py
  PASS + C CLOSED T10P283R off=255 agree. No DISSENT:
  cut bytes verify.
- PB0-diff secf391.py (cache path) + secf391b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0 (115221 + 114873);
  oracle115221-vs-114873 30/84; codeS0-vs-P282S0 30/84;
  diff positions identical code-vs-oracle; DIRECT tool
  30/84 with identical agree-pos 54 positions (0-3,8,12,
  19,21,26-63,76-83) both paths. 0 miss (ownloop pre-
  warmed). A-347 leg-1 "(byte-equal first-hand)" wording
  REFUTED first-hand, twice-derived (cache path + direct-
  tool path, identical agree positions): 30/84 differ.
  A-699 (30/84) + GATE CONFIRMED. Record corrected here
  (r54/A-342 precedent: correction lives in the VERIFY
  record; 3rd memo wording refutation: A-342/A-345/A-347).
  A-347 legs 2-3 + consts stand.
- b42 3-way tie b42tie391.py over ALL 64 Q oracle
  payloads (code H42/L42 first-hand): NIBSPLIT hi==H42[m]
  + lo==L42[q] 64/64; row-XOR X=[00,0c,0c,0c] 64/64;
  row-ADD A=[0,4,4,4] 64/64 (base = r0-form colbyte
  (H42[m]<<4)|5, stated formulation); bad []. Tie
  corroborated first-hand (10th b42-tie family member);
  code implements NIBSPLIT both sides (eye-verified
  above; py Q-comment cites the tie).
- C diff pure-add: numstat 647/0 (rgramc.c) + 266/0
  (rgram.py) + 1/1 (for-line) + 66/0 (PINS) == GATE;
  raw C 642 content + 5 bare-blank / 0 del; raw py 266
  content / 0 del. Normalized sweep (same recipe as
  GATE): C del-uniq 0 add-uniq 180, py del-uniq 0
  add-uniq 199, 0 missing == GATE EXACT.
- Wall on band diff added lines (scope 256db28a..
  2d5cbe97, 980 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 647/0, rgram.py 266/0 purely
  additive, test_rgram.sh 1/1, PINS +66/+0.
- Tiers: merge-msg +6/+66 (b67f7800), code 6 blocks,
  tier-comments `# T10P` 1586->1592 +6, singletons 598->
  600 +2 / ranges 584->588 +4 (stated literal methods),
  CLOSED T10P prints 1586->1592 +6 py + 1586->1592 +6 C,
  C singleton `if ((n) == (` 593->595 +2 (GATE pattern
  REPRODUCED EXACT) / C ranges 584->588 +4, seal 1680->
  1686 +6 (commit msgs): all agree, no slip. 5-count
  C-vs-py singleton offset pre-existing + unchanged (gap
  5 at base AND new under GATEPAT; my b388-pattern `(n)
  == (` gives 598->600 == py absolute -- methodology
  note, deltas +2 agree every pattern).
- CONFIRM evidence (CONVERT-01 rule b): A-699-q795-
  t10p283 verdict CONFIRM, tallies 13/13 + 14/14 + 12/12
  = 39/39 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 8/6/4, counting unit irreproducible; methodology
  note, NO verdict impact) + exact-value corroboration
  incl PBA/C10-2SIG 6+4 map, QUAD1s + b42 NIBSPLIT + R6
  last3-pair + QT tails r123-3B + b5 const, M-tails NEW,
  ring STANDARD + TR7 16/16 UNPAIRED + edges + consts
  (all re-checked above) + A-347 viewer corroboration
  (legs 2-3 CONFIRM, consts 76/67/66/73 INCL; leg-1 byte-
  equal wording REFUTED per secf above, all other leg-1
  values CONFIRM). No CONFIRM-P283.md file (absence
  verified); A-699 suffices per rule. Agrees with cport
  commit msg (PYID 8344, RGRAM 16688).
- Quiz: no conflicting CLAIM/GATE/FLAG on b391 (own seat
  CLAIM only). Newest PARENT-* is QNUM-21 (w2b block) +
  QNUM-20 (w2f block): pure Q-block grants, read, no gate
  impact -- GATE cites QNUM-19: 1 immaterial staleness x2
  (standing pattern). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + prose (1
immaterial QNUM staleness, QNUM-19 vs -21).
FLAG for parent/memo (code PASS): A-347 leg-1 byte-equal
wording refuted + corrected above (3rd memo wording
refutation this project: A-342/A-345/A-347 -- pattern:
viewer-r8 leg-1 "byte-equal" claims vs memo-r3 measured
diffs; suggest memo-side byte-diff discipline).
