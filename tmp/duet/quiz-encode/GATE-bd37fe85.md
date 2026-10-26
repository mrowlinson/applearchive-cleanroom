# GATE bd37fe85 b364 T10P256 pins 105825..106172 (1524 tiers) PASS-functional

Seat sweep2-r54, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r54/w364 @bd37fe85.
Band = bbb91641 (py merge w2b@f97e2a9b partial, +6 tiers, +62 pins)
+ bd37fe85 (C port). Base 26effd6a (b363 tip, 1518 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build364/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4a5bffb0 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52/r53/r54 builds;
  band touches no aae sources per numstat).
- RGRAMC-PYID 7494/7494 covered=7494/7494 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14988/14988 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 14988/14988 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (cmp 0 diff, 14988/14988).
- PINS-RGRAM cells set-eq 7494/7494 (xor 0, PINS base-N
  set vs for-list; PASS-names vs PINS-names xor 0);
  PINS 14990 rows (2 hdr + 14988 = PASS lines, +62 vs base
  14928). For-list union +31 (105825 105826 105827 105828
  105833 105837 105841 105842 105843 105846 105847 105849
  105850 105852 105853 105855 105856 105868 105869 105884
  105885 105900 105901 105916 105917 105983 105984 106045
  106111 106112 106172), 0 removed, range 105825..106172
  exact. Each for-N yields 2 PASS lines (g-zN-closed +
  g-zN); 31x2 = 62 = 14988-14926.
  The 31 = S0/S1 (2) + A head/mids/tail (6) + C
  head/mids/tail (6) + Q head/carry-pair/mid-pairs/tail
  (10) + ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P256 C-vs-py, script-compared, TABAUDIT-GREEN
  77 PASS 0 FAIL (tabaudit256.py rc=0): S0/S1 168ch
  EXACT sigs 641a0300 NEW / e58c3506 NEW (vs P255
  e4180300 / 0dc83406, code-verified), AM 16/16 10B
  distinct, CM 10/10 14B distinct, M 16/16 7B, QR 4/4
  10B, QT 4/4 4B, RM 16/16 7B distinct, RQ 16/16 7B
  distinct, AC 72, CC 68, QC 61, RC 72; C _N decls
  72/68/61/72 match actual; byte-coverage unions exact
  every block (84/84/84/88, 0 overlap, b4/b5 in no
  const set).
  CM sig-map exact order: 3506 x4 @105843-46 +
  1503 x3 @105847-49 + 3506 x3 @105850-52 (CC
  b0,b1 e5,8c const + CM b2,b3 in tab; 2 distinct sigs,
  10/10 diverge NO pair).
  QR r0==r1 PAIRED 7c1a33e6d67f356a6afc x2, r2
  3c8db35b04fad4c1fe7f + r3 3c8db35b08fad4c1fe7f
  1B-off 04-vs-08; pair-led a0802f7c (r01) /
  a0802f3c (r23) via QC b0-2 + QR b3 EXACT.
  QT values 10299170/36299170/6c301f67/87aa49cb
  (4/4 distinct; r0/r1 share TRUE 3B 299170,
  matching R-pair).
  AC b0-3 a0802f7c NEW vs P255PBA 79824c63
  (code-verified).
  RC b0-3 06000000 ==P253T (code-verified vs P253RC
  b0-3); RC b84-87 edf84115 ring-wide.
  RM/RQ UNPAIRED, tails SPLIT (RM b80-83 by COL 16/16,
  RQ b76-79 by ROW 16/16; TR7 b42 in T-R).
  Same-tier RQ rows = M rows 16/16 full-row (byte
  positions differ: QM7 b36-38 vs TR7 b40-42 -
  staging, NOT a finding per precedent).
  Code-consts vs A-610 INCL (PBA 73 / C10 69 / quad 61 /
  T88 72): impl 72/68 = memo-1 on PBA/C10 (standing
  incl/excl bookkeeping), 61/72 identical on quad/T88.
  M-tails 16/16 ALL NEW vs P255T (zero overlap vs BOTH
  P255RM-tail and P255RQ-tail sets; P255 RM 16x14ch /
  RQ 16x18ch order re-read first-hand).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=105825 (PB0 sig 641a0300 NEW, lenB 84), S1
  n=105826 (fat PB1 sig e58c3506 NEW, lenB 84),
  A 105827-105842 PBA16 (sig a0802f7c NEW via AC
  b0-b3, AM 16/16 distinct 10B widest PBA M yet, mtab
  b14,15,21-23,31,76-79, b5 const 3a raw lencode),
  C 105843-105852 C10-2SIG sandwich (sig map exact order
  above, CM 10/10 distinct 14B diverge 10/10, mtab
  b2,3,22,23,30-35,80-83 sig-b2,b3-in-tab, b5 const
  3a),
  Q 105853-105916 QUADms pair-led 1B-off
  (a0802f7c-r01/a0802f3c-r23, QM7 b36-38,76-79 M
  16/16 7B + R10 b3,15,22,23,30-35 pair above + QT
  tails above, b5-carry 3a->3b @105855->105856 EARLY
  raw lencode),
  R 105917-106172 T88-ring STANDARD (sig 06000000
  ==P252/253T, TM7 b39,46,47,80-83 by COL RM 16/16,
  TR7 b40-42,76-79 by ROW RQ 16/16 UNPAIRED,
  tails SPLIT b80-83 col / b76-79 row, b84-87 const
  edf84115 ring-wide, b4=(0x7b+2off)&FF,
  b5=0x3b+(off>=67)+(off>=195)). C blocks carry
  T70351/70356/70361/70377/70394/70418 py-line mirrors
  (each re-read: hits the exact py guard line), bounds
  + byte positions exact (A 10B, C 14B, Q 7/10/4B, R
  7/7B), counter b4=(0x7b+2off)&FF + (off>=67)+
  (off>=195), temps _t5428-5445 (base max _t5427, no
  reuse) + _b3302-3311/_i3303-3312 (base max
  _b3300/_i3301, no reuse), all 6 verified.
  Insert position exact both sides: after T10P255R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-610/A-367 geometry (PB0/PB1 NEW, PBA16 VPOS
  11 b5 const 3a widest-10, C10-2SIG VPOS 15 4/3/3 b5
  const 3a 10/10 diverge NO pair, QUAD VPOS 23
  pair-led + R10 pair + QT 3B-share + M-tails NEW,
  T88 VPOS 16 STANDARD SPLIT + b84-87 edf84115,
  lencode 348/348 whole-tier, Q-carry 105855->105856
  EARLY, ring edges 105983->105984 + 106111->106112,
  NO D dips) incl exact values (CM 4/3/3 map, QR pair
  + 1B-off, QT tails + 3B-share, pair-led pair, ring
  TM7/TR7 16/16 UNPAIRED, tails SPLIT, consts stand).
