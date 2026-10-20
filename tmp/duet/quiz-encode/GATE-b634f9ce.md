# GATE b634f9ce b333 T10P225 pins 95037..95384 (348 pins) PASS-functional

Seat sweep-r44, first-hand, WT tmp/wt-encode-sweep @b634f9ce,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r44.
Band = 1da14576 (py merge w2b@9bf285ad partial, +6 tiers
+52 pins) + b634f9ce (C port). Base 9a6da30d (b332 tip,
1328 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build333/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r44), rgramc d5cf79d0.
- RGRAMC-PYID 6550/6550 covered=6550/6550 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 13100/13100 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 13100/13100 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (13100/13100, version-sorted).
- PINS-RGRAM cells set-eq 13100/13100 (cmp-equal).
  PINS base-N vs for-list 6550/6550 exact.
- PINS 13102 rows (2 hdr + 13100, +52 vs base 13050). py diff
  +52/-0 (pure P225 addition); test_rgram.sh 1/1 (for-line).
  For-list union +26 (95037 95038 95039 95054 95055 95056
  95057 95058 95059 95064 95065 95080 95081 95096 95097
  95103 95104 95112 95113 95128 95129 95231 95232 95359
  95360 95384), 0 removed: 2 sing + A 2 + F 6 (all 4 sig
  groups: 4e pair 95055/56, 3e 95057, 2e 95058, 36 head/tail
  95059/95064) + Q 10 (carry pair 95103/95104) + R 6 (ring
  edges 95231/95232 + 95359/95360 + tail 95384).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P225 C-vs-py, 19-table FRAG layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 3f240000 / fe044e00);
  AM 16/16, FM0 2/2, FM3 6/6, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16 EXACT;
  FS 10/10, FO 10/10 EXACT (py-hex vs C-decimal);
  AC 75/75, FC0 78/78, FC1 82/82, FC2 82/82,
  FC3 70/70, QC 63/63, RC 67/67 EXACT (py-hex vs
  C-decimal normalized);
  C _N decls 75/78/82/82/70/63/67 match actual;
  TABAUDIT-GREEN rc=0. No BM/BC (FRAG replaces B),
  no _T10P225PT/PC/CM/CC (NO PAIR/C8),
  grep-verified inventory.
  Excl-b4/b5 accounting: b4/b5 in no const table (False x7).
  Missing-sets first-hand EXACT: AC-9 [4,5,48,49,50,76,77,
  78,79] = VPOS 8 (b4+M7 b48-50,76-79) + b5-const;
  FC0-6 [4,5,80,81,82,83] = {b4}+b5-const+tails;
  FC1-2 [4,5] + FC2-2 [4,5] (singletons);
  FC3-14 [4,5,23,35,46,47,48,49,50,51,80,81,82,83]
  = VPOS 13 (b4+M12 b23,35,46-51,80-83) + b5-const;
  QC-21 [4,5,6,7,23,35,45-51,76-83] = VPOS 21
  (b4,b5+M6 b6,7,76-79 + R13 b23,35,45-51,80-83);
  RC-17 [4,5,6,7,13-17,72-79] = VPOS 17
  (b4,b5+M9 b13-17,76-79 + R6 b6,7,72-75).
  Code AC75/FC3-70/QC63/RC67; incl = +1/+1/+0/+0
  (b5 const e6 verified first-hand over all 67 head cells
  95037..95103, Q carry in-table, T counter)
  = 76/71/63/67 = A-295 consts EXACT.
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/F/Q/R): P2250 n==95037 / P2251 n==95038
  singleton-const (offs 0/1);
  P225A 95039..95054 off=n-95039 sig fe048604 ==P224Q
  (m-tab 7B b48-50,76-79);
  P225F 95055..95064 off=n-95055 FRAG UNEVEN 4-sig
  (sigtag pay[2]==FS[off] + k=FO[off]: 0x4E -> FM0[k]
  4B b80-83 + FC0; 0x3E -> FC1 only; 0x2E -> FC2 only;
  0x36 -> FM3[k] 12B b23,35,46-51,80-83 + FC3);
  P225Q 95065..95128 off=n-95065 m=off&15 q=off>>4
  single-sig ec4f6003 r2==r3 paired (M 6B b6,7,76-79
  + R9 9B b23,35,45-51 + QT b80-83);
  P225R(T-ring) 95129..95384 off=n-95129 c=off&15
  r=off>>4 STANDARD sig dafe0436 (RM 9B b13-17,76-79
  by COL + RQ 6B b6,7,72-75 by ROW);
  all paylen 84; A/F/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0x33+2off)&FF
  b5=0xe7+(off>=103)+(off>=231).
  C blocks carry T62145/150/155/170/207/230 py-line
  mirrors (exact); F elif-chain as nested else-if,
  tags 78/62/46/54 = 0x4E/0x3E/0x2E/0x36 exact;
  C byte-index lists match py per block; insert position
  exact (dispatch tail, N out-of-scope follows).
  Value checks first-hand: FS 4e,4e,3e,2e,36x6;
  FO 0,1,0,0,0,1,2,3,4,5; FM0 pair 62f7924c/
  aa7b3f50 distinct; FM3 6/6 distinct; M 16/16;
  QR r2==r3 PAIRED 5059f9fbb271c537a9 x2, 3/4
  distinct (r0 d03979c06db1743f03, r1 d079796ce
  171905756); QT 4/4 distinct 9129bc09/682b13ce/
  e6315da9/15325da9, r2/r3 share last 2B 5da9;
  RM 16/16 + RQ 16/16 UNPAIRED distinct;
  M-tails 0/16 vs P224RM ALL NEW (QT 0/4 vs P224QT);
  R9 positions == F36M+b45 set-exact (positional:
  {23,35,46-51}+{45}={23,35,45-51}).
  Counter edges computed first-hand (never trusted
  from comments): head b5 e6 x67 (95037..95103) then
  e7 x25 (95104..95128); Q carry 95103 ff/e6 ->
  95104 01/e7; T off102 ff/e7 -> off103 01/e8
  (95231->95232) + off230 ff/e8 -> off231 01/e9
  (95359->95360). All edge pins PASS (batteries GREEN).
  @off2/@off3 in F-zone comments (py+C) = singleton
  offset text, NOT carry labels (read first-hand).
  Matches A-503/A-295 geometry (PB0 3f240000 NEW,
  PB1 fe044e00 ==P224B10, PBA fe048604 ==P224Q VPOS 8
  b5 const e6, FRAG uneven 4-sig exact map 4ex2+3ex1+
  2ex1+36x6 VPOS 13 6/6 diverge b5 const e6 NO PAIR/
  C8/B10, QUAD64 M6 shared + R9 r2==r3 PAIRED 3/4 +
  tails 4/4 r2/r3 share 5da9 + carry e6->e7, T-ring
  STANDARD M9 by COL + R6 by ROW UNPAIRED 16/16,
  M-tails ALL NEW 0/16, ring edges + thresholds
  103/231, NO D dips).
