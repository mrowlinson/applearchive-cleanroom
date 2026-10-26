# VERIFY-42856cae b354 T10P246 pins 102345..102692 (1464 tiers) PASS

Seat viewer-r46, first-hand, detached tree-42856cae @42856cae,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r46.
Base dbbeec8b (b353, 1458 tiers). Band = 23ce1eb8 (py) + 42856cae (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build354/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 329d4031 / aae d6e27c97
  (== GATE; aae.c untouched).
- RGRAMC-PYID 7184/7184 covered=7184/7184 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14368/14368 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14368/14368 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14368/14368, sorted).
- PINS 14370 rows (2 hdr + 14368, +62 vs base); PINS base-N
  7184 vs for-list 7184 exact both ways (0/0; tail 102692
  pinned AND in for-list). For-list 7153->7184 +31/-0
  verbatim == GATE's 31: sing 102345 102346; A 6 (102347
  head + 102348 + 102354 + 102358 + 102361 + 102362 tail);
  C 6 (102363 head + 102365 + 102366 + 102369 + 102371 +
  102372 tail; off 1,4,7 = 102364/102367/102370 unsampled);
  Q 10 (102373 head + 102381 + 102389 + carry pair 102399/
  102400 + 102405 + 102413 + 102421 + 102429 + 102436
  tail); R 7 (102437 head + edge pairs 102527/102528 +
  102655/102656 + mid 102565 + 102692 tail). 31x2=62=
  14368-14306. PINS adds == for-list adds.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR, default backend).
- Tables audit P246 C-vs-py, own script tables354.py, 79/79
  ALL-EXACT (13-table PBA/C10-2SIG/quad+T88): S0/S1
  (acdf0200 NEW @102345 b4b5 93/1f / 7d38be05 ==P245C10a
  @102346 b4b5 95/1f, len 168 == lencode); AM 16/16
  distinct 8B; CM 10/10 distinct 15B diverge (2-sig map
  order EXACT: be05 x3 @102363-65 + de02 x7 @102366-72 =
  full sigs 7d38be05 x3 + 7d38de02 x7 == P245C10 map);
  M 16/16 distinct 8B; QR 4/4 TRIPLE r1==r2==r3
  0684f4980f3390be + r0 68a3b49f6fb343aa; b42 ROW-LED
  0x9f r0 vs 0x98 r123 (R8 entry[6:8]); QT 4/4 exact
  a5790fa5/98d6bdbc/c2d6bdbc/ecd6bdbc + r1/r2/r3 TRUE-3B
  d6bdbc; RM 16/16 (6B) / RQ 16/16 (8B) UNPAIRED
  0-overlap, tails SPLIT 16/16 both; AC 74/74, CC 67/67,
  QC 62/62, RC 72/72; _N decls 74/67/62/72. Varsets exact:
  AC 10 (b4/b5+M8 b34,35,42,43,76-79), CC 17 (b4/b5+M15
  b2,3,34,35,41-47,80-83), QC 22 (b4/b5+QM8 b48-51,76-79 +
  R8 b34,35,41-46 incl b42 + T4 b80-83), RC 16 (b4/b5+TM6
  b6,7,80-83 + TR8 b52-55,76-79). Coverage 74+10/67+17/
  62+22/72+16 exact, 0 overlap, b4/b5 in no const set.
  Sig heads: AC 2085c74e NEW; CC 0:7d 1:38 const + b2,3
  in tab; QC 2085c72e (==P245PBA, cross-checked vs P245QC
  b0-3); RC 02000000 (==P245T). RC b84-87 03/ed/d2/98.
  M-tails 16/16 NEW vs P245M-tails AND 0/16 vs P245QT.
  A b5 const 1f (97/1f..b5/1f); C b5 const 1f (b7/1f..
  c9/1f); Q b5-carry 1f->20 @102399->102400 (ff/1f->01/20,
  tail 49/20); ring head 4b/20, edges off90/91 ff/20->01/
  21 + off218/219 ff/21->01/22, tail 49/22. No BM/BC/M42/
  X42/M8/X8/QB/M19/XA19/PT/FM; inventory exactly 13 + 4
  _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  102345, S1 102346, A 102347-62, C 102363-72, Q 102373-436
  m=off&15 q=off>>4, R 102437-692 c=off&15 r=off>>4); C
  T-mirrors 6/6 exact bodies (T67594/599/604/619/636/659);
  ordered pay-index sequences C==py per range block (A 8B,
  C 15B, Q 8/8/4B, R 6/8B); ring consts 75/32+(off>=91)+
  (off>=219) == py 0x4b/0x20; temps _t5228..5245 /
  _i3194..3203 / _b3193..3202 appended (base b353 max
  _t5227/_i3192/_b3191 first-hand, no reuse); insert at
  dispatch tail after T10P245R close, N-out-of-scope
  follows both sides.
- Edges head 102345 + Q-carry 102399/102400 + 102527/102528
  + 102655/102656 + tail 102692 PASS 2/2 cells both legs.
  Odd-lencode whole-tier via own-loop 348/348. Matches
  A-581 (33/33 = 11/11 shape + 13/13 quad/ring + 9/9
  counters, file read, counts verified).
- C diff purely additive: numstat 610/0 rgramc.c, 238/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 911). C 605 content + 5 bare-`+` / 0 del.
  Fine-norm: del-uniq 0, missing 0 (== GATE); add-uniq 384
  reproduces EXACTLY under decoded TNP (temp-number-only
  norm, BSD pipeline; full-number matrix 157/158/154/155
  nowhere near — further confirmation TNP is temp-only).
  sweep2-r50 now 2/2 exact (b352 505, b354 384); r49's
  b348/b350 1-off slips stand as genuine count slips.
- Wall on 911 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shebang/
  ct-cache 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1364->1370 +6, singletons `if n == ` 524->526 +2,
  range-guards `<= n <=` 436->440 +4 (== GATE stated
  method), CLOSED prints T10P-scoped 1364->1370 +6, seal
  1458->1464 +6: all agree.
- CONFIRM evidence (CONVERT-01 rule b): A-581 CONFIRM
  33/33 (predictive, own bed, BAD=0). No CONFIRM-P246.md
  file; A-581 suffices per rule. Agrees with cport msg
  (py/C 14368, PYID 7184).
- Own-loop 348/348 (102345..102692, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b354. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-11 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

Verdict: PASS. Code CORRECT; GATE CORRECT (0 slips).
Logs: NVME ws tmp/encode-viewer/r46/ (*354* set: build354,
pyid354, rgram354py/c, cmp354.py/.c(+full), for354-*,
sh354base, smoke354, tables354.py/.log, banddiff354(-c),
added354-all, numstat354, populate354, ownloop354.py/.log).
