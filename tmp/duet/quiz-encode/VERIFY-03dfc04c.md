# VERIFY-03dfc04c b460 T10P352 pins 139233..139580 (348 pins) PASS

Seat viewer-r73, first-hand, tree @03dfc04c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r73.
Base 4934f9d3 (b459 tip, 2094 tiers sealed; this
seat's VERIFY-4934f9d3 PASS-filed r72,
base-use only, respected). Band = f291211c (py
merge w2b@fc5f8a7d partial, +6 tiers, +58 pins;
commit msg verified via git log) + 03dfc04c (C
port; parent == f291211c verified via git
rev-list --parents). Chain f291211c parent ==
4934f9d3 verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P352 shape (A-938 Q1 + Q-1063 agree)
CONSUMED FIRST and VERIFIED first-hand EXACT:
PB0 ae40e406 @139233 (S0 head; SAME-sig-as-
P351PB0 31/84 diff, pay84 len-168, sig b0-3 NOT
in diff, NOT byte-equal) + PB1 0d000000 @139234
(S1 head; SAME-sig-as-P351PB1 80/88 diff, pay88
len-176, sig b0-3 NOT in diff, NOT byte-equal;
29/88 vs own C10[0] n139251, SIG-EQ-own-C10;
DIFFERS-vs-own-PB0 ae-vs-0d) + PBA b2000000 x16
@139235-250 (AC b0-3 = b2/00/00/00; A-mtab
b29,30,34,35,80-83) + C10-region 0d000000
pay88 x10 @139251-260 (CC b0-3 = 0d/00/00/00,
SAME-as-PB1-sig; pay88 verified first-hand per
cell, banked shape-change from pay92 noted) --
all corroborated against lane code both sides
before any battery step (no bank-miss).

- Build: seat-private build460/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 78397719...
  == GATE.
- RGRAMC-PYID 10481/10481 covered=10481/10481
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 20962/20962 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 20962/20962 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (20962/20962, sorted +
  raw identical).
