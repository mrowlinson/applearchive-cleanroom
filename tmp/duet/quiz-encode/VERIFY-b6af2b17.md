# VERIFY-b6af2b17 b430 T10P322 pins 128793..129140 (1920 tiers) PASS

Seat viewer-r65, first-hand, tree @b6af2b17,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r65.
Base aaaaa11f (b429 tip, 1914 tiers sealed; this seat's
VERIFY-aaaaa11f PASS-filed same round, base-use only,
respected). Band = e5d6a3b5 (py merge w2b@f5cfd527
partial, +6 tiers, +62 pins) + b6af2b17 (C port, 1920
sealed). Trees manifest-identical to tips (git ls-tree
vs git ls-files cmp clean, 117/117 both; WT detached
at band, will return to lanes/encode-viewer at round
end).

Banked Next-P322 shape (r65 from A-831) CONSUMED FIRST
and corroborated below: PB0 77435801 pay84 sig-eq-
P321PB0 (47/84 diff) @128793 / PB1 02000000 pay88
sig-eq-P321PB1 (76/88) @128794 / PBA88 29000000 x16
@128795-810 (SAME-sig-as-P321Q-r01) / C10-region
02000000 pay88 x10 @128811-820 -- all exact.

- Build: make -C src/c BUILDDIR=build430 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc dd0262c8273ad46f
  69f9af5ef609410c88fae99d1c3b41ccee80428d8b2ef1dc
  (== GATE; aae sha256 d6e27c97 pinned, band touches
  no aae sources per numstat).
- RGRAMC-PYID 9563/9563 covered=9563/9563 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary
  exported before the run, CT_CACHE_DIR set, NVME
  workdir).
- RGRAM py 19126/19126 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19126/19126 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 19126/19126;
  cmp430.py; GATE claims sorted only, raw corroborated
  too).
