# VERIFY-6cb51277 b433 T10P325 pins 129837..130184 (348 pins) PASS

Seat viewer-r66, first-hand, tree @6cb51277,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r66.
Base 33d2c85b (b432 tip, 1932 tiers sealed; this
seat's VERIFY-33d2c85b PASS-filed same round,
base-use only, respected). Band = 8bd4aa67 (py merge
w2b@ad08ffd1 partial, +6 tiers, +62 pins) + 6cb51277
(C port, 1938 sealed). Trees manifest-identical to
tips (git ls-tree vs git ls-files cmp clean, 117/117
both; WT detached at band, will return to
lanes/encode-viewer at round end).

Banked Next-P325 shape (GATE-33d2c85b FWD-check, this
seat verified first-hand in VERIFY-33d2c85b)
CONSUMED FIRST and corroborated below:
PB0 b7ce3001 pay84 SAME-sig-as-P324PB0 (32/84 diff)
@129837 / PB1 02000000 pay88 sig-eq-P324PB1 (66/88
diff) @129838 / PBA88 21000000 x16 @129839-854 /
C10 04000000 x10 DIFFERS-from-PB1-sig @129855-864 --
all exact.

- Build: make -C tree433/src/c BUILDDIR=$R/build433
  aae rgramc (absolute NVME path, -O2 -Wall -Wextra
  -std=c11), rc=0, 0 warnings. sha256 rgramc
  05f51773 (== GATE) / aae sha1 7d8dd3a2 + sha256
  d6e27c97 pinned (== GATE both; band touches no aae
  sources per numstat).
- RGRAMC-PYID 9659/9659 covered=9659/9659 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19318/19318 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19318/19318 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 19318/19318;
  cmp433.py; GATE claims sorted only, raw corroborated
  too).
