# GATE fc1d9af3 b303 T10P195 pins 84597..84944 (1112 tiers) PASS-functional

Seat sweep-r37, first-hand, WT tmp/wt-encode-sweep @fc1d9af3,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r37.
Band = 73f881de (py merge w2b@fb3c39a1 partial, +7 tiers +46 pins)
+ fc1d9af3 (C port). Base de815ae0 (b302 C tip, EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build303/{aae,rgramc}, rc=0, 0 warnings.
  aae sha d6e27c97 (stable: aae.c untouched).
- RGRAMC-PYID 5735/5735 covered=5735/5735 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11470/11470 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11470/11470 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (11470/11470).
- PINS-RGRAM cells set-eq 11470/11470 (diff 0 bytes).
  PINS base-N vs for-list 5735/5735 exact.
- PINS 11472 rows (2 hdr + 11470, +46 vs base 11426). py diff
  +268/-0 (pure P195 addition). For-list union +23 (84597
  84598 84599 84607 84608 84615 84616 84617 84618 84621
  84624 84625 84640 84641 84657 84673 84688 84689 84735
  84736 84863 84864 84944), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P195 C-vs-py, 15-table, all EXACT:
  S0/S1/S2 const strings EXACT (168 hex chars each,
  sigs 48030000 / 79ad0500 / d3dd0300);
  AM 16/16, BM 9/9, M 16/16, QR 4/4, QT 4/4,
  RM 16/16, RQ 16/16 EXACT; B42 16/16 EXACT
  (py hex ints vs C longs); AC 76/76, BC 70/70,
  QC 65/65, RC 67/67 EXACT (py-hex vs
  C-decimal normalized); C _N decls 76/70/65/67
  match actual. Excl-b5 accounting in-table (no b5
  entry in any const table; b5 via lencode/counter
  logic) = memo excl 76/70/65/67 exact;
  memo also verified incl 76/71/66/67 from own
  bed — resolved in-table per sweep2-r37 P192
  precedent, NOT a FAIL.
  Dispatch verified by eye both sides, all 7 tiers:
  P1950 n==84597 / P1951 n==84598 / P1952 n==84617
  singleton-const (offs 0/1/20);
  P195A 84599..84614 off=n-84599;
  P195B arm1 84615..84616 off=n-84615 +
  arm2 84618..84624 off=n-84616;
  P195Q 84625..84688 off=n-84625 m=off&15 q=off>>4;
  P195R 84689..84944 off=n-84689 c=off&15 r=off>>4;
  all paylen 84; A/B/Q raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8; R counter
  b4=(0xa3+2off)&FF b5=0x95+(off>=47)+(off>=175);
  mtab bytes A:b36,37,76-79 (6B), B:b32,33,37-42,
  80-83 (12B), Q:M b43,76-79 + b42 row-rule
  (B42[m], q<2 id, q==2 |1, else ^2) + b34
  col-half (0x17 m<8 else 0x1f) + QR b36-41
  (sigrb6) + QT b80-83, R:RM b48-51,72-75 by
  COL + RQ b34,42,43,76-79 by ROW;
  const sigs A:79ad6900 B:79ad0500 (==PB1)
  Q:79ad7900 R:79ad9906 both sides. C blocks carry
  T53902/907/912/927/943/948/964/993 py-line
  mirrors; insert position exact (dispatch tail, N
  out-of-scope follows). Matches A-420 geometry
  (VPOS A [4,5,36,37,76,77,78,79] / B b4+M12 /
  Q b4+b5const+M5+b42+b34+R6+tails, QUAD
  top-paired r0==r1, T-ring TRANSPOSED M8=f(c)
  Q7=g(r) + TAILS-SWAPPED, lencode step @84608
  ff/94->01/95, T-ring edges 84735->84736 +
  84863->84864 ff->01, flips {84608,84736,84864}
  all claimed).
- C diff renumber-only + new: raw 1476 del / 2145 add
  (incl 8 blank-plus, 0 blank-minus); normalized
  ([0-9]+ -> N, cut-c2 strip, sort -u) del-subset-add
  0 missing (del-uniq 949, add-uniq 1125).
- Wall on band diff added lines (scope de815ae0..fc1d9af3,
  2460 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-420-q426
  T10P195 CONFIRM all, 84/84 checks (23+14+5+42;
  A-265 corroborates same tier: PBB 2+7 split,
  b34 COLUMNS axis, consts 76/71/66/67 incl).
  Agrees with cport commit msg (py/C 11470,
  PYID 5735).
- Quiz: no conflicting CLAIM/GATE/FLAG on b303/fc1d9af3.
  b302 EVEN = sweep2 turf, used as diff-base only, NOT gated.
- Logs: NVME ws tmp/encode-sweep/r37/ (*303* files:
  build303.log, pyid303, rgram303py/c, pass303py/c,
  pins303-cells/-nums, seteq303.diff, for303-old/new/-nums,
  smoke303.log, tables303.log, tabaudit303.py,
  cdiff303.txt/-del-norm/-add-norm/-missing,
  banddiff303.txt, added303.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
