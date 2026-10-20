# VERIFY-cd1943ec b315 T10P207 pins 88773..89120 (1220 tiers): PASS

viewer-r36, first-hand, detached tree NVME tmp/encode-viewer/r36/
tree-cd1943ec @cd1943ec (base 74274d93 = b314 tip), seat build
build315/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2767240 B, sha256 rgramc c2cff2e6 / aae d6e27c97
  first-hand. GATE cites aae 7d8dd3a2 only: == my aae SHA-1
  first8 (algo undisclosed in this GATE; sibling r40 GATEs
  document SHA-1 — note, NOT a slip: value correct). Stable/
  bit-identical claim CORROBORATED: aae.c untouched
  c8b4a6a6..cd1943ec (git-empty) + my sha256 d6e27c97 == r39
  b313 cite. GATE omits rgramc sha again (standing suggestion
  stands: cite both shas).
- RGRAMC-PYID 6082/6082 covered=6082/6082 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12164/12164 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12164/12164 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12164/12164).
- PINS-RGRAM cell set-eq 12164/12164 (cmp-identical).
  PINS N-set == for-list 6082/6082 (== GATE "6082/6082").
- PINS 12166 rows = 2 hdr + 12164 (== GATE; +52 vs base).
  For-list +26 exactly: 88773 88774 88775 88782 88790 88791
  88793 88795 88800 88801 88816 88817 88831 88832 88833
  88848 88849 88864 88865 88896 88959 88960 89024 89087
  89088 89120. 0 removed (== GATE). 6082x2 = 12164 PASS.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 88773..89120 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P207 C-vs-py mechanical, 19-table ALL EXACT: S0/S1
  168-hex-char singletons 1/1 each (sigs 94070000 /
  e0300f00 == GATE); AM 16/16, FM0 4/4, FM1 6/6, M 16/16,
  QR3 2/2, QT3 2/2, RM 16/16, RQ 16/16; AC 75/75, FC0
  71/71, FC1 71/71, QC1 76/76, QC2 76/76, QC3 66/66, RC
  66/66 (py-hex vs C-decimal normalized); FS 10/10 + FO
  10/10 (order f4,f4,7a,7a,f4,7a,7a,7a,f4,7a == GATE);
  C _N decls 75/71/71/76/76/66/66 match actual rows
  (== GATE). Absent-inventory grep both sides: no B/BC/BM/
  Q/QC/QR/QT/CM/CC/TC/QR1/QT1/QR2/QT2 (== GATE). No b4/b5
  entry in any of the 7 const tables (first-hand); excl
  75/71/71/76/76/66/66 + b5-where-const (A/F0/F1/H1 +1,
  H2 +0 carry, H3 +1 const-b6, R +0) = incl 76/72/72/77/
  76/67/66 == memo (== GATE reconciliation).
