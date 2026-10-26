# VERIFY-f7832b11 b464 T10P356 pins 140625..140972 (348 pins) PASS

Seat viewer-r74, first-hand, tree @f7832b11,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r74.
Base 3d07ab9f (b463 tip, 2118 tiers sealed; this
seat's chain base-use only, respected). Band = 08a94eeb (py
merge w2b@1005ae89 partial, +6 tiers, +58 pins;
commit msg verified via git log) + f7832b11 (C
port; parent == 08a94eeb verified via git
rev-list --parents). Chain 08a94eeb parent ==
3d07ab9f verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P356 shape (A-942 Q1 + Q-1067 agree)
CONSUMED FIRST and VERIFIED first-hand EXACT:
PB0 aefa600f @140625 (S0 head; NEW-sig-1B-off
36/84 diff vs P355PB0 @ n140277, b3 IN diff
with b0-2 NOT, positions
[3-5,21-23,25-38,40-43,64-75]
first-hand, NOT byte-equal) + PB1 1c000000
@140626 (S1 head; NEW-sig 50/88 diff vs P355PB1
@ n140278, sig b0 IN diff, positions
[0,4,5,16-23,26,27,34-40,42-59,72-79,84-87]
first-hand, NOT byte-equal; 57/88 vs own C10[0]
n140643, DIFFERS-sig-vs-own-C10 1c-vs-1a;
DIFFERS-vs-own-PB0 af-vs-1c) +
PBA c5010000 x16 @140627-642 (AC b0-3 =
c5/01/00/00; A-mtab b6,7,9,80-83) + C10-region
1a000000 pay88 x10 @140643-652 (CC b0-3 =
1a/00/00/00, DIFFERS-from-PB1-sig; CM lanes
b84,85 with b86 const 0x9c + b87 const 0xc5 in
CC; CM rows b84,85 diverge 4ch) -- all
corroborated against lane code both sides
before any battery step (no bank-miss).

- Build: seat-private build464/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 f1fa922d...
  (full sha256 == GATE; GATE states full sha256
  this band).
- RGRAMC-PYID 10597/10597 covered=10597/10597
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21194/21194 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21194/21194 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21194/21194, sorted +
  raw identical; cmp464.py GREEN).
