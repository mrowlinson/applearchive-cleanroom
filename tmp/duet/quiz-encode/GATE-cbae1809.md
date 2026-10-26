# GATE cbae1809 b458 T10P350 pins 138537..138884 (2088 tiers) PASS-functional

Seat sweep2-r77, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r77/w458 @cbae1809.
Band = b3a6b6d6 (py merge w2b@54496646 partial, +6 tiers, +58 pins)
+ cbae1809 (C port). Base c3383244 (b457 tip, 2082 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build458/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc fa02115ccd89c97d10d0d392c3f3c5faf2620761012fe262eb2e4a00dbdbe519 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r77
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 10423/10423 covered=10423/10423 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 20846/20846 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 20846/20846 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 20846/20846).
- PINS-RGRAM cells set-eq 20846/20846 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 10423/10423 xor 0;
  PINS 20848 rows (2 hdr + 20846 = PASS lines, +58 vs base
  20790). For-list union 10394->10423 +29 (138537 138538
  138539 138540 138546 138547 138553 138554 138555 138556
  138559 138560 138563 138564 138565 138580 138596 138612
  138623 138624 138627 138628 138629 138751 138752 138800
  138879 138880 138884),
  0 removed, range 138537..138884 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 29x2 = 58 = 20846-20788.
  The 29 = S0/S1 (2) + A head/mid/tail pairs (6:
  head pair 138539/138540 off0/1, pair 138546/138547
  off7/8, tail pair 138553/138554 off14/15) +
  C head/mid/tail pairs (6: 138555/138556 off0/1,
  mid pair 138559/138560 off4/5, tail pair
  138563/138564 off8/9) +
  Q head/off15/off31/off47/edge-pair/off62/tail (8: head
  138565 off0, 138580 off15, 138596 off31, 138612 off47,
  EDGE pair 138623/138624 off58/59 (b5 edge),
  138627 off62, tail 138628 off63) +
  R head/edge-pair/mid/edge-pair/tail (7: head 138629
  off0, edge pair 138751/138752 off122/123, mid 138800
  off171, edge pair 138879/138880 off250/251, tail
  138884 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg c3383244..b3a6b6d6; C-port leg touched zero
  PINS rows); all 20846 rows test_rgram_fast.py-tagged;
  added 58 names == for-added closed+open pairs (29x2),
  checks sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P350 C-vs-py, script-compared, TABAUDIT-GREEN
  114 PASS 0 FAIL (tabaudit350.py rc=0, fresh first-hand;
  coverage checks run pre-exit, not dead code):
  S0 168ch sig ae40e407 NEW-sig
  (32/84 payload diff vs P349S0 first-hand, NOT byte-equal) /
  S1 176ch sig 0c000000 NEW-sig (48/88 payload diff vs
  P349S1 first-hand, NOT byte-equal; 46/88 diff vs
  own-C10[0] assembled n138555 first-hand, NOT byte-equal; sig
  DIFFERS-from-own-C10 0c-vs-0d and from own PB0),
  staged as full-payload singletons,
  AM 16/16 16ch distinct, CM 10/10 8ch distinct,
  M 16/16 18ch distinct, QR 4/4 4ch distinct, RM 16/16
  16ch distinct, RQ 16/16 18ch distinct, no QT (quad
  tails = R2 pairs + const b86/87) + no RT (SWAPPED tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; QM9 b51-55,80-83 by COL off&15 vs RQ9 b51-55,
  80-83 by ROW off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated),
  AC 78, CC 82, QC 75, RC 69; C _N decls
  78/82/75/69 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M8b38 sig 94000000 (b0 const 94, b5 const
  3a via raw lencode NOT in AC; AM 16/16 distinct NO pair;
  M8 b38,39,46,47,80-83) + vs P349PBA f4000000 (novelty =
  new sig 94 + AM 0-overlap).
  C10-1SIG-88-TAIL-M4 sig 0d000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 8ch b84-87; CC has no b84-87 (all in CM lane)
  and no b5, b5 const 3a full block via lencode).
  QUAD88-1SIG-QM9/R2-B5EDGE 1-sig 94000000 x64
  SAME-sig-as-PBA (QC b0 const 94; b5 STEP 3a->3b @off59
  via raw lencode NOT in QC (deducted, in VPOS); b4 base
  0x8b step2 64/64 range 8b..ff,01..09; QM9 b51-55,80-83
  M 16/16 18ch distinct NO frags (m = off&15 first-hand)
  + R2 b84,85 rows c7a6/e7a6/07a7/27a7 4/4 UNPAIRED
  BY-ROW const (q = off>>4 first-hand);
  tails = R2 pairs + const b86 ae / b87 d9 quad-wide,
  full-tail suffix-lcs 3/2/2/2/2/3).
  Ring SWAPPED-split: sig 4d090000 x256; code-RM8
  b6,7,9,10,76-79 by COL RM 16/16 + code-RQ9 b51-55,
  80-83 by ROW RQ 16/16 UNPAIRED (SWAPPED tails b80-83 row
  / b76-79 col); b0 const 4d (deducted); b84-87 const
  47a7aed9 ring-wide NEW; b4=(0x0b+2off)&FF +
  (off>=123)+(off>=251) (C literals 11/59/123/251 verified
  == 0x0b/0x3b/123/251)).
  VPOS partitions re-derived from code: PBA 9
  (b4+M8) / C10 5 (b4+M4) / quad 13
  (b4,b5+QM9+R2) / T 19
  (b4,b5+RM8+RQ9, b0-const-deducted)
  -- all match Q-1062/A-937.
  Code-consts vs A-937 INCL (PBA 79 / C10 83 /
  quad 75 / T88 69): impl 78/82/75/69 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  A-937 sheet counts b5 (memo confirms the
  sheet INCL values) -- S-F arithmetic persists
  in committed tables though the sheets are FIXED;
  memo-exact on quad (b5 step-varies, in VPOS, no
  deduction) and T88 (b5 counter-varies, in VPOS,
  no deduction); geometry exact, PORT verdict stands;
  FLAGGED for memo (24th even band running: b412/b414/
  b416/b418/b420/b422/b424/b426/b428/b430/b432/b434/
  b436/b438/b440/b442/b444/b446/b448/b450/b452/b454/
  b456/b458; PBA/C10 lag this tier).
  QUAD 1SIG 94 SAME-sig-as-PBA this tier;
  PBA sig 94 NEW vs P349 f4; AC-QC both=71 sameval=55
  (tables differ).
  M-tails 16/16 ALL NEW vs P349T col-led tails
  (zero overlap vs P349T tails first-hand).
  AM/CM/M/QR/RM/RQ 0-overlap vs P349 (widths P350 vs
  P349: AM 8B vs 7B, CM 4B vs 3B, M 9B vs 9B, QR 2B
  vs 4B, RM 8B vs 8B, RQ 9B vs 9B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=138537 (PB0 sig ae40e407 NEW-sig,
  32/84 diff, lenB 84),
  S1 n=138538 (fat PB1 sig 0c000000 NEW-sig,
  48/88 diff vs P349S1, 46/88 diff vs C10[0]
  n138555, DIFFERS-from-own-C10-and-PB0, lenB 88),
  A 138539-554 PBA88-PLAIN-M8b38 (sig 94000000 via AC
  b0-b3, b0 const 94, AM 16/16 distinct 16ch, mtab
  b38,39,46,47,80-83, raw lencode b4=(0x57+2off)&FF
  b5 const 3a NO step NO edge),
  C 138555-564 C10-1SIG-88-TAIL-M4 (0d000000 x10
  DIFFERS-from-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87, b5 const 3a raw lencode),
  Q 138565-628 QUAD88-1SIG-QM9/R2-B5EDGE (QM9
  b51-55,80-83 M 16/16 18ch NO-frags + R2
  b84,85 rows above (4/4 UNPAIRED, BY-ROW const)
  + tails b86-ae/b87-d9 const, b5=0x3a+(off>=59)
  raw lencode + edge 138623->138624),
  R 138629-884 T88-ring SWAPPED-split (sig 4d090000
  x256, code-RM8 b6,7,9,10,76-79 by COL RM 16/16,
  code-RQ9 b51-55,80-83 by ROW RQ 16/16 UNPAIRED,
  SWAPPED tails, b0 const 4d deducted, b84-87 const
  47a7aed9 ring-wide, b4=(0x0b+2off)&FF +
  (off>=123)+(off>=251) (C literals 11/59/123/251
  verified == 0x0b/0x3b/123/251)).
  C blocks carry T93044/93049/93054/93069/93084/
  93105 py-line cites (each re-read: hits the exact
  py guard line, C comment text matches py), bounds +
  byte positions exact (A 16ch, C 8ch, Q 18/4ch,
  R 16/18ch),
  A/C raw lencode (no counter literals) +
  Q b5-edge emergent + R counter b4=(0x0b+2off)&FF +
  (off>=123)+(off>=251) (C literals 11/59/123/251
  verified),
  temps _t7053-7068 (base max _t7052, no reuse) +
  _i4277/4279/4282/4285 (base max _i4275, no reuse) +
  _b4276/4278/4280/4281/4283/4284 (base max _b4274,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P349R close
  (C 247353 print + return, comment 247356, S0 block; py
  CLOSED + return + S0 guard 93044), at dispatch tail
  (N-out-of-scope fallthrough follows: C 247537,
  py 93125-26; early same-text guards at C 167003 /
  py 57606 are the T4 plateau-A n<=1076 check,
  unrelated scope).
  Matches A-937 geometry (PB0 NEW-sig 32/84;
  PB1 NEW-sig 48/88; PBA88-PLAIN-M8b38 VPOS 9 sig-94
  b5 const M8 16/16 distinct; C10-1SIG-88-TAIL-M4 VPOS 5
  DIFFERS-from-PB1-sig b5 const M4 10/10 diverge;
  QUAD88-1SIG-QM9/R2-B5EDGE VPOS 13 + R2 4/4 UNPAIRED
  c7a6/e7a6/07a7/27a7 + suffix-lcs-3/2/2/2/2/3 +
  b86-ae/b87-d9 + NO frags + b5-step + M-tails NEW;
  T88-SWAPPED-split VPOS 19 + RM8-by-COL/RQ9-by-ROW +
  SWAPPED-tails + b0-const-deducted + b84-87 47a7aed9 +
  counter 0b/3b/123/251; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R2 rows +
  tails + LCS + SWAPPED frame + consts stand;
  sheet-vs-tables const-count note is S-F arithmetic
  in tables only per memo, geometry unaffected; M==RQ
  16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 57/3a
  tail 75/3a b5set {3a} NO step, 0 ff;
  C head 77/3a tail 89/3a b5set {3a} NO step, 0 ff;
  Q head 8b/3a, edge off58 (ff/3a) -> off59 (01/3b),
  tail 09/3b, exactly 1 ff in 64 (b5 = 3a+(off>=59);
  b4 base 0x8b step2 64/64 range 8b..ff,01..09);
  ring off122 (ff/3b) -> off123 (01/3c);
  off250 (ff/3c) -> off251 (01/3d);
  exactly 2 ff in 256; R head 0b/3b tail
  09/3d mid-off171 61/3c (Q tail 09/3b vs R tail 09/3d
  same b4, differ in b5 -- labeled apart); formulas
  re-derived from T10P350R code text (0b/3b/123/251)
  + T10P350A/C/Q text (raw lencode, b5 const/step);
  all edge pins + mid 138800 + tail 138884 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b5 (3a
  both; b4 53/55) match raw lencode. Ring counter==raw-lencode
  256/256 + A/C/Q formula==raw 16/10/64. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges350.py EDGES-GREEN 60 PASS 0 FAIL,
  first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 233/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / only-del is the old for-line (replaced by superset:
  base for-N subset of band, removed 0); fine-norm
  equivalent (for457base.nums subset for458.nums,
  removed 0; C-scope del 0).
- Wall on band diff added lines (scope c3383244..
  cbae1809, 608 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 233/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons 727->729 +2 (138537/138538) /
  ranges 852->856 +4 = +6, C singletons 727->729 +2 /
  ranges 852->856 +4 = +6 (same 6 P350 blocks both
  sides; no elif/else-if added either side: py file-wide
  elif 50 both, C else-if 0 both; deltas agree every side),
  CLOSED T10P prints 1988->1994 +6 both sides, seal
  2082->2088 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-937-q1062-P350
  verdict CONFIRM 49/49 CLEAN (own bed r5-P350
  138537..138912 + r5-P349 cross-refs, BAD=0;
  verifier v501.py P350 49/49 PASS; file present, counts
  verified; tier GATED PORT; novelty gated: M-tails 16/16
  ALL NEW vs P349T col-led tails; exact-value corroboration
  incl PB0 NEW-sig 32/84, PB1 NEW-sig 48/88,
  PBA16 sig-94 VPOS 9, C10 sig-0d DIFFSIG VPOS 5,
  QUAD64 1-sig-94 SAME-as-PBA + R2 rows +
  suffix-lcs-3/2/2/2/2/3 + b86-ae/b87-d9 +
  QM9 + NO frags + b5-step + M-tails NEW, T256-SWAPPED
  + RM8-by-COL/RQ9-by-ROW + SWAPPED-tails + b0-4d +
  const 47a7aed9 + counter/edges; plus sheet-vs-tables
  const-count note: A-937 sheet excl 78/82/75/69
  memo-exact (incl +2 b5-const PBA/C10), committed
  tables 78/82/75/69 still deduct const-b5 on PBA/C10 --
  S-F arithmetic in tables only, geometry exact,
  PORT verdict stands).
  Agrees with cport commit msg (PYID 10423, RGRAM 20846).
- FWD-check first-hand: A-937 "Next P351"
  forward notes verified against P351 lane code
  (4934f9d3, no checkout): PB0 ae40e406 @138885 +
  PB1 0d000000 @138886 + PBA dc000000 x16 (AC b0=dc,
  138887..138902) + C10-region 0d000000 x10 (CC b0=0d,
  138903..138912) -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b458 (adjacent
  odds b457/b459 = sweep turf incl b457 C port c3383244
  + b459 C port 4934f9d3 live, base-use only, no verdict
  on b458). Activity polled (no b458 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above).
- Logs: NVME ws tmp/encode-sweep2/r77/ (build458.log,
  build458.sha, pyid458.log, rgram458py/c.log, cmp sets
  (pass458py/c.names), for-458/457base.nums, for458.added/
  .removed, smoke458.log, units458.log, tables458.log,
  tabaudit350.py, edges350.py, edges458.log, band458.diffstat,
  band458.addedlines, band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
