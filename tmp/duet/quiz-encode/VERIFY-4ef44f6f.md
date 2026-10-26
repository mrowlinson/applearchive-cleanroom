# VERIFY-4ef44f6f b389 T10P281 pins 114525..114872 (1674 tiers) PASS

Seat viewer-r55, first-hand, tree-4ef44f6f @4ef44f6f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r55.
Base 55198ed2 (b388, 1668 tiers). Band = 97be8410 (py merge
w2b@396f58dc partial, +6 tiers, +64 pins) + 4ef44f6f (C port,
1674 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build389/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 14fe509ba339d103 / aae
  7d8dd3a2d118e0db + sha256 rgramc 6b0f4be92d63f776 /
  aae d6e27c97ced21673 (== GATE all 4; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 8279/8279 covered=8279/8279 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16558/16558 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16558/16558 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16558/16558 sorted).
- PINS 16560 rows (2 hdr + 16558, +64 vs base 16496);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +32/-0:
  114525 114526 114527 114528 114532 114537 114541 114542
  114543 114544 114548 114549 114550 114551 114552 114553
  114559 114560 114568 114569 114584 114585 114600 114601
  114616 114617 114687 114688 114752 114815 114816 114872
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,5,10,14,15 +
  C7 offs 0,1,5,6,7,8,9 (offs 2,3,4 = 114545/46/47
  unsampled) + Q10 offs 0,6/7,15/16,31/32,47/48,63 + R7
  offs 0,70/71,135,198/199,255; 8247->8279); 32x2=64
  rows, range 114525..114872 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit389.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 126 PASS
  0 FAIL. Inventory exactly the 13 both sides (STANDARD
  ring, no RT/TT; no BM/BC, no M19, no QB/PT/FM, no
  M42/X42, no R8/X8); C==py 13/13. S0/S1 168ch sigs
  5eae0700 NEW / 2557520f NEW (full-string NEW vs BOTH
  P280 strings; S0-vs-P280S0 33/84 @ b0,4,5,11,18-24,
  26-29,32-37,52-55,72-79 EXACT + S1-vs-P280S1 47/84 @
  b4,5,22-40,42-55,72-83 EXACT; cross S0-P280S1 59 +
  S1-P280S0 71). AM 16x12ch distinct; AC 76, b0-3 c0/94/
  17/fb (b0 const c0), no b4/b5, PBA sig c09417fb x16.
  CM 10x24ch 10/10 diverge; rows 0-5 share 8B head
  520f769791c36744 + distinct 4B tails d037d006/f037d006/
  bff7820e/f8fc2833/41762933/80762933; map bytes ORDERED
  520f x6 + e20c + f20b + 920c x2; CC 70, b0,b1 = 25,57,
  full C10 map 2557520f x6 + 2557e20c + 2557f20b +
  2557920c x2 (FIRST 6+1+1+2, ORDERED); sig bytes b2,3
  in tab (no CC b2/b3 consts), no b4/b5. M 16x16ch
  distinct. QR r0 ceb6f8d1f53ff9 distinct (last3 f53ff9),
  r1==r2==r3 d4052931b9cf38 LAST3-PAIRED (last3 b9cf38),
  2 distinct; b0 row-split ce/d4/d4/d4. QT e86c5231/
  4134a70c/53ecad0c/78ecad0c 4/4 distinct; r2/r3 share
  last 3B ecad0c (first bytes 53/78 differ); r0/r1 last3
  6c5231/34a70c do not. QC 63, b0-2 5d/72/25, QUAD2s sigs
  5d7225ce x16 (row0) + 5d7225d4 x48 (rows1-3); b3-led
  (no QC b3 const), no b4/b5. RM 16x16ch distinct; RQ
  16x16ch 16/16 distinct; RC 70, b0-3 0c/00/00/00,
  b84-87 af/7c/ec/bc ring-wide. Sorted-unique + _N decls
  76/70/63/70 match actual. Missing-sets EXACT: AC [4,5,
  48,49,76,77,78,79]; CC [2,3,4,5,46,47,48,49,50,51,80,
  81,82,83]; QC [3,4,5,6,7,9,10,46,47,48,49,50,51,76,77,
  78,79,80,81,82,83]; RC [4,5,6,7,9,10,11,12,13,20,76,77,
  78,79,80,81,82,83]. Coverage unions exact every block
  (const U tab U {b4,b5} == 84/84/84/88, 0 overlap).
  Q legs M[m] + QR[q] + QT[q], no frags. R legs RM[c] +
  RQ[r] STANDARD. RQ==M PREFIX2+SUFFIX4 (prefix 16/16 +
  suffix 16/16, agree vector [16,16,0,0,16,16,16,16]
  EXACT; off-diagonal confusion max 1 at (0,3)/(5,6)/
  (6,5) -- GATE's "off-diagonal <=1/16" unit identified
  as same-row cross-position confusion (/16 rows) and
  CONFIRMED; mid all-differ 16/16; 1:1 remap 0067->0538
  / ed66->6d37 / ee66->7537 verbatim; byte-matrix max-
  offdiag 2 at (7,8)/(8,7) recorded -- my first reading
  was the wrong unit, methodology note). RM-vs-RQ
  UNPAIRED (full-row sets disjoint; RM-tail4/RQ-tail4 16
  distinct each, SPLIT-disjoint). QT byte-LCS all-pairs:
  (2,3)=3, (1,2)=(1,3)=1 (trailing 0c), rest 0 (memo
  values exact). P280 refs re-read: S0 58ae0700 / S1
  2557520f / PBA c09417fb / C10 2557520f (== A-690/A-343
  preds EXACT). P281 preds (A-691/A-344 Next-P281) x4
  corroborated (5eae0700/2557520f/c09417fb/6+1+1+2 map
  == staged). M-tails 16/16 ALL NEW vs P280M-tail8 +
  P280RM-tail8 + P280RQ-tail8 (0 overlap x3 -- covers
  every reading of "P280T reference"). QT 4/4 ALL NEW vs
  P280QT; RM ALL NEW vs P280RM. Memo INCL PBA 77 / C10
  71 / quad 63 / T88 70 (A-692 re-read): impl 76/70/63/
  70 = memo-1 on PBA/C10 (b5-const excluded), identical
  quad/T88. Base temp maxes _t5905/_b3578/_i3579.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 114525 / S1 114526 / A 114527-542 / C 114543-552 /
  Q 114553-616 / R 114617-872): bounds + paylens (92
  x84 / 256 x88) + S full-payload const (py hex-compare,
  C hex_of+strcpy+strcmp) + lencode l16=((n<<1)|1)&FFFF
  both sides (A/C/Q; b5-const/step emerge from raw
  lencode) + R counter b4=(0x73+2off)&FF b5=0x7F+(off>=
  71)+(off>=199) (py hex; C stages decimal 115/127/71/
  199, re-derived from code text both sides) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides + mtab/qtab/ttab
  byte positions exact (A 6B b48,49,76-79; C 12B b2,3,
  46-51,80-83; Q 8/7/4B QM8 b6,7,9,10,76-79 + b3-led R7
  b3,46-51 + T4 b80-83; R 8B TM8 b9-11,20,80-83 by COL +
  8B TR8 b6,7,12,13,76-79 by ROW) + NO frag leg in Q.
  T-mirrors T76626/76631/76636/76651/76667/76690 each
  re-read: hits the exact py guard line. C guards `if
  ((n) == (114525))` / `(114526)` + 4 range guards exact.
  Temps _t5906-5923 continuous (base max _t5905) + _b3580/
  3582/3584/3585/3586/3588/3589 (base max _b3578) +
  _i3581/3583/3587/3590 (base max _i3579): added-lines-
  only refs prove no reuse. C byte-index lists match py
  per block (A 6B, C 12B, Q 8/7/4B, R 8/8B). Insert exact
  both sides: after T10P280R close, at dispatch tail
  (N-out-of-scope follows; C 2 scope hits, py 2 scope
  hits). Matches A-692/A-345 geometry (values re-checked
  in audit above; NO D dips: ownloop tags exactly the 6
  P281 blocks).
