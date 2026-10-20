# GATE a8948f1f b321 T10P213 pins 90861..91208 (348 pins) PASS-functional

Seat sweep-r41, first-hand, WT tmp/wt-encode-sweep @a8948f1f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r41.
Band = db313a0f (py merge w2b@b4c7b051 partial, +6 tiers
+52 pins) + a8948f1f (C port). Base 2f100078 (b320 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build321/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  binary bit-identical to r41 build319 aae).
- RGRAMC-PYID 6238/6238 covered=6238/6238 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12476/12476 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12476/12476 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12476/12476).
- PINS-RGRAM cells set-eq 12476/12476 (cmp-equal).
  PINS base-N vs for-list 6238/6238 exact.
- PINS 12478 rows (2 hdr + 12476, +52 vs base 12426). py diff
  +52/-0 (pure P213 addition). For-list union +26 (90861
  90862 90863 90870 90878 90879 90880 90888 90889 90896
  90904 90905 90912 90920 90921 90928 90936 90937 90944
  90952 90953 91007 91008 91135 91136 91208), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P213 C-vs-py, 13-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 4b080000 / 837b1300);
  AM 16/16, BM 10/10, M 16/16, QR 4/4, QT 4/4,
  RM 16/16, RQ 16/16 EXACT;
  AC 74/74, BC 69/69, QC 63/63, RC 64/64 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 74/69/63/64 match actual;
  no _T10P213P*/C*/F*/H*/TC* symbols either side
  (novel A/B/Q/T geometry, grep-verified
  inventory).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in
  any of the 4 const tables) = memo code 74/63 exact
  (A/Q); memo also verified incl 75/64 from own bed
  (+b5-where-const: A +1 const-c5 90863 df/c5 ->
  90878 fd/c5 no wrap first-hand, Q +1 const-c6
  90889 13/c6 -> 90952 91/c6 no wrap first-hand)
  — resolved in-table per sweep2-r37 P192 precedent,
  NOT a FAIL. B 69 = memo 69 (b5-carry in-table,
  first B-carry); T 64 = memo 64 (counter logic, +0;
  84-64=20=VPOS first-hand from RC table, A-283
  CORRECTION holds).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + 4 tiers): P2130 n==90861 / P2131 n==90862
  singleton-const (offs 0/1);
  P213A 90863..90878 off=n-90863;
  P213B 90879..90888 off=n-90879;
  P213Q 90889..90952 off=n-90889 m=off&15 q=off>>4;
  P213R(T-ring) 90953..91208 off=n-90953 c=off&15
  r=off>>4;
  all paylen 84; A/B/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0x93+2off)&FF
  b5=0xc6+(off>=55)+(off>=183); mtab bytes A:b24-27,
  76-79 (8B), B:b20,21,25-31,80-83 (13B),
  Q:M b32-35,76-79 (8B) + QR b24-30 (7B) + QT
  b80-83, T:RM b32,37-39,76-79 (8B) by COL + RQ
  b14,15,21-23,31,72-75 (10B) by ROW;
  const sigs A:837b0b01 B:8f9b1100 Q:8f9b0901
  T:d0cf4b1c both sides (const-table b0-3).
  C blocks carry T59102/107/112/127/143/166 py-line
  mirrors (exact); insert position exact (dispatch
  tail, N out-of-scope follows).
  Counter edges computed first-hand (never trusted
  from comments): A const c5 across (no edge);
  B off0 ff/c5 -> off1 01/c6 (90879->90880,
  destination convention, explicit sides);
  Q const c6 across (no edge);
  T off54 ff/c6 -> off55 01/c7 (91007->91008) +
  off182 ff/c7 -> off183 01/c8 (91135->91136).
  Matches A-475/A-283 geometry (PBA VPOS b4+M8,
  PBB10 single-sig 10/10 diverge NO pair/C8,
  QUAD64 M8 shared 16/16 x3 + R7 b24-30 UNPAIRED
  4/4 + R-sharing 10/11 + tails 4/4
  4076c7ad/5774bc0b/bab1bb84/8d337c2f, T-ring
  STANDARD M8 by COL + R10 by ROW UNPAIRED 16
  distinct, M-tails ALL NEW 0/16, NO D dips).
- C diff pure-add: raw 0 del / 606 add (incl 5
  blank-plus, 0 blank-minus); normalized ([0-9]+ -> N,
  cut-c2 strip, sort -u) del-subset-add 0 missing
  (del-uniq 0, add-uniq 174).
- Wall on band diff added lines (scope 2f100078..a8948f1f,
  891 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-475-q605
  T10P213 predictive reproduces 28/28 (shape/quad+Tring/
  counters CONFIRM) + A-283 corroborates same tier
  (shape + quad/R-sharing/tails + T-ring + edges
  CONFIRM, incl consts 75/69/64/64, CORRECTION only
  re-tags T VPOS 18->20 = b4,b5+M8+R10 exact
  partition — counts stand, 84-64=20 verified
  first-hand, NO D dips). Agrees with cport commit msg
  (py/C 12476, PYID 6238).
- Quiz: no conflicting CLAIM/GATE/FLAG on b321/a8948f1f.
  b320 EVEN = sweep2 turf, used as diff-base only,
  NOT gated.
- Logs: NVME ws tmp/encode-sweep/r41/ (*321* files:
  build321.log, pyid321, rgram321py/c, pass321py/c,
  cells321-battery, pins320base/pins321new.csv,
  pins321-cells/-nums, for321-old/-new.nums,
  smoke321.log, tables321.log, tabaudit321.py,
  sigcheck321.py, cdiff321.txt/-del-norm/-add-norm/
  -missing, banddiff321.txt, added321.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
