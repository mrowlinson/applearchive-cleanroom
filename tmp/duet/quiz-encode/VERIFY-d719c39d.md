# VERIFY-d719c39d b357 T10P249 pins 103389..103736 (1482 tiers) PASS

Seat viewer-r47, first-hand, detached tree-d719c39d @d719c39d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r47.
Base f9bb207b (b356, 1476 tiers). Band = 1352f58d (py) + d719c39d (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build357/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 00ea4b5e / aae 7d8dd3a2 +
  sha256 51554ddc / d6e27c97 (== GATE both; aae.c untouched).
- RGRAMC-PYID 7277/7277 covered=7277/7277 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14554/14554 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14554/14554 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14554/14554, sorted).
- PINS 14556 rows (2 hdr + 14554, +62 vs base 14494); PINS
  base-N 7277 vs for-list 7277 exact both ways (0/0; tail
  103736 pinned AND in for-list). For-list 7246->7277 +31/-0
  verbatim == GATE's 31: sing 103389 103390; A 6 (103391
  head + 103392 + 103398 + 103402 + 103405 + 103406 tail);
  C 8 (103407 head + 103409 + 103410 + 103411 + 103412 +
  103413 + 103414 + 103415; offs 1,9 = 103408,103416
  unsampled); Q 8 (103417 head + EARLY-carry pair 103423 +
  103424 + 103433 + 103449 + 103465 + 103479 + 103480 tail);
  R 7 (103481 head + edge pairs 103551/103552 + 103679/103680
  + mid 103609 + 103736 tail). 31x2=62=14554-14492. PINS
  adds == for-list adds x2.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR, default backend).
- Tables audit P249 C-vs-py, own script tables357.py, 87/87
  ALL-EXACT (13-table A-PBA/C10-MS-7SIG/QUADms-1Boff+T88):
  S0/S1 (18e10200 NEW @103389 b4b5 bb/27 / c503ce05
  ==P248PB1 @103390 b4b5 bd/27 NEW string, len 168 ==
  lencode); AM 16/16 distinct 8B; CM 10/10 distinct 13B
  diverge (7-sig map order EXACT: c503ce05 x3 @103407-09
  + c5034e05/c5030e04/c5034e04/c5036e04/c5037e04 x1 +
  c503be04 x2 @103415-16, full sigs via CC b0,b1 c5,03);
  M 16/16 distinct 8B; QR 4/4 TRIPLE r1==r2==r3
  460a99cc5196b776 + r0 47cad1a5d1b2a75c (b3 row-sigs
  47/46/46/46); QT 4/4 exact 6d6d4ae9/706b3942/9a6b3942/
  c46b3942 (r1/r2/r3 share last-3B 6b3942); RQ==M
  shared-slice b6,7,76-79 same-index 16/16, full-string
  0/16 (P243-style, layouts diverge at byte2 RQ b12 vs M
  b8); M-tails 16/16 NEW vs P248M, RM 16/16 NEW vs P248RM,
  QT 4/4 NEW vs P248QT (0 shared each); RM 16/16 (7B) /
  RQ 16/16 (7B) UNPAIRED 0-overlap, tails SPLIT 16/16 both;
  AC 74/74, CC 69/69, QC 62/62, RC 72/72; _N decls
  74/69/62/72. Varsets exact: AC 10 (b4/b5+M8 b48-51,
  76-79), CC 15 (b4/b5+M13 b2,3,35,46-51,80-83), QC 22
  (b4/b5+QM8 b6-9,76-79+R8 b3,35,46-51+T4 b80-83), RC 16
  (b4/b5+TM7 b9-11,80-83+TR7 b6,7,12,76-79). Coverage
  74+10/69+15/62+22/72+16 exact, 0 overlap, b4/b5 in no
  const set. AC sig 809a1f4a == P248PBA; CC b0,1 c5,03 +
  b2,3 in tab; QC b0-2 5c,3c,e0 + b3 in tab (row-sig);
  RC sig 05000000 NEW (breaks 02000000 run, P248 first-hand);
  b42 const 0x9d/0x8a/0x8a/0x79 via consts, NO b42 leg;
  RC b84-87 79/ad/62/84. A b5 const 27 (bf27..dd27); C b5
  const 27 (df27..f127); Q b5-carry 27->28 (f327 head,
  ff27->0128 @103423->103424 EARLY-INTERNAL off6->7);
  ring head 73/28, edges off70/71 + off198/199 exact, tail
  off255 71/2a; counter==lencode 256/256. No BM/BC/M42/X42/
  M8/X8/QB/M19/XA19/PT/PC/FM/FC/FS/FO/RF; inventory exactly
  13 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  103389, S1 103390, A 103391-406, C 103407-416, Q 103417-480
  m=off&15 q=off>>4, R 103481-736 c=off&15 r=off>>4);
  C T-mirrors 6/6 exact bodies (T68300/68305/68310/68325/
  68341/68364); ordered pay-index sequences C==py per range
  block (A n=10, C n=15, Q n=22, R n=16); ring consts
  0x73/0x28 + (off>=71)+(off>=199) == py; temps _t5280..5297
  / _i3226..3235 / _b3225..3234 appended (base b356 max
  _t5279/_i3224/_b3223 first-hand via git show, no reuse;
  _i3225 skipped); insert at dispatch tail after T10P248R
  close, N-out-of-scope follows both sides.
- Edges head 103389 + Q-carry 103423/103424 + 103551/103552
  + 103679/103680 + tail 103736 PASS 2/2 cells both legs
  (8 cells). Odd-lencode whole-tier via own-loop 348/348.
  Matches A-597 (33/33 = 11/11 shape + 12/12 quad/ring +
  10/10 counters, file read, counts verified) + A-319 (3/3
  legs CONFIRM). Code-consts vs memo INCL (PBA 75 / C10 70
  / quad 62 / T88 72): impl 74/69 = memo-1 on PBA/C10,
  quad/T88 62/72 identical (A-597 §3 explicitly no-finding).
- C diff purely additive: numstat 610/0 rgramc.c, 237/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 910). C 605 content + 5 bare-`+` / 0 del (all 5 bare
  in rgramc.c). Fine-norm: del-uniq 0, add-uniq 174 EXACT
  under GATE's stated recipe (full-number strip +
  trailing-';' strip, keep-empty; excl-empty would be 173)
  — sweep-r51 strip+keep family; TNP temp-only reads 413
  (see standing drift note).
- Wall on 910 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shim/ct-cache
  0, shebang 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1382->1388 +6, singletons `if n == ` 530->532 +2,
  range-guards `<= n <=` 448->452 +4, CLOSED prints
  1382->1388 +6, C singletons 525->527 +2 + C ranges
  448->452 +4 (5-offset pre-existing, unchanged), seal
  1476->1482 +6: all agree (GATE literals reproduced
  exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-597 CONFIRM 33/33
  (backfill, own 364-cell bed, BAD=0) + A-319 corroborates
  3/3. No CONFIRM-P249.md file; A-files suffice per rule.
  Agrees with cport msg (py/C 14554, PYID 7277).
- Own-loop 348/348 (103389..103736, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b357. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-12 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing (all
  hex/counts from run output).

Verdict: PASS. Code CORRECT; GATE 1 immaterial staleness (QNUM-12 vs -13).
