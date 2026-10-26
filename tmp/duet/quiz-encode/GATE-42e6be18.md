# GATE 42e6be18 b376 T10P268 pins 110001..110348 (1596 tiers) PASS-functional

Seat sweep2-r57, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r57/w376 @42e6be18.
Band = 8c3709db (py merge w2b@6570612c partial, +6 tiers, +64 pins)
+ 42e6be18 (C port). Base e59e5d25 (b375 tip, 1590 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build376/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 7c94d51b / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52/r53/r54/r55/r56
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 7867/7867 covered=7867/7867 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 15734/15734 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 15734/15734 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (cmp 0 diff, 15734/15734).
- PINS-RGRAM cells set-eq 15734/15734 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 7867/7867 xor 0;
  PINS 15736 rows (2 hdr + 15734 = PASS lines, +64 vs base
  15672). For-list union 7835->7867 +32 (110001 110002
  110003 110004 110008 110013 110017 110018 110019 110020
  110022 110025 110027 110028 110029 110033 110034 110044
  110045 110060 110061 110076 110079 110080 110092 110093
  110207 110208 110236 110335 110336 110348), 0 removed, range
  110001..110348 exact. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 32x2 = 64 = 15734-15670.
  The 32 = S0/S1 (2) + A head/mids/tail (6) + C
  head/mids/tail (6) + Q head/mids/row-edges/step-edge/
  tail (11) + ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P268 C-vs-py, script-compared, TABAUDIT-GREEN
  84 PASS 0 FAIL (tabaudit268.py rc=0): S0/S1 168ch
  EXACT sigs a4740300 NEW / 1d188406 NEW (vs P267
  a0740300 / 1d18e406, full-string ne),
  AM 16/16 8B distinct, CM 10/10 11B distinct, M 16/16
  7B distinct, QR 4/4 4B, QT 4/4 4B, RM 16/16 8B
  distinct, RQ 16/16 7B distinct, AC 74, CC 71, QC 66,
  RC 71; C _N decls 74/71/66/71 match actual;
  byte-coverage unions exact every block (84/84/84/88,
  0 overlap, b4/b5 in no const set, QC b0 split-in-code
  staged).
  PBA16-PLAIN sig db814168 NEW via AC b0-b3 (P267 PBA
  c0822772 per P267AC code-verified), b0 const db; AC
  has no b5 (b5-const memo-1).
  C10-1SIG sig e4492707 x10 via CC b0-b3 (CM carries
  no sig bytes); CM 10/10 diverge (all distinct);
  CC has no b5 (b5-const memo-1).
  QUAD2s col-split: split-b0 (89 iff col<5, FIRST in
  quad) + b1-3 const 9c7472 -> 899c7472 x20 (cols 0-4,
  5x4) + 8a9c7472 x44 (cols 5-15, 11x4); NO frags (code
  has M+R4+T4 legs only, eye-verified); R4 LAST3-
  PAIRED r1==r2==r3 c5dec599 x3, r0 6fcb8377 distinct;
  tails row-shared 4/4 distinct 452ed3b4/b7e31656/
  dce31656/01e41656, r1/r2 share TRUE 3B e31656, r3
  shares 2B-only 1656 (3B differs, both lengths
  checked); b49 const 5a (b49-skipped); QC has no b5.
  Ring STANDARD: RM tail b80-83 (chars 8:16) 16/16
  distinct by COL, RQ tail b76-79 (chars 6:14) 16/16
  distinct by ROW, UNPAIRED (full-row sets + tail sets
  disjoint); RC b0-3 06000000 REPEAT vs P267T (P267 b0-3
  06000000 per P267RC code-verified; staged as sig-repeat,
  ring tabs 0-overlap novel both); RC b84-87
  e365abcd ring-wide NEW (P267 had de93eef2).
  Same-tier RQ-tail4B == M-tail4B 16/16, full-row 0/16
  (staging, NOT a finding per precedent).
  Code-consts vs A-652 INCL (PBA 75 / C10 72 / quad 66 /
  T88 71): impl 74/71/66/71 = memo-1 on PBA/C10,
  identical on quad/T88 (standing incl/excl bookkeeping;
  b5-const excluded).
  M-tails 16/16 ALL NEW vs P267T (zero overlap vs BOTH
  P267RM-tail and P267RQ-tail sets; P267 RM 16ch / RQ
  16ch rows re-read first-hand).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=110001 (PB0 sig a4740300 NEW, lenB 84), S1
  n=110002 (fat PB1 sig 1d188406 NEW, lenB 84),
  A 110003-110018 PBA16-PLAIN (sig db814168 NEW via
  AC b0-b3, b0 const db, AM 16/16 distinct 8B, mtab
  b6-9,76-79, b5 const 5b NO carry raw lencode),
  C 110019-110028 C10-1SIG (sig e4492707 via CC b0-b3,
  CM 10/10 distinct 11B diverge 10/10, mtab
  b6-8,48-51,80-83, b5 const 5b NO carry raw lencode),
  Q 110029-110092 QUAD2s col-split (split-b0 89 iff
  m<5 + b1-3 9c7472, QM7 b9-11,76-79 M 16/16 7B
  shared x3 + R4 b6,7,48,50 LAST3-PAIRED above + QT
  tails above, NO frags, b5 step off>=51 raw lencode),
  R 110093-110348 T88-ring STANDARD (sig 06000000
  REPEAT, TM8 b8-10,19,80-83 by COL RM 16/16, TR7
  b13-15,76-79 by ROW RQ 16/16 UNPAIRED, tails
  SPLIT b80-83 col / b76-79 row, b84-87 const
  e365abcd ring-wide, b4=(0x1b+2off)&FF,
  b5=0x5c+(off>=115)+(off>=243)). C blocks carry
  T73405/73410/73415/73430/73446/73471 py-line mirrors
  (each re-read: hits the exact py guard line), bounds
  + byte positions exact (A 8B, C 11B, Q 7/4/4B, R
  8/7B), counter b4=(27+2off)&FF + (off>=115)+
  (off>=243), temps _t5660-5677 (base max _t5659, no
  reuse) + _b3433/3435/3437/3438/3439/3441/3442 (base
  max _b3431, no reuse) + _i3434/3436/3440/3443 (base
  max _i3432, no reuse), all 6 verified.
  Insert position exact both sides: after T10P267R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-652/A-332 geometry (PB0/PB1 NEW, PBA16
  PLAIN VPOS 9 b5 const 5b 16/16 distinct NO pair,
  C10-1SIG VPOS 12 b5 const 5b 10/10 diverge NO pair,
  QUAD2s VPOS 18 split-b0 FIRST + R4 LAST3-PAIRED +
  QT TRUE-3B/2B-shares + M-tails NEW, T88 VPOS 17
  STANDARD SPLIT + b84-87 e365abcd, lencode 348/348
  whole-tier, ring edges 110207->110208 + 110335->110336,
  NO D dips) incl exact values (PBA/C10 sigs, QR/R4
  values, QT tails, ring TM8/TR7 16/16 UNPAIRED, tails
  SPLIT, consts stand).
- Edges via counter formula first-hand: A head 67/5b
  tail 85/5b b5set {5b} NO carry; PBA formula == raw
  lencode 16/16; C head 87/5b tail 99/5b b5set {5b}
  NO carry; Q head 9b/5b tail 19/5c, step edge 110079
  (o50, ff/5b) -> 110080 (o51, 01/5c) mid-row3;
  ring 110207 (off114, ff/5c) -> 110208 (off115, 01/5d);
  110335 (off242, ff/5d) -> 110336 (off243, 01/5e);
  R head 1b/5c tail 19/5e; all edge pins + tail 110348
  in for-list + 2 PASS lines each py+C. S0/S1 embedded
  b4/b5 (63/5b, 65/5b) match raw lencode. Ring counter
  == raw lencode 256/256, 0 mismatch. Odd-lencode
  348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 612 add / 0 del
  (rgramc.c) + 239/0 (rgram.py) + 1/1 (for-line) +
  64/0 (PINS); raw C grep 607 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 431).
