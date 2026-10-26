# VERIFY-aaaaa11f b429 T10P321 pins 128445..128792 (1914 tiers) PASS

Seat viewer-r65, first-hand, tree @aaaaa11f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r65.
Base c72b0b57 (b428 tip, 1908 tiers sealed; this seat's
VERIFY-c72b0b57 PASS-filed same round, base-use only,
respected). Band = 5d3fac7c (py merge w2b@1312c618
partial, +6 tiers, +62 pins) + aaaaa11f (C port, 1914
sealed). Trees manifest-identical to tips (git ls-tree
vs git ls-files cmp clean, 117/117 both; WT detached
at band, will return to lanes/encode-viewer at round
end).

Banked Next-P321 shape (r64 from A-829, refined by
A-830/A-831) CONSUMED FIRST and corroborated below:
PB0 77435801 pay84 NEW-sig (differs vs P320 heads
36ac2c01/02000000) @128445 / PB1 02000000 pay88
sig-eq-P320PB1 (62/88 diff) @128446 / PBA88 3d000000
x16 @128447-462 (SAME-sig-as-P320Q-r01) / C10-region
02000000 pay88 x10 @128463-472 -- all exact.

- Build: make -C src/c BUILDDIR=build429 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc 06fdaebdf6add1363
  a8347b6f1444485cb9d697fd49ddb991c53a833ea640920 /
  sha1 ca6b80778ba334d82f2b056161a97274b9bd2172
  (== GATE both; aae sha256 d6e27c97 pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 9532/9532 covered=9532/9532 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary
  exported BEFORE the run -- r428 lesson applied,
  no wrong-binary repeat, CT_CACHE_DIR set, NVME
  workdir).
- RGRAM py 19064/19064 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19064/19064 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 19064/19064;
  cmp429.py; GATE claims sorted only, raw corroborated
  too).
