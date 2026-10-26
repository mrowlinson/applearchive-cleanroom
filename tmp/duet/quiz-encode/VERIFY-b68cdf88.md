# VERIFY-b68cdf88 b396 T10P288 pins 116961..117308 (1716 tiers) PASS

Seat viewer-r57, first-hand, tree-b68cdf88 @b68cdf88,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r57.
Base 62f9b99c (b395, 1710 tiers). Band = a36a36d3 (py merge
w2b@31527a73 partial, +6 tiers, +62 pins) + b68cdf88 (C port,
1716 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build396/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4f4c483dd34d1aa4 / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  5b3150bfafd18cf8 / aae 7d8dd3a2d118e0db.
- RGRAMC-PYID 8499/8499 covered=8499/8499 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16998/16998 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16998/16998 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 16998/16998).
- PINS 17000 rows (2 hdr + 16998, +62 vs base 16936);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  116961 116962 116963 116964 116970 116971 116977 116978
  116979 116980 116983 116984 116987 116988 116989 116991
  116992 117004 117005 117013 117021 117029 117037 117052
  117053 117119 117120 117181 117247 117248 117308
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 116981/116982/
  116985/116986 unsampled) + Q10 offs 0,2,3,15,16,24,32,
  40,48,63 (b5 step o2->o3 straddled: 116991+116992 both
  pinned) + R7 offs 0,66/67,128,194/195,255 (both counter
  edges straddled); 8468->8499); 31x2=62 rows, range
  116961..117308 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit396.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 138 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/1SIG/QUAD88-4R/STANDARD ring; no QT/RT/TT; no
  BM/BC, no M19/XA19, no QB/PT/FM, no M42/X42/H42/L42);
  C==py 12/12. S0/S1 168ch sigs 0ac51600 NEW / 3bf3942d
  NEW (full-string NEW vs BOTH P287 strings; S0-vs-P287S0
  32/84 @ b0-2,4-11,13,15-18,45-47,50,51,60-62,64-71
  EXACT + cross-P287S1 72, S1-vs-P287S1 75/84 EXACT,
  agree-pos exactly b69,72-79 + cross-P287S0 67). AM
  16x16ch distinct; AC 78, b0-3 02/00/00/00 (b0 const
  02), no b4/b5, PBA sig 02000000 x16 PLAIN. CM 10x24ch
  10/10 diverge (rows span 3 distinct 4B heads 3b8ab9f9/
  4b67f57e/b34c3b7e); CC 70, b0-3 3bf3942d full-sig in
  consts, no b4/b5 (C10-1SIG x10 SAME-as-PB1-sig). M
  16x12ch distinct. QR 4x24ch 4-distinct UNPAIRED; r0
  2b022ff935b1da25e032bd5c distinct; r123 share 8B
  abe8237f75320326, byte8 41/66/8b; tails b84-87
  e032bd5c/416e5b06/666e5b06/8b6e5b06 4/4 distinct;
  r123 TRUE 3B 6e5b06; tail-LCS (0,*)=0, (1,2)=(1,3)=
  (2,3)=3 AND tail-lcsuf identical 0/3/3/3 (both
  computed first-hand, agree). QC 68, b0-3 02000000,
  no b4/b5. RM 16x14ch distinct; RQ 16x12ch distinct;
  RC 73, b0-3 2f/00/00/00, b84-87 de/75/77/5e ring-wide.
  M==RQ EXACT 16/16 (lists identical). RM-vs-RQ UNPAIRED
  (sets disjoint). Tails STANDARD-SPLIT (RM b80-83 by
  COL, RQ b76-79 by ROW, 16/16 distinct each, 0 overlap).
  Sorted-unique + _N decls 78/70/68/73 match actual.
  Missing-sets EXACT: AC [4,5,25,26,27,35,80,81,82,83];
  CC [4,5,22,23,30,31,32,33,34,35,80,81,82,83]; QC [4,5,
  26,27,34,35,36,37,38,39,40,41,80,81,82,83,84,85,86,
  87]; RC [4,5,39,40,41,46,47,76,77,78,79,80,81,82,83].
  Coverage unions exact every block (const U tab U {b4,
  b5} == 88/84/88/88, 0 overlap). Q legs M[m] + QR[q],
  no frags. R legs RM[c] + RQ[r] STANDARD. AC-QC
  shared-pos 67, same-val 29, AConly 11, QConly 1 (==
  GATE, computed first-hand; NOT const-repeat). C-mtab
  M12 b22,23,30-35,80-83 parsed from code text vs P287
  M11 b13-19,80-83 parsed from base code (geometry
  change code-verified). P287 refs re-read: S0 85620b00
  / S1 4c0ac516 / PBA 01000000 / C10 86148a2d / QUAD
  02000000 (== P287 preds EXACT). P288 preds (A-713/
  A-351 Next-P288: 0ac51600/3bf3942d/02000000/3bf3942d)
  x4 corroborated staged. PBA NEW vs P287 (02000000 vs
  01000000). C10 NEW vs P287 (3bf3942d vs 86148a2d).
  QUAD sig REPEAT vs P287 (02000000 == 02000000), rows
  NEW (R12 24ch vs P287 R11 22ch, 0-overlap). QR
  0-overlap vs P287QR. AM/CM/M/QR/RM/RQ 0-overlap vs
  P287 (widths differ M 12ch vs 18ch, AM 16ch vs 20ch,
  CM 24ch vs 22ch, RM 14ch vs 16ch, RQ 12ch vs 16ch, QR
  24ch vs 22ch, base widths re-read first-hand).
  M-tails 16/16 ALL NEW vs P287 M-tail8 + P287 RM-tail8
  + P287 RQ-tail8 (overlap 0 x3). Memo INCL PBA88 79 /
  C10 71 / quad88 68 / T88 73 (A-727 re-read): impl
  78/70/68/73 = memo-1 on PBA/C10 (b5-const excluded),
  identical quad/T88. Base temp maxes _t6027/_b3651/
  _i3652 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 116961 / S1 116962 / A 116963-978 / C 116979-988 /
  Q 116989-117052 / R 117053-117308): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-consts emerge from raw lencode) + Q b5
  step 0x91+(o>=3) edge o2->o3 + R counter b4=
  (0x7b+2off)&FF b5=0x92+(off>=67)+(off>=195) (py hex;
  C stages decimal 123/146/67/195, re-derived from
  code text both sides) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions exact
  (A 8B b25-27,35,80-83; C 12B b22,23,30-35,80-83; Q
  QM6 b40,41,80-83 + R12 b26,27,34-39,84-87; R TM7
  b39,46,47,80-83 by COL + TR6 b40,41,76-79 by ROW) +
  NO frag leg in Q. T-mirrors T78282/78287/78292/78307/
  78323/78344 each re-read: hits the exact py guard
  line. C guards `if ((n) == (116961))` / `(116962)` +
  4 range guards exact. C byte-index lists match py per
  block (A 8B, C 12B, Q 6B/12B, R 7/6B). Temps
  _t6028-6043 continuous (base max _t6027) + _b3653/
  3655/3657/3658/3660/3661 (base max _b3651) + _i3654/
  3656/3659/3662 (base max _i3652): added-lines-only
  refs (base tree zero refs to new temps) prove no
  reuse. Insert exact both sides: after T10P287R close,
  at dispatch tail (N-out-of-scope fallthrough follows;
  C 2 scope hits, py 2 scope hits). Matches A-727/A-352
  geometry (values re-checked in audit above; NO D dips:
  ownloop tags exactly the 6 P288 blocks).
