# VERIFY-a961bc67 b366 T10P258 pins 106521..106868 (1536 tiers) PASS

Seat viewer-r49, first-hand, detached tree-a961bc67 @a961bc67,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r49.
Base 926c1bd9 (b365, 1530 tiers). Band = beeebf03 (py) + a961bc67 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build366/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings (empty stderr). sha256 rgramc 1ce06e6d /
  aae d6e27c97 (== GATE; aae pinned, band touches no aae
  sources per numstat).
- RGRAMC-PYID 7556/7556 covered=7556/7556 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15112/15112 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15112/15112 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15112/15112).
- PINS 15114 rows (2 hdr + 15112, +62 vs base); base-N
  set-eq 7556/7556 (cmp 0); PASS-names vs PINS-names
  cmp-equal 15112/15112. For-list delta vs base +31/-0,
  added list verbatim == GATE (106521 106522 106523 106524
  106529 106533 106537 106538 106539 106542 106543 106544
  106545 106546 106547 106548 106549 106564 106565 106580
  106581 106596 106597 106612 106613 106623 106624 106741
  106751 106752 106868); 2 sing + A6 + C8 + Q8 + R7 ==
  GATE; 31x2=62 rows; range 106521..106868 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit366.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 110 PASS 0
  FAIL. C-vs-py EXACT all 13 (S0/S1 168ch sigs 20370300
  NEW / f8416e06 NEW vs P257 601a0300 / e58c3506
  re-read; AM 16x8B distinct; CM 10x15B distinct; M 16x6B
  distinct; QR 4x7B 4/4 distinct UNPAIRED
  d08f8179922dee/a5d2616e929df4/2ba0517412c0dc/
  9a8aa177927ed7, b0 all distinct; QT 4x4B distinct
  f2bc5daa/49f3db15/dab7ba8e/1469107b, all-pairs
  longest-common-suffix 0, last bytes + last-3B all
  differ; RM 16x9B distinct widest-9; RQ 16x6B distinct;
  AC/CC/QC/RC 74/67/65/71 pairs py-hex-vs-C-dec
  normalized). _N decls 74/67/65/71 match actual.
  Inventory exactly the 13 (no QB/BM/BC/M42/X42/PT/FM
  either side). Missing-sets EXACT: AC-10
  [4,5,12-14,19,76-79]; CC-17 [0-5,11,18-23,80-83] (CC
  has no b0-3, sig bytes in tab); QC-19
  [4,5,13,14,18-22,24,25,76-83]; RC-17
  [4,5,18,19,27-29,34,35,76-83]. CM 6-sig map exact
  order 85c86106x4@rows0-3 + 2dbe3b03/8d963a03/5d533103/
  7d053403@rows4-7 + 851a3e03x2@rows8-9 (6 distinct,
  10/10 diverge NO pair; rows = N 106539-42/106543-46/
  106547-48). QC b0-3 e0921f3a single-sig. AC b0-3
  40811f74 NEW vs P257AC b0-3 a0802f7c re-read. RC b0-3
  03000000 == P255RC b0-3 py+C re-read; RC b84-87
  0b3bb263. M rows == RQ rows 16/16 full-row (positions
  differ QM6 b24,25 vs TR6 b28,29, staging). RM[c]/RQ[r]
  UNPAIRED both sides, tails SPLIT col/row 16/16
  distinct each. M-tails 16 distinct, zero overlap vs
  BOTH P257RM-tail and P257RQ-tail sets (P257 RM/RQ
  16x14ch re-read). Coverage unions exact (A 8+74+2=84,
  C 15+67+2=84, Q 6+7+4+65+2=84, R 9+6+71+2=88;
  disjoint, b4/b5 in no const set; C _b positions == py
  all 7 legs; C _b var order 3324/3326/3328/3329/3330/
  3332/3333). Memo INCL PBA 75 / C10 68 / quad 66 / T88
  71 (A-615/A-322 re-read): impl 74/67/65 = memo-1 on
  PBA/C10/quad (standing), 71 identical.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 106521 / S1 106522 / A 106523-538 / C 106539-548 /
  Q 106549-612 / R 106613-868): bounds + paylens (84 x92
  / 88 x256) + lencode/counter formulas exact incl R
  0xeb/0x40/11/139 both sides (C 235/64/11/139).
  T-mirrors T70829/70834/70839/70854/70871/70894 each
  re-read: hits the exact py guard line (106521/106522/
  106523/106539/106549/106613). Temps _t5464-5481 (base
  max _t5463, no reuse) + _b3324/3326/3328/3329/3330/
  3332/3333 + _i3325/3327/3331/3334 (base max _b3322/
  _i3323, no reuse). Insert exact both sides: after
  T10P257R close, N-out-of-scope follows. Matches
  A-615/A-322 geometry (values re-checked in audit
  above; NO D dips).
