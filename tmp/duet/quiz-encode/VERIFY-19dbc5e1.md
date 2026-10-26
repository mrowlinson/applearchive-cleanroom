# VERIFY-19dbc5e1 b416 T10P308 pins 123921..124268 (1836 tiers) PASS

Seat viewer-r62, first-hand, tree416 @19dbc5e1,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r62.
Base c9b64be1 (b415, 1830 tiers). Band = 2cda9e71 (py merge
w2b@182e07f4 partial, +6 tiers, +62 pins) + 19dbc5e1 (C port,
1836 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117/117).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build416/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc d66b52c3cc92a4d1 / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  fa62bc728faeb14f / aae 7d8dd3a2d118e0db (recorded, no
  GATE claim).
- RGRAMC-PYID 9122/9122 covered=9122/9122 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 18244/18244 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 18244/18244 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp equal + raw-order identical, 18244/18244).
- PINS 18246 rows (2 hdr + 18244, +62 vs base 18184);
  PASS-names vs PINS-names xor 0 py+C; py-vs-C xor 0;
  base-N vs for-list xor 0 (4-way set-eq). For-list
  delta vs base +31/-0:
  123921 123922 123923 123924 123930 123931 123937 123938
  123939 123940 123943 123944 123947 123948 123949 123956
  123965 123972 123981 123988 123997 124004 124011 124012
  124013 124031 124032 124159 124160 124200 124268
  (== GATE verbatim: S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid pairs (6) + Q head/7-mids/tail-pair (10) + R
  head/edge-pair/edge-pair/mid/tail (7); 9091->9122);
  31x2=62 rows, range 123921..124268 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60/r61); band
  diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit416.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 162 PASS
  0 FAIL. Inventory exactly the 13 both sides (PBA88-
  PLAIN/C10-1SIG-88/QUAD88-2SIG-MUL2/RING-STANDARD + F;
  no F0/F1, no QT/RT, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42); C==py 13/13. S0 168ch sig
  ab685400 NEW (33/84 vs P307S0 @ 2,4,5,20-23,25,27-33,
  36-41,52-55,76-83 EXACT) / S1 176ch sig 01000000 NEW
  SAME-as-own-C10-sig (70/84 first-84 vs P307S1 EXACT;
  88B-vs-84B width novelty). AM 16x14ch distinct; AC 79,
  b0-3 10000000 (b0 const 10), no b4/b5, PBA sig
  10000000 x16 PLAIN (NEW sig 10). CM 10x20ch 10/10
  diverge; rows0-8 share 12ch cba8aa5a6d55 + (byte6,
  byte7) 9 distinct pairs (1935/3935/5935/7935/9934/
  9935/b934/d934/f934; byte7 split 34x4/35x5) + tail
  92ff; row9 a16208df842fb6b0c9df tail c9df. CC 76,
  b0-3 01000000, no b4/b5 (b5 const c8 via lencode).
  S1-vs-C10[0] staged assembly 59/88 NOT-byte-equal
  (C10[0] own lencode 47/c8 @123939 re-derived). M
  16x8ch distinct (QM4 b80-83). F 16x6ch 16 distinct
  incl 00782d @m7 (00-case). QR 4x32ch 4-distinct
  UNPAIRED; r0 0975ec41be8a4601b2d81e5da0bf881d
  distinct; r123 share 24ch 129b07827c158d0042dac637
  + b84-diverge 13/57/7c; tails b84-87 a0bf881d/
  13be75da/57be75da/7cbe75da 4/4 distinct; r123 ALL
  TRUE 3B be75da; full-row lcsuf r123 pairs 3,
  r0-vs-rest 0 + lcpre r123 12, r0-vs-rest 0 (r0
  lcs=0 holds both senses). QC 63, b0 in R16 tab
  (missing), b1-3 00/00/00, no b4/b5 (QUAD 2SIG:
  r0 09 x16 + r123 12 x48), b16 const 76 quad-wide.
  MUL2 chain formulas verified in code text both sides
  (py: (f13*2)&FF / f13>=0x80 / (f14*2+c13)&FF /
  f14*2+c13>=0x100 / (f15*2+c14)&FF; C literals
  identical); chain outputs 16 distinct; 00-case chain
  00f05a with byte-eq b13 (00*2=00); chain-ne-r0
  16/16. RM 16x18ch distinct; RQ 16x14ch distinct;
  RM-vs-RQ UNPAIRED (sets disjoint); RC 70, b0-1
  0b01, b84-87 e96a6311 ring-wide NEW. RQ-tail-EQ-M:
  M 4B vs RQ 7B agree (0,3),(1,4),(2,5),(3,6) 16/16
  each; ALL off-pattern cells 0/16 -- zero off-pattern
  incidentals HOLDS exactly; M[0:4]==RQ[3:7] all 16
  rows (TR7 b76-79 row-led == QM4 b80-83). Tails
  STANDARD-SPLIT (RM b80-83 by COL, RQ b76-79 by ROW,
  16/16 distinct each, 0 overlap). Sorted-unique +
  _N decls 79/76/63/70 match actual. Missing-sets
  EXACT: AC [4,5,6,7,12,80-83]; CC [4,5,6,7,52-55,
  84-87]; QC [0,4,5,6-15,52-55,80-87] (25); RC [4,5,
  9-14,18,19,76-83] (18). VPOS 8/11/24/18 (b5-const
  excluded PBA/C10/quad; T full 18) == A-793 EXACT.
  Coverage unions exact every block (const U tab U
  {b4,b5} == 88 x4, 0 overlap). Q legs M[m] + QR[q]
  + FRAG F[m] both sides. R legs RM[c] + RQ[r] both
  sides, NO F-legs. AC-QC shared-pos 63, same-val 23,
  AConly 16, QConly 0 (computed first-hand). P307
  refs re-read: S0 ab687400 / S1 803b4f44 / PBA
  05000000 / C10-1SIG 803b4f84 / QUAD 09000000 x64.
  Next-P308 preds (A-787 re-read: PB0 ab685400 NEW /
  PB1 01000000 pay88 / PBA88 10000000 x16 / C10-region
  01000000 pay88 x10 SAME-as-PB1) x4 corroborated
  (banked-from-r61 CONSUMED). PBA NEW vs P307
  (10000000 != 05000000); QUAD 2SIG vs P307 single
  09. AM/CM/M/QR/RM/RQ 0-overlap vs P307 (widths P308
  AM14/CM20/M8/QR32/RM18/RQ14 vs P307 AM16/CM22/M12/
  QR20/RM20/RQ14 chars, base widths re-read
  first-hand). M-tails 16/16 ALL NEW vs P307 M-tail8
  + RM-tail8 + RQ-tail8 (overlap 0 x3). Memo INCL
  PBA88 80 / C10 77 / quad88 64 / T88 70 (A-793
  re-read): impl 79/76/63/70 = memo-1 on PBA/C10/
  quad (b5-const excluded), identical T88 -- standing
  +1 rule coherent, +1/+1/+1/+0. Base temp maxes
  _t6358/_b3852/_i3853 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 123921 / S1 123922 / A 123923-938 / C 123939-948 /
  Q 123949-124012 / R 124013-268): bounds + paylens
  (1x84 + 347x88, SHAPE NOVELTY) + lencode
  l16=((n<<1)|1)&FFFF A/C/Q both sides (b5-const c8
  emerges from raw lencode) + FRAG MUL2 carry-chain
  b13->b15 BOTH sides (py: q==0 ftab vs F[m], else
  fmul2 e13/e14/e15 with c13/c14 carries; C: hexval
  triple + identical chain, literals 2/128/255/256
  re-derived from code text) + R counter b4=(0xdb+
  2off)&FF b5=0xc8+(off>=19)+(off>=147) (py hex; C
  staged decimal 219/200, re-derived: 219==0xdb,
  200==0xc8) + m=off&15/q=off>>4/c=off&15/r=off>>4
  both sides + mtab/rtab byte positions exact (A 7B
  b6,7,12,80-83; C 10B b6,7,52-55,84-87; Q QM4
  b80-83 + R16 b0,6-12,52-55,84-87 + F3 b13-15; R
  TM9 b12-14,18,19,80-83 by COL + TR7 b9-11,76-79
  by ROW) + C guards `if ((n) == (123921))` /
  `(123922)` + 4 range guards exact + C byte-index
  lists match py per block (A 7B, C 10B, Q 4B/16B/3B,
  R 9B/7B). T-mirrors T83042/83047/83052/83067/83083/
  83119 each re-read: hits the exact py guard line.
  Temps _t6359-6376 continuous-18 (base max _t6358;
  added-lines-only, context _t1/2/3 excluded) +
  _b3854/3856/3858/3859/3860/3862/3863 (base max
  _b3852) + _i3855/3857/3861/3864 (base max _i3853):
  added-only, no reuse. Insert exact both sides:
  P307R block precedes (C 221439-41, block 221442;
  py CLOSED 83040, guard 83042), at dispatch tail
  (N-out-of-scope fallthrough follows: C 221659, py
  83139). Matches A-793 geometry (values re-checked
  in audit above; NO D dips: ownloop tags exactly
  the 6 P308 blocks).
