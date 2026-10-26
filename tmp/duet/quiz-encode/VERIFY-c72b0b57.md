# VERIFY-c72b0b57 b428 T10P320 pins 128097..128444 (1908 tiers) PASS

Seat viewer-r65, first-hand, tree @c72b0b57,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r65.
Base 49f9f3e4 (b427 tip, 1902 tiers sealed; GATE-filed
PASS-functional, base-use only, respected). Band =
aab116ae (py merge w2b@aa3789ae partial, +6 tiers, +62 pins)
+ c72b0b57 (C port, 1908 sealed). Trees manifest-identical
to tips (git ls-tree vs git ls-files cmp clean, 117/117 both;
WT detached at band, will return to lanes/encode-viewer
at round end).

Banked Next-P320 shape (r64 from A-829, refined by A-830)
CONSUMED FIRST and corroborated below: PB0 36ac2c01 pay84
sig-eq-P319PB0 30/84 @128097 / PB1 02000000 pay88
sig-eq-P319PB1 76/88 @128098 / PBA88 36000000 x16
@128099-114 / C10-region 02000000 pay88 x10 @128115-124
-- all exact.

- Build: make -C src/c BUILDDIR=build428 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warning/error lines. sha256 rgramc c0fdc1959842
  08211113415692ecb00d061e11a83b777fc594609cf4741b4ef2 /
  aae d6e27c97ced21673cc73eee061ffdbd7f0358a87e48205
  6c222a867202110785 (== GATE sha256 both; aae
  pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 9501/9501 covered=9501/9501 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir). Scar note: first run
  WITHOUT RGRAMC export ran the stale default binary
  (/Volumes/NVME/.../build/aae/rgramc, Oct 20) and went
  RED 6082/7391 covered=7391/9501 -- caught by the run,
  re-ran with seat binary GREEN (r63/r64 wrong-binary
  class, same fix).
- RGRAM py 19002/19002 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19002/19002 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 19002/19002;
  cmp428.py; GATE claims sorted only, raw corroborated too).
- PINS 19004 rows (2 hdr + 19002, +62 vs base 18940);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq, seteq428.py). For-list union delta
  vs base +31/-0 (9501->9501... 9470->9501):
  128097 128098 128099 128100 128106 128107 128113 128114
  128115 128116 128119 128120 128123 128124 128125 128127
  128128 128141 128156 128157 128173 128180 128187 128188
  128189 128255 128256 128300 128383 128384 128444
  (== GATE sampled list EXACT). Decomposition first-hand
  from the added set: 2 sing (128097/98) + A head/mid/tail
  pairs (6: 99/100 + 06/07 + 13/14; offs 0,1,7,8,14,15) +
  C head/mid/tail pairs (6: 15/16 + 19/20 + 23/24; offs
  0,1,4,5,8,9; no unsampled C offs -- C10 b5-const full
  block, first-hand) + Q head 25/off0 + b5-step EARLY edge
  pair 27/28 /offs2,3 + mids 41/56/57/73/80 + tail pair
  87/88 (10: offs 0,2,3,16,31,32,48,55,62,63; edge pair
  pinned first-hand) + R head 89/edge-pairs 55/56+83/84/
  mid 300/tail 444 (7: offs 0,66/67,194/195,111,255).
  31x2=62 rows, range 128097..128444 exact. PINS-new-N
  == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py,
  no oracle; no env-block this round).
