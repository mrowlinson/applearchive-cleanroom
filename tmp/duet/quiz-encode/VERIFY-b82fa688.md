# VERIFY-b82fa688 b442 T10P334 pins 132969..133316 (348 pins) PASS

Seat viewer-r68, first-hand, tree @b82fa688,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r68.
Base 18016e8a (b441 tip, 1986 tiers sealed; this
seat's VERIFY-18016e8a PASS-filed same round,
base-use only, respected). Band = 88a5b299 (py
merge w2b@b33481b7 partial, +6 tiers, +62 pins;
commit msg verified via git log) + b82fa688 (C
port; parent == 88a5b299 verified). Trees via git
archive to TMPDIR tree442/tree442base; tests run
from NVME workdirs (no WT src/__pycache__).

Banked Next-P334 shape (b441 VERIFY, A-883 +
A-1045 agree) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 2e01ac06 NEW-sig 31/84
@132969 + PB1 0e000000 NEW-sig 47/88 vs
n132622 @132970 + PBA88 fb000000 x16 @132971-986
+ C10-region 0c000000 x10 @132987-996
DIFFERS-from-PB1-sig (0e-vs-0c) -- staged==oracle
0/0/0/0, sigs exact, counts+positions identical.
Bank-miss lesson applied: no trust without code.

- Build: make -C tree442/src/c BUILDDIR=$R/build442
  aae rgramc, rc=0, 0 warnings, build442/{aae,
  rgramc}. aae sha256 d6e27c97 (pinned stable
  continues), rgramc sha256 7347161b (== GATE
  both).
- RGRAMC-PYID 9939/9939 covered=9939/9939 GREEN
  rc=0 (tests/test_rgramc_fast.py, RGRAMC=seat
  binary, CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19878/19878 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 19878/19878 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 19878/19878; cmp442.py; GATE claims
  ordered+raw both, corroborated).
