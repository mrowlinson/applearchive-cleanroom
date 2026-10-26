# VERIFY-26effd6a b363 T10P255 pins 105477..105824 (1518 tiers) PASS

Seat viewer-r48, first-hand, detached tree-26effd6a @26effd6a,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r48.
Base ade4c863 (b362, 1512 tiers). Band = 2013543b (py) + 26effd6a (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build363/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc f97a6560 / aae 7d8dd3a2 +
  sha256 0ebbf0b2 / d6e27c97 (== GATE all 4; aae.c untouched).
- RGRAMC-PYID 7463/7463 covered=7463/7463 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14926/14926 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14926/14926 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14926/14926, sorted).
- PINS 14928 rows (2 hdr + 14926, +62 vs base 14866); PINS
  base-N 7463 vs for-list 7463 exact both ways (0/0; tail
  105824 pinned AND in for-list); PASS-names vs PINS-names
  xor 0. For-list 7432->7463 +31/-0 verbatim == GATE's 31:
  sing 105477 105478; A 6 (105479 head + 105480 + 105485 +
  105489 + 105493 + 105494 tail); C 6 (105495 head + 105498
  + 105499 + 105502 + 105503 + 105504 tail; offs 1,2,5,6 =
  105496,105497,105500,105501 unsampled); Q 10 (105505 head
  + 105520 + 105521 + 105536 + 105537 + mid 105545 + 105552
  + 105553 + 105561 + 105568 tail; NO carry pair, b5
  const); R 7 (105569 head + edge pairs 105599/105600 +
  105727/105728 + mid 105697 + 105824 tail). 31x2=62=
  14926-14864. PINS adds == for-list adds x2.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME workdir, default backend).
- Tables audit P255 C-vs-py, own script tables363.py, 105/105
  ALL-EXACT (17-table A-PBA/C10-2SIG/QUAD-3sig+T88, NO
  BM/BC/M42/X42/PT/FM: 18 syms, S-pair one family): S0/S1
  (e4180300 ==P254PB0 REPEAT @105477 b4b5 0b/38 / 0dc83406
  NEW @105478 b4b5 0d/38, both NEW strings, len 168 ==
  lencode); AM 16/16 distinct 7B; CM 10/10 distinct 16B,
  sandwich 26c83406x4/13641a03x4/26c83406x2 (full-sig in
  tab); M 16/16 distinct 4B tails-only; QB12/QB13/QB14/
  QB15/QB19 32/32 each, distinct 16/10/8/6/26 (== memo
  counts), all 5 group tabs r01-vs-r23 differ; QR 4/4
  PAIRED r2==r3 4089bf36856b85 + r0 009e1f769e1850 + r1
  608fcf66d88719 distinct (3-sig full-sig rows 009e1f76/
  608fcf66/4089bf36); QT 4/4 exact b3f8e313/492cce3a/
  feb89ebb/28b99ebb (r2/r3 share last-2B 9ebb ONLY, 2nd
  bytes b8/b9 1B-off, SecR-staged); RM 16/16 7B / RQ 16/16
  9B UNPAIRED 0-overlap, tails SPLIT 16/16 both (RM b80-83
  by COL, RQ b76-79 by ROW); RQ==M b76-79 same-index 16/16
  (shared-slice P249-style); AC 75/75, CC 66/66, QC 62/62,
  RC 70/70; _N decls 75/66/62/70. Varsets exact: AC 9
  (b4/b5+M7 b9-11,76-79), CC 18 (b4/b5+M16 b0-3,11,13-19,
  80-83; b12 const 00 SKIPPED, sig bytes in tab), QC 22
  (b4/b5+QM4 b76-79+5pair b12-15,19+R7 b0-3,16-18+T4
  b80-83), RC 18 (b4/b5+TM7 b28-30,80-83+TR9 b16-19,23,
  76-79). Coverage 75+9/66+18/62+22/70+18 exact, 0 overlap,
  b4/b5 in no const set. AC sig 79824c63 NEW; RC sig
  03000000 ==P241T (re-read first-hand); RC b84-87 a3/6f/
  d7/65. M-tails 16/16 NEW vs P254T (P254RQ 9B tails);
  QT 4/4 NEW vs P254QT. Inventory exactly 18 + 4 _N,
  novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  105477, S1 105478, A 105479-494, C 105495-504, Q 105505-568
  m=off&15 q=off>>4 g=0/16, R 105569-824 c=off&15 r=off>>4);
  C T-mirrors 6/6 exact bodies (T70102/70107/70112/70127/
  70144/70178); C pair-coltabs via snprintf %02lx of pay[12/
  13/14/15/19] vs QB[g+m] (matches py); ordered pay-index
  sequences C==py per range block (A n=9, C n=18, Q n=29,
  R n=20); ring consts 0xc3/0x38 + (off>=31)+(off>=159) ==
  py; temps _t5400..5427 contiguous (base max _t5399) +
  _i max 3301 / _b max 3300 (base max _i3290/_b3289
  first-hand via git show, no reuse); insert at dispatch
  tail after T10P254R close, N-out-of-scope follows both
  sides.
