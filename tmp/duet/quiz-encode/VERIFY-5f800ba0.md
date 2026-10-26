# VERIFY-5f800ba0 b466 T10P358 pins 141321..141668 (348 pins) PASS

Seat viewer-r74, first-hand, tree @5f800ba0,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r74.
Base be565d02 (b465 tip, 2130 tiers sealed; this
seat's VERIFY-be565d02 PASS-filed same round,
base-use only, respected). Band = ee21fae8 (py
merge w2b@367df011 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 5f800ba0 (C
port; parent == ee21fae8 verified via git
rev-list --parents). Chain ee21fae8 parent ==
be565d02 verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P358 shape (VERIFY-be565d02 "Next
P358" FWD, CONSUMED at that filing and
re-corroborated here pre-battery) CONSUMED
FIRST and VERIFIED first-hand EXACT: PB0
ada6240d @141321 (S0 head; NEW-sig sigdiff-3
31/84 diff vs P357PB0 @ n140973, b0-2 IN diff
with b3 same -- NOT 1B-off, positions
[0-2,4,5,13-17,19-21,24-29,56-67]
first-hand, NOT byte-equal) + PB1 18000000
@141322 (S1 head; NEW-sig 49/88 diff vs P357PB1
@ n140974, sig b0 IN diff, positions
[0,4,5,11,19-47,64-75,84-87]
first-hand, NOT byte-equal; 44/88 vs own C10[0]
n141339, DIFFERS-sig-vs-own-C10 18-vs-1d;
DIFFERS-vs-own-PB0 ad-vs-18) + PBA e0010000
x16 @141323-338 (AC b0-3 = e0/01/00/00;
A-mtab b30,39,47,80-83) + C10-region 1d000000
pay88 x10 @141339-348 (CC b0-3 = 1d/00/00/00,
DIFFERS-from-PB1-sig; CM lanes b84,85,86,87
M4, CC has no b84-87; CM rows b84-87 diverge
8ch) -- all corroborated against lane code
both sides before any battery step (no
bank-miss).

- Build: seat-private build466/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 3cf5d0bd...
  (full sha256 == GATE; GATE states full sha256
  this band).
- RGRAMC-PYID 10655/10655 covered=10655/10655
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21310/21310 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21310/21310 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21310/21310, sorted +
  raw identical; cmp466.py GREEN).