- PINS 19880 rows (2 hdr + 19878, +62 vs base
  19818; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq442.py). For-list
  union delta vs base +31/-0 (9908->9939):
  132969 132970 132971 132972 132978 132979
  132985 132986 132987 132988 132991 132992
  132995 132996 132997 133004 133012 133013
  133028 133029 133044 133045 133052 133060
  133061 133119 133120 133184 133247 133248
  133316 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (132969/70) + A head pair 971/972 off0/1
  + 978/979 off7/8 + tail pair 985/986 off14/15
  (6: offs 0,1,7,8,14,15) + C head pair
  987/988 off0/1 + B5EDGE pair 991/992 off4/5
  + tail pair 995/996 off8/9 (6) + Q head 997
  off0 + 1004 off7 + pairs 1012/1013 off15/16
  + 1028/1029 off31/32 + 1044/1045 off47/48 +
  1052 off55 + tail 1060 off63 (10: offs 0,7,
  15,16,31,32,47,48,55,63) + R head 1061 off0
  + edge pair 1119/1120 off58/59 + mid 1184
  off123 + edge pair 1247/1248 off186/187 +
  tail 1316 off255 (7). 31x2=62 rows, range
  132969..133316 exact. PINS-new-N == for-added
  31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit442.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 151 PASS 0 FAIL after 5 seat-script
  fixes (CC-b8687 const misplaced: b86,87 are M6
  lanes, const d14d lives in QC -- moved assert;
  S1-C10 [44]x10 over-assert: C10 B5EDGE splits
  cells [44]x5+[45]x5, b5-only delta recorded;
  QR-b87 check indexed wrong bytes -- replaced
  with b84 vals; M-ordered assert inverted: FULL
  means ordered-EQUAL -- fixed; all caught by
  runs, re-ran). Inventory exactly the 12 both
  sides, C==py (S0/S1/AM/AC/CM/CC/M/QR/QC/
  RM/RQ/RC; no F/FT, no F0/F1, no BM/BC, no M19/
  X19, no QB/PT/FM, no M42/X42/H42/L42, no
  RT/TT, no QT). S0 168ch sig 2e01ac06 NEW
  (sig-family change vs 6db296xx era; 31/84
  payload diff vs P333S0 @ 0-2,4,5,13,15-21,
  24-29,56-67 first-hand, NOT byte-equal;
  differs vs P333 heads 6db29606/0d000000) /
  S1 176ch sig 0e000000 NEW (47/88 payload diff
  vs P333S1 @ 0,4,5,16-19,22-28,30-38,40-47,
  64-75,84-87 first-hand incl sig b0, NOT
  byte-equal; 44/88 diff vs own C10[0] staged
  cell0; sig DIFFERS-from-own-C10 0e-vs-0c;
  differs vs own PB0), staged as full-payload
  singletons. AM 16/16 16ch distinct (8B), CM
  10/10 12ch distinct (6B: M6 b45,46,84-87;
  b45 {2e,6e,ee} first-hand), M 16/16 16ch
  distinct (8B: M8 b38,39,46,47,80-83), QR 4/4
  4ch distinct (2B R2 rows ec47/0c48/4b48/6b48;
  b84 vals ec/0c/4b/6b) UNPAIRED, RM 16/16 16ch
  distinct (8B RM8 b6-9,76-79), RQ 16/16 16ch
  distinct (8B RQ8 b52-55,80-83) UNPAIRED, no
  QT (quad tails = R2 b84,85 + consts) + no RT
  (SWAPPED tails) + no F (no frags). AC 78,
  b0-3 fb000000 (b0 const fb), no b4/b5.
  C10-DIFFSIG-M6b45-B5EDGE sig 0c000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts;
  CM 10/10 diverge, b45 {2e,6e,ee}; CC has no
  b4/b5, b5 edge 0e->0f @off4/5 in VPOS via raw
  lencode; b86,87 are M6 lanes, NOT const in
  CC). S1-vs-own-C10 staged per-cell (M6
  b45,46,84-87 + b0-3 CC sig + b4/b5 lencode
  with edge, each cell own assembly) [44]x5 +
  [45]x5 edge-split DIFFSIG (cells0-4 identical,
  cells5-9 identical, delta exactly b5-only;
  oracle secf442c same [44]x5+[45]x5), sig
  0e-vs-0c, NOT byte-equal -- NOT uniform
  (record stays 25).
  QUAD88-1SIG-4R-NOFRAG-C87 1-sig fb000000 x64
  SAME-sig-as-PBA (QC b0 const fb; b5 const 0f
  NO edge, deducted from QC; b4 base 0x0b step2
  64/64 contig+2 range 0b..89): QM8 b52-55,
  80-83 M 16/16 shared x3 vs row0 (M indexed by
  col off&15 first-hand) NO frags + R2 b84,85
  rows ec47/0c48/4b48/6b48 4/4 NO pairing
  BY-ROW const (QR indexed by row off>>4
  first-hand); tails b84-87 = row+d14d:
  ec47d14d/0c48d14d/4b48d14d/6b48d14d, r0
  TRUE-2B d14d vs all, r123 TRUE-3B 48d14d
  (b85=0x48 r1/r2/r3 + const d14d), suffix =
  subseq = substr = 2/2/2/3/3/3 (order
  01,02,03,12,13,23; computed all three first-
  hand; == A-1046 suffix-lcs); b86,87 const
  d14d in QC (b87 CONST 4d quad-wide); NO frags.
  R legs M[m] + QR[q] both sides, NO F-row leg,
  NO F-scalar leg; Q region m=off&15/q=off>>4.
  P334R(T88-ring SWAPPED) 133061..133316
  off=n-133061 1-sig bb0f0000 x256; code-RM8
  b6-9,76-79 by COL + code-RQ8 b52-55,80-83 by
  ROW UNPAIRED (SWAPPED tails b80-83 row /
  b76-79 col); b0 const bb; b1 const 0f; b84-87
  const 62c6d8c8 ring-wide NEW; counter b4=
  (0x8b+2off)&FF b5=0x0f+(off>=59)+(off>=187)
  (py hex 0x8b/0x0f; C staged literals 139/15,
  re-derived: 139==0x8b, 15==0x0f; edges
  off58/59 + off186/187 + mid off123
  first-hand). R legs RM[c] + RQ[r] both sides,
  NO F anywhere in R. RM 16/16 distinct + RQ
  16/16 distinct.
  M==RQ FULL 16/16 string-identical INTRA-tier,
  byte positions DIFFER (sets equal + ordered
  equal; SAME lanes QM8/RQ8 b52-55,80-83; M
  indexed by COL off&15 vs RQ by ROW off>>4
  first-hand; SWAPPED tails b80-83 row / b76-79
  col; diag-16 all 8 lanes; zero strays; running
  string-eq pattern continues after the b440
  0/16 lanes-differ tier) -- 38th even-band
  RQ==M instance (viewer evens b436-36th/b438-
  37th string-eq + b440 rows-disjoint outlier +
  b442-38th FULL; sweep "FULL string-identical,
  positions DIFFER" = tables ordered-identical
  + payload slots split, reconciled first-hand).
  Tails SWAPPED (RM b76-79 col-led tails / RQ
  b80-83 row-led tails, 16/16 distinct each, 0
  overlap UNPAIRED); M-tails 16/16 ALL NEW vs
  P333 (overlap 0 vs P333T RM col-led tails).
  AM/CM/M/QR/RM/RQ 0-overlap vs P333 (widths
  P334 vs P333: AM 8B vs 7B, CM 6B vs 2B, M 8B
  vs 8B, QR 2B vs 4B, RM 8B vs 7B, RQ 8B vs 8B).
  S0 string 31/84 differ vs P333S0 (NEW-sig
  family change) + S1 string 47/88 differ vs
  P333S1 (incl sig b0; [44]x5+[45]x5 edge-split
  vs own C10 DIFFSIG -- not a uniform case).
  P334 actuals (S0 2e01ac06/S1 0e000000/PBA88
  fb000000/C10 0c000000 x10 DIFFERS-from-PB1 +
  PB0-vs-P333PB0 31/84 + PB1-vs-P333PB1 47/88)
  == A-884 predicted next EXACT.
  Missing-sets first-hand EXACT: AC-10
  [4,5,38,39,46,47,80-83] = b4,b5+M8 (b5 const
  0e deducted from AC) / CC-8 [4,5,45,46,84-87]
  = b4,b5+M6 (full sig b0-3 in CC = 0c,00,00,00
  -> 0c000000 x10 DIFFERS-from-PB1-sig; b5 edge
  in VPOS, deducted) / QC-12
  [4,5,52,53,54,55,80-85] = b4,b5+QM8
  (b52-55,80-83)+R2 (b84,85; b0 const fb in QC
  = 1SIG, b5 const 0f deducted, b86,87 const
  d14d in QC) / RC-18
  [4,5,6,7,8,9,52-55,76-83] = b4,b5+RM8
  (b6-9,76-79)+RQ8 (b52-55,80-83). Code AC78/
  CC80/QC76/RC70; incl = +1/+0/+1/+0 (A b5
  const 0e, C b5 edge-varies in VPOS, Q b5
  const 0f, T counter) = 79/80/77/70; lane
  consts = A-884 INCL EXACT on C10+T88, PBA/
  quad writer-1 (deduct-b5-only-when-b5vary
  holds; A-1046 excl 78/80/76/70 = code EXACT).
  AC-QC both=72 sameval=54 == GATE. Sorted-
  unique + _N decls 78/80/76/70 match actual.
  Coverage unions exact every block (const U tab
  U lencode == 88 x4, 0 overlap; each missing
  == region pay-index set minus lencode EXACT
  all 4). Base temp maxes _t6796/_b4114/_i4115
  (no reuse: band adds _t6797-6812 continuous-16
  + _i4117/19/4122/4125 + _b4116/18/4120/4121/
  4123/4124, whole-file max _t6812, all above
  base maxes).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 132969 / S1 132970 / A 132971-986 /
  C 132987-996 / Q 132997-060 / R 133061-316):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A b5 const 0e, C b5=
  0e+(off>=5) edge 132991->132992, Q b5 const
  0f NO edge; A/C/Q use raw lencode, no counter
  literals anywhere A/C/Q) + R explicit counter
  (b4=(0x8b+2off)&FF b5=0x0f+(off>=59)+
  (off>=187); py hex 0x8b/0x0f; C staged
  literals 139/15, re-derived: 139==0x8b,
  15==0x0f) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions
  exact (A 16ch b38,39,46,47,80-83; C 12ch
  b45,46,84-87; Q 16/4ch; R 16/16ch). C blocks
  carry T89336/89341/89346/89361/89376/89395
  py-line mirrors (all 6 present, bounds + byte
  positions exact). Insert exact both sides:
  after T10P333R close (py 89334-guard then
  89336+; C 237625-27/237628/237629 per GATE),
  at dispatch tail (N-out-of-scope fallthrough
  follows: C 237809, py 89414; early same-text
  guards at C 160194 / py 55210 are the
  T4-plateau-B n<=1077 check, unrelated scope).
  Matches A-884 geometry (values re-checked in
  audit above; NO D dips: ownloop tags exactly
  the 6 P334 blocks).
