# VERIFY-2de6d522 b446 T10P338 pins 134361..134708 (348 pins) PASS

Seat viewer-r69, first-hand, tree @2de6d522,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r69.
Base aab37716 (b445 tip, 2010 tiers sealed; this
seat's VERIFY-aab37716 PASS-filed same round,
base-use only, respected). Band = 35e3c34d (py
merge w2b@12c56aae partial, +6 tiers, +62 pins;
commit msg verified via git log) + 2de6d522 (C
port; parent == 35e3c34d verified). Trees via git
archive to TMPDIR tree-sha dirs; tests run from
NVME workdirs (no WT src/__pycache__).

Banked Next-P338 shape (b445 VERIFY: A-895 FWD +
A-1049 Q1 agree) CONSUMED FIRST and VERIFIED
first-hand EXACT: PB0 aefd4106 SAME-sig-P337
33/84 @134361 + PB1 0c000000 SAME-sig-P337
60/88 @134362 + PBA88 cd000000 x16 @134363-378
+ C10-region 0c000000 x10 SAME-as-PB1-sig
@134379-388 (memo-derived; lane-code verified at
CONSUME time per bank-miss lesson).

- Build: make -C tree/src/c BUILDDIR=$R/build446
  aae rgramc, rc=0, 0 warnings, build446/{aae,
  rgramc}. aae sha256 d6e27c97 (pinned stable
  continues), rgramc sha256 ff7389f6 (== GATE).
- RGRAMC-PYID 10063/10063 covered=10063/10063
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, CT_CACHE_DIR default NVME, NVME
  workdir).
- RGRAM py 20126/20126 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, CT_CACHE_DIR
  set).
- RGRAM C 20126/20126 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary); C-py PASS-set
  cmp-equal (sorted cmp equal + raw-order
  identical, 20126/20126; cmp446.py; GATE claims
  sorted only, raw corroborated too).
