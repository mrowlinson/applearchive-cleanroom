# VERIFY-fa5e0143 b345 T10P237 pins 99213..99560 (1410 tiers) PASS

Seat viewer-r44, first-hand, detached tree-fa5e0143 @fa5e0143,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r44.
Base 5d63fca7 (b344, 1404 tiers). Band = b1b96b2b (py) + fa5e0143 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build345/bin, rc=0, 0 warnings. SHA-1 first8
  rgramc a14c9ab2 / aae 7d8dd3a2 (== GATE; aae.c untouched).
- RGRAMC-PYID 6905/6905 covered=6905/6905 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13810/13810 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 13810/13810 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 13812 rows (2 hdr + 13810, +62 vs base); PINS cells
  6905 vs for-list 6905 exact match both ways (sorted, diff 0;
  numeric-token parse, no `;` pollution; tail 99560 pinned AND
  in for-list). For-list 6874->6905 +31/-0 verbatim == GATE's
  31: sing 99213 99214; A 99215/99216/99222/99230
  (off0/1/7/15); C 99231 99232 99233 99234 99235 99237 99240
  (off0,1,2,3,4,6,9; off5,7,8 = 99236,99238,99239 confirmed
  unsampled); Q 12 (row starts 99241/99257/99273/99289 +
  row ends 99256/99272/99288/99304 + 99248/99264/99280/
  99296); R 6 (99305 + 99327/99328 + 99455/99456 + 99560).
  31x2=62=13810-13748. PINS adds == for-list adds, 0 removed.
- SMOKE-GREEN rc=0 (6/6 PASS, default backend).
- Tables audit P237 C-vs-py, own script tables345.py, 58/58
  ALL-EXACT: S0/S1 (93540100 NEW/b590ac02 NEW, len 168,
  b4b5 1b07/1d07 == lencode), AM 16/16 distinct 6B, CM 10/10
  distinct 18B 2-sig map a702 x3 + 5701 x7 exact order, M
  16/16 distinct 8B, QR 4/4 TRIPLE r1==r2==r3 e63c528914eb60
  + r0 aefc0117f49a39, QT 4/4 exact 4d4c1e83/0e319725/
  a0160327/ca160327 + r2/r3 share 160327 (r1 no triple
  share), RM 16/16 (7B) / RQ 16/16 (8B) UNPAIRED, AC 76/76,
  CC 64/64, QC 63/63, RC 71/71; _N decls 76/64/63/71.
  Varsets exact: AC 8, CC 20, QC 21, RC 17 (A-553 VPOS +
  b5-excl on A/C/Q). Coverage 76+8/64+20/63+21/71+17 exact,
  0 overlap, b4/b5 in no const set. Sig consts AC 609bd720,
  CC (0,ad),(1,52) + b2,3 tab, QC ad520714, RC 01000000.
  QC b42 0x14 via consts. RC b84-87 7a/cd/c1/0e. RQ==M FULL
  16/16 element-wise (verified hard, per-index). M-tails NEW
  vs P236T; RM NEW vs P236RM; QT 4/4 NEW vs P236QT. Ring
  tails SPLIT 16/16 both. A/C/Q b5 const 07 (full-range set
  {07}, no carry); ring edges off22/23 + off150/151 (0xd3/
  0x07 base). No M42/X42/BM/BC/PT/PC/FM/FC; inventory
  exactly 13 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  99213, S1 99214, A 99215-30, C 99231-40, Q 99241-304
  m=off&15 q=off>>4, R 99305-560 c=off&15 r=off>>4); C
  T-mirrors 6/6 exact (T65240/245/250/265/282/305); guards
  exact; Q byte lists M8 b21-23,31,76-79 + R7 b24-30 +
  tails b80-83 match; ring consts 211/7 + thresholds 23/151
  (211=0xd3); ring byte lists M7 b40-42,76-79 / R8
  b25-27,35,80-83 match; temps _t5052.._t5069 appended
  (base max _t5051, no reuse); insert after T10P236R close
  at dispatch tail, N-out-of-scope follows both sides.
- Edges 99327/99328 + 99455/99456 + head 99213 + tail 99560
  PASS 2/2 both legs. Odd-lencode whole-tier via own-loop
  348/348. Matches A-553 (33/33 = 15/15 shape + 10/10
  quad/ring + 8/8 counters, file read, counts verified) +
  A-307 (3/3 legs; PB0/PB1/PBA NEW, C10 map ad52a702 x3 +
  ad525701 x7 exact, quad triple/tails exact, ring STANDARD
  inverted explicit, consts 77/65/64/71 INCL with standing
  -1 x3 excl on PBA/C10/quad, NO D dips).
- C diff purely additive: numstat 610/0 rgramc.c, 237/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  910). C 610 add / 0 del; fine-norm by GATE's stated
  method ([0-9]+ -> N, sign/';' strip, python sets)
  del-uniq 0, add-uniq 158, missing 0 (== GATE, reproduced
  exactly).
- Wall on 910 added lines: vendor/disasm 0, depload 0,
  libcompression/aa/shim/shebang/nominated 0.
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1310->1316 +6, singletons `if n == ` 506->508 +2,
  range-guards `<= n <=` 400->404 +4, CLOSED prints
  `print("CLOSED` 1827->1833 +6, seal 1404->1410 +6: all
  agree (GATE literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-553 CONFIRM
  33/33; A-307 corroborates. Agrees with cport msg (py/C
  13810, PYID 6905).
- Own-loop 348/348 (99213..99560, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b345. Newest
  PARENT-* is QNUM-12 (GATE says QNUM-09 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

Verdict: PASS. Code CORRECT; GATE CORRECT, 0 slips.
Logs: NVME ws tmp/encode-viewer/r44/ (*345* set:
build345, pyid345, rgram345py/c, cmp345.py/.c, for345-*,
pins345.basen, smoke345, tables345.py/.log, banddiff345(-c),
added345, numstat345, populate345, ownloop345.py/.log).