- Edges own-loop ownloop389.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (316 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P281R N=114872 off=255.
  edges389.py: paylens 92 x84 + 256 x88; lencode 92/92
  (S0/S1 bb/7e + bd/7e == raw lencode 0x7EBB/0x7EBD) +
  aform 16/16 (A head bf/7e tail dd/7e b5set {7e} NO
  carry) + cform 10/10 (C head df/7e tail f1/7e b5set
  {7e} NO carry) + qform 64/64 (Q head f3/7e, step off6/7
  114559 ff/7e -> 114560 01/7f MID-ROW0, tail 71/7f,
  b5set {7e,7f}); ring counter 256/256 + ringraw 256/256
  (head 73/7f; 114687 off70 ff/7f -> 114688 off71 01/80;
  mid 114752 off135 81/80; 114815 off198 ff/80 ->
  114816 off199 01/81; tail off255 71/81); exactly 3 ff
  in tier (114559/114687/114815); odd-b4 348/348 by
  formula construction (all 5 formulas odd-base + 2off,
  all conformance checks green). Ring edges + tail 114872
  in for-list + 2 PASS lines each py+C. Tail 114872:
  oracle sha 5d9af54748cdbb2d... matches PINS; py PASS +
  C CLOSED T10P281R off=255 agree. No DISSENT: cut bytes
  verify.
- PB1-diff secf389.py (cache path) + secf389b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0 (114526 + 114178);
  oracle114526-vs-114178 47/84; codeS1-vs-P280S1 47/84;
  diff positions identical code-vs-oracle; DIRECT tool
  47/84 with identical agree-pos 37 positions (0-3,6-21,
  41,56-71) both paths. 0 miss (ownloop pre-warmed).
  A-345 leg-1 "(byte-equal to n114178 first-hand)" wording
  REFUTED first-hand, twice-derived (cache path + direct-
  tool path, identical agree positions): 47/84 differ.
  A-692 (47/84) + GATE CONFIRMED. Record corrected here
  (r54/A-342 precedent: correction lives in the VERIFY
  record). A-345 legs 2-3 + consts stand.
- C diff pure-add: numstat 610/0 (rgramc.c) + 237/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE;
  raw C 605 content + 5 bare-blank / 0 del; raw py 237
  content / 0 del. Normalized sweep (same recipe as
  GATE): C del-uniq 0 add-uniq 169, py del-uniq 0
  add-uniq 191, 0 missing == GATE EXACT.
- Wall on band diff added lines (scope 55198ed2..
  4ef44f6f, 912 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Loose-`aa`: my first-hand count 11 lines / 12
  occurrences, ALL benign hex (4 S-string lines py+C +
  7 PINS sha rows: g-z114525/26/37/48/600/752/872) --
  GATE's parenthetical "4" irreproducible under bare-`aa`
  (immaterial prose-count note; strict-0 verdict AGREED,
  wall clean either way). Files: rgramc.c 610/0,
  rgram.py 237/0 purely additive, test_rgram.sh 1/1,
  PINS +64/+0.
- Tiers: merge-msg +6/+64 (97be8410), code 6 blocks,
  tier-comments `# T10P` 1574->1580 +6, singletons 594->
  596 +2 / ranges 576->580 +4 (stated literal methods),
  CLOSED T10P prints 1574->1580 +6 py + 1574->1580 +6 C,
  C singleton `if ((n) == (` 589->591 +2 (GATE pattern
  REPRODUCED EXACT) / C ranges 576->580 +4, seal 1668->
  1674 +6 (commit msgs): all agree, no slip. 5-count
  C-vs-py singleton offset pre-existing + unchanged (gap
  5 at base AND new under GATEPAT; my b388-pattern `(n)
  == (` gives 594->596 == py absolute -- methodology
  note, deltas +2 agree every pattern).
- CONFIRM evidence (CONVERT-01 rule b): A-692-q793-
  t10p281 verdict CONFIRM, tallies 13/13 + 13/13 + 11/11
  = 37/37 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 8/5/4, counting unit irreproducible; methodology
  note, NO verdict impact) + exact-value corroboration
  incl PBA/C10-4SIG map, QUAD2s row-split + b3-led R7
  last3-pair + QT tails + LCS + b5 step, M-tails NEW,
  ring STANDARD + TR8 16/16 UNPAIRED + edges + consts,
  PB1-diff 47/84 (all re-checked above) + A-345 viewer
  corroboration (legs 2-3 CONFIRM, consts 77/71/63/70
  INCL; leg-1 byte-equal wording REFUTED per secf above,
  all other leg-1 values CONFIRM). No CONFIRM-P281.md
  file (absence verified); A-692 suffices per rule. Agrees
  with cport commit msg (PYID 8279, RGRAM 16558).
- Quiz: no conflicting CLAIM/GATE/FLAG on b389 (own seat
  CLAIM only). Newest PARENT-* is QNUM-21 (w2b block) +
  QNUM-20 (w2f block): pure Q-block grants, read, no gate
  impact -- GATE cites QNUM-19: 1 immaterial staleness x2
  (standing pattern). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + prose (2
immaterial notes: QNUM staleness QNUM-19 vs -21; loose-aa
parenthetical count 4 vs my 11/12 benign-hex).
FLAGS for parent/memo (code PASS throughout): (1) A-345
leg-1 byte-equal wording refuted + corrected above;
(2) RQ==M numbering: GATE calls this "12th odd-band"
instance -- viewer notes b388 RQ==M EXACT (VERIFY-
55198ed2, filed this round) sits between b387's 11th and
this; numbering reconciliation for parent/memo, NOT a
code issue.
