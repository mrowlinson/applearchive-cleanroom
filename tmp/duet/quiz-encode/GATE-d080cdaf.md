# GATE d080cdaf b410 T10P302 pins 121833..122180 (1800 tiers) PASS-functional

Seat sweep2-r65, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r65/w410 @d080cdaf.
Band = d5fabfc0 (py merge w2b@50c73988 partial, +6 tiers, +62 pins)
+ d080cdaf (C port). Base 676b823c (b409 tip, 1794 tiers sealed).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 = 113 non-tmp
+ 4 tmp); w410 +__pycache__ battery byproduct after runs,
w409base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build410/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 767417f4 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r65
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 8936/8936 covered=8936/8936 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 17872/17872 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 17872/17872 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 17872/17872).
- PINS-RGRAM cells set-eq 17872/17872 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 8936/8936 xor 0;
  PINS 17874 rows (2 hdr + 17872 = PASS lines, +62 vs base
  17812). For-list union 8905->8936 +31 (121833 121834
  121835 121836 121842 121843 121849 121850 121851 121852
  121855 121856 121859 121860 121861 121869 121877 121885
  121893 121901 121909 121917 121923 121924 121925 121983
  121984 122053 122111 122112 122180),
  0 removed, range 121833..122180 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 17872-17810.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/step-edge/tail pairs (6, o4->5 edge pinned) +
  Q head/mids/tail-pair (10, b5 const full block) +
  ring head/edge-pairs/mid/tail (7, 2 edge pairs pinned;
  one fewer ring mid than the usual 32 -- hence +62).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P302 C-vs-py, script-compared, TABAUDIT-GREEN
  112 PASS 0 FAIL (tabaudit302.py rc=0): S0/S1 168ch
  EXACT sigs 0b913100 NEW / 8031ff44 NEW (both NEW
  vs P301 sigs 2ab31200 / 0b887b25, full-payload NEW;
  staged as full-payload singleton consts; S1 sig-eq
  own-C10 b0-3 AND 47/84 payload byte-diff vs n121851
  reconstructed first-hand (CM0 + CC + lencode) --
  NOT byte-equal, comment corroborated),
  AM 16/16 7B distinct, CM 10/10 12B distinct, M 16/16
  6B distinct, QR 4/4 12B distinct, RM 16/16 7B
  distinct, RQ 16/16 6B distinct UNPAIRED, no QT
  (quad tails live in R12) + no RT (SPLIT tails) +
  no RF (no frag this tier),
  M==RQ 16/16 identical INTRA-tier (SWAPPED),
  AC 79, CC 70, QC 68, RC 73; C _N decls 79/70/68/73
  match actual; byte-coverage unions exact every block
  (88/84/88/88, 0 overlap, mtab/r-tab computed).
  PBA88-PLAIN sig 04000000 NEW (b0 const 04, b5 const
  b7 via lencode; AM 16/16 distinct NO pair; M7
  b38,46,47,80-83) + vs P301PBA 02000000 (novelty =
  new sig 04 + AM 0-overlap + M7 geometry).
  C10-STEP 8031ff44 x10 SAME-as-PB1-sig (sig in CC
  b0-3 consts; CM 10/10 diverge 12B; rows 0-7 share
  16ch d317d510bf740ac0 ch16 9/9/b/d/f/1/3/5, row0
  tail7 6e8cdb7 unique, rows 1-4 tail7 865d3b7,
  rows 5-7 tail7 866d3b7; rows 8-9 distinct heads
  4b14/4b15; CC has no b5, b5 stepped b7/b8 via
  lencode edge o4->5).
  QUAD88-4R single-sig 04000000 x64 (QC b0-3;
  b5 const b8 full 64/64 via lencode, NO step, NO
  ff; QM6 16/16 distinct NO frags + R12 rows r0
  1b029522 distinct vs r123 share-8B
  733415261f744e3e byte8-diverge 0b/30/af, tails
  b84-87 4/4 distinct b5a79a30/0bc7cad2/30c7cad2/
  af86cbd2, r12 TRUE 3B c7cad2, r3 1B d2;
  byte-LCS (1,2)=3, (1,3)=(2,3)=1, (0,1)=(0,3)=0,
  (0,2)=1 -- NOTE py-comment + memo say "r0 lcs=0"
  but first-hand tails (0,2)=1 via shared single
  byte 0x30 (r0 ..9a30 vs r2 30..); prose shorthand
  only, tails still 4-distinct, TRUE-3B/1B stand,
  geometry unaffected, tier stands).
  Ring SWAPPED-tails: TM7 b6,7,9,76-79 by COL RM
  16/16 7B + TR6 b52,53,80-83 by ROW RQ 16/16
  UNPAIRED (tails SWAPPED b76-79 col / b80-83 row;
  b8 const 9d, no frag); RC b0-3 48000000, b84-87
  badbc491 ring-wide NEW (P301 1d404253).
  VPOS partitions re-derived from code: PBA 8
  (M7+b4, b5const excluded) / C10 14 (M12+b4+b5vary)
  / quad 19 (QM6+R12+b4; b5 excluded const-b8,
  b51 excluded const-d1 in QC) / T 15 (TM7+TR6+
  b4+b5) -- all match A-770 incl b51/b5 exclusions.
  Code-consts vs A-770 INCL (PBA80 / C10 70 /
  quad 69 / T88 73): impl 79/70/68/73 =
  memo identical on C10/T88, writer-1 on PBA/quad
  (A-770 S-F: writer deducted const-b5 where b5vary
  is False so no deduction applies -- writer
  arithmetic only, geometry exact, PORT verdict
  stands).
  M-tails 16/16 ALL NEW vs P301 (zero overlap vs
  P301RQ ROW-led tails per memo -- P301T SWAPPED --
  AND vs P301M AND P301RM-tail8; P301 M/RM/RQ rows
  re-read first-hand). AM/CM/M/QR/RM/RQ 0-overlap
  vs P301 (widths P302 AM14/CM24/M12/QR24/RM14/RQ12
  vs P301 AM16/CM24/M20/QR22/RM16/RQ16; same-width
  CM pair 0-overlap by content).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=121833 (PB0 sig 0b913100 NEW, lenB 84), S1
  n=121834 (fat PB1 sig 8031ff44 NEW ==own-C10-sig,
  47/84 diff vs n121851, lenB 84),
  A 121835-850 PBA88-PLAIN (sig 04000000 via AC
  b0-b3, b0 const 04, AM 16/16 distinct 7B, mtab
  b38,46,47,80-83, b5 const b7 raw lencode),
  C 121851-860 C10-STEP (8031ff44 x10 SAME-as-PB1
  via CC b0-3 + CM tab, CM 10/10 distinct 12B
  diverge 10/10, mtab b34,35,41-46,80-83, b5
  0xb7+(o>=5) raw lencode step o4->5),
  Q 121861-924 QUAD88-4R single-sig 04000000 x64
  (QM6 b52,53,80-83 M 16/16 6B shared x4 + R12
  b38,39,45-50,84-87 rows above (r0 distinct,
  r123 share 8B) + tails above, NO frags, raw
  lencode b5 const b8 full block),
  R 121925-180 T88-RING-SWAPPED (sig 48000000,
  TM7 b6,7,9,76-79 by COL RM 16/16 7B, TR6
  b52,53,80-83 by ROW RQ 16/16 UNPAIRED,
  b84-87 const badbc491 ring-wide,
  b4=(0x8b+2off)&FF, b5=0xb8+(off>=59)+(off>=187)).
  C blocks carry T81619/81624/81629/81644/81660/
  81681 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 7B,
  C 12B, Q 6/12B, R 7/6B),
  R counter b4=(0x8b+2off)&FF + (off>=59)+(off>=187)
  (C literals 139/184 verified == 0x8b/0xb8),
  temps _t6261-6276 (base max _t6260, no reuse) +
  _b3794/3796/3798/3799/3801/3802 (base max _b3792,
  no reuse) + _i3795/3797/3800/3803 (base max _i3793,
  no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P301R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-770 geometry (PB0/PB1 NEW sigs + S1
  sig-eq-own-C10 + 47/84 NOT-byte-equal; PBA88-PLAIN
  VPOS 8 new-sig-04 b5 const b7 16/16 distinct NO
  pair, C10-STEP VPOS 14 b5 step 10/10 diverge,
  QUAD88-4R VPOS 19 + R12 4/4 UNPAIRED + share-8B +
  r12-TRUE-3B + r3-1B + b5 const + M-tails NEW,
  T88-RING-SWAPPED VPOS 15 + TM7/TR6 + tails-swapped
  + b84-87 badbc491 + counter 8b/b8/59/187,
  lencode 348/348 whole-tier, ring edges
  121983->121984 + 122111->122112, C10 step edge
  121855->121856, NO D dips) incl exact values (PBA/
  C10/QUAD/T88 sigs, R12 rows + tails + LCS, ring
  swap + consts stand; S-F const-count note is writer
  arithmetic per memo, geometry unaffected; LCS-NOTE
  above is the one prose imprecision found, cut bytes
  stand).
- Edges via counter formula first-hand: A head d7/b7
  tail f5/b7 b5set {b7} NO step, 0 ff;
  C head f7/b7 tail 09/b8 b5step o4->5 (121855
  ff/b7 -> 121856 01/b8), exactly 1 ff in 10;
  Q head 0b/b8 tail 89/b8 b5set {b8} NO step,
  0 ff in 64 (b5 const full block, b4 base 0x0b
  step2 64/64);
  ring 121983 (off58, ff/b8) -> 121984 (off59, 01/b9);
  122111 (off186, ff/b9) -> 122112 (off187, 01/ba);
  exactly 2 ff in 256; R head 8b/b8 tail
  89/ba (Q tail 89/b8 vs R tail 89/ba differ in b5 --
  labeled apart); formulas re-derived from T10P302R
  code text (8b/b8/59/187) + T10P302C text
  (b7/5/4/5); all edge pins + tail
  122180 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (d3/b7, d5/b7) match raw lencode.
  Odd-lencode 348/348. No DISSENT on cut bytes.
- C diff purely additive: numstat 604 add / 0 del
  (rgramc.c) + 232/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 599 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 399).
