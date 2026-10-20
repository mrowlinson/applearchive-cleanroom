# GATE f0b205de b325 T10P217 pins 92253..92600 (348 pins) PASS-functional

Seat sweep-r42, first-hand, WT tmp/wt-encode-sweep @f0b205de,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r42.
Band = 0c2f0098 (py merge w2b@b313e7f3 partial, +6 tiers
+52 pins) + f0b205de (C port). Base 35792e99 (b324 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build325/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r42).
- RGRAMC-PYID 6342/6342 covered=6342/6342 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12684/12684 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12684/12684 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12684/12684).
- PINS-RGRAM cells set-eq 12684/12684 (cmp-equal).
  PINS base-N vs for-list 6342/6342 exact.
- PINS 12686 rows (2 hdr + 12684, +52 vs base 12634). py diff
  +52/-0 (pure P217 addition). For-list union +26 (92253
  92254 92255 92270 92271 92272 92273 92276 92277 92280
  92281 92287 92288 92296 92297 92312 92313 92328 92329
  92344 92345 92415 92416 92543 92544 92600), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P217 C-vs-py, 18-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 9e100000 / 4ab22600);
  AM 16/16, FM0 2/2, FM1 7/7, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16 EXACT;
  AC 75/75, FC0 81/81, FC1 69/69, FC2 82/82,
  QC 65/65, RC 70/70 EXACT (py-hex vs C-decimal
  normalized);
  C _N decls 75/81/69/82/65/70 match actual;
  FS 10/10, FO 10/10 EXACT (py-hex vs C-decimal
  occurrence tag/map);
  no _T10P217B*/P*/C*/H*/TC* symbols either side
  (novel A/F/Q/T geometry — FRAG replaces B,
  grep-verified inventory).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in
  any of the 6 const tables) = memo code 75/70 exact
  (A/F16); memo also verified incl 76/70 from own
  bed (+b5-where-const: A +1 const-d0 92255 bf/d0 ->
  92270 dd/d0 no wrap first-hand, F +1 const-d0
  92271 df/d0 -> 92280 f1/d0 no wrap
  first-hand) — resolved in-table per sweep2-r37
  P192 precedent, NOT a FAIL. FC0 81 = 84-2-1
  (VPOS {b4,b80} pair-like, b5 const); FC2 82 =
  84-1-1 (singleton, only b4 varies). Q 65 = memo
  65 (b5-carry in-table, off6->7 edge); T 70 =
  memo 70 (counter logic, +0; 84-70=14=VPOS
  first-hand from RC table, A-287 partition
  exact).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + 4 tiers): P2170 n==92253 / P2171 n==92254
  singleton-const (offs 0/1);
  P217A 92255..92270 off=n-92255;
  P217F 92271..92280 off=n-92271 sigtag FS[off]
  + k=FO[off]: 0x26 -> FM0[k] 1B pay[80] + FC0,
  0x16 -> FM1[k] 13B + FC1, 0x1e -> FC2, else
  fail;
  P217Q 92281..92344 off=n-92281 m=off&15 q=off>>4;
  P217R(T-ring) 92345..92600 off=n-92345 c=off&15
  r=off>>4;
  all paylen 84; A/F/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0x73+2off)&FF
  b5=0xd1+(off>=71)+(off>=199); mtab bytes A:b48-50,
  76-79 (7B), F0:b80 (1B k=0,1: 95/b5),
  F1:b23,35,45-51,80-83 (13B),
  Q:M b6,7,76-79 (6B) + QR b35,46,47,48-51 (7B)
  + QT b80-83, T:RM b13,14,76-79 (6B) by COL +
  RQ b6,7,72-75 (6B) by ROW;
  const sigs A:4ab21602 F0:4ab22600 F1:4ab21600
  F2:4ab21e00 Q:ae246b01 T:fe4ab216 both sides
  (const-table b0-3).
  C blocks carry T60091/096/101/116/148/171 py-line
  mirrors (exact); insert position exact (dispatch
  tail, N out-of-scope follows).
  Counter edges computed first-hand (never trusted
  from comments): A const d0 across (no edge);
  F const d0 across incl singleton @off5 (no edge);
  Q off6 ff/d0 -> off7 01/d1 (92287->92288);
  T off70 ff/d1 -> off71 01/d2 (92415->92416) +
  off198 ff/d2 -> off199 01/d3 (92543->92544).
  Matches A-483/A-287 geometry (PBA VPOS b4+M7,
  FRAG uneven 3-sig EXACT 2x pair-like VPOS
  {b4,b80} + 7x M13 VPOS 14 + 1x singleton @off5,
  NO pair/C8/B10, QUAD64 M6 shared 16/16 x3 + R7
  TRIPLE-PAIRED r0==r2==r3 58958bd1ffff9c 2/4
  distinct first-triple + tails 4/4
  5ee9875d/97eccbbd/bde9875d/ece9875d r0/r2/r3
  share e9875d, T-ring STANDARD M6 by COL + R6
  by ROW UNPAIRED 16 distinct, M-tails ALL NEW
  0/16, NO D dips).
- C diff pure-add: raw 0 del / 813 add (incl 5
  blank-plus, 0 blank-minus); normalized ([0-9]+ -> N,
  cut-c2 strip, sort -u) del-subset-add 0 missing
  (del-uniq 0, add-uniq 189).
- Wall on band diff added lines (scope 35792e99..f0b205de,
  1160 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-483-q609
  T10P217 predictive reproduces 27/27 (shape 14/14 +
  quad+Tring 9/9 + counters 4/4 CONFIRM) + A-287
  corroborates same tier (shape + frag-3sig +
  quad/triple + tails + T-ring + edges CONFIRM,
  incl consts 76/70/65/70, NO D dips). Agrees with
  cport commit msg (py/C 12684, PYID 6342).
- Quiz: no conflicting CLAIM/GATE/FLAG on b325/f0b205de.
  b324 EVEN = sweep2 turf (GATE-35792e99 filed by
  sweep2-r43), used as diff-base only, NOT gated.
- Logs: NVME ws tmp/encode-sweep/r42/ (*325* files:
  build325.log, pyid325, rgram325py/c, pass325py/c,
  cells325-battery, pins324base/pins325-cells/-nums,
  for325-old/-new.nums, smoke325.log, tables325.log,
  tabaudit325.py, sigcheck325.log, cdiff325.txt/-del-norm/
  -add-norm/-missing, banddiff325.txt, added325.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
