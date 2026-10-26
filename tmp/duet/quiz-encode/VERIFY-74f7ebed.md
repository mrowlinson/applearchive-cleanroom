# VERIFY-74f7ebed b351 T10P243 pins 101301..101648 (1446 tiers) PASS

Seat viewer-r45, first-hand, detached tree-74f7ebed @74f7ebed,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r45.
Base 20efeb92 (b350, 1440 tiers). Band = 979dc293 (py) + 74f7ebed (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build351/bin, rc=0, 0 warnings. SHA-1 first8
  rgramc 0fdc075e / aae 7d8dd3a2 (== GATE; aae.c untouched).
- RGRAMC-PYID 7091/7091 covered=7091/7091 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14182/14182 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14182/14182 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 14184 rows (2 hdr + 14182, +62 vs base); PINS cells
  7091 vs for-list 7091 exact match both ways (sorted, diff 0;
  tail 101648 pinned AND in for-list). For-list 7060->7091
  +31/-0 verbatim == GATE's 31: sing 101301 101302; A 5
  (101303 head + 101304 + 101310 + 101314 + 101318 tail);
  B 5 (101319/101320 off0,1 + 101323/101324 off4,5 + 101328
  tail; off2,3,6,7,8 = 101321/101322/101325/101326/101327
  confirmed unsampled); Q 13 (101329 head + 101336 +
  101344/101345 + 101352 + 101360/101361 + 101368 + carry
  pair 101375/101376 + 101377 + 101384 + 101392 tail); R 6
  (101393 head + 101503/101504 + 101631/101632 + 101648
  tail). 31x2=62=14182-14120. PINS adds == for-list adds.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR).
- Tables audit P243 C-vs-py, own script tables351.py, 71/71
  ALL-EXACT (15-table A/B10/QUADms+T88, no CM/CC): S0/S1
  (4b620100 REPEAT-P242 / 3d31c602 NEW, len 168, b4b5 6b17/
  6d17 == lencode), AM 16/16 distinct 6B, BM 10/10 distinct
  11B diverge (b42 slice e1x3/cc/c3/c8/ca/cc/cf/ca varying;
  sig 3d31c602 in BC consts, NOT in tab — B10 not C10), M
  16/16 distinct 10B (b0 31x8/b1x8), M42 16x1B 4-valued
  06/46/86/c6 3/5/5/3 exact, X42 [00,0c,0c,0c], b42 XOR/ADD
  TIE recomputed 64/64 all (m,q) (XOR-staged per code
  comment + memo precedent), QR 4/4 6B TRIPLE r1==r2==r3
  36db363b3135 + r0 ed596928b1d5, QT 4/4 exact 8469e6f6/
  5d42faad/928403ae/bc8403ae + r2/r3 TRUE-3B 8403ae,
  RQ/M shared-slice b76-79 same-index 16/16, RM 16/16 (8B)
  / RQ 16/16 (11B) UNPAIRED, AC 76/76, BC 71/71, QC 61/61,
  RC 67/67; _N decls 76/71/61/67. Varsets exact: AC 8
  (b4/b5+M6 b36,37,76-79), BC 13 (b42 IN M-range), QC 23
  (QM10+b42+R6+T4), RC 21 (b4/b5+TM8+TR11). Coverage 76+8/
  71+13/61+23/67+21 exact, 0 overlap, b4/b5 in no const
  set. Sig heads: AC 0080773c (==P242Q), BC 3d31c602
  (==PB1), QC 0080773c (==PBA), RC 02000000 (==P242T), RC
  b84-87 cd/ea/d4/5d. M-tails NEW vs P242M-tails AND vs
  P242QT; RM NEW vs P242RM; QT 4/4 NEW vs P242QT. Ring
  tails SPLIT 16/16 both. A/B b5 const 17; Q b5-carry
  17->18 @101375->101376 (ff/17->01/18); ring head 23/18,
  edges off110/111 + off238/239, tail 21/1a (0x23/0x18
  base). No CM/CC/M19/XA19/PT/PC/FM/FC; inventory exactly
  15 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  101301, S1 101302, A 101303-18, B 101319-28, Q 101329-392
  m=off&15 q=off>>4, R 101393-648 c=off&15 r=off>>4); b42
  XOR leg both sides (py `pay[42] ^ X42[q] == M42[m]`; C
  via snprintf %02lx + hexval) + ADD-tie comment present;
  C T-mirrors 6/6 exact (T66711/716/721/736/752/778); guards
  + byte positions exact (A b36,37,76-79; B b36-42,80-83
  b42-IN; Q M b14,15,23,34,35,43,76-79 + b42 + R6 b36-41 +
  QT b80-83; R TM8 b52-55,80-83 + TR11 b18,19,27,38,39,46,
  47,76-79); ring consts 35/24/111/239 == py 0x23/0x18/
  111/239; temps _t5162.._t5181 appended (base max _t5161,
  no reuse); insert at dispatch tail, N-out-of-scope follows
  both sides.
