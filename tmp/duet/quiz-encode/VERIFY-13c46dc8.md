# VERIFY-13c46dc8 b312 T10P204 pins 87729..88076 (1196 tiers): PASS

viewer-r35, first-hand, detached tree NVME tmp/encode-viewer/r35/
tree-13c46dc8 @13c46dc8 (base bf0ee03b = b311 tip), seat build
build312/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2716056 B, sha256 rgramc b894500c / aae d6e27c97
  (BOTH == GATE).
- RGRAMC-PYID 6004/6004 covered=6004/6004 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 12008/12008 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 12008/12008 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (12008/12008).
- PINS-RGRAM cell set-eq 12008/12008 (cmp-identical).
  PINS N-set == for-list 6004/6004 (== GATE "6004/6004";
  standing half-cell phrasing, full cells 2x verified).
- PINS 12010 rows = 2 hdr + 12008 (== GATE). For-list +26
  exactly: 87729 87730 87731 87738 87746 87747 87748
  87749 87750 87753 87756 87757 87772 87773 87788 87789
  87804 87807 87808 87820 87821 87935 87936 88063 88064
  88076. 0 removed (== GATE). 6004x2 = 12008 PASS lines.
  +26 carries ring edges 87935/87936 + 88063/88064 +
  quad-carry pair 87807/87808 (== GATE DET26 note).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 87729..88076 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P204 C-vs-py mechanical, ALL EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each (sigs 3c070000 /
  95020d00 / de940700 == GATE dispatch cites); AM 16/16,
  BM 9/9, M 16/16, QR 4/4, QT 4/4, RM 16/16, RQ 16/16;
  AC 76/76, BC 72/72, QC 65/65, RC 68/68 (py-hex vs
  C-decimal normalized); C _N decls 76/72/65/68 match
  actual rows (== GATE). Sigs first-hand: A=5629d000,
  B=ab290f00, Q=3e9af200, R=1ea3290f (== GATE,
  const-table b0-3). Code-consts vs A-274 incl 77/73/
  65/68: quad+T exact; A/B -1 = b5-const-via-lencode
  bookkeeping (== GATE); byte-coverage 84/84 both
  tiers re-proven first-hand (A 2+6+76, B 2+10+72,
  0 overlap either).
- Dispatch by eye both impls, 8 tiers in order: S0
  n=87729 (PB0 3c070000 NEW) / S1 n=87730 (fat PB1
  95020d00); A 87731-87746 PBA16 off=n-87731, mtab
  6B b6,7,76-79, b5 const ad, raw lencode; B
  87747-87748 PBB pre-gap 2x off=n-87747, mtab 10B
  b6,7,48-51,80-83, b5 const ad, raw lencode; S2
  n=87749 SING gap de940700 NEW; B2 87750-87756 PBB
  post-gap 7x off=n-87750+2 (C: +2 literal ==),
  same mtab; Q 87757-87820 QUAD64 m=off&15 q=off>>4,
  M7 b9-11,76-79 + R6 b6,7,48-51 + tails b80-83,
  raw lencode; R 87821-88076 off=n-87821 c=off&15
  r=off>>4 T-ring TRANSPOSED (14th) + TAILS-SWAPPED
  (5th), b4=(0x1b+2off)&FF (C: 27 literal ==)
  b5=0xae+(off>=115)+(off>=243) (C: 174 literal ==),
  M7 b16-18,72-75 by COL, Q7 b9-11,76-79 by ROW;
  all paylen 84. Counter edges arith-verified
  first-hand: Q-carry @off51 = 87807->87808 ff/ad->
  01/ae; R off114->115 (87935->87936) ff/ae->01/af
  + off242->243 (88063->88064) ff/af->01/b0; all
  edge Ns in for-list (== GATE). C blocks carry
  T56469/474/479/494/510/515/531/554 py-line mirrors
  (8/8 exact == GATE). Insert position exact both
  sides: after T10P203R close, at dispatch tail ("N
  out of scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +258/-0 (0 deletions,
  2 hunks: tables after _T10P203RC + dispatch in main()),
  test_rgram.sh +1/-1 (for-line only), PINS +52/+0.
- C diff renumber-only + new: numstat 2219/1561; raw
  grep 2211 non-blank add + 8 bare `+` / 1561 del /
  0 blank `-` (2211+8=2219 consistent; GATE "raw grep
  2219 add ... (8 blank-only `+`, verified bare)" ==
  under all-plus-line grep). Fine-norm (b302-validated
  seds): del-uniq 1557 / add-uniq 1931 / 0 missing
  (all == GATE exact under blank-INCLUDING variant;
  excl variant is 1930, miss 0 either way — NOTE r40
  is INCL like r38, not r39 EXCL; internally
  consistent, not FAIL).
- Wall on band diff added lines (bf0ee03b..13c46dc8):
  vendor/disasm 0, depload 0, over full 2530-line
  added scope (== GATE). Files: rgramc.c 2219/1561,
  rgram.py +258/+0 purely additive, test_rgram.sh 1/1,
  PINS +52/+0 (== GATE).
- Band composition: 13c46dc8^ = 4b8ca051 single parent;
  4b8ca051 = merge bf0ee03b + 706ed5a4 (== GATE;
  cport msg PYID 6004 / RGRAM 12008 agrees).
- CONFIRM evidence: A-454-q436-t10p204 verdict CONFIRM
  (28/28 = 13 shape + 9 quad/ring + 6 counters; file
  present, counts verified; == GATE), A-274
  corroborates incl-consts 77/73/65/68 + VPOS 7/11/
  19/16 + M-tails ALL NEW vs P203T (== GATE), no
  DISSENT (CONVERT-01 rule b). No CONFIRM-P204.md
  file (== GATE; A-454 suffices per rule). GATE's
  A-454 cites (PB0/PB1 sigs, PBA16, PBB split 2+7 +
  SING gap, QUAD64 carry off51, ring TRANSPOSED+
  TAILS-SWAPPED, lencode 92/92, ring edges) all
  verbatim in file; A-274 quad-carry 87807 ff/ad ->
  87808 01/ae == my arithmetic. No FLAG/CLAIM/GATE
  conflict on b312.
- PROSE SLIP (flagged, code-PASS unaffected): GATE's
  "Newest PARENT-* is QNUM-04" is FALSE at filing —
  PARENT-QNUM-05 born 14:14:15, GATE born 14:48:09
  (birth times first-hand). Substance unaffected:
  QNUM-05 is w2e Q-block only (read at verify time),
  no gate impact. 1st slip in sweep2-r40's round
  (PROSE-01 3rd-slip bar not hit). Remainder of GATE
  prose CORRECT throughout.

Agrees with GATE-13c46dc8 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r35/
(*312* files).

Verdict: PASS. Ready for parent PV + merge.