- Edges own-loop ownloop416.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P308R N=124268
  off=255. edges416.py: paylens 1x84 + 347x88 (novel
  shape exact); lencode 92/92 (S/A/C/Q raw l16; S0/S1
  23/c8, 25/c8 == raw lencode) + aform 16/16 (A head
  27/c8 tail 45/c8 b5set {c8} NO step, 0 ff) + cform
  10/10 (C head 47/c8 tail 59/c8 b5set {c8} NO step,
  0 ff) + qform 64/64 + qb5flat 64/64 (Q head 5b/c8
  tail d9/c8 b5set {c8} NO step, 0 ff in 64; quad b4
  base 0x5b step2 5b..d9 == raw-lencode 64/64, NO
  edge); ring counter 256/256 + ringraw 256/256
  (head db/c8; 124031 off18 ff/c8 -> 124032 off19
  01/c9; 124159 off146 ff/c9 -> 124160 off147
  01/ca; tail off255 d9/ca; exactly 2 ff in 256 at
  o18/o146; Q tail d9/c8 vs R tail d9/ca differ in
  b5 -- labeled apart); ff total x2 (both ring).
  odd-lencode 92+256=348/348. Ring edges + tail
  124268 in for-list + 2 PASS lines each py+C. Tail
  124268: oracle sha 270259c76ad5c1db... matches
  PINS (rawlen 104 re-checked: paylen 88 + 12 + 4);
  py+C CLOSED T10P308R off=255 agree. No DISSENT:
  cut bytes verify.
