# VERIFY-33d2c85b b432 T10P324 pins 129489..129836 (348 pins) PASS

Seat viewer-r66, first-hand, tree @33d2c85b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r66.
Base 608c167f (b431 tip, 1926 tiers sealed; r65
VERIFY-608c167f PASS-filed prior round, base-use only,
respected). Band = f5a4d51d (py merge w2b@2b4193d8 partial,
+6 tiers, +64 pins) + 33d2c85b (C port, 1932
sealed). Trees manifest-identical to tips (git ls-tree
vs git ls-files cmp clean, 117/117 both; WT detached
at band, will return to lanes/encode-viewer at round
end).

Banked Next-P324 shape (r65 from A-833 FWD-check +
A-834) CONSUMED FIRST and corroborated below:
PB0 b7ce3001 pay84 NEW-sig (differs vs P323 heads
b7ce7001/02000000) @129489 / PB1 02000000 pay88
sig-eq-P323PB1 (41/88 diff) @129490 / PBA88 29000000
x16 @129491-506 / C10-region 02000000 pay88 x10
@129507-516 SAME-as-PB1-sig -- all exact.

- Build: make -C tree432/src/c BUILDDIR=$R/build432
  aae rgramc (absolute NVME path, -O2 -Wall -Wextra
  -std=c11), rc=0, 0 warnings. sha256 rgramc
  93cd6068 (== GATE) / aae d6e27c97 pinned (band
  touches no aae sources per numstat).
- RGRAMC-PYID 9628/9628 covered=9628/9628 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set, NVME workdir).
- RGRAM py 19256/19256 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19256/19256 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 19256/19256;
  cmp432.py; GATE claims sorted only, raw corroborated
  too).
