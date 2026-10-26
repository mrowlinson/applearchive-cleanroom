# VERIFY-3d07ab9f b463 T10P355 pins 140277..140624 (348 pins) PASS

Seat viewer-r73, first-hand, tree @3d07ab9f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r73.
Base 05398fc3 (b462 tip, 2112 tiers sealed; this
seat's VERIFY-05398fc3 PASS-filed same round,
base-use only, respected). Band = 4b86c220 (py
merge w2b@c20cad6d partial, +6 tiers, +58 pins;
commit msg verified via git log) + 3d07ab9f (C
port; parent == 4b86c220 verified via git
rev-list --parents). Chain 4b86c220 parent ==
05398fc3 verified, NO gap-jump (every sha via
git log at takeover).
Trees via git archive to TMPDIR tree-sha dirs;
tests run from NVME workdirs (no WT src/
__pycache__).

Banked Next-P355 shape (A-942 Q1 + Q-1067 agree)
CONSUMED FIRST and VERIFIED first-hand EXACT:
PB0 aefa6007 @140277 (S0 head; NEW-sig-3B-off
31/84 diff vs P354PB0 @ n139929, b0-2 IN diff
with b3 same, positions
[0-2,4-7,9-11,13-19,24,25,56-63,80-83]
first-hand, NOT byte-equal) + PB1 0f000000
@140278 (S1 head; NEW-sig 51/88 diff vs P354PB1
@ n139930, sig b0 IN diff, positions
[0,4,5,8-11,16-43,60-71,84-87] first-hand, NOT
byte-equal; 27/88 vs own C10[0] n140295,
SIG-EQ-own-C10; DIFFERS-vs-own-PB0 ae-vs-0f) +
PBA f5000000 x16 @140279-294 (AC b0-3 =
f5/00/00/00; A-mtab b40-43,80-83) + C10-region
0f000000 pay88 x10 @140295-304 (CC b0-3 =
0f/00/00/00, SAME-as-PB1-sig; CM lanes
b84,85,86 with b87 const 0x41 in CC; CM row
b84-86 diverge 3B) -- all corroborated against
lane code both sides before any battery step (no
bank-miss).

- Build: seat-private build463/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues; band touches no aae
  sources per numstat). rgramc sha256 2b0eaff2...
  (8-char prefix == GATE; GATE states truncated
  prefix this band).
- RGRAMC-PYID 10568/10568 covered=10568/10568
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch,
  CT_CACHE_DIR default NVME).
- RGRAM py 21136/21136 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 21136/21136 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (21136/21136, sorted +
  raw identical).
- PINS-RGRAM cells set-eq 10568/10568 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq463.py GREEN). PINS 21138 lines
  first-hand (2 hdr + 21136 rows; base 21080
  lines / 21078 rows; line delta +58 = row delta
  +58 = 29 for-Ns x2).
  For-list union 10539->10568 +29/-0 (python
  sets, trailing-';' strip, never comm): 140277
  140278 140279 140280 140287 140288 140293
  140294 140295 140296 140299 140300 140303
  140304 140305 140320 140321 140336 140337
  140352 140353 140368 140369 140415 140416
  140480 140543 140544 140624 (== GATE sampled
  list EXACT).
  29 = 2 sing (140277 140278) + A 6 (head
  140279 + 140280 + edge pair 140287/140288
  off8/9 (b5 edge 47->48) + pair 140293/140294
  tail; offs 0,1,8,9,14,15; offs 2-7,10-13
  unsampled) + C 6 (head 140295 + 140296 +
  140299 + 140300 + 140303 + tail 140304; offs
  0,1,4,5,8,9; offs 2,3,6,7 unsampled) + Q 8
  (head 140305 + boundary pairs 140320/140321 +
  140336/140337 + 140352/140353 + tail 140368;
  offs 0,15,16,31,32,47,48,63; NO mid (b5 const
  NO edge), all boundaries pair-covered,
  first-hand) + R 7 (head 140369 + edge pair
  140415/140416 off46/47 + mid 140480 off111 +
  edge pair 140543/140544 off174/175 + tail
  140624 off255; 1-mid shape off111 NEW, both
  counter edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  21136-21078.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes +
  aea encrypt/decrypt/bytes PASS, default oracle
  backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  synthetic shape tests, no oracle).
