# GATE c28c6aa1 b394 T10P286 pins 116265..116612 (1704 tiers) PASS-functional

Seat sweep2-r61, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r61/w394 @c28c6aa1.
Band = b959a4a1 (py merge w2b@21de6053 partial, +6 tiers, +62 pins)
+ c28c6aa1 (C port). Base 9cac7b4f (b393 tip, 1698 tiers sealed).
Trees diff-identical to tips at archive time (verified via git
ls-tree vs find); w394 +__pycache__ battery byproduct after runs,
w393base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build394/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 1be7f560 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r61
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8437/8437 covered=8437/8437 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 16874/16874 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 16874/16874 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 16874/16874).
- PINS-RGRAM cells set-eq 16874/16874 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8437/8437 xor 0;
  PINS 16876 rows (2 hdr + 16874 = PASS lines, +62 vs base
  16814). For-list union 8406->8437 +31 (116265 116266
  116267 116268 116274 116275 116281 116282 116283 116284
  116287 116288 116291 116292 116293 116308 116309 116317
  116325 116333 116341 116351 116352 116356 116357 116479
  116480 116485 116607 116608 116612),
  0 removed, range 116265..116612 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 16874-16812.
  The 31 = S0/S1 (2) + A head/mids/tail (6) +
  C head/mids/tail (6) + Q head/mids/step-edge/tail (10) +
  ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P286 C-vs-py, script-compared, TABAUDIT-GREEN
  93 PASS 0 FAIL (tabaudit286.py rc=0): S0/S1 168ch
  EXACT sigs 1df80a00 NEW / cd23fd15 (sig-eq P285C10,
  payload NEW: full-string NEW vs BOTH P285S0/S1, diffs
  S0 30/84 + 34/84, S1 57/84 + 46/84),
  AM 16/16 7B distinct, CM 10/10 13B distinct, M 16/16
  9B distinct, QR 4/4 11B distinct, RM 16/16 8B
  distinct, RQ 16/16 9B distinct UNPAIRED, no QT
  (tails live in R11) + no RT (SWAPPED SPLIT),
  M==RQ 16/16 identical INTRA-tier,
  AC 79, CC 69, QC 66, RC 69; C _N decls 79/69/66/69
  match actual; byte-coverage unions exact every block
  (88/84/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN sig 01000000 (b0 const 01; AC
  has no b5, b5 const 8c via lencode) + REPEAT vs
  P285PBA 01000000 (88B-pay PBA sig persists P285->P286;
  novelty = AM rows 0-overlap + M7 geometry
  b38,46,47,80-83 vs P285 M9).
  C10-1SIG cd236d10 x10 (full sig b0-3 in CC
  consts, CM 10/10 diverge; CC has no b5, b5
  const 8c via lencode) + NEW vs P285 C10-1SIG
  cd23fd15 (different sig, M13 geometry b34,35,41-47,
  80-83 vs P285 M12 b24-31,80-83 code-verified).
  QUAD88-4R single-sig 01000000 x64 (QC b0-3;
  QC has no b5, b5 step o>=59 varpos) + rows NEW vs
  P285 QUAD (same R11 width 22ch, 0-overlap
  code-verified; staged: AC-QC shared-pos 66,
  same-val 39, NOT const-repeat; QC positions
  subset of AC positions).
  R11 rows r0 8549271f5406c3bd851512 distinct vs
  r123 share-7B fb421acf3422d6, differ at byte 7
  (4e/73/98); tails b84-87 4/4 distinct
  bd851512/4ec1d406/73c1d406/98c1d406, r123 TRUE
  3B c1d406;
  byte-LCS (0,*)=0, (1,2)=(1,3)=(2,3)=3
  (own code-table LCS, memo/py-comment value
  re-derived exact).
  Ring SWAPPED-tails (NEW geometry, not STANDARD):
  TM8 b6,7,12,13,76-79 by COL RM 16/16 8B (M
  carries b76-79 col), TR9 b51-55,80-83 by ROW
  RQ 16/16 UNPAIRED (R carries b80-83 row);
  RC b0-3 10000000 NEW (P285 sig 16000000),
  b84-87 b0d5787a ring-wide NEW (P285
  e4654e71, both per P285RC code-verified).
  Code-consts vs A-710 INCL (PBA88 80 / C10 70 /
  quad88 66 / T88 69): impl 79/69/66/69 = memo-1
  on PBA/C10 (b5-const excluded), identical
  on quad/T88 (standing bookkeeping).
  M-tails 16/16 ALL NEW vs P285 (zero overlap vs
  P285 M AND P285RM-tail8 AND P285RQ-tail8; P285
  M/RM/RQ rows re-read first-hand). AM/CM/M/QR/
  RM/RQ 0-overlap vs P285 (widths differ M 18ch
  vs 16ch, AM 14ch vs 18ch, CM 26ch vs 24ch,
  RM 16ch vs 14ch, RQ 18ch vs 14ch; QR same
  width 22ch but 0-overlap).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=116265 (PB0 sig 1df80a00 NEW, lenB 84), S1
  n=116266 (fat PB1 sig cd23fd15 ==P285C10 sig,
  57/84 payload diff, lenB 84),
  A 116267-282 PBA88-PLAIN (sig 01000000 via AC
  b0-b3, b0 const 01, AM 16/16 distinct 7B, mtab
  b38,46,47,80-83, b5 const 8c raw lencode),
  C 116283-292 C10-1SIG (cd236d10 x10 via CC
  b0-3, CM 10/10 distinct 13B diverge 10/10,
  mtab b34,35,41-47,80-83, b5 const 8c raw lencode),
  Q 116293-356 QUAD88-4R single-sig 01000000 x64
  (QM9 b51-55,80-83 M 16/16 9B shared x3 + R11
  b38,39,46-50,84-87 rows above (r0 distinct,
  r123 share 7B) + tails above, NO frags, raw
  lencode b5 0x8c+(o>=59)),
  R 116357-116612 T88-SWAPPED (sig 10000000, TM8
  b6,7,12,13,76-79 by COL RM 16/16 8B, TR9
  b51-55,80-83 by ROW RQ 16/16 UNPAIRED,
  b84-87 const b0d5787a ring-wide,
  b4=(0x0b+2off)&FF, b5=0x8d+(off>=123)+(off>=251)).
  C blocks carry T77821/77826/77831/77846/77862/
  77883 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 7B,
  C 13B, Q 9/11B, R 8/9B), Q raw-lencode b5 step
  (equiv counter b4=(0x8b+2off)&FF verified 64/64),
  R counter b4=(0x0b+2off)&FF + (off>=123)+(off>=251),
  temps _t5996-6011 (base max _t5995, no reuse) +
  _b3633/3635/3637/3638/3640/3641 (base max _b3631,
  no reuse) + _i3634/3636/3639/3642 (base max _i3632,
  no reuse), all 6 verified.
  Insert position exact both sides: after T10P285R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-710/A-350 geometry (PB0 NEW, PB1 sig-eq
  P285C10 + 57/84 payload diff, PBA88 PLAIN VPOS 8
  b5 const 8c 16/16 distinct NO pair,
  C10-1SIG VPOS 14 b5 const 8c 10/10 diverge,
  QUAD88-4R VPOS 22 + R11 4/4 UNPAIRED + r123
  share-7B + TRUE-3B + b5 step o58->59 + edge
  116351->116352 + M-tails NEW,
  T88-SWAPPED VPOS 19 + TR9 16/16 UNPAIRED +
  b84-87 b0d5787a + counter 0b/8d/123/251,
  lencode 348/348 whole-tier, Q edge 116351->116352 +
  ring edges 116479->116480 + 116607->116608, NO D
  dips) incl exact values (PBA/C10 sigs, R11 rows +
  tails + LCS, ring TM8/TR9 + consts stand).
