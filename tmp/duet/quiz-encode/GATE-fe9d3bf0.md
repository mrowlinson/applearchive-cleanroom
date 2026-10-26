# GATE fe9d3bf0 b424 T10P316 pins 126705..127052 (1884 tiers) PASS-functional

Seat sweep2-r69, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r69/w424 @fe9d3bf0.
Band = b1e113f1 (py merge w2b@1b619914 partial, +6 tiers, +74 pins)
+ fe9d3bf0 (C port). Base 5321f012 (b423 tip, 1878 tiers sealed,
GATE-filed PASS-functional by odd seat).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both);
w424 +__pycache__ battery byproduct after runs, w423base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build424/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 216f8d29 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r69
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9377/9377 covered=9377/9377 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 18754/18754 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 18754/18754 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 18754/18754).
- PINS-RGRAM cells set-eq 18754/18754 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9377/9377 xor 0;
  PINS 18756 rows (2 hdr + 18754 = PASS lines, +74 vs base
  18682). For-list union 9340->9377 +37 (126705 126706
  126707 126708 126713 126714 126719 126720 126721 126722
  126723 126724 126727 126728 126731 126732 126733 126740
  126749 126756 126765 126772 126781 126788 126795 126796
  126797 126828 126829 126844 126845 126847 126848 126900
  126975 126976 127052),
  0 removed, range 126705..127052 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 37x2 = 74 = 18754-18680.
  The 37 = S0/S1 (2) + A head/mid/edge/tail pairs (8,
  b5-step edge pair 126719/126720 pinned) +
  C head/mid/tail pairs (6) + Q head/7-mids/tail-pair (10,
  NO step this tier, quad b5 const) +
  R head/mid-pairs/edge-pairs/mid/tail (11: head 126797,
  pairs 126828/126829 + 126844/126845, edge pairs
  126847/126848 + 126975/126976, mid 126900, tail 127052).
  PINS-new-N == for-added 37/37 (4th set-eq way),
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P316 C-vs-py, script-compared, TABAUDIT-GREEN
  106 PASS 0 FAIL (tabaudit316.py rc=0; first run 107/0 incl
  1 vacuous placeholder chk the seat spotted on re-read,
  placeholder deleted, re-ran 106/0 GREEN):
  S0 168ch sig 57a75201 sig-eq-P315S0 (33/84 payload
  diff vs P315S0 first-hand, NOT byte-equal) / S1 176ch
  sig 02000000 sig-eq-P315S1 (53/88 payload diff vs P315S1,
  NOT byte-equal; 76/88 diff vs own-C10[0] assembled,
  NOT byte-equal; sig SAME-as-own-C10), staged as
  full-payload singletons,
  AM 16/16 16ch distinct, CM 10/10 8ch distinct, M 16/16
  16ch distinct, QR 4/4 20ch distinct, RM 16/16 20ch
  distinct, RQ 16/16 18ch distinct UNPAIRED, no QT
  (quad tails live in R10) + no RT (STANDARD tails) +
  no F (no frag this tier),
  M-tails == RQ-tails 16/16 string-equal INTRA-tier BUT byte
  positions differ (QM8 b80-83 col vs TR9 b76-79 row;
  M 16ch vs RQ 18ch full strings differ; running pattern:
  b414 full-eq, b416 tail-eq, b418 full-eq,
  b420/b422 string-eq-positions-differ, b424
  tail-eq-positions-differ),
  AC 78, CC 82, QC 68, RC 67; C _N decls 78/82/68/67
  match actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-STEP-M8 sig 28000000 (b0 const 28, b5 STEP
  dd->de @off13 via lencode; AM 16/16 distinct NO pair; M8
  b6,7,8,9,80-83) + vs P315PBA 31000000 (novelty =
  new sig 28 + AM 0-overlap).
  C10-1SIG-88-TAIL sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 8ch:
  f7f1c696/456806a7/656806a7/856806a7/a56806a7/
  c56806a7/046906a7/246906a7/446906a7/646906a7;
  CC b80-83 const 73fd0265; CC has no b5, b5 const
  de full block via lencode).
  QUAD88-4R single-sig 2a000000 x64 (QC b0-3;
  b5 const de full 64, NO step, 0 ff; b4 base 0x1b
  step2 64/64 range 1b..99 NO edge; QM8 b13,14,15,16,80-83
  16/16 distinct NO frags + R10 b6,7,52-55,84-87 rows r0
  99f80c5d13 distinct vs r123 share-10ch 9f4c6adc58,
  tails b84-87 4/4 distinct 846906a7/d3672f03/
  f8672f03/1d682f03, r1r2 TRUE-3B 672f03, r3 2B
  2f03 (suffix of 672f03), r0-lcs0 vs all,
  r1r2-lcs3, r1r3/r2r3-lcs2).
  Ring 3SIG-STANDARD: rows 0-1 f1020000 (x32) + row 2
  bb020000 (x16) + rows 3-15 c9020000 (x208);
  TM10 b12,13,14,15,18,19,80-83 by COL RM 16/16 +
  TR9 b0,9,10,11,16,76-79 by ROW RQ 16/16 UNPAIRED
  (tails SPLIT b80-83 col / b76-79 row); b0 row-led
  (f1/f1/bb/c9x13 first-hand); b1 const 02; b84-87
  cae7888d ring-wide NEW (P315 b1020000/fb2f2a18
  single-sig era).
  VPOS partitions re-derived from code: PBA 10
  (b4,b5+M8, b5-STEP in tab) / C10 5 ({4,84-87},
  b5const excluded) / quad 19 (b4+QM8+R10,
  b5const excluded) / T 21 (b0,b4,b5+TM10+TR9,
  b0 in tab) -- all match A-819.
  Code-consts vs A-819 (PBA 78 / C10 83 /
  quad 69 / T88 67): impl 78/82/68/67 =
  memo-exact on PBA (b5 STEP-varies, in tab) and T88
  (b5 varies, no deduction), writer-1 on C10/quad:
  impl tables still deduct const-b5 (b5 covered by
  lencode instead) while Q-908 sheet counts b5 (memo
  A-819 confirms the sheet) -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  geometry exact, PORT verdict stands; FLAGGED for
  memo (7th band running: b412/b414/b416/b418/b420/
  b422/b424; PBA exact this tier, C10/quad lag).
  QUAD single-sig 2a vs P315; PBA sig
  28 NEW vs P315 31; AC-QC both=66 sameval=24
  (tables differ).
  M-tails 16/16 ALL NEW vs P315 (zero overlap vs
  P315M AND vs P315RM-tail8 AND vs P315RQ-tail8 --
  P315 widths M14/RM14/RQ14).
  AM/CM/M/QR/RM/RQ 0-overlap vs P315 (prev lens
  16/10/16/4/16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=126705 (PB0 sig 57a75201 sig-eq-P315PB0,
  33/84 diff, lenB 84),
  S1 n=126706 (fat PB1 sig 02000000 sig-eq-P315PB1,
  53/88 diff vs P315S1 n126358, 76/88 diff vs C10[0]
  n126723, lenB 88),
  A 126707-722 PBA88-STEP-M8 (sig 28000000 via AC
  b0-b3, b0 const 28, AM 16/16 distinct 16ch, mtab
  b6,7,8,9,80-83, raw lencode b5 STEP dd->de @off13),
  C 126723-732 C10-1SIG-88-TAIL (02000000 x10
  SAME-as-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87, b5 const de
  raw lencode),
  Q 126733-796 QUAD88-4R (QM8 b13-16,80-83 M
  16/16 16ch + R10 b6,7,52-55,84-87 rows above
  (r0 distinct, r123 share 10ch) + tails above,
  NO frags, raw lencode b5 const de b4 1b..99),
  R 126797-127052 T88-RING-3SIG (rows f1020000/
  bb020000/c9020000, TM10 b12-15,18,19,80-83
  by COL RM 16/16, TR9 b0,9-11,16,76-79 by ROW
  RQ 16/16 UNPAIRED, b0 row-led, b1 const 02,
  b84-87 const cae7888d ring-wide,
  b4=(0x9b+2off)&FF, b5=0xde+(off>=51)+(off>=179)).
  C blocks carry T84940/84945/84950/84965/84980/
  85001 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 16ch,
  C 8ch, Q 16/20ch, R 20/18ch),
  R counter b4=(0x9b+2off)&FF + (off>=51)+(off>=179)
  (C literals 155/222 verified == 0x9b/0xde),
  temps _t6491-6506 (base max _t6490, no reuse) +
  _i3936/3938/3941/3944 (base max _i3934,
  no reuse) + _b3935/3937/3939/3940/3942/3943
  (base max _b3933, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P315R close
  (C 226360-62, block 226363; py CLOSED 84938, guard
  84940), at dispatch tail (N-out-of-scope fallthrough
  follows: C 226553, py 85022).
  Matches A-819 geometry (PB0 sig-eq-P315PB0 33/84
  NOT-byte-equal; PB1 sig-eq-P315PB1 53/88 NOT-byte-equal
  SAME-as-C10 76/88; PBA88-STEP-M8 VPOS 10 sig-28 b5
  STEP dd->de @off13 16/16 distinct, M8;
  C10-TAIL VPOS 5 SAME-as-PB1-sig b5 const M4
  10/10 diverge; QUAD88-4R VPOS 19 + R10 4/4
  UNPAIRED + share-10ch + r1r2-TRUE-3B + r3-2B +
  r0-lcs0 + r1r2-lcs3 + QM8 + NO frags + b5-const +
  M-tails NEW; T88-RING-3SIG VPOS 21 + TM10/TR9 +
  row-led-b0 + tails-split + b84-87 cae7888d + counter
  9b/de/51/179; lencode 348/348 whole-tier, PBA step edge
  126719->126720, ring edges 126847->126848 +
  126975->126976, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R10 rows + tails + LCS,
  3SIG rows + consts stand; sheet-vs-tables const-count
  note is S-F arithmetic in tables only per memo,
  geometry unaffected; M-tails==RQ-tails string-equality
  unmentioned by memo, batteries confirm, tier stands).
- Edges via counter formula first-hand: A head e7/dd
  edge 126719 (off12, ff/dd) -> 126720 (off13, 01/de)
  tail 05/de, exactly 1 ff in 16;
  C head 07/de tail 19/de b5set {de} NO step, 0 ff;
  Q head 1b/de tail 99/de b5set {de} NO step, 0 ff
  (b4 base 0x1b step2 64/64 range 1b..99);
  ring 126847 (off50, ff/de) -> 126848 (off51, 01/df);
  126975 (off178, ff/df) -> 126976 (off179, 01/e0);
  exactly 2 ff in 256; R head 9b/de tail
  99/e0 (Q tail 99/de vs R tail 99/e0 differ in b5 --
  labeled apart); formulas re-derived from T10P316R
  code text (9b/de/51/179) + T10P316A text
  (STEP dd->de @off13) + T10P316Q text
  (b5 const de, b4 1b..99 NO edge); all edge pins + tail
  127052 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (e3/dd, e5/dd) match raw lencode.
  Odd-lencode 348/348. No DISSENT on cut bytes (edges316.py
  EDGES-GREEN 39 PASS 0 FAIL, first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 233/0 (rgram.py) + 1/1 (for-line) +
  74/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 411).
- Wall on band diff added lines (scope 5321f012..
  fe9d3bf0, 916 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 233/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +74/+0.
- Tiers: merge-msg +6/+74, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 654->656 +2 /
  ranges 694->698 +4 = +6, C identical deltas 654->656
  +2 / 694->698 +4 (py=C dispatch-exact; no else-if
  either side, deltas agree every side),
  CLOSED T10P prints 1784->1790 +6 both sides,
  seal 1878->1884 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-819-q908-P316
  verdict CONFIRM 64/64 CLEAN (b1 shape 30/30 + b2
  quad+T 17/17 + b3 counters 17/17; file present,
  counts verified; exact-value corroboration incl
  PB0 sig-eq-P315PB0 33/84 NOT-byte-equal, PB1
  sig-eq-P315PB1 53/88 NOT-byte-equal SAME-as-C10
  76/88, PBA88-STEP-M8 sig-28 M8 b5-STEP,
  C10-TAIL SAME-as-PB1-sig M4, QUAD88-4R +
  R10 rows + share-10ch + r1r2-TRUE-3B + r3-2B +
  r0-lcs0 + r1r2-lcs3 + QM8 + NO frags + b5-const +
  M-tails NEW, T88-RING-3SIG + TM10/TR9 + row-led-b0 +
  tails-split + b84-87 cae7888d + edges + consts;
  plus sheet-vs-tables const-count note: Q-908 sheet
  78/83/69/67 memo-exact, committed tables
  78/82/68/67 still deduct const-b5 on C10/quad --
  S-F arithmetic in tables only, geometry exact,
  PORT verdict stands).
  Agrees with cport commit msg (PYID 9377, RGRAM 18754).
- FWD-check first-hand: A-819 "Next P317" forward note
  verified against P317 lane code (54bca2c5, no checkout):
  PB0 57a75201 @127053 (31/84) + PB1 02000000 @127054
  (52/88) + PBA88 28000000 x16 @127055-70 + C10
  02000000 x10 @127071-80 -- all exact, triple-head-repeat
  confirmed in code comments + table sigs.
- Quiz: no conflicting CLAIM/GATE/FLAG on b424 (adjacent
  odds b423/b425 GATED PASS by odd seat, base-use and
  adjacency acknowledged; b424 mentions in odd GATEs are
  adjacency notes, no verdict on b424).
  Activity polled (no b424 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r69/ (build424.log, build424.sha,
  pyid424.log, rgram424py/c.log, cmp424.py/.c/.pyo/.co,
  for424.nums/for423base.nums, for424.added, pass424.nums/
  pins424.nums, pass424.names/pins424.names, pins424added.nums,
  smoke424.log, units424.log, tables424.log, tabaudit316.py,
  edges316.py, edges424.log, numstat424.txt, addnorm424.txt,
  delnorm424.txt, alladded424.txt, banddiff424.txt,
  pydiff316.txt, cdiff424.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
