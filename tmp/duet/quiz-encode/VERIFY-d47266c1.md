# VERIFY-d47266c1 b318 T10P210 pins 89817..90164 (1241 tiers): PASS

viewer-r36, first-hand, detached tree NVME tmp/encode-viewer/r36/
tree-d47266c1 @d47266c1 (base 65d48c12 = b317 tip), seat build
build318/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2801560 B, sha256 rgramc 23d71523 / aae d6e27c97
  (BOTH == GATE; both shas cited, sha256).
- RGRAMC-PYID 6160/6160 covered=6160/6160 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12320/12320 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12320/12320 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12320/12320, diff 0).
- PINS-RGRAM cell set-eq 12320/12320 (cmp-identical; GATE
  "6160/6160" = standing half-cell phrasing, full cells 2x
  verified). PINS N-set == for-list 6160/6160.
- PINS 12322 rows = 2 hdr + 12320 (== GATE). For-list +26
  exactly: 89817 89818 89819 89826 89834 89835 89836 89837
  89838 89839 89841 89845 89855 89856 89860 89861 89877
  89892 89893 89908 89909 89983 89984 90111 90112 90164.
  0 removed (== GATE). 6160x2 = 12320 PASS lines. DET26
  note verified: PAIR both cells 89835/89836 + PBC8 one
  pin per distinct sig (89837/38/39/41 = 8b/07/e5/d1 via
  CM order) + quad carry edge 89855/89856 + row edges +
  ring edges 89983/89984 + 90111/90112 (== GATE).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 89817..90164 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P210 C-vs-py mechanical, ALL EXACT: S0/S1
  168-hex-char singletons 1/1 each (sigs f0070000 /
  96e10f00 == GATE); AM 16/16, CM 8/8, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16; AC 76/76, CC 70/70, PC
  81/81, QC 63/63, RC 68/68 (py-hex vs C-decimal
  normalized); P80 2/2 (b4/d4 = 180/212 == GATE); C _N
  decls 76/70/81/63/68 match actual rows (== GATE).
  Code-consts vs A-280 incl 77/71/63/68: quad + T exact;
  A/C -1 each = b5-const-via-lencode bookkeeping (b5
  const bd both, first-hand; == GATE); byte-coverage
  84/84 all 5 groups re-proven first-hand (A 2+6+76, P
  2+1+81, C 2+12+70, Q 2+7+8+4+63, R 2+8+6+68; 0 overlap
  anywhere; b4/b5 in no const set — == GATE exact).
- Dispatch by eye both impls, 7 blocks in order: S0
  n=89817 (PB0 f0070000 NEW) / S1 n=89818 (fat PB1
  96e10f00 NEW); A 89819-89834 PBA16 off=n-89819, mtab
  6B b20,21,76-79, raw lencode; P 89835-89836 PAIR
  off=n-89835, b80=P80[off] + PC consts; C 89837-89844
  PBC8 MULTI-SIG off=n-89837, mtab 12B b0-2,11,18,19,
  24,25,80-83 CM[off] incl sig bytes (4 distinct
  8b980600/07af0500/e57c0600/d1090400, order 0:8b 1:07
  2:e5 3:e5 4:d1 5:07 6:e5 7:07 == GATE exact); Q
  89845-89908 QUAD64 MULTI-SIG off=n-89845 m=off&15
  q=off>>4, shared M7 b20,26,27,76-79 M[m] + R8
  b0-2,11,18,19,24,25 QR[q] (row sigs 07af7d00/4da87c00/
  91fa7e00/d1097c00: b0-2 from QR rows + b3=00 const,
  verified == GATE) + tails b80-83 QT[q]; R 89909-90164
  off=n-89909 c=off&15 r=off>>4 T-ring STANDARD (20th,
  whole-tier lencode), b4=(0x6b+2off)&FF (C: 107 literal
  ==) b5=0xbe+(off>=75)+(off>=203) (C: 190 literal ==),
  M8 b32-35,76-79 by COL c, R6 b24,25,72-75 by ROW r;
  all paylen 84. Sigs first-hand: A=6819fe00 P=43430e00
  R=4da8f007 (== GATE); CC/QC b0-2 absent (multi-sig
  bytes in mtab, == geometry). C-mtab positions ==
  quad-R positions 12/12 set-equal (first-hand == GATE
  == A-280). Counter edges computed first-hand: A/P/C
  b5 const bd (l16 0xBDB7..0xBDE9); Q off10->off11
  (89855->89856) ff/bd->01/be; R off74->75 (89983->
  89984) ff/be->01/bf + off202->203 (90111->90112)
  ff/bf->01/c0; all edge Ns in for-list (== GATE). R
  counter == lencode continuation proven (b4 low-byte
  identity + carry boundaries off>=75/off>=203 derived
  from 0xBE6B+2off crossings — whole-tier lencode ==
  GATE/A-280 348/348). C blocks carry T58320/325/330/
  345/359/375/398 py-line mirrors (7/7 exact == GATE).
  Insert position exact both sides: after T10P209R
  close, at dispatch tail ("N out of scope" + return 2).
  (== GATE.)