- PINS-RGRAM cells set-eq 10481/10481 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq460.py GREEN). PINS 20964 lines
  first-hand (2 hdr + 20962 rows; base 20906
  lines / 20904 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10452->10481 +29/-0 (python
  sets, trailing-';' strip, never comm): 139233
  139234 139235 139236 139242 139243 139249
  139250 139251 139252 139255 139256 139259
  139260 139261 139262 139263 139264 139276
  139292 139308 139324 139325 139391 139392
  139450 139519 139520 139580 (== GATE sampled
  list EXACT).
  29 = 2 sing (139233 139234) + A 6 (head pair
  139235/139236 + pair 139242/139243 + tail pair
  139249/139250; offs 0,1,7,8,14,15; offs
  2-6,9-13 unsampled) + C 6 (head 139251/139252
  + mid pair 139255/139256 + tail pair
  139259/139260; offs 0,1,4,5,8,9; offs 2,3,6,7
  unsampled) + Q 8 (head 139261 + off1 139262 +
  EDGE pair 139263/139264 off2/3 (b5 edge
  3f->40) + 139276 off15 + 139292 off31 +
  139308 off47 + tail 139324 off63; b5 step,
  edge pair-covered, first-hand) + R 7 (head
  139325 off0 + edge pair 139391/139392 off66/67
  + mid 139450 off125 + edge pair 139519/139520
  off194/195 + tail 139580 off255; 1-mid shape
  off125, both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  20962-20904.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit460.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 153 PASS 0 FAIL 2nd full-green run
  (1st run caught the seat-script quad-VPOS
  deduct miss: b5 STEPS here (varies, in VPOS),
  so no deduct -- missing 11 = VPOS 11 = 2+8+1;
  fixed to len(QCm)==11, re-greened; lesson:
  re-derive deduct per band from code, never
  carry).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig ae40e406 SAME-sig-as-P351PB0
  (31/84 payload diff vs P351S0, positions
  [4-11,13,15-18,44-47,50,51,56-59,76-83]
  first-hand, sig b0-3 NOT in diff, NOT byte-
  equal) / S1 176ch sig 0d000000 SAME-sig-as-
  P351PB1 (80/88 payload diff vs P351S1,
  positions [4-55,60-87] first-hand, sig b0-3
  NOT in diff, NOT byte-equal; vs own C10 cells
  TRUE NON-UNIFORM [10x29] staged+oracle,
  all-10 identical positions [4,11,19,26-43,
  68-71,84-87], sig b0-3 same-sig NOT in diff;
  NOT byte-equal; S1 SIG-DIFFERS own PB0),
  staged as full-payload singletons.
  AM 16/16 16ch distinct, CM 10/10 8ch distinct,
  M 16/16 16ch distinct, QR 4/4 2ch distinct
  UNPAIRED (R1 rows 7b/9b/bb/db exact; full
  tails = R1 singles + const b85-87 2f3fd0,
  4/4 distinct; trailing-suffix = TSHARE =
  subseq-lcs = 3/3/3/3/3/3 (all-3 agree,
  first-hand); tails 4 distinct),
  RM 16/16 18ch distinct, RQ 16/16 16ch
  distinct, no QT (R1 b84 inside QR + b85-87
  const) + no RT (SPLIT tails) + no F (no
  frags). M-vs-RQ ORDERED-IDENTICAL (M 8B vs
  RQ 8B lanes [30,31,39,46,47,80-83 head-cols?
  -- first-hand: all 8 cols 16/16 position-
  exact, rows element-wise 16/16, full-row sets
  EQUAL, sorted rows equal; M list == RQ list)
  -- 47th even-band RQ==M instance,
  ORDERED-IDENTICAL degree (viewer chain: 11th
  full-identity survey; GATE cites no sweep
  number for this tier -- no scope collision);
  ordered per lesson (d) (full-row sets EQUAL);
  width predictor dead, never cited. AC 78, CC
  82, QC 77, RC 69; C _N decls 78/82/77/69
  match actual; byte-coverage unions exact every
  block (88/88/88/88, 0 overlap gap-free, M/R-tab
  computed; Q b85-87 const 2f3fd0 in QC? no --
  b85-87 in QC table as consts 2f/3f/d0
  first-hand). PBA88-PLAIN-M8b29 sig b2000000
  (b0 const b2 via AC b0-3; AM 16/16 distinct NO
  pair; M8 b29,30,34,35,80-83; A-b5set {3f}
  const first-hand).
  C10-1SIG-88-TAIL-M4 sig 0d000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 full-sig
  consts; CM 10/10 diverge 8ch b84-87; b5 const
  3f full block via lencode).
  QUAD88-1SIG-QM8/R1-B5EDGE 1-sig 9d000000 x64
  DIFFERS-from-PBA-sig (b0 const 9d in QC, b1-3
  const 00; b5 STEP 3f->40 @off3 via raw
  lencode NOT in QC (in VPOS, varies); b4 base
  0xfb step2 64/64 range fb..ff,01..79 wrap, 64
  distinct; QM8 b40-43,80-83 M 16/16 16ch
  distinct NO frags (m = off&15 both sides)
  shared-x3-vs-row0 48/48 oracle (lanes
  40-43,80-83; see tabaudit460 shared-x3) NO
  frags + R1 b84 rows above 4/4 UNPAIRED BY-ROW
  const (q = off>>4 both sides); tails 4
  distinct (R1 singles + b85-87 2f3fd0
  quad-wide); b85-87 const 2f3fd0 quad-wide
  64/64 oracle (see edges460 qb8587); NO
  frags).
  Ring STANDARD-split: sig 9d0d0000 x256;
  code-TM9 b30,31,39,46,47,80-83 by COL RM 16/16 +
  code-TR8 b40-43,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79
  row); b0 const 9d (256/256 oracle, in RC
  table, deducted from VPOS); b1 const 0d
  (256/256 oracle, in RC table); b84-87 const
  fb2f3fd0 ring-wide NEW (256/256 oracle).
  VPOS partitions re-derived from code: PBA 9
  (missing 10 - 1; b4+M8, b5 const deducted) /
  C10 5 (missing 6 - 1; b4+M4, b5 const
  deducted) / quad 11 (missing 11 - 0; b4,b5+
  QM8+R1, b5 steps varies in VPOS, NO deduct --
  even-band step shape, cf P352 GATE) / T 19
  (missing 19 - 0; b4,b5+TM9+TR8, b0 const
  lives in-table, deducted from VPOS) -- all
  match A-939 (missing sets AC-10
  [4,5,29,30,34,35,80-83] / CC-6
  [4,5,84-87] / QC-11
  [4,5,40-43,80-84] / RC-19
  [4,5,30,31,39-43,46,47,76-83]
  first-hand EXACT; deduct-const-b5-or-in-table
  convention holds; b5 variance checked from
  oracle bytes: A {3f}, C {3f}, Q {3f,40}
  steps, T counter-varies).
  Code-consts vs A-939 INCL (PBA 80 / C10 84 /
  quad 77 / T88 69): impl 78/82/77/69 =
  memo-exact (A/C b5 const 3f deducted; T
  counter, no deduction; Q step-varies, in
  VPOS, no deduction) = incl +2/+2 for the two
  b5-const lanes; A-939 excl 78/82/77/69 = code
  EXACT -- lag on evens (deduct-only-when-vary
  holds). VPOS 9/5/11/19 = memo EXACT.
  M-tails 16/16 ALL NEW vs P351T RQ row-led
  tails (overlap 0; P351T RQ7 frame first-hand
  from code, ref = RQ7 7B rows, position-aware
  tails last-4B) + RQ-tails (b76-79) 16/16 ALL
  NEW vs P351T RM col-led tails (overlap 0;
  ref = RM7 7B rows).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P351
  (all 0/16; widths P352 vs P351: AM 8B vs 6B,
  CM 4B vs 4B, M 8B vs 7B, QR 1B vs 3B, RM 9B
  vs 7B, RQ 8B vs 7B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 139233 / S1 139234 / A 139235-250 /
  C 139251-260 / Q 139261-324 / R 139325-580):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C b5 const emerges
  from raw lencode) + R explicit counter
  (b4=(0x7b+2off)&FF b5=0x40+(off>=67)+
  (off>=195); py hex 0x7b/0x40; C staged
  literals 123/64/67/195 re-derived: 123==0x7b,
  64==0x40) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 8B b29,30,34,35,80-83; C
  4B lane b84-87; Q 8B/1B b40-43,80-83/b84; R
  9B/8B STANDARD-split TM9 b30,31,39,46,47,80-83
  by COL / TR8 b40-43,76-79 by ROW).
  C blocks carry T93509/93514/93519/93534/
  93549/93568 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present; bounds + byte positions
  exact: A 8B, C 4B, Q 8B/1B, R 9B/8B
  STANDARD-split tails),
  A/C/Q raw lencode (no counter literals) + R
  counter b4=(0x7b+2off)&FF + (off>=67)+(off>=195)
  (C literals 123/64/67/195 verified), temps
  _t7085-7100 (base max _t7084, no reuse) +
  _i4297/4299/4302/4305 (base max _i4295, no
  reuse) + _b4296/4298/4300/4301/4303/4304 (base
  max _b4294, no reuse; union 4296-4305
  contiguous, first-hand), all 6 blocks verified.
  Insert position exact both sides: after
  T10P351R close (C comment + S0 block; py
  CLOSED + return + S0 guard 93509), at dispatch
  tail (N-out-of-scope fallthrough follows: C
  248753 + py 93588; early same-text guards at C
  167867 / py 57911 are the T4 plateau-A
  n<=1076 check, unrelated scope -- line text
  verified first-hand).
  Matches A-939 geometry (framing 1x84+347x88
  pay = code dispatch 1+1+16+10+64+256 = 348
  pins; PB0 SAME-sig 31/84 + PB1 SAME-sig 80/88
  + SAME-as-own-C10 29/88 + differs-vs-own-PB0;
  PBA88-PLAIN-M8b29 VPOS 9 b5 const 3f; C10-
  1SIG-88-TAIL-M4 VPOS 5 b5 const 3f;
  QUAD88-1SIG-QM8/R1-B5EDGE VPOS 11 + R1 4/4
  UNPAIRED 7b/9b/bb/db + trailing 3/3/3/3/3/3
  + b85-87 const + b5 step + M-tails NEW 16/16;
  T88-STANDARD-split VPOS 19 + TM9-by-COL/TR8-
  by-ROW + SPLIT-tails + b0-const-in-table +
  b84-87 fb2f3fd0 + counter 7b/40/67/195;
  lencode 348/348 whole-tier, NO D dips)
  + A-939 (suffix-lcs 3/3/3/3/3/3 = TAIL4 b84-87
  all 3 metrics agree first-hand; consts excl
  78/82/77/69 = lane EXACT).
- Edges own-loop ownloop460.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warm
...[truncated 4471 chars]
