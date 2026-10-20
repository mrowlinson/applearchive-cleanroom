# GATE c8b4a6a6 b313 T10P205 pins 88077..88424 (348 pins) PASS-functional

Seat sweep-r39, first-hand, WT tmp/wt-encode-sweep @c8b4a6a6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r39.
Band = 2dd2e15e (py merge w2b@c2b4ec3a partial, +8 tiers
+52 pins) + c8b4a6a6 (C port). Base 13c46dc8 (b312 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build313/{aae,rgramc}, rc=0, 0 warnings.
  aae sha d6e27c97 (stable: aae.c untouched).
- RGRAMC-PYID 6030/6030 covered=6030/6030 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12060/12060 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12060/12060 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12060/12060).
- PINS-RGRAM cells set-eq 12060/12060 (diff 0 bytes).
  PINS base-N vs for-list 6030/6030 exact.
- PINS 12062 rows (2 hdr + 12060, +52 vs base 12010). py diff
  +52/-0 (pure P205 addition). For-list union +26 (88077
  88078 88079 88086 88094 88095 88097 88098 88101 88104
  88105 88120 88121 88136 88137 88152 88153 88168 88169
  88191 88192 88319 88320 88408 88409 88424), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P205 C-vs-py, 21-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 94070000 / 6b850e00);
  AM 16/16, FM0 6/6, FM1 4/4, M 16/16, QR1 2/2,
  QT1 2/2, QR2 2/2, QT2 2/2, RM 16/16, RQ 15/15
  EXACT;
  AC 75/75, FC0 69/69, FC1 70/70, QC1 63/63,
  QC2 69/69, RC 68/68, TC 76/76 EXACT (py-hex vs
  C-decimal normalized);
  C _N decls 75/69/70/63/69/68/76 match actual;
  FS 10/10, FO 10/10 EXACT (py-hex vs C-decimal);
  no B/BC/BM/Q/QC/QR/QT/CM/CC tables either side
  (novel F/H/R/T geometry, grep-verified inventory).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in
  any of the 7 const tables; b4/b5 via lencode/
  counter logic) = memo code 75/69/70/63/69/68/76
  exact; memo also verified incl 76/70/71/64/70/
  68/77 from own bed (+b5-where-const: A/F/H1/H2
  +1 const-b0 computed first-hand, R +0 counter,
  T +1 const-b2 continued) — resolved in-table per
  sweep2-r37 P192 precedent, NOT a FAIL.
  Dispatch verified by eye both sides, all 8 blocks
  (2 sing + 6 tiers): P2050 n==88077 / P2051 n==88078
  singleton-const (offs 0/1);
  P205A 88079..88094 off=n-88079;
  P205F 88095..88104 off=n-88095 sig-tag FS[off]
  + occurrence k=FO[off], 0x0D->FM0[k]/FC0 else
  0x05->FM1[k]/FC1;
  P205H1 88105..88136 off=n-88105 m=off&15 h=off>>4;
  P205H2 88137..88168 off=n-88137 m=off&15 h=off>>4;
  P205R 88169..88408 off=n-88169 c=off&15 r=off>>4;
  P205T 88409..88424 off=n-88169 k=n-88409;
  all paylen 84; A/F/H1/H2 raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  R/T shared full-ring counter b4=(0xd3+2off)&FF
  b5=0xb0+(off>=23)+(off>=151); mtab bytes A:b24-26,
  76-79 (7B), F0:b20,21,25-31,80-83 (13B) /
  F1:b20,21,25-30,80-83 (12B), H:M b32-35,76-79
  (8B shared) + H1:QR1 b24-30 (R7) + QT1 b80-83 /
  H2:QR2 b25 (R1) + QT2 b80-83, R:RM b37,38,76-79
  (6B) by COL + RQ b21-23,31,72-75 (8B) by ROW,
  T:RM[k] positional; const sigs A:6b85f200
  F0:1d6a0d00 F1:1d6a0500 H1:1d6af100 H2:1d6a7900
  R:1d6add0e T:1d6ae50e both sides (const-table
  b0-3). C blocks carry T56783/788/793/808/838/
  861/883/902 py-line mirrors (exact); insert
  position exact (dispatch tail, N out-of-scope
  follows).
  Counter edges computed first-hand (never trusted
  from comments): A/F/H1/H2 b5 const b0;
  R off22 ff/b0 -> off23 01/b1 (88191->88192) +
  off150 ff/b1 -> off151 01/b2 (88319->88320);
  tail b5 const b2 (continued value).
  Matches A-456/A-275 geometry (PBA VPOS b4+M7,
  FRAG10 interleave 0d,0d,05,0d,0d,05,05,0d,0d,05
  == FS, VPOS 14/13, H1/H2 shared M8 16/16 x4
  halves, H1 R7 2/2 + H2 R1 0x70/0x72, tails 4/4
  distinct, T240 TRANSPOSED 15th CLASSIC no-swap
  == impl comment, TAIL16 = ring row-15 own-sig M
  positional == 240M 16/16 + Q15 novel, M-tails
  ALL NEW 0/16, NO D dips).
- C diff renumber-only + new: raw 1569 del / 2533 add
  (incl 8 blank-plus, 0 blank-minus); normalized
  ([0-9]+ -> N, cut-c2 strip, sort -u) del-subset-add
  0 missing (del-uniq 1022, add-uniq 1236).
- Wall on band diff added lines (scope 13c46dc8..c8b4a6a6,
  2930 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-456-q437
  T10P205 predictions reproduce 31/31 (lencode 92/92,
  T240 240/240, shape/mid/ring/counters CONFIRM) +
  2 FINDINGS adopted (ring CLASSIC transposed NOT
  tails-swapped — matches impl "NO swap" comment;
  no ring-Q/quad-M swap relation); A-275
  corroborates same tier (shape + halves + split
  ring + edges CONFIRM, incl consts 76/70/71/64/
  70/68/77, CORRECTION only re-tags H1/H2/tail b5
  const — counts stand as filed, NO D dips). Agrees
  with cport commit msg (py/C 12060, PYID 6030).
- Quiz: no conflicting CLAIM/GATE/FLAG on b313/c8b4a6a6
  (GATE-c81821f is an unrelated writer2 gate).
  b312 EVEN = sweep2 turf (sweep2-live), used as
  diff-base only, NOT gated.
- Logs: NVME ws tmp/encode-sweep/r39/ (*313* files:
  build313.log, pyid313, rgram313py/c, pass313py/c,
  cells313-battery, pins313-cells/-nums, for313-old/
  -new.nums, smoke313.log, tables313.log,
  tabaudit313.py, cdiff313.txt/-del-norm/
  -add-norm/-missing, banddiff313.txt, added313.txt,
  pins312base/pins313new.csv).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
