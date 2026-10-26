# VERIFY-7e4dcf66 b397 T10P289 pins 117309..117656 (1722 tiers) PASS

Seat viewer-r57, first-hand, tree-7e4dcf66 @7e4dcf66,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r57.
Base b68cdf88 (b396, 1716 tiers). Band = 3acd872b (py merge
w2b@84f82ebd partial, +6 tiers, +64 pins) + 7e4dcf66 (C port,
1722 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build397/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 90364d740dc87e06 / aae
  7d8dd3a2d118e0db + sha256 rgramc 45357ab38441210b / aae
  d6e27c97ced21673 (== GATE all 4; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 8531/8531 covered=8531/8531 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17062/17062 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17062/17062 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17062/17062).
- PINS 17064 rows (2 hdr + 17062, +64 vs base 17000);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +32/-0:
  117309 117310 117311 117312 117318 117319 117325 117326
  117327 117328 117333 117334 117335 117336 117337 117352
  117353 117361 117369 117375 117376 117385 117392 117400
  117401 117409 117410 117503 117504 117631 117632 117656
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,6,7,8,9 (offs 2,3,4,5 = 117329/117330/
  117331/117332 unsampled) + Q10 offs 0,15,16,24,32,38,
  39,48,55,63 (b5 step edge o38->o39 straddled: 117375+
  117376 both pinned) + R8 offs 0,8/9,102/103,230/231,
  255 (colsplit pair + both counter edges straddled);
  8499->8531); 32x2=64 rows, range 117309..117656 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit397.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 131 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-2SIG/QUAD88-4R/T88-2SIG ring; no QT/RT/TT;
  no BM/BC, no M19/XA19, no QB/PT/FM, no M42/X42/H42/
  L42); C==py 12/12. S0/S1 168ch sigs 0fc51600 NEW /
  3bf3f420 NEW (full-string NEW vs BOTH P288 strings;
  S0-vs-P288S0 32/84 @ b0,4,5,18-29,32-37,52-55,72,74-79
  EXACT + cross-P288S1 59, S1-vs-P288S1 50/84 @ b2-5,
  22-55,72-83 EXACT + cross-P288S0 72). AM 16x14ch
  distinct; AC 79, b0-3 02/00/00/00 (b0 const 02), no
  b4/b5, PBA sig 02000000 x16 PLAIN. CM 10x24ch 10/10
  diverge; CM-b3 sequence 20 x7 + 1a x3 ORDERED (rows
  0-6/7-9); CC 70, b0-2 3bf3f4 const, b3 in tab
  (partial sig), no b4/b5; C10-2SIG 3bf3f420 x7 +
  3bf3f41a x3 ORDERED. M 16x12ch distinct. QR 4x20ch
  4-distinct UNPAIRED; r0 bbb12ce55fa605a90c59
  distinct; r123 share 6B c7d82676e7fa; tails b84-87
  05a90c59/42ec79b3/86ec79b3/bbed79b3 4/4 distinct;
  r1r2 TRUE 3B ec79b3; r3 shares 2B 79b3 (not the 3B);
  tail-lcsuf (1,2)=3, (1,3)=(2,3)=2, r0-vs-rest 0. QC
  70, b0-3 01000000 (back to 01), no b4/b5; b52-skipped
  const d1 verified in table. RM 16x18ch distinct;
  RM-b0 colsplit 1f x9 (cols 0-8) + 1d x7 (cols 9-15)
  ORDERED in tab. RQ 16x12ch distinct; RC 71, b0 in
  tab, b1-3 00/00/00, b84-87 85/36/00/0f ring-wide.
  RQ==M FULL 16/16 (lists identical; agree matrix
  perfect diagonal 16/16 x6; incidental off-diag (2,5)=
  (5,2)=1 -- NEW degree, all prior odd bands partial;
  16th odd-band RQ==M instance). RM-vs-RQ UNPAIRED
  (sets disjoint). Tails COL-SPLIT (RM b80-83 by COL,
  RQ b76-79 by ROW, 16/16 distinct each, 0 overlap).
  Sorted-unique + _N decls 79/70/70/71 match actual.
  Missing-sets EXACT: AC [4,5,52,53,54,80,81,82,83];
  CC [3,4,5,35,46,47,48,49,50,51,80,81,82,83]; QC [4,5,
  6,7,11,50,51,53,54,55,80,81,82,83,84,85,86,87]; RC
  [0,4,5,6,7,9,10,11,20,76,77,78,79,80,81,82,83].
  Coverage unions exact every block (const U tab U {b4,
  b5} == 88/84/88/88, 0 overlap). Q legs M[m] + QR[q],
  no frags. R legs RM[c] + RQ[r]. P288 refs re-read: S0
  0ac51600 / S1 3bf3942d / PBA 02000000 / C10 3bf3942d
  / QUAD 02000000 (== P288 preds EXACT). P289 preds
  (A-727/A-352 Next-P289: 0fc51600/3bf3f420/02000000/
  2SIG-7+3-ORDERED) x4 corroborated staged. PBA REPEAT
  vs P288 (02000000 == 02000000). QUAD sig back to 01
  vs P288 (01000000 vs 02000000). QR 0-overlap vs
  P288QR. M-tails 16/16 ALL NEW vs P288 RM-tail8
  (overlap 0); RM-tails ALL NEW vs P288 RM-tail8
  (overlap 0); RQ-tails ALL NEW vs P288 RM-tail8 +
  P288 RQ-tail8 (overlap 0 x2). Memo INCL PBA88 80 /
  C10 71 / quad88 70 / T88 71 (A-728 re-read): impl
  79/70/70/71 = memo-1 on PBA/C10 (b5-const excluded),
  identical quad/T88. Base temp maxes _t6043/_b3661/
  _i3662 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 117309 / S1 117310 / A 117311-326 / C 117327-336 /
  Q 117337-400 / R 117401-656): bounds + paylens (12x84
  + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q both
  sides (b5-consts emerge from raw lencode) + Q b5 step
  0x94+(o>=39) edge o38->o39 + R counter b4=
  (0x33+2off)&FF b5=0x95+(off>=103)+(off>=231) (py hex;
  C stages decimal 51/149/103/231, re-derived from
  code text both sides) + colsplit (c<9)?31:29 both
  sides (== 0x1f/0x1d) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions exact
  (A 7B b52-54,80-83; C 12B b3,35,46-51,80-83; Q QM6
  b6,7,80-83 + R10 b11,50,51,53-55,84-87; R TM9 b0,9,
  10,11,20,80-83 by COL + TR6 b6,7,76-79 by ROW) + NO
  frag leg in Q. T-mirrors T78513/78518/78523/78538/
  78554/78575 each re-read: hits the exact py guard
  line. C guards `if ((n) == (117309))` / `(117310)` +
  4 range guards exact. C byte-index lists match py per
  block (A 7B, C 12B, Q 6B/10B, R 9/6B). Temps
  _t6044-6059 continuous (base max _t6043) + _b3663/
  3665/3667/3668/3670/3671 (base max _b3661) + _i3664/
  3666/3669/3672 (base max _i3662): added-lines-only
  refs (base tree zero refs to new temps) prove no
  reuse. Insert exact both sides: after T10P288R close,
  at dispatch tail (N-out-of-scope fallthrough follows;
  C 2 scope hits, py 2 scope hits). Matches A-728/A-353
  geometry (values re-checked in audit above; NO D dips:
  ownloop tags exactly the 6 P289 blocks).
- Edges own-loop ownloop397.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (316 miss-warmed first run; tag-list sed miss
  fixed, re-run 0 miss). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P289R N=117656 off=
  255. edges397.py: paylens 12x84 + 336x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 7b/94, 7d/94 == raw
  lencode) + aform 16/16 (A 88B head 7f/94 tail 9d/94
  b5set {94} NO step, 0 ff) + cform 10/10 (C head 9f/
  94 tail b1/94 b5set {94} NO step, 0 ff) + qform 64/64
  + qb5step 64/64 (Q head b3/94 tail 31/95 b5set {94,
  95} step o38->o39: 117375 o38 ff/94 -> 117376 o39
  01/95, exactly 1 ff in 64 at o38; quad b4 formula ==
  raw-lencode 64/64); ring counter 256/256 + ringraw
  256/256 (head 33/95; 117503 off102 ff/95 -> 117504
  off103 01/96; mid off128 33/96; 117631 off230 ff/96
  -> 117632 off231 01/97; tail off255 31/97; exactly 2
  ff in 256 at o102/o230) + colsplit 144+112 bad=0 over
  oracle bytes; odd-lencode 348/348. Ring edges +
  tail 117656 in for-list + 2 PASS lines each py+C.
  Tail 117656: oracle sha 8bcb4fd24d00a120... matches
  PINS; py+C CLOSED T10P289R off=255 agree. No DISSENT:
  cut bytes verify.
