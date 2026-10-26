# VERIFY-b3b974d6 b349 T10P241 pins 100605..100952 (1434 tiers) PASS

Seat viewer-r45, first-hand, detached tree-b3b974d6 @b3b974d6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r45.
Base e97ace92 (b348, 1428 tiers). Band = a84ebe31 (py) + b3b974d6 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build349/bin, rc=0, 0 warnings. SHA-1 first8
  rgramc 1025c9de / aae 7d8dd3a2 (== GATE; aae.c untouched).
- RGRAMC-PYID 7029/7029 covered=7029/7029 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14058/14058 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14058/14058 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 14060 rows (2 hdr + 14058, +62 vs base); PINS cells
  7029 vs for-list 7029 exact match both ways (sorted, diff 0;
  tail 100952 pinned AND in for-list). For-list 6998->7029
  +31/-0 verbatim == GATE's 31: sing 100605 100606; A 4
  (100607 head + 100608 carry edge + 100614 off7 + 100622
  tail); C 7 (100623-100627 off0-4 + 100629 off6 + 100632
  off9; off5,7,8 = 100628/100630/100631 confirmed
  unsampled); Q 12 (row starts 100633/100649/100665/100681
  + row ends 100648/100664/100680/100696 + mids 100640/
  100656/100672/100688 = off7/23/39/55); R 6 (100697 head
  + 100735/100736 + 100863/100864 + 100952 tail).
  31x2=62=14058-13996. PINS adds == for-list adds.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR).
- Tables audit P241 C-vs-py, own script tables349.py, 66/66
  ALL-EXACT (13-table QUADms+T88): S0/S1 (3f550100 /
  4dc2a402, len 168, b4b5 fb11/fd11 == lencode; sigs REPEAT
  P240, bodies NEW both), AM 16/16 distinct 9B, CM 10/10
  distinct 20B 6-sig map exact order a402 x3 + f401/d401/
  f401/0402/1402/2402/f401 (6 distinct b2b3; CC b0/b1 const
  4d/c2), M 16/16 distinct 6B b0 16-distinct, QR 4/4 13B
  TRIPLE r1==r2==r3 2089f9b03c37ecc1fbfb745f57 + r0
  1f09fbcc61796e01b02aca478b + b3 row-sigs 1f/20/20/20,
  QT 4/4 exact a46dc517/a6780a47/d0780a47/fa780a47 +
  r1/r2/r3 TRUE-2B 0a47 (r0 ends c517), RQ==M FULL 16/16
  element-wise (staged full equality, hard-verified), RM
  16/16 (7B) / RQ 16/16 (6B) UNPAIRED, AC 73/73, CC 62/62,
  QC 59/59, RC 73/73; _N decls 73/62/59/73. Varsets exact:
  AC 11 (b4/b5+M9 b47-51,76-79), CC 22 (b22 skipped), QC 25
  (b48 skipped), RC 15 (b4/b5+M7+R6). Coverage 73+11/62+22/
  59+25/73+15 exact, 0 overlap, b4/b5 in no const set. Sig
  heads: AC b0-3 a0955736, QC b0-2 de/24/4c + b3 TAB
  (row-led), RC b0-3 03000000 NEW, RC b84-87 6b/af/ef/49.
  M-tails NEW vs P240M-tails AND vs P240QT; RM NEW vs
  P240RM; QT 4/4 NEW vs P240QT. Ring tails SPLIT 16/16
  both. A FIRST PBA b5-carry 11->12 @100607->100608
  (ff/11->01/12, b5set {11,12}); C/Q b5 const 12 (A/C/Q
  heads/mids/tails checked); ring edges off38/39 +
  off166/167 (0xb3/0x12 base). No M19/XA19/M42/X42/BM/BC/
  PT/PC/FM/FC; inventory exactly 13 + 4 _N, novel-clean
  both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  100605, S1 100606, A 100607-22, C 100623-32, Q 100633-696
  m=off&15 q=off>>4, R 100697-952 c=off&15 r=off>>4); C
  T-mirrors 6/6 exact (T66213/218/223/238/256/280); guards
  + byte positions exact (A b47-51,76-79; C b2,3,20,21,
  23-27,35,46-51,80-83 b22-skip; Q M b6,7,76-79 + R13
  b3,20,21,24-27,35,46,47,49-51 b48-skip + QT b80-83; R M7
  b9-11,80-83 + R6 b6,7,76-79); ring consts 179/18/39/167
  == py 0xb3/0x12/39/167; temps _t5126.._t5143 appended
  (base max _t5125, no reuse); insert at dispatch tail,
  N-out-of-scope follows both sides.
- Edges A-carry 100607/100608 + 100735/100736 + 100863/
  100864 + head 100605 + tail 100952 PASS 2/2 cells both
  legs (off38/39 ff/12->01/13, off166/167 ff/13->01/14).
  Odd-lencode whole-tier via own-loop 348/348. Matches
  A-562 (33/33 = 15/15 shape + 10/10 quad/ring + 8/8
  counters, file read, counts verified) + A-311 (3/3 legs;
  QUADms row-led + R13 triple + TRUE-2B + ring SPLIT
  explicit, consts 73/63/60/73 INCL, NO D dips).
- C diff purely additive: numstat 610/0 rgramc.c, 239/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  912/1). C 605 content + 5 bare-`+` / 0 del (611 incl +++
  header, == GATE). Fine-norm: del-uniq 0, missing 0
  (== GATE); add-uniq 154 reproduces EXACTLY — see note S1.
- Wall on 912 added lines (907 content + 5 bare): vendor/
  disasm 0, depload 0, libcompression/CT-cache/CT_CACHE 0,
  shebang/aa/nominated 0. (62 `ct-lzraven` PINS backend
  tags, provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10`
  1593->1599 +6, singletons `if n == ` 514->516 +2,
  range-guards `<= n <=` 416->420 +4, CLOSED prints
  `print("CLOSED` 1851->1857 +6, seal 1428->1434 +6: all
  agree (GATE literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-562 CONFIRM
  33/33 (predictive, own 364-cell bed, BAD=0) + A-311
  corroborates 3/3. Agrees with cport msg (py/C 14058,
  PYID 7029).
- Own-loop 348/348 (100605..100952, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b349. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-11 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

1 GATE METHOD NOTE (sweep-r48; code PASS): (S1) fine-norm
"add-uniq 154" is EXACT under their actual pipeline but the
method string under-specifies it: 154 reproduces iff input =
all 610 adds incl the 5 bare-`+` lines, norm = [0-9]+ -> N
+ trailing-';' strip + whitespace-strip, sets KEEP the empty
member (153 non-empty + 1 empty = 154; verified first-hand).
Without strip = 156/157; stripped + empty-excluded = 153.
(Same strip-omission class as r44's b347 note; b347's 178
needed strip-only, b349's 154 needs strip + keep-empty —
worth one canonical fine-norm recipe stating both.)

Verdict: PASS. Code CORRECT; GATE 1 method note (flagged).
Logs: NVME ws tmp/encode-viewer/r45/ (*349* set:
build349, pyid349, rgram349py/c, cmp349.py/.c, for349-*,
pins349.basen, smoke349, tables349.py/.log, banddiff349(-c),
added349(-all), numstat349, populate349, ownloop349.py/.log).