- A-470 FINDING re-checked first-hand (REQUIRED item):
  step sides ARE 89855 (off10, ff/bd) -> 89856 (off11,
  01/be) via l16 formula evaluated both pins (bdff /
  be01); code comment "b5-carry @off10" uses source
  convention (== GATE); bytes EXACT, pins PASS
  (both Ns pinned, own-loop oracle-agreeing). No
  DISSENT (A-470 §4 explicit).
- py diff pure addition: rgram.py +268/-0 (0 deletions,
  2 hunks: tables after _T10P209RC close + dispatch in
  main()), test_rgram.sh +1/-1 (for-line only), PINS
  +52/+0. (== GATE.)
- C diff renumber-only + new: numstat 2321/1607; raw
  grep 2321 add / 1607 del (7 bare `+` / 0 bare `-`;
  2314+7=2321 self-consistent total reading == GATE).
  Fine-norm (b302-validated _t/_i/_b/T seds, no-\b
  BSD variant, sign-strip, sort -u): del-uniq 1603 /
  add-uniq 2019 / 0 missing (all == GATE exact under
  blank-INCLUDING variant; r41 INCL like r38/r40;
  EXCL 2018, miss 0 either way — accounting note).
- Wall on band diff added lines (65d48c12..d47266c1,
  2642 added lines == GATE): vendor/disasm 0, depload
  0, /usr/bin/aa 0 (== GATE). Files: rgramc.c 2321/
  1607, rgram.py +268/+0, test_rgram.sh 1/1, PINS
  +52/+0 (== GATE).
- Band composition: d47266c1^ = 581bbd50 single parent;
  581bbd50 = merge 65d48c12 + e1295dde (py partial +7
  tiers +52 pins) (== GATE; cport msg PYID 6160 /
  RGRAM 12320 agrees).
- CONFIRM evidence: A-470-q602-t10p210 verdict CONFIRM
  24/24 = 13/13 shape + 8/8 ring + 3/3 counters +
  finding re-checked above (file present, counts
  verified; == GATE), A-280 corroborates incl-consts
  77/71/63/68 with -1 bookkeeping resolved + tails
  row-shared 4/4 == QT verbatim + R8 UNPAIRED 4/4 +
  NO D dips (== GATE), no DISSENT (CONVERT-01 rule b).
  No CONFIRM-P210.md file (== GATE; A-470 suffices per
  rule). GATE's A-470 cites (PB0/PB1 NEW, PBA16, PAIR
  b80, PBC8 4-sig, QUAD64 row sigs + shared M7, ring
  STANDARD 20th, lencode 348/348 whole-tier, ring
  edges, NO D) + A-280 cites (C8==quad-R 12/12,
  tails row-shared, consts stand) all verbatim in
  files. No FLAG/CLAIM/GATE conflict on b318. GATE's
  "newest PARENT-* QNUM-05" TRUE at filing (GATE born
  15:02:32, QNUM-05 14:14:15, QNUM-06 16:02:56 after;
  birth times first-hand).
- Logs: sweep2 NVME ws tmp/encode-sweep2/r41/ *318*
  files present (28 files).

Agrees with GATE-d47266c1 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r36/
(*318* files).

Verdict: PASS. Ready for parent PV + merge.
