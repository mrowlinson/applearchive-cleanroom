# VERIFY-65d48c12 b317 T10P209 pins 89469..89816 (1234 tiers): PASS

viewer-r36, first-hand, detached tree NVME tmp/encode-viewer/r36/
tree-65d48c12 @65d48c12 (base 27068708 = b316 tip), seat build
build317/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2784632 B, sha256 rgramc fe223940 / aae d6e27c97
  first-hand. GATE cites aae 7d8dd3a2 only: == my aae SHA-1
  first8 (algo undisclosed again — note, NOT a slip: value
  correct). Stable/bit-identical claim CORROBORATED: my aae
  sha256 d6e27c97 == b313/b315/b316 first-hand builds. GATE
  omits rgramc sha again (standing suggestion stands).
- RGRAMC-PYID 6134/6134 covered=6134/6134 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12268/12268 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12268/12268 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12268/12268).
- PINS-RGRAM cell set-eq 12268/12268 (cmp-identical).
  PINS N-set == for-list 6134/6134 (== GATE).
- PINS 12270 rows = 2 hdr + 12268 (== GATE; +52 vs base).
  For-list +26 exactly: 89469 89470 89471 89472 89478
  89486 89487 89488 89489 89492 89496 89497 89512 89513
  89528 89529 89544 89545 89560 89561 89599 89600 89664
  89727 89728 89816. 0 removed (== GATE). 6134x2 = 12268
  PASS lines.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 89469..89816 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P209 C-vs-py mechanical, 15-table ALL EXACT: S0/S1
  168-hex-char singletons 1/1 each (sigs 98070000 /
  bfab0e00 == GATE); AM 16/16, CM 8/8, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16; AC 74/74, CC 69/69, PC
  81/81, QC 63/63, RC 68/68 (py-hex vs C-decimal
  normalized); P80 2/2 (0x08/0x28 == GATE); C _N decls
  74/69/81/63/68 match actual rows (== GATE). Absent-
  inventory grep both sides: no B/BC/BM/F/FS/FO/FM0/FM1/
  FC0/FC1/H/QC1/QC2/QC3/QR1/QT1/QR2/QT2/QR3/QT3/TC/T
  (== GATE). No b4/b5 entry in any of the 5 const tables
  (first-hand); excl 74/69/63/68 (A/C/Q/R) + b5-where-
  const (A +0 carry, C +1 const-bb, Q +1 const-bb, R +0
  counter) = incl 74/70/64/68 == memo (== GATE
  reconciliation). PAIR PC 81 in-table; no memo incl
  count exists (A-469 VPOS [80]+b4 only — GATE's
  characterization accurate).
- Dispatch by eye both impls, 7 blocks in order: S0
  n=89469 (PB0 98070000 REPEAT P208) / S1 n=89470 (fat
  PB1 bfab0e00); A 89471-89486 PBA16 off=n-89471, mtab
  8B b48-51,76-79, raw lencode (comment "b5-carry @off0"
  = source-cell label, see FINDING); P 89487-89488 PAIR
  off=n-89487, b80=P80[off] + PC consts; C 89489-89496
  PBC8 off=n-89489, mtab 13B b23,35,45-51,80-83; Q
  89497-89560 QUAD64 off=n-89497 m=off&15 q=off>>4, M6
  b6,7,76-79 M[m] + R9 b23,35,45-51 QR[q] + tails b80-83
  QT[q]; R 89561-89816 off=n-89561 c=off&15 r=off>>4
  T-ring TRANSPOSED + value-crossover, b4=(0xb3+2off)&FF
  (C: 179 literal ==) b5=0xbb+(off>=39)+(off>=167) (C:
  187 literal ==), M8 b13-15,17,76-79 (b16 gap) by COL
  c, Q6 b6,7,72-75 by ROW r; all paylen 84. Sigs
  first-hand: A=bfabf200 P=bfab0e00 C=bfab0a00 Q=
  f7bbaa00 R=7cbfab0a (R single-sig b0 const ==
  GATE). QUAD64 middle-paired r1==r2 913452d700b18b6770
  3/4 distinct + tails 4/4 0696ac60/ebc705a9/1bc805a9/
  50ee0894, r1/r2 share last 2B 05a9 (== GATE ==
  A-279 fix). Counter edges computed first-hand: A
  off0->off1 (89471->89472) ff/ba->01/bb; P const bb
  (0xBB1F..0xBB21); C const bb (0xBB23..0xBB31); Q
  const bb (0xBB33..0xBBB1); R off38->39 (89599->89600)
  ff/bb->01/bc + off166->167 (89727->89728) ff/bc->01/
  bd; all edge Ns in for-list (== GATE). Quad quarter
  boundaries 89497/512/13/28/29/44/45/60 all pinned.
  C blocks carry T58052/057/062/077/091/107/130 py-line
  mirrors (7/7 exact == GATE). Insert position exact
  both sides: dispatch tail ("N out of scope" + return
  2). (== GATE.)