- C diff pure-add: numstat 909/0 (= 645+20+244 cport
  blocks); raw 909 add / 0 del (910/1 incl diff headers;
  5 blank-plus, 0 blank-minus); normalized ([0-9]+ -> N,
  cut-c2 strip, sort -u) del-subset-add 0 missing
  (del-uniq 0, add-uniq 197).
- Wall on band diff added lines (scope 9a6da30d..b634f9ce,
  1273 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, libcompression/CT-shim/shebang//usr/bin/aa/
  nominated 0 hits. Files touched: rgramc.c 909/0,
  rgram.py 311/0, test_rgram.sh 1/1 (for-line), PINS 52/0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  798->804 +6/0rm (stated literal method), seal
  1328->1334 +6: all agree, no slip (804 = 792 + b332
  EVEN 6 + 6, continuity holds).
- CONFIRM evidence (CONVERT-01 rule b): A-503-q617
  T10P225 predictive reproduces 29/29 (shape 15/15 +
  quad+Tring 10/10 + counters 4/4 CONFIRM) + A-295
  corroborates same tier (shape + quad/ring + tails
  + T-ring + edges CONFIRM, incl consts 76/71/63/67,
  NO D dips). No DISSENT on P225 (only P923/P924/P926,
  other turf, rebuttals filed). Agrees with cport commit
  msg (py/C 13100, PYID 6550).
- Quiz: no conflicting CLAIM/GATE/FLAG on b333/b634f9ce.
  b332 EVEN = sweep2 turf (tip 9a6da30d), used as
  diff-base only, NOT gated. Newest PARENT-* is QNUM-07
  (w2d Q-block only, read, no gate impact); PROSE-01
  re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r44/ (*333* files:
  build333.log, pyid333, rgram333py/c, pass333py/c,
  cells333-battery, pins332base/pins333-cells/-nums,
  for333-old/-new.nums, guards333-old/-new, smoke333.log,
  tables333.log, tabaudit333.py, sigcheck333.py/.log,
  verify333.py/.log, cdiff333.txt/-del-norm/
  -add-norm/-missing, banddiff333.txt, added333.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
