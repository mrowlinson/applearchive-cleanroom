# VERIFY-926c1bd9 b365 T10P257 pins 106173..106520 (1530 tiers) PASS

Seat viewer-r49, first-hand, detached tree-926c1bd9 @926c1bd9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r49.
Base bd37fe85 (b364, 1524 tiers). Band = 99d41bb0 (py) + 926c1bd9 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build365/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings (empty stderr). sha1 rgramc 2b96810f /
  aae 7d8dd3a2 + sha256 rgramc b813309f / aae d6e27c97
  (== GATE all 4; aae pinned, band touches no aae sources
  per numstat).
- RGRAMC-PYID 7525/7525 covered=7525/7525 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15050/15050 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15050/15050 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15050/15050 sorted).
- PINS 15052 rows (2 hdr + 15050, +62 vs base); base-N
  set-eq 7525/7525 (cmp 0); PASS-names vs PINS-names
  cmp-equal 15050/15050. For-list delta vs base +31/-0:
  106173 106174 106175 106176 106181 106185 106189
  106190 106191 106194 106195 106196 106197 106198
  106199 106200 106201 106217 106233 106239 106240
  106248 106249 106264 106265 106367 106368 106393
  106495 106496 106520 (2 sing + A6 + C8 + Q8 + R7 ==
  GATE decomposition); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit365.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 113 PASS 0
  FAIL first run. C-vs-py EXACT all 13 (S0/S1 168ch sigs
  601a0300 NEW / e58c3506 ==P256PB1 NEW string vs P256
  641a0300/e58c3506 re-read; AM 16x9B distinct; CM 10x13B
  distinct; M 16x8B distinct; QR 4x8B r2==r3 PAIRED
  4b9272aaf1b82f64 + r0/r1 distinct, row-sigs 53/55/4b/4b;
  QT 4x4B distinct d777ee49/223c1151/d528f87f/ff28f87f
  r2/r3 TRUE 3B-share 28f87f 1st-bytes differ; RM/RQ
  16x7B distinct; AC/CC/QC/RC 73/69/62/72 pairs
  py-hex-vs-C-dec normalized). _N decls 73/69/62/72
  match actual. Inventory exactly the 13 (no QB/BM/BC/
  M42/X42/PT/FM either side). Missing-sets EXACT: AC-11
  [4,5,47-51,76-79]; CC-15 [2-5,35,46-51,80-83] (b0,b1
  const e5,8c, sig b2,b3 in tab); QC-22 [3-9,35,46-51,
  76-83]; RC-16 [4-7,9-12,76-83]. CM sig-map exact
  order 3506x4@rows0-3 + d504/9504/b504/d504@rows4-7 +
  1505x2@rows8-9 (d504 repeats @rows4,7 = N 106195/
  106198, 5 distinct). AC b0-3 a0802f7c == P256AC b0-3
  re-read. RC b0-3 05000000 == P249RC + P251RC b0-3 py+C
  all re-read; RC b84-87 dc77ac14. M/RQ heads b6,7
  16/16 + tails b76-79 16/16 same-index (middle M-b8,9
  vs RQ-b12 differs; 8B vs 7B). RM[c]/RQ[r] UNPAIRED
  both sides, tails SPLIT col/row 16/16 distinct each.
  M-tails 16 distinct, zero overlap vs P256RQ-tail set
  (P256RQ 7B re-read). QT 4/4 NEW vs P256QT (10299170/
  36299170/6c301f67/87aa49cb re-read). Coverage unions
  exact (A 9+73+2=84, C 13+69+2=84, Q 8+8+4+62+2=84, R
  7+7+72+2=88; disjoint, b4/b5 in no const set; C _b
  positions == py all 7 legs; C _b var order 3313/3315/
  3317/3318/3319/3321/3322). Memo INCL PBA 74 / C10 70
  / quad 62 / T88 72 (A-611/A-321 re-read): impl
  73/69 = memo-1 on PBA/C10 (standing), 62/72 identical.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 106173 / S1 106174 / A 106175-190 / C 106191-200 /
  Q 106201-264 / R 106265-520): bounds + paylens
  (84 x92 / 88 x256) + lencode/counter formulas exact
  incl R 0x33/0x3E/103/231 both sides (C 51/62/103/231).
  T-mirrors T70591/70596/70601/70617/70633/70656 each
  re-read: hits the exact py guard line (106173/106174/
  106175/106191/106201/106265). Temps _t5446-5463 (base
  max _t5445, no reuse) + _b3313/3315/3317/3318/3319/
  3321/3322 + _i3314/3316/3320/3323 (base max _b3311/
  _i3312, no reuse). C guards `if ((n) == (106173))` /
  `(106174)` + 4 ranges exact. Insert exact both sides:
  after T10P256R close, N-out-of-scope follows.
  Matches A-611/A-321 geometry (values re-checked in
  audit above; NO D dips).