- Edges own-loop ownloop366.py over ALL 348 tier Ns
  (fresh oracle bytes via ct-cache miss path,
  tool-identical -encode -a lzraven; 31 cache hits +
  317 fresh encodes; seat rgramc each): 348/348 CLOSED.
  Q b5 const 40 NO carry (head 6b/40 @106549, tail
  e9/40 @106612); ring 106623 (off10 ff/40) -> 106624
  (off11 01/41); 106751 (off138 ff/41) -> 106752
  (off139 01/42); edge pins + tail 106868 in for-list +
  PASS py+C. A b5set {40}, C {40}, Q {40}. Heads/tails:
  A 37/40-55/40, C 57/40-69/40, R eb/40-e9/42.
  pay[4:6]==LE16((n<<1)|1) 348/348 whole-tier incl 88B
  cells (ring 256/256). Paylens 84 x92 + 88 x256.
- C diff purely additive: numstat 610/0 (rgramc.c) +
  239/0 (rgram.py) + 1/1 (for-line) + 62/0 (PINS) ==
  GATE; raw C 605 content + 5 blank-only / 0 del.
  Fine-norm (rgramc.c scope, letter-preserving
  _tN/_iN/_bN temp-norm, no lead/semi strip,
  empty-excluding, BSD sort -u): del-uniq 0, add-uniq
  403, del-subset-add 0 missing; norm file
  byte-identical (cmp 0) to sweep2-r54's filed
  addnorm366.txt. Same temp-norm-only family as b364
  (differs from pinned digits->N TNP recipe).
- Wall on band diff added lines (912): vendor/disasm 0,
  depload 0, libcompression/compression_tool/aa/
  nominated/shim/ct-cache 0, shebang 0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 548->550 +2 / ranges 484->488 +4 = +6,
  CLOSED T10P prints 1436->1442 +6, C singletons
  543->545 +2 (C-vs-py 5-offset pre-existing, unchanged),
  C ranges 484->488 +4, seal 1530->1536 +6: all agree,
  no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-615-q770
  verdict CONFIRM (shape 12/12 + quad/ring 11/11 +
  counters 12/12; verdict line 35/35 as-filed, sums
  exact, no quirk; exact-value corroboration incl CM
  6-sig map, QR 4/4 UNPAIRED, QT tails no-shared-suffix,
  single-sig, M-tails NEW, ring edges + consts
  re-checked above) + A-322 (all 3 legs CONFIRM,
  348-cell bed + P257T ref + P259 window). No
  CONFIRM-P258.md file; A-615 suffices per rule. Agrees
  with cport commit msg (PYID 7556, RGRAM 15112).
- Quiz: no conflicting CLAIM/GATE/FLAG on b366. Newest
  PARENT-* is QNUM-14 (grants only, read, no gate
  impact); GATE cites QNUM-13: 1 immaterial staleness.
  PROSE-01: every value above copied from own run
  output, GATE re-read before filing.
- Logs: NVME ws tmp/encode-viewer/r49/ (build366.log,
  pyid366.log, rgram366py/c.log, cmp366.py/.c,
  for366(-old).nums, pins366.basen/.names, pass366.names,
  smoke366.log, tables366.log, tabaudit366.py,
  ownloop366.log/.py, banddiff366-py/-c.txt,
  base366-py/-c.txt, addnorm366.txt).

Verdict: PASS. No RED. Code CORRECT; GATE CORRECT on code
(1 immaterial QNUM staleness). Ready for parent PV/merge.
