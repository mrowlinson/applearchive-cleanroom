# VERIFY-e97ace92 b348 T10P240 pins 100257..100604 (1428 tiers) PASS

Seat viewer-r45, first-hand, detached tree-e97ace92 @e97ace92,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r45.
Base 5f75b749 (b347, 1422 tiers). Band = f2d995a2 (py) + e97ace92 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build348/bin, rc=0, 0 warnings. sha256 rgramc
  92a65098 / aae d6e27c97 (== GATE; aae.c untouched).
- RGRAMC-PYID 6998/6998 covered=6998/6998 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13996/13996 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 13996/13996 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 13998 rows (2 hdr + 13996, +62 vs base); PINS cells
  6998 vs for-list 6998 exact match both ways (sorted, diff 0).
  For-list 6967->6998 +31/-0 verbatim == GATE's 31: sing
  100257 100258; A 4 (100259 head + 100260 off1 + 100266
  off7 + 100274 tail); C 7 (100275/100276/100277/100278/
  100279/100281/100284 = off0,1,2,3,4,6,9; off5,7,8 =
  100280/100282/100283 confirmed unsampled); Q 12 (row
  starts 100285/100301/100317/100333 + row ends 100300/
  100316/100332/100348 + mids 100292/100308/100324/100340);
  R 6 (100349 head + 100351/100352 + 100479/100480 + 100604
  tail).
  31x2=62=13996-13934. PINS adds == for-list adds.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR).
- Tables audit P240 C-vs-py, own script tables348.py, 59/59
  ALL-EXACT (13-table, no M19/XA19): S0/S1 (3f550100 NEW /
  4dc2a402 NEW, len 168, b4b5 430f/450f == lencode), AM 16/16
  distinct 10B, CM 10/10 distinct 20B 2-sig map a402 x3 +
  5401 x7 exact order (b2/b3 of 4dc2a402/4dc25401, CC b0/b1
  const 4d/c2), M 16/16 distinct 6B b0 16-distinct, QR 4/4
  TRIPLE r1==r2==r3 f14c2234156e + r0 2540eeb42b46, QT 4/4
  exact 58bdc6b0/ce29d41d/f829d41d/f9b1c924 + r1/r2 TRUE-3B
  29d41d, RM 16/16 (9B) / RQ 16/16 (6B) UNPAIRED, AC 72/72,
  CC 62/62, QC 66/66, RC 71/71; _N decls 72/62/66/71. Varsets
  exact: AC 12, CC 22, QC 18, RC 17 (A-561 VPOS + b5-excl on
  A/C/Q; b4/b5 in R VPOS). Coverage 72+12/62+22/66+18/71+17
  exact, 0 overlap, b4/b5 in no const set. Sig heads: AC
  b0-3 a0955736, QC b0-3 4dc25415 + b42 0x9f const (NO
  coupling leg, verified in consts), RC b0-3 01000000,
  RC b84-87 02/37/bb/ef. M-tails NEW vs P239M; QT 0/4 vs
  P239QT. Ring tails SPLIT 16/16 both. A/C/Q b5 const 0f,
  raw lencode (S/A/C/Q heads/mids/tails checked); ring
  edges off2/3 + off130/131 (0xfb/0x0f base). No M19/XA19/
  M42/X42/BM/BC/PT/PC/FM/FC; inventory exactly 13 + 4 _N,
  novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  100257, S1 100258, A 100259-74, C 100275-84, Q 100285-348
  m=off&15 q=off>>4, R 100349-604 c=off&15 r=off>>4); C
  T-mirrors 6/6 exact (T65974/979/984/66000/018/041); guards
  + byte positions exact (A b14,15,21-23,31,76-79; C
  b2,3,20-27,30-35,80-83; Q M b36,37,76-79 + QR
  b22,23,30,32-34 + QT b80-83; R M9 b19,27,39,46,47,80-83 +
  R6 b40,41,76-79); ring consts 251/15/3/131 == py
  0xfb/0x0f/3/131; temps _t5108.._t5125 + _b3127.._b3136 +
  _i3128.._i3137 appended (base max _t5107/_b3125/_i3126;
  _b3126/_i3127 generator gap, no reuse); insert after
  T10P239R close at dispatch tail, N-out-of-scope follows
  both sides.
- Edges 100351/100352 + 100479/100480 PASS 2/2 cells both
  legs (off2/3 ff/0f->01/10, off130/131 ff/10->01/11).
  Odd-lencode whole-tier via own-loop 348/348. Matches A-561
  (33/33 = 15/15 shape + 10/10 quad/ring + 8/8 counters,
  file read, counts verified; next-tier @100605/606/607
  repeat noted).
- C diff purely additive: numstat 610/0 rgramc.c, 238/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  911/1). C 605 content + 5 bare-`+` / 0 del; the 1 del is
  the for-line old version. Fine-norm: del-uniq 0, missing 0
  (== GATE); add-uniq 415 under temps-only norm (tried
  +strip 413, case-fold 415, LC_ALL=C 415, semi-strip 415,
  squeeze 413, trail/lead-strip 415/413) vs GATE's 414 —
  see note S1.
- Wall on 911 added lines (906 content + 5 bare): vendor/
  disasm 0, depload 0, libcompression/CT-shim/shebang/aa/
  nominated 0 on code; 62 `ct-lzraven` PINS backend tags
  (provenance column, every band).
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10`
  1587->1593 +6, singletons `if n == ` 512->514 +2,
  range-guards `<= n <=` 412->416 +4, CLOSED prints
  `print("CLOSED` 1845->1851 +6, seal 1422->1428 +6: all
  agree (GATE literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-561 CONFIRM
  33/33 (predictive, own 364-cell bed, BAD=0). Agrees with
  cport msg (py/C 13996, PYID 6998).
- Own-loop 348/348 (100257..100604, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b348. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-10 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

1 GATE COUNT SLIP (sweep2-r49; code PASS): (S1) fine-norm
"add-uniq 414" reproduces under no reasonable reading
(temps-only _tN/_iN/_bN norm = 415; any leading-strip = 413;
trail-strip/case-fold/LC_ALL=C/semi-strip = 415; the strip
merges exactly the 3 indent variants of bare-`}` 12/8/4-sp).
Theirs = plain-minus-1, the SAME systematic 1-off r44 caught
in sweep2-r48 GATEs (b344 438/437, b346 391/390 — now 3/3
sweep2 bands this pattern; consistent with a missing-trailing-
newline `wc -l` undercount in their pipeline). Del-uniq 0 +
missing 0 agree; purely-additive verdict unaffected.

Verdict: PASS. Code CORRECT; GATE 1 count slip (flagged).
Logs: NVME ws tmp/encode-viewer/r45/ (*348* set:
build348, pyid348, rgram348py/c, cmp348.py/.c, for348-*,
pins348.basen, smoke348, tables348.py/.log, banddiff348(-c),
added348(-all), numstat348, caddnorm348-plain/-strip,
populate348, ownloop348.py/.log).
