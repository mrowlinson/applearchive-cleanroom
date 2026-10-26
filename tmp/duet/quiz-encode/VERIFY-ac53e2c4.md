# VERIFY-ac53e2c4 b485 T10P377 pins 147933..148280 (348 pins) PASS

Seat viewer-r80, first-hand, tree @ac53e2c49c973c0d470c9167da1d988f75339e6f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r80.
Base d20309ab (b484 tip, 2244 tiers sealed; this
seat's VERIFY-d20309ab PASS-filed r79,
base-use only, respected). Band = 6710f728 (py
merge w2b@c37c2d277264f67ef64ee6be77e69a58495a98a2, +6 tiers, +58 pins;
commit msg verified via git log + rev-parse at boot) + ac53e2c4 (C
port; parent == 6710f728 verified via git
rev-list --parents). Chain d20309ab -> 6710f728
-> ac53e2c4, every sha via git log at takeover,
NO gap-jump. GATE-ac53e2c4 PASS-functional filed
by sweep-r83 (post-battery) -- reconciled
first-hand below (values agree; uniform-count +
guard-pattern phrasing differ, code facts identical). NO other
GATE/FLAG on b485 at file time (FLAGs on file are
SUPERSEDED holds; no DISSENT names bandbeth tiers;
sweep notes viewer CLAIM-r80 FRONTIER post-gate turf
per pipeline order, uncontested).

Banked Next-P377 shape (Q-1125 + A-960-q1125-P377, both read first-hand
at boot) CONSUMED FIRST and VERIFIED
first-hand EXACT vs Q-1125/A-960 before any
battery step: PB0 df017f20 @147933 (S0 head;
NEW-sig 42/84 vs P376PB0 @ n147585, sig b0-3 ALL
IN diff, positions
[0-5,19-24,26,27,29,30,36,37,60-83]
first-hand, NOT byte-equal) + PB1 41000000
@147934 (S1 head; NEW-sig 66/88 vs
P376PB1 @ n147586, sig b0 IN diff with b1-3
same, positions [0,4,5,19,26-87]
first-hand, NOT byte-equal; diffs
vs own C10 cells 36x10 staged+oracle;
S1 SIG-SAME own C10 (41-vs-41) and own PB0-differs
(41-vs-df); S1 SIG-SAME own C10 DIFFERS from b484
DIFFERS-pattern, recorded; viewer TRUE-uniform
stays 39 (odd band): NOT TRUE-UNIFORM under
viewer convention (uniform-cells required; C10
10/10 DIVERGE + B5EDGE quad split-tier; P338
uniform-rule dispute stays DEFERRED to sweep
accounting, never re-litigated) +
PBA88-PLAIN-M9b51 sig d8040000 x16 @147935-950
(b0 const 0xd8 first-hand, b5 const 0x83 NO step
NO edge, 16/16 distinct NO pair) + C10-region
41000000 x10 @147951-960 SAME-as-PB1-sig
(b0 const 0x41, b5 const 0x83, 10/10 diverge,
TAIL-M5 b52 lane, NO trailer in CC) --
all corroborated against lane code both sides plus
Q-1125/A-960 before any battery step (py==C
S0/S1 staged strings; S0/S1 staged-eq-oracle
True/True first-hand; C10 staged-vs-oracle
10/10 DIVERGE GREEN first-run; no bank-miss).

- Build: seat-private build485/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 7c83d6db...
  (recorded first-hand here, never
  hand-transcribed; == GATE-recorded 7c83d6db
  first-hand).
- RGRAMC-PYID 11206/11206 covered=11206/11206
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, ct-cache;
  +29 vs b484 11177; unc=0).
- RGRAM py 22412/22412 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 22412/22412 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (22412/22412, sorted +
  raw identical; cmp485.py GREEN).