- PINS 19258 rows (2 hdr + 19256, +64 vs base 19194;
  +64 = 32 for-Ns x2); PASS-names vs PINS-names xor 0
  py+C; PINS-baseN vs for-list xor 0 (4-way set-eq,
  seteq432.py). For-list union delta vs base +32/-0
  (9628 vs 9596):
  129489 129490 129491 129492 129498 129499 129505
  129506 129507 129508 129511 129512 129515 129516
  129517 129532 129533 129535 129536 129548 129549
  129564 129565 129580 129581 129644 129645 129663
  129664 129791 129792 129836
  (== GATE sampled list EXACT). Decomposition first-hand
  from the added set: 2 sing (129489/90) + A head-pair
  91/92 + mids 98/99 + 505/506... (A: offs 0,1,7,8,14,
  15) + C head 507/508 + mids 511/512 + 515/tail 516
  (C: offs 0,1,4,5,8,9; offs 2,3,6,7 = 509/510/513/514
  unsampled) + Q head 517/off0 + mids 532/533 +
  B5EDGE pair 535/536 (offs 18/19) + mids 548/549 +
  564/565 + tail 580 (10: offs 0,15,16,18,19,31,32,
  47,48,63; b5 edge off18->19 pair-covered first-hand)
  + R head 581 + sig-boundary pair 644/645 (offs
  63/64) + edge-pairs 663/664 + 791/792 + tail 836 (7:
  offs 0,63,64,82/83,210/211,255; both counter edges
  pair-covered, first-hand). 32x2=64 rows, range
  129489..129836 exact. PINS-new-N == for-added 32/32,
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle
  backend, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit432.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 160 PASS
  0 FAIL after 5 seat-script fixes (S1-uniform
  expectation flipped by runs -- uniform confirmed;
  r2r3-LCS suffix-vs-subsequence convention; RC extra
  scope; B0ROW row-led literal form; band-t slice
  incl S0/S1 region; all caught by runs).
  Inventory exactly the 12 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC; no F anywhere this tier,
  no FT46, no F0/F1, no QT (R11 carries b84-87 in QR),
  no RT/TT, no BM/BC, no M19/X19, no QB/PT/FM, no
  M42/X42/H42/L42).
  S0 168ch sig b7ce3001 NEW (32/84 payload diff vs
  P323S0 @ b2,4,5,20-23,25-33,36-39,41,64-68,70-75
  first-hand, NOT byte-equal; differs vs P323 heads
  b7ce7001/02000000) / S1 176ch sig 02000000 sig-eq-
  P323PB1 (41/88 payload diff vs P323S1 @
  b4,5,11,19,26,27,34,36-40,42,43,45-59,72-79,84-87,
  NOT byte-equal; [59]x10 vs own C10 assembled, NOT
  byte-equal; sig SAME-as-own-C10; differs vs own PB0),
  staged as full-payload singletons.
  AM 16/16 16ch (8B) distinct, CM 10/10 8ch (4B)
  distinct == GATE list first-hand, M 16/16 18ch (9B)
  distinct, QR 4/4 22ch (11B) distinct UNPAIRED, RM
  16/16 12ch (6B) distinct, RQ 16/16 18ch (9B)
  distinct UNPAIRED, no QT + no RT (B0ROW tails) + no F
  (no frag this tier).
  AC 78, b0-3 29000000 (b0 const 29), no b4/b5.
  C10-1SIG-88-TAIL sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 8ch first-hand;
  CC has no b4/b5, b5 const f3 full block via lencode).
  S1-vs-own-C10 staged per-cell (M4 b84-87, b4/b5
  lencode, each cell own assembly) [59]x10
  TRUE-UNIFORM count+position (cell0 59 @
  4,6-55,80-87 EXACT; positions identical all 10
  staged AND oracle; sig 02000000 both, NOT byte-equal
  -- 19th TRUE-uniform case on record, 18th excluding
  unverified P299; beyond-GATE values corroborated by
  oracle leg below; GATE/memo state cell0 only).
  QUAD88-1SIG-4R-NOFRAG-B5EDGE 1-sig 26000000 x64
  DIFFERS-from-PBA-sig (QC b0 const 26, b0 NOT in tab;
  b5 edge f3->f4 @off19, edge 129535 ff/f3 ->
  129536 01/f4, exactly 1 ff in 64; QM9 b13-17,80-83
  16/16 distinct NO frags + R11 b6-8,52-55,84-87
  rows 4/4 NO pairing pairwise-disjoint: r0/r1 share
  7B prefix 5f4c22c5da3764, differ in 8th byte b84
  (02 vs 92); r2/r3 full tuples unequal;
  tails b84-87 4/4 distinct 02bb2623/927c7623/
  60f8796f/6435f8a3, r01 pair-only-1B 0x23 @b87,
  b87 NOT const quad-wide [23,23,6f,a3];
  suffix-LCS r01-vs-r23 cross 0/0/0/0, suffix-LCS
  r2r3=0 with shared byte 0xf8 (subsequence-LCS 1;
  GATE "tail-LCS r2r3=1" holds under subsequence
  convention only -- mild prose note, same class as
  memo section-F lcs-gloss tokens; py comment "other
  pairs lcs=0" is suffix-true; full-LCS r01=8
  (prefix-7 + b87-23), full-LCS r2r3=3, cross
  02=1/03=1/12=0/13=1, all recorded first-hand).
  Ring 2SIG-B0ROW: 50020000 x64 (rows0-3) + 19020000
  x192 (rows4-15); TM6 b18,19,80-83 by COL RM 16/16 +
  TR9 b0,9-11,16,76-79 by ROW RQ 16/16 UNPAIRED;
  b0 row-led (RQ b0s 50x4/19x12 first-hand; C b0 via
  strcpy(_t6650, _T10P324RQ[r]) + _b4023[0]=pay[0]
  consumed; all 16 row heads verified); sig boundary
  off63/64 = 129644->129645 pinned in for-list;
  b1 const 02; b84-87 a17b14ad ring-wide NEW.
  M-vs-RQ TAILS-EQ 16/16 positional (M b80-83 == RQ
  b76-79 per index; full strings 0/16 identical; head
  bytes differ; running pattern: b414 full-eq, b416
  tail-eq, b418 full-eq, b420/b422
  string-eq-positions-differ, b424 tail-eq-positions-
  differ, b426 full-eq, b428/b430 string-eq-tails-
  split, b432 tails-eq-strings-differ). Even tier:
  no RQ==M ordinal (viewer evens convention).
  Sorted-unique + _N decls 78/82/66/71 match actual.
  Missing-sets EXACT: AC-10 [4,5,6,7,8,9,80-83] =
  b4,b5+M8 / CC-6 [4,5,84-87] = b4,b5+M4 /
  QC-22 [4,5,6,7,8,13-17,52-55,80-87] = b4,b5+QM9+
  R11 (b0 const 26, NOT missing) / RC-17
  [0,4,5,9,10,11,16,18,19,76-83] = b0,b4,b5+TM6+TR9.
  VPOS 9/5/22/17 == A-834 EXACT (PBA b4+M8 (b5 const
  deducted) / C10 b4+M4 / quad b4,b5+QM9+R11 (b5 edge
  counted) / T b0,b4,b5+TM6+TR9). Coverage unions
  exact every block (const U tab U {b4,b5} (+{b0} for
  T) == 88 x4, 0 overlap); each missing == region
  pay-index set minus {b4,b5} EXACT all 4 (A/C/Q/R
  region text re-derived first-hand, tab == region-idx
  minus {b4,b5} EXACT; B0ROW region includes pay[0]).
  Q legs M[m] + QR[q] both sides, NO F-row leg, NO
  F-scalar leg either side (no frag class this tier);
  R legs RM[c] + RQ[r] both sides, NO F anywhere in R
  (STANDARD-subscript verified: m/q = off&15/off>>4,
  c/r = off&15/off>>4). RM 16/16 distinct + RQ 16/16
  distinct, sets disjoint.
  P323 refs re-read: S0 b7ce7001 / S1 02000000 /
  PBA 2d000000 / C10 02000000 / QUAD 2d (QC b0 const) /
  T ring ad030000.
  PBA sig 29 NEW vs P323 2d (29000000 != 2d000000);
  QUAD 1SIG 26 DIFFERS-from-PBA-sig vs P323 1SIG 2d
  (rows NEW, single-sig structure continues; R11
  replaces R10 class). AM/CM/M/QR/RM/RQ 0-overlap vs
  P323 (prev lens 16/10/16/4/16/16); M-tails 16/16
  ALL NEW vs P323T (zero overlap vs P323M AND vs
  P323RM-tail8 AND vs P323RQ-tail8). Memo INCL PBA
  79 / C10 83 / quad 66 / T88 71 (A-834 re-read): impl
  78/82/66/71 = b5 const deducted on PBA/C10 (b5
  covered by lencode), b5 edge-varies counted on quad,
  b5 varies counted on T -- INCL arithmetic exact,
  geometry exact, PORT verdict stands. 27th
  consecutive tables-lag band (b432 pattern +1/+1/+0/
  +0: PBA/C10 lag 1 each, quad/T exact; running
  b412-b431 per GATE + r64/r65 records).
  Base temp maxes _t6634/_b4013/_i4014 (no reuse:
  band adds _t6635-6650 continuous-16 + _b4015/17/19/
  20/22/23 + _i4016/18/21/24, whole-file max _t6650,
  all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 129489 / S1 129490 / A 129491-506 / C 129507-516 /
  Q 129517-580 / R 129581-836): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C/Q both sides
  (raw, no counter literals in Q) + R explicit counter
  (b4=(0x5b+2off)&FF b5=0xf4+(off>=83)+(off>=211); py
  hex 0x5b/0xf4; C staged literals 91/244,
  re-derived: 91==0x5b, 244==0xf4; ring thresholds
  coincide with lencode byte boundaries first-hand) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A M8 b6-9,80-83;
  C M4 b84-87; Q QM9 b13-17,80-83 + R11 b6-8,52-55,
  84-87; R TM6 b18,19,80-83 by COL + TR9 b0,9-11,16,
  76-79 by ROW, b0 row-led 50x4/19x12; B0ROW verified
  in code both sides) + C guards
  `if ((n) == (129489))` / `(129490)` + 4 range
  guards exact + counter literals exact + C byte-index
  lists match py per block (A 16ch, C 8ch, Q 18/22ch,
  R 12/18ch B0ROW-split). C blocks carry T86982/
  86987/86992/87007/87022/87043 py-line mirrors
  (all 6 re-read: hit the exact py guard lines above);
  bounds + byte positions exact. Insert exact both
  sides: after T10P323R close (py CLOSED-then-guard;
  C block follows P323R close), at dispatch tail
  (N-out-of-scope fallthrough follows; 2 scope hits py
  + 2 scope hits C; early same-text guards at C
  155925 / py 53671 are the T4-plateau-B n<=1077 check,
  unrelated scope). Matches A-834 geometry (values
  re-checked in audit above; NO D dips: ownloop tags
  exactly the 6 P324 blocks).
