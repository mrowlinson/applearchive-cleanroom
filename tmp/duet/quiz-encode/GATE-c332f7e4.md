# GATE c332f7e4 b327 T10P219 pins 92949..93296 (348 pins) PASS-functional

Seat sweep-r43, first-hand, WT tmp/wt-encode-sweep @c332f7e4,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r43.
Band = 7a163858 (py merge w2b@3e7b26c3 partial, +7 tiers
+52 pins) + c332f7e4 (C port). Base 7828ec30 (b326 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build327/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r43).
- RGRAMC-PYID 6394/6394 covered=6394/6394 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12788/12788 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12788/12788 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12788/12788).
- PINS-RGRAM cells set-eq 12788/12788 (cmp-equal).
  PINS base-N vs for-list 6394/6394 exact.
- PINS 12790 rows (2 hdr + 12788, +52 vs base 12738). py diff
  +52/-0 (pure P219 addition). For-list union +26 (92949
  92950 92951 92958 92966 92967 92968 92969 92972 92976
  92977 92985 92992 92993 93008 93009 93017 93024 93025
  93040 93041 93055 93056 93183 93184 93296), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P219 C-vs-py, 17-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 56110000 / 36bf2200);
  AM 16/16, PT 2/2, CM 8/8, M 16/16, X42 4/4,
  M42 16/16, QR 4/4, QT 4/4, RM 16/16, RQ 16/16 EXACT;
  AC 75/75, PC 81/81, CC 70/70, QC 63/63,
  RC 67/67 EXACT (py-hex vs C-decimal normalized);
  C _N decls 75/81/70/63/67 match actual;
  no _T10P219BM/BC/FM/FC/FS/FO/H/TC* symbols either side
  (novel A/P/C/Q/T geometry — PAIR+C8 replace single-sig
  B, grep-verified inventory).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in
  any of the 5 const tables) = memo code 76/71/64/67
  exact (A/C8/Q/T); memo also verified incl from own
  bed (+b5-where-const: A +1 const-d6, C +1 const-d6,
  Q +1 const-d6 first-hand, T +0) — resolved in-table
  per sweep2-r37 P192 precedent, NOT a FAIL. PC 81 =
  84-3 (VPOS {b4,b80} pair-like + b5 const d6
  first-hand). T 67: 84-67=17=VPOS (b4,b5+M6+R9
  partition first-hand from RC table, A-289
  partition exact).
  VPOS partitions first-hand EXACT all 5 (AC-9 /
  PC-3 / CC-14 / QC-21 / RC-17 missing-sets).
  Dispatch verified by eye both sides, all 7 blocks
  (2 sing + 5 tiers): P2190 n==92949 / P2191 n==92950
  singleton-const (offs 0/1);
  P219A 92951..92966 off=n-92951;
  P219P 92967..92968 off=n-92967 b80 tab PT[off]
  (1B: 4e/6e);
  P219C 92969..92976 off=n-92969;
  P219Q 92977..93040 off=n-92977 m=off&15 q=off>>4
  + b42 row-xor (pay[42]^X42[q] vs M42[m]);
  P219R(T-ring) 93041..93296 off=n-93041 c=off&15
  r=off>>4;
  all paylen 84; A/P/C/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0xe3+2off)&FF
  b5=0xd6+(off>=15)+(off>=143); mtab bytes A:b36-38,
  76-79 (7B), P:b80 (1B), C:b32,33,37-42,80-83 (12B),
  Q:M b23,34,35,43,76-79 (8B) + b42 xor + QR b36-41
  (6B) + QT b80-83, T:RM b48,49,76-79 (6B) by COL +
  RQ b23,34,35,42,43,72-75 (9B) by ROW;
  const sigs A:36bf2a02 P:36bf2200 C:36bf1200
  Q:36bf1a01 T:36bf5a11 both sides (const-table b0-3).
  C blocks carry T60622/627/632/647/661/677/702 py-line
  mirrors (exact); insert position exact (dispatch
  tail, N out-of-scope follows).
  Counter edges computed first-hand (never trusted
  from comments): A/P/C/Q b5 const d6 across (b4
  distinct 16/2/8/64);
  T off14 ff/d6 -> off15 01/d7 (93055->93056) +
  off142 ff/d7 -> off143 01/d8 (93183->93184).
  Matches A-486/A-289 geometry (PBA VPOS b4+M7,
  PAIR VPOS {b4,b80} + PBC8 VPOS 13 b4+M12 EXACT,
  NO FRAG/B10, QUAD64 M8 shared 16/16 x3 + b42
  row-xor X=[00,04,05,05] + R6 r2==r3 PAIRED
  ffdf4b9030d1 3/4 distinct + tails 4/4 distinct
  r2/r3 share e910 (df24e910/0e25e910), T-ring
  STANDARD M6 by COL + R9 by ROW UNPAIRED 16
  distinct, M-tails ALL NEW 0/16, NO D dips).
- C diff pure-add: raw 0 del / 750 add (incl 6
  blank-plus, 0 blank-minus); normalized ([0-9]+ -> N,
  cut-c2 strip, sort -u) del-subset-add 0 missing
  (del-uniq 0, add-uniq 182).
- Wall on band diff added lines (scope 7828ec30..c332f7e4,
  1098 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-486-q611
  T10P219 predictive reproduces 26/26 (shape 13/13 +
  quad+Tring 9/9 + counters 4/4 CONFIRM) + A-289
  corroborates same tier (shape + quad/triple + tails
  + T-ring + edges CONFIRM, incl consts 76/71/64/67,
  NO D dips). Agrees with cport commit msg (py/C
  12788, PYID 6394).
- Quiz: no conflicting CLAIM/GATE/FLAG on b327/c332f7e4.
  b326 EVEN = sweep2 turf (GATE-7828ec30 filed by
  sweep2-r43), used as diff-base only, NOT gated.
- Logs: NVME ws tmp/encode-sweep/r43/ (*327* files:
  build327.log, pyid327, rgram327py/c, pass327py/c,
  cells327-battery, pins326base/pins327-cells/-nums,
  for327-old/-new.nums, smoke327.log, tables327.log,
  tabaudit327.py, sigcheck327.py/.log, cdiff327.txt/-del-norm/
  -add-norm/-missing, banddiff327.txt, added327.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