- PINS-RGRAM cells set-eq 10597/10597 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq464.py GREEN). PINS 21196 lines
  first-hand (2 hdr + 21194 rows; base 21138
  lines / 21136 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10568->10597 +29/-0 (python
  sets, trailing-';' strip, never comm): 140625
  140626 140627 140628 140634 140635 140641
  140642 140643 140644 140647 140648 140651
  140652 140653 140658 140668 140671 140672
  140684 140700 140716 140717 140799 140800
  140860 140927 140928 140972 (== GATE sampled
  list EXACT).
  29 = 2 sing (140625 140626) + A 6 (head
  140627 + 140628 + pair 140634/140635 off7/8 +
  tail pair 140641/140642 off14/15; offs 0,1,7,
  8,14,15; b5 const 4a NO step NO edge) + C 6
  (head 140643 + 140644 + mid pair 140647/
  140648 off4/5 + tail pair 140651/140652 off8/
  9; offs 0,1,4,5,8,9; b5 const 4a NO step) + Q
  8 (head 140653 off0 + 140658 off5 + 140668
  off15 + edge pair 140671/140672 off18/19 +
  140684 off31 + 140700 off47 + tail 140716
  off63; b5 = 0x4a+(off>=19)) + R 7 (head
  140717 off0 + edge pair 140799/140800 off82/
  83 + mid 140860 off143 + edge pair 140927/
  140928 off210/211 + tail 140972 off255;
  1-mid shape off143 NEW, both counter edges
  pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21194-21136.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit464.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 152 PASS 0 FAIL second-run (1
  seat-script fix: QR tail-const slice t[2:]->
  t[1:]; ZERO GATE slips this band).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig aefa600f NEW-sig-1B-off (36/84
  payload diff vs P355S0, positions
  [3-5,21-23,25-38,40-43,64-75]
  first-hand, b3 IN diff with b0-2 NOT, NOT
  byte-equal) / S1 176ch sig 1c000000 NEW-sig
  (50/88 payload diff vs P355S1, positions
  [0,4,5,16-23,26,27,34-40,42-59,72-79,84-87]
  first-hand, sig b0 IN diff, NOT byte-equal;
  vs own C10 cells NOT-UNIFORM 57/88 x10
  staged+oracle: all-10 diff 57, sig 1c-vs-1a
  DIFFERS; S1 SIG-DIFFERS own C10; S1
  SIG-DIFFERS own PB0), staged as full-payload
  singletons.
  AM 16/16 14ch distinct, CM 10/10 4ch diverge,
  M 16/16 14ch distinct, QR 4/4 2ch distinct
  R1 rows 31/51/71/91 exact tuples; full tails =
  R1 + b85 const 0x7c + b86 const 0x9c + b87
  const 0xc5 quad-wide, 4/4 distinct;
  trailing-suffix = TSHARE = subseq-lcs =
  3/3/3/3/3/3 (all-3 agree first-hand); tails 4
  distinct), RM 16/16 16ch distinct, RQ 16/16
  14ch distinct, no QT (R1 b84 inside QR + b85/
  86/87 consts) + no RT (SPLIT tails) + no F
  (no frags).
  M==RQ 16/16 string-identical SAME-ORDER (M
  list == RQ list; QM7 b0,10,11,80-83 by COL
  m=off&15 vs TR7 b0,10,11,76-79 by ROW
  r=off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated) -- 49th even-band
  RQ==M instance, ORDERED-IDENTICAL degree
  (viewer chain: evens 48->49; full-identity
  survey 15th); ordered per lesson (same-width
  7B/7B, lists identical); width predictor
  dead, never cited; tails SPLIT (TM b12,13,18,
  19,80-83 by COL c=off&15, TR b0,10,11,76-79
  by ROW r=off>>4, 16/16 distinct each,
  sequences UNPAIRED); M-tails 16/16 ALL NEW
  vs P355T RM col-led tails (overlap 0; P355T
  frame first-hand from code); AM/CM/M/QR/RM/
  RQ full-row 0-overlap vs P355 (all 0/16;
  widths P356 vs P355: AM 7B vs 8B, CM 2B vs
  3B, M 7B vs 8B, QR 1B vs 2B, RM 8B vs 8B, RQ
  7B vs 8B).
  AC 79, CC 84, QC 78, RC 71; C _N decls
  79/84/78/71 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap gap-
  free, M/R-tab computed; Q b0 colsplit 20x70+
  44x71 (col<5 iff 70); b1 const 01 in QC
  first-hand; C b86/b87 const 9c/c5 in CC
  first-hand).
  PBA88-PLAIN-M7b6 sig c5010000 (b0 const c5
  via AC b0-3; AM 16/16 distinct NO pair; M7
  b6,7,9,80-83; b5 const 4a NO step NO edge --
  b5 const deducted, in AC-missing).
  C10-1SIG-88-TAIL-M2 sig 1a000000 x10
  DIFFERS-from-PB1-sig (full sig b0-3 in CC =
  1a000000; CM 10/10 diverge 4ch b84,85; CC has
  no b84,85 (both in CM lane); b86,87 const 9c/
  c5; b5 const 4a full block via lencode).
  QUAD88-2SIG-QM7/R1-COLSPLIT 2-sig b0=70-iff-
  col<5 (20x70 + 44x71; QM7 rows col<5 b0=70
  first-hand; b5 = 0x4a+(off>=19) in VPOS, edge
  off18->19; QM7 b0,10,11,80-83 M 16/16 14ch
  distinct NO frags (m = off&15 first-hand) +
  R1 b84 rows 31/51/71/91 4/4 UNPAIRED BY-ROW
  const (q = off>>4 first-hand); tails = R1 +
  const b85 7c / b86 9c / b87 c5 quad-wide,
  full-tail suffix-lcs 3/3/3/3/3/3 + R1 all-
  distinct).
  Ring T88-2SIG-ROWSPLIT: rows0-4 sig 701a0000
  x80 + rows5-15 sig 711a0000 x176 (b0 row-led
  70 iff row<5; TR7 rows 0-4 b0=70 first-hand;
  code-TM8 b12,13,18,19,80-83 by COL RM 16/16
  + code-TR7 b0,10,11,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79
  row); b1 const 1a; b84-87 const b17c9cc5
  ring-wide NEW; b4=(0x5b+2off)&FF +
  (off>=83)+(off>=211) (C literals 91/75/83/
  211 verified == 0x5b/0x4b/83/211)).
  VPOS partitions re-derived from code: PBA 8
  (missing 9 - 1; b4+M7 b6,7,9,80-83, b5 const
  deducted) / C10 3 (missing 4 - 1; b4+M2
  b84,85, b5 const deducted) / quad 10
  (missing 10 - 0; b0/b4/b5+QM7 7+R1, b5
  varies colsplit-edge in VPOS, NO deduct) / T
  17 (missing 17 - 0; b4,b5+TM8+TR8, b0/b1
  consts live in-table) -- all match A-943
  (missing sets AC-9 [4,5,6,7,9,80-83] / CC-4
  [4,5,84,85] / QC-10 [0,4,5,10,11,80-84] /
  RC-17 [0,4,5,10-13,18,19,76-83] first-hand
  EXACT; deduct-const-b5-or-in-table convention
  holds; b5 variance checked from oracle bytes:
  A {4a} const, C {4a} const, Q {4a,4b} steps,
  T counter-varies).
  Code-consts vs A-943 INCL/EXCL (PBA 79 / C10
  84 / quad 78 / T88 71 excl): impl 79/84/78/
  71 = memo-excl EXACT -- no lag on even band
  (deduct-only-when-vary holds; A-943 INCL
  +2/+2 for the two b5-const lanes = 80/85/78/
  71). VPOS 8/3/10/17 = memo EXACT. S-F lag
  stays 44; even sub-streak stays 26 (b464
  non-lag breaks the lag run; GATE's "27th
  even band running b412-b464" is memo's
  even-band run counter, not the lag streak).
  M-tails 16/16 ALL NEW vs P355T RM col-led
  tails (overlap 0); AM/CM/M/QR/RM/RQ 0-overlap
  vs P355 all six.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 140625 / S1 140626 / A 140627-642 /
  C 140643-652 / Q 140653-716 / R 140717-972):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C b5 const emerges
  from raw lencode; Q b5 step emerges from raw
  lencode + b4 formula) + R explicit counter
  (b4=(0x5b+2off)&FF b5=0x4b+(off>=83)+
  (off>=211); py hex 0x5b/0x4b; C staged
  literals 91/75/83/211 re-derived: 91==0x5b,
  75==0x4b) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 14ch b6,7,9,80-83; C 4ch
  lane b84,85 + b86/b87 consts; Q 14ch/1ch
  b0,10,11,80-83/b84; R 16ch/14ch SPLIT TM8
  b12,13,18,19,80-83 by COL / TR7 b0,10,11,
  76-79 by ROW).
  C blocks carry T94437/94442/94447/94462/
  94477/94496 py-line cites (each re-read: hits
  the exact py guard line, C comment text
  matches py, all 6 present; bounds + byte
  positions exact: A 14ch, C 4ch, Q 14/1ch, R
  16/14ch), A/C/Q raw lencode (no counter
  literals) + R counter b4=(0x5b+2off)&FF +
  (off>=83)+(off>=211) (C literals 91/75/83/
  211 verified), temps _t7149-7164 (base max
  _t7148, no reuse) + _i4337/4339/4342/4345
  (base max _i4335, no reuse) + _b4336/4338/
  4340/4341/4343/4344 (base max _b4334, no
  reuse), all 6 blocks verified.
  Insert position exact both sides: after
  T10P355R close (C "T10P3560 singleton" after
  "CLOSED T10P355R"; py return 0 + S0 guard
  94437), at dispatch tail (N-out-of-scope
  fallthrough follows: C 251188, py 94515;
  plateau guards at C 169595 / py 58521 are
  the T4 plateau, unrelated scope).
  Matches A-943 geometry (PB0 NEW-sig-1B-off
  36/84; PB1 NEW-sig 50/88; PBA88-PLAIN-M7b6
  VPOS 8 sig-c5 b5 const M7 16/16 distinct;
  C10-1SIG-88-TAIL-M2 VPOS 3 DIFFERS-from-PB1-
  sig b5 const M2 10/10 diverge; QUAD88-2SIG-
  QM7/R1-COLSPLIT VPOS 10 + R1 4/4 UNPAIRED
  31/51/71/91 + suffix-lcs-3/3/3/3/3/3 + R1-
  distinct + NO frags + M-tails NEW; T88-2SIG-
  ROWSPLIT VPOS 17 + TM8-by-COL/TR7-by-ROW +
  SPLIT-tails + b84-87 b17c9cc5 + counter 5b/
  4b/83/211; lencode 348/348 whole-tier, NO D
  dips) incl exact values; M==RQ 16/16 string-
  identical same-order first-hand this tier,
  tier stands.