- FRAG oracle leg frag416.py (staged F + MUL2 chain vs
  oracle pay[13..15] over all 64 Q Ns): ftab 16/16
  (q==0) + fmul2 48/48 (q>0, chain from code text)
  rc=0; oracle r0!=r123 triples 48/48. MUL2
  corroborated against oracle (00-case 00782d ->
  00f05a present in oracle at m7/q>0).
- PB-diff secf416.py (cache path) + secf416b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (123921 +
  123573 + 123922 + 123574); S0: oracle123921-vs-123573
  33/84, codeS0-vs-P307S0 33/84, positions identical;
  DIRECT tool 33/84 with identical agree-pos 51
  positions. S1-first84: oracle123922-vs-123574 70/84,
  codeS1-vs-P307S1 70/84, positions identical; DIRECT
  70/84 identical agree-pos 14 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (width novelty handled: S1 88B vs P307S1 84B,
  first-84 comparison + full-lens recorded 88/88/
  84/84). S1-vs-own-C10 secf416c.py (oracle C10 cells
  n123939-948): 59/88 TRUE-UNIFORM all 10 ([0]
  n123939 59/88 @ b4,6-55,64-67,84-87 == GATE staged-
  assembly count EXACT; counts [59]x10 AND positions
  identical all 10 -- verified beyond GATE's cell0
  staged assembly; sig 01000000 both, NOT byte-equal).
  Byte-diff discipline observed throughout, nothing
  to refute.
