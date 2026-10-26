# GATE db0378aa b384 T10P276 pins 112785..113132 (1644 tiers) PASS-functional

Seat sweep2-r59, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r59/w384 @db0378aa.
Band = 82011043 (py merge w2b@99ef3492 partial, +6 tiers, +62 pins)
+ db0378aa (C port). Base 49652d42 (b383 tip, 1638 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build384/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 0c553cbc / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r59
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8123/8123 covered=8123/8123 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 16246/16246 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 16246/16246 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 16246/16246).
- PINS-RGRAM cells set-eq 16246/16246 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8123/8123 xor 0;
  PINS 16248 rows (2 hdr + 16246 = PASS lines, +62 vs base
  16186). For-list union 8092->8123 +31 (112785 112786
  112787 112788 112792 112797 112801 112802 112803 112804
  112806 112809 112811 112812 112813 112825 112826 112841
  112842 112857 112858 112873 112874 112876 112877 112895
  112896 112953 113023 113024 113132),
  0 removed, range 112785..113132 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 16246-16184.
  The 31 = S0/S1 (2) + A head/mids/tail (6) + C head/mids/
  tail (6) + Q head/split-pairs/tail (10) +
  ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P276 C-vs-py, script-compared, TABAUDIT-GREEN
  94 PASS 0 FAIL (tabaudit276.py rc=0): S0/S1 168ch
  EXACT sigs b6690700 NEW / 0d2b660e NEW (vs P275
  b2690700 / 0d2bd60e, full-string ne both),
  AM 16/16 7B distinct, CM 10/10 11B distinct, M 16/16
  9B distinct, QR 4/4 6B, QT 4/4 4B, RM 16/16 8B
  distinct, RQ 16/16 9B distinct, RT ABSENT (FRAG
  ring, no RT table either side), R8 16/16 1B +
  X8 16/16 1B EXACT,
  AC 75, CC 71, QC 62, RC 68; C _N decls 75/71/62/68
  match actual; byte-coverage unions exact every block
  (84/84/84/88, 0 overlap, b4/b5 computed; QC
  cover includes split-b0, RC cover includes b8-xor).
  PBA16-PLAIN sig ddb062e6 NEW (P275 809907fc
  per P275AC code-verified), b0 const dd; AC
  b8 const dc; AC has no b5 (b5-const memo-1).
  C10-1SIG 386c550f x10 via CC b0-b3; CM 10/10
  diverge; CC has no b5.
  QUAD2s col-split b0 = c1 iff m<13 else e4 (2nd
  in quad, code-verified py 0xC1/0xE4 + C 193/228);
  QM9 shared 16/16 x3 NO frags; R6 LAST3-PAIRED
  r1==r2==r3 31142182fe5d x3 (last3 82fe5d), r0
  73ff014fe862 distinct (last3 4fe862); tails
  row-shared 4/4 distinct f6592f08/8da3a08d/
  b2a3a08d/d7a3a08d, r1/r2/r3 share TRUE 3B
  a3a08d (tails echo the R last3-pairing), r0
  distinct; b49 const df; QC has no b5 (b5
  const 71 raw lencode).
  Ring FRAG: b8 row-XOR X=[00x13,20,20,20]
  staged (ADD tie A=[0x13,32,32,32] noted in
  code comment), R8 per-col 16x1B
  41/c1/81/01/41/41/c1/01/41/c1/01/81/81/c1/81/c1;
  TM8 b9,10,11,19,80-83 16/16 distinct by COL,
  TR9 b13-17,76-79 16/16 distinct by ROW UNPAIRED
  (full-row sets disjoint), tails SPLIT b80-83
  col / b76-79 row; RC b0-3 0e000000, b84-87
  2c295916 ring-wide NEW (P275 sig 07000000,
  b84-87 f9b5ac58, both per P275RC code-verified).
  Code-consts vs A-676 INCL (PBA 76 / C10 72 /
  quad 63 / T88 68): impl 75/71/62/68 = memo-1
  on PBA/C10/quad (b5-const excluded), identical
  on T88 (standing bookkeeping).
  M-tails 16/16 ALL NEW vs P275 (zero overlap vs
  BOTH P275RM-tail8 and P275RQ-tail8; P275 RM/RQ
  16x8B rows re-read first-hand). AM/CM 0-overlap
  vs P275AM/CM (CM 22ch vs 32ch widths).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=112785 (PB0 sig b6690700 NEW, lenB 84), S1
  n=112786 (PB1 sig 0d2b660e NEW, lenB 84),
  A 112787-112802 PBA16-PLAIN (sig ddb062e6 NEW via
  AC b0-b3, b0 const dd, b8 const dc, AM 16/16
  distinct 7B, mtab b6,7,9,76-79, b5 const 71 raw
  lencode),
  C 112803-112812 C10-1SIG (386c550f x10 via CC
  b0-b3, CM 10/10 distinct 11B diverge 10/10, mtab
  b6-8,48-51,80-83, b5 const 71 raw lencode),
  Q 112813-112876 QUAD2s col-split c1c356f5-x52/
  e4c356f5-x12 (b0split above, QM9 b9-13,76-79 M
  16/16 9B shared x3 + R6 b6-8,48,50,51
  LAST3-PAIRED above + QT tails above, NO frags,
  b5 const 71 NO step),
  R 112877-113132 T88-FRAG (sig 0e000000, b8-XOR
  staged above, TM8 b9-11,19,80-83 by COL RM
  16/16 8B, TR9 b13-17,76-79 by ROW RQ 16/16 9B
  UNPAIRED, b84-87 const 2c295916 ring-wide,
  b4=(0xdb+2off)&FF, b5=0x71+(off>=19)+(off>=147)).
  C blocks carry T75397/75402/75407/75422/75438/75463
  py-line mirrors (each re-read: hits the exact py guard
  line), bounds + byte positions exact (A 7B, C 11B, Q
  9/6/4B, R 8/9B + b8xor), counter b4=(219+2off)&FF +
  (off>=19)+(off>=147), temps _t5810-5829 (base max
  _t5809, no reuse) + _b3523/3525/3527/3528/3529/3531/
  3532 + _i3524/3526/3530/3533 (base max _b3521/_i3522,
  no reuse), all 6 verified.
  Insert position exact both sides: after T10P275R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-676/A-340 geometry (PB0/PB1 NEW, PBA16 PLAIN
  VPOS 8 b5 const 71 16/16 distinct NO pair, C10-1SIG
  VPOS 12 b5 const 71 10/10 diverge, QUAD2s VPOS 21
  split + R6 LAST3-PAIRED + QT r123 TRUE-3B +
  M-tails NEW, T88-FRAG VPOS 20 + b84-87 2c295916,
  lencode 348/348 whole-tier, Q split-pairs 112825->
  112826 +112841->112842 +112857->112858 +112873->
  112874 (NO b5 step) + ring edges 112895->112896 +
  113023->113024, NO D dips) incl exact values (PBA/C10
  sigs, X8/R8 vectors, QR/R6 values, QT tails, ring
  TM8/TR9 UNPAIRED + SPLIT tails, consts stand).
