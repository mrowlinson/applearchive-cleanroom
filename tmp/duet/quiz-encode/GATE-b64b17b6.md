# GATE b64b17b6 b454 T10P346 pins 137145..137492 (2064 tiers) PASS-functional

Seat sweep2-r76, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r76/w454 @b64b17b6.
Band = f6c7385a (py merge w2b@220b7680 partial, +6 tiers, +62 pins)
+ b64b17b6 (C port). Base 3672d433 (b453 tip, 2058 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build454/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc c0570f1fa22395d110c6b28565f46ba64fb4e25763a853654c689ea27a5bbaf0 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r76
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 10307/10307 covered=10307/10307 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 20614/20614 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 20614/20614 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 20614/20614).
- PINS-RGRAM cells set-eq 20614/20614 (xor 0, PASS-N vs
  PINS-N); PINS N set vs for-list 10307/10307 xor 0;
  PINS 20616 rows (2 hdr + 20614 = PASS lines, +62 vs base
  20554). For-list union 10276->10307 +31 (137145 137146
  137147 137148 137154 137155 137161 137162 137163 137164
  137167 137168 137171 137172 137173 137188 137189 137204
  137205 137215 137216 137220 137221 137236 137237 137343
  137344 137408 137471 137472 137492),
  0 removed, range 137145..137492 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 20614-20552.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6:
  head pair 137147/137148 off0/1, pair 137154/137155
  off7/8, tail pair 137161/137162 off14/15) +
  C head/mid/tail pairs (6: 137163/137164 off0/1,
  mid pair 137167/137168 off4/5, tail pair
  137171/137172 off8/9) +
  Q head/off15/off16/pair/edge-pair/pair/tail (10: head
  137173 off0, 137188 off15, 137189 off16,
  pair 137204/137205 off31/32, EDGE pair 137215/137216
  off42/43 (b5 edge r2c10/c11),
  pair 137220/137221 off47/48, tail 137236 off63) +
  R head/edge-pair/mid/edge-pair/tail (7: head 137237
  off0, edge pair 137343/137344 off106/107, mid 137408
  off171, edge pair 137471/137472 off234/235, tail
  137492 off255).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0. PINS numstat 62/0 clean append (all in
  py-merge leg 3672d433..f6c7385a; C-port leg touched zero
  PINS rows); all 20614 rows test_rgram_fast.py-tagged;
  cols1-4 purity +62/-0, cols5-7 uniform first-hand
  (test_rgram_fast.py/27.0.1/ct-lzraven both, added ==
  existing); added-row names == for-added 31/31.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P346 C-vs-py, script-compared, TABAUDIT-GREEN
  111 PASS 0 FAIL (tabaudit346.py rc=0, fresh first-hand;
  coverage checks run pre-exit, not dead code):
  S0 168ch sig adcf0b07 SAME-sig-as-P345PB0
  (32/84 payload diff vs P345S0 first-hand, NOT byte-equal) /
  S1 176ch sig 0e000000 NEW-sig (60/88 payload diff vs
  P345S1 n136798 first-hand, NOT byte-equal; 29/88 diff vs
  own-C10[0] assembled n137163, NOT byte-equal; sig
  SAME-as-own-C10 0e-vs-0e; differs vs own PB0),
  staged as full-payload singletons,
  AM 16/16 14ch distinct, CM 10/10 6ch distinct,
  M 16/16 16ch distinct, QR 4/4 8ch distinct, RM 16/16
  16ch distinct, RQ 16/16 16ch distinct, no QT (quad
  tails = R4 b84-87 full tuples) + no RT (SPLIT tails) +
  no F (no frag this tier),
  M==RQ 16/16 string-identical SAME-ORDER (M list == RQ
  list; QM8 b28-31,80-83 by COL off&15 vs TR8 b28-31,
  76-79 by ROW off>>4 first-hand; string-eq HOLDS this
  tier -- reported, not gated),
  AC 79, CC 83, QC 74, RC 70; C _N decls
  79/83/74/70 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M7b20 sig ed000000 (b0 const ed, b5 const
  2f via raw lencode NOT in AC; AM 16/16 distinct NO pair; M7
  b20,21,22,80-83) + vs P345PBA c5000000 (novelty =
  new sig ed + AM 0-overlap).
  C10-1SIG-88-TAIL-M3 sig 0e000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 6ch b84-86; b87 const 52 in CC; CC has no
  b84-86 (all in CM lane) and no b5, b5 const 2f full
  block via lencode).
  QUAD88-1SIG-QM8/R4-B5EDGE 1-sig ed000000 x64
  SAME-sig-as-PBA (QC b0 const ed; b5 edge 2f->30
  @off42/43 in raw lencode emergent, NOT in QC const table
  (deducted, in VPOS); b4 base 0xab step2 64/64
  range ab..ff,01..29; QM8 b28-31,80-83 16/16 shared
  x3 vs row0 (M indexed by col off&15 first-hand)
  NO frags + R4 b84-87 rows 9437b852/
  b437b852/d437b852/ae291d7d 4/4 UNPAIRED
  BY-ROW const (QR indexed by row off>>4 first-hand);
  tails = full tuples 4/4 distinct, r012 TRUE-3B
  37b852 + r3 trailing-suffix lcs=0 vs all (anchored) +
  b87 NOT-const {52,7d}).
  Ring STANDARD-split: sig c90d0000 x256; code-TM8
  b19,27,34,35,80-83 by COL RM 16/16 + code-TR8 b28-31,
  76-79 by ROW RQ 16/16 UNPAIRED (SPLIT tails b80-83 col
  / b76-79 row); b0 const c9 (deducted); b84-87 const
  ce291d7d ring-wide NEW; b4=(0x2b+2off)&FF +
  (off>=107)+(off>=235) (C literals 43/48/107/235 verified
  == 0x2b/0x30/107/235)).
  VPOS partitions re-derived from code: PBA 8
  (b4+M7) / C10 4 (b4+M3) / quad 14
  (b4,b5+QM8+R4) / T 18
  (b4,b5+TM8+TR8, b0-const-deducted)
  -- all match A-925.
  Code-consts vs A-925/A-1058 INCL (PBA 80 / C10 84 /
  quad 74 / T88 70): impl 79/83/74/70 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  A-925/A-1058 sheets count b5 (memo confirms the
  sheet INCL values) -- S-F arithmetic persists
  in committed tables though the sheets are FIXED;
  memo-exact on quad (b5 edge-varies, in VPOS, no
  deduction) and T88 (b5 counter-varies, in VPOS,
  no deduction); geometry exact, PORT verdict stands;
  FLAGGED for memo (22nd even band running: b412/b414/
  b416/b418/b420/b422/b424/b426/b428/b430/b432/b434/
  b436/b438/b440/b442/b444/b446/b448/b450/b452/b454;
  PBA/C10 lag this tier).
  QUAD 1SIG ed SAME-sig-as-PBA this tier;
  PBA sig ed NEW vs P345 c5; AC-QC both=71 sameval=50
  (tables differ).
  M-tails 16/16 ALL NEW vs P345T RM col-led tails
  (zero overlap vs P345T tails first-hand).
  AM/CM/M/QR/RM/RQ 0-overlap vs P345 (widths P346 vs
  P345: AM 7B vs 6B, CM 3B vs 4B, M 8B vs 9B, QR 4B
  vs 4B, RM 8B vs 6B, RQ 8B vs 9B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=137145 (PB0 sig adcf0b07 SAME-sig-as-P345PB0,
  32/84 diff, lenB 84),
  S1 n=137146 (fat PB1 sig 0e000000 NEW-sig,
  60/88 diff vs P345S1, 29/88 diff vs C10[0]
  n137163, SAME-as-own-C10, lenB 88),
  A 137147-162 PBA88-PLAIN-M7b20 (sig ed000000 via AC
  b0-b3, b0 const ed, AM 16/16 distinct 14ch, mtab
  b20,21,22,80-83, raw lencode b4=(0x77+2off)&FF
  b5 const 2f NO step NO edge),
  C 137163-172 C10-1SIG-88-TAIL-M3 (0e000000 x10
  SAME-as-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 6ch b84-86 + b87 const 52, b5 const 2f
  raw lencode),
  Q 137173-236 QUAD88-1SIG-QM8/R4-B5EDGE (QM8
  b28-31,80-83 M 16/16 16ch shared-x3-by-col + R4
  b84-87 rows above (4/4 UNPAIRED, BY-ROW const)
  + tails above, NO frags, b5=2f+(off>=43) emergent
  from raw lencode, edge 137215->137216 r2c10/c11),
  R 137237-492 T88-ring STANDARD-split (sig c90d0000
  x256, code-TM8 b19,27,34,35,80-83 by COL RM 16/16,
  code-TR8 b28-31,76-79 by ROW RQ 16/16 UNPAIRED,
  SPLIT tails, b0 const c9 deducted, b84-87 const
  ce291d7d ring-wide, b4=(0x2b+2off)&FF +
  (off>=107)+(off>=235) (C literals 43/48/107/235
  verified == 0x2b/0x30/107/235)).
  C blocks carry T92114/92119/92124/92139/92154/
  92174 py-line cites (each re-read: hits the exact
  py guard line, C comment text matches py), bounds +
  byte positions exact (A 14ch, C 6ch, Q 16/8ch,
  R 16/16ch),
  A/C raw lencode (no counter literals) +
  Q b5-edge emergent + R counter b4=(0x2b+2off)&FF +
  (off>=107)+(off>=235) (C literals 43/48/107/235
  verified),
  temps _t6989-7004 (base max _t6988, no reuse) +
  _i4237/4239/4242/4245 (base max _i4235, no reuse) +
  _b4236/4238/4240/4241/4243/4244 (base max _b4234,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P345R close
  (C 244923, comment 244926, S0 block; py CLOSED +
  return + S0 guard 92114), at dispatch tail
  (N-out-of-scope fallthrough follows: C 245105,
  py 92193; early same-text guards at C 165350 /
  py 57040 are the plateau n<=1077 check,
  unrelated scope).
  Matches A-925 geometry (PB0 SAME-sig-as-P345 32/84;
  PB1 NEW-sig 60/88 SAME-as-C10 29/88;
  PBA88-PLAIN-M7b20 VPOS 8 sig-ed b5 const 2f M7
  16/16 distinct; C10-1SIG-88-TAIL-M3 VPOS 4
  SAME-as-PB1-sig b5 const M3 10/10
  diverge + b87-const-52; QUAD88-1SIG-QM8/R4-B5EDGE
  VPOS 14 + R4 4/4 UNPAIRED 9437b852/b437b852/
  d437b852/ae291d7d + r012-TRUE-3B + r3-lcs0 +
  b87-notconst + QM8-shared-x3 + NO frags + b5-edge +
  M-tails NEW; T88-STANDARD-split VPOS 18 +
  TM8-by-COL/TR8-by-ROW + SPLIT-tails + b0-const-deducted +
  b1-0d + b84-87 ce291d7d + counter 2b/30/107/235;
  lencode 348/348 whole-tier, NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R4 rows +
  tails + LCS + STANDARD frame + consts stand;
  sheet-vs-tables const-count note is S-F arithmetic
  in tables only per memo, geometry unaffected; M==RQ
  16/16 string-identical same-order first-hand this tier,
  tier stands).
- Edges via counter formula first-hand: A head 77/2f
  tail 95/2f b5set {2f} NO step, 0 ff;
  C head 97/2f tail a9/2f b5set {2f} NO step, 0 ff;
  Q head ab/2f, edge off42 (ff/2f) -> off43 (01/30),
  tail 29/30, exactly 1 ff in 64 (b5 = 2f+(off>=43);
  b4 base 0xab step2 64/64 range ab..ff,01..29);
  ring off106 (ff/30) -> off107 (01/31);
  off234 (ff/31) -> off235 (01/32);
  exactly 2 ff in 256; R head 2b/30 tail
  29/32 mid-off171 81/31 (Q tail 29/30 vs R tail 29/32
  same b4, differ in b5 -- labeled apart); formulas
  re-derived from T10P346R code text (2b/30/107/235)
  + T10P346A/C/Q text (raw lencode, b5 const/edge);
  all edge pins + mid 137408 + tail 137492 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b5 2f match
  raw lencode. Ring counter==raw-lencode 256/256 +
  A/C/Q formula==raw 16/10/64. Odd-lencode
  348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges346.py EDGES-GREEN 43 PASS 0 FAIL,
  first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 898 content + 5 bare-blank
  `+` lines (verified bare: `^+\s*$` matches, no whitespace;
  898+5 = 903 added lines)
  / only-del is the old for-line (replaced by superset:
  base for-N subset of band, removed 0); fine-norm
  equivalent (for453base.nums subset for454.nums,
  removed 0; C-scope del 0).
- Wall on band diff added lines (scope 3672d433..
  b64b17b6, 903 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 714->716 +2 (137145/137146) /
  ranges 814->818 +4 = +6, C singletons 719->721 +2 /
  ranges 836->840 +4 = +6 (same 6 P346 blocks both
  sides; no elif/else-if added either side: py file-wide
  elif 50 both, C else-if 0 both; deltas agree every side),
  CLOSED T10P prints 1964->1970 +6 both sides, seal
  2058->2064 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-925-q1058-P346
  verdict CONFIRM 51/51 CLEAN (own beds r4-P346
  137145..137520 + r4-P345 cross-refs, BAD=0;
  direct-oracle spot 4/4 byte-match; verifier v306.py
  P346 51/51 PASS; file present, counts verified;
  tier GATED PORT; novelty gated: M-tails 16/16 ALL NEW
  vs P345T RM col-led tails; exact-value corroboration
  incl PB0 SAME-sig 32/84, PB1 NEW-sig 60/88
  SAME-as-own-C10 29/88, PBA16 sig-ed VPOS 8,
  C10 sig-0e SAME-as-PB1 VPOS 4 (CM 10/10 diverge 6ch
  b84-86 + b87-const-52),
  QUAD64 1-sig-ed SAME-as-PBA + R4 rows +
  r012-TRUE-3B + r3-lcs0 + b87-notconst +
  QM8 + NO frags + b5-edge + M-tails NEW, T256-STANDARD
  + TM8-by-COL/TR8-by-ROW + SPLIT-tails + b0-c9 +
  b1-0d + const ce291d7d + counter/edges; plus
  sheet-vs-tables const-count note: A-925 sheet
  80/84/74/70 memo-exact, committed tables 79/83/74/70
  still deduct const-b5 on PBA/C10 -- S-F arithmetic
  in tables only, geometry exact, PORT verdict stands) +
  A-1058-q1058-P346 verdict CONFIRM 46/46 CLEAN
  (own bed r6-P346 137145..137520, 376 cells +
  r6-P345 cross-refs, BAD=0; verifier v600f3.py
  P346 46/46 PASS; file present, counts verified;
  tier GATED PORT; suffix-lcs 3/3/0/3/0/0 +
  M-tails NEW + STD frame + consts
  excl 79/83/74/70 script-claimed corroborated).
  Agrees with cport commit msg (PYID 10307, RGRAM 20614).
- FWD-check first-hand: A-925 + A-1058 "Next P347"
  forward notes verified against P347 lane code
  (b94eec82 lane tip merge of w2b@6ddee87a, no checkout):
  PB0 ef496f07 @137493 + PB1 0d000000 @137494 +
  PBA e8000000 x16 (AC b0) + C10 0d000000 x10 (CC b0)
  SAME-as-PB1 -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b454 (adjacent
  odds b453/b455 = sweep turf incl GATED b453 3672d433
  + b455 py-merge b94eec82 live, base-use only, no verdict
  on b454). Activity polled (no b454 conflict); PROSE-01
  re-read before filing (all hex/counts copied from run
  output above).
- Logs: NVME ws tmp/encode-sweep2/r76/ (build454.log,
  build454.sha, pyid454.log, rgram454py/c.log, cmp454.py/
  .c/.pyo/.co, for454.nums/for453base.nums, for454.added/
  .removed, smoke454.log, units454.log, tables454.log,
  tabaudit346.py, edges346.py, edges454.log, numstat
  (band454.diff), band454.addedlines/cleg454.added,
  fwd347 (via git show 6ddee87a), band diff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
