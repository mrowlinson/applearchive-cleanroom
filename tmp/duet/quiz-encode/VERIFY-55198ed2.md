# VERIFY-55198ed2 b388 T10P280 pins 114177..114524 (1668 tiers) PASS

Seat viewer-r55, first-hand, tree-55198ed2 @55198ed2,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r55.
Base 69eaa7e9 (b387, 1662 tiers). Band = 919acc47 (py merge
w2b@f8e5da44 partial, +6 tiers, +58 pins) + 55198ed2 (C port,
1668 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build388/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc e04827b7d91d6f9c /
  aae d6e27c97ced21673 (== GATE both) + sha1 rgramc
  b75b3e13131ce9110 / aae 7d8dd3a2d118e0db (aae pinned,
  band touches no aae sources per numstat).
- RGRAMC-PYID 8247/8247 covered=8247/8247 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16494/16494 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16494/16494 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16494/16494 sorted).
- PINS 16496 rows (2 hdr + 16494, +58 vs base 16438);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +29/-0:
  114177 114178 114179 114180 114184 114189 114193 114194
  114195 114196 114198 114201 114203 114204 114205 114220
  114221 114236 114237 114252 114253 114268 114269 114303
  114304 114368 114431 114432 114524
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,5,10,14,15 +
  C6 offs 0,1,3,6,8,9 (offs 2,4,5,7 unsampled) + Q8 offs 0,
  15/16,31/32,47/48,63 + R7 offs 0,34/35,99,162/163,255;
  8218->8247); 29x2=58 rows, range 114177..114524 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit388.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 127 PASS
  0 FAIL. Inventory exactly the 13 both sides (STANDARD
  ring, no RT/TT; no BM/BC, no M19, no QB/PT/FM, no
  M42/X42, no R8/X8); C==py 13/13. S0/S1 168ch sigs
  58ae0700 NEW / 2557520f NEW (full-string NEW vs BOTH
  P279 strings; diffs S0 31/72 + S1 66/74 EXACT). AM
  16x18ch distinct; AC 73, b0-3 c0/94/17/fb (b0 const c0),
  no b4/b5, PBA sig c09417fb. CM 10x24ch 10/10 diverge;
  CC 70, b0-3 25/57/52/0f, C10 sig 2557520f == PB1 sig
  (INTRA-tier sig repeat), no b4/b5. M 16x14ch distinct.
  QR r0 ffca8b7ff5c277 distinct (last3 f5c277), r1==r2==r3
  43bcbf7ed5979d LAST3-PAIRED (last3 d5979d), 2 distinct.
  QT 75713981/38ac6799/b7ac6799/163bd7bf 4/4 distinct;
  r1/r2 share last 3B ac6799 (first bytes 38/b7 differ);
  r0/r3 last3 713981/3bd7bf do not. QC 64, b0-3 c09417fb
  == PBA sig, no b4/b5. RM 16x18ch distinct; RQ 16x14ch
  16/16 distinct; RC 70, b0-3 0e/00/00/00, b84-87 06/36/
  19/3d ring-wide. Sorted-unique + _N decls 73/70/64/70
  match actual. Missing-sets EXACT: AC [4,5,15,21,22,23,
  31,76,77,78,79]; CC [4,5,22,23,30,31,32,33,34,35,80,81,
  82,83]; QC [4,5,22,23,30,31,32,33,34,36,37,38,76,77,78,
  79,80,81,82,83]; RC [4,5,30,31,39,40,41,42,46,47,76,77,
  78,79,80,81,82,83]. Coverage unions exact every block
  (const U tab U {b4,b5} == 84/84/84/88, 0 overlap).
  Q legs M[m] + QR[q] + QT[q], no frags. R legs RM[c] +
  RQ[r] STANDARD. RQ==M EXACT 16/16 row-for-row + set-eq
  + C-side identical (VIEWER FINDING, GATE-silent, 12th
  RQ==M instance, exact-equality form; oracle-confirmed
  via green py battery, genuine geometry). RM-vs-RQ
  UNPAIRED (full-row sets disjoint; RM-tail4/RQ-tail4 16
  distinct each, SPLIT-disjoint). AC-QC shared-pos 62
  same-val 26 (NOT const-repeat). QT byte-LCS all-pairs:
  (1,2)=3 rest 0 (own code-table LCS, memo value exact).
  P279 refs re-read: S0 b8aa0700 / S1 74b05c0f (== A-690
  preds); C10 5eb05c0f; RC b0-3 0f000000 + b84-87 75daa80b.
  P280 preds x4 corroborated (58ae0700/2557520f/c09417fb/
  2557520f == staged). M-tails 16/16 ALL NEW vs P279M +
  P279RM-tail8 + P279RQ-tail8 (0 overlap x3). AM/CM/RM/RQ/
  QT/QR 0-overlap vs P279 (widths 18v16/24v22/18v16/14v12
  EXACT). Memo INCL PBA 74 / C10 71 / quad 65 / T88 70
  (A-691 re-read): impl 73/70/64/70 = memo-1 on PBA/C10/
  quad (b5-const excluded), identical T88. Base temp maxes
  _t5887/_b3567/_i3568 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 114177 / S1 114178 / A 114179-194 / C 114195-204 /
  Q 114205-268 / R 114269-524): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (S/A/C/Q full-payload or const+mtab) + R counter
  b4=(0xBB+2off)&FF b5=0x7C+(off>=35)+(off>=163) (py hex;
  C stages decimal 187/124/35/163, re-derived from code
  text both sides) + m=off&15/q=off>>4/c=off&15/r=off>>4
  both sides + mtab/qtab/ttab byte positions exact (A 9B
  b15,21-23,31,76-79; C 12B b22,23,30-35,80-83; Q 7/7/4B
  QM7 b36-38,76-79 + R7 b22,23,30-34 + T4 b80-83; R 9B
  TM9 b30,31,39,46,47,80-83 by COL + 7B TR7 b40-42,76-79
  by ROW) + NO frag leg in Q (py + C region greps).
  T-mirrors T76389/76394/76399/76414/76430/76453 each
  re-read: hits the exact py guard line. C S0/S1 full-
  payload hex+strcmp; C guards `if ((n) == (114177))` /
  `(114178)` + 4 range guards exact. Temps _t5888-5905
  continuous (base max _t5887) + _b3569/3571/3573/3574/
  3575/3577/3578 (base max _b3567) + _i3570/3572/3576/
  3579 (base max _i3568): added-lines-only refs prove no
  reuse. Insert exact both sides: after T10P279R close
  (py 76388 / C 204266), at dispatch tail (N-out-of-scope
  fallthrough follows). Matches A-691/A-344 geometry
  (values re-checked in audit above; NO D dips: ownloop
  tags exactly the 6 P280 blocks).