- Tables audit own script tabaudit463.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 156 PASS 0 FAIL first-run (0
  seat-script fixes this band).
  Inventory exactly the 12 both sides (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT, no F0/F1,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM, no RT/TT, no QT).
  S0 168ch sig aefa6007 NEW-sig-3B-off (31/84
  payload diff vs P354S0, positions
  [0-2,4-7,9-11,13-19,24,25,56-63,80-83]
  first-hand, b0-2 IN diff with b3 same, NOT
  byte-equal) / S1 176ch sig 0f000000 NEW-sig
  (51/88 payload diff vs P354S1, positions
  [0,4,5,8-11,16-43,60-71,84-87] first-hand,
  sig b0 IN diff vs P354S1 0e000000, NOT
  byte-equal; vs own C10 cells TRUE UNIFORM
  [10x27] staged+oracle: all-10 identical
  positions
  [4,5,19,26,27,34-47,72-75,84-87], sig b0-3
  same-sig NOT in diff; NOT byte-equal; S1
  SIG-EQ own C10; S1 SIG-DIFFERS own PB0),
  staged as full-payload singletons.
  AM 16/16 8B distinct, CM 10/10 3B diverge,
  M 16/16 8B distinct, QR 4/4 2B distinct
  UNPAIRED (R2 rows r0 456e / r1 e46e / r2 046f
  / r3 246f exact tuples; full tails = R2 pairs
  + b86 const 0x59 + b87 const 0x41, 4/4
  distinct; trailing-suffix = TSHARE =
  subseq-lcs = 3/2/2/2/2/3 (all-3 agree
  first-hand); tails 4 distinct),
  RM 16/16 8B distinct, RQ 16/16 8B distinct,
  no QT (R2 b84,85 inside QR + b86/b87 consts)
  + no RT (SPLIT tails) + no F (no frags).
  M-vs-RQ 4OF8 (M 8B lanes [38,39,46,47]+tails
  both vs RQ 8B lanes [40,41,46,47,76-79]:
  heads cols 0-3 0/16 position-exact each,
  col-set overlaps 0/0/0/0 (fully disjoint);
  tails cols 4-7 16/16 position-exact each,
  tail-sets EQUAL; full-row sets DISJOINT
  (intersect 0); M list != RQ list) -- 49th
  odd-band RQ==M instance, FIRST 4OF8 degree (no
  precedent on file; viewer chain: 14th
  full-identity survey); ordered per lesson (d)
  (tails position-exact + tail-sets EQUAL +
  rows DISJOINT, same-width 8B/8B); width
  predictor dead, never cited;
  tails STANDARD-split (TM b52-55,80-83 by COL
  c=off&15, TR b40,41,46,47,76-79 by ROW
  r=off>>4, 16/16 distinct each, sequences
  UNPAIRED);
  M-tails 16/16 ALL NEW vs P354T RQ row-led
  tails (overlap 0; P354T RQ7 frame first-hand
  from code, ref = RQ7 7B rows, position-aware
  tails last-4B);
  RQ-tails (b76-79) 16/16 ALL NEW vs P354T RM
  col-led tails (overlap 0; P354T RM9 frame
  first-hand from code);
  AC 78, CC 83, QC 76, RC 70; C _N decls
  78/83/76/70 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap
  gap-free, M/R-tab computed; Q b85 varies per
  R2 rows (in QR lane), b86/b87 consts 59/41 in
  QC table first-hand; C b87 const 41 in CC
  first-hand).
  PBA88-PLAIN-M8b40 sig f5000000 (b0 const f5
  via AC b0-3; AM 16/16 distinct NO pair; M8
  b40-43,80-83; b5 0x47+(off>=9) edge
  140287->140288 -- A-steps 6th shape).
  C10-1SIG-88-TAIL-M3 sig 0f000000 x10
  SAME-as-PB1-sig (full sig b0-3 in CC =
  0f000000; CM 10/10 diverge 3B b84-86; b87
  const 0x41 in CC; b5 const 48 NO step NO
  edge).
  QUAD88-1SIG-QM8/R2-NOEDGE 1-sig f5000000 x64
  SAME-sig-as-PBA (b0 const f5 in QC, b1-3
  const 00; b5 const 48 full block via lencode;
  b4 base 0x23 step2 64/64 range 23..a1 NO
  wrap, 64 distinct; QM8 b38,39,46,47,80-83 M
  16/16 8B distinct NO frags (m = off&15 both
  sides) shared-x3-vs-row0 48/48 oracle (lanes
  38,39,46,47,80-83; see tabaudit463 shared-x3)
  NO frags + R2 b84,85 rows above 4/4 UNPAIRED
  BY-ROW const (q = off>>4 both sides); tails 4
  distinct (R2 pairs + b86 59 + b87 41
  quad-wide); b86/b87 consts 59/41 quad-wide
  64/64 oracle (see edges463 qb8687); NO
  frags).
  Ring STANDARD-split: sig 750b0000 x256;
  code-TM8 b52-55,80-83 by COL RM 16/16 +
  code-TR8 b40,41,46,47,76-79 by ROW RQ 16/16
  UNPAIRED (SPLIT tails b80-83 col / b76-79 row);
  b0 const 75 (256/256 oracle, in RC table);
  b1 const 0b (256/256 oracle, in RC table);
  b84-87 const 446f5941 ring-wide NEW
  (256/256 oracle).
  VPOS partitions re-derived from code: PBA 10
  (missing 10 - 0; b4,b5-step+M8, b5 steps
  varies in VPOS, NO deduct -- 6th shape, cf
  P355 GATE) / C10 4 (missing 5 - 1; b4+M3,
  b5 const deducted) / quad 11 (missing 12 - 1;
  b4+QM8+R2, b5 const deducted) / T 18 (missing
  18 - 0; b4,b5+TM8+TR8, b0/b1 consts live
  in-table) -- all match A-942 (missing sets
  AC-10 [4,5,40-43,80-83] / CC-5 [4,5,84-86] /
  QC-12 [4,5,38,39,46,47,80-85] / RC-18
  [4,5,40,41,46,47,52-55,76-83]
  first-hand EXACT; deduct-const-b5-or-in-table
  convention holds incl the A-steps 6th shape;
  b5 variance checked from oracle bytes: A
  {47,48} steps, C {48} const, Q {48} const, T
  counter-varies).
  Code-consts vs A-942 INCL (PBA 78 / C10 84 /
  quad 77 / T88 70): impl 78/83/76/70 =
  memo-exact (C/Q b5 const 48 deducted; A steps,
  in VPOS; T counter, no deduction) = incl +1/+1
  for the two b5-const lanes; A-942 excl
  78/83/76/70 = code EXACT -- no lag on odd
  band (deduct-only-when-vary holds incl the
  A-steps 6th shape). VPOS 10/4/11/18 = memo
  EXACT.
  M-tails 16/16 ALL NEW vs P354T RQ row-led
  tails (overlap 0; P354T RQ7 frame first-hand
  from code, ref = RQ7 7B rows, position-aware
  tails last-4B);
  RQ-tails (b76-79) 16/16 ALL NEW vs P354T RM
  col-led tails (overlap 0; P354T RM9 frame
  first-hand from code).
  AM/CM/M/QR/RM/RQ full-row 0-overlap vs P354
  (all 0/16; widths P355 vs P354: AM 8B vs 6B,
  CM 3B vs 5B, M 8B vs 7B, QR 2B vs 2B, RM 8B
  vs 9B, RQ 8B vs 7B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 140277 / S1 140278 / A 140279-294 /
  C 140295-304 / Q 140305-368 / R 140369-624):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A b5 step emerges from
  raw lencode + b4 formula; C/Q b5 const emerges
  from raw lencode) + R explicit counter
  (b4=(0xa3+2off)&FF b5=0x48+(off>=47)+
  (off>=175); py hex 0xa3/0x48; C staged
  literals 163/72/47/175 re-derived: 163==0xa3,
  72==0x48) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte
  positions exact (A 8B b40-43,80-83; C 3B lane
  b84-86 + b87 const; Q 8B/2B b38,39,46,47,
  80-83/b84,85; R 8B/8B STANDARD-split TM8
  b52-55,80-83 by COL / TR8 b40,41,46,47,76-79
  by ROW).
  C blocks carry T94205/T94210/T94215/T94230/
  T94245/T94265 py-line cites (each re-read: hits
  the exact py guard line, C comment text matches
  py, all 6 present; bounds + byte positions
  exact: A 8B, C 3B+const, Q 8B/2B, R 8B/8B
  STANDARD tails-split),
  A paylen 88 / raw lencode b4=(0xef+2off) b5
  0x47+(off>=9) edge 140287->140288 (C comment
  carries formula; A-block asserts lencode,
  step verified via oracle edges) / C paylen 88
  / raw lencode b4=(0x0f+2off) b5 const 48 (C,
  const emerges from raw lencode);
  Q paylen 88 / raw lencode b4=(0x23+2off) (b5
  const emerges from raw lencode 64/64);
  R paylen 88 +
  counter b4=(0xa3+2off)&FF b5=0x48+(off>=47)+
  (off>=175) (C literals 163/72/47/175 verified),
  temps _t7133-7148 (base max _t7132, no reuse) +
  _i band 4327,4329,4332,4335 (base max _i4325,
  no reuse) + _b band 4326,4328,4330,4331,4333,
  4334 (base max _b4324, union 4326-4335
  contiguous, first-hand), all 6 blocks verified.
  Insert position exact both sides: after
  T10P354R close (C comment + S0 block; py
  CLOSED + return + S0 guard 94205), at dispatch
  tail (N-out-of-scope fallthrough follows: C and
  py each 2 scope hits; early same-text guards
  are the T4 plateau-A n<=1076 check, unrelated
  scope -- same family as b460-b462, verified
  via scope-hit counts).
  Matches A-942 geometry (framing 1x84+347x88
  pay = code dispatch 1+1+16+10+64+256 = 348
  pins; PB0 NEW-3B-off 31/84 + PB1 NEW-sig 51/88
  + SAME-as-own-C10 27/88 + differs-vs-own-PB0;
  PBA88-PLAIN-M8b40 VPOS 10 b5 edge @8/9,
  C10-1SIG-88-TAIL-M3 VPOS 4 b5 const 48,
  QUAD88-1SIG-QM8/R2-NOEDGE VPOS 11 =
  b4+QM8+R2 (b5 const) + R2 4/4 UNPAIRED exact
  tuples + trailing 3/2/2/2/2/3 + b86/b87 consts
  + b5 const NO edge + M-tails ALL NEW 16/16;
  T88-RING-STANDARD-split sig 750b0000 TM8 by
  COL + TR8 by ROW UNPAIRED 16/16 + SPLIT tails
  + b84-87 const 446f5941, ring edges + thresholds
  47/175, NO D dips) + A-942 (suffix-lcs
  3/2/2/2/2/3 = TAIL4 b84-87 all 3 metrics agree
  first-hand; consts excl 78/83/76/70 = lane
  EXACT).
