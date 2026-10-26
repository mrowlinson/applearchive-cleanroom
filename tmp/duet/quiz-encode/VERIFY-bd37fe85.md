# VERIFY-bd37fe85 b364 T10P256 pins 105825..106172 (1524 tiers) PASS

Seat viewer-r49, first-hand, detached tree-bd37fe85 @bd37fe85,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r49.
Base 26effd6a (b363, 1518 tiers). Band = bbb91641 (py) + bd37fe85 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build364/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings (empty stderr). sha256 rgramc 4a5bffb0 /
  aae d6e27c97 (== GATE; aae pinned value, band touches no
  aae sources per numstat).
- RGRAMC-PYID 7494/7494 covered=7494/7494 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 14988/14988 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 14988/14988 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 14988/14988).
- PINS 14990 rows (2 hdr + 14988); base-N set-eq 7494/7494
  (for-list vs PINS, cmp 0); PASS-names vs PINS-names
  cmp-equal 14988/14988. For-list delta vs base +31/-0,
  added list verbatim == GATE (105825 105826 105827 105828
  105833 105837 105841 105842 105843 105846 105847 105849
  105850 105852 105853 105855 105856 105868 105869 105884
  105885 105900 105901 105916 105917 105983 105984 106045
  106111 106112 106172); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit364.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 102 PASS 0
  FAIL. C-vs-py EXACT all 13 (S0/S1 168ch sigs 641a0300
  NEW / e58c3506 NEW vs P255 e4180300 / 0dc83406
  re-read; AM 16x10B distinct; CM 10x14B distinct; M 16x7B
  distinct; QR 4x10B r0==r1 paired + r2/r3 1B-off idx4
  04-vs-08; QT 4x4B distinct r0/r1 TRUE 3B-share 299170;
  RM/RQ 16x7B distinct; AC/CC/QC/RC 72/68/61/72 pairs).
  _N decls 72/68/61/72 match actual. CM sig-map exact
  order 3506x4@105843-46 + 1503x3@105847-49 +
  3506x3@105850-52 (CC b0,b1 e5,8c const, sig b2,b3 in
  tab, 2 sigs, 10/10 diverge NO pair). Pair-led
  a0802f7c-r01/a0802f3c-r23 via QC b0-2 + QR b0
  (7c/7c/3c/3c). AC b0-3 a0802f7c NEW vs P255PBA 79824c63
  re-read. RC b0-3 06000000 == P253RC b0-3 py+C re-read;
  RC b84-87 edf84115. RM[c]/RQ[r] UNPAIRED both sides
  (c=off&15, r=off>>4); tails SPLIT (RM b80-83 col /
  RQ b76-79 row). M rows == RQ rows 16/16 full-row
  (positions differ QM7 b36-38 vs TR7 b40-42, staging).
  M-tails 16 distinct, zero overlap vs BOTH P255RM-tail
  and P255RQ-tail sets (P255 widths RM14ch/RQ18ch
  re-read). Coverage unions exact every block
  (A 10+72+2=84, C 14+68+2=84, Q 7+10+4+61+2=84, R
  7+7+72+2=88; tab/const disjoint, b4/b5 in no const
  set; C _b positions == py all 7 legs; C _b var order
  3302/3304/3306/3307/3308/3310/3311). Memo INCL PBA
  73 / C10 69 / quad 61 / T88 72 (A-610 re-read):
  impl 72/68 = memo-1 on PBA/C10 (standing), 61/72
  identical.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 105825 / S1 105826 / A 105827-42 / C 105843-52 /
  Q 105853-916 / R 105917-106172): bounds + paylens
  (84 x92 / 88 x256) + lencode/counter formulas exact
  incl R 0x7b/0x3b/67/195 both sides (C 123/59/67/195).
  T-mirrors T70351/70356/70361/70377/70394/70418 each
  re-read: hits the exact py guard line (105825/105826/
  105827/105843/105853/105917). Temps _t5428-5445 (base
  max _t5427, no reuse) + _b3302/3304/3306/3307/3308/
  3310/3311 + _i3303/3305/3309/3312 (base max _b3300/
  _i3301, no reuse). Insert exact both sides: after
  T10P255R close, N-out-of-scope follows T10P256R.
  Matches A-610/A-367 geometry (values re-checked in
  audit above; NO D dips).
