# VERIFY-1ff87cd1 b352 T10P244 pins 101649..101996 (1452 tiers) PASS

Seat viewer-r46, first-hand, detached tree-1ff87cd1 @1ff87cd1,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r46.
Base 74f7ebed (b351, 1446 tiers). Band = ee73b218 (py) + 1ff87cd1 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build352/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4a323a42 / aae d6e27c97
  (== GATE; aae.c untouched).
- RGRAMC-PYID 7122/7122 covered=7122/7122 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14244/14244 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14244/14244 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14244/14244, sorted).
- PINS 14246 rows (2 hdr + 14244, +62 vs base); PINS base-N
  7122 vs for-list 7122 exact both ways (0/0; tail 101996
  pinned AND in for-list). For-list 7091->7122 +31/-0
  verbatim == GATE's 31: sing 101649 101650; A 5 (101651
  head + 101652 + 101658 + 101662 + 101666 tail); C 6
  (101667 head + 101670 + 101671 + 101672 + 101673 + 101676
  tail); Q 10 (101677 head + 101687 + 101688 + 101693 +
  101703 + 101704 + 101709 + 101719 + 101725 + 101740 tail);
  R 8 (101741 head + edge pairs 101759/101760 + 101887/101888
  + mids 101805 + 101869 + 101996 tail). 31x2=62=14244-14182.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR, default backend).
- Tables audit P244 C-vs-py, own script tables352.py, 88/88
  ALL-EXACT (19-table PBA/C10-2SIG/quad-frag/T88 + M8/X8):
  S0/S1 (44620100 NEW @101649 b4b5 23/1a / 3d319602 NEW
  @101650 b4b5 25/1a, len 168 == lencode); AM 16/16 distinct
  6B; CM 10/10 distinct 17B diverge (2-sig map order EXACT:
  b8a9df02 x4 @101667-70 + dcd46f01 x2 @101671-72 +
  b8a9df02 x4 @101673-76); M 16/16 distinct 5B; QR 4/4
  TRIPLE r1==r2==r3 9bfa2d110601fedbf5b9 + r0
  4dfd1685ee000c5f8a75; QT 4/4 exact a3d62dc6/7e8e0fb4/
  a88e0fb4/d28e0fb4 + r1/r2/r3 TRUE-3B 8e0fb4; RM 16/16
  (8B) / RQ 16/16 (8B) UNPAIRED 0-overlap, tails SPLIT
  16/16 both; QB0/QB9/QB10/QB11 32/32 x4 (QB0 2x2-frag
  d0x11/c2x5/a0x11/85x5 exact; dual-coltab r0-vs-r123
  pos-diff QB9/QB10/QB11 = 15/16/16 exact); M8 16x1B
  4-valued a1x6/e1x6/61x2/21x2; X8 00x11+20x5 exact; b8
  XOR/ADD tie recomputed 256/256 all (c,r) with
  A=00x11+e0x5 (XOR staged per code comment); AC 76/76,
  CC 65/65, QC 59/59, RC 69/69; _N decls 76/65/59/69.
  Varsets exact: AC 8 (b4/b5+M6 b6,7,76-79), CC 19
  (b4/b5+M17 b0-3,6-8,10,11,48-51,80-83), QC 25
  (VPOS24+b5: b0-12,48-51,76-83), RC 19 (b4/b5+TM8 b9-11,
  19,76-79 + b8 + TR8 b13-16,80-83). Coverage 76+8/65+19/
  59+25/69+19 exact, 0 overlap, b4/b5 in no const set.
  Sig heads: AC de136329; CC b0-3 in tab (not consts), b9
  pinned const (skipped from mtab only); QC b0-3 in tabs;
  RC 02000000 (==P243T). RC b84-87 3e/1e/b3/cc. M-tails
  16/16 NEW vs P243M-tails AND vs P243QT (0 shared each).
  A/C/Q b5 const 1a whole-range (spots 271a/451a, 471a/591a,
  5b1a/d91a); ring head db/1a, edges off18/19
  ff/1a->01/1b + off146/147 ff/1b->01/1c, tail d9/1c.
  No BM/BC/M42/X42/M19/XA19/PT/PC/FM/FC; inventory
  exactly 19 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  101649, S1 101650, A 101651-66, C 101667-76, Q 101677-740
  m=off&15 q=off>>4 g=q==0?0:16, R 101741-996 c=off&15
  r=off>>4); C T-mirrors 6/6 exact bodies (T67107/112/117/
  132/149/182); ordered pay-index sequences C==py per range
  block (A 6B, C 17B b9-absent, Q 5+1+1+1+1+10+4B, R 8+8B +
  b8xor leg via snprintf/hexval); ring consts 219/26+
  (off>=19)+(off>=147) == py 0xdb/0x1a; temps _t5182..5209
  / _i3172..3181 / _b3171..3180 appended (base max _t5181/
  _i3170/_b3169, no reuse); insert at dispatch tail after
  T10P243R close, N-out-of-scope follows both sides.
