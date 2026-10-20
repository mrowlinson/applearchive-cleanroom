# VERIFY-936eddc9 b322 T10P214 pins 91209..91556 (1266 tiers): PASS

viewer-r37, first-hand, detached tree NVME tmp/encode-viewer/r37/
tree-936eddc9 @936eddc9 (base a8948f1f = b321 tip), seat build
build322/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2836136 B, sha256 rgramc 5719ece4 / aae d6e27c97
  (BOTH == GATE; aae stable, aae.c untouched).
- RGRAMC-PYID 6264/6264 covered=6264/6264 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12528/12528 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12528/12528 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12528/12528, diff 0).
- PINS-RGRAM cell set-eq 12528/12528 (cmp-identical; GATE
  "6264/6264" = standing half-cell phrasing, full cells 2x
  verified). PINS N-set == for-list 6264/6264.
- PINS 12530 rows = 2 hdr + 12528 (+52 vs base 12478).
  For-list +26 exactly: 91209 91210 91211 91218 91226 91227
  91231 91236 91237 91244 91252 91253 91263 91264 91268 91269
  91276 91284 91285 91300 91301 91391 91392 91519 91520 91556.
  0 removed (== GATE verbatim). DET26 shape verified: PB0/
  PB1 both, PBA edges+mid 91218, PBB edges+mid 91231, quad
  4x row edges + carry sides 91263/91264 + mids 91244/91276,
  ring start+edges+tail (== GATE).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 91209..91556 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P214 C-vs-py mechanical, ALL EXACT: S0/S1
  168/168-hex-char singletons (sigs 4b080000 / 8f9b1100 ==
  P213B10sig); AM 16/16, BM 10/10, M 16/16, QR 4/4, QT 4/4,
  RM 16/16, RQ 16/16; AC 73/73, BC 70/70, QC 63/63, RC
  67/67 (py-hex vs C-decimal normalized); C _N decls
  73/70/63/67 match actual rows (== GATE). Const sigs b0-3
  first-hand: A 8f9b3d01, B 8f9b1100, Q 8f9b0901, T
  f6b89910 (== GATE). b4/b5 in no const table (all 4).
  Absence inventory: _T10P214* symbols == known 13-table
  set exactly (py 13 / C 17 = +4 _N — == GATE). QR
  R-paired r1==r3 ce724597c793a218 x2, 3/4 distinct (r0
  3c77e585e7d3680d, r2 426d059977339b1e); QT 4/4 distinct
  f778fa40/7b78af92/3d6e68b8/7ab5df92 (== A-284 verbatim).
  Code-consts vs A-284 incl 74/71/63/67: Q + T exact; A/B
  -1 each = b5-const-via-lencode bookkeeping (b5 const
  c8 both, first-hand; == GATE); B10M==QR 12/12 set-exact
  vs code positions (== GATE/A-284); byte-coverage 84/84
  all 4 groups re-proven first-hand (A 2+9+73, B 2+12+70,
  Q 2+7+8+4+63, R 2+8+7+67; 0 overlap anywhere; b4/b5 in
  no const set — == GATE exact).
- Dispatch by eye both impls, 6 blocks in order: S0
  n=91209 (PB0 4b080000 REPEAT) / S1 n=91210 (fat PB1
  8f9b1100 == P213B10sig); A 91211-91226 PBA16 off=n-91211,
  mtab 9B b23,34,35,42,43,76-79, raw lencode; B 91227-91236
  PBB10 single-sig off=n-91227, mtab 12B b34,35,41-46,80-83,
  raw lencode; Q 91237-91300 QUAD64 R-paired off=n-91237
  m=off&15 q=off>>4, shared M7 b48-50,76-79 M[m] + R8
  b34,35,41-46 QR[q] + tails b80-83 QT[q], raw lencode;
  R 91301-91556 off=n-91301 c=off&15 r=off>>4 T-ring
  STANDARD, b4=(0x4b+2off)&FF (C: 75 literal ==)
  b5=0xc9+(off>=91)+(off>=219) (C: 201 literal ==), M8
  b6-9,76-79 by COL c, R7 b48-50,72-75 by ROW r; all
  paylen 84 (== GATE every value). C blocks carry
  T59340/345/350/365/381/404 py-line mirrors (6/6 exact
  == GATE). Insert position exact both sides: after
  T10P213R close, dispatch tail ("N out of scope" +
  return 2 follows).