- PINS 20128 lines (2 hdr + 20126, +62 vs base
  20066; +62 = 31 for-Ns x2); PASS-names vs
  PINS-names xor 0 py+C; PINS-baseN vs for-list
  xor 0 (4-way set-eq, seteq446.py). For-list
  union delta vs base +31/-0 (10032->10063):
  134361 134362 134363 134364 134370 134371
  134377 134378 134379 134380 134383 134384
  134387 134388 134389 134399 134400 134401
  134405 134420 134421 134436 134437 134452
  134453 134527 134528 134592 134655 134656
  134708 (== GATE sampled list EXACT).
  Decomposition first-hand from the added set: 2
  sing (134361/62) + A head pair 363/364 off0/1
  + 370/371 off7/8 + tail pair 377/378 off14/15
  (6: offs 0,1,7,8,14,15) + C head pair 379/380
  off0/1 + mid pair 383/384 off4/5 + tail pair
  387/388 off8/9 (6: offs 0,1,4,5,8,9; b5 const,
  sampling not edge) + Q head 389 off0 + edge
  399 off10 + 400 off11 + 401 off12 + 405 off16
  + pairs 420/421 off31/32 + 436/437 off47/48 +
  tail 452 off63 (10: offs 0,10,11,12,16,31,32,
  47,48,63) + R head 453 off0 + edge pair
  527/528 off74/75 + mid 592 off139 + edge pair
  655/656 off202/203 + tail 708 off255 (7: offs
  0,74/75,139,202/203,255; 1-mid off139 NEW
  shape, both counter edges pair-covered).
  31x2=62 rows, range 134361..134708 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes
  + aea encrypt/decrypt/bytes PASS, default
  oracle backend, no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit446.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 123 PASS 0 FAIL first full-green run
  (first file version; asserts derived from
  GATE shape throughout: no cloned-shape asserts
  -- M-vs-RQ recorded diag-16 + print strays
  rather than cloning a zero-stray claim).
  Inventory exactly the 12 both sides, C==py
  (S0/S1/AM/AC/CM/CC/M/QR/QC/RM/RQ/RC; no F/FT,
  no F0/F1, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42, no RT/TT, no QT). S0
  168ch sig aefd4106 SAME-sig-P337 (33/84
  payload diff vs P337S0 @ 4,5,32-55,72-79
  first-hand, NO sig bytes in diff, NOT byte-
  equal; differs vs P337 heads 0c000000-side) /
  S1 176ch sig 0c000000 SAME-sig-P337 (60/88
  payload diff vs P337S1 @ 4-25,28-31,37-43,
  45-59,76-87 first-hand (sig b0 NOT in diff,
  sig kept 0c); NOT byte-equal;
  29/88 diff vs own C10[0] staged cell0 @ 4,8-
  31,60-63,84-87; sig SAME-as-own-C10 0c-vs-0c;
  differs vs own PB0), staged as full-payload
  singletons. AM 16/16 12ch distinct, CM 10/10
  6ch distinct, M 16/16 16ch distinct, QR 4/4
  8ch distinct, RM 16/16 20ch distinct, RQ
  16/16 16ch distinct, no QT (quad tails = R4
  b84-87 full tuples) + no RT (COL-led tails) +
  no F (no frag this tier). M==RQ FULL 16/16
  string-identical INTRA-tier incl ORDER
  (M-ordered-equal-RQ True; diag-16 all 8 lanes;
  zero strays; sets+ordered EQUAL) -- lanes
  DIFFER (TM10 b0,11,19,27,34,35,80-83 vs TR8
  b28-31,76-79; M indexed by COL off&15 vs RQ
  by ROW off>>4 first-hand; COLSIG tails b0-
  led). AC 80, CC 83, QC 74, RC 68; C _N decls
  80/83/74/68 match actual; byte-coverage
  unions exact every block (88/88/88/88, 0
  overlap gap-free, mtab/r-tab computed).
  PBA88-PLAIN-M6b20 sig cd000000 (b0 const cd,
  AM 16/16 distinct NO pair; M6 b20,21,80-83;
  b5 const 19 via raw lencode NOT in AC).
  C10-1SIG-88-TAIL-M3 sig 0c000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM
  10/10 diverge 6ch b84-86; CC has no b4/b5, b5
  const 19 full block via lencode; CC has b87
  const 95). QUAD88-1SIG-4R-NOFRAG-B5EDGE
  1-sig cd000000 x64 SAME-sig-as-PBA (QC b0
  const cd, b1-3 const 00; b5 edge 19->1a
  @off10/11 emergent from raw lencode, edge
  134399->134400 r0c10/c11; b4 base 0xeb step2
  64/64 contig+2 range eb..ff,01..69; QM8
  b28-31,80-83 M 16/16 shared x3 vs row0 (M
  indexed by col off&15 first-hand) NO frags +
  R4 b84-87 rows 76fde595/de357ff4/fe357ff4/
  1e367ff4 4/4 NO pairing BY-ROW const (QR
  indexed by row off>>4 first-hand); tails =
  full tuples 4/4 distinct, r0 trailing-suffix
  lcs=0 vs all, r12 TRUE-3B 357ff4, r13 TRUE-2B
  + r23 TRUE-2B, else-pair suffix-LCS 0/0/0/3/2/2
  recorded first-hand (subseq/substr printed,
  suffix asserted); b87 NOT-const {95,f4}).
  Ring COLSIG 2-sig: sig 0a0d0000 x112 (col<7)
  + 0c0d0000 x144; code-RM10 b0,11,19,27,34,35,
  80-83 by COL RM 16/16 + code-RQ8 b28-31,76-79
  by ROW RQ 16/16 UNPAIRED; b0 COL-led (0a
  c0-6/0c c7-15 EVERY row verified 16x16); b1
  const 0d; b84-87 const 3e367ff4 ring-wide NEW
  (b0 NOT in RC table -- varies by COL -- b1
  const in table; RC missing incl b0).
  VPOS partitions re-derived from code: PBA 7
  (b4+M6; b5 const 19 excluded) / C10 4 (b4+M3;
  b5 const excluded) / quad 14 (b4,b5+QM8+R4;
  b5 edge-varies, in VPOS) / T 20
  (b0,b4,b5+TM10+TR8; b5 counter-varies, in
  VPOS) -- all match A-896/A-1050 (missing sets
  AC-8 [4,5,20,21,80-83] / CC-5 [4,5,84-86] /
  QC-14 [4,5,28-31,80-87] / RC-20
  [0,4,5,11,19,27,34,35,80-83,28-31,76-79]
  first-hand EXACT; deduct-const-b5 convention
  uniform P335/P336/P337/P338).
  Code-consts vs A-896 INCL (PBA 81 / C10 84 /
  quad 74 / T88 68): impl 80/83/74/68 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-1050 sheet counts b5 (memo A-896 confirms
  the sheet INCL values) -- S-F arithmetic
  persists in committed tables though the sheet
  is FIXED; memo-exact on quad (b5 edge-varies,
  in VPOS, no deduction) and T88 (b5 counter-
  varies, no deduction); geometry exact, PORT
  verdict stands; FLAGGED for memo (18th even
  band running: b412/b414/b416/b418/b420/b422/
  b424/b426/b428/b430/b432/b434/b436/b438/b440/
  b442/b444/b446 == GATE; PBA/C10 lag this
  tier). Even C10/quad-lag sub-streak: 18th
  (b444-17th + b446-18th consecutive).
  QUAD 1SIG cd SAME-sig-as-PBA this tier (vs
  P336 DIFFERS tier); PBA sig cd NEW vs P337
  8d; AC-QC both=72 sameval=50 (tables differ).
  M-tails 16/16 ALL NEW vs P337 (zero overlap vs
  P337T RM col-led tails; P337T STANDARD frame,
  ref = RM col-led 8B rows, position-aware tails
  last-4B). AM/CM/M/QR/RM/RQ full-row 0-overlap
  vs P337 (all 0/16 printed; widths P338 vs
  P337: AM 6B vs 7B, CM 3B vs 4B, M 8B vs 8B,
  QR 4B vs 3B, RM 10B vs 6B, RQ 8B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in
  order (S0 134361 / S1 134362 / A 134363-378 /
  C 134379-388 / Q 134389-452 / R 134453-708):
  bounds + paylens (1x84 + 347x88) + lencode
  l16 A/C/Q both sides (A/C raw lencode; Q b5
  edge emerges from raw lencode) + R explicit
  counter (b4=(0x6b+2off)&FF b5=0x1a+(off>=75)+
  (off>=203); py hex 0x6b/0x1a; C staged
  literals 107/26, re-derived: 107==0x6b,
  26==0x1a) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions
  exact (A 12ch b20,21,80-83; C 6ch b84-86;
  Q 16/8ch; R 20/16ch). C blocks carry
  T90262/90267/90272/90287/90301/90321 py-line
  mirrors (all 6 present, bounds + byte positions
  exact). Insert exact both sides: after T10P337R
  close (C 240060 comment, S0 guard `if ((n) ==
  (134361))`; py guard 90262), at dispatch tail
  (N-out-of-scope fallthrough follows: C 2 scope
  hits incl plateau n<=1077 check per GATE, py 2
  scope hits). Matches A-896 geometry (values
  re-checked in audit above; NO D dips: ownloop
  tags exactly the 6 P338 blocks).
- Edges own-loop ownloop446.py over ALL 348
  tier Ns (oracle bytes via tool-identical
  -encode -a lzraven through ct-cache; seat
  rgramc): 348/348 CLOSED rc=0 (0 miss-warmed;
  tier fully cache-warmed from sweep leg).
  Census R256/Q64/A16/C10/S0/S1 exact. Tail
  line: CLOSED T10P338R N=134708 off=255.
  edges446.py: paylens 1x84 + 347x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  b3/19, b5/19 == raw lencode) + aform 16/16 (A
  head b7/19 tail d5/19 b5set {19} NO step, 0
  ff) + cform 10/10 (C head d7/19 tail e9/19
  b5set {19} NO step, 0 ff) + qform 64/64 +
  qb5edge 64/64 (Q head eb/19, edge off10
  (ff/19) -> off11 (01/1a), tail 69/1a;
  b5 = 19+(off>=11); b4 base 0xeb step2 64/64
  contig+2 range eb..ff,01..69; exactly 1 ff in
  64) + ring counter 256/256 + ringraw 256/256
  (head 6b/1a; 134527 off74 ff/1a -> 134528
  off75 01/1b; mid off139 81/1b @134592;
  134655 off202 ff/1b -> 134656 off203 01/1c;
  tail off255 69/1c; exactly 2 ff in 256).
  Odd-lencode 348/348. Ring edges + mid + tail
  134708 in for-list + 2 PASS lines each py+C.
  Tail 134708: oracle rav sha 44f9faa56370b876...
  == PINS (match True; rawlen 104 re-checked);
  py+C CLOSED T10P338R off=255 agree. No
  DISSENT: cut bytes verify.
