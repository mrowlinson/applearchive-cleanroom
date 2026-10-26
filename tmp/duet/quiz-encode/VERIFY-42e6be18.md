# VERIFY-42e6be18 b376 T10P268 pins 110001..110348 (1596 tiers) PASS

Seat viewer-r52, first-hand, detached tree-42e6be18 @42e6be18,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r52.
Base e59e5d25 (b375, 1590 tiers). Band = 8c3709db (py merge
w2b@6570612c partial, +6 tiers, +64 pins) + 42e6be18 (C port,
1596 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build376/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 7c94d51b / aae d6e27c97
  (== GATE both; aae pinned, band touches no aae sources per
  numstat) + sha1 rgramc 18b99877 / aae 7d8dd3a2.
- RGRAMC-PYID 7867/7867 covered=7867/7867 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15734/15734 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15734/15734 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15734/15734 sorted).
- PINS 15736 rows (2 hdr + 15734, +64 vs base 15672);
  PASS-names vs PINS-names cmp-equal 15734/15734 py+C;
  base-N vs for-list cmp-equal 7867/7867. For-list delta vs
  base +32/-0: 110001 110002 110003 110004 110008 110013
  110017 110018 110019 110020 110022 110025 110027 110028
  110029 110033 110034 110044 110045 110060 110061 110076
  110079 110080 110092 110093 110207 110208 110236 110335
  110336 110348 (2 sing + A6 offs 0,1,5,10,14,15 + C6 offs
  0,1,3,6,8,9 + Q11 offs 0,4,5,15,16,31,32,47,50,51,63 +
  R7 offs 0,114,115,143,242,243,255 == GATE decomposition;
  7867->7867); 32x2=64 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit376.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 96 PASS 0
  FAIL first run. Inventory exactly the 13 both sides
  (no BM/BC, no M19, no M42/X42, no RT, no QB/PT/FM).
  S0/S1 168ch sigs a4740300 NEW / 1d188406 NEW (both NEW
  strings, sigs NEW vs P267 a0740300/1d18e406). AM 16x8B /
  CM 10x11B / M 16x7B / QR 4x4B / QT 4x4B / RM 16x8B / RQ
  16x7B all C==py. AM/CM/M/RM/RQ all 16/16 or 10/10
  distinct. PBA sig db814168 via AC b0-b3 (P267 PBA
  c0822772 re-read, NEW); b0 const db; AC no b5. C10-1SIG
  e4492707 x10 via CC b0-b3; CM 10/10 diverge; CC no b5.
  QUAD2s split-b0 staged (QC no b0; dispatch 89 iff m<5);
  QC b1-3 const 9c7472; b49 const 5a; QC no b5. QR
  r1==r2==r3 LAST3-PAIRED c5dec599 x3 (r0 6fcb8377
  distinct; 2 distinct). QT 452ed3b4/b7e31656/dce31656/
  01e41656; r1/r2 share TRUE 3B e31656 (first bytes b7/dc
  differ); r3 shares 2B-only 1656 (3B e416 vs e316
  differs, both lengths checked); r0 452ed3b4 distinct.
  RC b0-3 06000000 ==P267T (P267RC b0-b3 re-read
  06000000, sig-repeat); RC b84-87 e365abcd ring-wide NEW
  (P267 had de93eef2, re-read). RQ==M tails same-index
  16/16 + set-eq (M 7B vs RQ 7B; full-row eq 0/16,
  staging). Tails SPLIT (RM b80-83 by COL / RQ b76-79 by
  ROW, 16/16 distinct each, 0 overlap UNPAIRED; full-row
  sets disjoint too). AC/CC/QC/RC 74/71/66/71 py-vs-C
  normalized; _N decls 74/71/66/71 match actual;
  sorted-unique. Missing-sets EXACT: AC-10
  [4,5,6,7,8,9,76-79]; CC-13 [4,5,6,7,8,48-51,80-83];
  QC-18 [0,4,5,6,7,9,10,11,48,50,76-83]; RC-17
  [4,5,8,9,10,13,14,15,19,76-83]. Coverage unions exact
  every block (const U tab U {b4,b5} == 84/84/84/88, 0
  overlap). M-tails 16/16 ALL NEW vs P267T (overlap 0 vs
  P267 RM/RQ tail union); M-full also ALL NEW vs P267RQ;
  RM ALL NEW vs P267RM. Memo INCL PBA 75 / C10 72 / quad
  66 / T88 71 (A-652 re-read): impl 74/71/66/71 = memo-1
  on PBA/C10 (standing), identical quad/T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 110001 / S1 110002 / A 110003-018 / C 110019-028 /
  Q 110029-092 / R 110093-348): bounds + paylens (92 x84
  / 256 x88) + lencode both sides (Q b5-step emerges from
  raw lencode) + R counter b4=(27+2off)&FF
  b5=92+(off>=115)+(off>=243) both sides (C 27/92 =
  0x1b/0x5c) + mtab/qtab/ttab byte positions exact (A
  8B b6-9,76-79; C 11B b6-8,48-51,80-83; Q 7/4/4B;
  R 8/7B) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + Q b0split pay[0]==(0x89 iff m<5 else 0x8a) both
  sides (C (m<5)?137:138). T-mirrors T73405/73410/73415/
  73430/73446/73471 each re-read: hits the exact py guard
  line. Temps _t5660-5677 (base max _t5659, no reuse) +
  _b3433/3435/3437/3438/3439/3441/3442 (base max _b3431)
  + _i3434/3436/3440/3443 (base max _i3432, no reuse). C
  guards `if ((n) == (110001))` / `(110002)` + 4 ranges
  exact. Insert exact both sides: after T10P267R close,
  N-out-of-scope follows. Matches A-652/A-332 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop376.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache, 316 miss-warmed; seat rgramc each):
  348/348 CLOSED. Census R256/Q64/A16/C10/S0/S1 exact.
  edges376.py: paylens 92 x84 + 256 x88; lencode 92/92
  (A head 67/5b tail 85/5b b5set {5b} NO carry; C head
  87/5b tail 99/5b b5set {5b} NO carry; Q head 9b/5b,
  step 110079 (o50, ff/5b) -> 110080 (o51, 01/5c)
  mid-row3, tail 19/5c (110092)); ring counter 256/256
  (head 1b/5c; 110207 (off114, ff/5c) -> 110208 (off115,
  01/5d); 110335 (off242, ff/5d) -> 110336 (off243,
  01/5e); mid off143 (110236) 39/5d; tail 110348
  (off255) 19/5e). S0/S1 63/5b + 65/5b match raw
  lencode. Edge pins + tail 110348 in for-list + 2 PASS
  lines each py+C. No DISSENT: cut bytes verify.