- PINS 19128 rows (2 hdr + 19126, +62 vs base 19066);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq, seteq430.py). For-list
  union delta vs base +31/-0 (9532->9563):
  128793 128794 128795 128796 128802 128803 128809
  128810 128811 128812 128815 128816 128819 128820
  128821 128828 128837 128844 128853 128860 128869
  128876 128883 128884 128885 128895 128896 128950
  129023 129024 129140
  (== GATE sampled list EXACT). Decomposition first-hand
  from the added set: 2 sing (128793/94) + A head/mid/
  tail pairs (6: 95/96 + 02/03 + 09/10; offs 0,1,7,8,
  14,15) + C head/mid/tail pairs (6: 11/12 + 15/16 +
  19/20; offs 0,1,4,5,8,9; no unsampled C offs --
  C10 b5-const full block, first-hand) + Q head 21/
  off0 + 7 mids 28/37/44/53/60/69/76 + tail pair 83/84
  (10: offs 0,7,16,23,32,39,48,55,62,63; NO step,
  quad b5 const ee, NO edge, first-hand) + R head 85/
  edge-pairs 95/96 + 023/024/mid 50/tail 140 (7: offs
  0,10/11,65,138/139,255). 31x2=62 rows, range
  128793..129140 exact. PINS-new-N == for-added 31/31,
  PINS removed 0 (numstat 62/0 clean append, all in
  py-merge leg; all 19126 rows test_rgram_fast.py-
  tagged; cols1-4 purity +62/-0 first-hand).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle
  backend, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit430.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 146 PASS
  0 FAIL first run, no script fixes needed.
  Inventory exactly the 12 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F anywhere -- 0 hits
  both sources; no F0/F1, no QT (quad tails live in
  R11) + no RT (STANDARD tails) + no F (no frags)).
  S0 168ch sig 77435801 sig-eq-P321PB0 (47/84 payload
  diff vs P321S0 @ b4,5,32-35,37-40,42,43,45-79
  first-hand, NOT byte-equal) / S1 176ch sig 02000000
  sig-eq-P321PB1 (76/88 payload diff vs P321S1 @
  b4-14,16-25,28-31,36-43,45-87, NOT byte-equal;
  29/88 diff vs own C10[0] assembled, NOT byte-equal;
  sig SAME-as-own-C10; differs vs own PB0), staged as
  full-payload singletons.
  AM 16/16 14ch distinct, CM 10/10 6ch distinct,
  M 16/16 16ch distinct, QR 4/4 22ch distinct, RM 16/16
  16ch distinct, RQ 16/16 16ch distinct UNPAIRED, no QT
  + no RT (STANDARD tails) + no F (no frags this tier).
  AC 79, b0-3 29000000 (b0 const 29), no b4/b5.
  C10-1SIG-88-M3 sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 6ch first-hand:
  d269b8/f269b8/126ab8/326ab8/526ab8/b86ab8/38b8d4/
  58b8d4/78b8d4/98b8d4; CC b87 const 9f (first-hand),
  CC has no b4/b5, b5 const ee full block via lencode).
  S1-vs-own-C10 staged per-cell (M3 b84-86, b87 const,
  b4/b5 lencode, each cell own assembly) [29]x10
  TRUE-UNIFORM count+position (cell0 29 @
  4,8-11,16-31,60-63,84-87 EXACT; positions identical
  all 10 staged AND oracle; sig 02000000 both, NOT
  byte-equal -- 17th TRUE-uniform case on record, 16th
  excluding unverified P299; beyond-GATE values
  corroborated by oracle leg below).
  QUAD88-1SIG-4R 1-sig 29000000 x64 SAME-sig-as-PBA
  (QC b0 const 29, b0 NOT in tab; b5 const ee full 64,
  NO step, 0 ff; b4 base 0x6b step2 64/64 range 6b..e9
  NO edge; QM8 b28-31,80-83 16/16 distinct NO frags +
  R11 b20-26,84-87 rows 4/4 NO pairing
  pairwise-disjoint: r0/r1 share 7B prefix
  39da13aa3398e6, differ in first tail byte b84
  (b8 vs d8); r2/r3 fully distinct;
  tails b84-87 4/4 distinct b8b8d49f/d8b8d49f/
  e23a1c36/d3ec8ee1, r01 TRUE-3B b8d49f, r2/r3-lcs0
  vs all, r0r1-lcs3, all other pairs lcs0;
  M-tails 16/16 ALL NEW vs P321T (zero overlap vs P321M
  AND vs P321RM-tail8 AND vs P321RQ-tail8).
  Ring STANDARD: sig 5e020000 x256; TM8 b19,27,34,35,
  80-83 by COL RM 16/16 + TR8 b28-31,76-79 by ROW RQ
  16/16 UNPAIRED (tails SPLIT b80-83 col / b76-79 row);
  b0 const 5e b1 const 02; b84-87 2b3b1c36 ring-wide
  NEW (P321 STANDARD-split era per Q-914: P321T b80-83
  COL-led via RM).
  M==RQ FULL8: M 8B vs RQ 8B agree (0,0)..(7,7) 16/16
  each; tabs string-identical ordered AND as sets;
  off-pattern maxagree 1 (essentially no off-pattern);
  QM8 byte positions b28-31,80-83 (COL, Q region, m =
  off & 15) vs TR8 positions b28-31,76-79 (ROW, R
  region, r = off >> 4): b28-31 shared positions,
  tails SPLIT. Even band: no ordinal (viewer convention;
  even running pattern b414-full/b416-tail/b418-full/
  b420-strdiff/b422-strdiff/b424-tail-pos-differ/
  b426-full/b428-string-split/b430-string-split).
  Sorted-unique + _N decls 79/83/67/70 match actual.
  Missing-sets EXACT: AC-9 [4,5,20,21,22,80-83] =
  b4,b5+M7 / CC-5 [4,5,84,85,86] = b4,b5+M3 (b87 const
  9f, NOT missing -- first-hand) / QC-21 [4,5,20-26,
  28-31,80-87] = b4,b5+QM8+R11 (b0 const, NOT missing)
  / RC-18 [4,5,19,27,28-31,34,35,76-83] = b4,b5+TM8+
  TR8. VPOS 8/4/20/18 == A-832 EXACT (PBA b4+M7 / C10
  b4+M3 (b84-86) / quad b4+QM8+R11 (b5-const excluded)
  / T b4,b5+TM8+TR8). Coverage unions exact every
  block (const U tab U {b4,b5} == 88 x4, 0 overlap);
  each missing == region pay-index set (A/C/Q/R region
  text re-derived first-hand, tab == region-idx minus
  {b4,b5} EXACT all 4).
  Q legs M[m] + QR[q] both sides, NO F-legs in Q;
  R legs RM[c] + RQ[r] both sides, NO F-legs in R
  (STANDARD RM-col / RQ-row verified in region text
  both sides). RM 16/16 distinct + RQ 16/16 distinct,
  sets disjoint.
  P321 refs re-read: S0 77435801 / S1 02000000 /
  PBA 3d000000 / C10 02000000 / QUAD 2SIG 29/25.
  PBA sig 29 NEW vs P321 3d (29000000 != 3d000000);
  QUAD 1SIG 29 SAME-as-PBA vs P321 2SIG 29/25 (rows
  NEW, single-sig structure continues; R11 replaces
  R29 class). AM/CM/M/QR/RM/RQ 0-overlap vs P321.
  Memo INCL PBA 80 / C10 84 / quad 68 / T88 70
  (A-832 re-read): impl 79/83/67/70 = writer-1 on
  PBA/C10/quad: impl tables still deduct const-b5
  (b5 covered by lencode instead) while Q-914 sheet
  counts b5 (memo A-832 confirms the sheet) -- S-F
  arithmetic persists though the sheet is FIXED;
  geometry exact, PORT verdict stands; memo-exact on
  T88 (b5 varies, no deduction). 25th consecutive
  tables-lag band (b430 pattern +1/+1/+1/+0: PBA/C10/
  quad lag; running b412-b429 per GATE + r64/r65
  records).
  Base temp maxes _t6600/_b3993/_i3994 (no reuse:
  band adds _t6601-6616 continuous-16 + _b3995/97/99/
  4000/02/03 + _i3996/98/4001/04, all above base
  maxes).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 128793 / S1 128794 / A 128795-810 / C 128811-820 /
  Q 128821-884 / R 128885-129140): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C/Q both sides
  (b5 const ee emerges from raw lencode, NO step, NO
  edge, range 6b..e9; Q STEP none) + R explicit counter
  (b4=(0xeb+2off)&FF b5=0xee+(off>=11)+(off>=139); py
  hex 0xeb/0xee; C staged literals 235/238, re-derived:
  235==0xeb, 238==0xee; Q uses raw lencode, no counter
  literals) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A M7 b20-22,
  80-83; C M3 b84-86 + b87 const 9f; Q QM8 b28-31,
  80-83 + R11 b20-26,84-87; R TM8 b19,27,34,35,80-83
  by COL + TR8 b28-31,76-79 by ROW, tails SPLIT) + C
  guards `if ((n) == (128793))` / `(128794)` + 4 range
  guards exact + counter literals exact + C byte-index
  lists match py per block. C blocks carry T86495/
  86500/86505/86520/86535/86556 py-line mirrors
  (T86495/T86500 spot-verified verbatim against py
  lines 86495/86500); bounds + byte positions exact
  (A 14ch, C 6ch, Q 16/22ch, R 16/16ch).
  Insert exact both sides: after T10P321R close (py
  CLOSED-then-guard; C block 230225 follows P321R
  close), at dispatch tail (N-out-of-scope fallthrough
  follows). Matches A-832 geometry (values re-checked
  in audit above; NO D dips: ownloop tags exactly the
  6 P322 blocks).
