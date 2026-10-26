# GATE b82fa688 b442 T10P334 pins 132969..133316 (1992 tiers) PASS-functional

Seat sweep2-r73, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r73/w442 @b82fa688.
Band = 88a5b299 (py merge w2b@b33481b7 partial, +6 tiers, +62 pins)
+ b82fa688 (C port). Base 18016e8a (b441 tip, 1986 tiers sealed,
odd-seat turf, used as diff-base only).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build442/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 7347161b / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r73
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9939/9939 covered=9939/9939 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 19878/19878 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 19878/19878 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 19878/19878).
- PINS-RGRAM cells set-eq 19878/19878 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9939/9939 xor 0;
  PINS 19880 rows (2 hdr + 19878 = PASS lines, +62 vs base
  19818). For-list union 9908->9939 +31 (132969 132970
  132971 132972 132978 132979 132985 132986 132987 132988
  132991 132992 132995 132996 132997 133004 133012 133013
  133028 133029 133044 133045 133052 133060 133061 133119
  133120 133184 133247 133248 133316),
  0 removed, range 132969..133316 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 19878-19816.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6:
  head pair 132971/132972 off0/1, pair 132978/132979
  off7/8, tail pair 132985/132986 off14/15) +
  C head/B5EDGE/tail pairs (6: head pair 132987/132988
  off0/1, B5EDGE pair 132991/132992 pinned off4/5, tail
  pair 132995/132996 off8/9) + Q head/off7/
  boundary-pairs/off55/tail (10: head 132997 off0, 133004
  off7, pairs 133012/133013 off15/16 + 133028/133029
  off31/32 + 133044/133045 off47/48, 133052 off55, tail
  133060 off63) +
  R head/edge-pair/mid/edge-pair/tail (7: head 133061
  off0, edge pair 133119/133120 off58/59, mid 133184
  off123, edge pair 133247/133248 off186/187, tail
  133316 off255).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0. PINS numstat 62/0 clean append (all in
  py-merge leg 18016e8a..88a5b299; C-port leg touched zero
  PINS rows); all 19878 rows test_rgram_fast.py-tagged;
  cols1-4 purity +62/-0, cols5-7 unchanged first-hand
  (test_rgram_fast.py/27.0.1/ct-lzraven uniform both).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P334 C-vs-py, script-compared, TABAUDIT-GREEN
  122 PASS 0 FAIL (tabaudit334.py rc=0, first run):
  S0 168ch sig 2e01ac06 NEW (sig-family change vs 6db296xx
  era; differs vs P333 heads 6db29606/0d000000; 31/84
  payload diff vs P333S0 first-hand, NOT byte-equal) /
  S1 176ch sig 0e000000 NEW (differs vs P333 heads;
  47/88 payload diff vs P333S1 n132622 first-hand, NOT
  byte-equal; 44/88 diff vs own-C10[0] assembled n132987,
  NOT byte-equal; sig DIFFERS-from-own-C10 0e-vs-0c;
  differs vs own PB0), staged as full-payload singletons,
  AM 16/16 16ch distinct, CM 10/10 12ch distinct,
  M 16/16 16ch distinct, QR 4/4 4ch distinct, RM 16/16
  16ch distinct, RQ 16/16 16ch distinct, no QT (quad
  tails = R2 b84,85 + consts) + no RT (SWAPPED tails) +
  no F (no frag this tier),
  M==RQ FULL 16/16 string-identical INTRA-tier, byte
  positions DIFFER (SAME lanes QM8/RQ8 b52-55,80-83, M
  indexed by COL off&15 vs RQ by ROW off>>4 first-hand;
  SWAPPED tails b80-83 row / b76-79 col; running
  string-eq pattern continues after the b440 0/16
  lanes-differ tier),
  AC 78, CC 80, QC 76, RC 70; C _N decls
  78/80/76/70 match actual; byte-coverage unions exact
  every block (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M8b38 sig fb000000 (b0 const fb, b5 const
  0e via raw lencode NOT in AC; AM 16/16 distinct NO pair; M8
  b38,39,46,47,80-83) + vs P333PBA de000000 (novelty =
  new sig fb + AM 0-overlap).
  C10-DIFFSIG-M6b45-B5EDGE sig 0c000000 x10
  DIFFERS-from-PB1-sig (sig in CC b0-3 consts; CM 10/10
  diverge 12ch b45,46,84-87, b45 {2e,6e,ee} first-hand;
  CC has no b5, b5 edge 0e->0f @off4/5 in VPOS via
  raw lencode).
  QUAD88-1SIG-4R-NOFRAG-C87 1-sig fb000000 x64
  SAME-sig-as-PBA (QC b0 const fb; b5 const 0f NO edge,
  deducted from QC; b4 base 0x0b step2 64/64 range
  0b..89; QM8 b52-55,80-83 16/16 shared x3 vs row0
  (M indexed by col off&15 first-hand) NO frags +
  R2 b84,85 rows ec47/0c48/4b48/6b48 4/4 NO pairing
  BY-ROW const (QR indexed by row off>>4 first-hand);
  tails b84-87 4/4 distinct ec47d14d/0c48d14d/
  4b48d14d/6b48d14d, r0 TRUE-2B d14d vs all, r123
  TRUE-3B 48d14d (b85=0x48 r1/r2/r3 + const d14d),
  suffix-LCS 2/2/2/3/3/3 recorded first-hand;
  b86,87 const d14d (b87 CONST 4d quad-wide)).
  Ring SWAPPED 1-sig: sig bb0f0000 x256; code-RM8
  b6-9,76-79 by COL RM 16/16 + code-RQ8 b52-55,80-83
  by ROW RQ 16/16 UNPAIRED (SWAPPED tails b80-83 row /
  b76-79 col); b0 const bb; b1 const 0f; b84-87
  62c6d8c8 ring-wide NEW.
  VPOS partitions re-derived from code: PBA 9
  (b4+M8) / C10 8 (b4,b5+M6) / quad 11
  (b4+QM8+R2) / T 18
  (b4,b5+RM8+RQ8)
  -- all match A-884.
  Code-consts vs A-884 INCL (PBA 79 / C10 80 /
  quad 77 / T88 70): impl 78/80/76/70 =
  writer-1 on PBA/quad: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-1046 sheet counts b5 (memo A-884 confirms the
  sheet INCL values) -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  memo-exact on C10 (b5 edge-varies, in VPOS)
  and T88 (b5 counter-varies, no deduction);
  geometry exact, PORT verdict stands; FLAGGED for
  memo (16th even band running: b412/b414/b416/b418/
  b420/b422/b424/b426/b428/b430/b432/b434/b436/b438/
  b440/b442; PBA/quad lag this tier).
  QUAD 1SIG fb SAME-sig-as-PBA this tier (vs
  P332 DIFFERS tier); PBA sig fb NEW vs P333 de;
  AC-QC both=72 sameval=54 (tables differ).
  M-tails 16/16 ALL NEW vs P333 (zero overlap vs
  P333T RM col-led tails).
  AM/CM/M/QR/RM/RQ 0-overlap vs P333 (widths P334 vs
  P333: AM 8B vs 7B, CM 6B vs 2B, M 8B vs 8B, QR 2B
  vs 4B, RM 8B vs 7B, RQ 8B vs 8B).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=132969 (PB0 sig 2e01ac06 NEW, 31/84 diff,
  lenB 84),
  S1 n=132970 (fat PB1 sig 0e000000 NEW,
  47/88 diff vs P333S1 n132622, 44/88 diff vs C10[0]
  n132987, DIFFERS-from-own-C10, lenB 88),
  A 132971-986 PBA88-PLAIN-M8b38 (sig fb000000 via AC
  b0-b3, b0 const fb, AM 16/16 distinct 16ch, mtab
  b38,39,46,47,80-83, raw lencode b5 const 0e),
  C 132987-996 C10-DIFFSIG-M6b45-B5EDGE (0c000000 x10
  DIFFERS-from-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 12ch b45,46,84-87, b45 {2e,6e,ee}, raw
  lencode b5=0e+(off>=5) edge 132991->132992),
  Q 132997-060 QUAD88-1SIG-4R-NOFRAG-C87 (QM8 b52-55,
  80-83 M 16/16 16ch shared-x3-by-col + R2 b84,85
  rows above (4/4 NO pairing, BY-ROW const)
  + tails above, NO frags, raw lencode b5 const 0f
  NO edge),
  R 133061-316 T88-RING-SWAPPED (sig bb0f0000 x256,
  code-RM8 b6-9,76-79 by COL RM 16/16,
  code-RQ8 b52-55,80-83 by ROW RQ 16/16 UNPAIRED,
  SWAPPED tails, b0 const bb, b1 const 0f,
  b84-87 const 62c6d8c8 ring-wide,
  b4=(0x8b+2off)&FF, b5=0x0f+(off>=59)+(off>=187)).
  C blocks carry T89336/89341/89346/89361/89376/
  89395 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 16ch,
  C 12ch, Q 16/4ch, R 16/16ch),
  A/C/Q raw lencode (no counter literals; C B5EDGE
  emerges from raw lencode) +
  R counter b4=(0x8b+2off)&FF + (off>=59)+(off>=187)
  (C literals 139/15 verified == 0x8b/0x0f),
  temps _t6797-6812 (base max _t6796, no reuse) +
  _i4117/4119/4122/4125 (base max _i4115,
  no reuse) + _b4116/4118/4120/4121/4123/4124
  (base max _b4114, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P333R close
  (C 237625-27, comment 237628, block 237629; py CLOSED
  89334, guard 89336), at dispatch tail
  (N-out-of-scope fallthrough follows: C 237809,
  py 89414; early same-text guards at C 160194 /
  py 55210 are the T4-plateau-B n<=1077 check,
  unrelated scope).
  Matches A-884 geometry (PB0 NEW-sig 31/84;
  PB1 NEW-sig 47/88 DIFFERS-from-C10 44/88;
  PBA88-PLAIN-M8b38 VPOS 9 sig-fb b5 const 0e M8
  16/16 distinct; C10-DIFFSIG-M6b45-B5EDGE VPOS 8
  DIFFERS-from-PB1-sig b5 edge 0e->0f @off4/5 b45
  {2e,6e,ee} M6 10/10 diverge;
  QUAD88-1SIG-4R-NOFRAG-C87 VPOS 11 + R2 4/4 UNPAIRED
  ec47/0c48/4b48/6b48 + r0-TRUE-2B + r123-TRUE-3B +
  suffix-LCS-2/2/2/3/3/3 + b87-CONST-4d + QM8-shared-x3 +
  NO frags + b5-const + M-tails NEW; T88-RING-SWAPPED
  VPOS 18 + RM8-by-COL/RQ8-by-ROW + SWAPPED-tails +
  b0-bb + b1-0f + b84-87 62c6d8c8 + counter
  8b/0f/59/187; lencode 348/348 whole-tier, C b5 edge
  132991->132992, ring edges 133119->133120 +
  133247->133248, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R2 rows + tails + LCS,
  SWAPPED frame + consts stand; sheet-vs-tables
  const-count note is S-F arithmetic in tables only
  per memo, geometry unaffected; M==RQ
  string-eq-positions-differ unmentioned by memo,
  batteries confirm, tier stands).
- Edges via counter formula first-hand: A head d7/0e
  tail f5/0e b5set {0e} NO step, 0 ff;
  C head f7/0e edge 132991 (off4, ff/0e) ->
  132992 (off5, 01/0f) tail 09/0f, exactly 1 ff
  in 10 (b5 edge 0e->0f @off5; b4 base 0xf7 step2
  10/10);
  Q head 0b/0f tail 89/0f b5set {0f} NO step, 0 ff
  NO edge (b4 base 0x0b step2 64/64 range 0b..89);
  ring 133119 (off58, ff/0f) -> 133120 (off59, 01/10);
  133247 (off186, ff/10) -> 133248 (off187, 01/11);
  exactly 2 ff in 256; R head 8b/0f tail
  89/11 mid123 81/10 (Q tail 89/0f vs R tail 89/11
  differ in b5 -- labeled apart); formulas re-derived
  from T10P334R code text (8b/0f/59/187) + T10P334A/C/Q
  text (raw lencode, A/Q b5 const 0e/0f, C b5 edge);
  all edge pins + mid 133184 + tail 133316 in for-list +
  2 PASS lines each py+C. S0/S1 embedded b4/b5 (d3/0e,
  d5/0e) match raw lencode. Ring counter==raw-lencode
  256/256. Odd-lencode 348/348. No DISSENT on cut bytes
  (edges334.py EDGES-GREEN 68 PASS 0 FAIL, first run).
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 230/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 345).
- Wall on band diff added lines (scope 18016e8a..
  b82fa688, 901 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 690->692 +2 /
  ranges 766->770 +4 = +6, C identical deltas AND
  identical sets (py-only 0, C-only 0; no C-only offset
  this window; no elif added either side: py file-wide
  elif 50->50 pre-existing elsewhere, C else-if 0->0;
  deltas agree every side), CLOSED T10P prints
  1892->1898 +6 both sides, seal 1986->1992 +6
  (commit msgs; offset +94 vs CLOSED-T10P stable): all
  agree, no slip (absolute seal inherits lane tally;
  delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-884-q1046-P334
  verdict CONFIRM 61/61 CLEAN (own bed r3-P334
  132969..133348 BAD=0 + own r3-P333, verifier v270.py
  61/61 PASS; file present, counts verified; geometry
  GATED PORT, novelty FIRST-R2-quad + SWAPPED T-ring
  gated; exact-value corroboration incl PB0 NEW-sig
  31/84, PB1 NEW-sig 47/88 DIFFERS-from-own-C10 44/88,
  PBA88-PLAIN-M8b38 sig-fb M8, C10-DIFFSIG-M6b45-B5EDGE
  DIFFERS-from-PB1-sig b45-{2e,6e,ee} b5-edge,
  QUAD88-1SIG-4R-NOFRAG-C87 1-sig-fb-SAME-as-PBA + R2
  rows ec47/0c48/4b48/6b48 + r0-TRUE-2B + r123-TRUE-3B
  + b87-CONST-4d + QM8 + NO frags + b5-const +
  M-tails NEW, T88-RING-SWAPPED + RM8-by-COL/RQ8-by-ROW
  + SWAPPED-tails + b0-bb + b1-0f + b84-87 62c6d8c8 +
  counter + edges; plus sheet-vs-tables const-count
  note: Q-1046 sheet 79/80/77/70 memo-exact, committed
  tables 78/80/76/70 still deduct const-b5 on PBA/quad
  -- S-F arithmetic in tables only, geometry exact, PORT
  verdict stands) + A-1046-q1046-P334 verdict CONFIRM
  48/48 CLEAN (own bed r6-P334 132969..133344 +
  r6-P333, BAD=0 + direct-oracle 2/2 byte-match,
  verifier v600f3.py 48/48 PASS; file present, counts
  verified; tier GATED PORT; suffix-lcs 2/2/2/3/3/3 +
  M-tails NEW + SWAPPED-frame + consts excl 78/80/76/70
  script-claimed corroborated).
  Agrees with cport commit msg (PYID 9939, RGRAM 19878).
- FWD-check first-hand: A-884 "Next P335" forward note
  verified against P335 lane code (ff5b855c, no checkout):
  PB0 2e01ac06 SAME-sig-as-P334PB0 30/84 @133317 + PB1
  0d000000 NEW-sig 69/88 vs n132970 @133318 +
  PBA88 d5000000 x16 @133319-334 + C10
  0d000000 x10 SAME-as-PB1-sig @133335-344
  -- all exact.
- Quiz: no conflicting CLAIM/GATE/FLAG on b442 (adjacent
  odds b441/b443 = sweep turf, base-use only, no verdict
  on b442).
  Activity polled (no b442 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r73/ (build442.log,
  build442.sha, pyid442.log, rgram442py/c.log, cmp442.py/
  .c/.pyo/.co, for442.nums/for441base.nums, for442.added,
  pass442.names/pins442.names, pins442N.nums/
  pins441N.nums, pins442added.nums, smoke442.log,
  units442.log, tables442.log, tabaudit334.py, edges334.py,
  edges442.log, numstat442.txt, addnorm442.txt,
  delnorm442.txt, alladded442.txt, fwd335.txt, p335.py,
  banddiff via git, pydiff via git, cdiff via git).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
