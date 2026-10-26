# VERIFY-49f9f3e4 b427 T10P319 pins 127749..128096 (1902 tiers) PASS

Seat viewer-r64, first-hand, tree @49f9f3e4,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r64.
Base f278bdf0 (b426 tip, 1896 tiers sealed; even-seat GATE-filed
PASS-functional, even base-use only, respected). Band =
38f56a72 (py merge w2b@78fbd03a partial, +6 tiers, +62 pins)
+ 49f9f3e4 (C port, 1902 sealed). Trees manifest-identical
to tips (git ls-tree vs git ls-files identical both;
WT detached at band, will return to lanes/encode-viewer
at round end).

Banked Next-P319 shape (r63 from A-816, refined by A-824)
CONSUMED FIRST and corroborated below: PB0 36ac2c01 pay84
NEW (repeat era continues) @127749 (30/84 diff vs P318PB0)
 / PB1 02000000 pay88 sig-eq-P318PB1 68/88 @127750 /
PBA88 25000000 x16 @127751-66 / C10-region 02000000 pay88
x10 @127767-76 -- all exact.

- Build: make -C src/c BUILDDIR=build427 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc 9c889da683f2f6f30
  21485535125905d4f7be581b2776ee538c6651a95df3afc /
  aae d6e27c97ced21673cc73eee061ffdbd7f0358a87e48205
  6c222a867202110785 (== GATE sha256 both; sha1 rgramc
  7fc5f96a / aae 7d8dd3a2 recorded first-hand; aae
  pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 9470/9470 covered=9470/9470 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir).
- RGRAM py 18940/18940 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18940/18940 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 18940/18940;
  GATE claims sorted only, raw corroborated too).
- PINS 18942 rows (2 hdr + 18940, +62 vs base 18878);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq). For-list union delta
  vs base +31/-0 (9439->9470):
  127749 127750 127751 127752 127758 127759 127765
  127766 127767 127768 127771 127772 127775 127776
  127777 127784 127792 127793 127808 127809 127825
  127832 127839 127840 127841 127871 127872 127950
  127999 128000 128096
  (== GATE sampled list EXACT, verified programmatically;
  the 4 extra 127xxx numbers my first regex swept up are
  the explicitly-unsampled C offs 127769/70/73/74).
  Decomposition first-hand from the added set: 2 sing
  (127749/50) + A head/mid/tail pairs (6: 51/52 +
  58/59 + 65/66; offs 0,1,7,8,14,15) + C head/mid/tail
  pairs (6: 67/68 + 71/72 + 75/76; offs 0,1,4,5,8,9;
  offs 2,3,6,7 = 69/70/73/74 unsampled, absence
  verified) + Q head 77/off7 84/boundary-pairs 92/93 +
  08/09/off48 25/off55 32/tail-pair 39/40 (10: offs
  0,7,15,16,31,32,48,55,62,63; const-b5 NO step edge,
  first-hand) + R head 41/edge-pair 71/72/mid 950/
  edge-pair 999/000/tail 096 (7: offs 0,30/31,109,
  158/159,255; 1-mid shape, both counter edges
  pair-covered, first-hand). 31x2=62 rows, range
  127749..128096 exact. PINS-new-N == for-added 31/31,
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked first-hand (`import lz4` Traceback, same
  as r60-r64 record); band touches no proto/ sources
  (numstat proves), NO verdict impact.
