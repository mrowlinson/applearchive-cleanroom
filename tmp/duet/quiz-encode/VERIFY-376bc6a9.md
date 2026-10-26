# VERIFY-376bc6a9 b377 T10P269 pins 110349..110696 (1602 tiers) PASS

Seat viewer-r52, first-hand, detached tree-376bc6a9 @376bc6a9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r52.
Base 42e6be18 (b376, 1596 tiers). Band = 5ccbc0a1 (py merge
w2b@155cdd49 partial, +6 tiers, +64 pins) + 376bc6a9 (C port,
1602 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build377/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc c05ac326 / aae 7d8dd3a2 +
  sha256 rgramc 26edbfc6 / aae d6e27c97 (== GATE all 4;
  aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 7899/7899 covered=7899/7899 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15798/15798 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15798/15798 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15798/15798 sorted).
- PINS 15800 rows (2 hdr + 15798, +64 vs base 15736);
  PASS-names vs PINS-names cmp-equal 15798/15798 py+C;
  base-N vs for-list cmp-equal 7899/7899. For-list delta
  vs base +32/-0: 110349 110350 110351 110352 110356
  110361 110365 110366 110367 110368 110370 110373 110375
  110376 110377 110384 110391 110392 110393 110408 110409
  110424 110425 110440 110441 110463 110464 110584 110591
  110592 110665 110696 (2 sing + A6 offs 0,1,5,10,14,15 +
  C6 offs 0,1,3,6,8,9, offs 2,4,5,7 unsampled + Q10 offs
  0,7,14/15/16,31/32,47/48,63 + R8 offs 0,22/23,143,
  150/151,224,255 == GATE decomposition; 7867->7899);
  32x2=64 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit377.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 96 PASS 0
  FAIL first run. Inventory exactly the 14 both sides
  (RT present; no BM/BC, no M19, no M42/X42, no
  QB/PT/FM). S0/S1 168ch sigs a4930300 NEW / 3d502907
  NEW (both NEW strings, sigs NEW vs P268 a4740300/
  1d188406). AM 16x6B / CM 10x12B / M 16x10B / QR 4x7B /
  QT 4x4B / RM 16x7B / RQ 16x6B / RT 16x4B all C==py.
  AM/CM/M/RM/RT all 16/16 or 10/10 distinct. 1SIG: CC
  b0-3 const a5322507 (full sig const); CM 10/10
  diverge. QR r1==r2==r3 LAST3-PAIRED 23bc65c2d5c02d x3
  (r0 957c910d55dd0a distinct; 2 distinct). QT
  86296322/7d559c98/a2559c98/c7559c98; r1/r2/r3 share
  TRUE 3B 559c98 (first bytes 7d/a2/c7 differ, exactly
  3B); r0 last3B 296322 differs. RQ==M HEAD-REMAP FIRST
  (M 10B vs RQ 6B: bytes 1-5 identical 16/16, full-eq
  0/16, b0 remap 29->36 / a9->b6 all 16). RT==M-tails
  FIRST (row-led tail tab echoes quad col tails:
  same-index 16/16 + set-eq, RTuniq 16 Muniq 16; staged
  as independent table in code). RM UNPAIRED 16/16 by
  COL; RQ 15/16 (r14==r15 366722f9e715; tails
  disambiguate 607a9f8b vs 91f773c3). AC/CC/QC/RC
  76/70/61/69 py-vs-C normalized; _N decls 76/70/61/69
  match actual; sorted-unique. Missing-sets EXACT: AC-8
  [4,5,24,25,76-79]; CC-14 [4,5,24-31,80-83]; QC-23
  [4,5,14,15,21-31,76-83]; RC-19
  [4,5,18,19,25,26,27,35,40,41,42,76-83]. Coverage
  unions exact every block (const U tab U {b4,b5} ==
  84/84/84/88, 0 overlap). RC b0-3 07000000; RC b84-87
  1b2a6322 ring-wide. M-tails 16/16 ALL NEW vs P268T
  (overlap 0 vs P268 RM/RQ tail union); M-full also ALL
  NEW vs P268RQ; QT 4/4 NEW vs P268QT
  (452ed3b4/b7e31656/dce31656/01e41656 re-read); RM ALL
  NEW vs P268RM; RT ALL NEW vs P268T (overlap 0). Memo
  INCL PBA 77 / C10 71 / quad 62 / T88 69 (A-653
  re-read): impl 76/70/61/69 = memo-1 on PBA/C10/quad
  (standing), identical T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 110349 / S1 110350 / A 110351-366 / C 110367-376 /
  Q 110377-440 / R 110441-696): bounds + paylens (92 x84
  / 256 x88) + lencode both sides (Q b5 const, no step)
  + R counter b4=(211+2off)&FF b5=94+(off>=23)+
  (off>=151) both sides (C 211/94 = 0xd3/0x5e) +
  mtab/qtab/ttab byte positions exact (A 6B b24,25,
  76-79; C 12B b24-31,80-83; Q 10/7/4B; R 7/6/4B) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides.
  T-mirrors T73662/73667/73672/73687/73703/73727 each
  re-read: hits the exact py guard line. Temps
  _t5678-5697 (base max _t5677, no reuse) + _b3444/3446/
  3448/3449/3450/3452/3453/3454 (base max _b3442) +
  _i3445/3447/3451/3455 (base max _i3443, no reuse). C
  guards `if ((n) == (110349))` / `(110350)` + 4 ranges
  exact. Insert exact both sides: after T10P268R close,
  N-out-of-scope follows. Name note: memo/A-333 "TT" =
  code "RT" (row-led tail tab by r, eye-verified in
  dispatch). Matches A-653/A-333 geometry (values
  re-checked in audit above; NO D dips).