- PINS 19320 rows (2 hdr + 19318, +62 vs base 19258;
  +62 = 31 for-Ns x2); PASS-names vs PINS-names xor 0
  py+C; PINS-baseN vs for-list xor 0 (4-way set-eq,
  seteq433.py). For-list union delta vs base +31/-0
  (9628->9659):
  129837 129838 129839 129840 129846 129847 129853
  129854 129855 129856 129859 129860 129863 129864
  129865 129880 129881 129896 129897 129912 129913
  129919 129920 129928 129929 129993 130047 130048
  130175 130176 130184
  (== GATE sampled list EXACT). Decomposition first-hand
  from the added set: 2 sing (129837/38) + A head-pair
  39/40 + mids 46/47 + 53/tail 54 (6: offs 0,1,7,8,14,
  15) + C head 55/56 + mids 59/60 + 63/tail 64 (6:
  offs 0,1,4,5,8,9; offs 2,3,6,7 = 57/58/61/62
  unsampled) + Q head 65/off0 + boundary pairs 80/81
  + 96/97 + 112/113 + 12/13 + edge pair 19/20
  (offs 54/55) + tail 28 (10: offs 0,15,16,31,32,47,
  48,54,55,63; step@55 edge pair-covered + tail,
  first-hand, NEW shape) + R head 29 + mid 93 (off64,
  1-mid shape) + edge pairs 047/048 (offs 118/119) +
  175/176 (offs 246/247) + tail 184 (7: offs 0,64,
  118/119,246/247,255; both counter edges
  pair-covered, first-hand). 31x2=62 rows, range
  129837..130184 exact. PINS-new-N == for-added 31/31,
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle
  backend, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit433.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 182 PASS
  0 FAIL first run, no script fixes.
  Inventory exactly the 13 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC/F; bare F tab, 1 frag
  position b34, dual-ADD; no FT34, no F0/F1, no BM/BC,
  no M19/X19, no QB/PT/FM, no M42/X42/H42/L42, no
  RT/TT, no QT).
  S0 168ch sig b7ce3001 SAME-sig-as-P324PB0 (32/84
  payload diff vs P324S0 @ b4-11,34,35,41-48,50-55,
  76-83 first-hand, NOT byte-equal) / S1 176ch sig
  02000000 sig-eq-P324PB1 (66/88 payload diff vs
  P324S1 @ b4-14,16-27,36-38,40-43,48-55,60-87, NOT
  byte-equal; sig DIFFERS-from-own-C10 02-vs-04; [26]
  x10 vs own C10 assembled, NOT byte-equal),
  staged as full-payload singletons.
  AM 16/16 12ch (6B) distinct, CM 10/10 10ch (5B)
  diverge (b28 {a0,a1} first byte first-hand), M
  16/16 18ch (9B) distinct, QR 4/4 22ch (11B)
  distinct UNPAIRED, F 16/16 2ch (1B) distinct
  {0c,4c,8c,cc} (8cx8/4cx4/ccx3/0cx1 ordered
  8c,0c,4c,8c,cc,4c,8c,cc,8c,4c,8c,4c,8c,8c,cc,8c),
  RM 16/16 14ch (7B) distinct, RQ 16/16 20ch (10B)
  distinct UNPAIRED, no QT + no RT (ring STANDARD
  tails) + FRAG-b34 (dual-ADD, below).
  AC 80, b0-3 21000000 (b0 const 21), no b4/b5.
  C10-1SIG-88-DIFFSIG-M5b28 sig 04000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM
  10/10 diverge, b28 {a0,a1}; CC has no b4/b5, b5
  const f6 full block via lencode).
  S1-vs-own-C10 staged per-cell (M5 b28,84-87, b4/b5
  lencode, each cell own assembly) [26]x10
  TRUE-UNIFORM count+position (cell0 26 @
  0,4,17-19,22-28,30-35,64-67,84-87 EXACT incl
  DIFFSIG b0; positions identical all 10 staged AND
  oracle; sig 02000000-vs-04000000 DIFFSIG, NOT
  byte-equal -- 20th TRUE-uniform case on record, 19th
  excluding unverified P299; beyond-GATE values
  corroborated by oracle leg below).
  QUAD88-3SIG-4R-FRAG 41x32 rows0-1 + 4c x16 row2 +
  78 x16 row3 (b0 row-led 41/41/4c/78 in R lanes, QC
  b0-absent, b1-3 const 00 in QC; b5 edge f6->f7
  @off54/55, edge 129919 ff/f6 -> 129920 01/f7;
  QM9 b29-31,35,36,80-83 16/16 distinct NO frags +
  R11 b0,11,19,26,27,32,33,84-87 rows 4/4 NO pairing
  pairwise-disjoint: r0/r1 share 7B prefix
  419745a1fcca66, differ in 8th byte b84 (66 vs d1);
  r2/r3 full tuples unequal, fully distinct;
  tails b84-87 4/4 distinct 6671c43e/d126f13e/
  2de926a7/9cd4aea9, r01 pair-only-1B 0x3e @b87,
  b87 NOT const quad-wide [3e,3e,a7,a9];
  suffix-LCS r01=1 rest 0; subsequence-LCS (01)=1
  (12)=1 rest 0 (shared 0x26); GATE "TAIL4-LCS
  (01)=1 (12)=1" mixes suffix ((01)) and subsequence
  ((12)) conventions -- mild prose note, both computed
  first-hand; full-LCS 01=8/02=1/12=2 rest 0, all
  recorded first-hand);
  FRAG b34 dual-ADD second-of-class verified triple
  first-hand: tab16 ordered (8c,0c,4c,8c,cc,4c,8c,cc,
  8c,4c,8c,4c,8c,8c,cc,8c; 4 distinct {0c,4c,8c,cc},
  8cx8/4cx4/ccx3/0cx1) + oracle pay34 over all 64 Q
  Ns: q<=1 rows == F[m] 32/32, q==2 rows == F[m]+0xfe
  16/16 (set {0a,4a,8a,ca}), q==3 rows == F[m]+0xf6
  16/16 (set {02,42,82,c2}); C legs _T10P325F[m] +
  254/246 (&255) exact; memo "all 48 cells" =
  F-tab16 + r2 + r3 (r01 uses the same tab, 32 cells
  covered); M-tails 16/16 ALL NEW vs P324T (zero
  overlap vs P324M AND vs P324RM-tail8 AND vs
  P324RQ-tail8).
  Ring STANDARD-split: sig 72040000 x256; TM7
  b40-42,80-83 by COL RM 16/16 + TR10 b29-31,34-36,
  76-79 by ROW RQ 16/16 UNPAIRED (tails SPLIT b80-83
  col / b76-79 row); b0 const 72; b84-87 f0952aad
  ring-wide NEW.
  M==RQ HEADS4+TAILS4: M 9B b29-31,35,36,80-83 vs RQ
  10B b29-31,34-36,76-79: agree (0,0),(1,1),(3,4),
  (4,5),(5,6),(6,7),(7,8),(8,9) 16/16 each; heads
  b29,30,35,36 shared-lane agree; tails b80-83
  cross-lane agree b76-79; RQ rows embed M rows +2
  bytes (b31/b34); M2=b31 isolated maxagree 0 both
  sides (full row all 0); RQ b34 isolated maxagree 0
  both sides (full col all 0); noise singles (4,9)=1
  + (8,5)=1 recorded; tabs differ -- widths 9B/10B,
  full-row sets disjoint. FIRST HEADS4+TAILS4 degree
  instance. 34th odd-band RQ==M instance (viewer chain
  b421-28th FULL7/b423-29th TAILS4-ONLY/b425-30th
  TAILS4-ONLY/b427-31st FULL6/b429-32nd FULL7/b431-
  33rd TAILS4-ONLY/b433-34th HEADS4+TAILS4
  sequential). Memo-silent on the relation.
  Sorted-unique + _N decls 80/81/65/69 match actual.
  Missing-sets EXACT: AC-8 [4,5,28,29,80-83] = b4,b5+
  M6 / CC-7 [4,5,28,84-87] = b4,b5+M5 (full sig b0-3
  in CC = 04,00,00,00 -> 04000000 x10 DIFFERS-from-
  PB1-sig) / QC-23 [0,4,5,11,19,26,27,29-36,80-87] =
  b0,b4,b5+QM9+R11+F1 (b0 in R lanes row-led, b1-3
  const 00 in QC) / RC-19 [4,5,29-31,34-36,40-42,
  76-83] = b4,b5+TR10+TM7. VPOS 7/6/23/19 == A-835
  EXACT (PBA b4+M6 (b5 const deducted) / C10 b4+M5 /
  quad b0,b4,b5+QM9+R11+F1 (b0 shared) / T b4,b5+
  TM7+TR10). Coverage unions exact every block
  (const U tab U {b4,b5} == 88 x4, 0 overlap); each
  missing == region pay-index set minus {b4,b5} EXACT
  all 4 (A/C/Q/R region text re-derived first-hand,
  tab == region-idx minus {b4,b5} EXACT).
  Q legs M[m] + QR[q] + F[m]-scalar/ADD both sides, NO
  F-row leg in Q; R legs RM[c] + RQ[r] both sides, NO
  F anywhere in R (STANDARD RM-col / RQ-row verified
  in region text both sides). RM 16/16 distinct + RQ
  16/16 distinct, sets disjoint.
  P324 refs re-read: S0 b7ce3001 / S1 02000000 /
  PBA 29000000 / C10 02000000 / QUAD 1SIG 26 (QC b0
  const) / T ring 2SIG-B0ROW (b0 row-led).
  PBA sig 21 NEW vs P324 29 (21000000 != 29000000);
  QUAD 3SIG 41/4c/78 vs P324 1SIG 26 (rows NEW,
  3-sig novelty; R11 continues). AM/CM/M/QR/RM/RQ
  0-overlap vs P324; F NEW this tier (no T10P324F in
  base). Memo INCL PBA 81 / C10 82 / quad 65 / T88 69
  (A-835 re-read): impl 80/81/65/69 = b5 const
  counted on PBA/C10 (b5 covered by lencode),
  quad b5 STEP counted in VPOS, T b5 counter counted
  -- INCL arithmetic exact, geometry exact, PORT
  verdict stands; memo-exact on T88 (b5 counter, no
  deduction). 28th consecutive tables-lag band (b433
  pattern +1/+1/+0/+0; running b412-b432 per GATE +
  r64/r65/r66 records).
  Base temp maxes _t6650/_b4023/_i4024 (no reuse:
  band adds _t6651-6668 continuous-18 + _b4025/27/29/
  30/32/33 + _i4026/28/31/34, whole-file max _t6668,
  all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 129837 / S1 129838 / A 129839-854 / C 129855-864 /
  Q 129865-928 / R 129929-130184): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C/Q both sides
  (A b5 const f6, C b5 const f6, Q b5=f6+(off>=55)
  emerge from raw lencode, NO step in A/C; Q uses raw
  lencode, no counter literals) + R explicit counter
  (b4=(0x13+2off)&FF b5=0xf7+(off>=119)+(off>=247); py
  hex 0x13/0xf7; C staged literals 19/247,
  re-derived: 19==0x13, 247==0xf7) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/rtab byte
  positions exact (A M6 b28,29,80-83 + b5 const; C M5
  b28,84-87; Q QM9 b29-31,35,36,80-83 + R11 b0,11,19,
  26,27,32,33,84-87 + F1 b34; R TM7 b40-42,80-83 by
  COL + TR10 b29-31,34-36,76-79 by ROW, tails SPLIT)
  + C guards `if ((n) == (129837))` / `(129838)` + 4
  range guards exact + counter literals exact + C
  byte-index lists match py per block (A 6B, C 5B,
  Q 9B/11B/1B, R 7B/10B STANDARD tails-split) + FRAG
  dual-ADD hexval(F[m])+254 / hexval(F[m])+246 (&255)
  exact (C strcpy _t6664 from _T10P325F[m]). C blocks
  carry T87231/87236/87241/87256/87271/87300 py-line
  mirrors (all 6 re-read verbatim against the py guard
  lines above); bounds + byte positions exact (A 6B,
  C 5B, Q 9B/11B/1B, R 7B/10B). Insert exact both
  sides: after T10P324R close (py CLOSED-then-guard;
  C block follows P324R close @232098), at dispatch
  tail (N-out-of-scope fallthrough follows; 2 scope
  hits py + 2 scope hits C). Matches A-835 geometry
  (values re-checked in audit above; NO D dips:
  ownloop tags exactly the 6 P325 blocks).