- Edges via counter formula first-hand: A head 27/71
  tail 45/71 b5set {71} NO carry; C head 47/71 tail
  59/71 b5set {71} NO carry; Q head 5b/71 tail d9/71,
  formula b4=(0x5b+2off)&FF b5=0x71 64/64, NO ff
  edge (b4 range 0x5b..0xd9);
  ring 112895 (off18, ff/71) -> 112896 (off19, 01/72);
  113023 (off146, ff/72) -> 113024 (off147, 01/73);
  R head db/71 tail d9/73; split-pairs 112825 (m12,
  c1) / 112826 (m13, e4) +112841/112842 +112857/112858
  +112873/112874 in for-list; all edge pins + tail
  113132 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (23/71, 25/71) match raw lencode.
  Ring counter == raw lencode 256/256, 0 mismatch.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 654 add / 0 del
  (rgramc.c) + 262/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 649 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 441).
- Wall on band diff added lines (scope 49652d42..
  db0378aa, 979 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 654/0, rgram.py 262/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 584->586 +2 / ranges 556->560 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep), CLOSED T10P prints 1544->1550 +6, C singletons
  584->586 +2 / C ranges 556->560 +4 (deltas agree both
  sides), C CLOSED 1544->1550 +6, seal 1638->1644 +6
  (commit msgs): all agree, no slip (absolute seal
  inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-676-q788-
  t10p276 verdict CONFIRM (Q1 shape 14/14 + Q2 quad/ring
  15/15 + Q3 counters 12/12 = 41/41 as-filed; file
  present, counts verified; exact-value corroboration
  incl PBA/C10 sigs, QUAD2s split + R6 last3-pair + QT
  tails, M-tails NEW, ring FRAG + b8-XOR stage + edges
  + consts) + A-340 viewer corroboration (all 3 legs
  CONFIRM). No CONFIRM-P276.md file; A-676 suffices per
  rule. Agrees with cport commit msg (PYID 8123, RGRAM
  16246).
- Quiz: no conflicting CLAIM/GATE/FLAG on b384 (adjacent
  GATE-a33e4c8f b385 cites b384 tip as diff-base only,
  turf acknowledged). Newest PARENT-* is QNUM-18 (w2e/w2f
  Q-blocks only, read, no gate impact); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r59/ (build384.log,
  pyid384.log, rgram384py/c.log, cmp384.py/.c,
  for384-old/-new.nums, smoke384.log, tables384.log,
  tabaudit276.py, edges276.py, edges384.log,
  numstat384.txt, add/delnorm384.txt, banddiff384.txt,
  cdiff384.txt, pydiff384.txt, added384.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
