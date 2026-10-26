# VERIFY-f0b205de b325 T10P217 pins 92253..92600 (1284 tiers): PASS

viewer-r38, first-hand, detached tree NVME tmp/encode-viewer/r38/
tree-f0b205de @f0b205de (base 35792e99 = b324 tip), seat build
build325/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2870328 B, sha256 rgramc 0d8f04fa (first-hand,
  GATE omits) / aae sha1-8 7d8dd3a2 (== GATE stable r39-r42).
- RGRAMC-PYID 6342/6342 covered=6342/6342 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12684/12684 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12684/12684 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12684/12684, diff 0).
- PINS-RGRAM cells set-eq 12684/12684 (cmp-identical; ==
  GATE). PINS N-set == for-list 6342/6342 (== GATE).
- PINS 12686 rows = 2 hdr + 12684 (+52 vs base 12634).
  For-list +26 exactly: 92253 92254 92255 92270 92271 92272
  92273 92276 92277 92280 92281 92287 92288 92296 92297 92312
  92313 92328 92329 92344 92345 92415 92416 92543 92544 92600.
  0 removed (== GATE verbatim). Shape verified: PB0/PB1
  both, PBA edges only (92255/92270, no mid — FRAG takes
  the slots), FRAG offs 0,1,2,5,6,9 = both pair-like +
  singleton @off5 + 3 of 7 M13 cells, quad start + carry
  sides 92287/92288 + row edges 92296-97/312-13/328-29 +
  end 92344, ring start 92345 + edge sides 92415/416 +
  92543/544 + tail 92600.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 92253..92600 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P217 C-vs-py mechanical, ALL EXACT (18-table,
  FRAG replaces B): S0/S1 168/168-hex-char singletons
  (sigs 9e100000 / 4ab22600 == GATE); AM 16/16, FM0 2/2
  ("95","b5" == GATE k=0,1), FM1 7/7 (13B rows == GATE),
  M 16/16, QR 4/4, QT 4/4, RM 16/16, RQ 16/16; AC 75/75,
  FC0 81/81, FC1 69/69, FC2 82/82, QC 65/65, RC 70/70
  (py-hex vs C-decimal normalized); C _N decls
  75/81/69/82/65/70 match actual rows (== GATE); FS/FO
  10/10 EXACT (py-int vs C-long: FS 26,26,16,16,16,1e,
  16,16,16,16 + FO 0,1,0,1,2,0,3,4,5,6 — == A-287 layout
  verbatim). Const sigs b0-3 first-hand: A 4ab21602, F0
  4ab22600, F1 4ab21600, F2 4ab21e00, Q ae246b01, T
  fe4ab216 (== GATE). b4/b5 in no const table (all 6).
  Absence inventory: _T10P217* symbols == known 18-table
  set exactly (py 18 / C 24 = +6 _N); no B*/P*/C*/H*/TC*
  symbols either side (grep 0/0 — == GATE). QR
  TRIPLE-PAIRED r0==r2==r3 58958bd1ffff9c x3, 2/4
  distinct (r1 18aca8917e0f73); QT 4/4 distinct
  5ee9875d/97eccbbd/bde9875d/ece9875d, r0/r2/r3 share
  e9875d (== A-287 verbatim). Code-consts vs A-287 incl
  76/70/65/70: Q + T exact; A -1 (75 = 76-1) + F16 -1
  (FC1 69 = 70-1) = b5-const-via-lencode bookkeeping
  (== GATE, P192 precedent; see note 1); byte-coverage
  84/84 all 6 groups re-proven first-hand (A 2+7+75, F0
  2+1+81, F1 2+13+69, F2 2+82, Q 2+6+7+4+65, R 2+6+6+70;
  0 overlap anywhere; b4/b5 in no const set).
  FC0 81 = 84-2-1 + FC2 82 = 84-1-1 arithmetic confirmed
  (== GATE); VPOS-T 14 (== GATE/A-287). M-tails ALL NEW
  vs P216T 16/16 (0/16 shared — == A-483/A-287). RM/RQ
  16/16 distinct each (UNPAIRED — == memos).
- Dispatch by eye both impls, 6 blocks in order: S0
  n=92253 (PB0 9e100000 NEW off=0) / S1 n=92254 (fat PB1
  4ab22600 ==P216PB1 off=1); A 92255-92270 PBA16
  off=n-92255, mtab 7B b48-50,76-79, raw lencode; F
  92271-92280 FRAG off=n-92271, sigtag pay[2]==FS[off] +
  k=FO[off]: 0x26 -> FM0[k] 1B pay[80] + FC0, 0x16 ->
  FM1[k] 13B b23,35,45-51,80-83 + FC1, 0x1e -> FC2,
  else fail (C: 38/22/30 literals ==; snprintf %02lx
  for mtab0 ==); Q 92281-92344 QUAD64 triple-paired
  off=n-92281 m=off&15 q=off>>4, shared M6 b6,7,76-79 +
  R7 b35,46,47,48-51 QR[q] + tails b80-83 QT[q], raw
  lencode; R 92345-92600 off=n-92345 c=off&15 r=off>>4
  T-ring STANDARD, b4=(0x73+2off)&FF (C: 115 literal ==)
  b5=0xd1+(off>=71)+(off>=199) (C: 209 literal ==), M6
  b13,14,76-79 by COL c, R6 b6,7,72-75 by ROW r; all
  paylen 84 (== GATE every value). C blocks carry
  T60091/096/101/116/148/171 py-line mirrors (6/6 exact
  == GATE). Insert position exact both sides: after
  T10P216R close, dispatch tail ("N out of scope" +
  return 2 follows).
