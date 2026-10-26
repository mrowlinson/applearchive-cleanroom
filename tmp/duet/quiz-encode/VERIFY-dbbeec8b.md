# VERIFY-dbbeec8b b353 T10P245 pins 101997..102344 (1458 tiers) PASS

Seat viewer-r46, first-hand, detached tree-dbbeec8b @dbbeec8b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r46.
Base 1ff87cd1 (b352, 1452 tiers). Band = db592df5 (py) + dbbeec8b (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build353/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. SHA-1 first8 rgramc 974d4072 / aae
  7d8dd3a2 (== GATE; aae.c untouched; sha256 d3709400/
  d6e27c97).
- RGRAMC-PYID 7153/7153 covered=7153/7153 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14306/14306 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14306/14306 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14306/14306, sorted).
- PINS 14308 rows (2 hdr + 14306, +62 vs base); PINS base-N
  7153 vs for-list 7153 exact both ways (0/0; tail 102344
  pinned AND in for-list). For-list 7122->7153 +31/-0
  verbatim == GATE's 31: sing 101997 101998; A 6 (101999
  head + 102000 + 102006 + 102010 + 102013 + 102014 tail);
  C 6 (102015 head + 102016 + 102017 + 102018 + 102021 +
  102024 tail; off 4,5,7,8 = 102019/102020/102022/102023
  unsampled); Q 10 (102025 head + 102033 + 102041 + 102049
  + 102057 + 102065 + 102073 + 102081 + 102087 + 102088
  tail); R 7 (102089 head + edge pairs 102143/102144 +
  102271/102272 + mid 102217 + 102344 tail). 31x2=62=
  14306-14244. PINS adds == for-list adds.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR, default backend).
- Tables audit P245 C-vs-py, own script tables353.py, 79/79
  ALL-EXACT (13-table A/C10/QUADms+T88): S0/S1 (d46f0100
  NEW @101997 b4b5 db/1c / b553d702 NEW @101998 b4b5 dd/1c,
  len 168 == lencode); AM 16/16 distinct 6B; CM 10/10
  distinct 17B diverge (2-sig map order EXACT: be05 x3
  @102015-17 + de02 x7 @102018-24 = full sigs 7d38be05 x3
  + 7d38de02 x7 with b0,b1 consts); M 16/16 distinct 8B;
  QR 4/4 TRIPLE r1==r2==r3 ba7c80a31478a7 + r0
  933cc422d4f27c; QT 4/4 exact c26f98d7/78214c1b/a2214c1b/
  cc214c1b + r1/r2/r3 TRUE-3B 214c1b; RQ==M string-equal
  16/16 same-index (positions differ, no shared bytes);
  RM 16/16 (7B) / RQ 16/16 (8B) distinct, tails SPLIT
  16/16 both, full-overlap 0 (UNPAIRED holds); AC 76/76,
  CC 65/65, QC 63/63, RC 71/71; _N decls 76/65/63/71.
  Varsets exact: AC 8 (b4/b5+M6 b24,25,76-79), CC 19
  (b4/b5+M17 b2,3,21-31,80-83), QC 21 (b4/b5+M8 b21-23,
  31,76-79 + R7 b24-30 + T4 b80-83), RC 17 (b4/b5+TM7
  b40-42,76-79 + TR8 b25-27,35,80-83). Coverage 76+8/
  65+19/63+21/71+17 exact, 0 overlap, b4/b5 in no const
  set. Sig heads: AC 2085c72e NEW; CC 0:7d 1:38 const +
  b2,3 in tab (2-sig 7d38+tab); QC 2085c72e (==PBA sig);
  RC 02000000 (==P244T sig). QC b42 const 0x95 (NO b42
  leg). RC b84-87 b1/96/ff/e1. M-tails 16/16 NEW vs
  P244M-tails, RM 16/16 NEW vs P244RM, QT 4/4 NEW vs
  P244QT (0 shared each). A b5 const 1c (df/1c..fd/1c);
  C b5-carry 1c->1d INSIDE @102015->102016 (ff/1c->01/1d,
  tail 11/1d); Q b5 const 1d (13/1d, mid 53/1d, tail
  91/1d); ring head 93/1d, edges off54/55 ff/1d->01/1e +
  off182/183 ff/1e->01/1f, tail 91/1f. No BM/BC/M42/X42/
  M8/X8/QB/M19/XA19/PT/FM; inventory exactly 13 + 4 _N,
  novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  101997, S1 101998, A 101999-102014, C 102015-24, Q
  102025-88 m=off&15 q=off>>4, R 102089-344 c=off&15
  r=off>>4); C T-mirrors 6/6 exact bodies (T67356/361/366/
  381/398/421); ordered pay-index sequences C==py per range
  block (A 6B, C 17B, Q 8/7/4B, R 7/8B); ring consts 147/
  29+(off>=55)+(off>=183) == py 0x93/0x1d; temps _t5210..
  5227 / _i3183..3192 / _b3182..3191 appended (base b352
  max _t5209/_i3181/_b3180, no reuse); insert at dispatch
  tail after T10P244R close, N-out-of-scope follows both
  sides.
