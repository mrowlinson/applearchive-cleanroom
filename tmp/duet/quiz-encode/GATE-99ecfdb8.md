# GATE 99ecfdb8 b323 T10P215 pins 91557..91904 (348 pins) PASS-functional

Seat sweep-r42, first-hand, WT tmp/wt-encode-sweep @99ecfdb8,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r42.
Band = daa01b6e (py merge w2b@ae5a9305 partial, +6 tiers
+52 pins) + 99ecfdb8 (C port). Base 936eddc9 (b322 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build323/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r42).
- RGRAMC-PYID 6290/6290 covered=6290/6290 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12580/12580 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12580/12580 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12580/12580).
- PINS-RGRAM cells set-eq 12580/12580 (cmp-equal).
  PINS base-N vs for-list 6290/6290 exact.
- PINS 12582 rows (2 hdr + 12580, +52 vs base 12530). py diff
  +52/-0 (pure P215 addition). For-list union +26 (91557
  91558 91559 91566 91574 91575 91579 91584 91585 91592
  91600 91601 91608 91616 91617 91624 91632 91633 91640
  91647 91648 91649 91775 91776 91903 91904), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P215 C-vs-py, 13-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 4b080000 / f89f1000);
  AM 16/16, BM 10/10, M 16/16, QR 4/4, QT 4/4,
  RM 16/16, RQ 16/16 EXACT;
  AC 75/75, BC 71/71, QC 63/63, RC 64/64 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 75/71/63/64 match actual;
  no _T10P215P*/C*/F*/H*/TC* symbols either side
  (novel A/B/Q/T geometry, grep-verified
  inventory).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in
  any of the 4 const tables) = memo code 75/71 exact
  (A/B); memo also verified incl 76/72 from own bed
  (+b5-where-const: A +1 const-cb 91559 4f/cb ->
  91574 6d/cb no wrap first-hand, B +1 const-cb
  91575 6f/cb -> 91584 81/cb no wrap first-hand)
  — resolved in-table per sweep2-r37 P192 precedent,
  NOT a FAIL. Q 63 = memo 63 (b5-carry in-table,
  LAST-CELL edge); T 64 = memo 64 (counter logic,
  +0; 84-64=20=VPOS first-hand from RC table,
  A-285 partition exact).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + 4 tiers): P2150 n==91557 / P2151 n==91558
  singleton-const (offs 0/1);
  P215A 91559..91574 off=n-91559;
  P215B 91575..91584 off=n-91575;
  P215Q 91585..91648 off=n-91585 m=off&15 q=off>>4;
  P215R(T-ring) 91649..91904 off=n-91649 c=off&15
  r=off>>4;
  all paylen 84; A/B/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0x03+2off)&FF
  b5=0xcc+(off>=127)+(off>=255); mtab bytes A:b9-11,
  76-79 (7B), B:b13-19,80-83 (11B),
  Q:M b20-23,76-79 (8B) + QR b13-19 (7B) + QT
  b80-83, T:RM b20,21,25-27,76-79 (9B) by COL + RQ
  b12-15,19,72-75 (9B) by ROW;
  const sigs A:64ff0901 B:ee3f2100 Q:e5fe1302
  T:408b0738 both sides (const-table b0-3).
  C blocks carry T59576/581/586/601/617/640 py-line
  mirrors (exact); insert position exact (dispatch
  tail, N out-of-scope follows).
  Counter edges computed first-hand (never trusted
  from comments): A const cb across (no edge);
  B const cb across (no edge);
  Q off62 ff/cb -> off63 01/cc (91647->91648,
  LAST-CELL);
  T off126 ff/cc -> off127 01/cd (91775->91776) +
  off254 ff/cd -> off255 01/ce (91903->91904
  last-cell).
  Matches A-479/A-285 geometry (PBA VPOS b4+M7,
  PBB10 single-sig 10/10 diverge NO pair/C8,
  QUAD64 M8 shared 16/16 x3 + R7 b13-19
  BOTTOM-PAIRED r2==r3 a2bc521ae5788f 3/4
  distinct + B10-vs-quadR positions 11/11
  set-exact + tails 4/4
  8df0e13d/a1ee58a8/fc3ad4a8/2b3bd4a8 r2/r3
  share d4a8, T-ring STANDARD M9 by COL + R9
  by ROW UNPAIRED 16 distinct, M-tails ALL NEW
  0/16, NO D dips).
- C diff pure-add: raw 0 del / 606 add (incl 5
  blank-plus, 0 blank-minus); normalized ([0-9]+ -> N,
  cut-c2 strip, sort -u) del-subset-add 0 missing
  (del-uniq 0, add-uniq 174).
- Wall on band diff added lines (scope 936eddc9..99ecfdb8,
  895 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-479-q607
  T10P215 predictive reproduces 25/25 (shape 12/12 +
  quad+Tring 9/9 + counters 4/4 CONFIRM) + A-285
  corroborates same tier (shape + quad/R-pairing +
  tails + T-ring + edges CONFIRM, incl consts 76/72/
  63/64; CORRECTION only re-tags R7 r2==r3
  BOTTOM-PAIRED = first-hand QR table exact —
  counts stand, NO D dips). Agrees with cport commit
  msg (py/C 12580, PYID 6290).
- Quiz: no conflicting CLAIM/GATE/FLAG on b323/99ecfdb8.
  b322 EVEN = sweep2 turf, used as diff-base only,
  NOT gated.
- Logs: NVME ws tmp/encode-sweep/r42/ (*323* files:
  build323.log, pyid323, rgram323py/c, pass323py/c,
  cells323-battery, pins322base/pins323-cells/-nums,
  for323-old/-new.nums, smoke323.log, tables323.log,
  tabaudit323.py, sigcheck323.py, cdiff323.txt/-del-norm/
  -add-norm/-missing, banddiff323.txt, added323.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