- Tables audit own script tabaudit428.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 147 PASS
  0 FAIL first run after 2 seat script-transcription
  fixes (findall group target; over-strict r01-share) +
  1 first-hand correction (r01 shares 13B b0-b12, differ
  b13 ad/2d, NOT 16B) -- all caught by runs, none escaped.
  Inventory exactly the 12 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F anywhere -- 0 hits both
  sources; no F0/F1, no QT/RT/TT, no BM/BC, no M19/X19,
  no M42/X42/H42/L42, no QB/PT/FM).
  S0 168ch sig 36ac2c01 sig-eq-P319PB0 (30/84 payload diff
  vs P319S0 @ b4-11,13,15,17,18,44-47,50,51,56-63,80-83
  first-hand, NOT byte-equal) / S1 176ch sig 02000000
  sig-eq-P319PB1 (76/88 payload diff vs P319S1 @
  b4-55,64-87, NOT byte-equal; 28/88 diff vs own
  C10[0] assembled, NOT byte-equal; sig SAME-as-own-
  C10; differs vs own PB0), staged as full-payload
  singletons.
  AM 16/16 18ch distinct, CM 10/10 8ch distinct, M 16/16
  16ch distinct, QR 4/4 58ch distinct, RM 16/16 16ch
  distinct, RQ 16/16 16ch distinct UNPAIRED, no QT
  (quad tails live in R29) + no RT (STANDARD tails) +
  no F (no frag this tier).
  AC 77, b0-3 36000000 (b0 const 36), no b4/b5. C10-1SIG-
  88-TAIL sig 02000000 x10 SAME-as-PB1 (sig in CC b0-3
  consts; CM 10/10 diverge 8ch first-hand: fb512d1b/
  1b522d1b/3b522d1b/5b522d1b/7b522d1b/1a852d1b/3a852d1b/
  834b651d/a34b651d/c34b651d; CC HAS b8 const 0x99 --
  C10 assembly takes b8 from consts, tab is b84-87 only,
  first-hand from region text; CC has no b4/b5,
  b5 const e8 full block via lencode).
  S1-vs-own-C10 staged per-cell (M4 b84-87, b8 const,
  b4/b5 lencode, each cell own assembly) [28]x10
  TRUE-UNIFORM count+position (cell0 28 @
  4,19,26-43,72-75,84-87 EXACT; positions identical
  all 10 staged AND oracle; sig 02000000 both, NOT
  byte-equal -- 16th TRUE-uniform case on record, 15th
  excluding unverified P299; beyond-GATE values
  corroborated by oracle leg below).
  QUAD88-2SIG-PAIRED-4R rows0-1 3d000000 x32 + rows2-3
  11000000 x32; QM8 b40-43,80-83 16/16 x3 (shared
  16/16 x3 vs row0 first-hand, NO frags) + R29 rows 4/4
  NO pairing pairwise-disjoint (sig-paired r01/r23,
  full tuples all distinct; r01 share 13B b0-b12
  3df9e99c14009e7c7899736e1e, differ b13 ad/2d;
  r23 share 26 equal-positions; r2r3 tails TRUE-1B 0x25
  @pos3 (53 vs 1e @b86, 25/25 @b87), r0/r1-lcs0 vs all
  pairs, r2r3-lcs1; b87 NOT const quad-wide {ways differ};
  M-tails 16/16 ALL NEW vs P319T (zero overlap vs P319M
  AND vs P319RM-tail8 AND vs P319RQ-tail8).
  Ring STANDARD: sig bd020000 x256; TM8 b30,39,46,47,
  80-83 by COL RM 16/16 + TR8 b40-43,76-79 by ROW RQ
  16/16 UNPAIRED (tails SPLIT b80-83 col / b76-79 row);
  b0 const bd b1 const 02; b84-87 16cb2a30 ring-wide
  NEW (P319 SWAPPED-split era per Q-912: P319T b80-83
  ROW-led via RQ).
  M==RQ FULL8: M 8B vs RQ 8B agree (0,0)..(7,7) 16/16
  each; tabs string-identical ordered AND as sets;
  off-pattern maxagree 1 (essentially no off-pattern);
  QM8 byte positions b40-43,80-83 (COL, Q region, m =
  off & 15) vs TR8 positions b40-43,76-79 (ROW, R
  region, r = off >> 4): b40-43 shared positions,
  tails SPLIT. Even band: no ordinal (viewer convention;
  even running pattern b414-full/b416-tail/b418-full/
  b420-strdiff/b422-strdiff/b424-tail-pos-differ/
  b426-full/b428-string-split).
  Sorted-unique + _N decls 77/82/49/70 match actual.
  Missing-sets EXACT: AC-11 [4,5,29,30,31,34,35,80-83]
  = b4,b5+M9 / CC-6 [4,5,84,85,86,87] = b4,b5+M4 (b8 in
  consts, NOT missing -- first-hand) / QC-39 [0,4,5,8-15,
  19,25-43,80-87] = b0,b4,b5+QM8+R29 / RC-18
  [4,5,30,39,40,41,42,43,46,47,76-83] = b4,b5+TM8+TR8.
  VPOS 10/5/39/18 == A-830 EXACT (PBA b4+M9 / C10 b4+M4 /
  quad b0,b4,b5+QM8+R29 / T b4,b5+TM8+TR8). Coverage
  unions exact every block (const U tab U {b4,b5} == 88
  x4, 0 overlap); each missing == region pay-index set
  (A/C/Q/R region text re-derived first-hand, tab ==
  region-idx minus {b4,b5} EXACT all 4).
  Q legs M[m] + QR[q] both sides, NO F-legs in Q;
  R legs RM[c] + RQ[r] both sides, NO F-legs in R
  (STANDARD RM-col / RQ-row verified in region text
  both sides). RM 16/16 distinct + RQ 16/16 distinct,
  sets disjoint; b0 consts differ by row (RM 13x9a+3xa2
  vs RQ all-distinct b0s).
  P319 refs re-read: S0 36ac2c01 / S1 02000000 /
  PBA 25000000 / C10 02000000 / QUAD 2SIG 21/10.
  PBA sig 36 NEW vs P319 25 (36000000 != 25000000);
  QUAD 2SIG 3d/11 vs P319 2SIG 21/10 (rows NEW,
  PAIRED structure continues). AM/CM/M/QR/RM/RQ
  0-overlap vs P319 (prev lens 16/10/16/4/16/16).
  Memo INCL PBA88 78 / C10 83 / quad 49 / T88 70
  (A-830 re-read): impl 77/82/49/70 = writer-1 on
  PBA/C10: impl tables still deduct const-b5 on
  PBA/C10 (b5 covered by lencode instead) while
  Q-912 sheet counts b5 (memo A-830 confirms the
  sheet) -- S-F arithmetic persists in committed
  tables though the sheet is FIXED; geometry exact,
  PORT verdict stands; memo-exact on quad (b5
  STEP-varies, in tab) and T88 (b5 varies,
  no deduction). 23rd consecutive tables-lag band
  (b428 pattern +1/+1/+0/+0: PBA/C10 lag; running
  b412-b427 per GATE + r64 records).
  Base temp maxes _t6568/_b3973/_i3974 (no reuse:
  band adds _t6569-84 continuous-16 + _b3975/77/79/80/
  82/83 + _i3976/78/81/84, all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 128097 / S1 128098 / A 128099-114 / C 128115-124 /
  Q 128125-188 / R 128189-444): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C/Q both sides (b5
  const e6 emerges from raw lencode A/C, NO step; Q
  STEP e8->e9 @off3 EARLY: 128127 ff/e8 -> 128128
  01/e9) + R explicit counter (b4=(0x7b+2off)&FF
  b5=0xe9+(off>=67)+(off>=195); py hex 0x7b/0xe9; C
  staged literals 123/233, re-derived: 123==0x7b,
  233==0xe9; Q literals 251/232 == 0xfb/0xe8) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A M9 b29,30,31,34,35,
  80-83; C M4 b84-87 + b8 const; Q QM8 b40-43,80-83 +
  R29 b0,8-15,19,25-39,84-87; R TM8 b30,39,46,47,80-83
  by COL + TR8 b40-43,76-79 by ROW, tails SPLIT) + C
  guards `if ((n) == (128097))` / `(128098)` + 4 range
  guards exact + counter literals exact + C byte-index
  lists match py per block. C block line numbers follow
  C10-region (block 228990+); py CLOSED 86025 + guard
  86027 re-checked (GATE insert-position numbers
  re-read, not re-derived).
  Insert exact both sides: after T10P319R close (py
  CLOSED-then-guard; C block 228990 follows P319R
  close), at dispatch tail (N-out-of-scope fallthrough
  follows). Matches A-830 geometry (values re-checked
  in audit above; NO D dips: ownloop tags exactly the
  6 P320 blocks).