- C diff pure-add: numstat 612/0 (rgramc.c) + 239/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE; raw
  C 607 content + 5 bare-blank (verified bare, no
  whitespace) / 0 del; raw py 239 content / 0 del.
  Fine-norm temp-norm-only (_tN/_iN/_bN, empty-
  excluding): C del-uniq 0 add-uniq 431 EXACT (== GATE),
  py del-uniq 0 add-uniq 213. Sweep2 family.
- Wall on band diff added lines (scope e59e5d25..
  42e6be18, 916 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 612/0, rgram.py 239/0 purely
  additive, test_rgram.sh 1/1, PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, tier-comments
  `# T10P` 1496->1502 +6, singletons 568->570 +2,
  range-guards 524->528 +4, CLOSED T10P prints
  1496->1502 +6, C guards singleton 563->565 +2 +
  range 524->528 +4, seal 1590->1596 +6: all agree, no
  slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-652-q780-
  t10p268 verdict CONFIRM 42/42 (13+15+14 sums exact;
  file re-read; exact-value corroboration incl sigs,
  split-b0 64/64, QM7 shared, R4 last3-pair, QT 3B/2B
  shares, M-tails NEW, ring edges + consts re-checked
  above) + A-332 viewer corroboration (all 3 legs
  CONFIRM, consts 75/72/66/71 INCL). No CONFIRM-P268.md
  file; A-652 suffices per rule. Agrees with cport commit
  msg (PYID 7867, RGRAM 15734).
- Quiz: no conflicting CLAIM/GATE/FLAG on b376. Newest
  PARENT-* is QNUM-18 (w2e/w2f Q-block grants, read, no
  gate impact); GATE cites QNUM-13 (grants-only staleness,
  immaterial, standing pattern). PROSE-01: all hex/
  counts above copied from own run output.

Verdict: PASS. No RED. GATE CORRECT on code, 1 immaterial
prose staleness (QNUM-13 vs -18).