- Edges ring 105599 (off30, ff/38) -> 105600 (off31, 01/39)
  + 105727 (off158, ff/39) -> 105728 (off159, 01/3a) + mid
  105697 (off128, c3/39); all edge pins + tail 105824 in
  for-list + 2 PASS lines each py+C. A head 0f/38 tail
  2d/38 b5set {38}; C head 2f/38 tail 41/38 b5set {38}; Q
  head 43/38 tail c1/38 b5set {38} NO carry; R head c3/38
  tail c1/3a. Ring counter == raw lencode 256/256, 0
  mismatch. Odd-lencode 348/348. Matches A-609 (shape
  12/12 + quad 13/13 + counters 11/11 as sectioned;
  verdict line reads 39/39 + SecR as-filed; file read,
  counts verified; SecR writer-TBD tails ruled 2B 9ebb +
  b8/b9 1B-off - code stages exact QT values + Q comment
  states 2B 9ebb, P250/P253/P254 pattern) + A-366 (all 3
  legs CONFIRM; its S2 "r2/r3 last-3B" line predates SecR,
  values exact - SecR governs, memo-side prose only).
  Code-consts vs memo INCL (PBA 76 / C10 67 / quad 63 /
  T88 70): impl 75/66/62 = memo-1 on PBA/C10/quad (b5
  const 38 all three), 70 identical on T88 (A-609 S3
  explicitly no-finding).
- C diff purely additive: numstat 811/0 rgramc.c, 419/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 1293). C 806 content + 5 bare-`+` / 0 del; py 419
  content / 0 del. Fine-norm: C del-uniq 0 add-uniq 202
  EXACT + py del-uniq 0 add-uniq 219 EXACT under GATE's
  stated recipe ([0-9]+ -> N, diff-sign strip, trailing-';'
  strip, python sets, keep-empty; NO lead-ws strip) -
  sweep-r52 keep-empty family.
- Wall on 1293 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shim/ct-cache
  0, shebang 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1418->1424 +6, singletons `if n == ` 542->544 +2,
  range-guards `<= n <=` 472->476 +4, CLOSED prints
  1418->1424 +6, C singletons 537->539 +2 + C ranges
  472->476 +4 (5-offset pre-existing, unchanged), seal
  1512->1518 +6: all agree (GATE literals reproduced
  exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-609 CONFIRM
  39/39 + SecR (own 367-cell bed, BAD=0, tier cut SAFE) +
  A-366 corroborates 3/3. No CONFIRM-P255.md file; A-files
  suffice per rule. Agrees with cport msg (py/C 14926,
  PYID 7463).
- Own-loop 348/348 (105477..105824, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b363. Newest
  PARENT-* is QNUM-14 (GATE says QNUM-12 - stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing (all
  hex/counts from run output).

Verdict: PASS. Code CORRECT; GATE 1 immaterial staleness
(QNUM-12 vs -14).
