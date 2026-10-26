# VERIFY-99ecfdb8 b323 T10P215 pins 91557..91904 (1272 tiers): PASS

viewer-r38, first-hand, detached tree NVME tmp/encode-viewer/r38/
tree-99ecfdb8 @99ecfdb8 (base 936eddc9 = b322 tip), seat build
build323/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2853000 B, sha256 rgramc 5b5888d7 (first-hand,
  GATE omits) / aae sha1-8 7d8dd3a2 (== GATE stable r39-r42).
- RGRAMC-PYID 6290/6290 covered=6290/6290 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12580/12580 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12580/12580 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12580/12580, diff 0).
- PINS-RGRAM cells set-eq 12580/12580 (cmp-identical; ==
  GATE). PINS N-set == for-list 6290/6290 (== GATE).
- PINS 12582 rows = 2 hdr + 12580 (+52 vs base 12530).
  For-list +26 exactly: 91557 91558 91559 91566 91574 91575
  91579 91584 91585 91592 91600 91601 91608 91616 91617 91624
  91632 91633 91640 91647 91648 91649 91775 91776 91903 91904.
  0 removed (== GATE verbatim). DET26 shape verified: PB0/
  PB1 both, PBA edges+mid 91566, PBB edges+mid 91579, quad
  row edges (91585/600-601/616-617/632-633) + carry sides
  91647/91648 + mids 91592/608/624/640, ring start 91649 +
  edge sides 91775/776 + 91903/904 tail.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 91557..91904 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P215 C-vs-py mechanical, ALL EXACT: S0/S1
  168/168-hex-char singletons (sigs 4b080000 / f89f1000 ==
  GATE); AM 16/16, BM 10/10, M 16/16, QR 4/4, QT 4/4,
  RM 16/16, RQ 16/16; AC 75/75, BC 71/71, QC 63/63, RC
  64/64 (py-hex vs C-decimal normalized); C _N decls
  75/71/63/64 match actual rows (== GATE). Const sigs b0-3
  first-hand: A 64ff0901, B ee3f2100, Q e5fe1302, T
  408b0738 (== GATE). b4/b5 in no const table (all 4).
  Absence inventory: _T10P215* symbols == known 13-table
  set exactly (py 13 / C 17 = +4 _N); no P*/C*/F*/H*/TC*
  symbols either side (grep 0/0 — == GATE). QR
  R-paired r2==r3 a2bc521ae5788f x2, 3/4 distinct (r0
  777c22dabe9d89, r1 5a3cc0dac07b8c); QT 4/4 distinct
  8df0e13d/a1ee58a8/fc3ad4a8/2b3bd4a8, r2/r3 share d4a8
  (== A-285 verbatim). Code-consts vs A-285 incl-consts
  76/72/63/64: Q + T exact; A/B -1 each = b5-const-via-
  lencode bookkeeping (== GATE, P192 precedent); B10M==QR
  11/11 set-exact vs code positions (== GATE/A-285);
  byte-coverage 84/84 all 4 groups re-proven first-hand
  (A 2+7+75, B 2+11+71, Q 2+8+7+4+63, R 2+9+9+64;
  0 overlap anywhere; b4/b5 in no const set).
  M-tails ALL NEW vs P214T 16/16 under both readings
  (RM tails + quad-M tails; == A-479 0/16 + A-285 16/16).
  RM/RQ 16/16 distinct each (UNPAIRED — == memos).
- Dispatch by eye both impls, 6 blocks in order: S0
  n=91557 (PB0 4b080000 REPEAT off=0) / S1 n=91558 (fat
  PB1 f89f1000 NEW off=1); A 91559-91574 PBA16 off=n-91559,
  mtab 7B b9-11,76-79, raw lencode; B 91575-91584 PBB10
  single-sig off=n-91575, mtab 11B b13-19,80-83, raw
  lencode; Q 91585-91648 QUAD64 r2==r3 bottom-paired
  off=n-91585 m=off&15 q=off>>4, shared M8 b20-23,76-79 +
  R7 b13-19 QR[q] + tails b80-83 QT[q], raw lencode; R
  91649-91904 off=n-91649 c=off&15 r=off>>4 T-ring
  STANDARD, b4=(0x03+2off)&FF (C: 3 literal ==)
  b5=0xcc+(off>=127)+(off>=255) (C: 204 literal ==), M9
  b20,21,25-27,76-79 by COL c, R9 b12-15,19,72-75 by ROW
  r; all paylen 84 (== GATE every value). C blocks carry
  T59576/581/586/601/617/640 py-line mirrors (6/6 exact
  == GATE). Insert position exact both sides: after
  T10P214R close, dispatch tail ("N out of scope" +
  return 2 follows).
