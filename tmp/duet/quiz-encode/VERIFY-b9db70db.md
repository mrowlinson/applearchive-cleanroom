# VERIFY-b9db70db b379 T10P271 pins 111045..111392 (1614 tiers) PASS

Seat viewer-r52, first-hand, detached tree-b9db70db @b9db70db,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r52.
Base 9b8d6052 (b378, 1608 tiers). Band = 876cc8fd (py merge
w2b@e643e014 partial, +6 tiers, +66 pins) + b9db70db (C port,
1614 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build379/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 0d53f79a / aae 7d8dd3a2 +
  sha256 rgramc c4b6695e / aae d6e27c97 (== GATE all 4;
  aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 7965/7965 covered=7965/7965 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15930/15930 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15930/15930 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15930/15930 sorted).
- PINS 15932 rows (2 hdr + 15930, +66 vs base 15866);
  PASS-names vs PINS-names cmp-equal 15930/15930 py+C;
  base-N vs for-list cmp-equal 7965/7965. For-list delta
  vs base +33/-0: 111045 111046 111047 111048 111055
  111056 111057 111058 111061 111062 111063 111064 111066
  111069 111071 111072 111073 111088 111089 111096 111103
  111104 111105 111120 111121 111136 111137 111231 111232
  111280 111359 111360 111392 (2 sing + A8 split-aware
  offs 0,1,8,9,10,11,14,15 + C6 offs 0,1,3,6,8,9, offs
  2,4,5,7 unsampled + Q10 offs 0,15/16,23,30/31/32,
  47/48,63 + R7 offs 0,94/95,143,222/223,255 == GATE
  decomposition; 7932->7965); 33x2=66 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit379.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 101 PASS
  0 FAIL first run. Inventory exactly the 13 both sides
  (STANDARD ring, no RT; no BM/BC, no M19, no M42/X42,
  no QB/PT/FM). S0/S1 168ch sigs 76270700 NEW 7627-
  family / fcec550e NEW (both NEW strings, sigs NEW vs
  P270 a6930300/a5322507). AM 16x9B / CM 10x11B / M 16x
  8B / QR 4x6B / QT 4x4B / RM 16x6B / RQ 16x7B all C==
  py. AM/CM/M/RM/RQ all 16/16 or 10/10 distinct.
  SPLIT10/6 first-hand: AM b0 34 x10 (rows 0-9) + 20 x6
  (rows 10-15) ORDERED; AC b1-3 const cc5ee5 (AC no
  b0); sigs 34cc5ee5 x10 / 20cc5ee5 x6 derived. 1SIG:
  CC b0-3 const c3ec550e (full sig const); CM 10/10
  diverge. QR r1==r2==r3 LAST3-PAIRED 009d17da74de x3
  (r0 c09ba7a8f99b distinct; 2 distinct); QR sig-led
  (r0 head c09ba7 = row0 sig head, r123 head 009d17 =
  rows1-3 sig head). QT d45a1a47/81d84934/a6d84934/
  cbd84934; r1/r2/r3 share TRUE 3B d84934 (first bytes
  81/a6/cb differ, exactly 3B); r0 last3B 5a1a47
  differs. RQ==M MID+TAILS-SKIP FIRST (M 8B vs RQ 7B:
  bytes 1-2 identical 16/16 + tails RQ[3:7]==M[4:8]
  same-index 16/16 + set-eq, full-row eq 0/16; b0 own
  all 16 with no constant xor/add/sub relation over
  (M0,RQ0) first-hand). Tails SPLIT (RM b80-83 by COL
  / RQ b76-79 by ROW, 16/16 distinct each, 0 overlap
  UNPAIRED). AC/CC/QC/RC 73/71/64/73 py-vs-C
  normalized; _N decls 73/71/64/73 match actual;
  sorted-unique. Missing-sets EXACT: AC-11
  [0,4,5,9,10,11,12,76-79]; CC-13 [4,5,13-19,80-83];
  QC-20 [0,1,2,4,5,12,13,14,16,17,18,19,76-83]; RC-15
  [4,5,20,21,22,28,29,76-83]. Coverage unions exact
  every block (const U tab U {b4,b5} == 84/84/84/88, 0
  overlap). RC b0-3 0e000000; RC b84-87 f761b25f
  ring-wide. M-tails 16/16 ALL NEW vs P270T (overlap 0
  vs P270 RM/RQ tail union); M-full also ALL NEW vs
  P270RQ; QT 4/4 ALL NEW vs P270QT
  (ea14f78d/4e664444/73664444/98664444 re-read); RM ALL
  NEW vs P270RM. Memo INCL PBA 74 / C10 72 / quad 64 /
  T88 73 (A-659 re-read): impl 73/71/64/73 = memo-1 on
  PBA/C10 (standing), identical quad/T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 111045 / S1 111046 / A 111047-062 / C 111063-072 /
  Q 111073-136 / R 111137-392): bounds + paylens (92
  x84 / 256 x88) + lencode both sides (Q b5-step
  emerges from raw lencode) + R counter b4=(67+2off)&
  FF b5=100+(off>=95)+(off>=223) both sides (C 67/100
  = 0x43/0x64) + mtab/qtab/ttab byte positions exact
  (A 9B b0,9-12,76-79 covers split; C 11B b13-19,
  80-83; Q 8/6/4B; R 6/7B) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides. T-mirrors T74163/
  74168/74173/74189/74205/74228 each re-read: hits the
  exact py guard line. Temps _t5718-5735 (base max
  _t5717, no reuse) + _b3468/3470/3472/3473/3474/3476/
  3477 (base max _b3466) + _i3469/3471/3475/3478 (base
  max _i3467, no reuse). C guards
  `if ((n) == (111045))` / `(111046)` + 4 ranges
  exact. Insert exact both sides: after T10P270R close,
  N-out-of-scope follows. Matches A-659/A-335 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop379.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache, 315 miss-warmed; seat rgramc each):
  348/348 CLOSED. Census R256/Q64/A16/C10/S0/S1 exact.
  edges379.py: paylens 92 x84 + 256 x88; lencode 92/92
  (A head 8f/63 tail ad/63, b5set {63}; C head af/63
  tail c1/63, b5set {63} NO carry; Q head c3/63, step
  off30/31 (111103->111104) ff/63->01/64 + off32
  03/64 (111105) + tail 41/64 (111136), Q-form
  b4=(0xc3+2off)&FF b5=0x63+(off>=31) 64/64); ring
  counter 256/256 (head 43/64; 111231 (off94, ff/64)
  -> 111232 (off95, 01/65); 111359 (off222, ff/65) ->
  111360 (off223, 01/66); mid off143 (111280) 61/65;
  tail 111392 (off255) 41/66). S0/S1 8b/63 + 8d/63
  match raw lencode. Tail oracle sha 2dd0e7ad51b16b78
  (== GATE prefix). Edge pins + tail 111392 in
  for-list + 2 PASS lines each py+C. No DISSENT: cut
  bytes verify.
