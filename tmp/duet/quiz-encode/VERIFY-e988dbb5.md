# VERIFY-e988dbb5 b486 T10P378 pins 148281..148628 (348 pins) PASS

Seat viewer-r81, first-hand, tree @e988dbb5f83163fc8135711db0b972bc936a02d5,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r81.
Base ac53e2c4 (b485 tip, 2250 tiers sealed; this
seat's VERIFY-ac53e2c4 PASS-filed r80,
base-use only, respected). Band = a0fd3014 (py
merge w2b@68747e6d02be256ef7ce49a7fe5b0aa9edb1c312, +6 tiers, +58 pins;
commit msg verified via git log + rev-parse at boot) + e988dbb5 (C
port; parent == a0fd3014 verified via git
rev-list --parents). Chain ac53e2c4 -> a0fd3014
-> e988dbb5, every sha via git log at takeover,
NO gap-jump. GATE-e988dbb5 PASS-functional filed
by sweep2-r84 (post-landing) -- reconciled
first-hand below (values agree; tabaudit-count +
uniform-ledger phrasing differ, code facts identical). NO other
GATE/FLAG on b486 at file time (FLAGs on file are
SUPERSEDED holds; no DISSENT names bandbeth tiers).

Banked Next-P378 shape (Q-1126 + A-961-q1126-P378, both read first-hand
at boot) CONSUMED FIRST and VERIFIED
first-hand EXACT vs Q-1126/A-961 before any
battery step: PB0 df017f24 @148281 (S0 head;
NEW-sig 33/84 vs P377PB0 @ n147933, sig b3 ONLY
IN diff (b0-2 same), positions
[3-5,32-48,50-55,68-75]
first-hand, NOT byte-equal) + PB1 49000000
@148282 (S1 head; NEW-sig 46/88 vs
P377PB1 @ n147934, sig b0 IN diff with b1-3
same, positions [0,4-7,9,10,13,15-19,36-43,46,
48-59,72-79,84-87]
first-hand, NOT byte-equal; diffs
vs own C10 cells 23x9+22x1 (k=7 n148306 diffs
22, rest 23, staged+oracle first-hand);
S1 SIG-SAME own C10 (49-vs-49) and own PB0-differs
(49-vs-df); S1 SIG-SAME own C10 DIFFERS from b484
DIFFERS-pattern, recorded; viewer TRUE-uniform
stays 39 (even band): NOT TRUE-UNIFORM under
viewer convention (uniform-cells required; C10
10/10 DIVERGE + B5EDGE quad split-tier; P338
uniform-rule dispute stays DEFERRED to sweep
accounting, never re-litigated) +
PBA88-PLAIN-M7b20 sig 9b040000 x16 @148283-298
(b0 const 0x9b first-hand, b5 const 0x86 NO step
NO edge, 16/16 distinct NO pair) + C10-region
49000000 x10 @148299-308 SAME-as-PB1-sig
(b0 const 0x49, b5 const 0x86, 10/10 diverge,
M5 b20 lane + b84-87, b52 const f3 PRESENT in CC
(differs from b485 b52-absent, recorded), NO trailer
in CC) --
all corroborated against lane code both sides plus
Q-1126/A-961 before any battery step (py==C
S0/S1 staged strings; S0/S1 staged-eq-oracle
via embed-lencode True/True first-hand; C10 staged-vs-oracle
10/10 DIVERGE GREEN first-run; no bank-miss).

- Build: seat-private build486/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 df829ab1...
  (recorded first-hand here, never
  hand-transcribed; == GATE-prefix df829ab1? GATE
  records aae only -- rgramc hash recorded here
  first-hand for the chain).
- RGRAMC-PYID 11235/11235 covered=11235/11235
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, ct-cache;
  +29 vs b485 11206; unc=0).
- RGRAM py 22470/22470 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 22470/22470 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (22470/22470, sorted +
  raw identical; cmp486.py GREEN).
