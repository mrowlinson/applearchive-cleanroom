# GATE 0bb7a6a5 b456 T10P348 pins 137841..138188 (2076 tiers) PASS-functional

Seat sweep2-r77, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r77/w456 @0bb7a6a5.
Band = 0c8b1c76 (py merge w2b@9592dd82 partial, +6 tiers, +58 pins)
+ 0bb7a6a5 (C port). Base 2bc8d273 (b455 tip, 2070 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build456/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 114acabd4bb3d9e0798fe31a5c92f8d125ebca9c873e6a8c2ef69422bc1bc776 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r77
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 10365/10365 covered=10365/10365 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 20730/20730 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 20730/20730 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 20730/20730).
- PINS-RGRAM cells set-eq 20730/20730 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 10365/10365 xor 0;
  PINS 20732 rows (2 hdr + 20730 = PASS lines, +58 vs base
  20674). For-list union 10336->10365 +29 (137841 137842
  137843 137844 137850 137855 137856 137858 137859 137860
  137863 137864 137867 137868 137869 137884 137885 137900
  137901 137916 137917 137932 137933 137983 137984 138050
  138111 138112 138188),
  0 removed, range 137841..138188 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 29x2 = 58 = 20730-20672.
  The 29 = S0/S1 (2) + A head-pair/mid/edge-pair/tail (6:
  head pair 137843/137844 off0/1, 137850 off7, edge pair
  137855/137856 off12/13, tail 137858 off15) +
  C head/mid/tail pairs (6: 137859/137860 off0/1,
  mid pair 137863/137864 off4/5, tail pair
  137867/137868 off8/9) +
  Q head/off15/off16/pair/pair/tail (8: head
  137869 off0, 137884 off15, 137885 off16,
  pair 137900/137901 off31/32,
  pair 137916/137917 off47/48, tail 137932 off63;
  NO edge -- b5 const this tier) +
  R head/edge-pair/mid/edge-pair/tail (7: head 137933
  off0, edge pair 137983/137984 off50/51, mid 138050
  off117, edge pair 138111/138112 off178/179, tail
  138188 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg 2bc8d273..0c8b1c76; C-port leg touched zero
  PINS rows); all 20730 rows test_rgram_fast.py-tagged;
  added 58 names == for-added closed+open pairs (29x2),
  checks sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P348 C-vs-py, script-compared, TABAUDIT-GREEN
  112 PASS 0 FAIL (tabaudit348.py rc=0, fresh first-hand;
  coverage checks run pre-exit, not dead code):
  S0 168ch sig ef49ef07 NEW-sig 1B-off vs P347PB0
  (33/84 payload diff vs P347S0 first-hand, NOT byte-equal) /
  S1 176ch sig 0d000000 SAME-sig-as-P347PB1 (44/88 payload
  diff vs P347S1 first-hand, NOT byte-equal; 60/88 diff vs
  own-C10[0] assembled n137859 first-hand, NOT byte-equal; sig
  DIFFERS-from-own-C10 0d-vs-0f; differs vs own PB0),
  staged as full-payload singletons,
  AM 16/16 14ch distinct, CM 10/10 8ch distinct,
  M 16/16 12ch distinct, QR 4/4 8ch distinct, RM 16/16
  14ch distinct, RQ 16/16 12ch distinct, no QT (quad
  tails = R4 full tuples) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; QM6 b13,14,80-83 by COL off&15 vs TR6 b10,11,
  76-79 by ROW off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated),
  AC 79, CC 82, QC 76, RC 73; C _N decls
  79/82/76/73 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b6 sig d4000000 (b0 const d4, b5 STEP
  34->35 @off13 via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M7 b6,7,8,80-83) + vs P347PBA e8000000
  (novelty = new sig d4 + AM 0-overlap).
  C10-1SIG-88-TAIL-M4 sig 0f000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 8ch b84-87; CC has no b84-87 (all in CM lane)
  and no b5, b5 const 35 full block via lencode).
  QUAD88-1SIG-QM6/R4-NOEDGE 1-sig fd000000 x64
  DIFFERS-from-PBA-sig (QC b0 const fd; b5 const 35
  deducted to raw lencode NO edge; b4 base 0x1b step2
  64/64 range 1b..99; QM6 b13,14,80-83 M 16/16 12ch
  distinct NO frags (m = off&15 first-hand) + R4
  b84-87 rows 742b3d63/102c3d63/b4b15a77/d4b15a77
  4/4 UNPAIRED BY-ROW const (q = off>>4 first-hand);
  tails = full tuples 4/4 distinct, suffix-lcs
  2/0/0/0/0/3 + b87 NOT-const {63,77}).
  Ring STANDARD-split: sig 800f0000 x256; code-TM7
  b12,18,19,80-83 by COL RM 16/16 + code-TR6 b10,11,
  76-79 by ROW RQ 16/16 UNPAIRED (SPLIT tails b80-83 col
  / b76-79 row); b0 const 80 (deducted); b84-87 const
  13b25a77 ring-wide NEW; b4=(0x9b+2off)&FF +
  (off>=51)+(off>=179) (C literals 155/53/51/179 verified
  == 0x9b/0x35/51/179)).
  VPOS partitions re-derived from code: PBA 9
  (b4,b5+M7) / C10 5 (b4+M4) / quad 11
  (b4+QM6+R4) / T 15
  (b4,b5+TM7+TR6, b0-const-deducted)
  -- all match A-935.
  Code-consts vs A-935 INCL (PBA 79 / C10 83 /
  quad 77 / T88 73): impl 79/82/76/73 =
  writer-1 on C10/quad: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  A-935 sheet counts b5 (memo confirms the
  sheet INCL values) -- S-F arithmetic persists
  in committed tables though the sheets are FIXED;
  memo-exact on PBA (b5 step-varies, in VPOS, no
  deduction) and T88 (b5 counter-varies, in VPOS,
  no deduction); geometry exact, PORT verdict stands;
  FLAGGED for memo (23rd even band running: b412/b414/
  b416/b418/b420/b422/b424/b426/b428/b430/b432/b434/
  b436/b438/b440/b442/b444/b446/b448/b450/b452/b454/
  b456; C10/quad lag this tier).
  QUAD 1SIG fd DIFFERS-from-PBA-sig d4 this tier;
  PBA sig d4 NEW vs P347 e8; AC-QC both=73 sameval=8
  (tables differ).
  M-tails 16/16 ALL NEW vs P347T RM col-led tails
  (zero overlap vs P347T tails first-hand).
  AM/CM/M/QR/RM/RQ 0-overlap vs P347 (widths P348 vs
  P347: AM 7B vs 8B, CM 4B vs 4B, M 6B vs 9B, QR 4B
  vs 4B, RM 7B vs 7B, RQ 6B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=137841 (PB0 sig ef49ef07 NEW-sig 1B-off,
  33/84 diff, lenB 84),
  S1 n=137842 (fat PB1 sig 0d000000 SAME-sig-as-P347PB1,
  44/88 diff vs P347S1, 60/88 diff vs C10[0]
  n137859, DIFFERS-from-own-C10, lenB 88),
  A 137843-858 PBA88-PLAIN-M7b6 (sig d4000000 via AC
  b0-b3, b0 const d4, AM 16/16 distinct 14ch, mtab
  b6,7,8,80-83, raw lencode b4=(0xe7+2off)&FF
  b5=0x34+(off>=13) + edge 137855->137856),
  C 137859-868 C10-1SIG-88-TAIL-M4 (0f000000 x10
  DIFFERS-from-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87, b5 const 35 raw lencode),
  Q 137869-932 QUAD88-1SIG-QM6/R4-NOEDGE (QM6
  b13,14,80-83 M 16/16 12ch NO-frags + R4
  b84-87 rows above (4/4 UNPAIRED, BY-ROW const)
  + tails above, b5=35 raw lencode NO edge),
  R 137933-188 T88-ring STANDARD-split (sig 800f0000
  x256, code-TM7 b12,18,19,80-83 by COL RM 16/16,
  code-TR6 b10,11,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b0 const 80 deducted, b84-87 const
  13b25a77 ring-wide, b4=(0x9b+2off)&FF +
  (off>=51)+(off>=179) (C literals 155/53/51/179
  verified == 0x9b/0x35/51/179)).
  C blocks carry T92579/92584/92589/92604/92619/
  92639 py-line cites (each re-read: hits the exact
  py guard line, C comment text matches py), bounds +
  byte positions exact (A 14ch, C 8ch, Q 12/8ch,
  R 14/12ch),
  A/C/Q raw lencode (no counter literals) +
  R counter b4=(0x9b+2off)&FF + (off>=51)+(off>=179)
  (C literals 155/53/51/179 verified),
  temps _t7021-7036 (base max _t7020, no reuse) +
  _i4257/4259/4262/4265 (base max _i4255, no reuse) +
  _b4256/4258/4260/4261/4263/4264 (base max _b4254,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P347R close
  (C 246143 print + return, comment 246146, S0 block; py
  CLOSED + return + S0 guard 92579), at dispatch tail
  (N-out-of-scope fallthrough follows: C 246321,
  py 92658-59; early same-text guards at C 166147 /
  py 57301 are the T4 plateau-A n<=1076 check,
  unrelated scope).
  Matches A-935 geometry (PB0 NEW-sig 33/84;
  PB1 SAME-sig 44/88; PBA88-PLAIN-M7b6 VPOS 9 sig-d4
  b5 step M7 16/16 distinct; C10-1SIG-88-TAIL-M4 VPOS 5
  DIFFERS-from-PB1-sig b5 const M4 10/10 diverge;
  QUAD88-1SIG-QM6/R4-NOEDGE VPOS 11 + R4 4/4 UNPAIRED
  742b3d63/102c3d63/b4b15a77/d4b15a77 +
  suffix-lcs-2/0/0/0/0/3 + b87-notconst + NO frags +
  b5-const + M-tails NEW; T88-STANDARD-split VPOS 15 +
  TM7-by-COL/TR6-by-ROW + SPLIT-tails + b0-const-deducted +
  b84-87 13b25a77 + counter 9b/35/51/179;
  lencode 348/348 whole-tier, NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R4 rows +
  tails + LCS + STANDARD frame + consts stand;
  sheet-vs-tables const-count note is S-F arithmetic
  in tables only per memo, geometry unaffected; M==RQ
  16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head e7/34
  tail 05/35 (b5 steps 34x13+35x3, edge off12->13
  ff/34->01/35), exactly 1 ff in 16;
  C head 07/35 tail 19/35 b5set {35} NO step, 0 ff;
  Q head 1b/35 tail 99/35 b5set {35} NO edge, 0 ff
  (b4 base 0x1b step2 64/64 range 1b..99, NO wrap);
  ring off50 (ff/35) -> off51 (01/36);
  off178 (ff/36) -> off179 (01/37);
  exactly 2 ff in 256; R head 9b/35 tail
  99/37 mid-off117 85/36 (Q tail 99/35 vs R tail 99/37
  same b4, differ in b5 -- labeled apart); formulas
  re-derived from T10P348R code text (9b/35/51/179)
  + T10P348A/C/Q text (raw lencode, b5 step/const);
  all edge pins + mid 138050 + tail 138188 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b5 (34
  both; b4 e3/e5) match raw lencode. Ring counter==raw-lencode
  256/256 + A/C/Q formula==raw 16/10/64. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges348.py EDGES-GREEN 61 PASS 0 FAIL,
  first run -- Q-range NO-wrap verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 233/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / only-del is the old for-line (replaced by superset:
  base for-N subset of band, removed 0); fine-norm
  equivalent (for455base.nums subset for456.nums,
  removed 0; C-scope del 0).
- Wall on band diff added lines (scope 2bc8d273..
  0bb7a6a5, 608 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 233/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons 723->725 +2 (137841/137842) /
  ranges 844->848 +4 = +6, C singletons 723->725 +2 /
  ranges 844->848 +4 = +6 (same 6 P348 blocks both
  sides; no elif/else-if added either side: py file-wide
  elif 50 both, C else-if 0 both; deltas agree every side),
  CLOSED T10P prints 1976->1982 +6 both sides, seal
  2070->2076 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-935-q1060-P348
  verdict CONFIRM 47/47 CLEAN (own bed r5-P348
  137841..138216 + r5-P347 cross-refs, BAD=0;
  direct-oracle 2/2 byte-match; verifier v501.py
  P348 47/47 PASS; file present, counts verified;
  tier GATED PORT; novelty gated: M-tails 16/16 ALL NEW
  vs P347T RM col-led tails; exact-value corroboration
  incl PB0 NEW-sig 33/84, PB1 SAME-sig 44/88,
  PBA16 sig-d4 VPOS 9, C10 sig-0f DIFFSIG VPOS 5,
  QUAD64 1-sig-fd DIFFERS-from-PBA + R4 rows +
  suffix-lcs-2/0/0/0/0/3 + b87-notconst +
  QM6 + NO frags + b5 const/step + M-tails NEW, T256-STANDARD
  + TM7-by-COL/TR6-by-ROW + SPLIT-tails + b0-80 +
  const 13b25a77 + counter/edges; plus sheet-vs-tables
  const-count note: A-935 sheet excl 79/82/76/73
  memo-exact (incl +2 b5-const C10/quad), committed
  tables 79/82/76/73 still deduct const-b5 on C10/quad --
  S-F arithmetic in tables only, geometry exact,
  PORT verdict stands).
  Agrees with cport commit msg (PYID 10365, RGRAM 20730).
- FWD-check first-hand: A-935 "Next P349"
  forward notes verified against P349 lane code
  (c3383244, no checkout): PB0 ef49ef07 @138189 +
  PB1 0f000000 @138190 + PBA f4000000 x16 (AC b0=f4,
  138191..138206) + C10-region 0f000000 x10 (CC b0=0f,
  138207..138216) -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b456 (adjacent
  odds b455/b457 = sweep turf incl b457 C port c3383244
  live, base-use only, no verdict on b456).
  Activity polled (no b456 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above).
- Logs: NVME ws tmp/encode-sweep2/r77/ (build456.log,
  build456.sha, pyid456.log, rgram456py/c.log, cmp sets
  (pass456py/c.names), for-456/455base.nums, for456.added/
  .removed, smoke456.log, units456.log, tables456.log,
  tabaudit348.py, edges348.py, edges456.log, band456.diffstat,
  band456.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