- C diff pure-add: numstat 610/0 (rgramc.c) + 239/0
  (rgram.py) + 1/1 (for-line) + 66/0 (PINS) == GATE; raw
  C 605 content + 5 bare-blank (verified bare, no
  whitespace) / 0 del; raw py 239 content / 0 del.
  Sweep-family norm ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets, keep-empty): C
  del-uniq 0 add-uniq 172 EXACT, py del-uniq 0 add-uniq
  196 EXACT (== GATE).
- Wall on band diff added lines (scope 9b8d6052..
  b9db70db, 916 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression//usr/bin/aa/shim 0
  hits, shebang 0 hits. Files: rgramc.c 610/0,
  rgram.py 239/0 purely additive, test_rgram.sh 1/1,
  PINS +66/+0.
- Tiers: merge-msg +6/+66, code 6 blocks, tier-comments
  `# T10P` 1514->1520 +6, singletons 574->576 +2,
  range-guards 536->540 +4, CLOSED T10P prints
  1514->1520 +6, C guards singleton 569->571 +2 (5-
  count C-vs-py offset pre-existing, unchanged) +
  range 536->540 +4, seal 1608->1614 +6: all agree, no
  slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-659-q783-
  t10p271 verdict CONFIRM 37/37 (12+13+12 sums exact;
  file re-read; exact-value corroboration incl sigs,
  SPLIT10/6, 1SIG, QM8 shared, R6 sig-led last3, QT
  3B-share, ring edges + thresholds re-checked above)
  + A-335 viewer corroboration (all 3 legs CONFIRM,
  consts 74/72/64/73 INCL). No CONFIRM-P271.md file;
  A-659 suffices per rule. Agrees with cport commit msg
  (PYID 7965, RGRAM 15930).
- Quiz: no conflicting CLAIM/GATE/FLAG on b379. Newest
  PARENT-* is QNUM-18 (w2e/w2f Q-block grants, read, no
  gate impact); GATE cites QNUM-16 (grants-only
  staleness, immaterial, standing pattern). PROSE-01:
  all hex/counts above copied from own run output.
- Own near-miss caught pre-filing (script fixed, code
  never impugned): norm379 sed-clone broke the rev
  range (376->379 rewrite hit the range first),
  yielding empty 0/0; range fixed to 9b8d6052..
  b9db70db, C172/py196 EXACT.
- Cross-tier corroboration re-read: P270S0 sig a6930300
  == A-653 predicted next PB0 (A-653 "Next P270 PB0
  @110697 a6930300 NEW" re-read); P270S1 sig a5322507
  == P269 C10 sig carried forward (b378 audit).

Verdict: PASS. No RED. GATE CORRECT on code, 1 immaterial
prose staleness (QNUM-16 vs -18).
