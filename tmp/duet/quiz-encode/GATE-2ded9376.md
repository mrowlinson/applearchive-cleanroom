# GATE 2ded9376 b470 T10P362 pins 142713..143060 (2160 tiers) PASS-functional

Seat sweep2-r80, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r80/wB470 @2ded9376.
Band = d02550f5 (py merge w2b@3df79178 partial, +6 tiers, +58 pins)
+ 2ded9376 (C port). Base 0bf51d2c (b469 tip, 2154 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private buildB470/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. aae d6e27c97ced21673cc73eee061ffdbd7f0358a87e482056c222a867202110785
  (aae d6e27c97 = b288-b354 pinned value + r52-r80
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 10771/10771 covered=10771/10771 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 21542/21542 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 21542/21542 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 21542/21542).
- PINS-RGRAM cells set-eq 21542/21542 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 10771/10771 xor 0;
  PINS 21544 rows (2 hdr + 21542 = PASS lines, +58 vs base
  21486). For-list union 10742->10771 +29 (142713 142714
  142715 142716 142719 142720 142721 142730 142731 142732
  142735 142736 142739 142740 142741 142756 142757 142772
  142773 142788 142789 142804 142805 142847 142848 142920
  142975 142976 143060),
  0 removed, range 142713..143060 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 29x2 = 58 = 21542-21484.
  The 29 = S0/S1 (2) + A head-pair/edge-pair/off6/tail (6:
  head pair 142715/142716 off0/1, edge-pair 142719/142720
  off4/5 (ff->01 + b5 STEP 5a->5b), 142721 off6,
  tail 142730 off15) +
  C head/mid/tail pairs (6: 142731/142732 off0/1,
  mid pair 142735/142736 off4/5, tail pair
  142739/142740 off8/9; b5 const 5b NO step) +
  Q head/off15/off16/pair/pair/tail (8: head
  142741 off0, 142756 off15, 142757 off16,
  pair 142772/142773 off31/32,
  pair 142788/142789 off47/48, tail 142804 off63;
  NO edge -- b5 const 5b this tier) +
  R head/edge-pair/mid-pin/edge-pair/tail (7: head 142805
  off0, edge pair 142847/142848 off42/43,
  mid pin 142920 off115, edge pair 142975/142976
  off170/171, tail 143060 off255; no pre-edge pin
  in for-list -- witness pattern same as b466/b468,
  first-hand).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg 0bf51d2c..d02550f5; C-port leg touched zero
  PINS rows); all 21542 rows test_rgram_fast.py-tagged;
  added 58 names == for-added closed+open pairs (29x2),
  checks sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P362 C-vs-py, script-compared, TABAUDIT-GREEN
  124 PASS 0 FAIL (tabaudit362.py rc=0, fresh first-hand;
  coverage checks run pre-exit, not dead code):
  S0 168ch sig ef9ea60e NEW-sig 1B-off (31/84 payload diff vs
  P361S0 sig ef9ea60c first-hand, NOT byte-equal) /
  S1 176ch sig 1d000000 SIG-REPEAT (52/88 payload diff vs
  P361S1 sig 1d000000 first-hand, NOT byte-equal;
  29/88 diff vs own-C10[0] assembled n142731 first-hand,
  NOT byte-equal; sig SAME-as-own-C10 1d-vs-1d;
  DIFFERS from own PB0 ef-vs-1d),
  staged as full-payload singletons,
  AM 16/16 12ch distinct, CM 10/10 8ch distinct,
  M 16/16 14ch distinct, QR 4/4 6ch distinct, RM 16/16
  18ch distinct, RQ 16/16 14ch distinct, no QT (quad
  tails = R3 + const b87) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; QM7 b28,29,30,80-83 by COL m=off&15 vs TR7 b28,29,
  30,76-79 by ROW r=off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated),
  AC 80, CC 82, QC 76, RC 70; C _N decls
  80/82/76/70 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-STEP-M6b20 sig db010000 (b0 const db, b5 STEP
  0x5a+(off>=5) edge 142719->142720 via raw lencode NOT in
  AC; AM 16/16 distinct NO pair; M6 b20,21,80-83) + vs
  P361PBA sig ff (novelty = new sig db + STEP b5 + AM
  0-overlap).
  C10-1SIG-88-TAIL-M4 sig 1d000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 8ch b84,85,86,87; CC has no b84-87 (all in CM lane);
  b5 const 5b full block via lencode).
  QUAD88-1SIG-QM7/R3-NOEDGE 1-sig db010000 x64
  SAME-sig-as-PBA (QC b0 const db; b5 const 5b
  deducted to raw lencode NO edge; b4 base
  0x2b step2 64/64 range 2b..a9, NO wrap; QM7 b28,29,30,
  80-83 M 16/16 14ch distinct NO frags (m = off&15
  first-hand) + R3 b84,85,86 rows
  319155/519155/719155/834c7c 4/4 UNPAIRED BY-ROW const
  (q = off>>4 first-hand);
  tails = R3 + const b87 43 quad-wide,
  full-tail suffix-lcs 3/3/1/3/1/1 + R3 all-distinct).
  Ring T88-2SIG-TM9/TR7-COLSPLIT 2-sig
  (b0 = 0x17 iff col<6 else 0x18: 96+160;
  b1 const 1c; code-TM9 b0,19,27,34,35,80-83 by COL
  RM 16/16 (b0 COL-lane, RM rows 18ch) + code-TR7 b28,29,
  30,76-79 by ROW RQ 16/16 UNPAIRED (SPLIT tails b80-83
  col / b76-79 row); b84-87 const
  c24c7c43 ring-wide; b4=(0xab+2off)&FF +
  (off>=43)+(off>=171) (C literals 171/91/43/171
  verified == 0xab/0x5b/43/171)).
  VPOS partitions re-derived from code: PBA 6
  (b4 + M6 b20,21,80-83; b5 STEP in lencode) / C10 4
  (b4 + M4 b84-87) / quad 10 (b4 + QM7 7 + R3) / T 16
  (b0,b4,b5 + TM9 9 + TR7 7)
  -- all match A-949.
  Code-consts vs A-949 excl (PBA 80 / C10 82 /
  quad 76 / T88 70): impl 80/82/76/70 =
  exact all four, NO writer lag: committed tables match
  the sheet excl values (INCL +2 on C10/quad b5-const =
  82/84/78/70); geometry exact, PORT verdict stands;
  FLAGGED for memo (31st even band running: b412/b414/
  b416/b418/b420/b422/b424/b426/b428/b430/b432/b434/
  b436/b438/b440/b442/b444/b446/b448/b450/b452/b454/
  b456/b458/b460/b462/b464/b466/b468/b470; no-lag this tier).
  QUAD 1SIG db SAME-sig-as-PBA-sig this tier;
  PBA sig db NEW vs P361 ff; AC-QC both=74 sameval=51
  (tables differ).
  M-tails 16/16 ALL NEW vs P361T col-led tails
  (zero overlap vs P361T tails first-hand).
  AM/CM/M/RM/RQ/QR 0-overlap vs P361 (widths P362 vs
  P361: AM 6B vs 8B, CM 4B vs 5B, M 7B vs 8B, RM 9B vs 7B,
  RQ 7B vs 8B, QR 3B vs 2B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=142713 (PB0 sig ef9ea60e NEW-sig 1B-off,
  31/84 diff, lenB 84),
  S1 n=142714 (fat PB1 sig 1d000000 SIG-REPEAT,
  52/88 diff vs P361S1, 29/88 diff vs C10[0]
  n142731, SAME-sig-as-own-C10, lenB 88),
  A 142715-730 PBA88-STEP-M6b20 (sig db010000 via AC
  b0-b3, b0 const db, AM 16/16 distinct 12ch, mtab
  b20,21,80-83, lencode b4=(0xf7+2off)&FF
  b5 STEP 0x5a+(off>=5) edge 142719->142720),
  C 142731-740 C10-1SIG-88-TAIL-M4 (1d000000 x10
  SAME-as-PB1-sig via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87,
  b5 const 5b raw lencode),
  Q 142741-804 QUAD88-1SIG-QM7/R3-NOEDGE (QM7
  b28,29,30,80-83 M 16/16 14ch NO-frags + R3
  b84,85,86 rows 319155/519155/719155/834c7c (4/4
  UNPAIRED, BY-ROW const) + tails R3+43 above, b5 const
  5b raw lencode NO edge),
  R 142805-060 T88-ring 2SIG-COLSPLIT (sig 261d0000 x256,
  b0 colsplit 17/18 (96+160), b1 const 1c,
  code-TM9 b0,19,27,34,35,80-83 by COL RM 16/16,
  code-TR7 b28,29,30,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b84-87 const
  c24c7c43 ring-wide, b4=(0xab+2off)&FF +
  (off>=43)+(off>=171) (C literals 171/91/43/171
  verified == 0xab/0x5b/43/171)).
  C blocks carry T95824/95829/95834/95849/95864/95884
  py-line cites (each re-read: hits the exact
  py guard line, C comment text matches py), bounds +
  byte positions exact (A 12ch, C 8ch, Q 14/6ch,
  R 18/14ch),
  A STEP lencode + C/Q raw lencode (no counter literals) +
  R counter b4=(0xab+2off)&FF + (off>=43)+(off>=171)
  (C literals 171/91/43/171 verified),
  temps _t7245-7260 (base max _t7244, no reuse) +
  _i4397/4399/4402/4405 (base max _i4395, no reuse) +
  _b4396/4398/4400/4401/4403/4404 (base max _b4394,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P361R close
  (C "T10P3620 singleton" after "CLOSED T10P361R"; py
  return 0 + S0 guard 95824), at dispatch tail
  (N-out-of-scope fallthrough follows; plateau guards
  at C T34753 / py NOTE-w2s7-11 are the T4 plateau,
  unrelated scope).
  Matches A-949 geometry (PB0 NEW-sig 1B-off 31/84;
  PB1 SIG-REPEAT 52/88; PBA88-STEP-M6b20 VPOS 8 sig-db
  b5 STEP M6 16/16 distinct; C10-1SIG-88-TAIL-M4 VPOS 5
  SAME-as-PB1-sig b5 const M4 10/10 diverge;
  QUAD88-1SIG-QM7/R3-NOEDGE VPOS 11 + R3 4/4 UNPAIRED
  319155/519155/719155/834c7c + suffix-lcs-3/3/1/3/1/1 +
  R3-distinct + NO frags + M-tails NEW;
  T88-2SIG-COLSPLIT VPOS 18 + TM9-by-COL/TR7-by-ROW +
  SPLIT-tails + b84-87 c24c7c43 +
  counter ab/5b/43/171; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R3 rows +
  tails + LCS + COLSPLIT frame + consts stand;
  const-count note is tables==excl this tier per memo,
  geometry unaffected; M==RQ
  16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head f7/5a
  tail 15/5b; pre-edge off4 (ff/5a), edge off5 (01/5b);
  exactly 1 ff in 16 (STEP tier);
  C head 17/5b tail 29/5b b5set {5b} NO step, 0 ff;
  Q head 2b/5b tail a9/5b b5set {5b} NO edge, 0 ff
  (b4 base 0x2b step2 64/64 range 2b..a9, NO wrap);
  ring pre-edge off42 (ff/5b), edge off43 (01/5c);
  edge off170 (ff/5c) -> off171 (01/5d);
  exactly 2 ff in 256; R head ab/5b tail
  a9/5d; formulas re-derived from T10P362R code text
  (ab/5b/43/171) + T10P362A/C/Q text (STEP/raw lencode);
  all edge pins + mid pin 142920 + tail 143060 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (f3/5a +
  f5/5a) match raw lencode. Ring counter==raw-lencode
  256/256 + Q 64/64 + A 16/16 + C 10/10. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges362.py EDGES-GREEN 80 PASS 0 FAIL,
  first run -- PBA-STEP edge + Q-range NO-wrap verified
  first-hand, never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / C-file dels 0; for-line replaced by superset
  (base for-N subset of band, removed 0); fine-norm
  equivalent (forB469base.nums subset forB470.nums,
  removed 0; C-scope del 0).
- Wall on band diff added lines (scope 0bf51d2c..
  2ded9376, 899 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons py-ind4 746->748 (+2: 142713/142714) /
  ranges py-ind4 878->882 (+4; C singletons 751->753 +2 /
  ranges 900->904 +4, same 6 P362 blocks both
  sides; no elif/else-if added either side: py file-wide
  elif 50 both, C else-if 0 both; deltas agree every side),
  CLOSED T10P prints 2060->2066 +6 both sides, seal
  2154->2160 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-949-q1074-P362
  verdict CONFIRM 50/50 CLEAN (own bed r5-P362
  142713..143088 + r5-P361 cross-refs, BAD=0 + direct-oracle
  2/2 byte-match; verifier v501.py P362 50/50 PASS; file
  present, counts verified; tier GATED PORT; novelty gated:
  M-tails 16/16 ALL NEW vs P361T col-led tails;
  exact-value corroboration incl PB0 NEW-sig-1B-off 31/84,
  PB1 SIG-REPEAT 52/88, PBA16-STEP sig-db VPOS 8,
  C10 sig-1d SAME-PB1 VPOS 5, QUAD64 1-sig-NOEDGE + R3 rows +
  suffix-lcs-3/3/1/3/1/1 + R3-distinct + QM7 + NO frags +
  M-tails NEW, T256-2SIG-COLSPLIT + TM9-by-COL/TR7-by-ROW +
  SPLIT-tails + const c24c7c43 + counter/edges; plus
  const-count note: A-949 excl 80/82/76/70 memo-exact,
  committed tables match excl exactly -- no writer lag
  this tier, geometry exact, PORT verdict stands).
  Agrees with cport commit msg (PYID 10771, RGRAM 21542).
- FWD-check first-hand: A-949 "Next P363"
  forward notes verified against P363 lane code
  (3c030696, git show, no checkout): PB0 ef0da90e @143061
  (168ch pay84) + PB1 1c000000 @143062 (176ch pay88) +
  PBA sig 96010000 (guard 143063..143078,
  16 cells) + C10-region 1c000000 x10 (guard 143079..143088,
  10 cells) -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b470 (adjacent
  odds b469/b471 = sweep turf incl b469 C port 0bf51d2c +
  b471 py-merge 3c030696 live, base-use only, no verdict
  on b470).
  Activity polled (no b470 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above).
- Logs: NVME ws tmp/encode-sweep2/r80/ (buildB470.sha info,
  pyidB470.log, rgramB470py/c.log, cmp sets (passB470py/c.names,
  passB470pyo/co.txt), for-B470/B469base.nums, forB470.added/.removed,
  smokeB470.log, unitsB470.log, tablesB470.log, tabaudit362.py,
  edges362.py, edgesB470.log, bandB470.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