- PINS 19066 rows (2 hdr + 19064, +62 vs base 19004);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq, seteq429.py). For-list
  union delta vs base +31/-0 (9501->9532):
  128445 128446 128447 128448 128454 128455 128461
  128462 128463 128464 128467 128468 128471 128472
  128473 128480 128488 128489 128504 128505 128511
  128512 128535 128536 128537 128639 128640 128650
  128767 128768 128792
  (== GATE sampled list EXACT). Decomposition first-hand
  from the added set: 2 sing (128445/46) + A head/mid/
  tail pairs (6: 47/48 + 54/55 + 61/62; offs 0,1,7,8,
  14,15) + C head/mid/tail pairs (6: 63/64 + 67/68 +
  71/72; offs 0,1,4,5,8,9; offs 2,3,6,7 = 65/66/69/70
  unsampled, absence verified) + Q head 73/off0 + off7
  80 + boundary-pair 88/89 + pair 04/05 + step-edge
  pair 11/12 (offs 38/39, b5 STEP eb->ec NEW shape,
  first-hand) + tail pair 35/36 (10: offs 0,7,15,16,
  31,32,38,39,62,63) + R head 37/edge-pairs 39/40 +
  67/68/mid 50/tail 92 (7: offs 0,102/103,113,230/231,
  255; 1-mid shape, both counter edges pair-covered,
  first-hand). 31x2=62 rows, range 128445..128792
  exact. PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle
  backend, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit429.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 147 PASS
  0 FAIL first run, no script fixes needed.
  Inventory exactly the 12 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F anywhere -- 0 hits
  both sources; no F0/F1, no QT (R12 carries b84-87 in
  QR), no RT/TT, no BM/BC, no M19/X19, no M42/X42/H42/
  L42, no QB/PT/FM).
  S0 168ch sig 77435801 NEW (30/84 payload diff vs
  P320S0 @ b0,1,2,4,5,11,19-25,27,29,30,36,37,64-75
  first-hand, NOT byte-equal; differs vs P320 heads
  36ac2c01/02000000) / S1 176ch sig 02000000 sig-eq-
  P320PB1 (62/88 payload diff vs P320S1 @ b4,5,11,19,
  25-35,37-79,84-87, NOT byte-equal; [21,21,21,22x7]
  vs own C10 assembled, NOT uniform; sig SAME-as-own-
  C10; differs vs own PB0), staged as full-payload
  singletons.
  AM 16/16 14ch (7B) distinct, CM 10/10 12ch (6B)
  distinct, M 16/16 14ch (7B) distinct, QR 4/4 24ch
  (12B) distinct, RM 16/16 12ch (6B) distinct, RQ 16/16
  14ch (7B) distinct UNPAIRED, no QT + no RT
  (STANDARD tails) + no F (no frags this tier).
  AC 79, b0-3 3d000000 (b0 const 3d), no b4/b5.
  C10-1SIG-88-M6b52 sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 12ch first-hand;
  CC has no b4/b5, b5 const eb full block via lencode).
  S1-vs-own-C10 staged per-cell (M6 b52,53,84-87, b4/b5
  lencode, each cell own assembly) [21,21,21,22x7]
  NOT uniform (cell0 21 @ 4,38,39,45-51,53-59,84-87
  EXACT == oracle cell0; cells differ across k; sig
  02000000 both, NOT byte-equal -- no new TRUE-uniform
  case, chain stays 16 on record).
  QUAD88-2SIG-PAIRED-4R rows0-1 29000000 x32 + rows2-3
  25000000 x32; QM7 b6-8,80-83 16/16 x3 (shared 16/16
  x3 vs row0, NO frags) + R12 rows 4/4 NO pairing
  pairwise-disjoint (BY-ROW const x4; sig-paired r01/r23
  29/25 with b1-3 const 00 in QC; full tuples all
  distinct; r01 share 8B prefix 29b1b49611c5bf4b,
  differ b84 45/65; r23 share 8B prefix
  253fcaa4b16eff42, differ b84 b8/dd);
  tails b84-87 4 distinct 45ae2d53/65ae2d53/b86b2074/
  dd6b2074, DOUBLE paired share r01 TRUE 3B ae2d53 +
  r23 TRUE 3B 6b2074, cross-pair byte-lcs 0 all 4
  combos (lcsuf r01 3, r23 3, cross 0s);
  M-tails 16/16 ALL NEW vs P320T (zero overlap vs P320M
  AND vs P320RM-tail8 AND vs P320RQ-tail8).
  Ring STANDARD: sig 61020000 x256; TM6 b13,14,80-83
  by COL RM 16/16 + TR7 b6-8,76-79 by ROW RQ 16/16
  UNPAIRED (tails SPLIT b80-83 col / b76-79 row);
  b0 const 61 b1 const 02; b84-87 b5f7e384 ring-wide
  NEW.
  M==RQ FULL7: M 7B vs RQ 7B agree (0,0)..(6,6) 16/16
  each; tabs byte-identical ordered AND as sets;
  off-pattern maxagree 0 (zero off-pattern); QM7 byte
  positions b6-8,80-83 (COL, Q region, m = off & 15)
  vs TR7 positions b6-8,76-79 (ROW, R region,
  r = off >> 4). 32nd odd-band RQ==M instance (viewer
  chain b421-28th FULL7/b423-29th TAILS4-ONLY/b425-30th
  TAILS4-ONLY/b427-31st FULL6/b429-32nd FULL7
  sequential); 4th full-identity instance (after P311 +
  P313 + P319, all re-verified vs records).
  Memo-silent on the relation.
  Sorted-unique + _N decls 79/80/67/73 match actual.
  Missing-sets EXACT: AC-9 [4,5,52,53,54,80-83] =
  b4,b5+M7 / CC-8 [4,5,52,53,84-87] = b4,b5+M6 /
  QC-21 [0,4-8,19,50-55,80-87] = b0,b4,b5+QM7+R12 /
  RC-15 [4-8,13,14,76-83] = b4,b5+TM6+TR7.
  VPOS 8/7/21/15 == A-831 EXACT (PBA b4+M7 / C10 b4+M6 /
  quad b0,b4,b5+QM7+R12 (b0 shared) / T b4,b5+TM6+TR7).
  Coverage unions exact every block (const U tab U
  {b4,b5} == 88 x4, 0 overlap); each missing ==
  region pay-index set (A/C/Q/R region text re-derived
  first-hand, tab == region-idx minus {b4,b5} EXACT
  all 4).
  Q legs M[m] + QR[q] both sides, NO F-legs in Q;
  R legs RM[c] + RQ[r] both sides, NO F-legs in R
  (STANDARD RM-col / RQ-row verified in region text
  both sides). RM 16/16 12ch distinct + RQ 16/16 14ch
  distinct, sets disjoint.
  P320 refs re-read: S0 36ac2c01 / S1 02000000 /
  PBA 36000000 / C10 02000000 / QUAD 2SIG 3d/11.
  PBA sig 3d NEW vs P320 36 (3d000000 != 36000000);
  QUAD 2SIG 29/25 vs P320 2SIG 3d/11 (rows NEW,
  PAIRED structure continues). AM/CM/M/QR/RM/RQ
  0-overlap vs P320. Memo INCL PBA 80 / C10 81 /
  quad 67 / T88 73 (A-831 re-read): impl 79/80/67/73
  = deduct-b5-only-when-b5vary rule (A b5 const eb
  counted, C b5 const eb counted, Q b5 STEP-varies
  deducted, T b5 varies deducted) -- S-F arithmetic
  persists though the sheet is FIXED; geometry exact,
  PORT verdict stands; memo-exact on quad (b5 STEP-
  varies, in tab) and T88 (b5 varies, no deduction).
  24th consecutive tables-lag band (b429 pattern
  +1/+1/+0/+0: PBA/C10 lag; running b412-b428 per
  GATE + r64/r65 records).
  Base temp maxes _t6584/_b3983/_i3984 (no reuse:
  band adds _t6585-6600 continuous-16 + _i3986/88/91/
  94 + _b3985/87/89/90/92/93, all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 128445 / S1 128446 / A 128447-462 / C 128463-472 /
  Q 128473-536 / R 128537-792): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C both sides (b5
  const eb emerges from raw lencode, NO step; Q STEP
  eb->ec @off39: 128511 ff/eb -> 128512 01/ec) + R
  explicit counter (b4=(0x33+2off)&FF b5=0xec+
  (off>=103)+(off>=231); py hex 0x33/0xec; C staged
  literals 51/236, re-derived: 51==0x33, 236==0xec;
  Q literals 179/235 == 0xb3/0xeb) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A M7 b52-54,80-83;
  C M6 b52,53,84-87; Q QM7 b6-8,80-83 + R12 b0,19,
  50-55,84-87; R TM6 b13,14,80-83 by COL + TR7 b6-8,
  76-79 by ROW, tails SPLIT) + C guards
  `if ((n) == (128445))` / `(128446)` + 4 range guards
  exact + counter literals exact + C byte-index lists
  match py per block. C blocks carry T86264/86269/
  86274/86289/86304/86324 py-line mirrors (T86264/
  T86269 spot-verified verbatim against py lines
  86264/86269); bounds + byte positions exact (A 7B,
  C 6B, Q 7B/12B, R 6B/7B STANDARD-split).
  Insert exact both sides: after T10P320R close, at
  dispatch tail (N-out-of-scope fallthrough follows;
  2 scope hits py + 2 scope hits C). Matches A-831
  geometry (values re-checked in audit above; NO D
  dips: ownloop tags exactly the 6 P321 blocks).