- PINS-RGRAM cells set-eq 22412/22412 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq485.py GREEN, 15/15). PINS 22414 lines
  first-hand (2 hdr + 22412 rows; base 22356
  lines / 22354 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 11177->11206 +29/-0 (python
  sets on `for s in ...; do` exact token parse,
  trailing-';' glued last token handled, never
  comm; base tail ...147932, band tail ...148280):
  147933 147934 147935 147936 147942 147943
  147949 147950 147951 147952 147955 147956
  147959 147960 147961 147967 147968 147977
  147993 148008 148024 148025 148095 148096
  148160 148223 148224 148225 148280 (== GATE
  29-set exact, first-hand both sides; range
  147933..148280 exact).
  29 = 2 sing (147933 147934 offs 0/1) + A 6
  (head pair 147935/147936 offs 0/1 + mid pair
  147942/147943 offs 7/8 + tail pair 147949/
  147950 offs 14/15; offs 2-6,9-13 unsampled
  first-hand; NO mid-single; b5 const 83 NO
  edge) + C 6 (head pair 147951/147952 offs 0/1
  + mid pair 147955/147956 offs 4/5 + tail pair
  147959/147960 offs 8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 83 NO edge) + Q 7 (head
  147961 off0 + B5EDGE pair 147967/147968 offs
  6/7 + boundary off16 147977 + boundary off32
  147993 + mid off47 148008 + tail off63 148024;
  b5 83->84 edge; NO step at 15/16 or 31/32;
  NO D-class dips) + R 8 (head 148025 off0 +
  edge pair 148095/148096 offs 70/71 + mid
  off135 148160 + edge pair 148223/148224 offs
  198/199 + mate off200 148225 + tail off255
  148280; offs 1-69,72-134,136-197,201-254
  unsampled; both counter edges pair-covered,
  first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  22412-22354.
- SMOKE-GREEN rc=0 (6/6 PASS: aar
  encode/decode/bytes + aea encrypt/decrypt/bytes,
  default oracle backend, no BACKEND var, NVME
  workdir).
- UNITS-GREEN rc=0 (22/22 PASS,
  tests/test_units.py, synthetic shape tests, no
  oracle).
- Tables audit own script tabaudit485.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 191 PASS 0 FAIL first run (no own-script
  fixes; tree untouched).
  Inventory: exactly the 12 band
  tables both sides (S0/S1/AM/AC/CM/CC/M/QR/QC/
  RM/RQ/RC; no F/FT, no F0/F1, no BM/BC, no
  M19/X19, no M42/X42/H42/L42, no QB/PT/FM, no
  RT/TT (ring, not ROWTAIL), no QT (R1 carries
  b84 in-row, no const trailer); no _T10P377C
  in either tree -- base P376 has no _T10P376C
  either, nothing carried forward; 12 symbols
  enumerated first-hand).
  S0 168ch sig df017f20 NEW-sig (42/84 payload
  diff vs P376S0, positions first-hand, sig
  b0-3 ALL IN diff, NOT byte-equal) / S1 176ch
  sig 41000000 NEW-sig (66/88 payload diff vs
  P376S1, positions first-hand, sig b0 IN diff,
  b1-3 same-sig NOT in diff, NOT byte-equal; vs
  own C10 cells 36x10 staged+oracle; S1
  SIG-SAME own C10 (41-vs-41) and own PB0
  (41-vs-df); 39 stays (odd band)).
  AM 16/16 9ch distinct, CM 10/10 5ch M5 diverge
  (b52 mid-body M5 lane + b84-87, all 10
  distinct), M 16/16 8ch QM8 distinct, QR 4/4 1ch
  R1 rows 6a/8a/aa/ca exact, RM 16/16 6ch
  TM6 distinct, RQ 16/16 8ch TR8 distinct.
  AC 77, CC 81, QC 77, RC 72; C _N decls
  77/81/77/72 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap,
  mtab/rq-tab computed).
  QM8 shared 16/16 x3 vs row0 (48/48 cells,
  8 lanes b6,7,8,9,80-83, per-row 16
  distinct, NO frags; positions FIRST-this-lane
  never claimed -- staged P337Q/P353Q per code
  comment). R1 rows 4/4 distinct NO pairing
  EXACT (6a/8a/aa/ca; full 4B tails
  6ae94505/8ae94505/aae94505/cae94505; 1B-row
  span suffix/subseq (0x6) + 4B-full-tail span
  suffix/subseq/tshare (3,3,3,3,3,3)x3 -- BOTH
  spans corroborated first-hand, supplement485.py
  24/0; GATE cites trailing=TSHARE=subseq
  all-3s + 1B-row 0x6 alongside-only, code facts
  identical).
  M==RQ FULL-IDENTITY SAME-ORDER (lists equal,
  sets equal, overlap 16, positional 16/16;
  TAIL-IDENTITY ordered + set-eq 16/16; GATE
  adds HEAD-IDENTITY ordered 16/16 + lanes-differ
  flavor cf b477, code facts identical):
  odds 59->60 (b473 tails-shared precedent:
  identical degree counts; GATE: 60th odd-band
  instance, 14th FULL-identity, agrees) +
  survey 35->36 (every-method RQ-vs-M).
  M/RQ-tails 16/16 ALL NEW vs P376T RM col-led
  AND RQ row-led tails (true novelty, both legs;
  GATE adds RQ-tails 16/16 NEW both legs --
  mirrored first-hand here: RQ-tails-NEW 16/16
  vs P376T RM + 16/16 vs P376T RQ; code facts
  identical); RM-tails 16/16 ALL NEW both legs.
  AM/CM/M/QR/RM/RQ 0-overlap vs P376 (widths
  9/9, 5/4, 8/9, 1/2, 6/7, 8/9B).
  AC missing b4,b5+M9 (51,52,53,54,55,80-83);
  b0 const d8, b1-3 04/00/00, b5 deducted,
  b84-87 1c/e9/3c/0d. CC missing b4,b5,M5b52 +
  b84-87 (TAIL-M5, no trailer); sig 41000000
  SAME-as-PB1 (differs from b484 45-DIFFERS,
  recorded); CC b52 absent (M5 lane).
  QC missing b4,b5+QM8 8+R1 1; b0 const 10,
  b1-3 04/00/00, b86 const 45, b87 const 05.
  RC missing b4,b5+TM6 6+TR8 8; b0 const e0,
  b1 const 41, b84-87 ea/e9/45/05 ring-wide
  EXACT (1 ring-wide). IMPL consts
  77/81/77/72 == Q-1125 census-script excl
  exact (no S-F lag; lag stays 44). VPOS
  10/6/11/16 == census exact (viewer convention:
  PBA/C10 -1 for b5-const; quad/T no deduction).
  Dispatch mirrors 6/6
  (T99296/99301/99306/99321/99336/99355) +
  C cites 6/6 text-exact; py formulas A
  b4=(0xbf+2off)&FF / C raw-lencode+b5-const /
  Q raw-lencode+b5-0x83+(off>=7) /
  R ((0x73+2off)&FF, 0x84+(off>=71)+(off>=199));
  C literals 115/132/71/199 == 0x73/0x84/71/199;
  P3770-after-P376R-close both sides; scope
  hits N-out-of-scope 2/2 both sides + tail
  after R both sides; band-t 7485-7500 (base max
  7484), band-i 4547/4549/4552/4555 (base max
  4545), band-b 4546/4548/4550/4551/4553/4554
  (base max 4544); guards py 776->778/938->942,
  C 781->783/960->964, elif 50/else-if 0;
  numstat band rgramc.c +608/0, rgram.py +230/0,
  test_rgram.sh 1/1, PINS +58/0; bank stat
  +289/-1 verified first-hand (230-class carry).
- Edges own script edges485.py (oracle +
  staged): EDGES-GREEN first run (pay84 1/1,
  pay88 347/347, lenok 92/92, A/C/Q forms
  16/16/10/10/64/64, cb0/qsplit 10/64,
  ring/ringraw 256/256, rsplit 256/256, b1set
  {41}, b8487 256/256, 0 fails). b0 consts:
  A d8 x16 PLAIN-1SIG / Q 10 x64 / R e0 x256.
  b5sets A{83} C{83} Q{83,84} (B5EDGE quad only;
  NO edge A/C anywhere this tier). Q b4 exact-set
  f3-step2 64/64 distinct WITH wrap (ff->01).
  R b4 exact-set 73-step2 256vals/128uniq.
  ff-count 3 == [147967, 148095,
  148223] (0 A/C + 1 Q + 2 ring); edge pairs
  (147967,147968): ff/83->01/84 + (148095,
  148096): ff/84->01/85 + (148223,148224):
  ff/85->01/86, wrap-pairs verified.
  Spots: S0 bb/83, S1 bd/83, A bf/83->dd/83,
  C df/83->f1/83, Q f3/83->71/84, R head
  e0/73/84 tail 71/86. Tail pin g-z148280:
  sha match, rawlen 104.
- GATE reconciliation (supplement485.py 24/0;
  RQ-tails-NEW mirror added post-GATE, 16/16 both
  legs first-hand; tree untouched):
  for-added 29-set == GATE 29-set exact
  (programmatic, both sides); guards
  C-sing/C-ranges/elif/else-if all agree
  first-hand; py guard ABSOLUTES differ by pattern
  (viewer anchored `^    if n == ` 776->778 +
  `^    if d+ <= n <= ` 938->942 vs GATE
  unanchored `if n == ` 786->788 + `<= n <=`
  960->964; DELTAS +2/+4 identical both patterns,
  10/22 nested-guard offset pre-existing base AND
  band, code facts identical); numstat/bank-stat/
  P376-sigs/full-tail-spans/AC-QC-30-47/RC_N-72
  all agree first-hand. Ledger phrasing differs
  (GATE 4B-tail span suffix-only + sweep
  TRUE-uniform-28th + VPOS-lanes flavor + T-b5set
  {132,133,134} per-cell-implied; viewer 1B+4B
  spans + viewer-uniform-39-NOT + VPOS-missing
  convention + Q-b5set asserted/T-b5set
  formula-implied) -- code facts identical,
  every metric both-corroborated.
- Seal: tiers sealed 2250 (+6), CLOSED-T10P
  prints 2156 (+6) both sides; offset +94 vs
  CLOSED-T10P stable (2156/2250; b484 was
  2150/2244), no slip. aae d6e27c97 pinned
  (band touches no aae sources). Wall: 0 `aea'
  on added lines (band diff rgramc.c-only
  verified first-hand; GATE wall 892 added lines
  0 hits agrees). 348 pins contiguous
  147933..148280, no RED anywhere. RC_N 72
  (P376->P377 70->72 VARIES; port anchor prev
  _T10P376RC_N=70 verified 1-hit).

Chain state for r80+ (viewer ledger; sweep ledgers separately owned):
- TRUE-uniform 39 (b485 NOT: C10 DIVERGE + B5EDGE
  split-tier + S1 SAME-sig-but-cells-diverge).
  P338 stays OPEN, deferred to sweep accounting.
- S-F tables-lag 44 (no lag: impl 77/81/77/72 ==
  census-script excl).
- RQ==M evens 57 held (no even band) / odds 60
  (b485 identical FULL values-identical, lanes-differ
  flavor cf b477, 59->60).
- Full/diff survey 36 (b485 identical FULL 35->36).
- Seal +94 vs CLOSED-T10P stable (2156/2250).
- aae d6e27c97 pinned-stable (band C port never
  touches aae sources). rgramc sha 7c83d6db
  (recorded, never transcribed).
- Content-line variance class 230 (bank +230 carry;
  differs from b484 231-class, recorded).
- AC b84-87 1c/e9/3c/0d (b85 0xe9 noted first-hand).

Scars (own fixes, all values untouched, rerun GREEN):
- probe485: tlcs draft typo (stray tokens in zip,
  caught pre-run, fixed) + edges485 header comment
  wording (edge-pair description, comment-only).
- No DISSENT on cut bytes; FLAG files name no r79/r80
  band; no conflicting CLAIM/GATE/FLAG at filing
  (GATE-ac53e2c4 reconciled post-battery; only
  ledger-convention deltas, never values).

Lane holds (untouched, local-only): lanes/encode-viewer @4495498c
(no commits this round -- viewer files quiz only).