- py diff pure addition: rgram.py +268/-0 (0 deletions,
  2 hunks: tables after _T10P208RC close + dispatch in
  main()), test_rgram.sh +1/-1 (for-line only), PINS
  +52/+0. (GATE "py diff +52/-0" = PINS leg; rgram.py
  shape verified first-hand.)
- C diff renumber-only + new: numstat 2314/1600; raw grep
  2307 non-blank add + 7 bare `+` / 1600 del / 0 blank `-`
  (2307+7=2314 consistent; GATE "2307 add (incl 7 blank-
  plus)" == r34-precedent convention x5, CORRECT not a
  slip). Coarse-norm ([0-9]+ -> N, cut-c2, sort -u):
  del-uniq 1049 / add-uniq 1216-EXCL (1217 INCL; miss 0
  either way) / 0 missing (all == GATE exact under EXCL
  variant).
- Wall on band diff added lines (27068708..65d48c12):
  vendor/disasm 0, depload 0, /usr/bin/aa 0, CT-shim 0,
  shebang 0, over 2635-line added scope (GATE "2628" =
  non-blank count, same convention; my scope stronger,
  still 0). Files: rgramc.c 2314/1600, rgram.py +268/+0,
  test_rgram.sh 1/1, PINS +52/+0 (== GATE).
- Band composition: 65d48c12^ = fc304cf8 single parent;
  fc304cf8 = merge 27068708 + 52672313 (py partial +7
  tiers +52 pins) (== GATE; cport msg PYID 6134 / RGRAM
  12268 agrees).
- CONFIRM evidence: A-469-q601-t10p209 BACKFILL verdict
  CONFIRM 24/24 + FINDING (12/12+finding shape, 7/7
  ring, 5/5 counters; file present, counts verified;
  == GATE) with FINDING independently re-checked
  first-hand per §4 REQUIRED (pins-vs-oracle: edge IS
  89471->89472 ff/ba->01/bb destination-off1, both Ns
  pinned, own-loop oracle-agreeing 348/0; Q "@off0"
  label = source cell, bytes exact; == GATE), A-279
  corroborates same tier (shape + quad + motif ring +
  edges CONFIRM, incl consts 74/70/64/68 == my
  reconciliation, 3-tag b5 CORRECTION counts-stand,
  r1/r2 tails 2B fix == QT exactly, NO D dips; ==
  GATE), no DISSENT (A-469 §4 explicit + CONVERT-01
  rule b). GATE's geometry cites (PBA VPOS b4+M8,
  PAIR b80 tab, PBC8 VPOS b4+M13, QUAD64 middle-paired
  r1==r2 + tails 4/4 + r1/r2 2B share, ring TRANSPOSED
  19th + value-crossover IN PLACE, M-tails NEW 0/16,
  NO D) all verbatim in files.
- Quiz: no FLAG on b317/65d48c12 (flag inventory clean);
  GATE-d47266c1 cites 65d48c12 as diff-base only ("Base
  65d48c12 (b317 tip)", wall scope 65d48c12..); b316
  "NOT gated" = standing turf-note convention (== GATE).
- Logs: sweep NVME ws tmp/encode-sweep/r40/ *317* files
  present (26 files).

Agrees with GATE-65d48c12 (PASS-functional) on every
verdict-relevant leg. 4 prose notes, 0 slips (algo-
undisclosed aae sha value-correct; rgramc sha omitted
again; EXCL/INCL add-uniq accounting; precedent-ruled
"incl N blank-plus" phrasing). Logs: NVME ws tmp/encode-
viewer/r36/ (*317* files).

Verdict: PASS. Ready for parent PV + merge.