- Edges own-loop ownloop364.py over ALL 348 tier Ns
  (fresh oracle bytes via ct-cache miss path,
  tool-identical -encode -a lzraven; 31 cache hits +
  317 fresh encodes; seat rgramc each): 348/348 CLOSED.
  Q-carry 105855 (ff/3a) -> 105856 (01/3b) EARLY; ring
  105983 (off66 ff/3b) -> 105984 (off67 01/3c); 106111
  (off194 ff/3c) -> 106112 (off195 01/3d). A b5set {3a},
  C {3a}, Q {3a,3b}. Heads/tails: A c7/3a-e5/3a, C
  e7/3a-f9/3a, Q fb/3a-79/3b, R 7b/3b-79/3d.
  pay[4:6]==LE16((n<<1)|1) 348/348 whole-tier incl
  88B cells (ring 256/256). Paylens 84 x92 + 88 x256.
- C diff purely additive: numstat 610/0 (rgramc.c) +
  239/0 (rgram.py) + 1/1 (for-line) + 62/0 (PINS) ==
  GATE; raw C grep 605 content + 5 blank-only / 0 del.
  Fine-norm (rgramc.c scope, letter-preserving
  _tN/_iN/_bN temp-norm, no lead/semi strip,
  empty-excluding, BSD sort -u): del-uniq 0, add-uniq
  398, del-subset-add 0 missing; BOTH norm files
  byte-identical (cmp 0) to sweep2-r54's filed
  add/delnorm364.txt. NOTE: this recipe differs from
  the pinned digits->N TNP recipe (which yields 152
  on this band; recipe impl validated at 170 on b360)
  - new fine-norm family instance, flagged below.
- Wall on band diff added lines (912): vendor/disasm 0,
  depload 0, libcompression/compression_tool/aa/
  nominated/shim/ct-cache 0, shebang 0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 544->546 +2 / ranges 476->480 +4 (GATE
  method reproduced exact; strict-indent count
  534->536/454->458 same deltas), CLOSED T10P prints
  1424->1430 +6, C singletons 539->541 +2 (C-vs-py
  5-offset pre-existing, unchanged), C ranges 476->480
  +4, seal 1518->1524 +6: all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-610-q768
  verdict CONFIRM (shape 12/12 + quad/ring 11/11 +
  counters 12/12; verdict line 35/35 as-filed, sums
  exact, no quirk; exact-value corroboration incl CM
  4/3/3 map, QR pair + 1B-off, QT tails + 3B-share,
  pair-led pair, M-tails NEW, ring edges + consts
  re-checked above) + A-367 (all 3 legs CONFIRM,
  348-cell bed + P255T/P257 windows). No CONFIRM-P256.md
  file; A-610 suffices per rule. Agrees with cport
  commit msg (PYID 7494, RGRAM 14988).
- Quiz: no conflicting CLAIM/GATE/FLAG on b364. Newest
  PARENT-* is QNUM-14 (grants only, read, no gate
  impact); GATE cites QNUM-13: 1 immaterial staleness.
  PROSE-01: every value above copied from own run
  output, GATE re-read before filing.
- Logs: NVME ws tmp/encode-viewer/r49/ (build364.log,
  pyid364.log, rgram364py/c.log, cmp364.py/.c,
  for364(-old).nums, pins364.basen/.names, pass364.names,
  smoke364.log, tables364.log, tabaudit364.py,
  ownloop364.log/.py, banddiff364-py/-c.txt,
  base364-py/-c.txt, add/delnorm364.txt).

Verdict: PASS. No RED. Code CORRECT; GATE CORRECT on code
(1 immaterial QNUM staleness). Ready for parent PV/merge.
