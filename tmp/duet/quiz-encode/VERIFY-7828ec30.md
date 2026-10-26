# VERIFY-7828ec30 b326 T10P218 pins 92601..92948 (1290 tiers): PASS

viewer-r38, first-hand, detached tree NVME tmp/encode-viewer/r38/
tree-7828ec30 @7828ec30 (base f0b205de = b325 tip), seat build
build326/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2887176 B, sha256 rgramc eaad3f26 / aae d6e27c97
  (BOTH == GATE; aae stable, aae.c untouched).
- RGRAMC-PYID 6368/6368 covered=6368/6368 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12736/12736 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12736/12736 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12736/12736, diff 0).
- PINS-RGRAM cells set-eq 12736/12736 (cmp-identical; GATE
  "6368/6368" = standing half-cell phrasing, full cells 2x
  verified). PINS N-set == for-list 6368/6368.
- PINS 12738 rows = 2 hdr + 12736 (+52 vs base 12686).
  For-list +26 exactly: 92601 92602 92603 92610 92618 92619
  92620 92622 92625 92628 92629 92644 92645 92660 92661 92671
  92672 92676 92677 92692 92693 92799 92800 92927 92928 92948.
  0 removed (== GATE verbatim). DET26 shape verified: PB0/
  PB1 both (2), PBA edges+mid 92610 (3), FRAG10 5 cells
  (offs 0,1,3,6,9), quad start + row edges 92644-45/660-61/
  676-77 + carry sides 92671/92672 + end 92692 (10), ring
  start + edge sides 92799/92800 + 92927/92928 + tail (6)
  — 2+3+5+10+6 = 26 (== GATE exact).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 92601..92948 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P218 C-vs-py mechanical, ALL EXACT: S0/S1
  168/168-hex-char singletons (sigs 56110000 / 8aac2200 ==
  GATE; S0 b4/b5 73/d3 == lencode(92601), S1 75/d3 ==
  lencode(92602), first-hand); AM 16/16, FM 10/10 (10/10
  diverge; b0-2 multiset 02b921x1/0a9626x2/0ea621x1/
  328b10x1/869014x2/d2a325x3 EXACT == GATE), M 16/16,
  QR 4/4 (row sigs d2a32d02/328b1001/02b92902x2 == GATE;
  r2==r3 02b92902e1b25ff229015b x2, 3/4 distinct), QT 4/4
  (092744bf/02ab6e3b/c6aeb4af/f5aeb4af, r2/r3 share
  aeb4af — == A-288 verbatim), RM 16/16, RQ 16/16;
  AC 74/74, FC 64/64, QC 59/59, RC 66/66 (py-hex vs
  C-decimal normalized); C _N decls 74/64/59/66 match
  actual rows (== GATE). Const sigs: A a1c82a02, T
  609ce72e (b0-3 first-hand == GATE); FC b3=00-only
  (no b0-2 — sig bytes in tab, == GATE); QC no b0-3
  (multi-sig rows in R11 tab, == GATE). b4/b5 in no
  const table (all 4). Absence inventory: _T10P218*
  symbols == known 13-table set exactly (py 13 / C 17
  = +4 _N). Code-consts vs A-288 incl 75/65/59/66:
  Q + T exact; A/F -1 each = b5-const-via-lencode
  bookkeeping (== GATE); FM18 == QR+QM+tails minus
  b3,76-79 set-exact 18/18 re-checked first-hand
  (== GATE/A-288); byte-coverage 84/84 all 4 groups
  re-proven first-hand (A 2+8+74, F 2+18+64, Q
  2+8+11+4+59, R 2+8+8+66; 0 overlap anywhere; b4/b5
  in no const set — == GATE exact). M-tails ALL NEW
  vs P217T 16/16 (0/16 shared — == A-485/A-288). RM/RQ
  16/16 distinct each (UNPAIRED — == memos).
- Dispatch by eye both impls, 6 blocks in order: S0
  n=92601 (PB0 56110000 NEW off=0) / S1 n=92602 (fat
  PB1 8aac2200 NEW off=1); A 92603-92618 PBA16
  off=n-92603, mtab 8B b20-23,76-79, raw lencode; F
  92619-92628 FRAG10 6-sig MULTI-SIG off=n-92619, M18
  b0-2,11,18-27,80-83 (sig bytes in tab) + FC, raw
  lencode; Q 92629-92692 QUADms off=n-92629 m=off&15
  q=off>>4, shared M8 b24-27,76-79 + R11 sig-led
  b0-3,11,18-23 QR[q] + tails b80-83 QT[q], raw lencode
  b5-carry @off42->43; R 92693-92948 off=n-92693
  c=off&15 r=off>>4 T-ring STANDARD, b4=(0x2b+2off)&FF
  (C: 43 literal ==) b5=0xd4+(off>=107)+(off>=235)
  (C: 212 literal ==; ring consts 43/212 == GATE), M8
  b32-35,76-79 by COL c, R8 b24-27,72-75 by ROW r; all
  paylen 84 (== GATE every value). C blocks carry
  T60341/346/351/366/383/407 py-line mirrors (6/6 exact
  == GATE). Insert position exact both sides: after
  T10P217R close, dispatch tail ("N out of scope" +
  return 2 follows).