- Edges own-loop ownloop388.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (319 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. edges388.py: paylens 92 x84 + 256 x88;
  lencode 92/92 (S0/S1 03/7c + 05/7c == raw lencode
  0x7C03/0x7C05) + aform 16/16 (A head 07/7c tail 25/7c
  b5set {7c} NO carry) + cform 10/10 (C head 27/7c tail
  39/7c b5set {7c} NO carry) + qform 64/64 (Q head 3b/7c
  tail b9/7c b5set {7c} NO step NO ff); ring counter
  256/256 + ringraw 256/256 (head bb/7c; 114303 off34
  ff/7c -> 114304 off35 01/7d; mid 114368 off99 81/7d;
  114431 off162 ff/7d -> 114432 off163 01/7e; tail b9/7e);
  exactly 2 ff in tier (114303/114431); odd-b4 348/348 by
  formula construction (all 5 formulas odd-base + 2off,
  all conformance checks green). Ring edges + tail 114524
  in for-list + 2 PASS lines each py+C. Tail 114524:
  oracle sha bf758167b13a3489... matches PINS. No
  DISSENT: cut bytes verify.
- Staged-repeat secf388.py (cache path) + secf388b.py
  (DIRECT tool, no cache): S1-vs-own-C10 47x10 IDENTICAL
  both paths (NOT byte-repeat); staged n113847 from P279
  code (CC + CM row0 + CTAB b13-19,80-83 + lencode) vs
  oracle 0 diff; oracle113847-vs-P280S1 48/84, agree-pos
  36 positions identical both paths (3,6-10,12,14,32-51,
  72-79). 0 miss (ownloop pre-warmed).
- C diff pure-add: numstat 610/0 (rgramc.c) + 237/0
  (rgram.py) + 1/1 (for-line) + 58/0 (PINS) == GATE;
  raw C 605 content + 5 bare-blank / 0 del; raw py 237
  content / 0 del. Own-recipe sweep: C del-uniq 0
  add-uniq 157, py del-uniq 0 add-uniq 177, 0 missing.
  GATE temp-norm recipe replicated: C del-uniq 0
  add-uniq 396 missing 0 == GATE EXACT.
- Wall on band diff added lines (scope 69eaa7e9..
  55198ed2, 906 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 610/0, rgram.py 237/0 purely
  additive, test_rgram.sh 1/1, PINS +58/+0.
- Tiers: merge-msg +6/+58 (919acc47), code 6 blocks,
  singletons 592->594 +2 / ranges 572->576 +4 (stated
  method, plain `if n ==` / `<= n <=` BSD grep), C
  `(n) == (` 592->594 +2 / range idiom 572->576 +4
  (absolute agreement REPRODUCED; r54's 585->587 used a
  different C pattern -- methodology note), CLOSED T10P
  prints 1568->1574 +6 py + 1568->1574 +6 C (deltas agree
  both sides), seal 1662->1668 +6 (commit msgs): all
  agree, no slip (absolute seal inherits lane tally;
  delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-691-q792-
  t10p280 verdict CONFIRM, tallies 12/12 x3 = 36/36
  as-filed (file present, read in full; tallies are memo-
  internal bookkeeping -- my check-mark recount gives
  7/5/4, counting unit irreproducible; methodology note,
  NO verdict impact) + exact-value corroboration incl
  PBA/C10 sigs, QUAD1s + R7 last3-pair + QT tails + LCS
  + b5 const, M-tails NEW, ring STANDARD + TR7 16/16
  UNPAIRED + edges + consts, P279C10-head n113847
  reconstruction 48/84 (all re-checked above) + A-344
  viewer corroboration (all 3 legs CONFIRM, consts 74/71/
  65/70 INCL, values re-checked above). No CONFIRM-P280.md
  file (absence verified); A-691 suffices per rule. Agrees
  with cport commit msg (PYID 8247, RGRAM 16494).
- Quiz: no conflicting CLAIM/GATE/FLAG on b388 (own seat
  CLAIM only; writer seats on disjoint turf). Newest
  PARENT-* is QNUM-21 (w2b block) + QNUM-20 (w2f block):
  pure Q-block grants, read, no gate impact -- GATE cites
  QNUM-19: 1 immaterial staleness x2 (standing pattern).
  PROSE-01: all hex/counts above copied from own run
  output; GATE re-read before filing.
- Own near-misses caught pre-filing x2 (scripts fixed,
  code never impugned): temp one-liner display anomaly
  (base-max values shown in new-list despite strict
  filter, cause unidentified) superseded by TWO clean
  derivations (whole-file unique-set + added-lines-only,
  both == GATE verbatim, filed numbers from clean runs);
  cdiff temp grep polluted by context lines (fixed with
  ^+ filter pre-filing).

Verdict: PASS. No RED. GATE CORRECT on code + prose (1
immaterial QNUM staleness, QNUM-19 vs -21).
FINDING for parent/memo: RQ==M EXACT 16/16 both sides,
GATE/memo-silent, 12th RQ==M instance (exact-equality
form). Code PASS unaffected.
