# VERIFY-05398fc3 b462 T10P354 pins 139929..140276 (348 pins) PASS

Seat viewer-r73, first-hand, tree @05398fc3,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r73.
Base 238ba34c (b461 tip, 2106 tiers sealed; this
seat's VERIFY-238ba34c PASS-filed same round,
base-use only, respected). Band = f4bcf794 (py
merge w2b@2c691567 partial, +6 tiers, +58 pins;
commit msg verified via git log) + 05398fc3 (C
port; parent == f4bcf794 verified via git
rev-list --parents). Chain f4bcf794 parent ==
238ba34c verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P354 shape (A-941 Q1 + Q-1066 agree)
CONSUMED FIRST and VERIFIED first-hand EXACT:
PB0 ede93f07 @139929 (S0 head; SAME-sig-as-
P353PB0 33/84 diff, sig b0-3 NOT in diff,
positions [4,5,32-55,72-79] first-hand, NOT
byte-equal) + PB1 0e000000 @139930 (S1 head;
NEW-sig 60/88 diff vs P353PB1, sig b0 IN diff,
positions
[0,4-7,9-14,16-25,28-31,36-43,45-59,76-87]
first-hand, NOT byte-equal; 29/88 vs own C10[0]
n139947, SIG-EQ-own-C10; DIFFERS-vs-own-PB0
ed-vs-0e) + PBA e3000000 x16 @139931-946 (AC
b0-3 = e3/00/00/00; A-mtab b20,21,80-83) + C10-
region 0e000000 pay88 x10 @139947-956 (CC b0-3
= 0e/00/00/00, SAME-as-PB1-sig; CM lanes
b22,84,85,86,87 with b22 2-valued {f3,fb}
first-hand) -- all corroborated against lane
code both sides before any battery step (no
bank-miss).

- Build: seat-private build462/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 f7f5b9aa...
  == GATE (full-sha match).
- RGRAMC-PYID 10539/10539 covered=10539/10539
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21078/21078 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21078/21078 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21078/21078, sorted +
  raw identical).
