# VERIFY-a8948f1f b321 T10P213 pins 90861..91208 (1260 tiers): PASS

viewer-r37, first-hand, detached tree NVME tmp/encode-viewer/r37/
tree-a8948f1f @a8948f1f (base 2f100078 = b320 C tip), seat build
build321/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2835768 B, sha256 rgramc 2435d1e8 (first-hand,
  GATE omits) / aae d6e27c97 (stable) / aae sha1-8 7d8dd3a2
  (== GATE).
- RGRAMC-PYID 6238/6238 covered=6238/6238 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12476/12476 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12476/12476 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12476/12476, diff 0).
- PINS-RGRAM cell set-eq 12476/12476 (cmp-identical).
  PINS N-set == for-list 6238/6238.
- PINS 12478 rows = 2 hdr + 12476 (+52 vs base 12426).
  For-list +26 exactly: 90861 90862 90863 90870 90878 90879
  90880 90888 90889 90896 90904 90905 90912 90920 90921 90928
  90936 90937 90944 90952 90953 91007 91008 91135 91136 91208.
  0 removed (== GATE verbatim).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 90861..91208 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P213 C-vs-py mechanical, ALL EXACT: S0/S1
  168/168-hex-char singletons (sigs 4b080000 / 837b1300 ==
  GATE); AM 16/16, BM 10/10, M 16/16, QR 4/4, QT 4/4, RM
  16/16, RQ 16/16; AC 74/74, BC 69/69, QC 63/63, RC 64/64
  (py-hex vs C-decimal normalized); C _N decls 74/69/63/
  64 match actual rows (== GATE). Const sigs b0-3
  first-hand: A 837b0b01, B 8f9b1100, Q 8f9b0901, T
  d0cf4b1c (== GATE). b4/b5 in no const table (all 4).
  Absence inventory: _T10P213* symbols == known 13-table
  set exactly (py 13 / C 17 = +4 _N; no P/C/F/H/TC either
  side — == GATE). QR UNPAIRED 4/4 distinct; QT tails
  4076c7ad/5774bc0b/bab1bb84/8d337c2f (== GATE/A-283).
  Code-consts vs A-283 incl 75/69/64/64: B + T exact
  (B b5-carry in-table, first B-carry; T counter +0);
  A/Q -1 each = b5-const-via-lencode bookkeeping (b5
  const c5/c6, first-hand; == GATE); 84-64=20 = T VPOS
  first-hand from RC table (A-283 CORRECTION holds, ==
  GATE); byte-coverage 84/84 all 4 groups re-proven
  first-hand (A 2+8+74, B 2+13+69, Q 2+8+7+4+63, R
  2+8+10+64; 0 overlap anywhere; b4/b5 in no const set).
- Dispatch by eye both impls, 6 blocks in order: P2130
  n==90861 (PB0 4b080000 NEW) / P2131 n==90862 (fat PB1
  837b1300 NEW); A 90863-90878 PBA16 off=n-90863, mtab
  8B b24-27,76-79, raw lencode; B 90879-90888 PBB10
  single-sig off=n-90879, mtab 13B b20,21,25-31,80-83,
  raw lencode; Q 90889-90952 QUAD64 unpaired off=n-90889
  m=off&15 q=off>>4, shared M8 b32-35,76-79 M[m] + R7
  b24-30 QR[q] + tails b80-83 QT[q], raw lencode; R
  90953-91208 off=n-90953 c=off&15 r=off>>4 T-ring
  STANDARD, b4=(0x93+2off)&FF (C: 147 literal ==)
  b5=0xc6+(off>=55)+(off>=183) (C: 198 literal ==), M8
  b32,37-39,76-79 by COL c, R10 b14,15,21-23,31,72-75
  by ROW r; all paylen 84 (== GATE every value). C
  blocks carry T59102/107/112/127/143/166 py-line
  mirrors (6/6 exact == GATE). Insert position exact
  both sides: dispatch tail ("N out of scope" + return
  2 follows).
- Counter edges computed first-hand: A const c5
  (90863 df/c5 -> 90878 fd/c5, no wrap); B off0->off1
  (90879->90880) ff/c5->01/c6, destination convention
  explicit sides (code comment "b5-carry @off0->1" ==
  GATE); Q const c6 (90889 13/c6 -> 90952 91/c6, no
  wrap); R off54->55 (91007->91008) ff/c6->01/c7 +
  off182->183 (91135->91136) ff/c7->01/c8; all edge Ns
  in for-list (== GATE).
- py diff pure addition: rgram.py +237/-0 (0 deletions),
  test_rgram.sh +1/-1 (for-line only), PINS +52/-0
  (GATE's "+52/-0" == PINS leg).
- C diff pure-add: numstat 606/0; raw grep 606 add / 0
  del (5 bare `+`, 0 blank-minus; == GATE). Coarse-norm
  ([0-9]+ -> N, cut-c2, sort -u): del-uniq 0 / add-uniq
  174 / 0 missing (all == GATE exact).
- Wall on band diff added lines (2f100078..a8948f1f,
  891 non-blank added == GATE; 896 incl 5 bare-plus):
  vendor/disasm 0, depload 0, CT-shim/shebang 0,
  /usr/bin/aa 0 (== GATE). Files: rgramc.c 606/0,
  rgram.py +237/+0, test_rgram.sh 1/1, PINS +52/+0.
- Band composition: a8948f1f^ = db313a0f single parent;
  db313a0f = merge 2f100078 + b4c7b051 (py partial +6
  tiers +52 pins) (== GATE; cport msg PYID 6238 /
  RGRAM 12476 agrees).
- CONFIRM evidence: A-475-q605-t10p213 predictive
  verdict CONFIRM 28/28 = 13/13 shape + 10/10 quad/ring
  + 5/5 counters (file present, counts verified; ==
  GATE), A-283 corroborates (VPOS 9/15/20/20
  partition-exact vs code sets, B-carry explicit-sides,
  R-sharing 10/11 EXACT vs code positions [shared
  25-30,80-83; quad-only 24; B-only 20,21,31], tails
  == QT verbatim, consts 75/69/64/64 incl, T-VPOS
  CORRECTION 18->20 re-tag only counts-stand,
  edges, NO D dips; == GATE), no DISSENT (CONVERT-01
  rule b). GATE's A-475/A-283 cites (PBA b4+M8, PBB10
  single-sig 10/10 diverge NO pair/C8, QUAD64 M8
  shared + R7 UNPAIRED 4/4 + R-sharing 10/11 + tails
  4/4, T-ring STANDARD M8xCOL + R10xROW UNPAIRED 16,
  M-tails ALL NEW 0/16, NO D) all verbatim in files.
  No FLAG/CLAIM/GATE conflict on b321. Sweep logs: 27
  *321* files present.
- Notes (not slips): (1) wall "891 added lines" =
  non-blank convention (896 incl 5 bare-plus); value
  correct under EXCL reading (same as b319). (2) aae
  digest sha1-8 cited per sweep-r41 style (no sha256);
  sha256 stability corroborated (d6e27c97 == all prior
  cites). (3) rgramc sha256 omitted by GATE, recorded
  first-hand 2435d1e8 (standing r36 suggestion x4:
  cite BOTH shas).

Agrees with GATE-a8948f1f (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r37/
(*321* files).

Verdict: PASS. Ready for parent PV + merge.
