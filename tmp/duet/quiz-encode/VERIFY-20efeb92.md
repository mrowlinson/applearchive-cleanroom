# VERIFY-20efeb92 b350 T10P242 pins 100953..101300 (1440 tiers) PASS

Seat viewer-r45, first-hand, detached tree-20efeb92 @20efeb92,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r45.
Base b3b974d6 (b349, 1434 tiers). Band = 46f669c0 (py) + 20efeb92 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build350/bin, rc=0, 0 warnings. sha256 rgramc
  9ed948a1 / aae d6e27c97 (== GATE; aae.c untouched).
- RGRAMC-PYID 7060/7060 covered=7060/7060 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14120/14120 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14120/14120 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 14122 rows (2 hdr + 14120, +62 vs base); PINS cells
  7060 vs for-list 7060 exact match both ways (sorted, diff 0).
  For-list 7029->7060 +31/-0 verbatim == GATE's 31: sing
  100953 100954; A 3 (100955 head + 100962 off7 + 100970
  tail); C 7 (100971-100975 off0-4 + 100978 off7 + 100980
  off9; off5,6,8 = 100976/100977/100979 confirmed
  unsampled); Q 13 (100981 head + carry pair 100991/100992
  + 100996/100997 + 101004 + 101012/101013 + 101020 +
  101028/101029 + 101036 + 101044 tail); R 6 (101045 head
  + 101119/101120 + 101247/101248 + 101300 tail).
  31x2=62=14120-14058. PINS adds == for-list adds.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR).
- Tables audit P242 C-vs-py, own script tables350.py, 66/66
  ALL-EXACT (13-table C10-MS/quad/T88): S0/S1 (4b620100 NEW
  / 6197c402 NEW, len 168, b4b5 b3/14 + b5/14 == lencode),
  AM 16/16 distinct 9B, CM 10/10 distinct 13B 6-sig map
  exact order bd7dc6 x3 + f5c1ce/6517cb/1dfac9/f5c1ce/
  c5f9cd/9d6fcf/1dfac9 (b0-2 heads + b3 const 02; 6 distinct;
  repeats @100977==@100974 + @100980==@100976 verified),
  M 16/16 distinct 8B (b0 multiset f7 x3, entries still
  16/16 distinct), QR 4/4 7B r2==r3 b20f76d47c32b9 + r0
  32ce7f3478c7b0 + r1 b20f76d07c32b9 1B-off byte3 d0-vs-d4
  rest identical, QT 4/4 exact 049680e9/2930e3e7/45bd1e06/
  6fbd1e06 + r2/r3 TRUE-3B bd1e06, RQ==M FULL 16/16
  element-wise (hard-verified; GATE silent, recorded as
  observation), RM 16/16 (9B) / RQ 16/16 (8B) UNPAIRED, AC
  73/73, CC 69/69, QC 63/63, RC 69/69; _N decls 73/69/63/69.
  Varsets exact: AC 11 (b4/b5+M9 b12-15,19,76-79), CC 15
  (b0-2,11,18-22,80-83), QC 21 (b20 skipped, b20 const f2
  verified), RC 19 (b4/b5+M9+R8). Coverage 73+11/69+15/
  63+21/69+19 exact, 0 overlap, b4/b5 in no const set. Sig
  heads: AC b0-3 608fd732, CC b0-2 VAR + b3 const 02, QC
  b0-3 0080773c, RC b0-3 02000000 (==P234/235T per A-312
  correction, NOT P241T — code comment agrees), RC b84-87
  27/71/a8/dd. M-tails NEW vs P241M-tails AND vs P241QT;
  RM NEW vs P241RM; QT 0/4 vs P241QT. Ring tails SPLIT
  16/16 both. A/C b5 const 14; Q b5-carry 14->15 @100991->
  100992 (ff/14->01/15); ring edges off74/75 + off202/203
  (0x6b/0x15 base). No M19/XA19/M42/X42/BM/BC/PT/PC/FM/FC;
  inventory exactly 13 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  100953, S1 100954, A 100955-70, C 100971-80, Q 100981-
  101044 m=off&15 q=off>>4, R 101045-101300 c=off&15
  r=off>>4); C T-mirrors 6/6 exact (T66453/458/463/478/494/
  517); guards + byte positions exact (A b12-15,19,76-79; C
  b0-2,11,18-22,80-83; Q M b24-27,76-79 + R7 b12-14,18,19,
  21,22 b20-skip + QT b80-83; R M9 b18,19,27,34,35,80-83 +
  R8 b28-31,76-79); ring consts 107/21/75/203 == py 0x6b/
  0x15/75/203; temps _t5144.._t5161 appended (base max
  _t5143, no reuse); insert after T10P241R close at dispatch
  tail, N-out-of-scope follows both sides.