- PINS-RGRAM cells set-eq 10539/10539 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq462.py GREEN). PINS 21080 lines
  first-hand (2 hdr + 21078 rows; base 21022
  lines / 21020 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10510->10539 +29/-0 (python
  sets, trailing-';' strip, never comm): 139929
  139930 139931 139932 139938 139939 139945
  139946 139947 139948 139951 139952 139955
  139956 139957 139972 139973 139988 139989
  140004 140005 140020 140021 140030 140031
  140032 140159 140160 140276 (== GATE sampled
  list EXACT).
  29 = 2 sing (139929 139930) + A 6 (head pair
  139931/139932 + pair 139938/139939 + tail pair
  139945/139946; offs 0,1,7,8,14,15; offs
  2-6,9-13 unsampled) + C 6 (head 139947/139948
  + mid pair 139951/139952 + tail pair
  139955/139956; offs 0,1,4,5,8,9; offs 2,3,6,7
  unsampled) + Q 8 (head 139957 off0 + 139972
  off15 + 139973 off16 + pair 139988/139989
  off31/32 + pair 140004/140005 off47/48 + tail
  140020 off63; b5 const 45 NO edge, NO mid,
  all boundaries pair-covered, first-hand) + R 7
  (head 140021 off0 + pre-edge 140030 off9 +
  edge pair 140031/140032 off10/11 + edge pair
  140159/140160 off138/139 + tail 140276 off255;
  2-edge shape, both counter edges pair-covered,
  pre-edge pinned, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21078-21020.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit462.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 154 PASS 0 FAIL first-run (0
  seat-script fixes this band).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ede93f07 SAME-sig-as-P353PB0
  (33/84 payload diff vs P353S0, positions
  [4,5,32-55,72-79] first-hand, sig b0-3 NOT in
  diff, NOT byte-equal) / S1 176ch sig 0e000000
  NEW-sig (60/88 payload diff vs P353S1,
  positions
  [0,4-7,9-14,16-25,28-31,36-43,45-59,76-87]
  first-hand, sig b0 IN diff, NOT byte-equal; vs
  own C10 cells TRUE NON-UNIFORM [10x29] staged+
  oracle, all-10 identical positions
  [4,8-31,60-63,84-87], sig b0-3 same-sig NOT in
  diff; NOT byte-equal; S1 SIG-DIFFERS own
  PB0),
  staged as full-payload singletons.
  AM 16/16 6B distinct, CM 10/10 5B diverge
  (b22 2-valued mid-body M {f3,fb} first-hand),
  M 16/16 7B distinct, QR 4/4 2B distinct
  UNPAIRED (R2 rows r0 d9a9 / r1 f9a9 / r2 19aa
  / r3 39aa exact tuples; full tails = R2 pairs
  + const b86 da / b87 09, 4/4 distinct;
  trailing-suffix = subseq-lcs = 3/2/2/2/2/3
  (agree first-hand; tshare printed in log);
  tails 4 distinct),
  RM 16/16 9B distinct, RQ 16/16 7B distinct,
  no QT (R2 b84,85 inside QR + b86/b87 consts) +
  no RT (SPLIT tails) + no F (no frags). M-vs-RQ
  ORDERED-IDENTICAL (M 7B vs RQ 7B lanes
  [28,29,30,76-83 head? -- first-hand: all 7
  cols 16/16 position-exact, rows element-wise
  16/16, full-row sets EQUAL, sorted rows equal;
  M list == RQ list) -- 48th even-band RQ==M
  instance, ORDERED-IDENTICAL degree (viewer
  chain: 13th full-identity survey; GATE cites no
  sweep number for this tier -- no scope
  collision); ordered per lesson (d) (full-row
  sets EQUAL); width predictor dead, never
  cited. AC 80, CC 81, QC 77, RC 70; C _N decls
  80/81/77/70 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; Q b85 const in?
  -- b85 varies per R2 rows (in QR lane), b86/b87
  consts da/09 in QC table first-hand).
  PBA88-PLAIN-M6b20 sig e3000000 (b0 const e3
  via AC b0-3; AM 16/16 distinct NO pair; M6
  b20,21,80-83; A-b5set {45} const first-hand).
  C10-1SIG-88-M5b22 sig 0e000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 full-sig
  consts; CM 10/10 diverge 5B b22,84-87 with b22
  2-valued; b5 const 45 full block via lencode).
  QUAD88-1SIG-QM7/R2-NOEDGE 1-sig e3000000 x64
  SAME-sig-as-PBA (b0 const e3 in QC, b1-3
  const 00; b5 const 45 deducted to raw lencode
  NO edge; b4 base 0x6b step2 64/64 range
  6b..e9 NO wrap, 64 distinct; QM7
  b28,29,30,80-83 M 16/16 14ch distinct NO
  frags (m = off&15 both sides) shared-x3-vs-
  row0 48/48 oracle (lanes 28-30,80-83; see
  tabaudit462 shared-x3) NO frags + R2 b84,85
  rows above 4/4 UNPAIRED BY-ROW const
  (q = off>>4 both sides); tails 4 distinct (R2
  pairs + b86 da + b87 09 quad-wide); b86/b87
  consts da/09 quad-wide 64/64 oracle (see
  edges462 qb8687); NO frags).
  Ring 2SIG-COLSPLIT: sigs 140f0000 x160 +
  150f0000 x96 (b0 = 14 iff col<10 else 15
  first-hand per-col 160/96 exact); code-TM9
  b0,19,27,34,35,80-83 by COL RM 16/16 +
  code-TR7 b28,29,30,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79 row);
  b0 varies in TM9 COL lane (in VPOS, in
  missing); b1 const 0f (256/256 oracle, in RC
  table); b84-87 const 98ad080d ring-wide NEW
  (256/256 oracle).
  VPOS partitions re-derived from code: PBA 7
  (missing 8 - 1; b4+M6, b5 const deducted) /
  C10 6 (missing 7 - 1; b4+M5, b5 const
  deducted) / quad 10 (missing 11 - 1; b4+QM7+
  R2, b5 const deducted) / T 18 (missing 18 -
  0; b4,b5+TM9+TR8, b0 varies in TM9 COL lane
  in VPOS) -- all match A-941 (missing sets
  AC-8 [4,5,20,21,80-83] / CC-7
  [4,5,22,84-87] / QC-11
  [4,5,28-30,80-85] / RC-18
  [0,4,5,19,27-30,34,35,76-83]
  first-hand EXACT; deduct-const-b5-or-in-table
  convention holds; b5 variance checked from
  oracle bytes: A {45}, C {45}, Q {45} const, T
  counter-varies).
  Code-consts vs A-941 INCL (PBA 81 / C10 82 /
  quad 78 / T88 70): impl 80/81/77/70 =
  memo-exact (A/C/Q b5 const 45 deducted; T
  counter, no deduction) = incl +1/+1/+1 for
  the three b5-const lanes; A-941 excl
  80/81/77/70 = code EXACT -- lag on evens
  (deduct-only-when-vary holds). VPOS 7/6/10/18
  = memo EXACT.
  M-tails 16/16 ALL NEW vs P353T RM col-led
  tails (overlap 0; P353T RM7 frame first-hand
  from code, ref = RM7 7B rows, position-aware
  tails last-4B) + RQ-tails (b76-79) 16/16 ALL
  NEW vs P353T RQ row-led tails (overlap 0;
  ref = RQ8 8B rows).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P353
  (all 0/16; widths P354 vs P353: AM 6B vs 8B,
  CM 5B vs 5B, M 7B vs 8B, QR 2B vs 3B, RM 9B
  vs 7B, RQ 7B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 139929 / S1 139930 / A 139931-946 /
  C 139947-956 / Q 139957-020 / R 140021-276):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C/Q b5 const emerges
  from raw lencode) + R explicit counter
  (b4=(0xeb+2off)&FF b5=0x45+(off>=11)+
  (off>=139); py hex 0xeb/0x45; C staged
  literals 235/69/11/139 re-derived: 235==0xeb,
  69==0x45) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides (c/r colsplit-aware: b0 =
  14 iff col<10 else 15 first-hand 160/96) +
  mtab/rtab byte positions exact (A 6B
  b20,21,80-83; C 5B lane b22,84-87; Q 7B/2B
  b28-30,80-83/b84,85; R 9B/7B COLSPLIT TM9
  b0,19,27,34,35,80-83 by COL / TR7
  b28-30,76-79 by ROW).
  C blocks carry T93972/T93977/T93982/T93997/
  T94012/T94032 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present; bounds + byte positions
  exact: A 6B, C 5B, Q 7B/2B, R 9B/7B COLSPLIT
  tails-split),
  A/C/Q raw lencode (no counter literals) + R
  counter b4=(0xeb+2off)&FF + (off>=11)+(off>=139)
  (C literals 235/69/11/139 verified), temps
  _t7117-7132 (base max _t7116, no reuse) +
  _i4317/4319/4322/4325 (base max _i4315, no
  reuse) + _b4316/4318/4320/4321/4323/4324 (base
  max _b4314, no reuse; union 4316-4325
  contiguous, first-hand), all 6 blocks verified.
  Insert position exact both sides: after
  T10P353R close (C comment + S0 block; py
  CLOSED + return + S0 guard 93972), at dispatch
  tail (N-out-of-scope fallthrough follows: C and
  py each 2 scope hits; early same-text guards
  are the T4 plateau-A n<=1076 check, unrelated
  scope -- same family as b460/b461, verified
  first-hand via scope-hit counts).
  Matches A-941 geometry (framing 1x84+347x88
  pay = code dispatch 1+1+16+10+64+256 = 348
  pins; PB0 SAME-sig 33/84 + PB1 NEW-sig 60/88
  + SAME-as-own-C10 29/88 + differs-vs-own-PB0;
  PBA88-PLAIN-M6b20 VPOS 7 b5 const 45;
  C10-1SIG-88-M5b22 VPOS 6 b5 const 45 b22
  2-valued;
  QUAD88-1SIG-QM7/R2-NOEDGE VPOS 10 + R2 4/4
  UNPAIRED d9a9/f9a9/19aa/39aa + trailing
  3/2/2/2/2/3 + b86/b87 consts + b5 const NO
  edge + M-tails ALL NEW 16/16;
  T88-2SIG-COLSPLIT VPOS 18 + TM9-by-COL/TR7-
  by-ROW + SPLIT-tails + b0-varies-in-TM9 +
  b84-87 98ad080d + counter eb/45/11/139;
  lencode 348/348 whole-tier, NO D dips)
  + A-941 (suffix-lcs 3/2/2/2/2/3 = TAIL4 b84-87
  suffix+subseq agree first-hand; consts excl
  80/81/77/70 = lane EXACT).
- Edges own-loop ownloop462.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P354R N=140276 off=255.
  edges462.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0 embedded b4/b5
  33/45, S
...[truncated 4471 chars]