- Wall on band diff added lines (scope e59e5d25..
  42e6be18, 916 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0 hits.
  Files touched: rgramc.c 612/0, rgram.py 239/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, dispatch-guards
  singletons 568->570 +2 / ranges 524->528 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep), CLOSED T10P prints 1496->1502 +6, C singletons
  563->565 +2 / C ranges 524->528 +4 (deltas agree both
  sides), seal 1590->1596 +6 (commit msgs): all agree,
  no slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-652-q780-
  t10p268 verdict CONFIRM (shape 13/13 + quad/ring 15/15
  + counters 14/14 as sectioned; verdict line reads
  42/42 as-filed; file present, counts verified;
  exact-value corroboration incl PBA/C10 sigs, QUAD2s
  split-b0 + R4 last3-pair + QT tails, M-tails NEW,
  ring edges + consts re-checked above) + A-332 viewer
  corroboration (all 3 legs CONFIRM, no correction).
  No CONFIRM-P268.md file; A-652 suffices per rule.
  Agrees with cport commit msg (PYID 7867, RGRAM 15734).
- Quiz: no conflicting CLAIM/GATE/FLAG on b376. Newest
  PARENT-* is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r57/ (build376.log,
  pyid376.log, rgram376py/c.log, cmp376.py/.c,
  for376-old/-new.nums, smoke376.log, tables376.log,
  tabaudit268.py, edges268.py, edges376.log,
  numstat376.txt, add/delnorm376.txt, banddiff376.txt,
  cdiff376.txt, pydiff376.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
