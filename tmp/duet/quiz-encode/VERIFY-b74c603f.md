# VERIFY-b74c603f b346 T10P238 pins 99561..99908 (1416 tiers) PASS

Seat viewer-r44, first-hand, detached tree-b74c603f @b74c603f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r44.
Base fa5e0143 (b345, 1410 tiers). Band = cb665c1c (py) + b74c603f (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build346/bin, rc=0, 0 warnings. SHA-256 first8
  rgramc f3867663 / aae d6e27c97 (== GATE; aae.c untouched).
- RGRAMC-PYID 6936/6936 covered=6936/6936 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13872/13872 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 13872/13872 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 13874 rows (2 hdr + 13872, +62 vs base); PINS cells
  6936 vs for-list 6936 exact match both ways (sorted, diff 0;
  numeric-token parse, no `;` pollution). For-list 6905->6936
  +31/-0 verbatim == GATE's 31 (99561 99562 99563 99564 99570
  99578 99579 99580 99581 99582 99583 99584 99588 99589 99596
  99604 99605 99612 99620 99621 99628 99636 99637 99644 99652
  99653 99711 99712 99839 99840 99908): S0/S1 (2) + A (4) +
  C incl carry-pair 99583/99584 (7) + Q (12) + ring head/
  edge-pairs/tail (6). 31x2=62=13872-13810.
- SMOKE-GREEN rc=0 (6/6 PASS, default backend).
- Tables audit P238 C-vs-py, own script tables346.py, 57/57
  ALL-EXACT: S0/S1 (93540100 REPEAT/ad52a702 ==P237C10, len
  168, b4b5 d309/d509 == lencode), AM 16/16 distinct 8B, CM
  10/10 distinct 22B 2-sig map a702 x3 + 5701 x7 exact
  order, M 16/16 distinct 8B, QR 4/4 TRIPLE r1==r2==r3
  5412f085bfb30a9d + r0 cc2e70849f53448a + b42 split
  {84,85} row-split verified, QT 4/4 exact 53b7258b/
  ee3c65bc/183d65bc/e2b560fd + A-557 §F CONFIRMED (r1/r2
  share 2B 65bc, byte1 3c vs 3d differ), RM 16/16 (6B) /
  RQ 16/16 (8B) UNPAIRED, AC 74/74, CC 60/60, QC 62/62, RC
  72/72; _N decls 74/60/62/72. Varsets exact: AC 10, CC 24
  (b22 skipped confirmed absent from varset AND present in
  consts), QC 22, RC 16 (A-557 VPOS + b5-excl on A/Q).
  Coverage 74+10/60+24/62+22/72+16 exact, 0 overlap,
  b4/b5 in no const set. Sig consts AC 609bd720, CC (0,ad),
  (1,52) + b2,3 tab, QC ad524715, RC 01000000. RC b84-87
  85/f3/26/59. M-tails NEW vs P237T; QT overlap 0/4 vs
  P237T. Ring tails SPLIT 16/16 both. A b5 const 09, C
  carry ff09->010a @99583->99584, Q b5 const 0a; ring
  edges off58/59 + off186/187 (0x8b/0x0a base). No M42/X42/
  BM/BC/PT/PC/FM/FC; inventory exactly 13 + 4 _N,
  novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  99561, S1 99562, A 99563-78, C 99579-88, Q 99589-652
  m=off&15 q=off>>4, R 99653-908 c=off&15 r=off>>4); C
  T-mirrors 6/6 exact (T65476/481/486/501/519/542); guards
  exact; C m-tab 22B b2,3,20,21,23-27,34,35,41-47,80-83
  b22-skipped verified byte-for-byte both sides; Q byte
  lists M8 b48-51,76-79 + R8 b34,35,41-46 match; ring
  consts 139/59/187 (139=0x8b); ring byte lists M6
  b6,7,80-83 / R8 b52-55,76-79 match; insert after T10P237R
  close at dispatch tail, N-out-of-scope follows both.
- Edges 99711/99712 + 99839/99840 + C carry 99583/99584 +
  tail 99908 PASS 2/2 both legs. Odd-lencode whole-tier via
  own-loop 348/348. Matches A-557 (34/35 + §F finding =
  16/16 shape + 10/11 quad/ring + 8/8 counters, file read,
  counts verified; §F tail-share figure confirmed
  first-hand, descriptive only, cut SAFE, no DISSENT) +
  A-308 (3/3 legs; REPEAT/sig-geometry, C10 map exact,
  quad triple/tails exact, ring SPLIT explicit, consts
  75/60/63/72 INCL with standing -1 x2 excl on PBA/quad,
  NO D dips). NOTE: A-308's "r1/r2 share last 3B 3c65bc"
  is the off-by-1B A-557 §F corrects (true share 2B 65bc)
  — memo-side, already adjudicated, not a code/GATE issue.
- C diff purely additive: numstat 610/0 rgramc.c, 237/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  910). C 605 content + 5 bare-`+` / 0 del; fine-norm by
  GATE's stated method (_tN/_iN/_bN, BSD tools, empty-
  excluding) del-uniq 0, missing 0, add-uniq 391 (GATE
  says 390 — see slip S1; purely-additive verdict holds).
- Wall on 910 added lines: vendor/disasm 0, depload 0,
  libcompression/CT-shim/shebang/aa/nominated 0.
- Tiers: merge-msg +6, code 6 blocks, guards singletons
  508->510 +2 / ranges 404->408 +4 = +6, CLOSED prints
  1833->1839 +6, seal 1410->1416 +6: all agree.
- CONFIRM evidence (CONVERT-01 rule b): A-557 CONFIRM 34/35
  + §F descriptive finding (cut SAFE, no DISSENT); A-308
  corroborates. Agrees with cport msg (py/C 13872, PYID
  6936).
- Own-loop 348/348 (99561..99908, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b346. Newest
  PARENT-* is QNUM-12 (GATE says QNUM-09 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

1 GATE COUNT SLIP (sweep2-r48; code PASS): (S1) fine-norm
"add-uniq 390" vs first-hand 391 under the stated method
(same systematic 1-off as b344's 438-vs-437, same seat, same
direction — suggests their opaque "TNP" step or counter, not
random; del-uniq 0 + missing 0 agree both bands).
Purely-additive verdict unaffected.

Verdict: PASS. Code CORRECT; GATE prose 1 count slip (flagged).
Logs: NVME ws tmp/encode-viewer/r44/ (*346* set:
build346, pyid346, rgram346py/c, cmp346.py/.c, for346-*,
pins346.basen, smoke346, tables346.py/.log, banddiff346(-c),
added346, numstat346, caddnorm346, populate346,
ownloop346.py/.log).
