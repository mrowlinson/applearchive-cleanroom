# GATE b8ca9f9b b404 T10P296 pins 119745..120092 (1764 tiers) PASS-functional

Seat sweep2-r64, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r64/w404 @b8ca9f9b.
Band = d6f51bc4 (py merge w2b@40052c13 partial, +6 tiers, +62 pins)
+ b8ca9f9b (C port). Base d525fb04 (b403 tip, 1758 tiers sealed).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117); w404 +__pycache__
battery byproduct after runs, w403base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build404/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 28043d02 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r64
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8748/8748 covered=8748/8748 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 17496/17496 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 17496/17496 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical, 17496/17496).
- PINS-RGRAM cells set-eq 17496/17496 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8748/8748 xor 0;
  PINS 17498 rows (2 hdr + 17496 = PASS lines, +62 vs base
  17436). For-list union 8717->8748 +31 (119745 119746
  119747 119748 119754 119755 119761 119762 119763 119764
  119767 119768 119771 119772 119773 119788 119789 119797
  119805 119807 119808 119821 119829 119836 119837 119935
  119936 119965 120063 120064 120092),
  0 removed, range 119745..120092 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 17496-17434.
  The 31 = S0/S1 (2) + A head/mids/tail (6) +
  C head/mids/tail (6) + Q head/mids/tail/step-edge (10,
  o34->35 edge pinned) + ring head/edge-pairs/mid/tail (7).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P296 C-vs-py, script-compared, TABAUDIT-GREEN
  103 PASS 0 FAIL (tabaudit296.py rc=0): S0/S1 168ch
  EXACT sigs 63501000 SIG-EQ-P295PB0 / 7b80af20
  NEW-own-C10 (S diffs: S0 31/84 vs P295S0, S1 46/84
  vs own C10-head n119763; P295 sigs 63501000 /
  f2c7a020; sig-eq NEVER byte-equal, standing rule),
  AM 16/16 10B distinct, CM 10/10 12B distinct, M 16/16
  8B distinct, QR 4/4 11B distinct, RM 16/16 8B
  distinct, RQ 16/16 8B distinct UNPAIRED, no QT
  (tails live in R11) + no RT (STANDARD SPLIT),
  M==RQ 16/16 identical INTRA-tier,
  AC 76, CC 70, QC 67, RC 70; C _N decls 76/70/67/70
  match actual; byte-coverage unions exact every block
  (88/84/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN sig 02000000 (b0 const 02; AC
  has no b5, b5 const a7 via lencode) + REPEAT vs
  P295PBA 02000000 (88B-pay PBA sig persists P295->P296;
  novelty = AM widths 20ch vs P295 14ch 0-overlap +
  M10 geometry b18,19,25-27,35,80-83).
  C10-1SIG 7b80af20 x10 SAME-as-PB1-sig (sig in CC
  const b0-3; CM 10/10 diverge 12B; CM rows 0-7 share
  16ch 1be355f8f58e6f07 byte8 8-diverge, rows 8-9
  share 16ch 737f4df955e51906 differ byte 8 (fb/ef);
  CC has no b5, b5 const a7 via lencode).
  QUAD88-4R single-sig 02000000 x64 (QC b0-3;
  QC has no b5, b5 stepped 0xa7+(o>=35) via lencode,
  step edge o34->35 ff/a7->01/a8, exactly 1 ff) +
  rows NEW vs P295 QUAD (R11 width 22ch same as P295,
  0-overlap by content code-verified; staged: AC-QC
  shared-pos 64, same-val 31, NOT const-repeat;
  12 AConly + 3 QConly).
  R11 rows r0 bfbd937e55ff42 distinct vs
  r123 share-7B 6757b37f75526e, differ at byte 7
  (a5/ca/ef); b39-skipped const 6e verified in QC;
  tails b84-87 4/4 distinct
  057437ba/a56fbb3a/ca6fbb3a/ef6fbb3a, r123 TRUE
  3B 6fbb3a;
  byte-LCS (0,1)=(0,2)=(0,3)=0, (1,2)=(1,3)=(2,3)=3
  (own code-table LCS hand-verified: r0 shares no
  byte-run with r123 tails; r0 lcs=0 memo/py-comment
  agrees; memo claims only 'differ in tail bytes',
  no conflict).
  Ring STANDARD-split: TM8 b30,39,46,47,80-83 by COL
  RM 16/16 8B (M carries b80-83 col), TR8
  b40-43,76-79 by ROW RQ 16/16 UNPAIRED (R carries
  b76-79 row); RC b0-3 26000000 NEW (P295 sig
  20000000), b84-87 2f7cf316 ring-wide NEW (P295
  21e74240, per P295RC code-verified).
  Code-consts vs A-749 INCL (PBA88 77 / C10 71 /
  quad88 67 / T88 70): impl 76/70/67/70 = memo-1
  on PBA/C10 (b5-const excluded), identical
  on quad/T88 (standing bookkeeping).
  M-tails 16/16 ALL NEW vs P295 (zero overlap vs
  P295 M AND P295RM-tail8 AND P295RQ-tail8; P295
  M/RM/RQ rows re-read first-hand). AM/CM/M/QR/
  RM/RQ 0-overlap vs P295 (widths differ AM 20ch
  vs 14ch, CM 24ch vs 22ch, RM 16ch vs 12ch;
  M/RQ 16ch + QR 22ch same width, 0-overlap by
  content).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=119745 (PB0 sig 63501000 SIG-EQ P295PB0,
  31/84 payload diff, NOT byte-equal, lenB 84), S1
  n=119746 (fat PB1 sig 7b80af20 NEW ==own-C10-sig,
  46/84 diff vs own C10-head n119763, NOT byte-equal,
  lenB 84),
  A 119747-762 PBA88-PLAIN (sig 02000000 via AC
  b0-b3, b0 const 02, AM 16/16 distinct 10B, mtab
  b18,19,25-27,35,80-83, b5 const a7 raw lencode),
  C 119763-772 C10-1SIG (7b80af20 x10 via CC
  b0-3, CM 10/10 distinct 12B diverge 10/10,
  mtab b22,23,30-35,80-83, b5 const a7 raw lencode),
  Q 119773-836 QUAD88-4R single-sig 02000000 x64
  (QM8 b40-43,80-83 M 16/16 8B shared x4 + R11
  b26,27,34-38,84-87 rows above (r0 distinct,
  r123 share 7B) + tails above, b39 const 6e, NO
  frags, raw lencode b5 0xa7+(o>=35) step o34->35),
  R 119837-120092 T88-STANDARD (sig 26000000, TM8
  b30,39,46,47,80-83 by COL RM 16/16 8B, TR8
  b40-43,76-79 by ROW RQ 16/16 UNPAIRED,
  b84-87 const 2f7cf316 ring-wide,
  b4=(0x3b+2off)&FF, b5=0xa8+(off>=99)+(off>=227)).
  C blocks carry T80186/80191/80196/80212/80228/
  80249 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 10B,
  C 12B, Q 8/11B, R 8/8B),
  R counter b4=(0x3b+2off)&FF + (off>=99)+(off>=227)
  (C literals 59/168 verified == 0x3b/0xa8),
  temps _t6161-6176 (base max _t6160, no reuse) +
  _b3734/3736/3738/3739/3741/3742 (base max _b3732,
  no reuse) + _i3735/3737/3740/3743 (base max _i3733,
  no reuse), all 6 verified.
  Insert position exact both sides: after T10P295R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-749/A-360 geometry (PB0 sig-eq + 31/84,
  PB1 sig-eq-own-C10 + 46/84, NEVER byte-equal per w2b
  standing rule; PBA88 PLAIN VPOS 11 b5 const a7
  16/16 distinct NO pair, C10-1SIG VPOS 13 b5 const
  a7 10/10 diverge, QUAD88-4R VPOS 21 + R11 4/4
  UNPAIRED + share-7B + TRUE-3B + b5 step +
  M-tails NEW, T88-STANDARD VPOS 18 + TR8 16/16
  UNPAIRED + b84-87 2f7cf316 + counter 3b/a8/99/227,
  lencode 348/348 whole-tier, ring edges
  119935->119936 + 120063->120064, Q step edge
  119807->119808, NO D dips) incl exact values
  (PBA/C10 sigs, R11 rows + tails + LCS, ring
  TM8/TR8 + consts stand; A-360 S0 byte-equal prose
  STALE per NOTE-w2b-r24-p296-pb0-sigeq, geometry
  unaffected).