- Counter edges computed first-hand: A/B b5 const c8
  whole ranges; Q off26->off27 (91263->91264) ff/c8->
  01/c9 (code comment "b5-carry @off26->27" == GATE);
  R off90->91 (91391->91392) ff/c9->01/ca + off218->219
  (91519->91520) ff/ca->01/cb; all edge Ns in for-list
  (== GATE).
- Quad b5-carry sides re-checked first-hand via l16
  formula evaluated both pins: 91263 (off26, ff/c8) ->
  91264 (off27, 01/c9); bytes EXACT, pins PASS (both Ns
  pinned, own-loop oracle-agreeing). No DISSENT (==
  GATE).
- py diff pure addition: rgram.py +237/-0 (0 deletions),
  test_rgram.sh +1/-1 (for-line only), PINS +52/-0
  (== GATE).
- C diff purely additive: numstat 606/0; raw grep 606
  add / 0 del (5 bare `+`, 0 blank-minus; == GATE).
  Normalized (generic [0-9]+ -> N collapse, cut-c2,
  sort -u): del-uniq 0 / add-uniq 159-INCL (158 EXCL) /
  0 missing (== GATE exact; my INCL file BYTE-EQUAL to
  sweep2 addnorm322 — same note as b320: prose names
  _t/_i/_b/T seds, artifact is digit-collapse).
- Wall on band diff added lines (a8948f1f..936eddc9,
  896 added == GATE; 891 non-blank + 5 bare-plus):
  vendor/disasm 0, depload 0, CT-shim/shebang 0,
  /usr/bin/aa 0 (== GATE). Files: rgramc.c 606/0,
  rgram.py +237/+0, test_rgram.sh 1/1, PINS +52/+0
  (== GATE).
- Tiers: merge-msg +6, code 6 blocks, seal 1260->1266
  +6 (cport msg "1266 tiers sealed"): all agree (== GATE).
- Band composition: 936eddc9^ = e8ed9492 single parent;
  e8ed9492 = merge a8948f1f + 21376730 (py partial +6
  tiers +52 pins) (== GATE; cport msg PYID 6264 /
  RGRAM 12528 agrees).
- CONFIRM evidence: A-478-q606-t10p214 verdict CONFIRM
  25/25 = 12/12 shape + 9/9 quad/ring + 4/4 counters
  (file present, counts verified; == GATE), A-284
  corroborates incl-consts 74/71/63/67 with -1
  bookkeeping resolved + R-pair CORRECTION adopted in
  code (r1==r3 values + r0/r2 + tails verbatim match)
  + B10M==QR 12/12 + VPOS 10/13/21/17 partition-exact
  vs code sets + carry sides + NO D dips (== GATE),
  no DISSENT (CONVERT-01 rule b). No CONFIRM-P214.md
  file (== GATE; A-478 suffices per rule). GATE's
  A-478/A-284 cites (PB0 REPEAT, PB1 ==P213B10sig,
  PBA16 NEW, PBB10 ==PB1 single-sig NO pair/C8, QUAD64
  R-paired r1==r3 with b5-carry c8->c9 @91263->91264,
  ring STANDARD UNPAIRED, lencode 348/348 whole-tier,
  ring edges, NO D) all verbatim in files. No
  FLAG/CLAIM/GATE conflict on b322. GATE's "newest
  PARENT-* QNUM-05" TRUE at filing (GATE born 15:27:14,
  QNUM-05 14:14:15, QNUM-06 16:02:56 after; birth times
  first-hand). Sweep2 logs: 25 *322* files present.
- Notes (not slips): (1) norm-pipeline prose abbreviated
  vs digit-collapse artifact (byte-equal; same as b320).
  (2) wall "896 added lines" = INCL convention here
  (891 non-blank + 5 bare); sweep-r41 odd bands use
  EXCL (b319: 1094, b321: 891) — per-seat convention
  stable (sweep EXCL / sweep2 INCL), values correct
  both.

Agrees with GATE-936eddc9 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r37/
(*322* files).

Verdict: PASS. Ready for parent PV + merge.