- Edges own-loop ownloop442.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P334R N=133316 off=255.
  edges442.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  d3/0e, d5/0e == raw lencode) + aform 16/16 (A
  head d7/0e tail f5/0e b5set {0e} NO step, 0
  ff) + cform 10/10 (C head f7/0e edge 132991
  off4 ff/0e -> 132992 off5 01/0f tail 09/0f
  b5set {0e,0f} edge, exactly 1 ff in 10; b4
  base 0xf7 step2 10/10) + qform 64/64 +
  qb5const 64/64 (Q head 0b/0f tail 89/0f b4
  base 0x0b step2 64/64 contig+2 range 0b..89
  b5set {0f} NO edge, 0 ff in 64) + ring
  counter 256/256 + ringraw 256/256 (head
  8b/0f; 133119 off58 ff/0f -> 133120 off59
  01/10; mid off123 81/10 @133184; 133247
  off186 ff/10 -> 133248 off187 01/11; tail
  off255 89/11; exactly 2 ff in 256; Q tail
  89/0f vs R tail 89/11 differ in b5 -- labeled
  apart). S0/S1 embedded b4/b5 match raw
  lencode. Odd-lencode 348/348. Ring edges +
  mid + tail 133316 in for-list + 2 PASS lines
  each py+C. Tail 133316: oracle rav sha
  faf85bfa84910abb... == PINS (match True;
  rawlen 104 re-checked); py+C CLOSED T10P334R
  off=255 agree. No DISSENT: cut bytes verify.