- Dispatch by eye both impls, 8 blocks in order: S0 n=88773
  / S1 n=88774 singleton-const (offs 0/1); A 88775-88790
  PBA16 off=n-88775, mtab 7B b9-11,76-79, raw lencode;
  F 88791-88800 FRAG10 off=n-88791, sigtag pay[0]==FS[off],
  k=FO[off], 0xF4->FM0[k]/FC0 else 0x7A->FM1[k]/FC1 (C:
  244/122 literals ==), same M11 template b13-19,80-83
  both; H1 88801-88816 / H2 88817-88832 shared M6
  b20,21,76-79 positional M[off]; H3 88833-88864 mini-quad
  m=off&15 h=off>>4, shared M6 M[m] + QR3[h] R6 b13-15,
  17-19 (b16 gap) + QT3[h] b80-83 per half; R 88865-89120
  off=n-88865 c=off&15 r=off>>4 T-ring TRANSPOSED,
  b4=(0x43+2off)&FF (C: 67 literal ==) b5=0xB6+(off>=95)+
  (off>=223) (C: 182 literal ==), M9 b20,21,25-27,76-79
  by SLOT c, Q7 b0,11,19,72-75 by ROW r; all paylen 84.
  Sigs first-hand: A=5e0ff300 F0=f4300f00 F1=7a980700
  H1/H3=a2877900 H2=440ff300 (== GATE); R b1-3=e22a0d
  (b0 absent from RC, in Q) + RQ-b0 10-sig e4/e5/e6/e7/
  e9/ec/ed/ef/f1/f3 (distinct set first-hand == GATE;
  row map e4/e5/e5/e6/e6/e7/e9/ec/ec/ed/ed/ef/ef/f1/f3/
  f3 == A-459 r0..r15 verbatim + block sizes 16/32/32/
  16/16/32/32/32/16/32 == code comment == A-277).
  Counter edges computed first-hand: A b5 const b5
  (0xB58F..0xB5AD); F const b5 (0xB5AF..0xB5C1); H1
  const b5 (0xB5C3..0xB5E1); H2 off14->15 (88831->88832)
  ff/b5->01/b6; H3 const b6 (0xB603..0xB641); R off94->95
  (88959->88960) ff/b6->01/b7 + off222->223 (89087->89088)
  ff/b7->01/b8; all edge Ns in for-list (== GATE). C
  blocks carry T57451/456/461/476/506/521/536/559 py-line
  mirrors (8/8 exact, targets verified == GATE). Insert
  position exact both sides: dispatch tail ("N out of
  scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +330/-0 (0 deletions,
  2 hunks: tables after _T10P206RC close + dispatch in
  main()), test_rgram.sh +1/-1 (for-line only), PINS
  +52/+0. (GATE "py diff +52/-0" = PINS leg; rgram.py
  shape verified first-hand.)
- C diff renumber-only + new: numstat 2531/1585; raw grep
  2523 non-blank add + 8 bare `+` / 1585 del / 0 blank `-`
  (2523+8=2531 consistent; GATE "2523 add (incl 8 blank-
  plus)" == r34-precedent convention x4, CORRECT not a
  slip). Coarse-norm ([0-9]+ -> N, cut-c2, sort -u):
  del-uniq 1036 / add-uniq 1236-EXCL (1237 INCL: one
  empty-line uniq entry from bare `+`; miss 0 either way)
  / 0 missing (all == GATE exact under EXCL variant).
- Wall on band diff added lines (74274d93..cd1943ec):
  vendor/disasm 0, depload 0, /usr/bin/aa 0, CT-shim 0,
  shebang 0, over 2914-line added scope (GATE "2906" =
  non-blank count, same convention; my scope stronger,
  still 0). Files: rgramc.c 2531/1585, rgram.py +330/+0,
  test_rgram.sh 1/1, PINS +52/+0 (== GATE).
- Band composition: cd1943ec^ = 8af9ec5f single parent;
  8af9ec5f = merge 74274d93 + 98380946 (py partial +8
  tiers +52 pins) (== GATE; cport msg PYID 6082 / RGRAM
  12164 agrees).
- CONFIRM evidence: A-459-q439-t10p207 verdict CONFIRM
  28/28 (file present; shape/mid/ring/counters + TBDs
  resolved §1/§2; ring r0..r15 sig rows reproduce
  verbatim row-by-row first-hand; NO D dips; == GATE),
  A-277 corroborates same tier (shape + H-shared + motif
  ring + edges CONFIRM, incl consts 76/72/72/77/76/67/66
  == my reconciliation, 5-tag b5 CORRECTION counts-stand,
  FRAG f4/7a positions per-N == FS order, NO D dips;
  == GATE), no DISSENT (CONVERT-01 rule b). H32 2-halves
  cut (QR3 127c67c317bb/b6fcd2d05bb6 + tails 2/2 ==
  GATE) resolves A-459's 4-row "3/4 distinct" framing,
  corroborated by A-277's independent bed (2/2 halves
  exact) + GREEN both halves (own-loop every-N 348/0;
  h0 88833..88848 / h1 88849..88864 boundary Ns pinned;
  == GATE).
- Quiz: no FLAG on b315/cd1943ec (flag inventory clean);
  GATE-27068708 cites cd1943ec as diff-base only ("Base
  cd1943ec (b315 tip)", wall scope cd1943ec..); sweep2-
  HANDOFF-r39 "Odds = sweep turf" verbatim; b314 "NOT
  gated" = standing turf-note convention (b310/b312
  precedent, r35-ruled CORRECT). (== GATE.)
- Logs: sweep NVME ws tmp/encode-sweep/r40/ *315* files
  present (26 files; build/pyid/rgram/smoke/tables/
  tabaudit/cdiff/banddiff/added/pins/for legs all there;
  pyid agrees 6082).

Agrees with GATE-cd1943ec (PASS-functional) on every
verdict-relevant leg. 3 prose notes, 0 slips (algo-
undisclosed aae sha value-correct; rgramc sha omitted
again; EXCL/INCL add-uniq accounting). Logs: NVME ws
tmp/encode-viewer/r36/ (*315* files).

Verdict: PASS. Ready for parent PV + merge.