- Edges own-loop ownloop430.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (302 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P322R N=129140
  off=255. edges430.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 33/ee, 35/ee
  == raw lencode) + aform 16/16 (A head 37/ee tail
  55/ee b5set {ee} NO step, 0 ff) + cform 10/10 (C
  head 57/ee tail 69/ee b5set {ee} NO step, 0 ff) +
  qform 64/64 + qb5const 64/64 (Q head 6b/ee tail
  e9/ee b5set {ee} NO step, NO edge, range 6b..e9,
  0 ff in 64) + ring counter 256/256 + ringraw 256/256
  (head eb/ee; 128895 off10 ff/ee -> 128896 off11
  01/ef; 129023 off138 ff/ef -> 129024 off139 01/f0;
  tail off255 e9/f0; exactly 2 ff in 256); ff total x2
  (both R, no Q ff); ff-in-Q 0. odd-lencode 92+256=
  348/348. Ring edges + tail 129140 in for-list + 2
  PASS lines each py+C. Tail 129140: oracle rav sha
  bd073b6e09c2c41d == PINS (== GATE prefix EXACT;
  rawlen 104 re-checked: paylen 88 + 12 + 4); py+C
  CLOSED T10P322R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf430.py (cache path, 0 miss) + secf430b.py
  (DIRECT tool, no cache): staged-vs-oracle 0/0/0/0
  (128793 + 128445 + 128794 + 128446); S0: oracle128793-
  vs-128445 47/84, codeS0-vs-P321S0 47/84, positions
  identical (agree-pos 37 positions listed); DIRECT
  tool 47/84 agree. S1: oracle128794-vs-128446 76/88,
  codeS1-vs-P321S1 76/88, positions identical; DIRECT
  76/88 agree. Triple-derived both pairs (same novel
  shape both tiers: 84/84/84/84 + 88/88/88/88).
  S1-vs-own-C10 secf430c.py (oracle C10 cells n128811-
  820): [29]x10 TRUE-UNIFORM counts AND positions
  identical all 10 (cell0 pos 4,8-11,16-31,60-63,84-87
  == staged EXACT; sig 02000000 both, NOT byte-equal).
  Byte-diff discipline observed throughout.