- PINS-RGRAM cells set-eq 10655/10655 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq466.py GREEN). PINS 21312 lines
  first-hand (2 hdr + 21310 rows; base 21254
  lines / 21252 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10626->10655 +29/-0 (python
  sets, trailing-';' strip, never comm): 141321
  141322 141323 141324 141330 141331 141337
  141338 141339 141340 141343 141344 141347
  141348 141349 141364 141365 141380 141381
  141396 141397 141412 141413 141439 141440
  141500 141567 141568 141668 (== GATE sampled
  list EXACT).
  29 = 2 sing (141321 141322) + A 6 (head pair
  141323/141324 off0/1 + pair 141330/141331
  off7/8 + tail pair 141337/141338 off14/15;
  b5 const 50 NO step NO edge) + C 6 (head
  141339/141340 off0/1 + mid pair 141343/141344
  off4/5 + tail pair 141347/141348 off8/9; b5
  const 50 NO step) + Q 8 (head 141349 off0 +
  141364 off15 + 141365 off16 + pair 141380/
  141381 off31/32 + pair 141396/141397 off47/48
  + tail 141412 off63; NO edge -- b5 const 50
  this tier) + R 7 (head 141413 off0 + edge
  pair 141439/141440 off26/27 + mid pin 141500
  off87 + edge pair 141567/141568 off154/155 +
  tail 141668 off255; no pre-edge pin in
  for-list -- witness pattern differs,
  first-hand; 1-mid shape off87 NEW, both
  counter edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21310-21252.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit466.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 153 PASS 0 FAIL first-run (0
  seat-script fixes this band; 1 GATE prose
  note: INCL "80/85/79/71" slips C10 85-vs-83,
  excl exact, code GREEN -- recorded below).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ada6240d NEW-sig sigdiff-3
  (31/84 payload diff vs P357S0, positions
  [0-2,4,5,13-17,19-21,24-29,56-67]
  first-hand, b0-2 IN diff with b3 same -- NOT
  1B-off, NOT byte-equal) / S1 176ch sig
  18000000 NEW-sig (49/88 payload diff vs
  P357S1, positions
  [0,4,5,11,19-47,64-75,84-87]
  first-hand, sig b0 IN diff, NOT byte-equal;
  vs own C10 cells NOT-UNIFORM 44/88 x10
  staged+oracle: all-10 diff 44, sig 18-vs-1d
  DIFFERS; S1 SIG-DIFFERS own C10; S1
  SIG-DIFFERS own PB0), staged as full-payload
  singletons.
  AM 16/16 14ch distinct, CM 10/10 8ch diverge
  M4 (b84-87 all in CM lane), M 16/16 14ch
  distinct, QR 4/4 2ch distinct R1 rows 41/61/
  81/a1 exact tuples; full tails = R1 + b85
  const 0x3f + b86 const 0x2b + b87 const 0xa9
  quad-wide, 4/4 distinct; trailing-suffix =
  TSHARE = subseq-lcs = 3/3/3/3/3/3 (all-3
  agree first-hand); tails 4 distinct), RM
  16/16 16ch distinct, RQ 16/16 14ch distinct,
  no QT (R1 b84 inside QR + b85/86/87 consts) +
  no RT (SWAPPED tails) + no F (no frags).
  M==RQ 16/16 string-identical SAME-ORDER (M
  list == RQ list; QM7 b52,53,54,80-83 by COL
  m=off&15 vs TR7 b52,53,54,80-83 by ROW
  r=off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated) -- 50th even-band
  RQ==M instance, ORDERED-IDENTICAL degree
  (viewer chain: evens 49->50; full-identity
  survey 17th); ordered per lesson (same-width
  7B/7B, lists identical); width predictor
  dead, never cited; tails SWAPPED (TM b6,7,8,
  9,76-79 by COL c=off&15, TR b52,53,54,80-83
  by ROW r=off>>4, 16/16 distinct each,
  sequences UNPAIRED); M-tails 16/16 ALL NEW
  vs P357T RM col-led tails (overlap 0; P357T
  frame first-hand from code); AM/CM/M/QR/RM/
  RQ full-row 0-overlap vs P357 (all 0/16;
  widths P358 vs P357: AM 7B vs 8B, CM 4B vs
  2B, M 7B vs 9B, RM 8B vs 8B, RQ 7B vs 8B, QR
  1B vs 2B).
  AC 79, CC 82, QC 78, RC 71; C _N decls
  79/82/78/71 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; Q b0 const e0
  1-sig SAME-as-PBA in QC first-hand (b1 const
  01, b2-3 const 00); C b84-87 all absent from
  CC (M4 lane) first-hand).
  PBA88-PLAIN-M7b30 sig e0010000 (b0 const e0
  via AC b0-3; AM 16/16 distinct NO pair; M7
  b30,39,47,80-83; b5 const 50 NO step NO edge
  -- b5 const deducted, in AC-missing).
  C10-1SIG-88-TAIL-M4 sig 1d000000 x10
  DIFFERS-from-PB1-sig (full sig b0-3 in CC =
  1d000000; CM 10/10 diverge 8ch b84-87; CC has
  no b84-87 (all in CM lane); b5 const 50 full
  block via lencode).
  QUAD88-1SIG-QM7/R1-NOEDGE 1-sig e0010000 x64
  SAME-sig-as-PBA (QC b0 const e0; b5 const 50
  deducted to raw lencode NO edge; b4 base
  0x4b step2 64/64 range 4b..c9, NO wrap; QM7
  b52,53,54,80-83 M 16/16 14ch distinct NO
  frags (m = off&15 first-hand) + R1 b84 rows
  41/61/81/a1 4/4 UNPAIRED BY-ROW const (q =
  off>>4 first-hand); tails = R1 + const b85
  3f / b86 2b / b87 a9 quad-wide, full-tail
  suffix-lcs 3/3/3/3/3/3 + R1 all-distinct).
  Ring T88-SWAPPED 1-sig 051e0000 x256 (b0
  const 05 256/256 oracle, in RC table; b1
  const 1e 256/256 oracle, in RC table;
  code-TM8 b6,7,8,9,76-79 by COL RM 16/16 +
  code-TR7 b52,53,54,80-83 by ROW RQ 16/16
  UNPAIRED (SWAPPED tails b80-83 row / b76-79
  col); b84-87 const c13f2ba9 ring-wide NEW;
  b4=(0xcb+2off)&FF + (off>=27)+(off>=155) (C
  literals 203/80/27/155 verified == 0xcb/0x50/
  27/155)).
  VPOS partitions re-derived from code: PBA 8
  (missing 9 - 1; b4+M7 b30,39,47,80-83, b5
  const deducted) / C10 5 (missing 6 - 1;
  b4+M4 b84-87, b5 const deducted) / quad 9
  (missing 10 - 1; b4+QM7 7+R1, b5 const
  deducted NOEDGE) / T 17 (missing 17 - 0;
  b4,b5+TM8+TR8, b0/b1 consts live in-table)
  -- all match A-945 (missing sets AC-9
  [4,5,30,39,47,80-83] / CC-6 [4,5,84-87] /
  QC-10 [4,5,52-54,80-84] / RC-17
  [4,5,6-9,52-54,76-83] first-hand EXACT;
  deduct-const-b5-or-in-table convention holds
  incl the M4/M7b30/NOEDGE/SWAPPED shapes; b5
  variance checked from oracle bytes: A {50}
  const, C {50} const, Q {50} const, T
  counter-varies).
  Code-consts vs A-945 INCL/EXCL (PBA 79 / C10
  82 / quad 78 / T88 71 excl): impl 79/82/78/
  71 = memo-excl EXACT -- no lag on even band
  (deduct-only-when-vary holds; A-945 INCL
  +1/+1/+1 for the three b5-const lanes =
  80/83/79/71; GATE prose "80/85/79/71" slips
  C10 85-vs-83, excl exact, code GREEN).
  VPOS 8/5/9/17 = memo EXACT. S-F lag stays 44;
  even sub-streak stays 26 (b466 non-lag breaks
  the lag run; GATE's "28th even band running
  b412-b466" is memo's even-band run counter,
  not the lag streak). M-tails 16/16 ALL NEW
  vs P357T col-led tails (overlap 0); AM/CM/M/
  QR/RM/RQ 0-overlap vs P357 all six.
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 141321 / S1 141322 / A 141323-338 /
  C 141339-348 / Q 141349-412 / R 141413-668):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C/Q b5 const emerges
  from raw lencode) + R explicit counter
  (b4=(0xcb+2off)&FF b5=0x50+(off>=27)+
  (off>=155); py hex 0xcb/0x50; C staged
  literals 203/80/27/155 re-derived: 203==0xcb,
  80==0x50) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 14ch b30,39,47,80-83; C
  8ch lane b84-87 + no consts; Q 14ch/1ch
  b52,53,54,80-83/b84; R 16ch/14ch SWAPPED TM8
  b6,7,8,9,76-79 by COL / TR7 b52,53,54,80-83
  by ROW).
  C blocks carry T94899/94904/94909/94924/
  94939/94958 py-line cites (each re-read: hits
  the exact py guard line, C comment text
  matches py, all 6 present; bounds + byte
  positions exact: A 14ch, C 8ch, Q 14/1ch, R
  16/14ch), A/C/Q raw lencode (no counter
  literals) + R counter b4=(0xcb+2off)&FF +
  (off>=27)+(off>=155) (C literals 203/80/27/
  155 verified), temps _t7181-7196 (base max
  _t7180, no reuse) + _i4357/4359/4362/4365
  (base max _i4355, no reuse) + _b4356/4358/
  4360/4361/4363/4364 (base max _b4354, no
  reuse), all 6 blocks verified.
  Insert position exact both sides: after
  T10P357R close (C "T10P3580 singleton" after
  "CLOSED T10P357R"; py return 0 + S0 guard
  94899), at dispatch tail (N-out-of-scope
  fallthrough follows: C 170526, py 94977;
  plateau guards at C 170460 / py 58826 are
  the T4 plateau, unrelated scope).
  Matches A-945 geometry (PB0 NEW-sig sigdiff-3
  31/84; PB1 NEW-sig 49/88; PBA88-PLAIN-M7b30
  VPOS 8 sig-e0 b5 const M7 16/16 distinct;
  C10-1SIG-88-TAIL-M4 VPOS 5 DIFFERS-from-PB1-
  sig b5 const M4 10/10 diverge; QUAD88-1SIG-
  QM7/R1-NOEDGE VPOS 9 + R1 4/4 UNPAIRED
  41/61/81/a1 + suffix-lcs-3/3/3/3/3/3 + R1-
  distinct + NO frags + M-tails NEW; T88-
  SWAPPED VPOS 17 + TM8-by-COL/TR7-by-ROW +
  SWAPPED-tails + b84-87 c13f2ba9 + counter cb/
  50/27/155; lencode 348/348 whole-tier, NO D
  dips) incl exact values; M==RQ 16/16 string-
  identical same-order first-hand this tier,
  tier stands.