- Edges own-loop ownloop429.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (302 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P321R N=128792
  off=255. edges429.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 7b/eb, 7d/eb
  == raw lencode) + aform 16/16 (A head 7f/eb tail
  9d/eb b5set {eb} NO step, 0 ff) + cform 10/10 (C
  head 9f/eb tail b1/eb b5set {eb} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head b3/eb edge
  128511 ff/eb -> 128512 01/ec tail 31/ec b5set
  {eb,ec} STEP @off39, exactly 1 ff in 64) + ring
  counter 256/256 + ringraw 256/256 (head 33/ec;
  128639 off102 ff/ec -> 128640 off103 01/ed; mid
  off113 15/ed at 128650; 128767 off230 ff/ed ->
  128768 off231 01/ee; tail off255 31/ee; exactly
  2 ff in 256); ff total x3 (1 Q + 2 R); ff-in-Q 1
  (128511, the STEP edge). odd-lencode 92+256=348/348.
  Ring edges + tail 128792 in for-list + 2 PASS lines
  each py+C. Tail 128792: oracle rav sha 88f2188f1cec
  1b15... == PINS (== GATE prefix EXACT; rawlen 104
  re-checked: paylen 88 + 12 + 4); py+C CLOSED
  T10P321R off=255 agree. No DISSENT: cut bytes verify.
- PB-diff secf429.py (cache path, 0 miss) + secf429b.py
  (DIRECT tool, no cache): staged-vs-oracle 0/0/0/0
  (128445 + 128097 + 128446 + 128098); S0: oracle128445-
  vs-128097 30/84, codeS0-vs-P320S0 30/84, positions
  identical (agree-pos 54 positions listed); DIRECT
  tool 30/84 agree. S1: oracle128446-vs-128098 62/88,
  codeS1-vs-P320S1 62/88, positions identical; DIRECT
  62/88 agree. Triple-derived both pairs (same novel
  shape both tiers: 84/84/84/84 + 88/88/88/88).
  S1-vs-own-C10 secf429c.py (oracle C10 cells n128463-
  472): [21,21,21,22x7] NOT uniform (matches GATE);
  cell0 pos == staged cell0 pos EXACT (21 positions);
  sig 02000000 both, NOT byte-equal. Byte-diff
  discipline observed throughout.
