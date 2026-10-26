# VERIFY-4b8d0444 b355 T10P247 pins 102693..103040 (1470 tiers) PASS

Seat viewer-r46, first-hand, detached tree-4b8d0444 @4b8d0444,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r46.
Base 42856cae (b354, 1464 tiers). Band = bd86982f (py) + 4b8d0444 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build355/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. SHA-1 first8 rgramc 25c89b8d / aae
  7d8dd3a2 + sha256 8aa5d7c9 / d6e27c97 (== GATE both;
  aae.c untouched).
- RGRAMC-PYID 7215/7215 covered=7215/7215 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14430/14430 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14430/14430 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14430/14430, sorted).
- PINS 14432 rows (2 hdr + 14430, +62 vs base); PINS base-N
  7215 vs for-list 7215 exact both ways (0/0; tail 103040
  pinned AND in for-list). For-list 7184->7215 +31/-0
  verbatim == GATE's 31: sing 102693 102694; A 6 (102695
  head + 102697 + 102698 + 102703 + 102709 + 102710 tail;
  off 1,4,5,7 = 102696/102699/102700/102702 unsampled);
  C 6 (102711 head + 102713 + 102714 + 102717 + 102719 +
  102720 tail; off 1,4,5,7 = 102712/102715/102716/102718
  unsampled); Q 10 (102721 head + 102729 + 102737 + 102745
  + 102753 + 102761 + 102769 + 102777 + carry pair 102783
  + 102784 tail LAST-INTERNAL); R 7 (102785 head + mid
  102849 + edge pair 102911/102912 + 102913 + LAST-CELL
  pair 103039/103040 tail). 31x2=62=14430-14368. PINS
  adds == for-list adds.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR, default backend).
- Tables audit P247 C-vs-py, own script tables355.py, 83/83
  ALL-EXACT (13-table A-split/C10-2SIG/QUADms-rowled+T88):
  S0/S1 (bcdf0200 NEW @102693 b4b5 4b/22 / dd39c205 NEW
  @102694 b4b5 4d/22, len 168 == lencode); AM 16/16
  distinct 9B (split map order EXACT: b0 b5 x3 @102695-97
  + b6 x12 @102698-709 + 98 x1 @102710 = full sigs
  b59d235c x3 + b69d235c x12 + 989d235c x1); CM 10/10
  distinct 16B diverge (2-sig map order EXACT: d939c205 x3
  @102711-13 + ec1ce102 x7 @102714-20, full sigs in tab);
  M 16/16 distinct 8B; QR 4/4 TRIPLE r1==r2==r3
  9ad7208268f9 + r0 8b072e0ee3cf; QT 4/4 exact a3afe2d0/
  69bd80b9/93bd80b9/bdbd80b9 + r1/r2/r3 TRUE-3B bd80b9;
  RQ==M shared-slice b76-79 same-index 16/16, full-string
  0/16 (P243-style, NOT P245 string-equal); RM 16/16 (8B)
  / RQ 16/16 (8B) UNPAIRED 0-overlap, tails SPLIT 16/16
  both; AC 73/73, CC 66/66, QC 64/64, RC 70/70; _N decls
  73/66/64/70. Varsets exact: AC 11 (b4/b5+M9 b0,9-12,
  76-79 split-b0 in m-tab), CC 18 (b4/b5+M16 b0-3,11,
  13-19,80-83 b12-skipped), QC 20 (b4/b5+M8 b12-14,19,
  76-79 + R6 b1-3,16-18 + T4 b80-83), RC 18 (b4/b5+TM8
  b28-31,80-83 + TR8 b16-18,23,76-79). Coverage 73+11/
  66+18/64+20/70+18 exact, 0 overlap, b4/b5 in no const
  set. b0-3: AC b1-3 9d235c const + b0 in tab; CC b0-3
  all in tab; QC b0 const 0x40; RC 02000000 (==P246T).
  CC b12 const 0x00 (skipped in m-tab); QC b42 const
  0x58 (NO b42 leg). RC b84-87 34/77/c0/b3. M-tails 16/16
  NEW vs P246M-tails, RM 16/16 NEW vs P246RM, QT 4/4 NEW
  vs P246QT (0 shared each). A b5 const 22 (4f/22..
  6d/22); C b5 const 22 (6f/22..81/22); Q b5-carry 22->23
  @102783->102784 LAST-INTERNAL (ff/22->01/23, head 83/22,
  mid c3/22); ring head 03/23, edge off126/127 ff/23->01/
  24, LAST-CELL edge off254/255 ff/24->01/25. No BM/BC/
  M42/X42/M8/X8/QB/M19/XA19/PT/FM; inventory exactly 13 +
  4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  102693, S1 102694, A 102695-710, C 102711-20, Q 102721-784
  m=off&15 q=off>>4, R 102785-103040 c=off&15 r=off>>4);
  C T-mirrors 6/6 exact bodies (T67831/836/841/857/874/897);
  ordered pay-index sequences C==py per range block (A 9B,
  C 16B b12-absent, Q 8/6/4B, R 8/8B); ring consts 3/35+
  (off>=127)+(off>=255) == py 0x03/0x23; temps _t5246..5263
  / _i3205..3214 / _b3204..3213 appended (base b354 max
  _t5245/_i3203/_b3202 first-hand, no reuse; _t max + _i/_b
  maxes == GATE); insert at dispatch tail after T10P246R
  close, N-out-of-scope follows both sides.