- Edges via counter formula first-hand: A head 57/8c
  tail 75/8c b5set {8c} NO step, 0 ff;
  C head 77/8c tail 89/8c b5set {8c} NO step, 0 ff;
  Q head 8b/8c tail 09/8d b5set {8c,8d} step
  o58->59: 116351 (o58, ff/8c) -> 116352 (o59,
  01/8d) Q-row3, exactly 1 ff in 64 (o58);
  ring 116479 (off122, ff/8d) -> 116480 (off123, 01/8e);
  116607 (off250, ff/8e) -> 116608 (off251, 01/8f);
  exactly 2 ff in 256 (o122/o250); R head 0b/8d tail
  09/8f; formula re-derived from T10P286R code text
  (0b/8d/123/251); all edge pins + tail 116612 in
  for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (53/8c, 55/8c) match raw lencode.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 604 add / 0 del
  (rgramc.c) + 230/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 599 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 403).
- Wall on band diff added lines (scope 9cac7b4f..
  c28c6aa1, 897 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 594->596 +2 / ranges 596->600 +4 = +6,
  C singletons 599->601 +2 / ranges 596->600 +4
  (C absolute +5 = standing 5 pre-existing nested py
  guards, gap unchanged since b392 verification),
  CLOSED T10P prints 1604->1610 +6 both sides,
  seal 1698->1704 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-710-q798-
  t10p286 verdict CONFIRM (Q1 shape 14/14 + Q2 quad/ring
  12/12 + Q3 counters 12/12 = 38/38 as-filed; file
  present, counts verified; exact-value corroboration
  incl PB0 NEW + PB1 sig-eq + 57/84 diff, PBA88-PLAIN,
  C10-1SIG, QUAD88-4R + R11 rows + 7B-share + TRUE-3B
  + b5 step + edge + M-tails NEW, ring SWAPPED + TR9
  16/16 UNPAIRED + edges + consts, own P285C10-head
  n115935 reconstruction 57/84 vs P286S1 payload-NEW)
  + A-350 viewer corroboration (all legs CONFIRM,
  1 label nit, no geometry correction). No
  CONFIRM-P286.md file; A-710 suffices per rule.
  Agrees with cport commit msg (PYID 8437, RGRAM
  16874).
- Quiz: no conflicting CLAIM/GATE/FLAG on b394 (adjacent
  odds b393 base-used, b395 beyond-cap acknowledged).
  Activity polled (no b394 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r61/ (build394.log,
  pyid394.log, rgram394py/c.log, cmp394.py/.c,
  for394-w394/-w393base.nums, smoke394.log, tables394.log,
  tabaudit286.py, edges286.py, edges394.log,
  numstat394.txt, add/delnorm394.txt, added394.txt,
  banddiff394.txt, pydiff286.txt, cdiff394.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