- Edges own-loop ownloop365.py over ALL 348 tier Ns
  (fresh oracle bytes via ct-cache miss path,
  tool-identical -encode -a lzraven; 31 cache hits +
  317 fresh encodes; seat rgramc each): 348/348 CLOSED.
  Q-carry 106239 (ff/3d) -> 106240 (01/3e) INTERNAL
  off38->39 single flip; ring 106367 (off102 ff/3e) ->
  106368 (off103 01/3f); 106495 (off230 ff/3f) ->
  106496 (off231 01/40); mid off128 (106393) 33/3f. A
  b5set {3d}, C {3d}, Q {3d,3e}. Heads/tails: A
  7f/3d-9d/3d, C 9f/3d-b1/3d, Q b3/3d-31/3e, R
  33/3e-31/40. S0/S1 embedded b4/b5 7b/3d + 7d/3d match
  raw lencode. pay[4:6]==LE16((n<<1)|1) 348/348
  whole-tier incl 88B cells (ring 256/256). Paylens 84
  x92 + 88 x256.
- C diff pure-add: numstat 610/0 (rgramc.c) + 238/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 605 content + 5 blank-only / 0 del; raw py 238
  content / 0 del. Normalized ([0-9]+ -> N, diff-sign
  strip, trailing-';' strip, python sets, keep-empty/
  no-lead-strip): C del-uniq 0 add-uniq 174, py del-uniq
  0 add-uniq 195, del-subset-add 0 missing - sweep
  family, EXACT. Band-level sole del = for-line churn.
- Wall on band diff added lines (911): vendor/disasm 0,
  depload 0, libcompression/compression_tool/aa/
  nominated/shim/ct-cache 0, shebang 0.
- Tiers: merge-msg +6, code 6 blocks, `# T10P` 1430->
  1436 +6, singletons `if n == ` 546->548 +2,
  range-guards `<= n <=` 480->484 +4, CLOSED T10P prints
  1430->1436 +6 (bare-CLOSED 1948->1954 +6, same delta),
  C guards singleton 541->543 +2 / range 480->484 +4
  (5-count C-vs-py offset pre-existing, unchanged), seal
  1524->1530 +6: all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-611-q769
  verdict CONFIRM (shape 12/12 + quad/ring 11/11 +
  counters 12/12; verdict line 35/35 as-filed, sums
  exact, no quirk; TRUE-3B 28f87f memo re-verified
  programmatically; tier cut SAFE; exact-value
  corroboration incl CM 5-sig map, QR r2==r3 + rowsigs,
  QT tails + 3B-share, M-tails NEW, ring edges +
  consts re-checked above) + A-321 (all 3 legs CONFIRM,
  348-cell bed + P256 refs + P258 window, consts
  74/70/62/72 INCL). No CONFIRM-P257.md file; A-611
  suffices per rule. Agrees with cport commit msg (py/C
  15050, PYID 7525).
- Quiz: no conflicting CLAIM/GATE/FLAG on b365. Newest
  PARENT-* is QNUM-14 (grants only, read, no gate
  impact); GATE cites QNUM-12: 1 immaterial staleness
  (2 behind). PROSE-01: every value above copied from
  own run output, GATE re-read before filing.
- Logs: NVME ws tmp/encode-viewer/r49/ (build365.log,
  pyid365.log, rgram365py/c.log, cmp365.py/.c,
  for365(-old).nums, pins365.basen/.names, pass365.names,
  smoke365.log, tables365.log, tabaudit365.py,
  ownloop365.log/.py, banddiff365-py/-c.txt,
  base365-py/-c.txt, sweepnorm365-c/py-add.txt).

Verdict: PASS. No RED. Code CORRECT; GATE CORRECT on code
(1 immaterial QNUM staleness). Ready for parent PV/merge.
