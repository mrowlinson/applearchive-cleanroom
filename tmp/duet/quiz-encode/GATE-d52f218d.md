# GATE d52f218d b319 T10P211 pins 90165..90512 (348 pins) PASS-functional

Seat sweep-r41, first-hand, WT tmp/wt-encode-sweep @d52f218d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r41.
Band = 06c29573 (py merge w2b@aff70122 partial, +7 tiers
+52 pins) + d52f218d (C port). Base d47266c1 (b318 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build319/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  binary bit-identical to r40 build317 aae).
- RGRAMC-PYID 6186/6186 covered=6186/6186 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12372/12372 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12372/12372 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12372/12372).
- PINS-RGRAM cells set-eq 12372/12372 (cmp-equal).
  PINS base-N vs for-list 6186/6186 exact.
- PINS 12374 rows (2 hdr + 12372, +52 vs base 12322). py diff
  +52/-0 (pure P211 addition). For-list union +26 (90165
  90166 90167 90174 90182 90183 90184 90185 90188 90192
  90193 90208 90209 90224 90225 90239 90240 90241 90256
  90257 90300 90367 90368 90495 90496 90512), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P211 C-vs-py, 17-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs f0070000 / e96d0f00);
  AM 16/16, PT 2/2, CM 8/8, M 16/16, X42 4/4,
  M42 16/16, QR 4/4, QT 4/4, RM 16/16, RQ 16/16
  EXACT;
  AC 75/75, PC 78/78, CC 70/70, QC 65/65,
  RC 67/67 EXACT (py-hex vs C-decimal normalized);
  C _N decls 75/78/70/65/67 match actual;
  no _T10P211B*/F*/H*/TC* symbols either side
  (novel A/P/C/Q/T geometry, grep-verified
  inventory).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in
  any of the 5 const tables) = memo code 75/70 exact
  (A/C); memo also verified incl 76/71 from own bed
  (+b5-where-const: A +1 const-c0 90167 6f/c0 ->
  90182 8d/c0 no wrap first-hand, C +1 const-c0
  90185 93/c0 -> 90192 a1/c0 no wrap first-hand)
  — resolved in-table per sweep2-r37 P192 precedent,
  NOT a FAIL. Q 65 = memo 65 (b5-carry in-table);
  T 67 = memo 67 (counter logic, +0). PAIR PC 78
  in-table full-tail (no memo incl count; A-281 VPOS
  {b4}+FULL-tail, battery GREEN).
  Dispatch verified by eye both sides, all 7 blocks
  (2 sing + 5 tiers): P2110 n==90165 / P2111 n==90166
  singleton-const (offs 0/1);
  P211A 90167..90182 off=n-90167;
  P211P 90183..90184 off=n-90183 b80-83=PT[off] + PC;
  P211C 90185..90192 off=n-90185;
  P211Q 90193..90256 off=n-90193 m=off&15 q=off>>4;
  P211R(T-ring) 90257..90512 off=n-90257 c=off&15
  r=off>>4;
  all paylen 84; A/P/C/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0x23+2off)&FF
  b5=0xc1+(off>=111)+(off>=239); mtab bytes A:b36-38,
  76-79 (7B), P:b80-83 (PT tab 4B), C:b32,33,37-42,
  80-83 (12B), Q:M b34,43,76-79 (6B) + b42 row-xor
  X42[q]^M42[m] + QR b36-41 (6B) + QT b80-83,
  T:RM b48-51,72-75 (8B) by COL + RQ b34,42,43,
  76-79 (7B) by ROW;
  const sigs A:e96dff00 P:e96d0f00 C:e96d0700
  Q:e96d6300 T:e96de307 both sides (const-table
  b0-3). C blocks carry T58612/617/622/637/652/668/
  693 py-line mirrors (exact); insert position exact
  (dispatch tail, N out-of-scope follows).
  Counter edges computed first-hand (never trusted
  from comments): A const c0 across (no edge);
  P const c0 (90183 8f/c0 -> 90184 91/c0);
  C const c0 across (no edge);
  Q off46 ff/c0 -> off47 01/c1 (90239->90240;
  destination off47 — A-471 FINDING label @off46 =
  source cell, bytes exact);
  T off110 ff/c1 -> off111 01/c2 (90367->90368) +
  off238 ff/c2 -> off239 01/c3 (90495->90496).
  Matches A-471/A-281 geometry (PBA VPOS b4+M7,
  full-tail PAIR b80-83 tab, PBC8 VPOS b4+M12,
  QUAD64 single-sig unpaired R6 b36-41 distinct +
  b42 row-xor X=[00,02,03,07] 64/64 + tails 4/4
  a14d25f5/5907bd9e/23a5c1c0/df267dea, T-ring
  ROLE-SWAP TRANSPOSED 21st + TAILS-SWAPPED,
  M-tails ALL NEW 0/16, NO D dips).
- C diff pure-add: raw 0 del / 752 add (incl 6
  blank-plus, 0 blank-minus); normalized ([0-9]+ -> N,
  cut-c2 strip, sort -u) del-subset-add 0 missing
  (del-uniq 0, add-uniq 198).
- Wall on band diff added lines (scope d47266c1..d52f218d,
  1094 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-471-q603
  T10P211 BACKFILL reproduces 23/23 (shape/ring/
  counters CONFIRM) + FINDING (quad b5-carry label
  @off46 vs destination off47 — first-hand lencode
  confirms edge 90239->90240 ff/c0->01/c1, batteries
  GREEN pins-vs-oracle, no DISSENT per A-471 §4) +
  A-281 corroborates same tier (shape + quad/b42xor/
  tails + T-ring + edges CONFIRM, incl consts 76/71/
  65/67, NO D dips). Agrees with cport commit msg
  (py/C 12372, PYID 6186).
- Quiz: no conflicting CLAIM/GATE/FLAG on b319/d52f218d.
  b318 EVEN = sweep2 turf, used as diff-base only,
  NOT gated.
- Logs: NVME ws tmp/encode-sweep/r41/ (*319* files:
  build319.log, pyid319, rgram319py/c, pass319py/c,
  cells319-battery, pins318base/pins319new.csv,
  pins319-cells/-nums, for319-old/-new.nums,
  smoke319.log, tables319.log, tabaudit319.py,
  sigcheck319.py, cdiff319.txt/-del-norm/-add-norm/
  -missing, banddiff319.txt, added319.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