- Edges own-loop ownloop428.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (302 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P320R N=128444
  off=255. edges428.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 c3/e8, c5/e8
  == raw lencode) + aform 16/16 (A head c7/e8 tail
  e5/e8 b5set {e8} NO step, 0 ff) + cform 10/10 (C
  head e7/e8 tail f9/e8 b5set {e8} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head fb/e8 edge
  128127 ff/e8 -> 128128 01/e9 tail 79/e9 b5set
  {e8,e9} STEP @off3, exactly 1 ff in 64) + ring
  counter 256/256 + ringraw 256/256 (head 7b/e9;
  128255 off66 ff/e9 -> 128256 off67 01/ea; mid
  off111 59/ea at 128300; 128383 off194 ff/ea ->
  128384 off195 01/eb; tail off255 79/eb; exactly
  2 ff in 256); ff total x3 (1 Q + 2 R, both ring
  edges counted in R); ff-in-Q 1 (128127, the EARLY
  edge). odd-lencode 92+256=348/348. Ring
  edges + tail 128444 in for-list + 2 PASS lines each
  py+C. Tail 128444: oracle rav sha 44e643b375490faa
  == PINS (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P320R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf428.py (cache path, 0 miss) + secf428b.py
  (DIRECT tool, no cache): staged-vs-oracle 0/0/0/0
  (128097 + 127749 + 128098 + 127750); S0: oracle128097-
  vs-127749 30/84, codeS0-vs-P319S0 30/84, positions
  identical (agree-pos 54 positions listed); DIRECT
  tool 30/84 agree. S1: oracle128098-vs-127750 76/88,
  codeS1-vs-P319S1 76/88, positions identical; DIRECT
  76/88 agree. Triple-derived both pairs (same novel
  shape both tiers: 84/84/84/84 + 88/88/88/88).
  S1-vs-own-C10 secf428c.py (oracle C10 cells n128115-
  124): [28]x10 TRUE-UNIFORM counts AND positions
  identical all 10 (cell0 pos 4,19,26-43,72-75,84-87
  == staged EXACT; sig 02000000 both, NOT byte-equal).
  Byte-diff discipline observed throughout.
- C diff pure-add: numstat 607/0 (rgramc.c) + 232/0
  (rgram.py) + 1/1 (for-line) + PINS regen 10730/10668
  (cols1-4 purity +62/-0 verified first-hand, gen-col
  normalized test_rgram.sh -> test_rgram_fast.py on all
  old rows, cols6-7 stable 27.0.1/ct-lzraven) == GATE;
  raw C 602 content + 5 bare-blank / 0 del (verified
  bare, no whitespace); full-digit norm ([0-9]+ -> N):
  C del-uniq 0 add-uniq 151/148/150/147 across the 4
  strip/dropempty variants, missing 0 every variant;
  py del-uniq 0 add-uniq 169 all four variants,
  missing 0 (integrity intact, variant-robust -- no
  norm-gap on this even band); C-tempnorm 399 (==
  GATE) / py-tempnorm 191 recorded. Band-level sole
  del = old for-line churn (1/1).
- Wall on band diff added lines (scope 49f9f3e4..
  c72b0b57, 11570 added lines == GATE): vendor 0 hits,
  disasm 0 hits, depload 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits. Files: rgramc.c 607/0,
  rgram.py 232/0 purely additive, test_rgram.sh 1/1
  (for-line), PINS regen (values +62/-0).
- Tiers: merge-msg +6/+62 (aab116ae), code 6 blocks,
  dispatch-guards file-wide singletons `if n == ` 672->
  674 +2 / range-guards `<= n <=` 732->736 +4 = +6 py;
  C file-wide singletons `if ((n) == (` 667->669 +2 /
  range lower-bound `) <= (n)` 732->736 +4
  (5-count C-vs-py singleton offset pre-existing,
  unchanged: 674-669 = 672-667 = 5); 4-space
  dispatch-exact subset gives 662->664 +2 / 710->714 +4
  on BOTH files identically (deltas agree under every
  method; no else-if either side: py elif 46->46, C
  else-if 0->0), CLOSED T10P prints 1808->1814 +6 py +
  1808->1814 +6 C (seal 1902->1908 +6; offset
  +94 vs CLOSED-T10P: 1908-1814 = 94, stable b401-b428).
  All agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-830-q912-P320
  verdict CONFIRM 63/63 CLEAN (own bed r3-P320
  128097..128476 BAD=0 + own r3-P319, verifier v216.py
  63/63 PASS; writer CORRECTION PBA M8->M9 verified:
  9-pos list b29,30,31,34,35,80-83, VPOS 10 exact; file
  present, counts verified; exact-value corroboration
  incl PB0 sig-eq-P319PB0 30/84, PB1 sig-eq-P319PB1
  76/88 SAME-as-C10 28/88, PBA88-PLAIN-M9 sig-36 M9,
  C10-TAIL SAME-as-PB1-sig M4 (b8 in consts, tab b84-87
  only), QUAD88-2SIG-PAIRED-4R rows0-1-3d/rows2-3-11 +
  R29 rows + r2r3-paironly-25 + b87-{25,8f,26} +
  r0/r1-share-13B + QM8 + NO frags + b5-step-EARLY +
  M-tails NEW, T88-RING-STANDARD + TM8/TR8 + tails-
  split + b84-87 16cb2a30 + edges + consts; plus
  sheet-vs-tables const-count note: Q-912 sheet 78/83/
  49/70 memo-exact, committed tables 77/82/49/70 still
  deduct const-b5 on PBA/C10 -- 23rd consecutive
  tables-lag band, geometry exact, PORT verdict stands).
  Agrees with cport commit msg (PYID 9501, RGRAM 19002).
  No viewer P320 geometry answer on file at gate time
  (memo-only recon; this VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b428 (own seat
  CLAIM only; exactly 1 GATE-c72b0b57; zero FLAG hits
  on b428/c72b0b57/T10P320/128097; later-band GATE-
  aaaaa11f uses b428 tip as base + P320 tables as
  novelty baseline = adjacency, no verdict on b428;
  odd bases b427 respected). PROSE-01: all hex/counts
  above copied from own run output; GATE re-read in
  FULL before filing (temps + tiers lines re-read twice
  after first-read misrecall of _b list).
- RQ==M chain: b428 even FULL8 (M 8B vs RQ 8B agree
  (0,0)..(7,7) 16/16; tabs string-identical ordered;
  off-pattern maxagree 1; positions tails-split QM8-col/
  TR8-row). Even-band no-ordinal (viewer convention);
  even running pattern continues b414-full/b416-tail/
  b418-full/b420-strdiff/b422-strdiff/b424-tail-pos-
  differ/b426-full/b428-string-split.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 mild prose-level note (tiers sentence mixes
py-4space counts 662->664/710->714 with C-filewide
counts 667->669/732->736 under one "(4-space
dispatch-exact)" label -- every stated number is a real
count first-hand and all deltas agree +2/+4; suggest
single-method presentation; code GREEN since gated
artifact == verified artifact). Next-P321 SHAPE banked
(A-830 re-read, for b429: PB0 77435801 pay84 NEW-sig
@128445 / PB1 02000000 pay88 @128446 sig-eq-P320PB1
62/88 / PBA88 3d000000 x16 @128447-462 SAME-sig-as-
P320Q-r01 / C10 02000000 x10 @128463-472).