- Edges head 101997 + C-carry 102015/102016 + 102143/102144
  + 102271/102272 + tail 102344 PASS 2/2 cells both legs.
  Odd-lencode whole-tier via own-loop 348/348. Matches
  A-580 (34/34 = 12/12 shape + 13/13 quad/ring + 9/9
  counters, file read, counts verified) + A-315 (3/3 legs
  CONFIRM, consts 77/65/64/71 INCL).
- C diff purely additive: numstat 610/0 rgramc.c, 237/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 910). C 605 content + 5 bare-`+` / 0 del.
  Fine-norm: del-uniq 0, missing 0 (== GATE); add-uniq 158
  reproduces EXACTLY — see note S1.
- Wall on 910 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shebang/
  ct-cache 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1358->1364 +6, singletons `if n == ` 522->524 +2,
  range-guards `<= n <=` 432->436 +4, CLOSED prints
  T10P-scoped 1358->1364 +6 (== GATE literals; all-CLOSED
  1875->1881 +6 same delta), seal 1452->1458 +6: all agree
  (GATE literals reproduced exactly; cport msg seals 1458).
- CONFIRM evidence (CONVERT-01 rule b): A-580 CONFIRM
  34/34 (predictive, own 364-cell bed, BAD=0) + A-315
  corroborates 3/3. No CONFIRM-P245.md file; A-files
  suffice per rule. Agrees with cport msg (py/C 14306,
  PYID 7153).
- Own-loop 348/348 (101997..102344, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b353. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-11 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

S1 FINE-NORM METHOD NOTE (sweep-r49; code PASS, count EXACT):
"add-uniq 158" is EXACT under nostrip full-number norm +
trailing-';' strip with sets KEEPING the empty member (157+1;
verified first-hand; full matrix 157/158/154/155). Same
actual pipeline as r49's own b351 (182, nostrip+keep-empty)
— r49 self-consistent; the strip/nostrip split is r48-vs-r49
(b349 stripped), not within r49. Standing request (r44/r45/
r46-S1-b352): one canonical fine-norm recipe stating
strip/nostrip + empty-handling + number-scope (full vs TNP
temp-only).
Own near-miss caught pre-filing (script-only, code never
impugned): CM sig check first sliced entry[:8] (4B incl
b21,b22); sig bytes b2,b3 = entry[:4] — fixed, ALL-EXACT
re-run. No script bugs filed.

Verdict: PASS. Code CORRECT; GATE CORRECT (0 slips) + 1
standing method note (flagged).
Logs: NVME ws tmp/encode-viewer/r46/ (*353* set: build353,
pyid353, rgram353py/c, cmp353.py/.c(+full), for353-*,
sh353base, smoke353, tables353.py/.log, banddiff353(-c),
added353-all, numstat353, populate353, ownloop353.py/.log).
