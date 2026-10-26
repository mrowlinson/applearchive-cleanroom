# GATE f278bdf0 b426 T10P318 pins 127401..127748 (1896 tiers) PASS-functional

Seat sweep2-r69, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r69/w426 @f278bdf0.
Band = dbcef7b4 (py merge w2b@76bf89ba partial, +6 tiers, +62 pins)
+ f278bdf0 (C port). Base d1c18b6c (b425 tip, 1890 tiers sealed,
GATE-filed PASS-functional by odd seat).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both);
w426 +__pycache__ battery byproduct after runs, w425base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build426/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 3cdda4dc / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r69
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9439/9439 covered=9439/9439 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 18878/18878 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 18878/18878 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 18878/18878).
- PINS-RGRAM cells set-eq 18878/18878 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9439/9439 xor 0;
  PINS 18880 rows (2 hdr + 18878 = PASS lines, +62 vs base
  18818). For-list union 9408->9439 +31 (127401 127402
  127403 127404 127410 127411 127417 127418 127419 127420
  127423 127424 127427 127428 127429 127436 127444 127445
  127461 127477 127487 127488 127491 127492 127493 127600
  127615 127616 127743 127744 127748),
  0 removed, range 127401..127748 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 18878-18816.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid/tail pairs (6) + Q head/5-mids/edge-pair/
  tail-pair (10: head 127429, mids 127436/127444/127445/
  127461/127477, b5-step edge pair 127487/127488 pinned,
  tail pair 127491/127492) +
  R head/mid/edge-pairs/tail (7: head 127493, mid 127600,
  edge pairs 127615/127616 + 127743/127744, tail 127748).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, tests/test_units.py, no oracle).
