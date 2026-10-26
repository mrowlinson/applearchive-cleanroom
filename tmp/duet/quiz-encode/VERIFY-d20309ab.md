# VERIFY-d20309ab b484 T10P376 pins 147585..147932 (348 pins) PASS

Seat viewer-r79, first-hand, tree @d20309abbed55b1f707520d789978bab6158a812,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r79.
Base 246d3408 (b483 tip, 2238 tiers sealed; this
seat's VERIFY-246d3408 PASS-filed r78,
base-use only, respected). Band = 5101a773 (py
merge w2b@6f57f6dc293653fe30ee582b06213a8348eca78b, +6 tiers, +58 pins;
commit msg verified via git log + rev-parse at boot) + d20309ab (C
port; parent == 5101a773 verified via git
rev-list --parents). Chain 246d3408 -> 5101a773
-> d20309ab, every sha via git log at takeover,
NO gap-jump. GATE-d20309ab PASS-functional filed
by sweep2-r84 (mid-battery) -- reconciled
first-hand below (values agree; tail-span + ledger
phrasing differ, code facts identical). NO other
GATE/FLAG on b484 at file time (FLAGs on file are
SUPERSEDED holds; DISSENTs q846/847/849 name
writer tiers only).

Banked Next-P376 shape (Q-1123 NEXT + Q-1124 +
A-959-q1124-P376, all read first-hand) CONSUMED FIRST and VERIFIED
first-hand EXACT vs Q-1124/A-959 before any
battery step: PB0 dcb0d222 @147585 (S0 head;
NEW-sig 36/84 vs P375PB0 @ n147237, sig b0-3 ALL
IN diff, positions
[0-11,13-18,44-47,50,51,56-59,76-83]
first-hand, NOT byte-equal) + PB1 44000000
@147586 (S1 head; NEW-sig 80/88 vs
P375PB1 @ n147238, sig b0 IN diff with b1-3
same, positions [0,4-55 excl 12,60-87]
first-hand, NOT byte-equal; diffs
vs own C10 cells 41/40/41x8 staged+oracle;
sig b0 IN diff; S1 SIG-DIFFERS own C10 (44-vs-45)
and own PB0 (44-vs-dc); viewer TRUE-uniform
stays 39 (even band): NOT TRUE-UNIFORM under
viewer convention (uniform-cells required; C10
10/10 DIVERGE + SIG-DIFFERS PB1; P338
uniform-rule dispute stays DEFERRED to sweep
accounting, never re-litigated) +
PBA88-PLAIN-M9b29 sig 29040000 x16 @147587-602
(b0 const 0x29 first-hand, b5 const 81 NO step
NO edge, 16/16 distinct NO pair) + C10-region
45000000 pay88 x10 @147603-612 DIFFERS-from-PB1-sig
(b0 const 0x45, b5 const 81, 10/10 diverge,
TAIL-M4 NO trailer in CC) -- all
corroborated against lane code both sides plus
Q-1124/A-959 + NOTE-cport-r68-hb1 before any battery step (py==C
S0/S1 staged strings; S0/S1 staged-eq-oracle
True/True first-hand; C10 staged-vs-oracle
10/10 DIVERGE GREEN first-run; no bank-miss).

- Build: seat-private build484/{aae,rgramc},
  rc=0, 0 warnings. aae sha256 d6e27c97...
  (pinned stable continues, verified
  programmatically; band touches no aae sources
  per numstat). rgramc sha256 b3fe0725...
  (recorded first-hand here, never
  hand-transcribed).
- RGRAMC-PYID 11177/11177 covered=11177/11177
  GREEN rc=0 (tests/test_rgramc_fast.py, RGRAMC=
  seat binary, NVME workdir, TMPDIR=NVME scratch;
  +29 vs b483 11148).
- RGRAM py 22354/22354 PASS 0 FAIL RGRAM-GREEN
  rc=0 (tests/test_rgram_fast.py, NVME workdir,
  ct-cache).
- RGRAM C 22354/22354 PASS 0 FAIL RGRAM-GREEN
  rc=0 (RGRAM_BIN=seat binary, NVME workdir);
  C-py PASS-set cmp-equal (22354/22354, sorted +
  raw identical; cmp484.py GREEN).
- PINS-RGRAM cells set-eq 22354/22354 (xor 0 all
  4 ways: for^pass-py for^pass-C py^C for^pins;
  seteq484.py GREEN, 15/15). PINS 22356 lines
  first-hand (2 hdr + 22354 rows; base 22298
  lines / 22296 rows; line delta +58 = row delta
  +58 = 29 for-N x2).
  For-list union 11148->11177 +29/-0 (python
  sets on `for s in ...; do` exact token parse,
  trailing-';' glued last token handled, never
  comm; base tail ...147584, band tail ...147932):
  147585 147586 147587 147588 147595 147596
  147601 147602 147603 147604 147607 147608
  147611 147612 147613 147628 147629 147644
  147645 147660 147676 147677 147711 147712
  147776 147839 147840 147841 147932 (= GATE
  29-set exact, first-hand both sides; range
  147585..147932 exact).
  29 = 2 sing (147585 147586 offs 0/1) + A 6
  (head pair 147587/147588 offs 0/1 + mid pair
  147595/147596 offs 8/9 + tail pair 147601/
  147602 offs 14/15; offs 2-7,10-13 unsampled
  first-hand; NO mid-single; b5 const 81 NO
  edge) + C 6 (head pair 147603/147604 offs 0/1
  + mid pair 147607/147608 offs 4/5 + tail pair
  147611/147612 offs 8/9; offs 2,3,6,7 unsampled
  first-hand; b5 const 81 NO edge) + Q 7 (head
  147613 off0 + mid pair 147628/147629 offs
  15/16 + mid pair 147644/147645 offs 31/32 +
  mid 147660 off47 + tail 147676 off63; b5 const
  81 NO step NO edge; NO mid-single; NO edge
  anywhere this tier) + R 8 (head 147677 off0 +
  edge pair 147711/147712 offs 34/35 + mid
  147776 off99 + edge triple 147839/147840/
  147841 offs 162/163/164 (pre-edge+edge+
  post-edge) + tail 147932 off255; offs 1-33,
  36-98,100-161,165-254 unsampled; both counter
  edges pair-covered, first-hand).
  PINS adds = same 29 tier pins (2 rows each,
  full-range numeric filter, 0 out-of-range).
  Each for-N yields 2 PASS lines; 29x2 = 58 =
  22354-22296.
- SMOKE-GREEN rc=0 (6/6 PASS: aar
  encode/decode/bytes + aea encrypt/decrypt/bytes,
  default oracle backend, no BACKEND var, NVME
  workdir).
- UNITS-GREEN rc=0 (22/22 PASS,
  tests/test_units.py, synthetic shape tests, no
  oracle).
- Tables audit own script tabaudit484.py (parses
  tree sources, C-vs-py + derived): TABAUDIT-
  GREEN 185 PASS 0 FAIL (1 own-script fix:
  S0-sig-assert b0b1->b0b1b2b3 IN-diff
  (full-sig NEW); tree untouched).
  Inventory: exactly the 12 band
  tables both sides (S0/S1/AM/AC/CM/CC/M/QR/QC/
  RM/RQ/RC; no F/FT, no F0/F1, no BM/BC, no
  M19/X19, no M42/X42/H42/L42, no QB/PT/FM, no
  RT/TT (ring, not ROWTAIL), no QT (R2 carries
  b84,85 in-row, no const trailer); no _T10P376C
  in either tree -- base P375 has no _T10P375C
  either, nothing carried forward; 12 symbols
  enumerated first-hand).
  S0 168ch sig dcb0d222 NEW-sig (36/84 payload
  diff vs P375S0, positions first-hand, sig
  b0-3 ALL IN diff, NOT byte-equal) / S1 176ch
  sig 44000000 NEW-sig (80/88 payload diff vs
  P375S1, positions first-hand, sig b0 IN diff,
  b1-3 same-sig NOT in diff, NOT byte-equal; vs
  own C10 cells 41/40/41x8 staged+oracle; S1
  SIG-DIFFERS own C10 (44-vs-45) and own PB0
  (44-vs-dc); 39 stays (even band)).
  AM 16/16 9ch distinct, CM 10/10 4ch M4 diverge
  (b84,85,86,87 mid-body M4 lane, all 10
  distinct), M 16/16 9ch QM9 distinct, QR 4/4 2ch
  R2 rows aeee/ceee/eeee/0eef exact, RM 16/16 7ch
  TM7 distinct, RQ 16/16 9ch TR9 distinct.
  AC 77, CC 82, QC 75, RC 70; C _N decls
  77/82/75/70 match actual; byte-coverage unions
  exact every block (88/88/88/88, 0 overlap,
  mtab/rq-tab computed).
  QM9 shared 16/16 x3 vs row0 (48/48 cells,
  9 lanes b40,41,42,43,44,80-83, per-row 16
  distinct, NO frags; positions FIRST this
  lane). R2 rows 4/4 distinct NO pairing
  EXACT (aeee/ceee/eeee/0eef; full tails
  aeee3df8/ceee3df8/eeee3df8/0eef3df8; 2B-row
  span suffix/subseq/tshare (1,1,0,1,0,0) +
  4B-full span (3,3,2,3,2,2) -- BOTH spans
  corroborated first-hand, supplement484.py
  18/0; GATE cites 4B span, viewer cites 2B
  span, code facts identical (b483 precedent)).
  M==RQ FULL-IDENTITY SAME-ORDER (lists equal,
  sets equal, overlap 16, positional 16/16;
  TAIL-IDENTITY ordered + set-eq 16/16):
  evens 56->57 (b473 tails-shared precedent:
  identical degree counts) + survey 34->35
  (every-method RQ-vs-M). M/RM-tails 16/16 ALL
  NEW vs P375T RM col-led AND RQ row-led tails
  (true novelty, both legs). AM/CM/M/QR/RM/RQ
  0-overlap vs P375 (widths 9/4/9/2/7/9B vs
  7/5/8/1/6/8B).
  AC missing b4,b5+M9 (29,30,31,34,35,80-83);
  b0 const 29, b1-3 04/00/00, b5 deducted,
  b84-87 ca/3b/d2/67. CC missing b4,b5,84-87
  (TAIL-M4, no trailer); sig 45000000;
  b52 const 22; CC HAS b80-83 consts
  c7/f4/c3/86 (GATE-cited, verified first-hand).
  QC missing b4,b5+QM9 9+R2 2; b0 const d8,
  b1-3 04/00/00, b86 const 3d, b87 const f8.
  RC missing b4,b5+RM7 7+RQ9 9; b0 const d8,
  b1 const 41, b84-87 2e/ef/3d/f8. IMPL consts
  77/82/75/70 == Q-1124 census-script excl
  exact (no S-F lag; lag stays 44). VPOS
  10/5/12/18 == census exact.
  P375 sigs: PBA 08x6/10x1/24x9 ORDERED (oracle
  b0 first-hand) so P376 sig-29 NEW; P375 C10
  sig 45 REPEAT (P376 C10 sig-45 REPEATs-P375C10;
  S1 does NOT repeat). Dispatch mirrors 6/6
  (T99065/99070/99075/99090/99105/99125) +
  C cites 6/6 text-exact; py formulas A
  b4=(0x07+2off)&FF / C raw-lencode+b5-const /
  Q raw-lencode+b5-const-81-NO-edge / R
  ((0xbb+2off)&FF, 0x81+(off>=35)+(off>=163));
  C literals 187/129/35/163 == 0xbb/0x81/35/163;
  P3760-after-P375R-close both sides; scope
  hits N-out-of-scope 2/2 both sides + tail
  after R both sides; band-t 7469-7484 (base max
  7468), band-i 4537/4539/4542/4545 (base max
  4535), band-b 4536/4538/4540/4541/4543/4544
  (base max 4534); guards py 774->776/934->938,
  C 779->781/956->960, elif 50/else-if 0;
  numstat band rgramc.c +608/0, rgram.py +231/0,
  test_rgram.sh 1/1, PINS +58/0; bank stat
  +290/-1 verified first-hand (231-class carry).
- Edges own script edges484.py (oracle +
  staged): EDGES-GREEN first run (pay84 1/1,
  pay88 347/347, lenok 92/92, A/C/Q forms
  16/16/10/10/64/64, cb0/qsplit 10/64,
  ring/ringraw 256/256, rsplit 256/256, b1set
  {41}, b8487 256/256, 0 fails). b0 consts:
  A 29 x16 PLAIN-1SIG / Q d8 x64 / R d8 x256.
  b5sets A{81} C{81} Q{81} (NO edge anywhere
  this tier). Q b4 exact-set 3b-step2 64/64 NO
  wrap no-ff (3b..b9). R b4 exact-set bb-step2
  256vals/128uniq. ff-count 2 == [147711,
  147839] (0 A/C/Q + 2 ring); edge pairs
  (147711,147712): ff/81->01/82 + (147839,
  147840): ff/82->01/83, wrap-pairs verified.
  Spots: S0 03/81, S1 05/81, A 07/81->25/81,
  C 27/81->39/81, Q 3b/81->b9/81, R head
  d8/bb/81 tail b9/83. Tail pin g-z147932:
  sha match, rawlen 104.
- GATE reconciliation (supplement484.py 18/0;
  2 own-script fixes: AM-row-vs-oracle-b0 range
  slip (P372 range used for P375); numstat range
  base..port + for-added file; tree untouched):
  for-added 29-set == GATE 29-set exact;
  guards/C-counts/numstat/bank-stat/P375-sigs/
  CC-b80-83/full-tail-spans/AC-QC-42 all agree
  first-hand. Ledger phrasing differs (GATE
  4B-tail span + "sameval-42"; viewer 2B-row
  span + VPOS convention) -- code facts
  identical, tail metric both-corroborated.
- Seal: tiers sealed 2244 (+6), CLOSED-T10P
  prints 2150 (+6) both sides; offset +94 vs
  CLOSED-T10P stable (2150/2244; b483 was
  2144/2238), no slip. aae d6e27c97 pinned
  (band touches no aae sources). Wall: 0 `aea'
  on added lines (band diff rgramc.c-only
  verified first-hand). 348 pins contiguous
  147585..147932, no RED anywhere. RC_N 70
  (P375->P376 72->70 VARIES; port anchor prev
  _T10P375RC_N=72 verified 1-hit).

Chain state for r79+ (viewer ledger; sweep ledgers separately owned):
- TRUE-uniform 39 (b484 NOT: C10 DIVERGE + SIG-DIFFERS).
  P338 stays OPEN, deferred to sweep accounting.
- S-F tables-lag 44 (no lag: impl 77/82/75/70 ==
  census-script excl).
- RQ==M evens 57 (b484 identical FULL, same-lanes,
  same-order 56->57) / odds 59 held (no odd band).
- Full/diff survey 35 (b484 identical FULL 34->35).
- Seal +94 vs CLOSED-T10P stable (2150/2244).
- aae d6e27c97 pinned-stable (band C port never
  touches aae sources). rgramc sha b3fe0725
  (recorded, never transcribed).
- Content-line variance class 231 (bank +231 carry).
- AC b84-87 ca/3b/d2/67 (b86 0xd2 noted first-hand).

Scars (own fixes, all values untouched, rerun GREEN):
- tabaudit484: 1 own-assert fix (S0 sig b0b1->b0b1b2b3
  IN-diff, full-sig NEW) + rerun (185/0).
- supplement484: PBA-oracle range slip (P372 range for
  P375) + numstat range (merge..port -> base..port) +
  for-added file (full-nums -> .added); rerun 18/0.
- No DISSENT on cut bytes; FLAG files name no r79 band;
  no conflicting CLAIM/GATE/FLAG at filing (GATE-d20309ab
  reconciled mid-battery).

Lane holds (untouched, local-only): lanes/encode-viewer @4495498c
(no commits this round -- viewer files quiz only).