- Edges via counter formula first-hand: A head
  a7/4a tail c5/4a b5set {4a} NO step, 0 ff; C
  head c7/4a tail d9/4a b5set {4a} NO step, 0
  ff; Q head db/4a tail 59/4b b5set {4a,4b}
  edge off18 (ff/4a) -> off19 (01/4b), exactly
  1 ff; ring pre-edge off82 (ff/4b), edge
  off83 (01/4c); edge off210 (ff/4c) -> off211
  (01/4d); exactly 2 ff in 256; R head 5b/4b
  tail 59/4d; formulas re-derived from
  T10P356R code text (5b/4b/83/211) +
  T10P356A/C/Q text (raw lencode); all edge
  pins + mid pin 140860 (off143) + tail 140972
  in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (a3/a5 + 4a) match raw
  lencode. Ring counter==raw-lencode 256/256 +
  Q 64/64 + A 16/16 + C 10/10. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT on cut
  bytes (edges464.py EDGES-GREEN, Q single-ff
  edge + range-with-wrap asserts verified
  first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 231/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; for-line replaced by superset (base
  for-N subset of band, removed 0); fine-norm
  equivalent (for463base.nums subset
  for464.nums, removed 0; C-scope del 0).
- Wall on band diff added lines (scope
  3d07ab9f..f7832b11, 898 added lines): vendor
  0 hits, disasm 0 hits, depload 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits; 1 `aea` substring = PINS sha hex
  fragment (d52289b5..., 0 invocations -- same
  hex-fragment class as r73 b463). Files
  touched: rgramc.c 608/0, rgram.py 231/0
  purely additive, test_rgram.sh 1/1 (for-line
  extension), PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-ind4 734->736
  (+2: 140625/140626) / ranges py-ind4 854->
  858 (+4; C singletons 739->741 +2 / ranges
  876->880 +4, same 6 P356 blocks both sides;
  no elif/else-if added either side: py
  file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2024->2030 +6 both sides, seal 2118->2124 +6
  (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
  Viewer-vs-sweep reconcile first-hand:
  GATE-tier absolutes 4sp-dispatch-exact (py
  734->736, ranges 854->858; C 739->741,
  ranges 876->880 -- all EXACT, no slip this
  band); file-wide unanchored py 744->746
  (+10 non-dispatch early-tier guards) + 5-
  count C-vs-py dip-guard offset; deltas
  +2/+4/+6 every method.
- CONFIRM evidence (CONVERT-01 rule b):
  A-943-q1068-P356 verdict CONFIRM 52/52 CLEAN
  (own bed r5-P356 140625..141000 + r5-P355
  cross-refs, BAD=0 + direct-oracle 2/2
  byte-match; verifier v501.py P356 52/52
  PASS; file present, counts verified; tier
  GATED PORT; novelty gated: M-tails 16/16 ALL
  NEW vs P355T col-led tails; exact-value
  corroboration incl PB0 NEW-sig-1B-off 36/84,
  PB1 NEW-sig 50/88, PBA16 sig-c5 VPOS 8, C10
  sig-1a DIFFERS-PB1 VPOS 3, QUAD64 2-sig-
  colsplit + R1 rows + suffix-lcs-3/3/3/3/3/3
  + R1-distinct + QM7 + NO frags + M-tails
  NEW, T256-2SIG-ROWSPLIT + TM8-by-COL/TR7-
  by-ROW + SPLIT-tails + const b17c9cc5 +
  counter/edges; plus const-count note: A-943
  excl 79/84/78/71 memo-exact, committed
  tables match excl exactly -- no writer lag
  this tier, geometry exact, PORT verdict
  stands). Agrees with cport commit msg (PYID
  10597, RGRAM 21194).
- FWD-check first-hand: A-943 "Next P357"
  forward notes verified against P357 lane code
  (58b503c0, git show, no checkout): PB0
  aefa600d @140973 (168ch pay84) + PB1
  1a000000 @140974 (176ch pay88) + PBA
  a6010000 x16 (guard 140975..140990) +
  C10-region 1a000000 x10 (guard 140991..
  141000) -- all exact (banked for b465
  CONSUME).
- Quiz: no conflicting CLAIM/GATE/FLAG on b464.
  Activity polled (no b464 conflict); PROSE-01
  re-read before filing (all hex/counts copied
  from run output above).
- Logs: NVME ws tmp/encode-viewer/r74/
  (build464.log, pyid464.log, rgram464py/c.log,
  cmp464.py, seteq464.py, ownloop464.py,
  secf464a/b/c.py, edges464.py, tabaudit464.py,
  w464loop.log, smoke464.log, units464.log,
  band diff via git).

Verdict: PASS. No RED. 348-pin contiguous range
140625..140972 sealed. Ready for viewer b465.