- Edges own-loop ownloop432.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc): 348/348 CLOSED
  rc=0 (298 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P324R N=129836
  off=255. edges432.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 embedded b4/b5
  a3/f3, a5/f3 == raw lencode) + aform 16/16 (A head
  a7/f3 tail c5/f3 b5set {f3} NO step, 0 ff) + cform
  10/10 (C head c7/f3 tail d9/f3 b5set {f3} NO step,
  0 ff) + qform 64/64 + qb5 64/64 (Q head db/f3 edge
  off18->19 129535 ff/f3 -> 129536 01/f4 tail 59/f4
  b5set {f3,f4}, exactly 1 ff in 64, b5=f3+(off>=19)
  verified) + ring counter 256/256 + ringraw 256/256
  (head 5b/f4; 129663 off82 ff/f4 -> 129664 off83
  01/f5; 129791 off210 ff/f5 -> 129792 off211 01/f6;
  tail off255 59/f6; exactly 2 ff in 256; thresholds
  83/211 coincide with lencode high-byte steps
  first-hand); ff total x3 (1 Q + 2 R); ff-in-Q 1
  (edge pin only). S0/S1 embedded b4/b5 (a3/f3, a5/f3)
  match raw lencode. Odd-lencode 348/348 (346 + S0/S1
  embedded). No DISSENT on cut bytes (edges432.py
  EDGES-GREEN 160-check script rc=0, first run). Ring
  edges + tail 129836 in for-list + 2 PASS lines each
  py+C. Tail 129836: oracle rav sha 77702ed676fc9c08
  == PINS (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P324R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf432.py (cache path, 0 miss-warmed after
  ownloop) + secf432b.py (DIRECT tool, no cache):
  staged-vs-oracle 0/0/0/0 (129489 + 129141 + 129490 +
  129142); S0: oracle129489-vs-129141 32/84,
  codeS0-vs-P323S0 32/84, positions identical
  (differ-pos 2,4,5,20-23,25-33,36-39,41,64-68,70-75
  listed); DIRECT 32/84 agree. S1: oracle129490-
  vs-129142 41/88, codeS1-vs-P323S1 41/88, positions
  identical; DIRECT 41/88 agree. Triple-derived both
  pairs (same novel shape both tiers: 84/84/84/84 +
  88/88/88/88).
  S1-vs-own-C10 secf432c.py (oracle C10 cells n129507-
  516): [59]x10 TRUE-UNIFORM counts AND positions
  identical all 10 (cell0 pos 4,6-55,80-87 == staged
  EXACT; sig 02000000 both, NOT byte-equal).
  Byte-diff discipline observed throughout.
- C diff pure-add: numstat 608/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + PINS +64/+0 (clean
  append, 32 Ns x2) == GATE; raw C 608 total = 603
  content + 5 bare-blank / 0 del (verified bare `+`
  lines; GATE states "603 content + 5 bare-blank"
  correctly -- no overcount this band; full-digit
  norm ([0-9]+ -> N): C del-uniq 0 add-uniq
  167/164/166/163 across the 4 strip/dropempty
  variants (163 = strip+dropempty, as cited), missing
  0 every variant; py del-uniq 0 add-uniq 192 x4 (as
  cited), missing 0 (integrity intact,
  variant-robust); C-tempnorm 429 / py-tempnorm 206
  recorded. Band-level sole del = old for-line churn
  (1/1).
- Wall on band diff added lines (scope 608c167f..
  33d2c85b, 903 added lines == GATE): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files: rgramc.c 608/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1 (for-line), PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks,
  tier-comments `# T10P` 1832->1838 +6, 4-space
  dispatch-exact singletons 670->672 +2 /
  range-guards 726->730 +4 = +6 py AND C identical
  (== GATE method; unanchored literal counts 680->682
  +2 / 748->752 +4 py, 675->677 +2 / 748->752 +4 C;
  5-count C-vs-py singleton offset pre-existing,
  unchanged: 682-677 = 680-675 = 5), CLOSED T10P
  prints 1832->1838 +6 py + 1832->1838 +6 C (seal
  1926->1932 +6; offset +94 vs CLOSED-T10P: 1932-1838
  = 94, stable b401-b432). All agree (stated literal
  methods first-hand; no method-mix this band).
  Deliberate structural add: none (no elif/else-if
  either side: py elif 48->48 pre-existing elsewhere,
  C else-if 0->0; Q uses raw lencode, no counter
  literals).
- CONFIRM evidence (CONVERT-01 rule b): A-834-q916
  memo CONFIRM 67/68 + section-F (r2/r3 share f8)
  (own bed r3-P324 129489..129868 BAD=0 + own r3-P323,
  verifier v220.py 67/68 PASS, single FAIL = Q-claim
  witness; file present, counts verified; exact-value
  corroboration incl PB0 NEW-sig b7ce3001 32/84, PB1
  sig-eq-P323PB1 41/88 SAME-as-C10 59/88, PBA88-PLAIN-
  M8b6 sig-29 M8, C10-TAIL SAME-as-PB1-sig M4,
  QUAD88-1SIG-4R-NOFRAG-B5EDGE 1-sig-26 + R11 rows +
  r01-share-7B + r01-paironly-23 + b87-[23,23,6f,a3]
  + cross-suffix-lcs0 + r2r3-shared-f8 + QM7 + NO
  frags + b5-edge-off19 + M-tails NEW, T88-RING-
  2SIG-B0ROW + TM6/TR9 + b0-row-led-50x4/19x12 +
  sig-boundary-off63/64 + b84-87 a17b14ad + edges +
  consts; plus sheet-vs-tables const-count note: Q-916
  sheet 79/83/66/71 memo-exact, committed tables
  78/82/66/71 still deduct const-b5 on PBA/C10 --
  S-F arithmetic in tables only, geometry exact, PORT
  verdict stands; plus section-F: r2/r3 tails share
  byte 0xf8 (subsequence-LCS 1, suffix-LCS 0) with
  cross pairs suffix-0, comment-gloss only, bytes
  unaffected; M-vs-RQ tails-eq unmentioned by memo,
  batteries confirm, tier stands).
  Agrees with cport commit msg (PYID 9628, RGRAM 19256).
  No viewer P324 geometry answer on file at gate time
  (memo-only recon; this VERIFY is the viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b432 (own
  seat CLAIM only; exactly 1 GATE-33d2c85b; zero FLAG
  hits; even base b431 respected; b433 = sweep-r70
  turf untouched, used as nothing here). PROSE-01:
  all hex/counts above copied from own run output;
  GATE-33d2c85b re-read in FULL before filing (2 mild
  prose notes below, substance exact).
- RQ==M chain: b432 EVEN tails-eq-strings-differ (M
  9B b13-17,80-83 vs RQ 9B b0,9-11,16,76-79; tails
  b80-83==b76-79 16/16 positional; full rows 0/16
  identical). No ordinal (viewer evens convention:
  b414-full/b416-tail/b418-full/b420-strdiff/b422-
  strdiff/b424-tail-pos-differ/b426-full/b428-string-
  split/b430-string-split/b432-tails-eq-strings-
  differ).
- TRUE-uniform chain: 19th case (18th excl P299):
  P324 S1-vs-C10 [59/88]x10 staged+oracle NEW this
  band (GATE/memo cell0-only; beyond-GATE finding,
  code GREEN since gated artifact == verified
  artifact).

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 mild prose-level notes (tier-count absolute
method -- GATE 4-space dispatch-exact vs unanchored
literals, deltas agree every side; tail-LCS r2r3=1
holds under subsequence convention (shared f8),
suffix-convention value 0 -- same token class as memo
section-F lcs-gloss issues; code GREEN since gated
artifact == verified artifact).