- Edges own-loop ownloop396.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P288R N=117308 off=255.
  edges396.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 c3/91, c5/91 == raw lencode) +
  aform 16/16 (A 88B head c7/91 tail e5/91 b5set {91} NO
  step, 0 ff) + cform 10/10 (C head e7/91 tail f9/91
  b5set {91} NO step, 0 ff) + qform 64/64 + qb5step 64/
  64 (Q head fb/91 tail 79/92 b5set {91,92} step o2->o3:
  116991 o2 ff/91 -> 116992 o3 01/92, exactly 1 ff in
  64 at o2; quad b4 formula == raw-lencode 64/64); ring
  counter 256/256 + ringraw 256/256 (head 7b/92; 117119
  off66 ff/92 -> 117120 off67 01/93; mid off128 7b/93;
  117247 off194 ff/93 -> 117248 off195 01/94; tail
  off255 79/94; exactly 2 ff in 256 at o66/o194);
  odd-lencode 348/348. Ring edges + tail 117308 in
  for-list + 2 PASS lines each py+C. Tail 117308:
  oracle sha 77370beccc2f8f14... matches PINS; py+C
  CLOSED T10P288R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf396.py (cache path) + secf396b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (116961 +
  116613 + 116962 + 116614); S0: oracle116961-vs-116613
  32/84, codeS0-vs-P287S0 32/84, positions identical;
  DIRECT tool 32/84 with identical agree-pos 52
  positions. S1: oracle 75/84, code 75/84, positions
  identical; DIRECT 75/84 identical agree-pos 9
  positions (b69,72-79 == tabaudit). 0 miss (ownloop
  pre-warmed). Twice-derived both pairs. C10-head
  n116979 vs S1: 47/84 differ, sig-eq 3bf3942d ==
  3bf3942d (py-comment + A-727 figure re-derived exact
  first-hand). No byte-equal wording in A-727/A-352 this
  band (both stage NEW sigs + explicit NOT-byte-equal
  on the sig-eq pair, consistent with 32/75/47 diffs)
  -- byte-diff discipline observed, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 231/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 231
  content / 0 del. Fine-norm (temp-norm, empty-
  excluding): del-uniq 0 add-uniq 409 missing 0 ==
  GATE EXACT (first-hand, no reconstruction needed;
  this GATE states the temp-norm recipe explicitly).
  del-subset-add 0 missing holds (integrity intact).