- PB-diff secf442.py (cache path, 0 miss-warmed
  after ownloop) + secf442b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (132969 +
  132621 + 132970 + 132622); S0: oracle132969-
  vs-132621 31/84, codeS0-vs-P333S0 31/84,
  positions identical (differ-pos 0-2,4,5,13,
  15-21,24-29,56-67 listed); DIRECT 31/84
  agree. S1: oracle132970-vs-132622 47/88,
  codeS1-vs-P333S1 47/88, positions identical
  (differ-pos 0,4,5,16-19,22-28,30-38,40-47,
  64-75,84-87 listed); DIRECT 47/88 agree.
  Triple-derived both pairs (same novel shape
  both tiers: 84/84/84/84 + 88/88/88/88).
  S1-vs-own-C10 secf442c.py (oracle C10 cells
  n132987-996): [44]x5+[45]x5 edge-split
  DIFFSIG staged+oracle (cells0-4 identical,
  cells5-9 identical, delta exactly b5-only),
  sig 0e-vs-0c, NOT byte-equal. NOT uniform --
  record stays 25. Byte-diff discipline
  observed throughout.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  230/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw C
  608 total = 603 content + 5 bare-blank / 0
  del (verified bare `+` lines; GATE states
  "603 content + 5 bare-blank" EXACT -- stated
  correctly this band, no overcount).
  Band-level sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope 18016e8a..
  b82fa688, 901 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 230/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1892->1898 +6, singletons
  `if n == ` 700->702 +2 (unanchored; 4sp
  695->697 +2) / range-guards `<= n <=`
  788->792 +4 (unanch and 4sp) = +6 py;
  C guards: singleton `if ((n) == (` 695->697
  +2 / range 788->792 +4 / CLOSED T10P prints
  1892->1898 +6 both sides (seal 1986->1992 +6;
  offset +94 vs CLOSED-T10P: 1992-1898 = 94,
  stable b401-b442). All agree (deltas agree
  every method; 5-count C-vs-py singleton offset
  pre-existing, unchanged: 702-697 = 700-695
  = 5; GATE-tier absolute 690->692 is sweep2's
  unanchored-literal convention, delta +2 agrees
  -- viewer-vs-sweep absolute convention
  reconciled, no slip). No elif either side (py
  elif 50->50, C else-if 0->0; A/C/Q use raw
  lencode, no counters).