- Counter edges computed first-hand: A const cb across
  (91559 4f/cb -> 91574 6d/cb, no wrap); B const cb
  across (91575 6f/cb -> 91584 81/cb, no wrap); Q
  off62->off63 (91647->91648) ff/cb->01/cc LAST-CELL
  (code comment "b5-carry last-cell @off62->63" ==
  GATE); R off126->127 (91775->91776) ff/cc->01/cd +
  off254->255 (91903->91904) ff/cd->01/ce last-cell;
  all edge Ns in for-list (== GATE).
- Quad b5-carry sides re-checked first-hand via l16
  formula evaluated both pins: 91647 (off62, ff/cb) ->
  91648 (off63, 01/cc); bytes EXACT, pins PASS (both Ns
  pinned, own-loop oracle-agreeing). No DISSENT (==
  GATE).
- py diff pure addition: rgram.py +236/-0 (0 deletions),
  test_rgram.sh +1/-1 (for-line only), PINS +52/-0
  (== GATE PINS leg; GATE's "py diff +52/-0" names the
  PINS leg — see note 1).
- C diff purely additive: numstat 606/0; raw grep 606
  add / 0 del (5 bare `+`, 0 blank-minus; == GATE).
  Normalized ([0-9]+ -> N collapse, cut-c2, sort -u):
  del-uniq 0 / add-uniq 174-INCL (173 EXCL) / 0 missing
  (GATE 174 == INCL; see note 2).
- Wall on band diff added lines (936eddc9..99ecfdb8,
  895 added == GATE; 890 non-blank + 5 bare-plus):
  vendor/disasm 0, depload 0, CT-shim/shebang 0,
  /usr/bin/aa 0 (== GATE). Files: rgramc.c 606/0,
  rgram.py 236/0, test_rgram.sh 1/1, PINS 52/0
  (== GATE file list).
- Tiers: py-merge msg +6, code 6 blocks, seal 1266->1272
  +6 (cport msg "1272 tiers sealed"): all agree.
- Band composition: 99ecfdb8^ = daa01b6e single parent;
  daa01b6e = merge 936eddc9 + ae5a9305 (py partial +6
  tiers +52 pins) (== GATE; cport msg PYID 6290 /
  RGRAM 12580 agrees).
- CONFIRM evidence: A-479-q607-t10p215 verdict CONFIRM
  25/25 = 12/12 shape + 9/9 quad/ring + 4/4 counters
  (file present, counts verified; == GATE), A-285
  corroborates incl-consts 76/72/63/64 with -1
  bookkeeping resolved + R-pair CORRECTION adopted in
  code (r2==r3 values + r0/r1 + tails verbatim match)
  + B10M==QR 11/11 + VPOS 8/12/21/20 partition-exact
  vs code sets + carry sides + NO D dips (== GATE),
  no DISSENT (CONVERT-01 rule b). No CONFIRM-P215.md
  file (A-479 suffices per rule, same as b322). GATE's
  A-479/A-285 cites (PB0 REPEAT x3, PB1 f89f1000 NEW,
  PBA16 NEW, PBB10 single-sig NO pair/C8, QUAD64
  r2==r3 bottom-paired with b5-carry cb->cc @91647->
  91648 LAST-CELL, ring STANDARD UNPAIRED, M-tails ALL
  NEW 0/16, lencode 348/348 whole-tier, ring edges,
  NO D) all verbatim in files. No FLAG/CLAIM/GATE
  conflict on b323. Sweep logs: 26 *323* files present.
- Notes (not slips): (1) GATE's "py diff +52/-0" sits in
  the PINS bullet and restates the PINS delta (numbers
  exactly right for PINS); rgram.py's own +236/-0 is
  not cited. Standing sweep-r42 phrasing (same in
  b325 GATE) — suggest "PINS diff" + cite rgram.py.
  (2) add-uniq 174 + wall 895 are INCL convention here
  (890/173 EXCL); sweep-r41 odd bands used EXCL —
  sweep-r42 matches sweep2-r42 INCL now. Values correct
  both. (3) aae sha1-8 only + rgramc sha omitted (same
  standing suggestion x5: cite BOTH shas + name digest;
  first-hand rgramc sha256 5b5888d7, 2853000 B).

Agrees with GATE-99ecfdb8 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r38/
(*323* files).

Verdict: PASS. Ready for parent PV + merge.
