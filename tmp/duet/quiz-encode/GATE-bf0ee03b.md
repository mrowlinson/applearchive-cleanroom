# GATE bf0ee03b b311 T10P203 pins 87381..87728 (348 pins) PASS-functional

Seat sweep-r39, first-hand, WT tmp/wt-encode-sweep @bf0ee03b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r39.
Band = 664b1070 (py merge w2b@6e356170 partial, +6 tiers
+52 pins) + bf0ee03b (C port). Base 76e7bf34 (b310 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build311/{aae,rgramc}, rc=0, 0 warnings.
  aae sha d6e27c97 (stable: aae.c untouched).
- RGRAMC-PYID 5978/5978 covered=5978/5978 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11956/11956 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11956/11956 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (11956/11956).
- PINS-RGRAM cells set-eq 11956/11956 (diff 0 bytes).
  PINS base-N vs for-list 5978/5978 exact.
- PINS 11958 rows (2 hdr + 11956, +52 vs base 11906). py diff
  +52/-0 (pure P203 addition). For-list union +26 (87381
  87382 87383 87390 87398 87399 87403 87408 87409 87423
  87424 87425 87432 87440 87441 87448 87456 87457 87464
  87472 87473 87551 87552 87679 87680 87728), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P203 C-vs-py, 14-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 9e030000 / 95020500);
  AM 16/16, BM 10/10, M 16/16, QR 4/4, QT 4/4,
  RM 16/16, RQ 16/16 EXACT;
  AC 76/76, BC 70/70, QC 63/63, RC 65/65
  EXACT (py-hex vs C-decimal normalized);
  C _N decls 76/70/63/65 match actual;
  B42 16/16 EXACT (py-hex vs C-decimal);
  no T/TC/CM/CC tables either side (grep-verified).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in any
  const table; b4/b5 via lencode/counter logic) = memo
  code 76/70/63/65 exact; memo also verified incl
  77/71/63/65 from own bed (+b5-where-const: A/B +1
  const-aa computed first-hand, Q +0 b5-carry @off15,
  R +0 counter) — resolved in-table per sweep2-r37 P192
  precedent, NOT a FAIL.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + 4 tiers): P2030 n==87381 / P2031 n==87382
  singleton-const (offs 0/1);
  P203A 87383..87398 off=n-87383;
  P203B 87399..87408 off=n-87399;
  P203Q 87409..87472 off=n-87409 m=off&15 q=off>>4;
  P203R 87473..87728 off=n-87473 c=off&15 r=off>>4;
  all paylen 84; A/B/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  Q b42 rule b42b=B42[m] b42e=q<2?b42b:b42b-1;
  R full-ring counter b4=(0x63+2off)&FF
  b5=0xab+(off>=79)+(off>=207); mtab bytes A:b36,37,
  76-79 (6B), B:b32,33,37-42,80-83 (12B),
  Q:M b23,34,35,43,76-79 + QR b36-41 (sigr6) + QT
  b80-83 + b42 rule, R:RM b48-51,72-75 (8B) by COL
  + RQ b23,34,35,42,43,76-79 (9B) by ROW; const sigs
  A:95027100 B:95020500 Q:95026d00 R:95022d07 both
  sides (const-table b0-3). C blocks carry T56228/233/
  238/253/269/296 py-line mirrors (exact); insert
  position exact (dispatch tail, N out-of-scope
  follows).
  Counter edges computed first-hand (never trusted
  from comments): A b5 const aa, B b5 const aa;
  Q 87423 ff/aa -> 87424 01/ab; R off78 ff/ab ->
  off79 01/ac + off206 ff/ac -> off207 01/ad.
  Matches A-441 geometry (PBA VPOS b4+M6, PBB10
  10-diverge 10/10, QUAD VPOS 21 double-paired
  r0==r1+r2==r3 2/4 distinct + tails 4/4 distinct
  13/16 bytes, b42 rule 64/64, T-ring TRANSPOSED
  13th + TAILS-SWAPPED 4th, ring-Q common-8B rows
  == quad-M row0 16/16, M-tails ALL NEW 0/16,
  edges 87551->87552 + 87679->87680 ff->01).
- C diff renumber-only + new: raw 1555 del / 2161 add
  (incl 6 blank-plus, 0 blank-minus); normalized
  ([0-9]+ -> N, cut-c2 strip, sort -u) del-subset-add
  0 missing (del-uniq 1010, add-uniq 1185).
- Wall on band diff added lines (scope 76e7bf34..bf0ee03b,
  2458 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-441-q435
  T10P203 CONFIRM all, 70/70 checks (14+12+9+35;
  A-273 corroborates same tier on all 3 legs:
  shape+quad+b42-double-pair, counters+edges,
  incl consts 77/71/63/65, NO D dips). Agrees
  with cport commit msg (py/C 11956, PYID 5978).
- Quiz: no conflicting CLAIM/GATE/FLAG on b311/bf0ee03b.
  b310 EVEN = sweep2 turf, used as diff-base only, NOT
  gated.
- Logs: NVME ws tmp/encode-sweep/r39/ (*311* files:
  build311.log, pyid311, rgram311py/c, pass311py/c,
  cells311-battery, pins311-cells/-nums, for311-old/
  -new.nums, smoke311.log, tables311.log,
  tabaudit311.py, b45check311.py, cdiff311.txt/-del-norm/
  -add-norm/-missing, banddiff311.txt, added311.txt,
  pins310base/pins311new.csv).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
