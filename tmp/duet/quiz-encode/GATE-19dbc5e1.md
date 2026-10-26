# GATE 19dbc5e1 b416 T10P308 pins 123921..124268 (1836 tiers) PASS-functional

Seat sweep2-r67, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r67/w416 @19dbc5e1.
Band = 2cda9e71 (py merge w2b@182e07f4 partial, +6 tiers, +62 pins)
+ 19dbc5e1 (C port). Base c9b64be1 (b415 tip, 1830 tiers sealed).
Trees diff-verified identical to tips at archive time (git
ls-tree vs find file lists identical, 117/117 both);
w416 +__pycache__ battery byproduct after runs, w415base clean.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build416/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc d66b52c3 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52-r67
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 9122/9122 covered=9122/9122 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  TMPDIR=NVME scratch, CT_CACHE_DIR set).
- RGRAM py 18244/18244 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 18244/18244 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (ordered identical + raw-order identical, 18244/18244).
- PINS-RGRAM cells set-eq 18244/18244 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 9122/9122 xor 0;
  PINS 18246 rows (2 hdr + 18244 = PASS lines, +62 vs base
  18182). For-list union 9091->9122 +31 (123921 123922
  123923 123924 123930 123931 123937 123938 123939 123940
  123943 123944 123947 123948 123949 123956 123965 123972
  123981 123988 123997 124004 124011 124012 124013 124031
  124032 124159 124160 124200 124268),
  0 removed, range 123921..124268 exact. Each for-N yields
  2 PASS lines (g-zN-closed + g-zN); 31x2 = 62 = 18244-18182.
  The 31 = S0/S1 (2) + A head/mid/tail pairs (6) +
  C head/mid pairs (6) + Q head/7-mids/tail-pair (10) +
  R head/edge-pair/edge-pair/mid/tail (7).
  PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0. (For-line carries a duplicate "0";
  for-list deduped via sort -n -u to 9122, method note.)
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P308 C-vs-py, script-compared, TABAUDIT-GREEN
  110 PASS 0 FAIL (tabaudit308.py rc=0): S0 168ch sig
  ab685400 NEW (33/84 diff vs P307S0) / S1 176ch sig
  01000000 NEW SAME-as-own-C10 (59/88 payload diff vs
  C10[0] first-hand assembled, NOT byte-equal; 70/84
  vs P307S1 which is 84B -- width novelty),
  staged as full-payload singletons,
  AM 16/16 7B distinct, CM 10/10 10B distinct, M 16/16
  4B distinct, QR 4/4 16B distinct, F 16/16 3B distinct,
  RM 16/16 9B distinct, RQ 16/16 7B distinct UNPAIRED,
  no QT (quad tails live in R16) + no RT (SPLIT tails),
  RQ-tail-EQ-M 16/16 (ring TR7 b76-79 row-led values ==
  quad M b80-83 values INTRA-tier; P307 0/16 with
  M-width 12 -- P308 novelty),
  AC 79, CC 76, QC 63, RC 70; C _N decls 79/76/63/70
  match actual; byte-coverage unions exact every block
  (88/88/88/88, 0 overlap, mtab/r-tab/f-tab computed).
  PBA88-PLAIN sig 10000000 (b0 const 10, b5 const
  c8 via lencode; AM 16/16 distinct NO pair; M7
  b6,7,12,80-83) + vs P307PBA 05000000 (novelty =
  new sig 10 + AM 0-overlap).
  C10-1SIG-88 sig 01000000 x10 SAME-as-PB1 (sig in CC
  b0-3 consts; CM 10/10 diverge; rows 0-8 share
  12ch cba8aa5a6d55 + (byte6,byte7) 9 distinct pairs
  (byte7 split 34x4/35x5), tail 92ff; row9 distinct
  a16208df842fb6b0c9df tail c9df; CC has no b5,
  b5 const c8 full block via lencode; M10 tail-tab
  b84-87 first C10 on tail bytes).
  QUAD88-2SIG-MUL2 r0 09000000 x16 + r123 12000000 x48
  (b0 in R16 tab; QM4 b80-83 16/16 distinct shared
  across sig boundary + R16 b0,6-12,52-55,84-87 rows
  r0 0975ec41 distinct all-16B vs r123 share-24ch
  129b07827c158d0042dac637 b84-diverge 13/57/7c,
  tails b84-87 4/4 distinct a0bf881d/13be75da/
  57be75da/7cbe75da, r123 TRUE 3B be75da,
  r0 lcs=0 vs all, r123-pair LCS 3/3/3; FRAG MUL2
  carry-chain b13->b14->b15: F 16 entries 16
  distinct triples incl 00782d 00-case (chain
  00f05a byte-eq b13), chain outputs 16 distinct,
  chain-ne-r0 16/16, b16 const 76 quad-wide;
  b5 const c8, b4 base 0x5b step2 5b..d9 NO edge
  0 ff in 64).
  Ring STANDARD-split: TM9 b12,13,14,18,19,80-83 by
  COL RM 16/16 + TR7 b9,10,11,76-79 by ROW RQ 16/16
  UNPAIRED (tails SPLIT b80-83 col / b76-79 row);
  RC b0-1 0b01, b84-87 e96a6311 ring-wide NEW
  (P307 1ff20ec5, sig 93000000).
  VPOS partitions re-derived from code: PBA 8
  (M7+b4, b5const excluded) / C10 11 (M10+b4,
  b5const excluded) / quad 24 (b4+QM4+R16+F3,
  b5 correctly excluded) / T 18 (TM9+TR7+
  b4+b5) -- all match A-793.
  Code-consts vs A-793 (PBA 80 / C10 77 /
  quad 64 / T88 70): impl 79/76/63/70 =
  memo-exact on T88 only (b5vary, no deduction),
  writer-1 on PBA/C10/QUAD: impl tables still deduct
  const-b5 (b5 covered by lencode instead) while
  Q-900 sheet counts b5-iff-const (memo A-793
  confirms the sheet) -- S-F arithmetic persists
  in committed tables though the sheet is FIXED;
  geometry exact, PORT verdict stands; FLAGGED for
  memo (3rd band running: b412/b414/b416).
  QUAD 2SIG (09 vs 12) vs P307; PBA sig
  10 NEW vs P307 05; AC-QC both=63 sameval=23
  (tables differ).
  M-tails 16/16 ALL NEW vs P307 (zero overlap vs
  P307M AND vs P307RM-tail8 AND vs P307RQ-tail8 --
  P307 widths M12/RM20/RQ14 differ).
  AM/CM/M/QR/RM/RQ 0-overlap vs P307 (prev lens
  16/10/16/4/16/16).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=123921 (PB0 sig ab685400 NEW, 33/84 diff,
  lenB 84), S1 n=123922 (fat PB1 sig 01000000
  NEW same-as-C10, 59/88 diff, lenB 88),
  A 123923-938 PBA88-PLAIN (sig 10000000 via AC
  b0-b3, b0 const 10, AM 16/16 distinct 7B, mtab
  b6,7,12,80-83, raw lencode b4/b5 const c8),
  C 123939-948 C10-1SIG-88 (01000000 x10 SAME-as-PB1
  via CC b0-3 + CM tab, CM 10/10 distinct 10B
  pair-diverge, mtab b6,7,52-55,84-87, b5
  const c8 raw lencode),
  Q 123949-124012 QUAD88-2SIG-MUL2 (QM4 b80-83 M
  16/16 4B + R16 b0,6-12,52-55,84-87 rows above
  (r0 distinct, r123 share 24ch) + F16 ftab q==0
  / fmul2 carry-chain else + tails above, raw
  lencode b5 const c8 b4 5b..d9 NO edge),
  R 124013-268 T88-RING-STANDARD (sig 0b010000,
  TM9 b12-14,18,19,80-83 by COL RM 16/16, TR7
  b9-11,76-79 by ROW RQ 16/16 UNPAIRED,
  b84-87 const e96a6311 ring-wide,
  b4=(0xdb+2off)&FF, b5=0xc8+(off>=19)+(off>=147)).
  C blocks carry T83042/83047/83052/83067/83083/
  83119 py-line mirrors (each re-read: hits the exact
  py guard line), bounds + byte positions exact (A 7B,
  C 10B, Q 4/16/3B, R 9/7B),
  R counter b4=(0xdb+2off)&FF + (off>=19)+(off>=147)
  (C literals 219/200 verified == 0xdb/0xc8),
  temps _t6359-6376 (base max _t6358, no reuse) +
  _i3855/3857/3861/3864 (base max _i3853,
  no reuse) + _b3854/3856/3858/3859/3860/3862/3863
  (base max _b3852, no reuse), all 6 blocks verified.
  Insert position exact both sides: after T10P307R close
  (C 221439-41, block 221442; py CLOSED 83040, guard
  83042), at dispatch tail (N-out-of-scope fallthrough
  follows: C 221659, py 83139).
  Matches A-793 geometry (PB0 NEW + 33/84; PB1 NEW 88B
  SAME-as-C10 59/88 NOT-byte-equal; PBA88-PLAIN VPOS 8
  sig-10 b5 const c8 16/16 distinct, M7;
  C10-1SIG-88 VPOS 11 SAME-as-PB1-sig b5 const tail-tab
  b84-87 10/10 diverge; QUAD88-2SIG-MUL2 VPOS 24 +
  R16 4/4 UNPAIRED + share-24ch + r123-TRUE-3B +
  r0-lcs0 + QM4-shared + F16 + mul2-chain + 00-case +
  b16-76 + M-tails NEW; T88-RING-STANDARD VPOS 18 +
  TM9/TR7 + tails-split + b84-87 e96a6311 + counter
  db/c8/19/147; lencode 348/348 whole-tier, ring
  edges 124031->124032 + 124159->124160, NO D dips)
  incl exact values (PBA/C10/QUAD/T88 sigs, R16 rows
  + tails + LCS, F tab + chain, ring split + consts
  stand; sheet-vs-tables const-count note is S-F
  arithmetic in tables only per memo, geometry
  unaffected; RQ-tail-EQ-M equality unmentioned by
  memo, batteries confirm, tier stands).