- Edges via counter formula first-hand: Q-carry 105855
  (ff/3a) -> 105856 (01/3b); ring 105983 (off66, ff/3b)
  -> 105984 (off67, 01/3c); 106111 (off194, ff/3c) ->
  106112 (off195, 01/3d); all six pins + tail 106172 in
  for-list + 2 PASS lines each py+C. A b5set {3a}, C
  b5set {3a}, Q b5set {3a,3b} (single EARLY carry). A
  head c7/3a tail e5/3a, C head e7/3a tail f9/3a, Q
  head fb/3a tail 79/3b, R head 7b/3b tail 79/3d. Ring
  counter == raw lencode 256/256, 0 mismatch. Odd-lencode
  348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del
  (rgramc.c) + 239/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 605 content + 5 blank-only
  `+` lines (verified bare) / 0 del; fine-norm
  (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD tools,
  empty-excluding) del-subset-add 0 missing (del-uniq
  0, add-uniq 398).
- Wall on band diff added lines (scope 26effd6a..
  bd37fe85, 912 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0 hits.
  Files touched: rgramc.c 610/0, rgram.py 239/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 544->546 +2 / ranges 476->480 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep), CLOSED T10P prints 1424->1430 +6, C singletons
  539->541 +2 (C-vs-py 5-offset pre-existing, unchanged),
  C ranges 476->480 +4, seal 1518->1524 +6: all agree,
  no slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-610-q768-
  t10p256 verdict CONFIRM (shape 12/12 + quad/ring 11/11
  + counters 12/12 as sectioned; verdict line reads
  35/35 as-filed; file present, counts verified;
  exact-value corroboration incl CM 4/3/3 map, QR pair
  + 1B-off, QT tails + 3B-share, pair-led pair,
  M-tails NEW, ring edges + consts re-checked above) +
  A-367 viewer corroboration (all 3 legs CONFIRM).
  No CONFIRM-P256.md file; A-610 suffices per rule.
  Agrees with cport commit msg (PYID 7494, RGRAM 14988).
- Quiz: no conflicting CLAIM/GATE/FLAG on b364. Newest
  PARENT-* is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r54/ (build364.log,
  pyid364.log, rgram364py/c.log, cmp364.py/.c,
  for364-old/-new.nums, pins364.basen, smoke364.log,
  tables364.log, tabaudit256.py, edges256.py,
  edges364.log, numstat364.txt, added364.txt,
  add/delnorm364.txt, banddiff364.txt, cdiff364.txt,
  cadd364.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
