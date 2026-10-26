# GATE a961bc67 b366 T10P258 pins 106521..106868 (1536 tiers) PASS-functional

Seat sweep2-r54, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r54/w366 @a961bc67.
Band = beeebf03 (py merge w2b@e7f2f5da partial, +6 tiers, +62 pins)
+ a961bc67 (C port). Base 926c1bd9 (b365 tip, 1530 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build366/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 1ce06e6d / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52/r53/r54 builds;
  band touches no aae sources per numstat).
- RGRAMC-PYID 7556/7556 covered=7556/7556 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 15112/15112 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 15112/15112 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (cmp 0 diff, 15112/15112).
- PINS-RGRAM cells set-eq 7556/7556 (xor 0, PINS base-N
  set vs for-list; PASS-names vs PINS-names xor 0);
  PINS 15114 rows (2 hdr + 15112 = PASS lines, +62 vs base
  15052). For-list union +31 (106521 106522 106523 106524
  106529 106533 106537 106538 106539 106542 106543 106544
  106545 106546 106547 106548 106549 106564 106565 106580
  106581 106596 106597 106612 106613 106623 106624 106741
  106751 106752 106868), 0 removed, range 106521..106868
  exact. Each for-N yields 2 PASS lines (g-zN-closed +
  g-zN); 31x2 = 62 = 15112-15050.
  The 31 = S0/S1 (2) + A head/mids/tail (6) + C
  head/6-sig-probes/tail (8) + Q head/mid-pairs/tail
  (8) + ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P258 C-vs-py, script-compared, TABAUDIT-GREEN
  76 PASS 0 FAIL (tabaudit258.py rc=0): S0/S1 168ch
  EXACT sigs 20370300 NEW / f8416e06 NEW (vs P257
  601a0300 / e58c3506, code-verified), AM 16/16 8B
  distinct, CM 10/10 15B distinct, M 16/16 6B, QR 4/4
  7B distinct UNPAIRED, QT 4/4 4B, RM 16/16 9B
  distinct (widest M yet), RQ 16/16 6B distinct, AC
  74, CC 67, QC 65, RC 71; C _N decls 74/67/65/71
  match actual; byte-coverage unions exact every block
  (84/84/84/88, 0 overlap, b4/b5 in no const set).
  CM 6-sig map exact order: 85c86106 x4 @106539-42 +
  2dbe3b03/8d963a03/5d533103/7d053403 x1 @106543-46
  + 851a3e03 x2 @106547-48 (b0-3 in tab, CC has no
  b0-3; 6 distinct sigs in order, 10/10 diverge NO
  pair).
  QR values d08f8179922dee/a5d2616e929df4/
  2ba0517412c0dc/9a8aa177927ed7 EXACT (4/4 distinct
  UNPAIRED, first R with NO pairing); QC b0-3
  e0921f3a single-sig x64 (b3 const).
  QT values f2bc5daa/49f3db15/dab7ba8e/1469107b
  (4/4 distinct; last bytes aa/15/8e/7b all differ,
  last-3B all differ, no shared suffix).
  AC b0-3 40811f74 NEW vs P257PBA a0802f7c
  (code-verified).
  RC b0-3 03000000 ==P255T (code-verified vs P255RC
  b0-3); RC b84-87 0b3bb263 ring-wide.
  RM/RQ UNPAIRED, tails SPLIT (RM b80-83 by COL 16/16,
  RQ b76-79 by ROW 16/16).
  Same-tier RQ rows = M rows 16/16 full-row (byte
  positions differ: QM6 b24,25 vs TR6 b28,29 -
  staging, NOT a finding per precedent).
  Code-consts vs A-615 INCL (PBA 75 / C10 68 / quad 66 /
  T88 71): impl 74/67/65 = memo-1 on PBA/C10/quad
  (standing incl/excl bookkeeping), 71 identical on
  T88.
  M-tails 16/16 ALL NEW vs P257T (zero overlap vs BOTH
  P257RM-tail and P257RQ-tail sets; P257 RM/RQ 16x14ch
  order re-read first-hand).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=106521 (PB0 sig 20370300 NEW, lenB 84), S1
  n=106522 (fat PB1 sig f8416e06 NEW, lenB 84),
  A 106523-106538 PBA16 (sig 40811f74 NEW via AC
  b0-b3, AM 16/16 distinct 8B, mtab b12-14,19,76-79,
  b5 const 40 raw lencode),
  C 106539-106548 C10-MS 6-sig (sig map exact order
  above, CM 10/10 distinct 15B diverge 10/10, mtab
  b0-3,11,18-23,80-83 sig-bytes-in-tab, b5 const
  40),
  Q 106549-106612 QUAD single-sig e0921f3a x64
  (QM6 b24,25,76-79 M 16/16 6B + R7 b13,14,18-22
  UNPAIRED above + QT tails above, b5 const 40 NO
  carry raw lencode),
  R 106613-106868 T88-ring STANDARD (sig 03000000
  ==P255T, TM9 b18,19,27,34,35,80-83 by COL RM
  16/16 widest-9, TR6 b28,29,76-79 by ROW RQ 16/16
  UNPAIRED, tails SPLIT b80-83 col / b76-79 row,
  b84-87 const 0b3bb263 ring-wide, b4=(0xeb+2off)
  &FF, b5=0x40+(off>=11)+(off>=139)). C blocks carry
  T70829/70834/70839/70854/70871/70894 py-line mirrors
  (each re-read: hits the exact py guard line), bounds
  + byte positions exact (A 8B, C 15B, Q 6/7/4B, R
  9/6B), counter b4=(0xeb+2off)&FF + (off>=11)+
  (off>=139), temps _t5464-5481 (base max _t5463, no
  reuse) + _b3324-3333/_i3325-3334 (base max
  _b3322/_i3323, no reuse), all 6 verified.
  Insert position exact both sides: after T10P257R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-615/A-322 geometry (PB0/PB1 NEW, PBA16 VPOS
  9 b5 const 40 NO pair, C10-MS VPOS 16 6-sig b5 const
  40 10/10 diverge NO pair, QUAD VPOS 18 single-sig +
  R7 UNPAIRED + QT no-shared-suffix + M-tails NEW, T88
  VPOS 17 STANDARD SPLIT + b84-87 0b3bb263, lencode
  348/348 whole-tier, NO Q-carry, ring edges
  106623->106624 + 106751->106752, NO D dips) incl
  exact values (CM 6-sig map, QR 4/4, QT tails, ring
  TM9/TR6 16/16 UNPAIRED, tails SPLIT, consts stand).