- Edges Q-carry 101375/101376 + 101503/101504 + 101631/
  101632 + head 101301 + tail 101648 PASS 2/2 cells both
  legs (off110/111 ff/18->01/19, off238/239 ff/19->01/1a).
  Odd-lencode whole-tier via own-loop 348/348. Matches
  A-573 (34/34 = 15/15 shape + 11/11 quad/ring + 8/8
  counters, file read, counts verified; b42 tie staged XOR
  per P235 precedent) + A-313 (3/3 legs; tie flagged per
  request, VERDICT tie, staged XOR stands).
- C diff purely additive: numstat 640/0 rgramc.c, 262/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  965/1). C 635 content + 5 bare-`+` / 0 del. Fine-norm:
  del-uniq 0, missing 0 (== GATE); add-uniq 182 reproduces
  EXACTLY — see note S1.
- Wall on 965 added lines (960 content + 5 bare): vendor/
  disasm 0, depload 0, libcompression/CT-cache/CT_CACHE/aa/
  nominated 0, shebang 0. (62 `ct-lzraven` PINS backend
  tags, provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1346->1352 +6, singletons `if n == ` 518->520 +2,
  range-guards `<= n <=` 424->428 +4, CLOSED prints
  `print("CLOSED` 1863->1869 +6, seal 1440->1446 +6: all
  agree (GATE literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-573 CONFIRM
  34/34 (predictive, own 364-cell bed, BAD=0) + A-313
  corroborates 3/3. Agrees with cport msg (py/C 14182,
  PYID 7091).
- Own-loop 348/348 (101301..101648, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b351. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-11 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

1 GATE METHOD NOTE (sweep-r49; code PASS): (S1) fine-norm
"add-uniq 182" is EXACT under their actual pipeline
(nostrip [0-9]+ -> N + trailing-';' strip over all 640 adds
incl 5 bare, sets KEEP the empty member: 181 + 1 = 182;
verified first-hand) — but the method string omits the
empty-inclusion, and NOTE: b349's identical method string
needed strip+keep-empty for its 154 (sweep-r48 strips,
sweep-r49 does not — the 3-delta both ways is exactly the
4-indent-`}` group). So same-seat adjacent rounds run
DIFFERENT actual pipelines under IDENTICAL method strings;
worth one canonical fine-norm recipe stating strip/nostrip
+ empty-handling (extends VERIFY-b3b974d6 S1).
Own near-miss caught pre-filing (BM check first assumed
C10-style sig-in-tab; B10 sig is BC-const — fixed before
run 2; run-1 failure was script-only, code never impugned).

Verdict: PASS. Code CORRECT; GATE 1 method note (flagged).
Logs: NVME ws tmp/encode-viewer/r45/ (*351* set:
build351, pyid351, rgram351py/c, cmp351.py/.c, for351-*,
pins351.basen, smoke351, tables351.py/.log, banddiff351(-c),
added351(-all), numstat351, populate351, ownloop351.py/.log).