- Edges own-loop ownloop463.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P355R N=140624 off=255.
  edges463.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0 embedded b4/b5
  eb/47, S1 ed/47 == raw lencode) + aform 16/16
  (A head ef/47 edge off8->9 (140287->140288)
  ff/47->01/48 tail 0d/48, b5set {47,48}) +
  cform 10/10 (C head 0f/48 tail 21/48 b5set
  {48} NO step, 0 ff) + qform 64/64 (Q head
  23/48 tail a1/48, b5set {48} NO edge; quad
  b4=(0x23+2off) 64/64 contig+2 range 23..a1
  NO wrap, 64 distinct) + ring counter 256/256
  + ringraw 256/256 (head a3/48; off46/47
  (140415->140416) ff/48->01/49; mid off111
  81/49 @140480; off174/175 (140543->140544)
  ff/49->01/4a; tail off255 a1/4a @140624) + b0
  const 75 256/256 + b1 const 0b 256/256 +
  b84-87 const 446f5941 256/256 (all from oracle
  bytes first-hand). Odd-lencode 348/348 (346
  code-path + 2 singleton-embedded). Ring
  counter==raw-lencode 256/256 b4 mismatches 0
  (b5 thresholds 47/175 identical first-hand
  arithmetic, per-off values in edges log);
  quad counter==raw-lencode 64/64 b4 mismatches
  0; A formula==raw 16/16 (b5 step edge
  140287->140288 first-hand). Edges + mid
...[truncated 4477 chars]