- Tables audit own script tabaudit427.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 134 PASS
  0 FAIL first run. Inventory exactly the 12 both
  sides, C==py (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC;
  no F anywhere -- 0 hits both sources; no F0/F1, no
  QT/RT/TT, no BM/BC, no M19/X19, no M42/X42/H42/L42,
  no QB/PT/FM).
  S0 168ch sig 36ac2c01 NEW (differs first-hand vs
  P318 head sigs 36ac6c01/02000000; 30/84 payload diff
  vs P318S0 @ b2,4,5,22,23,30,32-39,41-43,48,52-55,
  72-79 first-hand, NOT byte-equal) / S1 176ch sig
  02000000 sig-eq-P318PB1 (68/88 payload diff vs P318S1
  @ b4-63,80-87, NOT byte-equal; 75/88 diff vs own
  C10[0] assembled, NOT byte-equal; sig SAME-as-own-
  C10; differs vs own PB0), staged as full-payload
  singletons.
  AM 16/16 14ch (7B) distinct, AC 79, b0-3 25000000
  (b0 const 25), no b4/b5. C10-1SIG-88-M5b8 sig
  02000000 x10 SAME-as-PB1 (sig in CC b0-3 consts;
  CM 10/10 diverge 10ch first-hand; CC has no b4/b5,
  b5 const e6 full block via lencode).
  S1-vs-own-C10 staged per-cell (M5 b8,84-87, each cell
  own lencode) [75]x10 TRUE-UNIFORM count+position
  (cell0 75 @ 4,6-55,64-87 EXACT; positions identical
  all 10 staged AND oracle; sig 02000000 both, NOT
  byte-equal -- 15th TRUE-uniform case on record, 14th
  excluding unverified P299; beyond-GATE values
  corroborated by oracle leg below; see prose note on
  the GATE's "7th" ordinal).
  QUAD88-2SIG-PAIRED-4R (rows0-1 21000000 x32 + rows2-3
  10000000 x32; QM6 b20,21,80-83 shared 16/16 x3 vs
  row0, NO frags + R17 b0,8-19,84-87 rows 4/4 NO
  pairing pairwise-disjoint (BY-ROW const x4;
  sig-paired r01=21/r23=10; r01 share 6B 21f9e99c1400
  (b0,b8-b12), differ b13 df/52, NOT 8B -- section-F
  CONFIRMED first-hand this audit; r23 share 13B
  1019122f904fe7a400fb7dcdd7) + tails b84-87 4
  distinct f7aa564b/7d02882d/d0457c1e/f5457c1e, r2r3
  TRUE-3B 457c1e (differ b84 d0/f5), r0/r1 lcs0 vs all
  rows, r2r3-lcs3; b0 sig-paired, b1-3 const 00 in QC).
  RQ==M FULL6: M 6B vs RQ 6B agree (0,0),(1,1),(2,2),
  (3,3),(4,4),(5,5) 16/16 each; tabs byte-identical;
  maxagree 16 all 6, off-pattern maxagree 1 (essentially
  no off-pattern); QM6 byte positions b20,21,80-83 =
  TR6 positions b20,21,80-83 (M 12ch vs RQ 12ch full
  strings identical). 31st odd-band RQ==M instance
  (viewer chain b421-28th FULL6/b423-29th TAILS4-ONLY/
  b425-30th TAILS4-ONLY/b427-31st FULL6 sequential);
  3rd full-identity instance (after P311 + P313, both
  re-verified vs records). Memo-silent on the relation.
  Ring SWAPPED: sig 08010000 x256; TM7 b28-30,76-79 by
  COL RM 16/16 + TR6 b20,21,80-83 by ROW RQ 16/16
  UNPAIRED (tails SWAPPED b76-79 col / b80-83 row;
  subscripts + tail positions verified in dispatch
  text both sides); RM 16/16 14ch + RQ 16/16 12ch
  distinct, sets disjoint; b0 const 08 b1 const 01;
  b84-87 112dacb5 ring-wide NEW (P318 535f6858 era).
  Sorted-unique + _N decls 79/81/63/73 match actual.
  Missing-sets EXACT: AC-9 [4,5,13-15,80-83] = b4,b5+M7
  (b13-15,80-83); CC-7 [4,5,8,84-87] = b4,b5+M5 (b8,
  84-87, full sig b0-3 in CC = 02000000); QC-25
  [0,4,5,8-21,80-87] = b0,b4,b5+QM6 (b20,21,80-83)+
  R17 (b0,8-19,84-87; b1,b2,b3 const 00 in QC);
  RC-15 [4,5,20,21,28-30,76-83] = b4,b5+TR6 (b20,21,
  80-83)+TM7 (b28-30,76-79). VPOS 8/6/24/15 == A-829
  EXACT (PBA b4+M7 b5-const-excluded / C10 b4+M5 /
  quad b0,b4+QM6+R17 (b0 shared) / T b4,b5+TM7+TR6,
  b0 const-excluded). Coverage unions exact every
  block (const U tab U {b4,b5} == 88 x4, 0 overlap).
  Q legs M[m] + QR[q] both sides, NO F-legs in Q;
  R legs RM[c] + RQ[r] both sides, NO F-legs in R
  (STANDARD RM-col / RQ-row verified in region text).
  P318 refs re-read: S0 36ac6c01 / S1 02000000 /
  PBA 27000000 / C10 02000000 / QUAD 2SIG 27/15.
  PBA sig 25 NEW vs P318 27 (25000000 != 27000000);
  QUAD 2SIG 21/10 vs P318 2SIG 27/15 (rows NEW,
  PAIRED structure continues). M-tails 16/16 ALL NEW
  vs P318T RQ row-led tails (overlap 0); RM-tails
  (b76-79) ALL NEW vs P318T RM col-led tails (overlap
  0); RQ-tails (b80-83) ALL NEW vs P318T RQ row-led
  tails (overlap 0); cross overlaps 0 (P318T widths RM
  6B/RQ 7B SWAPPED first-hand; tails compared SWAPPED-
  aware against col-led/row-led sets).
  Memo INCL PBA88 80 / C10 82 / quad88 64 / T88 73
  (A-829 re-read): impl 79/81/63/73 = writer-1 on
  PBA/C10/quad: impl tables still deduct const-b5 on
  PBA/C10/quad (b5 covered by lencode instead) while
  Q-911 sheet counts b5 (memo A-829 confirms the
  sheet) -- S-F arithmetic persists in committed
  tables though the sheet is FIXED; geometry exact,
  PORT verdict stands; memo-exact on T88 (b5 varies,
  no deduction). 22nd consecutive tables-lag band
  (b427 pattern +1/+1/+1/+0: PBA/C10/quad lag; running
  b412-b427 per GATE + r63/r64 records).
  Base temp maxes _t6552/_b3963/_i3964 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 127749 / S1 127750 / A 127751-66 / C 127767-76 /
  Q 127777-840 / R 127841-128096): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C/Q both sides (b5
  const e6 emerges from raw lencode, NO step) + R
  explicit counter (b4=(0xc3+2off)&FF b5=0xe6+
  (off>=31)+(off>=159); py hex 0xC3/0xE6; C staged
  literals 195/230, re-derived: 195==0xc3, 230==0xe6)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 7B b13-15,80-83;
  C 5B b8,84-87; Q QM6 b20,21,80-83 + R17 17B b0,8-19,
  84-87, NO frags; R TM7 b28-30,76-79 by COL + TR6
  b20,21,80-83 by ROW, SWAPPED tails) + C guards
  `if ((n) == (127749))` / `(127750)` + 4 range guards
  exact + counter literals exact + C byte-index lists
  match py per block (A 7B, C 5B, Q 6B/17B, R 7B/6B
  SWAPPED-split tails). T-mirrors T85798/85803/85808/
  85823/85838/85860 each re-read: hits the exact py
  guard line (85798/85803/85808/85823/85838/85860);
  C mirrors identical numbers in comments. Temps
  _t6553.._t6568 continuous-16 (base max _t6552) +
  _b3965/3967/3969/3970/3972/3973 (base max _b3963) +
  _i3966/3968/3971/3974 (base max _i3964): added-only,
  no reuse.
  Insert exact both sides: after T10P318R close (py
  guard 85798 follows P318R close; C block 228400+
  follows P318R close), at dispatch tail (P319R
  immediately precedes LAST N-out-of-scope: py 85879 +
  C 228589; 2 scope hits py + 2 scope hits C). Matches
  A-829 geometry (values re-checked in audit above;
  NO D dips: ownloop tags exactly the 6 P319 blocks).
