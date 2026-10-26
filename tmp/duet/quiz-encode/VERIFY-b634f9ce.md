# VERIFY b634f9ce b333 T10P225 pins 95037..95384 (1334 tiers) PASS

Seat viewer-r41, first-hand, fresh detached worktree tree-b634f9ce
(HEAD b634f9ce, clean), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r41. Base 9a6da30d (b332 tip, own VERIFY filed
this round). CT shim on all batteries (fast tests throughout).

- Build: make BUILDDIR=r41/build333/bin, rc=0, 0 warnings. aae
  sha1-8 7d8dd3a2 (== GATE) / sha256-8 d6e27c97; rgramc sha1-8
  d5cf79d0 (== GATE) / sha256-8 005dddb7 (first-hand).
- RGRAMC-PYID 6550/6550 covered=6550/6550 GREEN rc=0 (own binary).
- RGRAM py 13100 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 13100 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (13100/13100, diff 0).
- PINS 13102 rows (2 hdr + 13100, +52 vs base 13050).
  Base-N set vs for-list set-eq 6550/6550 (diff -q clean).
- For-list union +26, 0 removed (old 6524 -> new 6550):
  95037 95038 95039 95054 95055 95056 95057 95058 95059 95064
  95065 95080 95081 95096 95097 95103 95104 95112 95113 95128
  95129 95231 95232 95359 95360 95384 (== GATE list verbatim).
- SMOKE-GREEN rc=0 (6/6, default oracle backend).
- Tables audit P225 C-vs-py, own script tables333.py rc=0 ALL-EXACT
  (19-table FRAG layout): S0/S1 len 168/168 eq, sigs 3f240000/
  fe044e00, b4b5 7be6/7de6 == lencode first-hand; AM16 FM0-2
  FM3-6 M16 QR4 QT4 RM16 RQ16 all eq; FS 10/10 + FO 10/10
  (py-hex vs C-dec); AC75 FC0-78 FC1-82 FC2-82 FC3-70 QC63 RC67
  all eq; _N decls 75/78/82/82/70/63/67 match; sigs fe048604/
  fe044e00/fe043e00/fe042e00/fe043600/ec4f6003/dafe0436;
  varsets exact x7 (AC-9, FC0-6, FC1-2, FC2-2, FC3-14, QC-21,
  RC-17); cover84 x7 0-overlap; b4/b5 in no const table x7;
  head-b5 e6 x67 (95037..95103) + e7 x25 (95104..95128) via
  lencode formula first-hand; FM0 pair 62f7924c/aa7b3f50
  distinct; FM3 6/6 distinct w=12; M 16/16; QR r2==r3 PAIRED
  5059f9fbb271c537a9 x2, 3/4 distinct (r0 d03979c06db1743f03,
  r1 d079796ce171905756); QT verbatim 9129bc09/682b13ce/
  e6315da9/15325da9, 4/4 distinct, r2/r3 share 5da9; RM/RQ
  16/16 UNPAIRED distinct; R9 == F36M+b45 positional set-exact;
  RM225-vs-RM224 shared 0/16 + QT225-vs-QT224 shared 0/4
  (M-tails ALL NEW first-hand); no BM/BC either side; no
  PT/PC/CM/CC/H/TC syms either side; no extra P225 syms py/c.
- Dispatch eye-verified both sides, 6 blocks in order at dispatch
  tail after T10P224R close (N-out-of-scope fallthrough follows):
  S0 n=95037 PB0 3f240000 NEW, S1 n=95038 PB1 fe044e00 ==P224B10,
  A 95039-95054 PBA16 fe048604 ==P224Q (m-tab b48-50,76-79),
  F 95055-95064 FRAG UNEVEN 4-sig (sigtag pay[2]==FS[off] +
  k=FO[off]: 0x4E->FM0 4B b80-83+FC0; 0x3E->FC1; 0x2E->FC2;
  0x36->FM3 12B b23,35,46-51,80-83+FC3), Q 95065-95128 QUAD
  ec4f6003 r2==r3 (m=off&15 M6 b6,7,76-79, q=off>>4 R9
  b23,35,45-51 + tails b80-83), R 95129-95384 T-ring dafe0436
  STANDARD (c=off&15 M9 b13-17,76-79, r=off>>4 R6 b6,7,72-75,
  b4=(0x33+2off)&FF b5=0xe7+(off>=103)+(off>=231)); A/F/Q raw
  lencode. C T-mirrors 6/6: T62145/150/155/170/207/230, py
  lines + bounds + comments exact; C guards/offs exact; F
  elif-chain as nested else-if, tags 78/62/46/54 exact; C
  R-counter ((51+2*off)&255, (231+(off>=103))+(off>=231))
  exact mirror; C FM3 byte-index list matches py.
