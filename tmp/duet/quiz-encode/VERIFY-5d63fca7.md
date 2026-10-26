# VERIFY-5d63fca7 b344 T10P236 pins 98865..99212 (1404 tiers) PASS

Seat viewer-r44, first-hand, detached tree-5d63fca7 @5d63fca7,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r44.
Base 6242a462 (b343, 1398 tiers). Band = b4e3657b (py) + 5d63fca7 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build344/bin, rc=0, 0 warnings. SHA-256 first8
  rgramc b077a09a / aae d6e27c97 (== GATE; aae.c untouched).
- RGRAMC-PYID 6874/6874 covered=6874/6874 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13748/13748 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 13748/13748 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 13750 rows (2 hdr + 13748, +62 vs base); PINS cells
  6874 vs for-list 6874 exact match both ways (sorted, diff 0;
  numeric-token parse, no `;` pollution). For-list 6843->6874
  +31/-0 verbatim == GATE's 31 (98865 98866 98867 98868 98874
  98882 98883 98884 98885 98886 98889 98891 98892 98893 98900
  98908 98909 98924 98925 98940 98941 98943 98944 98945 98956
  98957 99071 99072 99199 99200 99212). 31x2=62=13748-13686.
- SMOKE-GREEN rc=0 (6/6 PASS, default backend).
- Tables audit P236 C-vs-py, own script tables344.py, 57/57
  ALL-EXACT: S0/S1 (83470100 NEW/45f45702 NEW, len 168,
  b4b5 6304/6504 == lencode), AM 16/16 distinct 6B, CM 10/10
  distinct 18B 2-sig map a826a902 x3 + 54935401 x7 exact
  order, M 16/16 distinct 7B, QR 4/4 TRIPLE r1==r2==r3
  d1dec3de4951 + r0 0dc9f25f207c, QT 4/4 exact
  bec350e6/4906c3ab/7306c3ab/9d06c3ab + 06c3ab share, RM
  16/16 (9B) / RQ 16/16 (6B) UNPAIRED, AC 76/76, CC 64/64,
  QC 65/65, RC 71/71; _N decls 76/64/65/71. Varsets exact:
  AC 8, CC 20, QC 19, RC 17 (A-549 VPOS + b5-excl on A/C).
  Coverage 76+8/64+20/65+19/71+17 exact, 0 overlap,
  b4/b5 in no const set. Sig consts AC 5c447f25, CC b0-3
  in-tab, QC f4344915, RC 01000000. RC b84-87 09/a5/a2/f2.
  M-tails NEW vs P235M; QT overlap 0/4 vs P235T. Ring
  tails SPLIT 16/16 both. A/C b5 const 04, Q carry
  ff04->0105 @98943->98944, ring edges off114/115 +
  off242/243 (0x1b/0x05 base). No M42/X42/BM/BC/PT/PC/
  FM/FC; inventory exactly 13 + 4 _N, novel-clean both.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  98865, S1 98866, A 98867-82, C 98883-92, Q 98893-956
  m=off&15 q=off>>4, R 98957-99212 c=off&15 r=off>>4);
  C T-mirrors 6/6 exact (T65003/008/013/028/045/068);
  guards exact; ring consts 27/115/243 (27=0x1b); b42
  0x06 via QC consts, no b42 leg; byte-index lists match;
  insert after T10P235R close at dispatch tail, N-out-of-
  scope fallthrough follows both sides.
- Edges 99071/99072 + 99199/99200 + carry pair 98943/98944
  + tail 99212 PASS 2/2 both legs. Odd-lencode whole-tier
  via own-loop 348/348. Matches A-549 (33/33 = 15/15 shape
  + 10/10 quad/ring + 8/8 counters, file read, counts
  verified) + A-306 (3/3 legs; PB0/PB1/PBA NEW, C10 map
  exact, quad triple/tails exact, ring STANDARD inverted
  explicit, consts 77/65/65/71 INCL with standing -1 x2
  excl on PBA/C10, NO D dips).
- C diff purely additive: numstat 610/0 rgramc.c, 237/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  910). C 605 content + 5 bare-`+` / 0 del; fine-norm by
  GATE's stated method (_tN/_iN/_bN, BSD tools, empty-
  excluding) del-uniq 0, missing 0, add-uniq 438 (GATE
  says 437 — see slip S1; purely-additive verdict holds
  under every normalization tried).
- Wall on 910 added lines: vendor/disasm 0, depload 0,
  libcompression/CT-shim/shebang/aa/nominated 0.
- Tiers: merge-msg +6, code 6 blocks, guards singletons
  504->506 +2 / ranges 396->400 +4 = +6, CLOSED prints
  1552->1558 +6, seal 1398->1404 +6: all agree.
- CONFIRM evidence (CONVERT-01 rule b): A-549 CONFIRM
  33/33; A-306 corroborates. Agrees with cport msg (py/C
  13748, PYID 6874).
- Own-loop 348/348 (98865..99212, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b344. Newest
  PARENT-* is QNUM-12 (GATE says QNUM-09 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

1 GATE COUNT SLIP (sweep2-r48; code PASS): (S1) fine-norm
"add-uniq 437" vs first-hand 438 under the stated method
(BSD grep/sed/sort -u, empty-excluding; reproduced 438 also
case-fold + LC_ALL=C; full-number norm gives 171, symbol
norm ~426-435 — 437 matches no reasonable reading). Del-uniq
0 + missing 0 agree; purely-additive verdict unaffected.

Verdict: PASS. Code CORRECT; GATE prose 1 count slip (flagged).
Logs: NVME ws tmp/encode-viewer/r44/ (*344* set:
build344, pyid344, rgram344py/c, cmp344.py/.c, for344-*,
pins344.basen, smoke344, tables344.py/.log, banddiff344(-c),
added344, numstat344, caddnorm344, cdelnorm344, populate344,
ownloop344.py/.log).