- Edges own-loop ownloop433.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc): 348/348 CLOSED
  rc=0 (249 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P325R N=130184
  off=255. edges433.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  5b/f6, 5d/f6 == raw lencode) + aform 16/16 (A head
  5f/f6 tail 7d/f6 b5set {f6} NO step, 0 ff) + cform
  10/10 (C head 7f/f6 tail 91/f6 b5set {f6} NO step,
  0 ff) + qform 64/64 + qb5 64/64 (Q head 93/f6 edge
  off54->55 129919 ff/f6 -> 129920 01/f7 tail 11/f7
  b5set {f6,f7}, exactly 1 ff in 64, b5=f6+(off>=55)
  verified; quad b4=(0x93+2off) 64/64 range
  93..ff,01..11) + ring counter 256/256 + ringraw
  256/256 (head 13/f7; mid off64 93/f7 @129993; edge
  off118->119 130047 ff/f7 -> 130048 01/f8; edge
  off246->247 130175 ff/f8 -> 130176 01/f9; tail
  off255 11/f9; exactly 2 ff in 256). S0/S1 embedded
  b4/b5 (5b/f6, 5d/f6) match raw lencode.
  Odd-lencode 348/348 (346 + S0/S1 embedded). Ring
  edges + mid + tail 130184 in for-list + 2 PASS lines
  each py+C. Tail 130184: oracle rav sha
  6c4896d0fcc8006a == PINS (== GATE prefix EXACT;
  rawlen 104 re-checked: paylen 88 + 12 + 4); py+C
  CLOSED T10P325R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf433.py (cache path, 0 miss-warmed after
  ownloop) + secf433b.py (DIRECT tool, no cache):
  staged-vs-oracle 0/0/0/0 (129837 + 129489 + 129838 +
  129490); S0: oracle129837-vs-129489 32/84,
  codeS0-vs-P324S0 32/84, positions identical
  (differ-pos 4-11,34,35,41-48,50-55,76-83 listed);
  DIRECT 32/84 agree. S1: oracle129838-vs-129490
  66/88, codeS1-vs-P324S1 66/88, positions identical;
  DIRECT 66/88 agree. Triple-derived both pairs
  (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88).
  S1-vs-own-C10 secf433c.py (oracle C10 cells n129855-
  864): [26]x10 TRUE-UNIFORM counts AND positions
  identical all 10 (cell0 pos 0,4,17-19,22-28,30-35,
  64-67,84-87 == staged EXACT; sig 02000000-vs-
  04000000 DIFFSIG, NOT byte-equal). Byte-diff
  discipline observed throughout.
