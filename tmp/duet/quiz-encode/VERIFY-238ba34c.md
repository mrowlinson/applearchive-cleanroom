# VERIFY-238ba34c b461 T10P353 pins 139581..139928 (348 pins) PASS

Seat viewer-r73, first-hand, tree @238ba34c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r73.
Base 03dfc04c (b460 tip, 2100 tiers sealed; this
seat's VERIFY-03dfc04c PASS-filed same round,
base-use only, respected). Band = b50202d2 (py
merge w2b@b6ab031b partial, +6 tiers, +58 pins;
commit msg verified via git log) + 238ba34c (C
port; parent == b50202d2 verified via git
rev-list --parents). Chain b50202d2 parent ==
03dfc04c verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P353 shape (A-940 Q1 + Q-1065 agree)
CONSUMED FIRST and VERIFIED first-hand EXACT:
PB0 ede93f07 @139581 (S0 head; NEW-sig 34/84
diff vs P352PB0 @ n139233, sig b0-3 IN diff,
positions [0-5,11,19-31,36,37,60-71]
first-hand, NOT byte-equal) + PB1 0d000000
@139582 (S1 head; SAME-sig-as-P352PB1 57/88
diff, sig b0-3 NOT in diff, positions
[4,5,11,19,26-44,46-75,84-87] first-hand, NOT
byte-equal; 41/88 vs own C10[0] n139599,
SIG-EQ-own-C10; DIFFERS-vs-own-PB0 ed-vs-0d) +
PBA 9d000000 x16 @139583-598 (AC b0-3 =
9d/00/00/00; A-mtab b52,53,54,55,80-83) + C10-
region 0d000000 pay88 x10 @139599-608 (CC b0-3
= 0d/00/00/00, SAME-as-PB1-sig; CM lanes
b52,84,85,86,87 with b52 2-valued {92,b2}
first-hand) -- all corroborated against lane
code both sides before any battery step (no
bank-miss).

- Build: seat-private build461/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 784a8cf2...
  (8-char prefix == GATE; GATE states truncated
  prefix this band).
- RGRAMC-PYID 10510/10510 covered=10510/10510
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21020/21020 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21020/21020 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21020/21020, sorted +
  raw identical).