- Edges via counter formula first-hand: Q b5 const 40
  NO carry (head 6b/40 @106549, tail e9/40 @106612);
  ring 106623 (off10, ff/40) -> 106624 (off11, 01/41);
  106751 (off138, ff/41) -> 106752 (off139, 01/42);
  all four edge pins + tail 106868 in for-list + 2 PASS
  lines each py+C. A b5set {40}, C b5set {40}, Q
  b5set {40}. A head 37/40 tail 55/40, C head 57/40
  tail 69/40, R head eb/40 tail e9/42. Ring counter ==
  raw lencode 256/256, 0 mismatch. Odd-lencode 348/348.
  No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del
  (rgramc.c) + 239/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 605 content + 5 blank-only
  `+` lines (verified bare) / 0 del; fine-norm
  (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD tools,
  empty-excluding) del-subset-add 0 missing (del-uniq
  0, add-uniq 403).
- Wall on band diff added lines (scope 926c1bd9..
  a961bc67, 912 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0 hits.
  Files touched: rgramc.c 610/0, rgram.py 239/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 548->550 +2 / ranges 484->488 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep), CLOSED T10P prints 1436->1442 +6, C singletons
  543->545 +2 (C-vs-py 5-offset pre-existing, unchanged),
  C ranges 484->488 +4, seal 1530->1536 +6: all agree,
  no slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-615-q770-
  t10p258 verdict CONFIRM (shape 12/12 + quad/ring 11/11
  + counters 12/12 as sectioned; verdict line reads
  35/35 as-filed; file present, counts verified;
  exact-value corroboration incl CM 6-sig map, QR 4/4
  UNPAIRED, QT tails no-shared-suffix, single-sig,
  M-tails NEW, ring edges + consts re-checked above) +
  A-322 viewer corroboration (all 3 legs CONFIRM).
  No CONFIRM-P258.md file; A-615 suffices per rule.
  Agrees with cport commit msg (PYID 7556, RGRAM 15112).
- Quiz: no conflicting CLAIM/GATE/FLAG on b366. Newest
  PARENT-* is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r54/ (build366.log,
  pyid366.log, rgram366py/c.log, cmp366.py/.c,
  for366-old/-new.nums, pins366.basen, smoke366.log,
  tables366.log, tabaudit258.py, edges258.py,
  edges366.log, numstat366.txt, added366.txt,
  add/delnorm366.txt, banddiff366.txt, cdiff366.txt,
  cadd366.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