- Tables audit P318 C-vs-py, script-compared, TABAUDIT-GREEN
  105 PASS 0 FAIL (tabaudit318.py rc=0; first run 104/0
  GREEN, exact tails-vals chk added from INFO output,
  re-ran 105/0 GREEN):
  S0 168ch sig 36ac6c01 NEW-sig (differs first-hand vs P317
  head sigs 57a75201/02000000) / S1 176ch sig 02000000
  sig-eq-P317S1 (58/88 payload diff vs P317S1, NOT byte-equal;
  49/88 diff vs own-C10[0] assembled, NOT byte-equal; sig
  SAME-as-own-C10; differs vs own PB0), staged as
  full-payload singletons,
  AM 16/16 16ch distinct, CM 10/10 10ch distinct, M 16/16
  14ch distinct, QR 4/4 68ch distinct, RM 16/16 12ch
  distinct, RQ 16/16 14ch distinct UNPAIRED, no QT
  (quad tails live in R34) + no RT (SWAPPED tails) +
  no F (no frag this tier),
  M==RQ 16/16 FULL string-identical INTRA-tier, SAME byte
  positions (QM7/TR7 b52-54,80-83; running pattern:
  b414 full-eq, b416 tail-eq, b418 full-eq,
  b420/b422 string-eq-positions-differ, b424
  tail-eq-positions-differ, b426 full-eq),
  AC 78, CC 81, QC 45, RC 73; C _N decls 78/81/45/73
  match actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN-M8b38 sig 27000000 (b0 const 27, b5 const
  e3 via lencode; AM 16/16 distinct NO pair; M8
  b38,39,46,47,80-83) + vs P317PBA 28000000 (novelty =
  new sig 27 + AM 0-overlap).
  C10-1SIG-88-M5b45 sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 10ch:
  211782e3d6/213782e3d6/215782e3d6/217782e3d6/
  213ec7fcd6/215ec7fcd6/217ec7fcd6/219ec7fcd6/
  6138ae7614/611adb364d; CC has no b5, b5 const
  e3 full block via lencode).
  QUAD88-2SIG-4R row0 27000000 SAME-sig-as-PBA + rows1-3
  15000000 x48 (QC has no b0, b0 in tab; row sigs
  assembled b0(row)+QC b1-3 const; b5 STEP e3->e4 @off59,
  edge 127487 ff/e3 -> 127488 01/e4, exactly 1 ff in 64;
  b4 base 0x8b step2 64/64; QM7 b52,53,54,80-83
  16/16 distinct NO frags + R34 b0,8-15,19,25-35,38,39,
  45-51,84-87 rows 4/4 NO pairing pairwise-disjoint
  (r0 27-led fully distinct, r123 15-led, r2/r3 share
  60ch non-tail prefix, differ in tails),
  tails b84-87 4/4 distinct 3adb364d/392fd794/
  0d5f067f/325f067f, r2r3 TRUE-3B 5f067f,
  r0/r1-lcs0 vs all, r2r3-lcs3).
  Ring SWAPPED: sig 55010000 x256; TM6 b6,7,76-79 by
  COL RM 16/16 + TR7 b52-54,80-83 by ROW RQ 16/16
  UNPAIRED (tails SWAPPED b76-79 col / b80-83 row);
  b0 const 55 b1 const 01; b84-87 535f6858 ring-wide
  NEW (P317 3f010000/bf2724fb single-sig era).
  VPOS partitions re-derived from code: PBA 9
  (b4+M8, b5const excluded) / C10 6 (b4+M5,
  b5const excluded) / quad 43 (b0,b4,b5+QM7+R34,
  b0 in tab) / T 15 (b4,b5+TM6+TR7) -- all match A-824.
  Code-consts vs A-824 (PBA 79 / C10 82 /
  quad 45 / T88 73): impl 78/81/45/73 =
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-910 sheet counts b5 (memo A-824 confirms the
  sheet) -- S-F arithmetic persists in committed
  tables though the sheet is FIXED; memo-exact on
  quad (b5 STEP-varies, in tab) and T88 (b5 varies,
  no deduction); geometry exact, PORT verdict stands;
  FLAGGED for memo (8th band running: b412/b414/b416/
  b418/b420/b422/b424/b426; PBA/C10 lag this tier).
  QUAD 2SIG 27/15 vs P317; PBA sig
  27 NEW vs P317 28; AC-QC both=45 sameval=19
  (tables differ).
  M-tails 16/16 ALL NEW vs P317 (zero overlap vs
  P317M AND vs P317RM-tail8 AND vs P317RQ-tail8 --
  P317 widths M8/RM16/RQ14).
  AM/CM/M/QR/RM/RQ 0-overlap vs P317 (prev lens
  16/10/16/4/16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=127401 (PB0 sig 36ac6c01 NEW-sig, lenB 84),
  S1 n=127402 (fat PB1 sig 02000000 sig-eq-P317PB1,
  58/88 diff vs P317S1 n127054, 49/88 diff vs C10[0]
  n127419, NOT-SAME payload, lenB 88),
  A 127403-418 PBA88-PLAIN-M8b38 (sig 27000000 via AC
  b0-b3, b0 const 27, AM 16/16 distinct 16ch, mtab
  b38,39,46,47,80-83, raw lencode b5 const e3),
  C 127419-428 C10-1SIG-88-M5b45 (02000000 x10
  SAME-as-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 10ch b45,84-87, b5 const e3
  raw lencode),
  Q 127429-492 QUAD88-2SIG-4R (QM7 b52-54,80-83 M
  16/16 14ch + R34 rows above (4/4 NO pairing,
  r0 27-led, r123 15-led, r2r3 share-60ch) + tails
  above, NO frags, counter b4=(0x8b+2off)&FF
  b5=0xe3+(off>=59)),
  R 127493-748 T88-RING-SWAPPED (sig 55010000,
  TM6 b6,7,76-79 by COL RM 16/16, TR7 b52-54,80-83
  by ROW RQ 16/16 UNPAIRED, b0 const 55 b1 const 01,
  b84-87 const 535f6858 ring-wide,
  b4=(0x0b+2off)&FF, b5=0xe4+(off>=123)+(off>=251)).
  C blocks carry T85562/85567/85572/85587/85602/
  85627 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 16ch,
  C 10ch, Q 14/68ch, R 12/14ch),
  Q counter b4=(0x8b+2off)&FF + (off>=59)
  (C literals 139/227 verified == 0x8b/0xe3) +
  R counter b4=(0x0b+2off)&FF + (off>=123)+(off>=251)
  (C literals 11/228 verified == 0x0b/0xe4),
  temps _t6537-6552 (base max _t6536, no reuse) +
  _i3956/3958/3961/3964 (base max _i3954,
  no reuse) + _b3955/3957/3959/3960/3962/3963
  (base max _b3953, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P317R close
  (C 227771-73, block 227774; py CLOSED 85560, guard
  85562), at dispatch tail (N-out-of-scope fallthrough
  follows: C 227981, py 85646).
  Matches A-824 geometry (PB0 NEW-sig 36ac6c01;
  PB1 sig-eq-P317PB1 58/88 NOT-byte-equal SAME-as-C10
  49/88; PBA88-PLAIN-M8b38 VPOS 9 sig-27 b5 const e3
  16/16 distinct, M8; C10-M5b45 VPOS 6 SAME-as-PB1-sig
  b5 const 10/10 diverge; QUAD88-2SIG-4R VPOS 43 +
  R34 4/4 UNPAIRED + share-60ch + r2r3-TRUE-3B +
  r0/r1-lcs0 + r2r3-lcs3 + QM7 + NO frags + b5-step
  off59 + M-tails NEW; T88-RING-SWAPPED VPOS 15 +
  TM6/TR7 + swapped-split + b84-87 535f6858 + counter
  0b/e4/123/251; lencode 348/348 whole-tier, Q step edge
  127487->127488, ring edges 127615->127616 +
  127743->127744, NO D dips) incl exact values
  (PBA/C10/QUAD/T88 sigs, R34 rows + tails + LCS,
  SWAPPED split + consts stand; sheet-vs-tables
  const-count note is S-F arithmetic in tables only per
  memo, geometry unaffected; M==RQ full-equality
  unmentioned by memo, batteries confirm, tier stands).
- Edges via counter formula first-hand: A head 57/e3
  tail 75/e3 b5set {e3} NO step, 0 ff;
  C head 77/e3 tail 89/e3 b5set {e3} NO step, 0 ff;
  Q head 8b/e3 edge 127487 (off58, ff/e3) ->
  127488 (off59, 01/e4) tail 09/e4, exactly 1 ff in 64
  (formula == raw lencode 64/64 cross-checked);
  ring 127615 (off122, ff/e4) -> 127616 (off123, 01/e5);
  127743 (off250, ff/e5) -> 127744 (off251, 01/e6);
  exactly 2 ff in 256; R head 0b/e4 tail
  09/e6 (Q tail 09/e4 vs R tail 09/e6 differ in b5 --
  labeled apart); formulas re-derived from T10P318Q
  code text (8b/e3/59) + T10P318R text
  (0b/e4/123/251) + T10P318A/C text
  (b5 const e3); all edge pins + tail
  127748 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (53/e3, 55/e3) match raw lencode.
  Odd-lencode 348/348. No DISSENT on cut bytes
  (edges318.py EDGES-GREEN 42 PASS 0 FAIL, first run).
- C diff purely additive: numstat 607 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 602 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 398).
- Wall on band diff added lines (scope d1c18b6c..
  f278bdf0, 902 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 607/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 658->660 +2 /
  ranges 702->706 +4 = +6, C identical deltas 658->660
  +2 / 702->706 +4 (py=C dispatch-exact; no else-if
  either side, deltas agree every side),
  CLOSED T10P prints 1796->1802 +6 both sides,
  seal 1890->1896 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-824-q910-P318
  verdict CONFIRM 65/65 CLEAN (Q1 shape + Q2 quad+T +
  Q3 counters, verifier v210.py 65/65 PASS; file present;
  exact-value corroboration incl PB0 NEW-sig 36ac6c01,
  PB1 sig-eq-P317PB1 58/88 NOT-byte-equal SAME-as-C10
  49/88, PBA88-PLAIN-M8b38 sig-27 M8, C10-M5b45
  SAME-as-PB1-sig, QUAD88-2SIG-4R row0-same-as-PBA +
  R34 rows + share-60ch + r2r3-TRUE-3B + r0/r1-lcs0 +
  r2r3-lcs3 + QM7 + NO frags + b5-step + M-tails NEW,
  T88-RING-SWAPPED + TM6/TR7 + swapped-split +
  b84-87 535f6858 + edges + consts; plus sheet-vs-tables
  const-count note: Q-910 sheet 79/82/45/73 memo-exact,
  committed tables 78/81/45/73 still deduct const-b5
  on PBA/C10 -- S-F arithmetic in tables only, geometry
  exact, PORT verdict stands).
  Agrees with cport commit msg (PYID 9439, RGRAM 18878).
- FWD-check first-hand: A-824 "Next P319" forward note
  verified against P319 lane code (38f56a72, no checkout):
  PB0 36ac2c01 NEW @127749 + PB1 02000000 sig-eq-P318PB1
  68/88 vs n127402 @127750 + PBA88 25000000 x16 @127751-66
  (AC b0=0x25) + C10 02000000 x10 @127767-76 (CC b0=0x02)
  -- all exact, new-sig era confirmed (repeat era ended
  at P317 as predicted).
- Quiz: no conflicting CLAIM/GATE/FLAG on b426 (adjacent
  odds b425/b427 GATED PASS by odd seat, base-use and
  adjacency acknowledged; b426 mentions in odd GATEs are
  adjacency notes, no verdict on b426).
  Activity polled (no b426 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r69/ (build426.log,
  build426.sha, pyid426.log, rgram426py/c.log, cmp426.py/
  .c/.pyo/.co, for426.nums/for425base.nums, for426.added,
  for426added.nums, pass426.names/pins426.names, pins426N.nums/
  pins425N.nums, pins426added.nums, smoke426.log, units426.log,
  tables426.log, tabaudit318.py, edges318.py, edges426.log,
  numstat426.txt, addnorm426.txt, delnorm426.txt, alladded426.txt,
  banddiff426.txt, pydiff318.txt, cdiff426.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