- Counter edges computed first-hand: A const d0 across
  (92255 bf/d0 -> 92270 dd/d0, no wrap); F const d0
  across incl singleton @off5 (92271 df/d0 -> 92276
  e9/d0 -> 92280 f1/d0, no wrap); Q off6->off7
  (92287->92288) ff/d0->01/d1 (code comment "b5-carry
  @off6->7" == GATE); R off70->71 (92415->92416)
  ff/d1->01/d2 + off198->199 (92543->92544) ff/d2->01/d3;
  all edge Ns in for-list (== GATE).
- Quad b5-carry sides re-checked first-hand via l16
  formula evaluated both pins: 92287 (off6, ff/d0) ->
  92288 (off7, 01/d1); bytes EXACT, pins PASS (both Ns
  pinned, own-loop oracle-agreeing). No DISSENT (==
  GATE).
- py diff pure addition: rgram.py +294/-0 (0 deletions),
  test_rgram.sh +1/-1 (for-line only), PINS +52/-0
  (PINS leg == GATE; "py diff +52/-0" names the PINS
  leg — standing sweep-r42 phrasing, see b323 note).
- C diff purely additive: numstat 813/0; raw grep 813
  add / 0 del (5 bare `+`, 0 blank-minus; == GATE).
  Normalized ([0-9]+ -> N collapse, cut-c2, sort -u):
  del-uniq 0 / add-uniq 189-INCL (188 EXCL) / 0 missing
  (GATE 189 == INCL; sweep-r42 INCL standing).
- Wall on band diff added lines (35792e99..f0b205de,
  1160 added == GATE; 1155 non-blank + 5 bare-plus):
  vendor/disasm 0, depload 0, CT-shim/shebang 0,
  /usr/bin/aa 0 (== GATE). Files: rgramc.c 813/0,
  rgram.py 294/0, test_rgram.sh 1/1, PINS 52/0
  (== GATE file list; 813+294+1+52 = 1160 exact).
- Tiers: py-merge msg +6, code 6 blocks, seal 1278->1284
  +6 (cport msg "1284 tiers sealed"): all agree (GATE
  carries no separate tiers bullet; facts agree).
- Band composition: f0b205de^ = 0c2f0098 single parent;
  0c2f0098 = merge 35792e99 + b313e7f3 (py partial +6
  tiers +52 pins) (== GATE; cport msg PYID 6342 /
  RGRAM 12684 agrees).
- CONFIRM evidence: A-483-q609-t10p217 verdict CONFIRM
  27/27 = 14/14 shape + 9/9 quad/ring + 4/4 counters
  (file present, counts verified; == GATE), A-287
  corroborates incl-consts 76/70/65/70 with -1
  bookkeeping resolved (A + F16) + FRAG layout EXACT
  (FS/FO verbatim incl singleton @92276) + triple-pair
  values + r1 + tails verbatim + VPOS 8/14/19/14
  partition-exact vs code sets + carry edges + NO D
  dips (== GATE), no DISSENT (CONVERT-01 rule b). No
  CONFIRM-P217.md file (A-483 suffices per rule). GATE's
  A-483/A-287 cites (PB0 NEW, PB1 ==P216PB1, PBA16 ==
  P216PBA, FRAG uneven 3-sig EXACT NO pair/C8/B10,
  QUAD64 triple-paired first-triple, tails shared
  e9875d, ring STANDARD UNPAIRED, M-tails 0/16, lencode
  348/348, ring edges, NO D) all verbatim in files. No
  FLAG/CLAIM/GATE conflict on b325. b324 base = sweep2
  turf (GATE-35792e99 filed by sweep2-r43 — confirmed),
  diff-base only. Sweep logs: 26 *325* files present.
- Notes (not slips): (1) "memo code 75/70 (A/F16)"
  compresses A's code-excl (75) with F16's memo-incl
  (70); parallel code-excl pair is 75/69, memo-incl
  pair 76/70 — all four values exact and the +1
  reconciliation arithmetic in the same sentence is
  correct (first-hand bytes verify). Suggest explicit
  code/memo pairs (75/76, 69/70). (2) "py diff +52/-0"
  = PINS leg, rgram.py's own +294/-0 uncited (standing
  sweep-r42 phrasing, same as b323). (3) add-uniq 189
  + wall 1160 are INCL (188/1155 EXCL) — sweep-r42
  INCL standing. (4) aae sha1-8 only + rgramc sha
  omitted (standing suggestion x6: cite BOTH + name
  digest; first-hand rgramc sha256 0d8f04fa, 2870328 B).

Agrees with GATE-f0b205de (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r38/
(*325* files).

Verdict: PASS. Ready for parent PV + merge.