- C diff pure-add: numstat 644/0 (rgramc.c) + 258/0
  (rgram.py) + 1/1 (for-line) + PINS +62/+0 (clean
  append, 31 Ns x2) == GATE; raw C 644 total = 639
  content + 5 bare-blank / 0 del (verified bare `+`
  lines; GATE states "644 content + 5 blank" which
  sums 649 vs numstat 644 -- mild overcount-by-5,
  3rd instance of the token after b429/b431 GATEs,
  same class; first-hand 639+5=644; full-digit norm
  ([0-9]+ -> N): C del-uniq 0 add-uniq
  172/166/171/165 across the 4 strip/dropempty
  variants (165 = strip+dropempty, as cited), missing
  0 every variant; py del-uniq 0 add-uniq 192/191/
  192/191 (191 = strip+dropempty variants, as cited),
  missing 0 (integrity intact, variant-robust);
  C-tempnorm 415 / py-tempnorm 217 recorded.
  Band-level sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope 33d2c85b..
  6cb51277, 965 added lines == GATE): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files: rgramc.c 644/0, rgram.py 258/0 purely
  additive, test_rgram.sh 1/1 (for-line), PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks,
  tier-comments `# T10P` 1838->1844 +6, singletons
  `if n == ` 682->684 +2 / range-guards `<= n <=`
  752->756 +4 = +6 py; C guards: singleton
  `if ((n) == (` 677->679 +2 / range 752->756 +4
  (5-count C-vs-py singleton offset pre-existing,
  unchanged: 684-679 = 682-677 = 5), CLOSED T10P
  prints 1838->1844 +6 py + 1838->1844 +6 C (seal
  1932->1938 +6; offset +94 vs CLOSED-T10P: 1938-1844
  = 94, stable b401-b433). All agree (stated literal
  methods first-hand; no method-mix this band).
  Deliberate structural add: py elif 48->50 (+2 =
  the FRAG q-branch `elif q == 2:` + `elif
  pay[34]...0xF6...` in T10P325Q region, verified
  located @87290/87293);
  C else-if 0->0 (C uses separate ifs).