- PB-diff secf397.py (cache path) + secf397b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (117309 +
  116961 + 117310 + 116962); S0: oracle117309-vs-116961
  32/84, codeS0-vs-P288S0 32/84, positions identical;
  DIRECT tool 32/84 with identical agree-pos 52
  positions. S1: oracle 50/84, code 50/84, positions
  identical; DIRECT 50/84 identical agree-pos 34
  positions. 0 miss (ownloop pre-warmed). Twice-derived
  both pairs. No byte-equal wording in A-728/A-353 this
  band (both stage NEW sigs, consistent with 32/50
  diffs) -- byte-diff discipline observed, nothing to
  refute.
- C diff pure-add: numstat 607/0 (rgramc.c) + 233/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE;
  raw C 602 content + 5 bare-blank / 0 del; raw py 233
  content / 0 del. Normalized ([0-9]+ -> N recipe):
  py del-uniq 0 add-uniq 175 missing 0 == GATE EXACT.
  C add-uniq: stated recipe gives 151 first-hand (python
  + BSD shell, twice-derived, same inputs: sweep's
  cdiff397 +line set cmp-equal mine 607/607); lstrip +
  drop-empty reconstruction gives 147 == GATE EXACT
  (python + BSD shell, twice-derived; py is 175 under
  EVERY variant, so one lstrip+drop-empty script yields
  exactly GATE's 147/175 pair). del-uniq 0 +
  del-subset-add 0 missing hold under EVERY variant
  (integrity property intact). Recipe-description
  imprecision only (GATE prose omits the lstrip +
  empty-drop steps); numbers are genuine script
  outputs. Code unaffected. NOTE: r56's r60
  reconstruction needed keep-empty (166/165); r61 needs
  drop-empty (147) -- sweep-side one-liner drift;
  suggest sweep publish the one-liner (one line, no
  re-GATE needed).
- Wall on band diff added lines (scope b68cdf88..
  7e4dcf66, 905 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 607/0, rgram.py 233/0 purely
  additive, test_rgram.sh 1/1, PINS +64/+0.
- Tiers: merge-msg +6/+64 (3acd872b), code 6 blocks,
  tier-comments `# T10P` 1622->1628 +6, singletons
  610->612 +2 / ranges 608->612 +4, CLOSED T10P prints
  1622->1628 +6 py + 1622->1628 +6 C, C singleton
  `if ((n) == (` 605->607 +2 / C ranges 608->612 +4,
  seal 1716->1722 +6 (commit msgs): all agree, no slip.
  5-count py-vs-C singleton offset pre-existing +
  unchanged (gap 5 at base AND new).
- CONFIRM evidence (CONVERT-01 rule b): A-728-q881-
  t10p289 verdict CONFIRM, tallies 14/14 + 11/11 + 12/12
  = 37/37 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 17 total vs 37, counting unit irreproducible;
  methodology note, NO verdict impact) + exact-value
  corroboration incl PB0 NEW + PB1 NEW, PBA88-PLAIN +
  b5 const, C10-2SIG ORDERED 7+3, QUAD88-4R + R10 rows
  + tails + TRUE-3B + b5 step + edge + M-tails NEW,
  T88-2SIG col-split 144+112 + TM9/TR6 16/16 UNPAIRED
  + SPLIT tails + b84-87 const + ring edges +
  thresholds (all re-checked above) + A-353 viewer
  corroboration (CONFIRM all legs, consts 80/71/70/71
  INCL). No CONFIRM-P289.md file (absence verified);
  A-728 suffices per rule. Agrees with cport commit msg
  (PYID 8531, RGRAM 17062).
- Quiz: no conflicting CLAIM/GATE/FLAG on b397 (own seat
  CLAIM only). Newest PARENT-QNUM-22 (w2e Q-block grant,
  read, no gate impact) -- GATE cites QNUM-19: 1
  immaterial staleness (standing pattern). PROSE-01: all
  hex/counts above copied from own run output; GATE
  re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 immaterial GATE prose notes (QNUM-19 vs -22
staleness; norm recipe prose omits lstrip + empty-drop
steps -- 147/175 verified genuine via reconstruction,
integrity intact).
Next-P290 predictions banked for r58 (A-728/A-353: PB0
@117657 5f6f1300 NEW / PB1 ccbede26 NEW / PBA88 02000000
x16 / C10-3SIG 1b19db26 x7 @117675-81 + bb9cdb26 x1
@117682 + 8bf4d626 x2 @117683-84 ORDERED 7/1/2
window-resolved).