- PINS-RGRAM cells set-eq 10510/10510 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq461.py GREEN). PINS 21022 lines
  first-hand (2 hdr + 21020 rows; base 20964
  lines / 20962 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10481->10510 +29/-0 (python
  sets, trailing-';' strip, never comm): 139581
  139582 139583 139584 139590 139591 139597
  139598 139599 139600 139603 139604 139607
  139608 139609 139624 139640 139647 139648
  139656 139671 139672 139673 139775 139776
  139800 139903 139904 139928 (== GATE sampled
  list EXACT).
  29 = 2 sing (139581 139582) + A 6 (head
  139583 + 139584 + pair 139590/139591 + pair
  139597/139598 tail; offs 0,1,7,8,14,15; offs
  2-6,9-13 unsampled) + C 6 (head 139599 +
  139600 + 139603 + 139604 + 139607 + tail
  139608; offs 0,1,4,5,8,9; offs 2,3,6,7
  unsampled) + Q 8 (head 139609 + 139624 off15
  + 139640 off31 + edge pair 139647/139648
  off38/39 (b5 edge 42->43) + 139656 off47 +
  139671 off62 + tail 139672 off63; b5 steps,
  edge pair-covered, NO mid, first-hand) + R 7
  (head 139673 off0 + edge pair 139775/139776
  off102/103 + mid 139800 off127 + edge pair
  139903/139904 off230/231 + tail 139928 off255;
  1-mid shape off127, both counter edges
  pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21020-20962.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit461.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 156 PASS 0 FAIL first-run (0 seat-script
  fixes this band).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ede93f07 NEW-sig (34/84 payload
  diff vs P352S0, positions [0-5,11,19-31,36,
  37,60-71] first-hand, sig b0-3 IN diff, NOT
  byte-equal) / S1 176ch sig 0d000000 SAME-sig
  (57/88 payload diff vs P352S1, positions
  [4,5,11,19,26-44,46-75,84-87] first-hand, sig
  b0-3 NOT in diff, NOT byte-equal; vs own C10
  cells TRUE NON-UNIFORM [41,42x9] staged+
  oracle: cell0 41, cells1-9 42 (differ at b84
  only), identical within cells1-9, sig b0-3
  same-sig NOT in diff; NOT byte-equal; S1
  SIG-DIFFERS own PB0),
  staged as full-payload singletons.
  AM 16/16 8B distinct, CM 10/10 5B diverge
  (b52 2-valued mid-body M {92,b2} first-hand),
  M 16/16 8B distinct, QR 4/4 3B distinct
  UNPAIRED (R3 rows r0 7cf2fe / r1 bd00ff / r2
  dd00ff / r3 1c01ff exact tuples; full tails =
  R3 pairs + const b87 a8, 4/4 distinct;
  trailing-suffix = TSHARE = subseq-lcs =
  1/1/1/3/2/2 (all-3 agree first-hand; pairs
  share b87 const a8; pair (1,2) trailing 3,
  rest per log); tails 4 distinct),
  RM 16/16 7B distinct, RQ 16/16 8B distinct,
  no QT (R3 b84-86 inside QR + b87 const) + no
  RT (SPLIT tails) + no F (no frags). M-vs-RQ
  FULL8 (M 8B vs RQ 8B lanes [6,7,8,9]+tails
  both: rows element-wise 16/16, all 8 cols
  16/16 position-exact, full-row sets EQUAL,
  sorted rows equal; M list == RQ list) -- 48th
  odd-band RQ==M instance, EIGHTH full-identity
  degree (viewer chain: 12th full-identity survey;
  GATE cites no sweep number for this tier -- no
  scope collision); ordered per lesson (d)
  (full-row sets EQUAL); width predictor dead,
  never cited. AC 78, CC 81, QC 75, RC 71;
  C _N decls 78/81/75/71 match actual;
  byte-coverage unions exact every block
  (88/88/88/88, 0 overlap gap-free, M/R-tab
  computed; Q b85-87 consts in QC? b85,86 vary
  per R3 rows (in QR lane), b87 const a8 in QC
  first-hand). PBA88-PLAIN-M8b52 sig 9d000000
  (b0 const 9d via AC b0-3; AM 16/16 distinct NO
  pair; M8 b52,53,54,55,80-83; A-b5set {42}
  const first-hand).
  C10-1SIG-88-M5b52 sig 0d000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 full-sig
  consts; CM 10/10 diverge 5B b52,84-87 with b52
  2-valued; b5 const 42 full block via lencode).
  QUAD88-1SIG-QM8/R3-B5EDGE 1-sig dd000000 x64
  DIFFERS-from-PBA-sig (b0 const dd in QC, b1-3
  const 00; b5 STEPS 42->43 @off38/39 via raw
  lencode NOT in QC (in VPOS, varies -- 5th
  shape: Q-steps deduct); b4 base 0xb3 step2
  64/64 range 01..ff WITH wrap (off39 lands
  0x01; 64 distinct; exact arithmetic set
  {(0xb3+2k)} verified first-hand); QM7.../QM8
  b6,7,8,9,80-83 M 16/16 16ch distinct NO frags
  (m = off&15 both sides) shared-x3-vs-row0
  48/48 oracle (lanes 6-9,80-83; see tabaudit461
  shared-x3) NO frags + R3 b84,85,86 rows above
  4/4 UNPAIRED BY-ROW const (q = off>>4 both
  sides); tails 4 distinct (R3 pairs + b87 a8
  quad-wide); b87 const a8 quad-wide 64/64
  oracle (see edges461 qb87); NO frags).
  Ring STANDARD-split: sig b50d0000 x256;
  code-TM7 b13,15,16,80-83 by COL RM 16/16 +
  code-TR8 b6-9,76-79 by ROW RQ 16/16 UNPAIRED
  (SPLIT tails b80-83 col / b76-79 row); b0
  const b5 (256/256 oracle, in RC table); b1
  const 0d (256/256 oracle, in RC table); b14
  const bc gap (256/256 oracle, in RC table);
  b84-87 const 3c01ffa8 ring-wide NEW
  (256/256 oracle).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - 1; b4+M8, b5 const deducted) /
  C10 6 (missing 7 - 1; b4+M5, b5 const
  deducted) / quad 13 (missing 13 - 0; b4,b5+
  QM8+R3, b5 steps varies in VPOS, NO deduct --
  5th shape, cf P353 GATE) / T 17 (missing 17 -
  0; b4,b5+TM7+TR8, b0/b14 consts live
  in-table, deducted from VPOS) -- all match
  A-940 (missing sets AC-10
  [4,5,52-55,80-83] / CC-7 [4,5,52,84-87] /
  QC-13 [4,5,6-9,80-86] / RC-17
  [4,5,6-9,13,15,16,76-83]
  first-hand EXACT; deduct-const-b5-or-in-table
  convention holds incl the Q-steps 5th shape;
  b5 variance checked from oracle bytes: A {42},
  C {42}, Q {42,43} steps, T counter-varies).
  Code-consts vs A-940 INCL (PBA 79 / C10 82 /
  quad 75 / T88 71): impl 78/81/75/71 =
  memo-exact (A/C b5 const 42 deducted; Q
  steps, in VPOS; T counter, no deduction) =
  incl +2 for the two b5-const lanes; A-940 excl
  78/81/75/71 = code EXACT -- no lag on odd
  band (deduct-only-when-vary holds incl the
  Q-steps 5th shape). VPOS 9/6/13/17 = memo
  EXACT.
  M-tails 16/16 ALL NEW vs P352T RQ row-led
  tails (overlap 0; P352T RQ8 frame first-hand
  from code, ref = RQ8 8B rows, position-aware
  tails last-4B) + RQ-tails (b76-79) 16/16 ALL
  NEW vs P352T RM col-led tails (overlap 0;
  ref = RM9 9B rows).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P352
  (all 0/16; widths P353 vs P352: AM 8B vs 8B,
  CM 5B vs 4B, M 8B vs 8B, QR 3B vs 1B, RM 7B
  vs 9B, RQ 8B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 139581 / S1 139582 / A 139583-598 /
  C 139599-608 / Q 139609-672 / R 139673-928):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C b5 const emerges
  from raw lencode) + R explicit counter
  (b4=(0x33+2off)&FF b5=0x43+(off>=103)+
  (off>=231); py hex 0x33/0x43; C staged
  literals 51/67/103/231 re-derived: 51==0x33,
  67==0x43) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 8B b52-55,80-83; C 5B lane
  b52,84-87; Q 8B/3B b6-9,80-83/b84-86; R
  7B/8B STANDARD-split TM7 b13,15,16,80-83 by
  COL / TR8 b6-9,76-79 by ROW).
  C blocks carry T93740/T93745/T93750/T93765/
  T93780/T93800 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present; bounds + byte positions
  exact: A 8B, C 5B, Q 8B/3B, R 7B/8B STANDARD
  tails-split),
  A/C paylen 88 / raw lencode b4=(0x7f+2off) b5
  const 42 (A) / b4=(0x9f+2off) b5 const 42 (C,
  both const emerge from raw lencode);
  Q paylen 88 / raw lencode b4=(0xb3+2off) (b5
  step emerges from raw lencode 64/64);
  R paylen 88 +
  counter b4=(0x33+2off)&FF b5=0x43+(off>=103)+
  (off>=231) (C literals 51/67/103/231 verified),
  temps _t7101-7116 (base max _t7100, no reuse) +
  _i band 4307,4309,4312,4315 (base max _i4305,
  no reuse) + _b band 4306,4308,4310,4311,4313,
  4314 (base max _b4304, union 4306-4315
  contiguous, first-hand), all 6 blocks verified.
  Insert position exact both sides: after
  T10P352R close (C 249178 print + return, comment
  249181, S0 block; py CLOSED + return + S0 guard
  93740), at dispatch tail (N-out-of-scope
  fallthrough follows: C and py each 2 scope hits;
  early same-text guards at C 167867-line region
  / py 57911-line region are the T4 plateau-A
  n<=1076 check, unrelated scope -- verified
  first-hand same family as b460).
  Matches A-940 geometry (framing 1x84+347x88
  pay = code dispatch 1+1+16+10+64+256 = 348
  pins; PB0 NEW-sig 34/84 + PB1 SAME-sig 57/88
  + SAME-as-own-C10 41/88 +
  differs-vs-own-PB0,
  PBA88-PLAIN-M8b52 VPOS 9 b5 const 42,
  C10-1SIG-88-M5b52 VPOS 6 b5 const 42 b52
  2-valued,
  QUAD88-1SIG-QM8/R3-B5EDGE VPOS 13 =
  b4,b5+QM8+R3 + R3 4/4 UNPAIRED exact tuples +
  trailing 1/1/1/3/2/2 + b87 const +
  b5 edge @38/39 +
  M-tails ALL NEW 16/16,
  T88-RING-STANDARD-split sig b50d0000 TM7 by COL +
  TR8 by ROW UNPAIRED 16/16 + SPLIT tails +
  b84-87 const 3c01ffa8, ring edges + thresholds
  103/231, NO D dips) + A-940 (suffix-lcs
  1/1/1/3/2/2 = TAIL4 b84-87 all 3 metrics agree
  first-hand; consts excl 78/81/75/71 = lane
  EXACT).
- Edges own-loop ownloop461.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P353R N=139928 off=255.
  edges461.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0 embedded b4/b5
  7b/42, S1 7d/42 == raw lencode) + aform 16/16
  (A head 7f/42 tail 9d/42 b5set {42} NO step,
  0 ff) + cform 10/10 (C head 9f/42 tail b1/42
  b5set {42} NO step, 0 ff) + qform 64/64 (Q
  head b3/42 edge off38->39 (139647->139648)
  ff/42->01/43 tail 31/43 (139672), b5set
  {42,43}; quad b4=(0xb3+2off) 64/64 range
  01..ff WITH wrap (off39 lands 0x01),
...[truncated 3881 chars]
