# GATE cd1943ec b315 T10P207 pins 88773..89120 (348 pins) PASS-functional

Seat sweep-r40, first-hand, WT tmp/wt-encode-sweep @cd1943ec,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r40.
Band = 8af9ec5f (py merge w2b@98380946 partial, +8 tiers
+52 pins) + cd1943ec (C port). Base 74274d93 (b314 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build315/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (stable: aae.c untouched
  c8b4a6a6..cd1943ec, binary bit-identical to r39
  build313 aae).
- RGRAMC-PYID 6082/6082 covered=6082/6082 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12164/12164 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12164/12164 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12164/12164).
- PINS-RGRAM cells set-eq 12164/12164 (cmp-equal).
  PINS base-N vs for-list 6082/6082 exact.
- PINS 12166 rows (2 hdr + 12164, +52 vs base 12114). py diff
  +52/-0 (pure P207 addition). For-list union +26 (88773
  88774 88775 88782 88790 88791 88793 88795 88800 88801
  88816 88817 88831 88832 88833 88848 88849 88864 88865
  88896 88959 88960 89024 89087 89088 89120), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P207 C-vs-py, 19-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 94070000 / e0300f00);
  AM 16/16, FM0 4/4, FM1 6/6, M 16/16, QR3 2/2,
  QT3 2/2, RM 16/16, RQ 16/16 EXACT;
  AC 75/75, FC0 71/71, FC1 71/71, QC1 76/76,
  QC2 76/76, QC3 66/66, RC 66/66 EXACT (py-hex vs
  C-decimal normalized);
  C _N decls 75/71/71/76/76/66/66 match actual;
  FS 10/10, FO 10/10 EXACT (py-hex vs C-decimal);
  no B/BC/BM/Q/QC/QR/QT/CM/CC/TC/QR1/QT1/QR2/
  QT2 tables either side (novel A/F/H/R geometry,
  grep-verified inventory).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in
  any of the 7 const tables; b4/b5 via lencode/
  counter logic) = memo code 75/71/71/76/76/66/66
  exact; memo also verified incl 76/72/72/77/76/
  67/66 from own bed (+b5-where-const: A/F0/F1/H1
  +1 const-b5 computed first-hand, H2 +0 carry,
  H3 +1 const-b6, R +0 counter) — resolved in-table
  per sweep2-r37 P192 precedent, NOT a FAIL.
  Dispatch verified by eye both sides, all 8 blocks
  (2 sing + 6 tiers): P2070 n==88773 / P2071 n==88774
  singleton-const (offs 0/1);
  P207A 88775..88790 off=n-88775;
  P207F 88791..88800 off=n-88791 sig-tag FS[off]
  + occurrence k=FO[off], 0xF4->FM0[k]/FC0 else
  0x7A->FM1[k]/FC1;
  P207H1 88801..88816 off=n-88801 M[off];
  P207H2 88817..88832 off=n-88817 M[off];
  P207H3 88833..88864 off=n-88833 m=off&15 h=off>>4;
  P207R 88865..89120 off=n-88865 c=off&15 r=off>>4;
  all paylen 84; A/F/H1/H2/H3 raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  R shared full-ring counter b4=(0x43+2off)&FF
  b5=0xb6+(off>=95)+(off>=223); mtab bytes A:b9-11,
  76-79 (7B), F:b13-19,80-83 (11B both), H:M b20,21,
  76-79 (6B shared) + H3:QR3 b13-15,17-19 (R6, b16
  gap) + QT3 b80-83, R:RM b20,21,25-27,76-79 (9B)
  by SLOT + RQ b0,11,19,72-75 (7B) by ROW;
  const sigs A:5e0ff300 F0:f4300f00 F1:7a980700
  H1/H3:a2877900 H2:440ff300 R:b1-3 e22a0d + RQ-b0
  10-sig e4/e5/e6/e7/e9/ec/ed/ef/f1/f3 both sides
  (const-table b0-3; R b0 in Q). C blocks carry
  T57451/456/461/476/506/521/536/559 py-line mirrors
  (exact); insert position exact (dispatch tail, N
  out-of-scope follows).
  Counter edges computed first-hand (never trusted
  from comments): A b5 const b5 (l16 0xB58F..0xB5AD);
  F const b5 (0xB5AF..0xB5C1); H1 const b5
  (0xB5C3..0xB5E1); H2 off14 ff/b5 -> off15 01/b6
  (88831->88832); H3 const b6 (0xB603..0xB641);
  R off94 ff/b6 -> off95 01/b7 (88959->88960) +
  off222 ff/b7 -> off223 01/b8 (89087->89088).
  Matches A-459/A-277 geometry (PBA VPOS b4+M7,
  FRAG10 interleave f4,f4,7a,7a,f4,7a,7a,7a,f4,7a
  == FS, MID64 16/16/32, H-shared M6 16/16 x4 rows,
  H32 mini-quad R6 2/2 + tails 2/2, ring
  TRANSPOSED 10-sig CLASSIC positions, M-tails
  ALL NEW 0/16, NO D dips).
- C diff renumber-only + new: raw 1585 del / 2523 add
  (incl 8 blank-plus, 0 blank-minus); normalized
  ([0-9]+ -> N, cut-c2 strip, sort -u) del-subset-add
  0 missing (del-uniq 1036, add-uniq 1236).
- Wall on band diff added lines (scope 74274d93..cd1943ec,
  2906 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-459-q439
  T10P207 predictions reproduce 28/28 (shape/mid/
  ring/counters CONFIRM, TBDs resolved first-hand
  §1/§2) + A-277 corroborates same tier (shape +
  H-shared + motif ring + edges CONFIRM, incl consts
  76/72/72/77/76/67/66, CORRECTION only re-tags b5
  const/carry — counts stand as filed, NO D dips).
  H32 2-halves cut matches A-277 2/2 first-hand
  (QR3 127c67c317bb/b6fcd2d05bb6 + tails 2/2);
  A-459's 4-row "3/4 distinct" framing resolved to
  2 halves in the cut, corroborated by A-277 bed +
  GREEN batteries on both halves (88833/88848 h0,
  88849/88864 h1). Agrees with cport commit msg
  (py/C 12164, PYID 6082).
- Quiz: no conflicting CLAIM/GATE/FLAG on b315/cd1943ec
  (GATE-27068708 b316-even cites it as diff-base only;
  sweep2-HANDOFF-r39 confirms odds = sweep turf).
  b314 EVEN = sweep2 turf, used as diff-base only,
  NOT gated.
- Logs: NVME ws tmp/encode-sweep/r40/ (*315* files:
  build315.log, pyid315, rgram315py/c, pass315py/c,
  cells315-battery, pins315-cells/-nums, for315-old/
  -new.nums, smoke315.log, tables315.log,
  tabaudit315.py, cdiff315.txt/-del-norm/
  -add-norm/-missing, banddiff315.txt, added315.txt,
  pins314base/pins315new.csv).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
