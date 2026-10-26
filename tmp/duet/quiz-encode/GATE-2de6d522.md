# GATE 2de6d522 b446 T10P338 pins 134361..134708 (2016 tiers) PASS-functional

Seat sweep2-r74, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r74/w446 @2de6d522.
Band = 35e3c34d (py merge w2b@12c56aae partial, +6 tiers, +62 pins)
+ 2de6d522 (C port). Base aab37716 (b445 tip, 2010 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find -type-f file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build446/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ff7389f6 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r74
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 10063/10063 covered=10063/10063 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 20126/20126 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 20126/20126 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 20126/20126).
- PINS-RGRAM cells set-eq 20126/20126 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 10032/10032 xor 0;
  PINS 20128 rows (2 hdr + 20126 = PASS lines, +62 vs base
  20066). For-list union 10032->10063 +31 (134361 134362
  134363 134364 134370 134371 134377 134378 134379 134380
  134383 134384 134387 134388 134389 134399 134400 134401
  134405 134420 134421 134436 134437 134452 134453 134527
  134528 134592 134655 134656 134708),
  0 removed, range 134361..134708 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 20126-20064.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6:
  head pair 134363/134364 off0/1, pair 134370/134371
  off7/8, tail pair 134377/134378 off14/15) +
  C head/mid/tail pairs (6: head pair 134379/134380
  off0/1, mid pair 134383/134384 off4/5, tail pair
  134387/134388 off8/9; b5 const, sampling not edge) +
  Q head/edge-pair/edge+1/off12/off16/pairs/tail (10:
  head 134389 off0, edge 134399 off10, 134400 off11,
  134401 off12, 134405 off16, pairs 134420/134421
  off31/32 + 134436/134437 off47/48, tail 134452
  off63) +
  R head/edge-pair/mid/edge-pair/tail (7: head 134453
  off0, edge pair 134527/134528 off74/75, mid 134592
  off139, edge pair 134655/134656 off202/203, tail
  134708 off255).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0. PINS numstat 62/0 clean append (all in
  py-merge leg aab37716..35e3c34d; C-port leg touched zero
  PINS rows); all 20126 rows test_rgram_fast.py-tagged;
  cols1-4 purity +62/-0, cols5-7 unchanged first-hand
  (test_rgram_fast.py/27.0.1/ct-lzraven uniform both).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P338 C-vs-py, script-compared, TABAUDIT-GREEN
  92 PASS 0 FAIL (tabaudit338.py rc=0, second file version;
  first version asserted QC-b5 direction wrongly -- b5-edge
  means deducted from const table per b442 precedent,
  fixed first-hand):
  S0 168ch sig aefd4106 SAME-sig-P337 (33/84 payload diff
  vs P337S0 first-hand, NOT byte-equal) / S1 176ch sig
  0c000000 SAME-sig-P337 (60/88 payload diff vs P337S1
  n134014 first-hand, NOT byte-equal; 29/88 diff vs
  own-C10[0] assembled n134379, NOT byte-equal; sig
  SAME-as-own-C10 0c-vs-0c; differs vs own PB0),
  staged as full-payload singletons,
  AM 16/16 12ch distinct, CM 10/10 6ch distinct,
  M 16/16 16ch distinct, QR 4/4 8ch distinct, RM 16/16
  20ch distinct, RQ 16/16 16ch distinct, no QT (quad
  tails = R4 b84-87 full tuples) + no RT (COL-led tails) +
  no F (no frag this tier),
  M==RQ FULL 16/16 string-identical INTRA-tier, lanes
  DIFFER (TM10 b0,11,19,27,34,35,80-83 vs TR8 b28-31,
  76-79; M indexed by COL off&15 vs RQ by ROW off>>4
  first-hand; running string-eq pattern continues after
  the b442/b444 string-eq tiers),
  AC 80, CC 83, QC 74, RC 68; C _N decls
  80/83/74/68 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M6b20 sig cd000000 (b0 const cd, b5 const
  19 via raw lencode NOT in AC; AM 16/16 distinct NO pair; M6
  b20,21,80-83) + vs P337PBA 8d000000 (novelty =
  new sig cd + AM 0-overlap).
  C10-1SIG-88-TAIL-M4 sig 0c000000 x10
  SAME-as-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 6ch b84-86; CC has no b5, b5 const 19 full block
  via lencode; CC has b87 const 95).
  QUAD88-1SIG-4R-NOFRAG-B5EDGE 1-sig cd000000 x64
  SAME-sig-as-PBA (QC b0 const cd; b5 edge 19->1a @off10/11
  in VPOS via raw lencode (edge 134399->134400 r0c10/c11);
  b4 base 0xeb step2 64/64 range eb..ff,01..69; QM8
  b28-31,80-83 16/16 shared x3 vs row0 (M indexed by col
  off&15 first-hand) NO frags + R4 b84-87 rows 76fde595/
  de357ff4/fe357ff4/1e367ff4 4/4 NO pairing BY-ROW const
  (QR indexed by row off>>4 first-hand); tails = full
  tuples 4/4 distinct, r0 trailing-suffix lcs=0 vs all,
  r12 TRUE-3B 357ff4, r13 TRUE-2B + r23 TRUE-2B,
  else-pair suffix-LCS 0/0/0/3/2/2 recorded first-hand;
  b87 NOT-const {95,f4}).
  Ring COLSIG 2-sig: sig 0a0d0000 x112 (col<7) +
  0c0d0000 x144; code-RM10 b0,11,19,27,34,35,80-83 by COL
  RM 16/16 + code-RQ8 b28-31,76-79 by ROW RQ 16/16
  UNPAIRED; b0 COL-led (0a c0-6, 0c c7-15); b1 const 0d;
  b84-87 3e367ff4 ring-wide NEW.
  VPOS partitions re-derived from code: PBA 7
  (b4+M6) / C10 4 (b4+M3) / quad 14
  (b4,b5+QM8+R4) / T 20
  (b4,b5+TM10+TR8)
  -- all match A-896.
  Code-consts vs A-896 INCL (PBA 81 / C10 84 /
  quad 74 / T88 68): impl 80/83/74/68 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-1050 sheet counts b5 (memo A-896 confirms the
  sheet INCL values) -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  memo-exact on quad (b5 edge-varies, in VPOS, no
  deduction) and T88 (b5 counter-varies, no deduction);
  geometry exact, PORT verdict stands; FLAGGED for
  memo (18th even band running: b412/b414/b416/b418/
  b420/b422/b424/b426/b428/b430/b432/b434/b436/b438/
  b440/b442/b444/b446; PBA/C10 lag this tier).
  QUAD 1SIG cd SAME-sig-as-PBA this tier
  (vs P336 DIFFERS tier); PBA sig cd NEW vs P337 8d;
  AC-QC both=72 sameval=50 (tables differ).
  M-tails 16/16 ALL NEW vs P337 (zero overlap vs
  P337T RM col-led tails).
  AM/CM/M/QR/RM/RQ 0-overlap vs P337 (widths P338 vs
  P337: AM 6B vs 7B, CM 3B vs 4B, M 8B vs 8B, QR 4B
  vs 3B, RM 10B vs 6B, RQ 8B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=134361 (PB0 sig aefd4106 SAME-sig-P337, 33/84 diff,
  lenB 84),
  S1 n=134362 (fat PB1 sig 0c000000 SAME-sig-P337,
  60/88 diff vs P337S1 n134014, 29/88 diff vs C10[0]
  n134379, SAME-as-own-C10, lenB 88),
  A 134363-378 PBA88-PLAIN-M6b20 (sig cd000000 via AC
  b0-b3, b0 const cd, AM 16/16 distinct 12ch, mtab
  b20,21,80-83, raw lencode b5 const 19),
  C 134379-388 C10-1SIG-88-TAIL-M4 (0c000000 x10
  SAME-as-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 6ch b84-86, b87 const 95, b5 const 19
  raw lencode),
  Q 134389-452 QUAD88-1SIG-4R-NOFRAG-B5EDGE (QM8
  b28-31,80-83 M 16/16 16ch shared-x3-by-col + R4 b84-87
  rows above (4/4 NO pairing, BY-ROW const)
  + tails above, NO frags, b5=19+(off>=11) emergent
  from raw lencode, edge 134399->134400 r0c10/c11),
  R 134453-708 T88-RING-COLSIG (sigs 0a0d0000 x112 +
  0c0d0000 x144, code-RM10 b0,11,19,27,34,35,80-83 by
  COL RM 16/16, code-RQ8 b28-31,76-79 by ROW RQ 16/16
  UNPAIRED, b0 COL-led 0a-c0-6/0c-c7-15, b1 const 0d,
  b84-87 const 3e367ff4 ring-wide,
  b4=(0x6b+2off)&FF, b5=0x1a+(off>=75)+(off>=203)).
  C blocks carry T90262/90267/90272/90287/90301/
  90321 py-line cites (each re-read: hits the exact
  py guard line, C comment text matches py), bounds +
  byte positions exact (A 12ch, C 6ch, Q 16/8ch,
  R 20/16ch),
  A/C raw lencode (no counter literals; Q b5 edge
  emerges from raw lencode) +
  R counter b4=(0x6b+2off)&FF + (off>=75)+(off>=203)
  (C literals 107/26 verified == 0x6b/0x1a),
  temps _t6861-6876 (base max _t6860, no reuse) +
  _i4157/4159/4162/4165 (base max _i4155,
  no reuse) + _b4156/4158/4160/4161/4163/4164
  (base max _b4154, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P337R close
  (C 240058, return 240059, } 240060, comment 240061,
  S0 block 240062; py CLOSED 90260, return 90261,
  S0 guard 90262), at dispatch tail
  (N-out-of-scope fallthrough follows: C 240241,
  py 90341; early same-text guards at C 161917 /
  py 55822 are the plateau n<=1077 check,
  unrelated scope).
  Matches A-896 geometry (PB0 SAME-sig 33/84;
  PB1 SAME-sig 60/88 SAME-as-C10 29/88;
  PBA88-PLAIN-M6b20 VPOS 7 sig-cd b5 const 19 M6
  16/16 distinct; C10-1SIG-88-TAIL-M4 VPOS 4
  SAME-as-PB1-sig b5 const M3 10/10 diverge b87-95;
  QUAD88-1SIG-4R-NOFRAG-B5EDGE VPOS 14 + R4 4/4
  UNPAIRED 76fde595/de357ff4/fe357ff4/1e367ff4 +
  r0-lcs0 + r12-TRUE-3B + r13/r23-TRUE-2B +
  b87-notconst + QM8-shared-x3 + NO frags + b5-edge +
  M-tails NEW; T88-RING-COLSIG VPOS 20 + TM10-by-COL/
  TR8-by-ROW + b0-COL-led + b1-0d + b84-87 3e367ff4 +
  counter 6b/1a/75/203; lencode
  348/348 whole-tier, NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R4 rows +
  tails + LCS, COLSIG frame + consts stand;
  sheet-vs-tables const-count note is S-F arithmetic
  in tables only per memo, geometry unaffected; M==RQ
  16/16 string-eq-positions-differ unmentioned by memo,
  batteries confirm, tier stands).
- Edges via counter formula first-hand: A head b7/19
  tail d5/19 b5set {19} NO step, 0 ff;
  C head d7/19 tail e9/19 b5set {19} NO step, 0 ff;
  Q head eb/19, edge off10 (ff/19) -> off11 (01/1a),
  tail 69/1a, exactly 1 ff in 64 (b5 = 19+(off>=11);
  b4 base 0xeb step2 64/64 range eb..ff,01..69);
  ring off74 (ff/1a) -> off75 (01/1b);
  off202 (ff/1b) -> off203 (01/1c);
  exactly 2 ff in 256; R head 6b/1a tail
  69/1c mid139 81/1b (Q tail 69/1a vs R tail 69/1c
  differ in b5 -- labeled apart); formulas
  re-derived from T10P338R code text (6b/1a/75/203)
  + T10P338A/C/Q text (raw lencode);
  all edge pins + mid 134592 + tail 134708 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (b3/19,
  b5/19) match raw lencode. Ring counter==raw-lencode
  256/256. Odd-lencode 348/348 (16+10+64+256+2). No DISSENT
  on cut bytes (edges338.py EDGES-GREEN 77 PASS 0 FAIL,
  first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 898 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / only-del
  is the old for-line (replaced by superset: base for-N
  subset of band, removed 0); fine-norm equivalent
  (for445base.nums subset for446.nums, removed 0;
  C-scope del 0).
- Wall on band diff added lines (scope aab37716..
  2de6d522, 903 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 698->700 +2 /
  LE-guards 903 const / ranges 782->786 +4 = +6, C
  identical deltas AND identical sets (py-only 0,
  C-only 0; no C-only offset this window; no elif added
  either side: py file-wide elif 50->50 pre-existing
  elsewhere, C else-if 0->0; deltas agree every side),
  CLOSED T10P prints 1916->1922 +6 both sides, seal
  2010->2016 +6 (commit msgs; offset +94 vs CLOSED-T10P
  stable): all agree, no slip (absolute seal inherits
  lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-896-q1050-P338
  verdict CONFIRM 63/63 CLEAN (own beds r3-P338
  134361..134740 + r3-P337 380 cells, BAD=0; verifier
  v282.py 63/63 PASS; file present, counts verified;
  tier GATED PORT; novelty gated: COLSIG T-ring (b0
  COL-led 0a/0c split, 2-sig 112/144, VPOS 20);
  exact-value corroboration incl PB0 SAME-sig 33/84,
  PB1 SAME-sig 60/88 SAME-as-own-C10 29/88, PBA16
  sig-cd VPOS 7, C10 sig-0c SAME-as-PB1 VPOS 4 b87
  const 95, QUAD64 1-sig-cd SAME-as-PBA + R4 rows +
  r0-lcs0 + r12-TRUE-3B + r13/r23-TRUE-2B + b87-notconst +
  QM8 + NO frags + b5-edge + M-tails NEW, T256-RING-COLSIG
  + TM10-by-COL/TR8-by-ROW + b0-COL-led + b1-0d + const
  3e367ff4 + counter/edges; plus sheet-vs-tables
  const-count note: Q-1050 sheet 81/84/74/68 memo-exact,
  committed tables 80/83/74/68 still deduct const-b5 on
  PBA/C10 -- S-F arithmetic in tables only, geometry
  exact, PORT verdict stands) +
  A-1050-q1050-P338 verdict CONFIRM 48/48 CLEAN
  (own bed r6-P338 134361..134736 376 cells +
  r6-P337 cross-refs, BAD=0; verifier v600f3.py
  48/48 PASS; file present, counts verified; tier
  GATED PORT; suffix-lcs 0/0/0/3/2/2 +
  M-tails NEW + COLSPLIT-frame + consts excl
  80/83/74/68 script-claimed corroborated).
  Agrees with cport commit msg (PYID 10063, RGRAM 20126).
- FWD-check first-hand: A-896 "Next P339" forward note
  verified against P339 lane code (1a1af327, no checkout):
  PB0 ee4a0a06 @134709 + PB1 0d000000 @134710 +
  PBA 86000000 x16 @134711-726 + C10
  0d000000 x10 SAME-as-PB1 @134727-736
  -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b446 (adjacent
  odds b445/b447 = sweep turf incl GATED b445 aab37716
  + b447 30d227cf, base-use only, no verdict on b446).
  Activity polled (no b446 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r74/ (build446.log,
  build446.sha, pyid446.log, rgram446py/c.log, cmp446.py/
  .c/.pyo/.co, for446.nums/for445base.nums, for446.added,
  pass446.names/pins446.names, pins446N.nums/
  pins445N.nums, pins446added.nums, smoke446.log,
  units446.log, tables446.log, tabaudit338.py, edges338.py,
  edges446.log, numstat446.txt, alladded446.txt, fwd339
  (p339.py), guards_py/c_w446/w445base.txt, banddiff via
  git, pydiff via git, cdiff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