- Edges via counter formula first-hand: A head 27/c8
  tail 45/c8 b5set {c8} NO step, 0 ff;
  C head 47/c8 tail 59/c8 b5set {c8} NO step, 0 ff;
  Q head 5b/c8 tail d9/c8 b5set {c8} NO step,
  0 ff in 64 (b4 base 0x5b step2 64/64);
  ring 124031 (off18, ff/c8) -> 124032 (off19, 01/c9);
  124159 (off146, ff/c9) -> 124160 (off147, 01/ca);
  exactly 2 ff in 256; R head db/c8 tail
  d9/ca (Q tail d9/c8 vs R tail d9/ca differ in b5 --
  labeled apart); formulas re-derived from T10P308R
  code text (db/c8/19/147) + T10P308Q text
  (5b/d9 NO edge); all edge pins + tail
  124268 in for-list + 2 PASS lines each py+C. S0/S1
  embedded b4/b5 (23/c8, 25/c8) match raw lencode.
  Odd-lencode 348/348. No DISSENT on cut bytes.
- C diff purely additive: numstat 656 add / 0 del
  (rgramc.c) + 265/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 651 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 460).
- Wall on band diff added lines (scope c9b64be1..
  19dbc5e1, 984 added lines): vendor 0 hits,
  disasm 0 hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  compression_tool//usr/bin/aa/nominated/shim/ct-cache
  0 hits, shebang 0 hits.
  Files touched: rgramc.c 656/0, rgram.py 265/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  (4-space dispatch-exact) singletons 638->640 +2 /
  ranges 662->666 +4 = +6, C identical deltas 643->645
  +2 / 684->688 +4 (py=C dispatch-exact; nested extras
  outside dispatch scope, standing bookkeeping, deltas
  agree every side),
  CLOSED T10P prints 1736->1742 +6 both sides,
  seal 1830->1836 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-793-q900-P308
  verdict CONFIRM 62/62 CLEAN (b1 shape 26/26 + b2
  quad+T 22/22 + b3 counters 14/14; file present,
  counts verified; exact-value corroboration incl
  PB0 NEW, PB1 88B SAME-as-C10 59/88 NOT-byte-equal,
  PBA88-PLAIN sig-10 M7, C10-1SIG-88 SAME-as-PB1-sig
  M10 tail-tab, QUAD88-2SIG-MUL2 + R16 rows +
  share-24ch + r123-TRUE-3B + r0-lcs0 + QM4-shared +
  F16 + mul2-chain + M-tails NEW, T88-RING-STANDARD +
  TM9/TR8 + tails-split + b84-87 e96a6311 + edges +
  consts; plus sheet-vs-tables const-count note: Q-900
  sheet FIXED-rule 80/77/64/70 memo-exact, committed
  tables 79/76/63/70 still deduct const-b5 -- S-F
  arithmetic in tables only, geometry exact, PORT
  verdict stands).
  Agrees with cport commit msg (PYID 9122, RGRAM 18244).
- Quiz: no conflicting CLAIM/GATE/FLAG on b416 (adjacent
  odds b415 base-used, b417 sweep-turf acknowledged).
  Activity polled (no b416 conflict); PROSE-01 re-read
  before filing (all hex/counts copied from run output
  above).
- Logs: NVME ws tmp/encode-sweep2/r67/ (build416.log,
  pyid416.log, rgram416py/c.log, cmp416.py/.c/.pyo/.co,
  for416.nums/for415base.nums, pins416.nums/pins415.nums,
  pass416.names/pins416.names, smoke416.log, tables416.log,
  tabaudit308.py, edges308.py, edges416.log,
  numstat416.txt, addnorm416.txt, delnorm416.txt,
  added416.txt, alladded416.txt, banddiff416.txt,
  pydiff308.txt, cdiff416.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