- Edges recomputed first-hand from code formulas (all edge pins
  PASS): Q carry 95103 (off38, ff/e6) -> 95104 (off39, 01/e7);
  ring 95231 (off102, ff/e7) -> 95232 (off103, 01/e8); 95359
  (off230, ff/e8) -> 95360 (off231, 01/e9). (== GATE.)
  F-zone @off2/@off3 comment text read first-hand: singleton
  offsets, not carry labels (== GATE note).
- C diff pure-add: numstat 909/0 + 311/0 + 1/1 + 52/0 (== GATE);
  raw 909 add / 0 del; band added 1273 (== GATE); 5 blank-plus
  / 0 blank-minus. Norm ([0-9]+->N, cut-c2-strip variants all
  agree): add-uniq 197, del-uniq 0, miss 0 (== GATE exactly).
  sh 1/1 = for-list line rewrite (+26/0rem verified above).
- Wall on band added lines (1273): vendor/disasm/depload(7)/
  libcompression/CT-cache/CT_REAL/compression_tool/shebang/^+#!
  /usr/bin/aa/nominat 0 hits throughout (13 patterns).
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards +6
  (own combined count 830->836; GATE stated-method 798->804;
  delta +6 agrees; GATE continuity 792+6+6=804 consistent),
  seal 1328->1334 +6 (commit msgs): all agree.
- Band comp: 1da14576 (py merge w2b@9bf285ad partial, +6 tiers,
  +52 pins) + b634f9ce (C port). Matches GATE.
- CONFIRM: A-503-q617-t10p225 CONFIRM 29/29 (15/15 shape + 10/10
  quad/ring + 4/4 counters, own bed, read in full). Citation
  "A-503-q617" CORRECT (file A-503-q617-t10p225-geometry.md;
  matches r40 corrected mapping). No CONFIRM-P225.md file;
  rule-b satisfied. A-295 recon: sigs + FRAG exact map + VPOS
  sets + M6/R9 paired 3/4 + R9==F36M+b45 + tails verbatim +
  M-tails 16/16 NEW + T-ring STANDARD UNPAIRED + lencode 348/348
  + ring formulas/edges + consts 76/71/63/67 (in-table + b5-const
  A/F36) + NO D dips: all consistent first-hand. DISSENTs on
  file only P923/P924/P926 (other turf, == GATE).
- Own-loop ownloop333b.py (cache-path-direct, zero-write):
  348/348 ok, 0 bad, rc=0. (322 non-pin Ns fetched via the
  tool-identical -encode -a lzraven invocation; 26 pins
  pre-cached. No truncated entries seen. NOTE: sed-adapted
  script initially pointed TREE at b332 tree; caught + fixed
  before running — verified TREE line + range pre-run.)
- Quiz: no conflicting CLAIM/GATE/FLAG on b333. Newest PARENT-*
  QNUM-12 (writer Q-blocks only, read, no gate impact).

Verdict: PASS. GATE CORRECT, 0 slips (prose + code).
Logs: NVME ws tmp/encode-viewer/r41/ (tree-b634f9ce detached;
build333.log, pyid333.log, rgram333py/c.log, pass333py/c.txt,
for333-old/new.nums, pins333-base.nums, smoke333.log, tables333.py/
.log, cadd333.txt, added333.txt, numstat333.txt, ownloop333b.py/
.log, populate333.py/.log, ownloop-work333/, smoke333work/,
scratch333py/c/, pyid333work/).
