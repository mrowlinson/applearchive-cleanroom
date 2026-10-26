# VERIFY-0b7920eb b359 T10P251 pins 104085..104432 (1494 tiers) PASS

Seat viewer-r47, first-hand, detached tree-0b7920eb @0b7920eb,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r47.
Base 00142e87 (b358, 1488 tiers). Band = 7226d19c (py) + 0b7920eb (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build359/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 98a09d55 / aae 7d8dd3a2 +
  sha256 a16d347d / d6e27c97 (== GATE both; aae.c untouched).
- RGRAMC-PYID 7339/7339 covered=7339/7339 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14678/14678 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14678/14678 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14678/14678, sorted).
- PINS 14680 rows (2 hdr + 14678, +62 vs base 14618); PINS
  base-N 7339 vs for-list 7339 exact both ways (0/0; tail
  104432 pinned AND in for-list). For-list 7308->7339 +31/-0
  verbatim == GATE's 31: sing 104085 104086; A 6 (104087
  head + 104088 + 104094 + 104098 + 104101 + 104102 tail);
  B 6 (104103 head + 104104 + 104107 + 104109 + 104111 +
  104112 tail; offs 2,3,5,7 = 104105,104106,104108,104110
  unsampled); Q 10 step-8 (104113 head + 104121 + 104129 +
  104137 + 104145 + 104153 + 104161 + 104169 + 104175 +
  104176 tail; NO carry pair, b5 const); R 7 (104177 head +
  edge pairs 104191/104192 + 104319/104320 + mid 104305 +
  104432 tail). 31x2=62=14678-14616. PINS adds == for-list
  adds x2.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR, default backend).
- Tables audit P251 C-vs-py, own script tables359.py, 94/94
  ALL-EXACT (15-table A-PBA/B10-1SIG/QUAD-b42xor+T88, NO
  CM/CC): S0/S1 (90fc0200 ==P250PB0 REPEAT @104085 b4b5
  2b/2d / 5d16fd05 NEW @104086 b4b5 2d/2d, both NEW strings,
  len 168 == lencode); AM 16/16 distinct 7B; BM 10/10
  distinct 11B diverge (single-sig rows); M 16/16 distinct
  7B; M42 16/16 1B 4-valued {d6x6,96x4,56x3,16x3}
  low-nibble const 6; X42 [00,06,06,06] EXACT; b42xor
  staged both sides (py + C snprintf/%02lx vs M42); ADD-tie
  A=[0,fa,fa,fa] verified algebraically 64/64 (all 16 M42
  x all 4 q: XOR==ADD mod 256, low-3-bits==6 throughout —
  tie STANDS, XOR staged per precedent); QR 4/4 TRIPLE
  r1==r2==r3 865bd276b11b + r0 dc5dc1973145; QT 4/4 exact
  50155041/7e8da7ed/a88da7ed/d28da7ed (r1/r2/r3 share
  last-3B 8da7ed); RQ==M tail-slice b76-79 same-index 16/16,
  full-string 0/16 (P243-style, RQ 8B vs M 7B layouts);
  M-tails 16/16 NEW vs P250M, RM 16/16 NEW vs P250RM, QT 4/4
  NEW vs P250QT (0 shared each); RM 16/16 (7B) / RQ 16/16
  (8B) UNPAIRED 0-overlap, tails SPLIT 16/16 both; AC 75/75,
  BC 71/71, QC 64/64, RC 71/71; _N decls 75/71/64/71.
  Varsets exact: AC 9 (b4/b5+M7 b36-38,76-79), BC 13
  (b4/b5+M11 b36-42,80-83, b42 IN range), QC 20 (b4/b5+QM7
  b34,35,43,76-79+b42 xor-leg+R6 b36-41+T4 b80-83), RC 17
  (b4/b5+TM7 b52-54,80-83+TR8 b38,39,46,47,76-79). Coverage
  75+9/71+13/64+20/71+17 exact, 0 overlap, b4/b5 in no
  const set. AC sig 00882f46 NEW (P250Q 00882f26 1B-off
  adjacent); BC sig 5d16fd05 == PB1; QC sig 00882f46 == PBA;
  RC sig 05000000 == P249T; b42: AC const 0x2f, BC in m-tab,
  QC xor-leg (42 NOT in consts), RC const 0x7e; RC b84-87
  d3/11/a2/7a. A b5 const 2d (2f2d..4d2d); B b5 const 2d
  (4f2d..612d); Q b5 const 2d NO carry (632d..e12d); ring
  head e3/2d, edges off14/15 + off142/143 exact, mid off128
  e3/2e, tail off255 e1/2f; counter==lencode 256/256. No
  CM/CC/M19/XA19/PT/PC/FM/FC/FS/FO/RF/M8/X8/QB; inventory
  exactly 15 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  104085, S1 104086, A 104087-102, B 104103-112, Q 104113-176
  m=off&15 q=off>>4, R 104177-432 c=off&15 r=off>>4);
  C T-mirrors 6/6 exact bodies (T68797/68802/68807/68822/
  68838/68863); ordered pay-index sequences C==py per range
  block (A n=9, B n=13, Q n=20, R n=17); ring consts
  0xe3/0x2d + (off>=15)+(off>=143) == py; temps _t5316..5335
  / _i3248..3257 / _b3247..3256 appended (base b358 max
  _t5315/_i3246/_b3245 first-hand via git show, no reuse;
  _i3247 skipped); insert at dispatch tail after T10P250R
  close, N-out-of-scope follows both sides.
- Edges head 104085 + 104191/104192 + mid 104305 + 104319/
  104320 + tail 104432 PASS 2/2 cells both legs (7 cells).
  Odd-lencode whole-tier via own-loop 348/348. Matches
  A-599 (37/37 = 12/12 shape + 14/14 quad/ring + 11/11
  counters, file read, counts verified; tie 64/64 + 64/64
  first-hand) + A-362 (3/3 legs CONFIRM incl tie-stands).
  Code-consts vs memo INCL (PBA 76 / B10 72 / quad 65 /
  T88 71): impl 75/71/64 = memo-1 on PBA/B10/quad, T88 71
  identical (A-599 §3 explicitly no-finding).
- C diff purely additive: numstat 640/0 rgramc.c, 260/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 963). C 635 content + 5 bare-`+` / 0 del (all 5 bare
  in rgramc.c). Fine-norm: del-uniq 0, add-uniq 168 EXACT
  under GATE's stated recipe (full-number strip +
  trailing-';' strip, keep-empty; excl-empty would be 167)
  — sweep-r51 strip+keep family (see standing drift note).
- Wall on 963 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shim/ct-cache
  0, shebang 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1394->1400 +6, singletons `if n == ` 534->536 +2,
  range-guards `<= n <=` 456->460 +4, CLOSED prints
  1394->1400 +6, C singletons 529->531 +2 + C ranges
  456->460 +4 (5-offset pre-existing, unchanged), seal
  1488->1494 +6: all agree (GATE literals reproduced
  exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-599 CONFIRM 37/37
  (backfill 4/4 complete, own 376-cell bed, BAD=0) +
  A-362 corroborates 3/3. No CONFIRM-P251.md file; A-files
  suffice per rule. Agrees with cport msg (py/C 14678,
  PYID 7339).
- Own-loop 348/348 (104085..104432, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b359. Newest
  PARENT-* is QNUM-13 (GATE says QNUM-12 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing (all
  hex/counts from run output).

Verdict: PASS. Code CORRECT; GATE 1 immaterial staleness (QNUM-12 vs -13).