- C diff pure-add: numstat 656/0 (rgramc.c) + 265/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 651 content + 5 bare-blank / 0 del == GATE
  EXACT; raw py 265 content / 0 del. C-tempnorm
  del-uniq 0 add-uniq 460 missing 0 == GATE EXACT
  (recipe stated explicitly: rgramc.c scope,
  _tN/_iN/_bN temp-norm, empty-excluding -- no
  variant gap, b412/b414 family). Full-digit norm
  recorded (no GATE claim): C 193/186/192/185 +
  py 209 x4, del-uniq 0 missing 0 every variant
  (integrity intact). py-tempnorm 235 recorded.
- Wall on band diff added lines (scope c9b64be1..
  19dbc5e1, 984 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 656/0, rgram.py 265/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (2cda9e71), code 6 blocks,
  dispatch-exact (4-space) singletons 638->640 +2 /
  ranges 662->666 +4 py + C identical 638->640 +2 /
  662->666 +4 (C broad 643->645 +2 / 684->688 +4,
  deltas +2/+4 every series == GATE), CLOSED T10P
  prints 1736->1742 +6 py + C == GATE EXACT, seal
  1830->1836 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1836-1742 = 94, stable b401-b416):
  all agree, no slip. Broad-method cross-check: py
  648->650 +2 / 684->688 +4 (nested extras outside
  dispatch scope, standing bookkeeping).
- CONFIRM evidence (CONVERT-01 rule b): A-793-q900-P308
  verdict CONFIRM, tallies 26/26 + 22/22 + 14/14 =
  62/62 arith-consistent as-filed + exact-value
  corroboration incl PB0 NEW + PB1 88B SAME-as-C10
  59/88 NOT-byte-equal, PBA88-PLAIN sig-10 M7,
  C10-1SIG-88 M10 tail-tab, QUAD88-2SIG-MUL2 + R16
  rows + share-24ch + r123-TRUE-3B + r0-lcs0 +
  QM4-shared + F16 + mul2-chain + 00-case + b16-76 +
  M-tails NEW, T88-RING-STANDARD + TM9/TR7 16/16
  UNPAIRED + SPLIT tails + b84-87 e96a6311 + edges
  + consts db/c8/19/147 + lencode 348/348 + VPOS
  8/11/24/18 (all re-checked above). Sheet-vs-
  tables const-count note: Q-900 sheet rule 80/77/
  64/70 memo-exact (5th straight fully clean w2b
  sheet per memo; w2b-r26 [1/8]), committed tables
  79/76/63/70 still deduct const-b5 in PBA/C10/QUAD
  -- 11th consecutive tables-lag band (geometry
  exact, PORT verdict stands). No viewer P308
  geometry answer on file at gate time (memo-only
  recon; this VERIFY is the viewer record). No
  CONFIRM-P308.md file (absence verified); A-793
  suffices per rule. Agrees with cport commit msg
  (PYID 9122, RGRAM 18244).
- Quiz: no conflicting CLAIM/GATE/FLAG on b416 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites no
  QNUM (no staleness; newest PARENT at VERIFY time is
  QNUM-24, w2e Q-block refill, no gate impact).
  PROSE-01: all hex/counts above copied from own run
  output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 prose-level note ("P307 0/16" tail-contrast:
first-hand P307 M-tail4 (b80-83) == RQ-tail4 (b76-79)
16/16 -- corroborated by VERIFY-c9b64be1 SHIFT cells
(2,3),(3,4),(4,5),(5,6) -- so under the GATE's own
positional definition (TR7 b76-79 == QM b80-83) the
relation HOLDS on P307 too; the claimed 0/16 holds
only for a head-vs-tail index alignment the GATE
doesn't state; P308's 16/16 + zero off-pattern stand
first-hand, code GREEN; the novelty is the DEGREE --
4B M wholly consumed by tails, M-width 4 vs 12 -- not
the existence of tail equality). Even-band RQ==M
instance corroborated as TAIL-EQ (no ordinal per
even/odd convention; convention holds). Next-P309
predictions banked (A-793 re-read: PB0 ab689400 NEW
pay84 @124269 / PB1 01000000 pay88 @124270 /
PBA88 12000000 x16 @124271-86 -- same novel shape
continues).