- Wall on band diff added lines (scope 62f9b99c..
  b68cdf88, 898 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (a36a36d3), code 6 blocks,
  tier-comments `# T10P` 1616->1622 +6, py top-level
  singletons (^4sp `if n == `) 598->600 +2 == GATE
  stated-method EXACT (recipe: top-level dispatch
  guards only; 5 nested 8sp guards excluded both
  trees), py T10P range guards 582->586 +4 == GATE
  EXACT, CLOSED T10P prints 1616->1622 +6 py + 1616->
  1622 +6 C, C singleton `if ((n) == (` 603->605 +2 ==
  GATE EXACT / C ranges 604->608 +4 == GATE EXACT,
  seal 1710->1716 +6 (commit msgs): all agree, no slip.
  C-vs-py-GATE +5 offset pre-existing + unchanged
  (nested guards counted in C total both trees).
- CONFIRM evidence (CONVERT-01 rule b): A-727-q880-
  t10p288 verdict CONFIRM, tallies 15/15 + 11/11 + 12/12
  = 38/38 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 18 total vs 38, counting unit irreproducible;
  methodology note, NO verdict impact) + exact-value
  corroboration incl PB0 NEW + PB1 NEW + sig-eq own-C10
  + 47/84 diff, PBA88-PLAIN, C10-1SIG, QUAD88-4R + R12
  rows + 8B-share + TRUE-3B + b5 step + edge + M-tails
  NEW, ring STANDARD + TR6/TM6 16/16 UNPAIRED + edges +
  consts (all re-checked above) + A-352 viewer
  corroboration (CONFIRM all legs, consts 79/71/68/73
  INCL). No CONFIRM-P288.md file (absence verified);
  A-727 suffices per rule. Agrees with cport commit msg
  (PYID 8499, RGRAM 16998).
- Quiz: no conflicting CLAIM/GATE/FLAG on b396 (own seat
  CLAIM only). Newest PARENT-QNUM-22 (w2e Q-block grant,
  read, no gate impact) -- GATE cites no QNUM (no
  staleness). PROSE-01: all hex/counts above copied from
  own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 0 prose slips (norm recipe stated explicitly this
band, temp-norm 409 reproduced EXACT with no variant
gap; py-tier recipe reproduced EXACT via top-level-
guard reading).
Next-P289 predictions banked for r58 (A-727/A-352: PB0
@117309 0fc51600 NEW / PB1 3bf3f420 NEW / PBA88 02000000
x16 / C10-2SIG 3bf3f420 x7 @117327-33 + 3bf3f41a x3
@117334-36 ORDERED 7+3 window-resolved).