- Edges Q-carry 100991/100992 + 101119/101120 + 101247/
  101248 + head 100953 + tail 101300 PASS 2/2 cells both
  legs (off74/75 ff/15->01/16, off202/203 ff/16->01/17).
  Odd-lencode whole-tier via own-loop 348/348. Matches
  A-568 (33/33 = 15/15 shape + 10/10 quad/ring + 8/8
  counters, file read, counts verified) + A-312 (3/3 legs +
  1 sig-ref CORRECTION adopted: ring 02000000 ==P234/235T
  only; code comment matches corrected form).
- C diff purely additive: numstat 610/0 rgramc.c, 237/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  910/1). C 605 content + 5 bare-`+` / 0 del. Fine-norm:
  del-uniq 0, missing 0 (== GATE); add-uniq 398 under
  temps-only norm (tried case-fold/LC_ALL=C/semi-strip/
  trail-strip 398, lead-strip/squeeze 396, full-num 156)
  vs GATE's 397 — see note S1.
- Wall on 910 added lines (905 content + 5 bare): vendor/
  disasm 0, depload 0, libcompression/CT-cache/CT_CACHE/aa/
  nominated 0, shebang 0. (62 `ct-lzraven` PINS backend
  tags, provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10`
  1599->1605 +6, singletons `if n == ` 516->518 +2,
  range-guards `<= n <=` 420->424 +4, CLOSED prints
  `print("CLOSED` 1857->1863 +6, seal 1434->1440 +6: all
  agree (GATE literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-568 CONFIRM
  33/33 (predictive, own 364-cell bed, BAD=0) + A-312
  corroborates (3/3 + correction). Agrees with cport msg
  (py/C 14120, PYID 7060).
- Own-loop 348/348 (100953..101300, C+py agree CLOSED each N;
  populate fetched 316, 32 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b350. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-11 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

1 GATE COUNT SLIP (sweep2-r49; code PASS): (S1) fine-norm
"add-uniq 397" reproduces under no reasonable reading
(temps-only _tN/_iN/_bN norm = 398 under plain/case-fold/
LC_ALL=C/semi-strip/trail-strip; any leading-strip/squeeze =
396; full-number norm = 156). Theirs = plain-minus-1, the
SAME systematic 1-off as b348 (415/414) + r44's b344/b346
(438/437, 391/390) — now 4/4 sweep2 bands this pattern;
consistent with a missing-trailing-newline `wc -l`
undercount in their pipeline. Del-uniq 0 + missing 0 agree;
purely-additive verdict unaffected.
Own near-miss caught pre-filing (CLOSED-count self-check on
the QR 1B-off leg: first wrote hex-char-diff ==2, correct is
byte3 d0-vs-d4 rest-identical — fixed, ALL-EXACT re-run).

Verdict: PASS. Code CORRECT; GATE 1 count slip (flagged).
Logs: NVME ws tmp/encode-viewer/r45/ (*350* set:
build350, pyid350, rgram350py/c, cmp350.py/.c, for350-*,
pins350.basen, smoke350, tables350.py/.log, banddiff350(-c),
added350(-all), numstat350, populate350, ownloop350.py/.log).