- PB-diff secf446.py (cache path, 0 miss-warmed
  after ownloop) + secf446b.py (DIRECT tool, no
  cache): staged-vs-oracle 0/0/0/0 (134361 +
  134013 + 134362 + 134014); S0: oracle134361-
  vs-134013 33/84, codeS0-vs-P337S0 33/84,
  positions identical (differ-pos 4,5,32-55,
  72-79 listed); DIRECT 33/84 agree. S1:
  oracle134362-vs-134014 60/88, codeS1-vs-
  P337S1 60/88, positions identical (differ-pos
  4-25,28-31,37-43,45-59,76-87 listed); DIRECT
  60/88 agree. Triple-derived both pairs (same
  novel shape both tiers: 84/84/84/84 +
  88/88/88/88). S1-vs-own-C10 secf446c.py
  (oracle C10 cells n134379-388): [29]x10
  staged+oracle, cells0-9 positions identical
  (cell0 pos 4,8-31,60-63,84-87 == staged
  EXACT; sig b0-3 same-sig NOT in diff), sig
  0c000000 both, NOT byte-equal. Verdict NOT
  uniform (structural relation uniform per-cell,
  but sweep accounting excludes P338: b447 GATE
  counts P339 as the 15th TRUE-uniform case;
  discriminating factor consistent with all 14
  prior cases = NEW-sig S1 (P338 S1 SAME-sig-
  P337) and/or odd-band (P338 even); every
  prior uniform case is both NEW-sig and odd,
  every prior non-uniform fails structure
  (DIFFSIG/edge-split) so the novelty/parity
  conditions were never isolated before --
  P338 isolates them and sweep counts exclusion.
  Viewer DEFERS to sweep accounting (chain
  owner) rather than forking the shared count
  on an unstated-rule dispute; structural facts
  ([29]x10 staged+oracle, SAMESIG, identical,
  NOT-byte-equal, FIRST 29-wide relation)
  recorded first-hand above for parent/memo
  adjudication; flagged in handoff scars).
  Record stays 27. Byte-diff discipline
  observed.
