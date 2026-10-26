# VERIFY-c332f7e4 b327 T10P219 pins 92949..93296 (1297 tiers): PASS

viewer-r39, first-hand, detached tree NVME tmp/encode-viewer/r39/
tree-c332f7e4 @c332f7e4 (base 7828ec30 = b326 tip), seat build
build327/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2887656 B, sha256 rgramc a4d21379 (first-hand,
  GATE omits) / aae d6e27c97 (== b326, stable); aae SHA-1
  first8 7d8dd3a2 == GATE.
- RGRAMC-PYID 6394/6394 covered=6394/6394 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12788/12788 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12788/12788 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12788/12788, diff 0).
- PINS-RGRAM cells set-eq 12788/12788 (cmp-identical).
  PINS N-set == for-list 6394/6394.
- PINS 12790 rows = 2 hdr + 12788 (+52 vs base 12738).
  For-list +26 exactly: 92949 92950 92951 92958 92966 92967
  92968 92969 92972 92976 92977 92985 92992 92993 93008 93009
  93017 93024 93025 93040 93041 93055 93056 93183 93184 93296.
  0 removed (== GATE verbatim). DET26 shape: PB0/PB1 (2),
  PBA edges+mid 92958 (3: 92951/92958/92966), PAIR both (2),
  PBC8 edges 92969/92976 + mids 92972 (3 of 8), quad start
  92977 + row edges 92992-93/93008-09/93024-25 + carry sides
  92985/93017 + end 93040 (10), ring start 93041 + edge sides
  93055/93056 + 93183/93184 + tail 93296 (6) — 2+3+2+3+10+6
  = 26 (== GATE exact).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 92949..93296 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (Zero-write variant ownloop327b.py, cache-path-direct: NVME
  ENOSPC windows during run; see notes 3-4.)
- Tables P219 C-vs-py mechanical, ALL EXACT: S0/S1
  168/168-hex-char singletons (sigs 56110000 / 36bf2200 ==
  GATE); AM 16/16, PT 2/2 (4e/6e), CM 8/8, M 16/16, X42
  4/4 (00/04/05/05), M42 16/16 (C-vs-py eq; 7 distinct 1B
  col-vals, repeats natural — see note 1), QR 4/4 (row sigs
  18deb721/6adc0bc5/ffdf4b90x2, r2==r3 full-row
  ffdf4b9030d1 x2, 3/4 distinct == GATE), QT 4/4
  (7cc4b6cf/298c9e0c/df24e910/0e25e910 4/4 distinct, r2/r3
  share e910 — == A-289 verbatim), RM 16/16, RQ 16/16;
  AC 75/75, PC 81/81, CC 70/70, QC 63/63, RC 67/67 (py-hex
  vs C-decimal normalized); C _N decls 75/81/70/63/67 match
  actual rows (== GATE). Const sigs: A 36bf2a02, P 36bf2200,
  C 36bf1200, Q 36bf1a01, T 36bf5a11 (b0-3 first-hand ==
  GATE). b4/b5 in no const table (all 5). Absence inventory:
  _T10P219BM/BC/FM/FC/FS/FO/H/TC* 0 hits either side (==
  GATE); _T10P219* symbols == known 17-table set exactly
  (py 17 / C 22 = +5 _N). VPOS missing-sets first-hand
  EXACT all 5: AC-9 [4,5,36,37,38,76,77,78,79] / PC-3
  [4,5,80] / CC-14 [4,5,32,33,37-42,80-83] / QC-21
  [4,5 + M8 + b42 + R6 + tails] / RC-17 [4,5 + R9 + M6]
  (== GATE partitions). Memo excl-code cross-check: in-table
  excl (no b4/b5 entry anywhere) + b5-const-via-lencode
  bookkeeping (A/C/Q +1 const-d6, T +0) = memo 76/71/64/67
  (== GATE/A-289). Byte-coverage 84/84 all 5 groups
  re-proven first-hand (A 2+7+75, P 2+1+81, C 2+12+70, Q
  2+8+1+6+4+63, R 2+6+9+67; 0 overlap anywhere; b4/b5 in no
  const set — == GATE exact).
- Dispatch by eye both impls, 7 blocks in order: S0
  n=92949 (PB0 56110000 off=0) / S1 n=92950 (fat PB1
  36bf2200 off=1); A 92951-92966 PBA16 off=n-92951, mtab
  7B b36-38,76-79, raw lencode; P 92967-92968 PAIR
  off=n-92967, b80 tab PT[off], raw lencode; C 92969-92976
  PBC8 off=n-92969, M12 b32,33,37-42,80-83, raw lencode; Q
  92977-93040 QUAD off=n-92977 m=off&15 q=off>>4, shared M8
  b23,34,35,43,76-79 + b42 row-xor (pay[42]^X42[q] vs
  M42[m]) + R6 sig-led b36-41 QR[q] + tails b80-83 QT[q],
  raw lencode; R 93041-93296 off=n-93041 c=off&15 r=off>>4
  T-ring STANDARD, b4=(0xe3+2off)&FF (C: 227 literal ==)
  b5=0xd6+(off>=15)+(off>=143) (C: 214 literal ==), M6
  b48,49,76-79 by COL c, R9 b23,34,35,42,43,72-75 by ROW r;
  all paylen 84 (== GATE every value). C blocks carry
  T60622/627/632/647/661/677/702 py-line mirrors (7/7 exact
  == GATE). Insert position exact both sides: after
  T10P218R close, dispatch tail ("N out of scope" + return 2
  follows).