- Edges head 101649 + 101759/101760 + 101887/101888 + tail
  101996 PASS 2/2 cells both legs. Odd-lencode whole-tier
  via own-loop 348/348. Matches A-577 (38/38 = 16/16 shape
  + 14/14 quad/ring + 8/8 counters, file read, counts
  verified; b8 tie staged XOR per family precedent).
- C diff purely additive: numstat 814/0 rgramc.c, 405/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 1282). C 809 content + 5 bare-`+` / 0 del.
  Fine-norm: del-uniq 0, missing 0 (== GATE); add-uniq 505
  reproduces EXACTLY — see note S1 (TNP decoded).
- Wall on 1282 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shebang/
  ct-cache 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1352->1358 +6, singletons `if n == ` 520->522 +2,
  range-guards `<= n <=` 428->432 +4, CLOSED prints
  1869->1875 +6, seal 1446->1452 +6: all agree (GATE
  literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-577 CONFIRM
  38/38 (predictive, own 364-cell bed, BAD=0). No
  CONFIRM-P244.md file; A-577 suffices per rule. Agrees
  with cport msg (py/C 14244, PYID 7122).
- Own-loop 348/348 (101649..101996, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b352. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-11 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

S1 TNP DECODED (method note resolving r44/r45 flag; code PASS,
GATE EXACT): sweep2's "TNP" fine-norm = normalize ONLY
_tN/_iN/_bN temp numbers (sed 's/_t[0-9]*/_tN/g' etc for
t/i/b), all other digits literal, sort -u, empty-excluding.
b352's 505 reproduces EXACTLY (python-set AND BSD pipeline
both 505). Cross-check on the flagged bands: same recipe
gives 415 (b348) and 398 (b350) = r45's recomputed values —
so r49's GATE counts (414/397) were genuine 1-off undercount
slips (same direction, consistent with the missing-trailing-
newline wc-l theory), NOT pipeline ambiguity; r50's b352
count is exact. Recommend parent ask sweep2 to spell TNP as
"temp-number-only norm" in the method string (their
"TNP/_tN/_iN/_bN" already says this — prior rounds tried
full-number norms).
Own near-misses caught pre-filing (script-only, code never
impugned): b9 first assumed varying (b9 IS a pinned const,
skipped from mtab only — fixed); "N out of scope" anchors
first hit helper occurrences (re-anchored past P244R close);
C-mirror check had a "/ * T" typo (fixed); edge-count probe
used BRE `$`-in-group (recounted with -E, 2/2). ALL-EXACT
re-run after fixes. No script bugs filed.

Verdict: PASS. Code CORRECT; GATE CORRECT (0 slips) + TNP
method decoded (flagged for parent).
Logs: NVME ws tmp/encode-viewer/r46/ (*352* set: build352,
pyid352, rgram352py/c, cmp352.py/.c(+full), for352-*,
sh352base, smoke352, tables352.py/.log, banddiff352(-c),
added352-all, numstat352, populate352, ownloop352.py/.log).