- Edges head 102693 + Q-carry 102783/102784 + 102911/102912
  + LAST-CELL 103039/103040 PASS 2/2 cells both legs.
  Odd-lencode whole-tier via own-loop 348/348. Matches
  A-582 (33/33 = 11/11 shape + 13/13 quad/ring + 9/9
  counters, file read, counts verified) + A-317 (3/3 legs
  CONFIRM, consts 74/67/64/70 INCL).
- C diff purely additive: numstat 610/0 rgramc.c, 238/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 911 — see note S2). C 605 content + 5 bare-`+` / 0
  del. Fine-norm: del-uniq 0, missing 0 (== GATE); add-uniq
  163 reproduces EXACTLY — see note S1.
- Wall on 911 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shebang/
  ct-cache 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1370->1376 +6, singletons `if n == ` 526->528 +2,
  range-guards `<= n <=` 440->444 +4, CLOSED prints
  T10P-scoped 1370->1376 +6, seal 1464->1470 +6: all agree
  (GATE literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-582 CONFIRM
  33/33 (predictive, own bed, BAD=0) + A-317 corroborates
  3/3. No CONFIRM-P247.md file; A-files suffice per rule.
  Agrees with cport msg (py/C 14430, PYID 7215).
- Own-loop 348/348 (102693..103040, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b355. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-11 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

S1 FINE-NORM METHOD NOTE (sweep-r50; code PASS, count EXACT):
"add-uniq 163" is EXACT under strip full-number norm +
trailing-';' strip, sets EXCLUDING the empty member (full
matrix 166/167/163/164). NOTE the pipeline drift: r48/b349
strip+keep, r49/b351+b353 nostrip+keep, r50/b355 strip+excl
— the SAME method string now covers 3 distinct actual
pipelines (4-cell matrix nearly populated). Standing
request (r44/r45/r46-S1-b352+b353): one canonical fine-norm
recipe stating strip/nostrip + empty-handling + number-scope.
S2 WALL-SCOPE COUNT SLIP (sweep-r50; code PASS, verdict
unaffected): GATE says "906 added lines" for scope
42856cae..4b8d0444, but its own numstat sums to 911
(610+238+1+62) and the diff holds 911 `+` lines (5 bare,
all rgramc.c). 911-906 = 5 = exactly the bare-line count:
their counter dropped empties (empty-excluding habit from
fine-norm leaking into the scope count). Bare lines cannot
carry vendor strings; my wall scan covers all 911 with 0
hits. Verdict stands; count worth one-line correcti
...[truncated 470 chars]