- C diff pure-add: numstat 607/0 (rgramc.c) + 232/0
  (rgram.py) + 1/1 (for-line) + PINS +62/+0 (clean
  addition, gen tag test_rgram_fast.py, cols 27.0.1/
  ct-lzraven stable) == GATE; raw C 607 content = 602
  content + 5 bare-blank / 0 del (verified bare, no
  whitespace); full-digit norm ([0-9]+ -> N): C
  del-uniq 0 add-uniq 150/147/149/146 across the 4
  strip/dropempty variants, missing 0 every variant;
  py del-uniq 0 add-uniq 174 all four variants,
  missing 0 (integrity intact, variant-robust);
  C-tempnorm 368 / py-tempnorm 190 recorded. Band-level
  sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope c72b0b57..
  aaaaa11f, 902 added lines == GATE): vendor 0 hits,
  disasm 0 hits, depload 0 hits, libcompression/
  compression_tool//usr/bin/aa 0 hits, shebang 0 hits.
  Files: rgramc.c 607/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62 (5d3fac7c), code 6 blocks,
  tier-comments `# T10P` 1814->1820 +6, singletons
  `if n == ` 674->676 +2 / range-guards `<= n <=`
  736->740 +4 = +6 py; C guards: singleton
  `if ((n) == (` 669->671 +2 / range 736->740 +4
  (5-count C-vs-py singleton offset pre-existing,
  unchanged: 676-671 = 674-669 = 5), CLOSED T10P
  prints 1814->1820 +6 py + 1814->1820 +6 C (seal
  1908->1914 +6; offset +94 vs CLOSED-T10P: 1914-1820
  = 94, stable b401-b429). All agree, no slip
  (stated literal methods, first-hand).
- CONFIRM evidence (CONVERT-01 rule b): A-831-q913
  memo CONFIRM 61/61 CLEAN (own bed r3-P321 128445..
  128824 BAD=0 + own r3-P320, verifier v217.py 61/61
  PASS, novelty DOUBLE paired tail-share gated; w2b-r27
  [6/8]; file present, counts verified; exact-value
  corroboration incl PB0 NEW-sig 77435801, PB1 sig-eq-
  P320PB1 62/88 SAME-as-C10 21/88, PBA88-PLAIN-M7b52
  sig-3d M7, C10-1SIG-88-M6b52 SAME-as-PB1-sig M6,
  QUAD88-2SIG-PAIRED-4R rows0-1-29/rows2-3-25 + R12
  rows + DOUBLE-r01-TRUE3 + DOUBLE-r23-TRUE3 +
  cross-lcs0 + b0-sig-paired + step edge @39 +
  M-tails NEW, T88-RING-STANDARD + TM6/TR7 + tails-
  split + b84-87 b5f7e384 + edges + consts; plus
  sheet-vs-tables const-count note: Q-913 sheet 80/81/
  67/73 memo-exact, committed tables 79/80/67/73 --
  deduct-b5-only-when-b5vary rule, geometry exact,
  PORT verdict stands; 24th consecutive tables-lag
  band). Agrees with cport commit msg (PYID 9532,
  RGRAM 19064). No viewer P321 geometry answer on file
  at gate time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b429 (own seat
  CLAIM only; exactly 1 GATE-aaaaa11f; zero FLAG hits
  on b429/aaaaa11f/T10P321/128445; even bases b428/b430
  respected: b428 tip used as diff-base only, b430
  untouched). PROSE-01: all hex/counts above copied
  from own run output; GATE re-read in FULL before
  filing (zero prose slips found -- every numeric claim
  verified: temps lists, edge values, tail sha, guard
  counts, VPOS, missing sets, INCL consts).
- RQ==M chain: b429 odd FULL7 (M 7B vs RQ 7B agree
  (0,0)..(6,6) 16/16; tabs byte-identical; off-pattern
  maxagree 0). 32nd odd-band instance (viewer chain
  b421-28th FULL7/b423-29th TAILS4-ONLY/b425-30th
  TAILS4-ONLY/b427-31st FULL6/b429-32nd FULL7
  sequential); 4th full-identity instance (after P311 +
  P313 + P319). Running odd pattern continues.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs and prose (zero slips). Next-P322 SHAPE banked
(A-831 re-read, for b430: PB0 77435801 pay84 @128793
sig-eq-P321PB0 47/84 / PB1 pay88 @128794 76/88 /
PBA88 29000000 x16 @128795-810 SAME-sig-as-P321Q-r01 /
C10 02000000 x10 @128811-820).