- C diff pure-add: numstat 608/0 (rgramc.c) +
  232/0 (rgram.py) + 1/1 (for-line) + PINS +62/
  +0 (clean append, 31 Ns x2) == GATE; raw band
  903 total = 898 content + 5 bare-blank / 0
  del (verified bare `+` lines, 0 ws-only; all 5
  blanks inside rgramc.c; GATE states band split
  correctly "raw C grep 898 content + 5 bare-
  blank" == 898+5 = 903 band-wide, no overcount
  this even band -- evens pattern: b440/b442/
  b444/b446 stated correctly, odds overcount).
  Band-level sole del = old for-line churn (1/1).
- Wall on band diff added lines (scope aab37716..
  2de6d522, 903 added lines == GATE): vendor 0
  hits, disasm 0 hits, depload (dylib/CDLL/
  dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  libcompression/compression_tool//usr/bin/aa/
  nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 608/0, rgram.py 232/0
  purely additive, test_rgram.sh 1/1 (for-line),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-
  comments `# T10P` 1916->1922 +6, singletons
  `if n == ` 708->710 +2 (unanchored; 4sp
  698->700 +2 = GATE-tier absolutes) /
  range-guards `<= n <=` 804->808 +4 (unanch and
  4sp) = +6 py (== GATE deltas 698->700 /
  782->786 scoped-literal method; deltas agree
  every literal method; viewer-vs-sweep absolute
  convention reconciled: GATE-tier absolutes use
  4sp-dispatch-exact (C singletons 698->700
  verified 4sp 700/698 both sides), viewer
  unanchored 708->710; +10 = non-dispatch
  guards, pre-existing) / CLOSED T10P prints
  1916->1922 +6 both sides (seal 2010->2016 +6;
  offset +94 vs CLOSED-T10P: 2016-1922 = 94,
  stable b401-b446). All agree (stated literal
  methods first-hand; deltas agree every method;
  5-count C-vs-py singleton offset pre-existing,
  unchanged: 710-705 = 708-703 = 5; C guards:
  singleton `if ((n) == (` 703->705 +2 / range
  804->808 +4; C-closed 1922; no C-only offset
  this window). No elif either side (py elif
  50->50, C else-if 0->0; A/C/Q use raw lencode,
  no counters).
- CONFIRM evidence (CONVERT-01 rule b): A-896-
  q1050-P338 verdict CONFIRM 63/63 CLEAN (own
  beds r3-P338 134361..134740 + r3-P337 380
  cells, BAD=0, verifier v282.py 63/63 PASS;
  tier GATED PORT; novelty gated: COLSIG T-ring
  (b0 COL-led 0a/0c split, 2-sig 112/144, VPOS
  20); exact-value corroboration incl PB0
  SAME-sig 33/84, PB1 SAME-sig 60/88 SAME-as-
  own-C10 29/88, PBA16 sig-cd VPOS 7, C10
  sig-0c SAME-as-PB1 VPOS 4 b87 const 95,
  QUAD64 1-sig-cd SAME-as-PBA + R4 rows + r0-
  lcs0 + r12-TRUE-3B + r13/r23-TRUE-2B +
  b87-notconst + QM8 + NO frags + b5-edge +
  M-tails NEW, T256-RING-COLSIG + TM10-by-COL/
  TR8-by-ROW + b0-COL-led + b1-0d + const
  3e367ff4 + counter/edges; plus sheet-vs-tables
  const-count note: Q-1050 sheet 81/84/74/68
  memo-exact, committed tables 80/83/74/68
  still deduct const-b5 on PBA/C10 -- S-F
  arithmetic in tables only, geometry exact,
  PORT verdict stands) + A-1050-q1050-P338
  verdict CONFIRM 48/48 CLEAN (own bed r6-P338
  134361..134736 376 cells + r6-P337 cross-refs,
  BAD=0, verifier v600f3.py 48/48 PASS; tier
  GATED PORT; suffix-lcs 0/0/0/3/2/2 + M-tails
  NEW + COLSPLIT-frame + consts excl 80/83/74/
  68 script-claimed corroborated; files present,
  counts verified; tier GATED PORT). Agrees with
  cport commit msg (PYID 10063, RGRAM 20126).
  No viewer P338 geometry answer on file at gate
  time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b446/
  2de6d522 (quiz poll + filename grep first-
  hand; own seat CLAIM only; exactly 1 GATE-
  2de6d522; zero FLAG hits; odd base b445
  respected; no future turf touched). PROSE-01:
  all hex/counts above copied from own run
  output; GATE-2de6d522 re-read in FULL before
  filing (zero prose notes; raw-C stated
  correctly).
- RQ==M chain: b446 even FULL string-identical
  incl ORDER (M 8B vs RQ 8B same-lanes diag-16,
  zero strays; sets+ordered EQUAL) -- 40th
  even-band RQ==M instance (viewer evens b436-
  36th/b438-37th + b440 outlier unnumbered +
  b442-38th/b444-39th FULL/b446-40th FULL
  sequential; odds sequential 40 at b445).
  Viewer-vs-sweep convention reconciled
  first-hand (sweep rows; viewer confirms +
  records column detail: ordered-equal, zero
  strays).
- TRUE-uniform chain: b446 NOT uniform (S1
  SAMESIG-own-C10 [29]x10 staged+oracle,
  cells0-9 identical, NOT-byte-equal -- structure
  uniform per-cell, but sweep accounting excludes:
  P339 counted 15th; novelty/parity rule
  unresolved, viewer defers, evidence on file).
  Record stays 27 (P338 adds 0). FIRST 29-wide
  staged relation (not a uniform case).
- S-F tables-lag: b446 even band lag (impl
  80/83/74/68 vs A-896 INCL 81/84/74/68,
  PBA/C10 writer-1; memo-exact on quad+T88) --
  36th S-F instance, 18th even-band C10/quad-lag
  sub-streak (b444-17th + b446-18th consecutive).
  Odd-band rule deduct-b5-only-when-b5vary holds.
- Next-P339 FWD (A-896 Q1 + A-1050 Q1 agree, for
  r69 b447 to CONSUME FIRST): PB0 @134709 sig
  ee4a0a06 NEW-sig + PB1 @134710 sig 0d000000
  NEW + PBA 86000000 x16 @134711-726 + C10
  0d000000 x10 SAME-as-PB1 @134727-736
  (memo-derived; lane-code verify pending at
  CONSUME time per bank-miss lesson).

Verdict: PASS. No RED. GATE CORRECT on code +
behavior legs; zero prose slips. Novelty calls
this band (first-hand): COLSIG T-ring gated +
verified; B5EDGE quad gated + verified; P338
S1-C10 [29]x10 staged-relation (first 29-wide
relation; NOT a uniform case per sweep
accounting -- flagged for adjudication);
M==RQ zero-stray FULL (vs b444 1B-stray pair).