- Counter edges computed first-hand: A/P/C/Q b5 const d6
  across (raw lencode, b4 distinct 16/2/8/64 — == GATE);
  R off14->off15 (93055->93056) ff/d6->01/d7 +
  off142->off143 (93183->93184) ff/d7->01/d8; all four edge
  Ns pinned + PASS (own-loop oracle-agreeing). No DISSENT:
  cut bytes verify (== GATE).
- py diff pure addition: rgram.py +295/-0, test_rgram.sh
  +1/-1 (for-line only), PINS +52/-0 (== GATE totals).
- C diff purely additive: numstat 750/0; raw grep 750 add /
  0 del (6 bare `+`, 0 blank-minus; == GATE). Normalized
  ([0-9]+ -> N, cut-c2, sort -u): del-uniq 0 / add-uniq
  182-INCL (181 EXCL) / 0 missing — md5-BYTE-EQUAL to
  sweep's cdiff327-add-norm.txt artifact (eb1fd6ea; ==
  GATE exact). (Own-echo scare, see note 2.)
- Wall on band diff added lines (7828ec30..c332f7e4,
  1098 added == GATE): vendor/disasm 0, depload 0,
  libcompression/CT-shim/shebang//usr/bin/aa/nominated 0
  (== GATE). Files: rgramc.c 750/0, rgram.py 295/0,
  test_rgram.sh 1/1, PINS 52/0 (750+295+1+52 = 1098 exact).
- Tiers: merge-msg +7, code 7 blocks (2 sing + 5 tiers),
  CLOSED-count 1444->1451 +7 (stated method, reproducible),
  seal 1290->1297 +7 (cport msg "1297 tiers sealed"): agree.
- Band composition: c332f7e4^ = 7a163858 single parent;
  7a163858 = merge 7828ec30 + 3e7b26c3 (py partial +7
  tiers +52 pins) (== GATE; cport msg PYID 6394 /
  RGRAM 12788 agrees).
- CONFIRM evidence: A-486-q611-t10p219 verdict CONFIRM
  26/26 = 13/13 shape + 9/9 quad/ring + 4/4 counters
  (file present, counts verified; == GATE), A-289
  corroborates (PB0 REPEAT/PB1 NEW/PBA VPOS-8/PAIR VPOS/
  PBC8 VPOS-13/quad VPOS-20 + row-xor + r2==r3 + tails
  verbatim + T-ring STANDARD UNPAIRED + consts 76/71/64/67
  + edges + NO D — all verbatim in file, == GATE), no
  DISSENT (CONVERT-01 rule b). No CONFIRM-P219.md file
  (A-486 suffices per rule). GATE's A-486/A-289 cites
  (PAIR VPOS {b4,b80}, NO FRAG/B10, QUAD64 M8 shared 16/16
  x3 + b42 row-xor X=[00,04,05,05], R6 r2==r3 PAIRED
  ffdf4b9030d1 + tails r2/r3 share e910, T-ring STANDARD
  M6-by-COL + R9-by-ROW UNPAIRED 16 distinct, M-tails ALL
  NEW 0/16, lencode 348/348, ring edges, NO D) all verbatim
  in files. No FLAG/CLAIM/GATE conflict on b327. GATE makes
  no newest-QNUM claim (N/A; born 16:08:37, newest then
  QNUM-06 16:02:56). Sweep logs: 27 *327* files present.
- Notes (not slips): (1) M42 distinctness: my audit's first
  cut wrongly expected 16 distinct; M42 is a 1B b42-column
  table (values 56/f6/16/36/b6/76/96, 7 distinct) where
  repeats are natural — expectation corrected, C-vs-py eq
  True throughout. (2) add-norm scare: my first pipe via
  `echo "$D"` gave 184 (BSD echo eats backslash-n in C
  printf lines, splitting 7 lines); direct pipe = 182,
  md5-identical to sweep artifact — my pipe error, not a
  GATE slip. (3) ct-cache poisoning: 2 entries (N=92952/
  92953 keys) were 12-byte truncated files dated 20:36
  (ENOSPC window); fresh tool encodes deterministic 100B;
  entries removed + re-fetched verified; own-loop then
  348/348. Fail-closed throughout (batteries never false-
  PASS). Reported in NOTE-viewer-r39-hb3; 554 window-files
  census left for parent scrub decision. (4) NVME 100%
  full repeatedly during run (Spotlight mds_stores GB-scale
  index churn on the volume + live seats); removed 167
  ancient reproducible trees in tmp/encode-viewer/ only
  (merged+clean+registered guards, r37+ spared, logs kept,
  audit cleanup327.log) freeing 3.1G, since re-consumed.
  Standing ask: mdutil-exclude /Volumes/NVME (owner call).

Agrees with GATE-c332f7e4 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r39/
(*327* files; ownloop327.log content = "348 ok / 0 bad"
via zero-write variant, ENOSPC blocked tee).

Verdict: PASS. Ready for parent PV + merge.