- Edges via counter formula first-hand: A head 87/a7
  tail a5/a7 b5set {a7} NO step, 0 ff;
  C head a7/a7 tail b9/a7 b5set {a7} NO step, 0 ff;
  Q head bb/a7 tail 39/a8 step o34->35 (119807 ff/a7
  -> 119808 01/a8), exactly 1 ff in 64;
  ring 119935 (off98, ff/a8) -> 119936 (off99, 01/a9);
  120063 (off226, ff/a9) -> 120064 (off227, 01/aa);
  exactly 2 ff in 256; R head 3b/a8 tail
  39/aa (Q tail 39/a8 vs R tail 39/aa differ in b5 --
  labeled apart); formula re-derived from T10P296R
  code text (3b/a8/99/227) + T10P296Q text
  (a7/35/34/35); all edge pins + tail
  120092 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (83/a7, 85/a7) match raw lencode.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 604 add / 0 del
  (rgramc.c) + 231/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 599 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 402).
- Wall on band diff added lines (scope d525fb04..
  b8ca9f9b, 898 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 604/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 614->616 +2 /
  ranges 614->618 +4 = +6, C identical 614->616 +2 /
  614->618 +4 (py=C dispatch-exact; nested 8-space extras
  5 singletons + 22 ranges outside dispatch scope, standing
  bookkeeping, deltas agree every side),
  CLOSED T10P prints 1664->1670 +6 both sides,
  seal 1758->1764 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-749-q888-
  t10p296 verdict CONFIRM (Q1 shape 14/14 + Q2 quad/ring
  11/11 + Q3 counters 14/14 = 39/39 as-filed + TBD settled;
  file present, counts verified; exact-value corroboration
  incl PB0/PB1 sig-eq + 31/84 + 46/84 diffs, PBA88-PLAIN,
  C10-1SIG, QUAD88-4R + R11 rows + 7B-share +
  r123-TRUE-3B + b5 step + M-tails NEW, ring STANDARD +
  TR8 16/16 UNPAIRED + edges + consts, own C10-head
  n119763 reconstruction 46/84 vs S1 (sig 7b80af20
  sig-eq own-C10sig, NOT byte-equal -- S1 staged
  full-payload))
  + A-360 corroboration (legs CONFIRM; S0 byte-equal
  prose STALE per w2b correction, geometry unaffected).
  No CONFIRM-P296.md file; A-749 suffices per rule.
  Agrees with cport commit msg (PYID 8748, RGRAM 17496).
- Quiz: no conflicting CLAIM/GATE/FLAG on b404 (adjacent
  odds b403 base-used, b405 sweep-turf acknowledged).
  Activity polled (no b404 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r64/ (build404.log,
  pyid404.log, rgram404py/c.log, cmp404.py/.c,
  for404-w404/-w403base.nums, smoke404.log, tables404.log,
  tabaudit296.py, edges296.py, edges404.log,
  numstat404.txt, add/delnorm404.txt, added404.txt,
  banddiff404.txt, pydiff296.txt, cdiff404.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