- Edges own-loop ownloop377.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache, 316 miss-warmed; seat rgramc each):
  348/348 CLOSED. Census R256/Q64/A16/C10/S0/S1 exact.
  edges377.py: paylens 92 x84 + 256 x88; lencode 92/92
  (A head 1f/5e tail 3d/5e b5set {5e}; C head 3f/5e
  tail 51/5e b5set {5e} NO carry; Q head 53/5e +
  triple 6f/5e (o14) 71/5e (o15) 73/5e (o16) + tail
  d1/5e (o63), b5set {5e} NO step); ring counter
  256/256 (head d3/5e; 110463 (off22, ff/5e) -> 110464
  (off23, 01/5f); 110591 (off150, ff/5f) -> 110592
  (off151, 01/60); mid off143 (110584) f1/5f; off224
  (110665) 93/60; tail 110696 (off255) d1/60). S0/S1
  1b/5e + 1d/5e match raw lencode. Tail oracle sha
  1387d003459518a5 (== GATE prefix). Edge pins + tail
  110696 in for-list + 2 PASS lines each py+C. No
  DISSENT: cut bytes verify.
- C diff pure-add: numstat 636/0 (rgramc.c) + 259/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE; raw
  C 631 content + 5 bare-blank (verified bare, no
  whitespace) / 0 del; raw py 259 content / 0 del.
  Sweep-family norm ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets, keep-empty): C
  del-uniq 0 add-uniq 188 EXACT, py del-uniq 0 add-uniq
  208 EXACT (== GATE).
- Wall on band diff added lines (scope 42e6be18..
  376bc6a9, 960 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression//usr/bin/aa/shim 0
  hits, shebang 0 hits. Files: rgramc.c 636/0,
  rgram.py 259/0 purely additive, test_rgram.sh 1/1,
  PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, tier-comments
  `# T10P` 1502->1508 +6, singletons 570->572 +2,
  range-guards 528->532 +4, CLOSED T10P prints
  1502->1508 +6, C guards singleton 565->567 +2 (5-
  count C-vs-py offset pre-existing, unchanged) +
  range 528->532 +4, seal 1596->1602 +6: all agree, no
  slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-653-q781-
  t10p269 verdict CONFIRM 39/39 (13+14+12 sums exact;
  file re-read; exact-value corroboration incl sigs,
  1SIG, QM10 shared, R7 last3, QT 3B-share, ROWTAIL
  15/16 + row-led tails, ring edges + thresholds
  re-checked above) + A-333 viewer corroboration (all 3
  legs CONFIRM, consts 77/71/62/69 INCL). No
  CONFIRM-P269.md file; A-653 suffices per rule. Agrees
  with cport commit msg (PYID 7899, RGRAM 15798).
- Quiz: no conflicting CLAIM/GATE/FLAG on b377. Newest
  PARENT-* is QNUM-18 (w2e/w2f Q-block grants, read, no
  gate impact); GATE cites QNUM-16 (grants-only
  staleness, immaterial, standing pattern). PROSE-01:
  all hex/counts above copied from own run output.
- Own near-miss caught pre-filing (script fixed, code
  never impugned): ownloop377 first run carried stale
  probe-pin list (b376 numbers) after sed clone; tags
  showed None for stale pins, 348/348 CLOSED unaffected;
  probe list corrected, re-ran 0-miss full-tag.

Verdict: PASS. No RED. GATE CORRECT on code, 1 immaterial
prose staleness (QNUM-16 vs -18).