- Wall on band diff added lines (scope 676b823c..
  d080cdaf, 899 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 604/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 626->628 +2 /
  ranges 638->642 +4 = +6, C identical 626->628 +2 /
  638->642 +4 (py=C dispatch-exact; nested 8-space extras
  outside dispatch scope, standing bookkeeping, deltas
  agree every side),
  CLOSED T10P prints 1700->1706 +6 both sides,
  seal 1794->1800 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-770-q894-P302
  verdict CONFIRM 53/55 + S-F (b1 shape 25/25 + b2
  quad+T 15/15 + b3 counters 13/15; the 2 short are
  S-F writer const-arithmetic, geometry exact, PORT
  verdict; file present, counts verified;
  exact-value corroboration incl PB0/PB1 NEW sigs +
  S1 47/84 NOT-byte-equal, PBA88-PLAIN new-sig-04,
  C10-STEP + edge, QUAD88-4R + R12 rows + 8B-share +
  r12-TRUE-3B + r3-1B + b5 const + M-tails NEW,
  T88-RING-SWAPPED + TM7/TR6 + tails-swapped +
  b84-87 badbc491 + edges + consts; plus LCS-NOTE:
  "r0 lcs=0" shorthand imprecise first-hand
  ((0,2)=1 shared 0x30), prose-only, tier stands).
  No CONFIRM-P302.md file; A-770 suffices per rule.
  Agrees with cport commit msg (PYID 8936, RGRAM 17872).
- Quiz: no conflicting CLAIM/GATE/FLAG on b410 (adjacent
  odds b409 base-used, b411 sweep-turf acknowledged).
  Activity polled (no b410 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r65/ (build410.log,
  pyid410.log, rgram410py/c.log, cmp410.py/.c,
  for410.nums/for409base.nums, smoke410.log, tables410.log,
  tabaudit302.py, edges302.py, edges410.log,
  numstat410.txt, add/delnorm410.txt, added410.txt,
  banddiff410.txt, pydiff302.txt, cdiff410.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
