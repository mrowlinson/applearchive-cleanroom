# GATE 4ad8ae20 b422 T10P314 pins 126009..126356 (1872 tiers) PASS-functional

Seat sweep2-r68, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r68/w422 @4ad8ae20.
Band = 49dcf348 (py merge w2b@881c672c partial, +6 tiers, +64 pins)
+ 4ad8ae20 (C port). Base 75aa70e6 (b421 tip, 1866 tiers sealed,
GATE-filed PASS-functional by odd seat during run).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both);
w422 +__pycache__ battery byproduct after runs, w421base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build422/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc c690cd66 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r68
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9309/9309 covered=9309/9309 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 18618/18618 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 18618/18618 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 18618/18618).
- PINS-RGRAM cells set-eq 18618/18618 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9309/9309 xor 0;
  PINS 18620 rows (2 hdr + 18618 = PASS lines, +64 vs base
  18556). For-list union 9277->9309 +32 (126009 126010
  126011 126012 126018 126019 126025 126026 126027 126028
  126031 126032 126035 126036 126037 126044 126053 126060
  126069 126079 126080 126085 126092 126100 126101 126113
  126114 126207 126208 126335 126336 126356),
  0 removed, range 126009..126356 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 32x2 = 64 = 18618-18554.
  The 32 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid/tail pairs (6) + Q head/8-mids/tail (10,
  b5-step edge pair 126079/126080 pinned) +
  R head/colsplit-pair/edge-pair/edge-pair/tail (8,
  colsplit boundary pair 126113/126114 off12/13 pinned).
  PINS-new-N == for-added 32/32 (4th set-eq way),
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P314 C-vs-py, script-compared, TABAUDIT-GREEN
  101 PASS 0 FAIL (tabaudit314.py rc=0, first run):
  S0 168ch sig 97016d01 sig-eq-P313S0 (32/84 payload
  diff vs P313S0 first-hand, NOT byte-equal) / S1 176ch
  sig 01000000 NEW-sig (59/88 payload diff vs P313S1,
  NOT byte-equal; 29/88 diff vs own-C10[0] assembled,
  NOT byte-equal; sig NOT-SAME-as-own-C10), staged as
  full-payload singletons,
  AM 16/16 12ch distinct, CM 10/10 10ch distinct, M 16/16
  12ch distinct, QR 4/4 22ch distinct, RM 16/16 20ch
  distinct, RQ 16/16 12ch distinct UNPAIRED, no QT
  (quad tails live in R11) + no RT (STANDARD tails) +
  no F (no frag this tier),
  M==RQ string-identical 16/16 INTRA-tier BUT byte
  positions differ (QM6 b28,29,80-83 vs TR6 b28,29,76-79;
  running pattern: b414 full-eq, b416 tail-eq, b418 full-eq,
  b420/b422 string-eq-positions-differ),
  AC 80, CC 81, QC 69, RC 70; C _N decls 80/81/69/70
  match actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN sig 16000000 (b0 const 16, b5 const
  d8 via lencode; AM 16/16 distinct NO pair; M6
  b20,21,80-83) + vs P313PBA 26000000 (novelty =
  new sig 16 + AM 0-overlap).
  C10-1SIG-88-NOTPB1 sig 02000000 x10 NOT-PB1-sig (sig
  in CC b0-3 consts; CM 10/10 diverge 10ch:
  78e029db6a/78002adb6a/78202adb6a/78402adb6a/
  787f2adb6a/789f2adb6a/78bf2adb6a/80c6b23522/
  80e6b23522/8081730b5c; CC has no b5, b5 const
  d8 full block via lencode).
  QUAD88-4R-STEP single-sig 2c000000 x64 (QC b0-3;
  b5 0xd8+(off>=43) step edge off42->43 @126079 ff/d8
  -> 126080 01/d9, exactly 1 ff in 64; b4 base 0xab
  step2 64/64; QM6 b28,29,80-83 16/16 distinct NO
  frags + R11 b20-26,84-87 rows r0 53db210bb393ad
  distinct vs r123 share-14ch 295d712a13bf8a,
  tails b84-87 4/4 distinct 70e9aabd/7e308796/
  33ad7b9b/58ad7b9b, r2r3 TRUE-3B ad7b9b,
  r0-lcs0 AND r1-lcs0 vs all, r2r3-lcs3 --
  second r2r3-pair variant after b418's 2B, here 3B).
  Ring STANDARD-COLSPLIT: TM10 b0,11,19,27,34,35,80-83
  by COL RM 16/16 (b0 col-led 13+3 split: 2b cols 0-12
  / 2c cols 13-15: cols0-12 sig 2b020000 208 cells +
  cols13-15 sig 2c020000 48 cells) + TR6 b28,29,76-79
  by ROW RQ 16/16 UNPAIRED (tails SPLIT b80-83 col /
  b76-79 row); RC carries no b0 (col-led), b1 const
  02, b84-87 f4728f80 ring-wide NEW (P313
  38020000/cbed6982 1-sig STANDARD).
  VPOS partitions re-derived from code: PBA 7
  (M6+b4, b5const excluded) / C10 6 ({4,22,84-87},
  b5const excluded) / quad 19 (b4,b5+QM6+R11,
  b27 excluded verified) / T 18 (b0 in tab +
  TM10+TR6+b4+b5) -- all match A-812.
  Code-consts vs A-812 (PBA 81 / C10 82 /
  quad 69 / T88 70): impl 80/81/69/70 =
  memo-exact on quad/T88 (b5 STEP/varies, no deduction),
  writer-1 on PBA/C10: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-906 sheet counts b5 (memo A-812
  confirms the sheet) -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  geometry exact, PORT verdict stands; FLAGGED for
  memo (6th band running: b412/b414/b416/b418/b420/b422).
  QUAD single-sig 2c vs P313; PBA sig
  16 NEW vs P313 26; AC-QC both=69 sameval=37
  (tables differ).
  M-tails 16/16 ALL NEW vs P313 (zero overlap vs
  P313M AND vs P313RM-tail8 AND vs P313RQ-tail8 --
  P313 widths M12/RM14/RQ12).
  AM/CM/M/QR/RM/RQ 0-overlap vs P313 (prev lens
  16/10/16/4/16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=126009 (PB0 sig 97016d01 sig-eq-P313PB0,
  32/84 diff, lenB 84),
  S1 n=126010 (fat PB1 sig 01000000 NEW-sig,
  59/88 diff vs P313S1 n125662, 29/88 diff vs C10[0]
  n126027, NOT-SAME-as-C10, lenB 88),
  A 126011-026 PBA88-PLAIN (sig 16000000 via AC
  b0-b3, b0 const 16, AM 16/16 distinct 12ch, mtab
  b20,21,80-83, raw lencode b5 const d8),
  C 126027-036 C10-1SIG-88-NOTPB1 (02000000 x10
  NOT-PB1 via CC b0-3 + CM tab, CM 10/10
  distinct 10ch b22,84-87, b5 const d8
  raw lencode),
  Q 126037-100 QUAD88-4R-STEP (QM6 b28,29,80-83 M
  16/16 12ch + R11 b20-26,84-87 rows above
  (r0 distinct, r123 share 14ch) + tails above,
  NO frags, raw lencode b5 step off42->43),
  R 126101-356 T88-RING-STANDARD-COLSPLIT (2-sig
  2b020000/2c020000, TM10 b0,11,19,27,34,35,80-83
  by COL RM 16/16, TR6 b28,29,76-79 by ROW RQ 16/16
  UNPAIRED, b84-87 const f4728f80 ring-wide,
  b4=(0x2b+2off)&FF, b5=0xd9+(off>=107)+(off>=235)).
  C blocks carry T84454/84459/84464/84479/84494/
  84515 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 12ch,
  C 10ch, Q 12/22ch, R 20/12ch),
  R counter b4=(0x2b+2off)&FF + (off>=107)+(off>=235)
  (C literals 43/217 verified == 0x2b/0xd9),
  temps _t6457-6472 (base max _t6456, no reuse) +
  _i3916/3918/3921/3924 (base max _i3914,
  no reuse) + _b3915/3917/3919/3920/3922/3923
  (base max _b3913, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P313R close
  (C 225119-21, block 225122; py CLOSED 84452, guard
  84454), at dispatch tail (N-out-of-scope fallthrough
  follows: C 225307, py 84535).
  Matches A-812 geometry (PB0 sig-eq-P313PB0 32/84
  NOT-byte-equal; PB1 NEW-sig 59/88 NOT-byte-equal
  NOT-SAME-as-C10 29/88; PBA88-PLAIN VPOS 7 sig-16
  b5 const d8 16/16 distinct, M6; C10-NOTPB1 VPOS 6
  b5 const M5 10/10 diverge; QUAD88-4R-STEP VPOS 19 +
  R11 4/4 UNPAIRED + share-14ch + r2r3-TRUE-3B +
  r0+r1-lcs0 + r2r3-lcs3 + QM6 + NO frags + b5-step
  off42->43 + M-tails NEW; T88-RING-STANDARD-COLSPLIT
  VPOS 18 + TM10/TR6 + b0-colsplit-13+3 + tails-split +
  b84-87 f4728f80 + counter 2b/d9/107/235; lencode
  348/348 whole-tier, Q step edge 126079->126080,
  ring edges 126207->126208 + 126335->126336, NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R11 rows +
  tails + LCS, colsplit + consts stand; sheet-vs-tables
  const-count note is S-F arithmetic in tables only per
  memo, geometry unaffected; M==RQ string-equality
  unmentioned by memo, batteries confirm, tier stands).
- Edges via counter formula first-hand: A head 77/d8
  tail 95/d8 b5set {d8} NO step, 0 ff;
  C head 97/d8 tail a9/d8 b5set {d8} NO step, 0 ff;
  Q head ab/d8 tail 29/d9 b5step o42->43 (126079
  ff/d8 -> 126080 01/d9), exactly 1 ff in 64
  (b4 base 0xab step2 64/64);
  ring 126207 (off106, ff/d9) -> 126208 (off107, 01/da);
  126335 (off234, ff/da) -> 126336 (off235, 01/db);
  exactly 2 ff in 256; R head 2b/d9 tail
  29/db (Q tail 29/d9 vs R tail 29/db differ in b5 --
  labeled apart); COLSPLIT boundary off12->13
  (126113/126114) both in for-list (sig 2b->2c cols
  flip, NOT a counter edge -- labeled apart); formulas
  re-derived from T10P314R code text (2b/d9/107/235) +
  T10P314Q text (d8/43/42/43); all edge pins + colsplit
  pair + tail 126356 in for-list + 2 PASS lines each
  py+C. S0/S1 embedded b4/b5 (73/d8, 75/d8) match raw
  lencode. Odd-lencode 348/348. No DISSENT on cut bytes.
- C diff purely additive: numstat 608 add / 0 del
  (rgramc.c) + 233/0 (rgram.py) + 1/1 (for-line) +
  64/0 (PINS); raw C grep 603 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 374).
- Wall on band diff added lines (scope 75aa70e6..
  4ad8ae20, 906 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 608/0, rgram.py 233/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 650->652 +2 /
  ranges 686->690 +4 = +6, C identical deltas 650->652
  +2 / 686->690 +4 (py=C dispatch-exact; deltas
  agree every side),
  CLOSED T10P prints 1772->1778 +6 both sides,
  seal 1866->1872 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-812-q906-P314
  verdict CONFIRM 62/62 CLEAN (b1 shape 30/30 + b2
  quad+T 18/18 + b3 counters 14/14; file present,
  counts verified; exact-value corroboration incl
  PB0 sig-eq-P313PB0 32/84 NOT-byte-equal, PB1 NEW-sig
  59/88 NOT-byte-equal NOT-SAME-as-C10 29/88,
  PBA88-PLAIN sig-16 M6, C10-NOTPB1 M5,
  QUAD88-4R-STEP + R11 rows + share-14ch +
  r2r3-TRUE-3B + r0+r1-lcs0 + r2r3-lcs3 + QM6 +
  NO frags + b5-step + M-tails NEW,
  T88-RING-STANDARD-COLSPLIT + TM10/TR6 + b0-colsplit +
  tails-split + b84-87 f4728f80 + edges + consts; plus
  sheet-vs-tables const-count note: Q-906 sheet
  81/82/69/70 memo-exact, committed tables
  80/81/69/70 still deduct const-b5 -- S-F arithmetic
  in tables only, geometry exact, PORT verdict stands).
  Agrees with cport commit msg (PYID 9309, RGRAM 18618).
- Quiz: no conflicting CLAIM/GATE/FLAG on b422 (adjacent
  odds b421/b423 GATED PASS by odd seat, base-use and
  adjacency acknowledged; b422 mentions in odd GATEs are
  adjacency notes, no verdict on b422).
  Activity polled (no b422 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r68/ (build422.log,
  pyid422.log, rgram422py/c.log, cmp422.py/.c/.pyo/.co,
  for422.nums/for421base.nums, for422.added, pins422.nums/
  pins421.nums, pass422.names/pins422.names, pins422.added,
  smoke422.log, tables422.log, tabaudit314.py, edges314.py,
  edges422.log, numstat422.txt, addnorm422.txt, delnorm422.txt,
  added422.txt, alladded422.txt, banddiff422.txt,
  pydiff314.txt, cdiff422.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