- Counter edges computed first-hand: Q off42->off43
  (92671->92672) ff/d3->01/d4 (code comment "b5-carry
  @off42->43" == GATE); R off106->107 (92799->92800)
  ff/d4->01/d5 + off234->235 (92927->92928) ff/d5->01/d6;
  all six edge Ns pinned + PASS (own-loop oracle-
  agreeing). No DISSENT: cut bytes verify (== GATE).
- py diff pure addition: rgram.py +236/-0 (0 deletions),
  test_rgram.sh +1/-1 (for-line only), PINS +52/-0
  (== GATE).
- C diff purely additive: numstat 606/0; raw grep 606
  add / 0 del (5 bare `+`, 0 blank-minus; == GATE).
  Fine-norm reproduced BYTE-EQUAL from GATE's stated pipe
  (_t/_i/_b/T numbers via BSD sed, sign-strip, empty-
  excluding): del-uniq 0 / add-uniq 373 / 0 missing
  (== GATE exact; artifact byte-identical). Coarse
  ([0-9]+ -> N) independently: del-uniq 0 / add-uniq
  159-INCL (158 EXCL) / 0 missing — pure addition proven
  two ways.
- Wall on band diff added lines (f0b205de..7828ec30,
  895 added == GATE; 890 non-blank + 5 bare-plus):
  vendor/disasm 0, depload 0, libcompression/CT-shim/
  shebang//usr/bin/aa/nominated 0 (== GATE). Files:
  rgramc.c 606/0, rgram.py 236/0, test_rgram.sh 1/1,
  PINS 52/0 (== GATE; 606+236+1+52 = 895 exact).
- Tiers: merge-msg +6, code 6 blocks, guards delta +6
  (absolute 1438->1444 not reproducible — no method
  stated; +6 corroborated first-hand via py dispatch-
  ifs 754->760; series self-consistent +6/band
  1426->1432->1438->1444 across b324-b326 — see
  note 1), seal 1284->1290 +6 (cport msg "1290 tiers
  sealed"): agree.
- Band composition: 7828ec30^ = 6b890a79 single parent;
  6b890a79 = merge f0b205de + 7d5f1fcc (py partial +6
  tiers +52 pins) (== GATE; cport msg PYID 6368 /
  RGRAM 12736 agrees).
- CONFIRM evidence: A-485-q610-t10p218 verdict CONFIRM
  26/26 = 13/13 shape + 9/9 quad/ring + 4/4 counters
  (file present, counts verified; == GATE), A-288
  corroborates incl-consts 75/65/59/66 with -1
  bookkeeping resolved + FM18 set-claim re-checked +
  R11 value + tails verbatim + VPOS 9/19/25/18
  partition-exact vs code sets + carry edges + NO D
  dips (== GATE), no DISSENT (CONVERT-01 rule b). No
  CONFIRM-P218.md file (A-485 suffices per rule). GATE's
  A-485/A-288 cites (PB0/PB1 NEW, PBA16 NEW, FRAG10
  6-sig 10/10 diverge, QUADms row sigs r2==r3 + carry
  d3->d4 @92671->92672, ring STANDARD UNPAIRED, lencode
  348/348, ring edges, NO D) all verbatim in files. No
  FLAG/CLAIM/GATE conflict on b326. GATE's "newest
  PARENT-* QNUM-05" TRUE at filing (GATE born 15:57:08,
  QNUM-05 14:14, QNUM-06 16:02 after; birth times
  first-hand). Sweep2 logs: 26 *326* files present.
- Notes (not slips): (1) guards absolute 1438->1444
  unreproducible as stated (no method; same as b324
  note — series coherent +6/band, delta verified;
  later GATEs added stated methods). (2) PINS-RGRAM
  "6368/6368" = standing half-cell phrasing (full
  12736 cells cmp-identical).

Agrees with GATE-7828ec30 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r38/
(*326* files).

Verdict: PASS. Ready for parent PV + merge.