- C diff pure-add: numstat 608/0 (rgramc.c) + 232/0
  (rgram.py) + 1/1 (for-line) + PINS +62/+0 (clean
  append, all 19126 rows test_rgram_fast.py-tagged,
  cols1-4 purity +62/-0) == GATE; raw C 608 content =
  603 content + 5 bare-blank / 0 del (verified bare, no
  whitespace); full-digit norm ([0-9]+ -> N): C
  del-uniq 0 add-uniq 149/146/148/145 across the 4
  strip/dropempty variants, missing 0 every variant;
  py del-uniq 0 add-uniq 173 all four variants,
  missing 0 (integrity intact, variant-robust);
  C-tempnorm 370 (== GATE) / py-tempnorm 190 recorded.
  Band-level sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope aaaaa11f..
  b6af2b17, 903 added lines == GATE): vendor 0 hits,
  disasm 0 hits, depload 0 hits, libcompression/
  compression_tool//usr/bin/aa 0 hits, shebang 0 hits.
  Files: rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62 (e5d6a3b5), code 6 blocks,
  tier-comments `# T10P` 1820->1826 +6, singletons
  `if n == ` 676->678 +2 / range-guards `<= n <=`
  740->744 +4 = +6 py; C guards: singleton
  `if ((n) == (` 671->673 +2 / range 740->744 +4
  (5-count C-vs-py singleton offset pre-existing,
  unchanged: 678-673 = 676-671 = 5), CLOSED T10P
  prints 1820->1826 +6 py + 1820->1826 +6 C (seal
  1914->1920 +6; offset +94 vs CLOSED-T10P: 1920-1826
  = 94, stable b401-b430). All agree (stated literal
  methods first-hand; 4-space dispatch-exact subset
  gives 666->668 +2 / 718->722 +4 on BOTH files
  identically).
- CONFIRM evidence (CONVERT-01 rule b): A-832-q914
  memo CONFIRM 62/62 CLEAN (own bed r3-P322 128793..
  129172 BAD=0 + own r3-P321, verifier v218.py 62/62
  PASS; w2b-r27 [7/8]; file present, counts verified;
  exact-value corroboration incl PB0 sig-eq-P321PB0
  47/84, PB1 sig-eq-P321PB1 76/88 SAME-as-C10 29/88,
  PBA88-PLAIN-M7b20 sig-29 M7, C10-1SIG-88-M3 SAME-as-
  PB1-sig M3 b87-9f, QUAD88-1SIG-4R SAME-sig-as-PBA +
  R11 rows + r01-share-7B + r01-TRUE-3B + r2r3-lcs0 +
  QM8 + NO frags + b5-const + M-tails NEW, T88-RING-
  STANDARD + TM8/TR8 + tails-split + b84-87 2b3b1c36 +
  edges + consts; plus sheet-vs-tables const-count note:
  Q-914 sheet 80/84/68/70 memo-exact, committed tables
  79/83/67/70 still deduct const-b5 on PBA/C10/quad --
  25th consecutive tables-lag band, geometry exact,
  PORT verdict stands). Agrees with cport commit msg
  (PYID 9563, RGRAM 19126). No viewer P322 geometry
  answer on file at gate time (memo-only recon; this
  VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b430 (own seat
  CLAIM only; exactly 1 GATE-b6af2b17; zero FLAG hits
  on b430/b6af2b17/T10P322/128793; odd bases b429/b431
  respected: b429 tip used as diff-base only; b431 GATE
  uses b430 tip as base + P322 tables as novelty
  baseline = adjacency, no verdict on b430). PROSE-01:
  all hex/counts above copied from own run output; GATE
  re-read in FULL before filing (zero slips on values;
  1 mild method-label note below on tiers sentence).
- RQ==M chain: b430 even FULL8 (M 8B vs RQ 8B agree
  (0,0)..(7,7) 16/16; tabs byte-identical; off-pattern
  maxagree 1). Even-band no-ordinal (viewer convention);
  even running pattern continues b414-full/b416-tail/
  b418-full/b420-strdiff/b422-strdiff/b424-tail-pos-
  differ/b426-full/b428-string-split/b430-string-split.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 mild prose-level note (tiers sentence mixes
py-4space counts 666->668/718->722 with C-filewide
counts 671->673/740->744 under one "(4-space
dispatch-exact)" label -- every stated number is a real
count first-hand and all deltas agree +2/+4; same class
as the b428 note; code GREEN since gated artifact ==
verified artifact). Next-P323 SHAPE banked (A-831/A-832
FWD + GATE FWD-check, for b431: PB0 b7ce7001 pay84
NEW-sig @129141 / PB1 02000000 pay88 @129142 sig-eq-
P322PB1 50/88 / PBA88 2d000000 x16 @129143-158 /
C10 02000000 x10 @129159-168).