- PINS-RGRAM cells set-eq 22470/22470 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq486.py GREEN, 15/15). PINS 22472 lines
  first-hand (2 hdr + 22470 rows; base 22414
  lines / 22412 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 11206->11235 +29/-0 (python
  sets on `for s in ...; do` exact token parse,
  trailing-';' glued last token handled, never
  comm; base tail ...148280, band tail ...148628):
  148281 148282 148283 148284 148290 148291
  148297 148298 148299 148300 148303 148304
  148307 148308 148309 148324 148325 148340
  148351 148352 148372 148373 148479 148480
  148544 148607 148608 148609 148628 (== GATE
  29-set exact, first-hand both sides; range
  148281..148628 exact).
  29 = 2 sing (148281 148282 offs 0/1) + A 6
  (head pair 148283/148284 offs 0/1 + mid pair
  148290/148291 offs 7/8 + tail pair 148297/
  148298 offs 14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 86 NO
  edge) + C 6 (head pair 148299/148300 offs 0/1
  + mid pair 148303/148304 offs 4/5 + tail pair
  148307/148308 offs 8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 86 NO edge) + Q 7 (head
  148309 off0 + mid pair 148324/148325 offs
  15/16 + mid off31 148340 + edge pair 148351/
  148352 offs 42/43 (B5EDGE 86->87) + tail off63
  148372; NO step at 15/16; NO D-class dips) + R 8
  (head 148373 off0 + edge pair 148479/148480 offs
  106/107 + mid off171 148544 + edge triple 148607/
  148608/148609 offs 234/235/236 (pre+edge+post) +
  tail off255 148628; offs 1-105,108-170,172-233,
  237-254 unsampled; both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  22470-22412.
- SMOKE-GREEN rc=0 (6/6 PASS: aar
  encode/decode/bytes + aea encrypt/decrypt/bytes,
  default oracle backend, no BACKEND var, NVME
  workdir).
- UNITS-GREEN rc=0 (22/22 PASS,
  tests/test_units.py, synthetic shape tests, no
  oracle).
- Tables audit own script tabaudit486.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 191 PASS 0 FAIL first rerun (one own-script
  slice-bound scar, values untouched; tree untouched).
  Inventory: exactly the 12 band
  tables both sides (S0/S1/AM/AC/CM/CC/M/QR/QC/
  RM/RQ/RC; no F/FT, no F0/F1, no BM/BC, no
  M19/X19, no M42/X42/H42/L42, no QB/PT/FM, no
  RT/TT (ring, not ROWTAIL), no QT (R1 carries
  b84 in-row, no const trailer); no _T10P378C
  in either tree -- base P377 has no _T10P377C
  either, nothing carried forward; 12 symbols
  enumerated first-hand).
  S0 168ch sig df017f24 NEW-sig (33/84 payload
  diff vs P377S0, positions first-hand, sig
  b3 ONLY IN diff (b0-2 same), NOT byte-equal) /
  S1 176ch sig 49000000 NEW-sig (46/88 payload diff
  vs P377S1, positions first-hand, sig b0 IN diff,
  b1-3 same-sig NOT in diff, NOT byte-equal; vs
  own C10 cells 23x9+22x1 staged+oracle; S1
  SIG-SAME own C10 (49-vs-49) and own PB0-differs
  (49-vs-df); 39 stays (even band)).
  AM 16/16 7ch distinct, CM 10/10 5ch M5 diverge
  (b20 mid-body M5 lane + b84-87, all 10
  distinct), M 16/16 8ch QM8 distinct, QR 4/4 1ch
  R1 rows 2b/4b/6b/8b exact, RM 16/16 8ch
  TM8 distinct, RQ 16/16 8ch TR8 distinct.
  AC 79, CC 81, QC 77, RC 70; C _N decls
  79/81/77/70 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap,
  mtab/rq-tab computed).
  QM8 shared 16/16 x3 vs row0 (48/48 cells,
  8 lanes b28,29,30,31,80-83, per-row 16
  distinct, NO frags; positions FIRST-this-lane
  never claimed -- staged P346Q/P370Q per code
  comment). R1 rows 4/4 distinct NO pairing
  EXACT (2b/4b/6b/8b; full 4B tails
  2b31bd4d/4b31bd4d/6b31bd4d/8b31bd4d; 1B-row
  span suffix/subseq (0,0,0,0,0,0) + 4B-full-tail span
  suffix/subseq/tshare (3,3,3,3,3,3)x3 -- BOTH
  spans corroborated first-hand, supplement486.py
  25/0; GATE cites suffix-3s + R1-distinct
  alongside-only, code facts identical).
  M==RQ FULL-IDENTITY SAME-ORDER (lists equal,
  sets equal, overlap 16, positional 16/16;
  TAIL-IDENTITY ordered + set-eq 16/16; GATE
  adds string-identical SAME-ORDER + Q-vs-R lane-use
  flavor (M b28-31 by COL vs RQ b28-31 by ROW),
  code facts identical):
  evens 57->58 (b486 even FULL-identity; r80 ledger
  evens-57-held with no even band, agrees) +
  survey 36->37 (every-method RQ-vs-M).
  M/RQ-tails 16/16 ALL NEW vs P377T RM col-led
  AND RQ row-led tails (true novelty, both legs;
  GATE agrees both legs first-hand; code facts
  identical); RM-tails 16/16 ALL NEW both legs.
  AM/CM/M/QR/RM/RQ 0-overlap vs P377 (widths
  7/9, 5/5, 8/8, 1/1, 8/6, 8/8B).
  AC missing b4,b5+M7 (20,21,22,80-83);
  b0 const 9b, b1-3 04/00/00, b5 deducted,
  b84-87 08/b2/b2/54. CC missing b4,b5,M5b20 +
  b84-87 (TAIL-M5, no trailer); sig 49000000
  SAME-as-PB1 (differs from b485 41-SAME, recorded:
  b486 PB1 sig is 49); CC b52 const f3 PRESENT
  (M5 lane; differs from b485 b52-absent, recorded).
  QC missing b4,b5+QM8 8+R1 1; b0 const 9a,
  b1-3 04/00/00, b86 const bd, b87 const 4d.
  RC missing b4,b5+TM8 8+TR8 8; b0 const ab,
  b1 const 4f, b84-87 ab/31/bd/4d ring-wide
  EXACT (1 ring-wide). IMPL consts
  79/81/77/70 == Q-1126 census-script excl
  exact (no S-F lag; lag stays 44). VPOS
  8/6/11/18 == census exact (viewer convention:
  PBA/C10 -1 for b5-const; quad/T no deduction).
  Dispatch mirrors 6/6
  (T99527/99532/99537/99552/99567/99586) +
  C cites 6/6 text-exact; py formulas A
  b4=(0x77+2off)&FF / C raw-lencode+b5-const /
  Q raw-lencode+b5-0x86+(off>=43) /
  R ((0x2b+2off)&FF, 0x87+(off>=107)+(off>=235));
  C literals 43/135/107/235 == 0x2b/0x87/107/235;
  P3780-after-P377R-close both sides; scope
  hits N-out-of-scope 2/2 both sides + tail
  after R both sides; band-t 7501-7516 (base max
  7500), band-i 4557/4559/4562/4565 (base max
  4555), band-b 4556/4558/4560/4561/4563/4564
  (base max 4554); guards py 778->780/942->946,
  C 783->785/964->968, elif 50/else-if 0;
  numstat band rgramc.c +608/0, rgram.py +231/0,
  test_rgram.sh 1/1, PINS +58/0; quiz-bank
  +0/-0 in band range (Q-1126/A-961 banked in
  working tree uncommitted at file time; 231-class
  carry) verified first-hand.
  AC-QC both-keys 74 + sameval-pairs 35 ==
  GATE both=74/sameval=35 exact first-hand.
- Edges own script edges486.py (oracle +
  staged): EDGES-GREEN first rerun (pay84 1/1,
  pay88 347/347, lenok 92/92, A/C/Q forms
  16/16/10/10/64/64, cb0/qsplit 10/64,
  ring/ringraw 256/256, rsplit 256/256, b1set
  {4f}, b8487 256/256, 0 fails). b0 consts:
  A 9b x16 PLAIN-1SIG / Q 9a x64 / R ab x256.
  b5sets A{86} C{86} Q{86,87} (B5EDGE quad only;
  NO edge A/C anywhere this tier). Q b4 exact-set
  ab-step2 64/64 distinct WITH wrap (ff->01).
  R b4 exact-set 2b-step2 256vals/128uniq.
  ff-count 3 == [148351, 148479,
  148607] (0 A/C + 1 Q + 2 ring); edge pairs
  (148351,148352): ff/86->01/87 + (148479,
  148480): ff/87->01/88 + (148607,148608):
  ff/88->01/89, wrap-pairs verified.
  Spots: S0 73/86, S1 75/86, A 77/86->95/86,
  C 97/86->a9/86, Q ab/86->29/87, R head
  ab/2b/87 tail 29/89. Tail pin g-z148628:
  sha match, rawlen 104.
- GATE reconciliation (supplement486.py 25/0;
  AC-QC both/sameval added post-GATE, 74/35
  first-hand; tree untouched):
  for-added 29-set == GATE 29-set exact
  (programmatic, both sides); guards
  C-sing/C-ranges/elif/else-if all agree
  first-hand; py guard ABSOLUTES +2/+4 both sides
  (viewer anchored `^    if n == ` 778->780 +
  `^    if d+ <= n <= ` 942->946; GATE cites same
  778->780/942->946 absolute pattern, DELTAS +2/+4
  identical, code facts identical); numstat/bank-stat/
  P377-sigs/full-tail-spans/AC-QC-both-74/RC_N-70
  all agree first-hand. Ledger phrasing differs
  (GATE tabaudit-135 vs viewer tabaudit-191 check
  granularity + GATE TRUE-uniform-even-39th vs viewer
  uniform-39-NOT + S1-C10 GATE cites C10[0]-only 23
  vs viewer full-10 23x9+22x1) -- code facts identical,
  every metric both-corroborated.
- Seal: tiers sealed 2256 (+6), CLOSED-T10P
  prints 2162 (+6) both sides; offset +94 vs
  CLOSED-T10P stable (2162/2256; b485 was
  2156/2250), no slip. aae d6e27c97 pinned
  (band touches no aae sources). Wall: 0 `aea'
  on added lines (band diff rgramc.c+rgram.py
  verified first-hand; GATE wall 608 added lines
  0-hits class agrees: GATE raw-C 603 content + 5
  bare-blank = 608). 348 pins contiguous
  148281..148628, no RED anywhere. RC_N 70
  (P377->P378 72->70 VARIES; port anchor prev
  _T10P377RC_N=72 verified 1-hit).

Chain state for r81+ (viewer ledger; sweep ledgers separately owned):
- TRUE-uniform 39 (b486 NOT: C10 DIVERGE + B5EDGE
  split-tier + S1 SAME-sig-but-cells-diverge;
  even band).
  P338 stays OPEN, deferred to sweep accounting.
- S-F tables-lag 44 (no lag: impl 79/81/77/70 ==
  census-script excl).
- RQ==M evens 57->58 (b486 even FULL values-identical,
  lanes-differ flavor cf b477-style) / odds 60
  held (no odd band).
- Full/diff survey 37 (b486 identical FULL 36->37).
- Seal +94 vs CLOSED-T10P stable (2162/2256).
- aae d6e27c97 pinned-stable (band C port never
  touches aae sources). rgramc sha df829ab1
  (recorded, never transcribed).
- Content-line variance class 231 (rgram +231 carry;
  differs from b485 230-class, recorded).
- AC b84-87 08/b2/b2/54 (b85 0xb2 noted first-hand).

Scars (own fixes, all values untouched, rerun GREEN):
- edges486: two S0/S1 spot-value typos (own hex
  arithmetic pre-run, oracle-corrected 73/86 + 75/86)
  + header comment embeds to match.
- tabaudit486: tail-scope slice bound (99603->99606,
  N-scope print at 99605, coverage-only).
- No DISSENT on cut bytes; FLAG files name no r81
  band; no conflicting CLAIM/GATE/FLAG at filing
  (GATE-e988dbb5 reconciled post-landing; only
  ledger-convention deltas, never values).

Lane holds (untouched, local-only): lanes/encode-viewer @4495498c
(no commits this round -- viewer files quiz only).
