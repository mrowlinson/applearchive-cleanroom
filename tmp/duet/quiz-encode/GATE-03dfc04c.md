# GATE 03dfc04c b460 T10P352 pins 139233..139580 (2100 tiers) PASS-functional

Seat sweep2-r78, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r78/w460 @03dfc04c.
Band = f291211c (py merge w2b@fc5f8a7d partial, +6 tiers, +58 pins)
+ 03dfc04c (C port). Base 4934f9d3 (b459 tip, 2094 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build460/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 78397719cbe11cc00aa51ec1bdfc07ec3afa2bb8a6347c0bc1858f8043b20da6 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r78
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 10481/10481 covered=10481/10481 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 20962/20962 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 20962/20962 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 20962/20962).
- PINS-RGRAM cells set-eq 20962/20962 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 10481/10481 xor 0;
  PINS 20964 rows (2 hdr + 20962 = PASS lines, +58 vs base
  20906). For-list union 10452->10481 +29 (139233 139234
  139235 139236 139242 139243 139249 139250 139251 139252
  139255 139256 139259 139260 139261 139262 139263 139264
  139276 139292 139308 139324 139325 139391 139392 139450
  139519 139520 139580),
  0 removed, range 139233..139580 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 29x2 = 58 = 20962-20904.
  The 29 = S0/S1 (2) + A head-pair/pair/tail-pair (6:
  head pair 139235/139236 off0/1, pair 139242/139243
  off7/8, tail pair 139249/139250 off14/15; b5 const 3f
  NO step NO edge) +
  C head/mid/tail pairs (6: 139251/139252 off0/1,
  mid pair 139255/139256 off4/5, tail pair
  139259/139260 off8/9; b5 const 3f NO step) +
  Q head/off1/edge-pair/off15/off31/off47/tail (8: head
  139261 off0, 139262 off1, EDGE pair 139263/139264
  off2/3 (b5 edge 3f->40), 139276 off15, 139292 off31,
  139308 off47, tail 139324 off63) +
  R head/edge-pair/mid/edge-pair/tail (7: head 139325
  off0, edge pair 139391/139392 off66/67, mid 139450
  off125, edge pair 139519/139520 off194/195, tail
  139580 off255).
  PINS-new-N == for-added 29/29 (4th set-eq way),
  PINS removed 0. PINS numstat 58/0 clean append (all in
  py-merge leg 4934f9d3..f291211c; C-port leg touched zero
  PINS rows); all 20962 rows test_rgram_fast.py-tagged;
  added 58 names == for-added closed+open pairs (29x2),
  checks sha/str 29/29, gens/os/backends uniform
  (test_rgram_fast.py/27.0.1/ct-lzraven, added == existing).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir; aa/aea pinned shas on file).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P352 C-vs-py, script-compared, TABAUDIT-GREEN
  114 PASS 0 FAIL (tabaudit352.py rc=0, fresh first-hand;
  coverage checks run pre-exit, not dead code):
  S0 168ch sig ae40e406 SAME-sig-as-P351PB0
  (31/84 payload diff vs P351S0 first-hand, NOT byte-equal) /
  S1 176ch sig 0d000000 SAME-sig-as-P351PB1 (80/88 payload
  diff vs P351S1 first-hand, NOT byte-equal; 29/88 diff vs
  own-C10[0] assembled n139251 first-hand, NOT byte-equal; sig
  SAME-as-own-C10 0d-vs-0d and SAME-as-own-PB1; DIFFERS
  from own PB0 ae-vs-0d),
  staged as full-payload singletons,
  AM 16/16 16ch distinct, CM 10/10 8ch distinct,
  M 16/16 16ch distinct, QR 4/4 2ch distinct, RM 16/16
  18ch distinct, RQ 16/16 16ch distinct, no QT (quad
  tails = R1 singles + const b85-87) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; QM8 b40-43,80-83 by COL off&15 vs TR8 b40-43,
  76-79 by ROW off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated),
  AC 78, CC 82, QC 77, RC 69; C _N decls
  78/82/77/69 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M8b29 sig b2000000 (b0 const b2, b5 const
  3f via raw lencode NOT in AC; AM 16/16
  distinct NO pair; M8 b29,30,34,35,80-83) + vs P351PBA dc000000
  (novelty = new sig b2 + AM 0-overlap).
  C10-1SIG-88-TAIL-M4 sig 0d000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 8ch b84-87; CC has no b84-87 (all in CM lane)
  and no b5, b5 const 3f full block via lencode).
  QUAD88-1SIG-QM8/R1-B5EDGE 1-sig 9d000000 x64
  DIFFERS-from-PBA-sig (QC b0 const 9d; b5 STEP 3f->40
  @off3 via raw lencode NOT in QC (deducted, in VPOS); b4 base
  0xfb step2 64/64 range fb..ff,01..79; QM8 b40-43,80-83
  M 16/16 16ch distinct NO frags (m = off&15 first-hand) + R1
  b84 rows 7b/9b/bb/db 4/4 UNPAIRED BY-ROW const
  (q = off>>4 first-hand);
  tails = R1 singles + const b85-87 2f3fd0, full-tail
  suffix-lcs 3/3/3/3/3/3 + R1 all-distinct).
  Ring STANDARD-split: sig 9d0d0000 x256; code-TM9
  b30,31,39,46,47,80-83 by COL RM 16/16 + code-TR8 b40-43,
  76-79 by ROW RQ 16/16 UNPAIRED (SPLIT tails b80-83 col
  / b76-79 row); b0 const 9d (deducted); b84-87 const
  fb2f3fd0 ring-wide NEW; b4=(0x7b+2off)&FF +
  (off>=67)+(off>=195) (C literals 123/64/67/195 verified
  == 0x7b/0x40/67/195)).
  VPOS partitions re-derived from code: PBA 9
  (b4+M8) / C10 5 (b4+M4) / quad 11
  (b4,b5+QM8+R1) / T 19
  (b4,b5+TM9+TR8, b0-const-deducted)
  -- all match A-939.
  Code-consts vs A-939 INCL (PBA 80 / C10 84 /
  quad 77 / T88 69): impl 78/82/77/69 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  A-939 sheet counts b5 (memo confirms the
  sheet INCL values) -- S-F arithmetic persists
  in committed tables though the sheets are FIXED;
  memo-exact on quad (b5 step-varies, in VPOS, no
  deduction) and T88 (b5 counter-varies, in VPOS,
  no deduction); geometry exact, PORT verdict stands;
  FLAGGED for memo (25th even band running: b412/b414/
  b416/b418/b420/b422/b424/b426/b428/b430/b432/b434/
  b436/b438/b440/b442/b444/b446/b448/b450/b452/b454/
  b456/b458/b460; PBA/C10 lag this tier).
  QUAD 1SIG 9d DIFFERS-from-PBA-sig-b2 this tier;
  PBA sig b2 NEW vs P351 dc; AC-QC both=73 sameval=49
  (tables differ).
  M-tails 16/16 ALL NEW vs P351T row-led tails
  (zero overlap vs P351T tails first-hand).
  AM/CM/M/QR/RM/RQ 0-overlap vs P351 (widths P352 vs
  P351: AM 8B vs 6B, CM 4B vs 4B, M 8B vs 7B, QR 1B
  vs 3B, RM 9B vs 7B, RQ 8B vs 7B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=139233 (PB0 sig ae40e406 SAME-as-P351PB0,
  31/84 diff, lenB 84),
  S1 n=139234 (fat PB1 sig 0d000000 SAME-as-P351PB1,
  80/88 diff vs P351S1, 29/88 diff vs C10[0]
  n139251, SAME-sig-as-own-C10, lenB 88),
  A 139235-250 PBA88-PLAIN-M8b29 (sig b2000000 via AC
  b0-b3, b0 const b2, AM 16/16 distinct 16ch, mtab
  b29,30,34,35,80-83, raw lencode b4=(0xc7+2off)&FF
  b5 const 3f NO step NO edge),
  C 139251-260 C10-1SIG-88-TAIL-M4 (0d000000 x10
  SAME-as-PB1-sig via CC b0-3 + CM tab, CM 10/10
  distinct 8ch b84-87, b5 const 3f raw lencode),
  Q 139261-324 QUAD88-1SIG-QM8/R1-B5EDGE (QM8
  b40-43,80-83 M 16/16 16ch NO-frags + R1
  b84 rows above (4/4 UNPAIRED, BY-ROW const)
  + tails R1+2f3fd0 above, b5=0x3f+(off>=3)
  raw lencode + edge 139263->139264),
  R 139325-580 T88-ring STANDARD-split (sig 9d0d0000
  x256, code-TM9 b30,31,39,46,47,80-83 by COL RM 16/16,
  code-TR8 b40-43,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b0 const 9d deducted, b84-87 const
  fb2f3fd0 ring-wide, b4=(0x7b+2off)&FF +
  (off>=67)+(off>=195) (C literals 123/64/67/195
  verified == 0x7b/0x40/67/195)).
  C blocks carry T93509/93514/93519/93534/93549/93568
  py-line cites (each re-read: hits the exact
  py guard line, C comment text matches py), bounds +
  byte positions exact (A 16ch, C 8ch, Q 16/2ch,
  R 18/16ch),
  A/C/Q raw lencode (no counter literals) +
  R counter b4=(0x7b+2off)&FF + (off>=67)+(off>=195)
  (C literals 123/64/67/195 verified),
  temps _t7085-7100 (base max _t7084, no reuse) +
  _i4297/4299/4302/4305 (base max _i4295, no reuse) +
  _b4296/4298/4300/4301/4303/4304 (base max _b4294,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P351R close
  (C 248571 print + return, comment 248574, S0 block; py
  CLOSED + return + S0 guard 93509), at dispatch tail
  (N-out-of-scope fallthrough follows: C 248753,
  py 93588-89; early same-text guards at C 167867 /
  py 57911 are the T4 plateau-A n<=1076 check,
  unrelated scope).
  Matches A-939 geometry (PB0 SAME-sig 31/84;
  PB1 SAME-sig 80/88; PBA88-PLAIN-M8b29 VPOS 9 sig-b2
  b5 const M8 16/16 distinct; C10-1SIG-88-TAIL-M4 VPOS 5
  SAME-as-PB1-sig b5 const M4 10/10 diverge;
  QUAD88-1SIG-QM8/R1-B5EDGE VPOS 11 + R1 4/4 UNPAIRED
  7b/9b/bb/db + suffix-lcs-3/3/3/3/3/3 + R1-distinct +
  NO frags + b5-step + M-tails NEW; T88-STANDARD-split
  VPOS 19 + TM9-by-COL/TR8-by-ROW + SPLIT-tails +
  b0-const-deducted + b84-87 fb2f3fd0 + counter
  7b/40/67/195; lencode 348/348 whole-tier,
  NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R1 rows +
  tails + LCS + STANDARD frame + consts stand;
  sheet-vs-tables const-count note is S-F arithmetic
  in tables only per memo, geometry unaffected; M==RQ
  16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head c7/3f
  tail e5/3f b5set {3f} NO step, 0 ff;
  C head e7/3f tail f9/3f b5set {3f} NO step, 0 ff;
  Q head fb/3f, edge off2 (ff/3f) -> off3 (01/40),
  tail 79/40, exactly 1 ff in 64 (b5 = 3f+(off>=3);
  b4 base 0xfb step2 64/64 range fb..ff,01..79);
  ring off66 (ff/40) -> off67 (01/41);
  off194 (ff/41) -> off195 (01/42);
  exactly 2 ff in 256; R head 7b/40 tail
  79/42 mid-off125 75/41 (Q tail 79/40 vs R tail 79/42
  same b4, differ in b5 -- labeled apart); formulas
  re-derived from T10P352R code text (7b/40/67/195)
  + T10P352A/C/Q text (raw lencode, b5 const/step);
  all edge pins + mid 139450 + tail 139580 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b5 (3f
  both; b4 c3/c5) match raw lencode. Ring counter==raw-lencode
  256/256 + A/C/Q formula==raw 16/10/64. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges352.py EDGES-GREEN 60 PASS 0 FAIL,
  first run -- Q-range wrap verified first-hand,
  never assumed).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  58/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare; 603+5 = 608 added lines)
  / only-del is the old for-line (replaced by superset:
  base for-N subset of band, removed 0); fine-norm
  equivalent (for459base.nums subset for460.nums,
  removed 0; C-scope del 0).
- Wall on band diff added lines (scope 4934f9d3..
  03dfc04c, 608 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +58/+0.
- Tiers: merge-msg +6/+58, code 6 blocks, dispatch-guards
  singletons 731->733 (+2: 139233/139234) /
  ranges 860->864 (+4 = +6 total; C singletons 731->733 +2 /
  ranges 860->864 +4, same 6 P352 blocks both
  sides; no elif/else-if added either side: py file-wide
  elif 50 both, C else-if 0 both; deltas agree every side),
  CLOSED T10P prints 2000->2006 +6 both sides, seal
  2094->2100 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-939-q1064-P352
  verdict CONFIRM 51/51 CLEAN (own bed r5-P352
  139233..139608 + r5-P351 cross-refs, BAD=0;
  verifier v501.py P352 51/51 PASS; file present, counts
  verified; tier GATED PORT; novelty gated: M-tails 16/16
  ALL NEW vs P351T row-led tails; exact-value corroboration
  incl PB0 SAME-sig 31/84, PB1 SAME-sig 80/88,
  PBA16 sig-b2 VPOS 9, C10 sig-0d SAMESIG VPOS 5,
  QUAD64 1-sig-9d DIFFERS-from-PBA + R1 rows +
  suffix-lcs-3/3/3/3/3/3 + R1-distinct +
  QM8 + NO frags + b5-step + M-tails NEW, T256-STANDARD
  + TM9-by-COL/TR8-by-ROW + SPLIT-tails + b0-9d +
  const fb2f3fd0 + counter/edges; plus sheet-vs-tables
  const-count note: A-939 sheet excl 78/82/77/69
  memo-exact (incl +2 b5-const PBA/C10), committed
  tables 78/82/77/69 still deduct const-b5 on PBA/C10 --
  S-F arithmetic in tables only, geometry exact,
  PORT verdict stands).
  Agrees with cport commit msg (PYID 10481, RGRAM 20962).
- FWD-check first-hand: A-939 "Next P353"
  forward notes verified against P353 lane code
  (f4bcf794/b50202d2, git show, no checkout): PB0 ede93f07 @139581 +
  PB1 0d000000 @139582 + PBA 9d000000 x16 (AC b0=9d,
  139583..139598) + C10-region 0d000000 x10 (CC b0=0d,
  139599..139608) -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b460 (adjacent
  odds b459/b461 = sweep turf incl b461 C port 238ba34c
  live, base-use only, no verdict on b460).
  Activity polled (no b460 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above).
- Logs: NVME ws tmp/encode-sweep2/r78/ (build460.log,
  build460.sha, pyid460.log, rgram460py/c.log, cmp sets
  (pass460py/c.names, pass460pyo/co.txt), for-460/459base.nums,
  for460.added/.removed, smoke460.log, units460.log, tables460.log,
  tabaudit352.py, edges352.py, edges460.log, band460.addedlines,
  band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