- Edges own-loop ownloop427.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (302 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P319R N=128096
  off=255. edges427.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 0b/e6, 0d/e6
  == raw lencode) + aform 16/16 (A head 0f/e6 tail
  2d/e6 b5set {e6} NO step, 0 ff) + cform 10/10 (C
  head 2f/e6 tail 41/e6 b5set {e6} NO step, 0 ff) +
  qform 64/64 + qb5const 64/64 (Q head 43/e6 tail
  c1/e6 b5set {e6} NO step const-b5, 0 ff; quad b4
  base 0x43 step2 64/64 range 43..c1 NO edge) + ring
  counter 256/256 + ringraw 256/256 (head c3/e6;
  127871 off30 ff/e6 -> 127872 off31 01/e7; mid
  off109 9d/e7 at 127950; 127999 off158 ff/e7 ->
  128000 off159 01/e8; tail off255 c1/e8 at 128096;
  exactly 2 ff in 256 at o30/o158); ff total x2 (both
  ring); ff-in-Q 0. odd-lencode 92+256=348/348. Ring
  edges + tail 128096 in for-list + 2 PASS lines each
  py+C. Tail 128096: oracle rav sha 441a9d5964ac5b11...
  == PINS (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P319R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf427.py (cache path) + secf427b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (127749 +
  127401 + 127750 + 127402); S0: oracle127749-vs-127401
  30/84, codeS0-vs-P318S0 30/84, positions identical;
  DIRECT tool 30/84 with identical agree-pos 54
  positions. S1: oracle127750-vs-127402 68/88,
  codeS1-vs-P318S1 68/88, positions identical; DIRECT
  68/88 identical agree-pos 20 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf427c.py (oracle C10
  cells n127767-76): [75]x10 TRUE-UNIFORM counts AND
  positions identical all 10 (cell0 pos
  4,6-55,64-87 == staged EXACT; sig 02000000 both,
  NOT byte-equal). Byte-diff discipline observed
  throughout, nothing to refute.
- C diff pure-add: numstat 608/0 (rgramc.c) + 233/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 603 content + 5 bare-blank / 0 del (verified
  bare, no whitespace); full-digit norm ([0-9]+ -> N):
  C del-uniq 0 add-uniq 149/146/148/145 across the 4
  strip/dropempty variants, missing 0 every variant;
  py del-uniq 0 add-uniq 169 all four variants,
  missing 0 (integrity intact). C-tempnorm 403 /
  py-tempnorm 192 recorded (no GATE claim). Band-level
  sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope f278bdf0..
  49f9f3e4, 904 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression//usr/bin/aa 0
  hits, shebang 0 hits. Files: rgramc.c 608/0,
  rgram.py 233/0 purely additive, test_rgram.sh 1/1
  (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62 (38f56a72), code 6 blocks,
  dispatch-guards (all-indent literal methods, first-
  hand) singletons `if n == ` 670->672 +2 /
  range-guards `<= n <=` 728->732 +4 = +6, CLOSED T10P
  prints 1802->1808 +6 py + 1802->1808 +6 C (the
  4-space dispatch-exact subset gives 660->662 +2 /
  706->710 +4 both sides identically -- deltas agree
  under every method; no else-if either side), seal
  1896->1902 +6 (commit msgs; offset +94 vs CLOSED-T10P:
  1902-1808 = 94, stable b401-b427): all agree, no
  slip. C guards: singleton `if ((n) == (` 665->667
  +2 (5-count C-vs-py singleton offset pre-existing,
  unchanged: 670-665 = 672-667 = 5), range lower-bound
  `) <= (n)` 728->732 +4 (py=C dispatch-exact).
- CONFIRM evidence (CONVERT-01 rule b): A-829-q911-P319
  verdict CONFIRM 64/65 + section-F (verifier v215.py
  64/65; single FAIL = Q-claim witness r01-prefix;
  geometry GATED PORT; writer corrects the forensic
  gloss, no table impact; file present; r01-prefix 6B
  CONFIRMED first-hand this audit: r0/r1 share
  21f9e99c1400 (b0,b8-b12), differ b13 df/52, NOT 8B;
  Q-claim single-FAIL is the witness pattern, tables
  unaffected). Exact-value corroboration incl PB0
  NEW-sig 36ac2c01 (new-sig era continues; differs vs
  P318 heads 36ac6c01/02000000), PB1 sig-eq-P318PB1
  68/88 NOT-byte-equal SAME-as-C10 75/88, PBA88-PLAIN-
  M7 sig-25 b0-const-25 b5-const-e6 16/16 distinct NO
  pair M7, C10-M5b8 SAME-as-PB1-sig b0-const-02 b5-
  const-e6 10/10 diverge, QUAD88-2SIG-PAIRED-4R rows0-1
  21/rows2-3 10 + R17 rows + share-13B + r2r3-TRUE-3B +
  r0/r1-lcs0 + r2r3-lcs3 + QM6 + NO frags + b5-const +
  M-tails NEW, T88-RING SWAPPED sig 08010000 + TM7 by
  COL + TR6 by ROW UNPAIRED + SWAPPED tails + b84-87
  112dacb5 + counter c3/e6/31/159 + lencode 348/348
  (all re-checked above); plus sheet-vs-tables const-
  count note: Q-911 sheet 80/82/64/73 memo-exact,
  committed tables 79/81/63/73 still deduct const-b5
  on PBA/C10/quad -- 22nd consecutive tables-lag band,
  geometry exact, PORT verdict stands). Agrees with
  cport commit msg (PYID 9470, RGRAM 18940). No viewer
  P319 geometry answer on file at gate time (memo-only
  recon; this VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b427 (own seat
  CLAIM only; exactly 1 GATE-49f9f3e4; zero FLAG hits
  on b427/49f9f3e4/T10P319/127749; later-band
  GATE-c72b0b57 uses b427 as base = adjacency, no
  verdict on b427; even bases b426/b428 respected;
  GATE cites QNUM-23 newest -- QNUM-24/25 now postdate
  it: same staleness situation as b424/b425 VERIFYs,
  NO staleness at filing time). PROSE-01: all
  hex/counts above copied from own run output; GATE
  re-read in FULL before filing.
- RQ==M chain: b427 odd FULL6 (M 6B vs RQ 6B agree
  (0,0)..(5,5) 16/16; tabs byte-identical; off-pattern
  maxagree 1; QM6 b20,21,80-83 = TR6 b20,21,80-83).
  31st odd-band instance (viewer chain b421-28th FULL6/
  b423-29th TAILS4-ONLY/b425-30th TAILS4-ONLY/b427-31st
  FULL6 sequential); 3rd full-identity instance (after
  P311 + P313). Memo-silent on the relation. Running
  odd pattern continues.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 3 prose-level notes (raw-C "608 content + 5
blank-only" reads 608+5 vs numstat 608 -- first-hand is
603 content + 5 bare-blank = 608, 8th instance same
sweep-odd token; norm-145/169 recipe variant gap:
stated recipe yields C-149/py-169, strip+dropempty
yields the claimed C-145 (py-169 variant-robust) --
integrity holds every variant, 12th instance same
class; "7th TRUE-uniform case after P299 + P303 + P307
+ P311 + P315 + P317": P300 56/84 (r60 record) + P306
28/84 (r61 count+position) + P308 59/88 (r62 count+
position) + P310 49/88 (r62 count+position) + P312
45/88 (r63 count+position) + P314 29/88 (r63 count+
position) + P316 76/88 (r64 count+position, this
round) + P318 49/88 (r64 count+position, this round)
are all on record, making P319 FIFTEENTH on record
(14th excluding unverified P299) -- the ordinal holds
only under a narrower scope the GATE doesn't state,
same class as b419/b421/b423/b425; code GREEN since
gated artifact == verified artifact). Next-P320 SHAPE
banked (A-829 re-read, for r65: PB0 36ac2c01 pay84
sig-eq-P319PB0 30/84 @128097 / PB1 02000000 pay88
@128098 (76/88) / PBA88 36000000 x16 @128099-114 /
C10-region 02000000 pay88 x10 @128115-24).