- CONFIRM evidence (CONVERT-01 rule b): A-835-q917
  memo CONFIRM 69/70 + section-F (r1/r2 share 0x26)
  (own bed r3-P325 129837..130216 BAD=0 + own r3-P324,
  verifier v221.py 69/70 PASS, single FAIL = Q-claim
  witness; file present, counts verified; exact-value
  corroboration incl PB0 SAME-sig-b7ce3001 32/84,
  PB1 sig-eq-P324PB1 66/88 DIFFERS-from-own-C10
  02-vs-04 26/88, PBA88-PLAIN-M6 sig-21 M6, C10-
  DIFFSIG-M5b28 DIFFERS-from-PB1-sig b28-{a0,a1},
  QUAD88-3SIG-4R-FRAG rows-41/4c/78 + R11 rows +
  r01-share-7B + r01-paironly-3e + b87-[3e,3e,a7,a9]
  + suffix-(01)-1/subseq-(12)-1 + QM9 + FRAG-b34
  dual-ADD sets + M-tails NEW, T88-RING-STANDARD +
  TM7/TR10 + SPLIT tails + b84-87 f0952aad + edges +
  consts; plus sheet-vs-tables const-count note: Q-917
  sheet 81/82/65/69 memo-exact, committed tables
  80/81/65/69 -- INCL arithmetic exact (b5 const
  counted on PBA/C10), geometry exact, PORT verdict
  stands; plus section-F: r1/r2 share byte 0x26
  (subsequence-LCS 1, suffix-LCS 0) with other pairs
  suffix-0, comment-gloss only, bytes unaffected).
  Agrees with cport commit msg (PYID 9659, RGRAM
  19318). No viewer P325 geometry answer on file at
  gate time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b433 (own
  seat CLAIM only; exactly 1 GATE-6cb51277; zero FLAG
  hits; odd base b432 respected; b434 = sweep2 turf
  untouched, used as nothing here). PROSE-01: all
  hex/counts above copied from own run output; GATE-
  6cb51277 re-read in FULL before filing (2 mild prose
  notes below, substance exact).
- RQ==M chain: b433 odd HEADS4+TAILS4 FIRST degree
  (M 9B vs RQ 10B; agree (0,0),(1,1),(3,4),(4,5),(5,6),
  (6,7),(7,8),(8,9) 16/16; M2 noise-free isolated; RQ
  b34 isolated; noise singles (4,9),(8,5)).
  34th odd-band instance (viewer chain b421-28th FULL7/
  b423-29th TAILS4-ONLY/b425-30th TAILS4-ONLY/b427-31st
  FULL6/b429-32nd FULL7/b431-33rd TAILS4-ONLY/b433-34th
  HEADS4+TAILS4 sequential); 1st HEADS4+TAILS4 degree
  instance. Memo-silent on the relation.
- TRUE-uniform chain: 20th case (19th excl P299):
  P325 S1-vs-C10 [26/88]x10 staged+oracle NEW this
  band (GATE/memo cell0-only; beyond-GATE finding,
  code GREEN since gated artifact == verified
  artifact).

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 mild prose-level notes (raw-C content overcount
by 5: "644 content + 5 blank" sums 649 vs numstat 644;
first-hand 644 total = 639 content + 5 bare-blank --
same token as b429/b431 GATEs; TAIL4-LCS token mixes
suffix ((01)) and subsequence ((12)) conventions, both
computed first-hand; code GREEN since gated artifact ==
verified artifact).