- CONFIRM evidence (CONVERT-01 rule b): A-884-
  q1046 verdict CONFIRM 61/61 CLEAN (own bed
  r3-P334 132969..133348 BAD=0 + own r3-P333,
  verifier v270.py 61/61 PASS; tier GATED PORT;
  novelty FIRST-R2-quad + SWAPPED T-ring gated;
  exact-value corroboration incl PB0 NEW-sig
  31/84 + PB1 NEW-sig 47/88 DIFFERS-from-own-
  C10 44/88 + PBA88-PLAIN-M8b38 sig-fb M8 +
  C10-DIFFSIG-M6b45-B5EDGE + QUAD 1-sig-fb-
  SAME-as-PBA + R2 rows ec47/0c48/4b48/6b48 +
  r0-TRUE-2B + r123-TRUE-3B + b87-CONST-4d +
  QM8 + NO frags + b5-const + M-tails NEW +
  T88-RING-SWAPPED + RM8-by-COL/RQ8-by-ROW +
  SWAPPED-tails + b0-bb + b1-0f + b84-87
  62c6d8c8 + counter + edges; sheet-vs-tables
  const-count note: Q-1046 sheet 79/80/77/70
  memo-exact, committed tables 78/80/76/70
  still deduct const-b5 on PBA/quad -- S-F
  arithmetic in tables only, geometry exact,
  PORT stands) + A-1046-q1046 verdict CONFIRM
  48/48 CLEAN (own bed r6-P334 132969..133344 +
  r6-P333, BAD=0 + direct-oracle 2/2 byte-match,
  verifier v600f3.py 48/48 PASS; suffix-lcs
  2/2/2/3/3/3 at all 3 metrics (computed
  suffix+subseq+substr first-hand) + M-tails
  NEW + SWAPPED-frame + consts excl 78/80/76/70
  script-claimed corroborated; files present,
  counts verified; tier GATED PORT). Agrees
  with cport commit msg (PYID 9939, RGRAM
  19878). No viewer P334 geometry answer on
  file at gate time (memo-only recon; this
  VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b442
  (own seat CLAIM only; exactly 1 GATE-b82fa688;
  zero FLAG hits; odd base b441 respected;
  b443 = future turf, used for FWD-check code
  reads only, no verdict). PROSE-01: all
  hex/counts above copied from own run output;
  GATE-b82fa688 re-read in FULL before filing
  (no prose slip found; raw-C stated correctly).
- RQ==M chain: b442 even FULL string-eq-
  positions-differ (sets+ordered equal, diag-16
  all 8, zero strays; slots split COL-vs-ROW).
  38th even-band instance (viewer evens b436-
  36th/b438-37th string-eq + b440 rows-disjoint
  outlier + b442-38th FULL sequential). Memo-
  silent on the relation; batteries confirm;
  tier stands.
- TRUE-uniform chain: b442 NOT uniform (S1
  DIFFSIG vs own C10, [44]x5+[45]x5 edge-
  split). Record stays 25 (24 excl P299).
- S-F tables-lag: b442 impl 78/80/76/70 vs
  A-884 sheet 79/80/77/70 (PBA/quad writer-1,
  C10+T88 memo-exact) -- 16th even-band running
  per GATE count (b412..b442); odd-band rule
  (deduct-b5-only-when-b5vary) unaffected.
- Next-P335 SHAPE banked (A-884 FWD + lane code
  first-hand, for b443 to CONSUME FIRST): PB0
  2e01ac06 SAME-sig-as-P334PB0 30/84 @133317 +
  PB1 0d000000 NEW-sig 69/88 vs n132970 @133318
  + PBA88 d5000000 x16 @133319-334 + C10-region
  0d000000 x10 SAME-as-PB1-sig @133335-344
  (sigs + PBA/C10 ranges verified first-hand
  against ff5b855c code no-checkout; diffs
  30/84 + 69/88 banked for CONSUME-time verify).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; zero prose slips found.