- Edges via counter formula first-hand: A head
  17/50 tail 35/50 b5set {50} NO step, 0 ff; C
  head 37/50 tail 49/50 b5set {50} NO step, 0
  ff; Q head 4b/50 tail c9/50 b5set {50} NO
  edge, 0 ff (b4 base 0x4b step2 64/64 range
  4b..c9, NO wrap); ring pre-edge off26
  (ff/50), edge off27 (01/51); edge off154
  (ff/51) -> off155 (01/52); exactly 2 ff in
  256; R head cb/50 tail c9/52; formulas
  re-derived from T10P358R code text (cb/50/27/
  155) + T10P358A/C/Q text (raw lencode); all
  edge pins + mid pin 141500 (off87) + tail
  141668 in for-list + 2 PASS lines each py+C.
  S0/S1 embedded b4/b5 (13/15 + 50) match raw
  lencode. Ring counter==raw-lencode 256/256 +
  Q 64/64 + A 16/16 + C 10/10. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT on cut
  bytes (edges466.py EDGES-GREEN, Q-range
  NO-wrap + range-with-wrap asserts verified
  first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0
  del (rgramc.c) + 231/0 (rgram.py) + 1/1
  (for-line) + 58/0 (PINS); raw C grep 603
  content + 5 bare-blank `+` lines (verified
  bare; 603+5 = 608 added lines) / C-file dels
  0; for-line replaced by superset (base
  for-N subset of band, removed 0); fine-norm
  equivalent (for465base.nums subset
  for466.nums, removed 0; C-scope del 0).
- Wall on band diff added lines (scope
  be565d02..5f800ba0, 898 added lines): vendor
  0 hits, disasm 0 hits, depload 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits; 2 `aea` substrings = PINS sha hex
  fragments (7bf4f255... + 5fbbadd9..., 0
  invocations -- same hex-fragment class as
  b464/b465). Files touched: rgramc.c 608/0,
  rgram.py 231/0 purely additive, test_rgram.sh
  1/1 (for-line extension), PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks,
  dispatch-guards singletons py-ind4 738->740
  (+2: 141321/141322) / ranges py-ind4 862->
  866 (+4; C singletons 743->745 +2 / ranges
  884->888 +4, same 6 P358 blocks both sides;
  no elif/else-if added either side: py
  file-wide elif 50 both, C else-if 0 both;
  deltas agree every side), CLOSED T10P prints
  2036->2042 +6 both sides, seal 2130->2136 +6
  (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
  Viewer-vs-sweep reconcile first-hand:
  GATE-tier absolutes 4sp-dispatch-exact (py
  738->740, ranges 862->866; C 743->745,
  ranges 884->888 -- all EXACT, no slip this
  band); file-wide unanchored py 748->750
  (+10 non-dispatch early-tier guards) + 5-
  count C-vs-py dip-guard offset; deltas
  +2/+4/+6 every method.
- CONFIRM evidence (CONVERT-01 rule b):
  A-945-q1070-P358 verdict CONFIRM 50/50 CLEAN
  (own bed r5-P358 141321..141696 + r5-P357
  cross-refs, BAD=0; verifier v501.py P358
  50/50 PASS; file present, counts verified;
  tier GATED PORT; novelty gated: M-tails 16/16
  ALL NEW vs P357T col-led tails; exact-value
  corroboration incl PB0 NEW-sig sigdiff-3
  31/84, PB1 NEW-sig 49/88, PBA16 sig-e0 VPOS
  8, C10 sig-1d DIFFERS-PB1 VPOS 5, QUAD64
  1-sig-NOEDGE + R1 rows + suffix-lcs-3/3/3/3/
  3/3 + R1-distinct + QM7 + NO frags + M-tails
  NEW, T256-SWAPPED + TM8-by-COL/TR7-by-ROW +
  SWAPPED-tails + const c13f2ba9 +
  counter/edges; plus const-count note: A-945
  excl 79/82/78/71 memo-exact, committed
  tables match excl exactly -- no writer lag
  this tier, geometry exact, PORT verdict
  stands). Agrees with cport commit msg (PYID
  10655, RGRAM 21310).
- FWD-check first-hand: A-945 "Next P359"
  forward notes verified against P359 lane code
  (6e01480c, git show, no checkout): PB0
  ada6a40c @141669 (168ch pay84) + PB1
  19000000 @141670 (176ch pay88) + PBA multi
  d4010000+d5010000 (guard 141671..141686, 16
  cells) + C10-region 19000000 x10 (guard
  141687..141696, 10 cells) -- all exact
  (banked for b467 CONSUME).
- Quiz: no conflicting CLAIM/GATE/FLAG on b466.
  Activity polled (no b466 conflict); PROSE-01
  re-read before filing (all hex/counts copied
  from run output above).
- Logs: NVME ws tmp/encode-viewer/r74/
  (build466.log, pyid466.log, rgram466py/c.log,
  cmp466.py, seteq466.py, ownloop466.py,
  secf466a/b/c.py, edges466.py, tabaudit466.py,
  w466loop.log, smoke466.log, units466.log,
  band diff via git).

Verdict: PASS. No RED. 348-pin contiguous range
141321..141668 sealed. Ready for viewer b467.
