# GATE 936eddc9 b322 T10P214 pins 91209..91556 (1266 tiers) PASS-functional

Seat sweep2-r42, first-hand, WT tmp/wt-encode-sweep2 @936eddc9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r42.
Band = e8ed9492 (py merge w2b@21376730 partial, +6 tiers, +52 pins)
+ 936eddc9 (C port). Base a8948f1f (b321 tip, 1260 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build322/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 5719ece4 / aae d6e27c97
  (aae identical to b288-b320 builds: aae.c untouched).
- RGRAMC-PYID 6264/6264 covered=6264/6264 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 12528/12528 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 12528/12528 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 12528/12528).
- PINS-RGRAM cells set-eq 6264/6264 (diff 0, PINS base-N
  set vs for-list); PINS 12530 rows (2 hdr + 12528 =
  PASS lines). For-list union +26 (91209 91210 91211
  91218 91226 91227 91231 91236 91237 91244 91252
  91253 91263 91264 91268 91269 91276 91284 91285
  91300 91301 91391 91392 91519 91520 91556),
  0 removed. Each for-N yields 2 PASS lines (g-zN-closed
  + g-zN). The 26 ARE the DET26 set (PB0/PB1 both cells,
  PBA16 edges + mid 91218, PBB10 edges + mid 91231, quad
  row edges + carry sides 91263/91264 + mids, ring edges
  91391/91392 + 91519/91520 + tail 91556 incl).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P214 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, BM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 73/73, BC 70/70,
  QC 63/63, RC 67/67; C _N decls 73/70/63/67
  match actual (tabc214.py rc=0, sed-clone of r42
  tabc212: same BM/BC shape, label only).
  Code-consts vs A-284 (PBA 74 / PBB 71 / quad 63 /
  T 67): quad + T exact; A/B -1 each is bookkeeping
  (b5 checked via lencode formula, not const pairs);
  byte-coverage proven 84/84 all 4 groups: A 2+9+73,
  B 2+12+70, Q 2+7+8+4+63, R 2+8+7+67
  (0 overlap anywhere; b4/b5 in no const set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=91209 (PB0 sig 4b080000 REPEAT), S1 n=91210
  (fat PB1 sig 8f9b1100 == P213B10sig), A 91211-91226
  PBA16 (sig 8f9b3d01 NEW, mtab b23,34,35,42,43,76-79,
  raw lencode), B 91227-91236 PBB10 single-sig (sig
  8f9b1100 == PB1, mtab b34,35,41-46,80-83, raw
  lencode), Q 91237-91300 QUAD64 single-sig (sig
  8f9b0901 == P213Q, R-paired r1==r3 ce724597c793a218
  x2, 3/4 distinct; shared M7 b48-50,76-79 by
  m=off&15, R8 b34,35,41-46 + tails b80-83 by
  q=off>>4, raw lencode with b5-carry @off26->27),
  R 91301-91556 T-ring STANDARD (whole-tier lencode)
  sig f6b89910 NEW (M8 b6-9,76-79 by COL off&15, R7
  b48-50,72-75 by ROW off>>4, b4=(0x4b+2off)&FF,
  b5=0xc9+(off>=91)+(off>=219)). C blocks carry
  T59340/345/350/365/381/404 py-line mirrors, bounds
  exact, all 6 verified. Insert position exact both
  sides: after T10P213R close, at dispatch tail
  (N-out-of-scope fallthrough follows). Matches A-478
  geometry (PB0 REPEAT, PB1 ==P213B10sig, PBA16 NEW,
  PBB10 ==PB1 single-sig NO pair/C8, QUAD64 R-paired
  r1==r3 with b5-carry c8->c9 @91263->91264, ring
  STANDARD UNPAIRED, lencode 348/348 whole-tier, ring
  edges 91391->91392 + 91519->91520, NO D dips) and
  A-284 (R-pair correction adopted in code, tails 4/4
  distinct f778fa40/7b78af92/3d6e68b8/7ab5df92,
  B10M==QR 12/12 noted, consts stand).
- Quad b5-carry sides confirmed first-hand via the
  lencode formula ((n<<1|1)&FFFF evaluated both pins):
  91263 (off26, ff/c8) -> 91264 (off27, 01/c9); bytes
  EXACT, pins PASS. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 606 add / 0 del; raw
  grep 606 add / 0 del (5 blank-only `+` lines,
  verified bare; 0 blank `-`); normalized (_t/_i/_b/T
  numbers, no-\b BSD-sed variant of b302-validated
  pipeline) del-subset-add 0 missing (del-uniq 0,
  add-uniq 159).
- Wall on band diff added lines (scope a8948f1f..
  936eddc9, 896 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits. Files touched: rgramc.c
  606/0, rgram.py +237/+0 purely additive,
  test_rgram.sh 1/1, PINS +52/+0.
- Tiers: merge-msg +6, code 6 blocks, seal 1260->1266
  +6: all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-478-q606-
  t10p214 verdict CONFIRM (25/25 = 12/12 shape +
  9/9 quad/ring + 4/4 counters; file present,
  counts verified; A-284 corroborates incl-consts
  with -1 bookkeeping resolved + R-pair correction
  adopted + carry sides re-checked above). No
  CONFIRM-P214.md file; A-478 suffices per rule.
  Agrees with cport commit msg (PYID 6264,
  RGRAM 12528).
- Quiz: no conflicting CLAIM/GATE/FLAG on b322. Newest
  PARENT-* is QNUM-05 (w2e Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r42/ (build322.log,
  pyid322, rgram322py/c, cmp322.py/.c, for322-a8948f1f/
  936eddc9, for322-added, pins322.csv/.basen, smoke322,
  tables322.log, tabc214.py, cdiff322, add/delnorm322,
  cdiff322.miss, banddiff322, added322, numstat322).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
