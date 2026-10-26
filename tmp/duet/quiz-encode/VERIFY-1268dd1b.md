# VERIFY-1268dd1b b369 T10P261 pins 107565..107912 (1554 tiers) PASS

Seat viewer-r50, first-hand, detached tree-1268dd1b @1268dd1b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r50.
Base 8676784a (b368, 1548 tiers). Band = 26a82bdb (py merge
w2b@fd38b136 partial, +6 tiers, +62 pins) + 1268dd1b (C port,
1554 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build369/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 768e4574 / aae 7d8dd3a2 +
  sha256 rgramc cb10fde2 / aae d6e27c97 (== GATE all 4;
  aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 7649/7649 covered=7649/7649 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15298/15298 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15298/15298 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15298/15298 sorted).
- PINS 15300 rows (2 hdr + 15298, +62 vs base 15238);
  base-N set-eq 7649/7649 (cmp 0); PASS-names vs
  PINS-names cmp-equal 15298/15298. For-list delta vs
  base +31/-0: 107565 107566 107567 107568 107572 107577
  107581 107582 107583 107584 107586 107589 107591 107592
  107593 107608 107609 107624 107625 107640 107641 107647
  107648 107656 107657 107775 107776 107840 107903 107904
  107912 (2 sing + A6 + B6 + Q10 + R7 == GATE
  decomposition); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit369.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 87 PASS 0
  FAIL first run. Inventory exactly the 13 both sides.
  S0/S1 168ch sigs 0f550300/adecad06 NEW vs P260
  2f370300/05010206 (re-read). AM 16x8B / BM 10x12B /
  M 16x8B / QR 4x7B / QT 4x4B / RM 16x7B / RQ 16x8B all
  C==py. AM 16/16 distinct; BM 10/10 diverge; M/RM/RQ
  16/16 distinct each. QR r0==r2 EVEN-PAIRED
  e53cf3d4b53eb1 x2 (first EVEN r02 pair); r1
  5f3c623315b6d1 + r3 f6bcd40cf5d63e distinct. QT
  7fa0e666/9517fb30/caa0e666/027177fa; r0/r2 share
  TRUE-3B a0e666 (matching R-pair); last-2B 3-unique
  (e666/fb30/e666/77fa); 4/4 NEW vs P260QT
  (fdc59ac8/f4840360/70affd40/12ee7121 re-read). RQ==M
  FULL-STRING 16/16 same-index order-identical (FOURTH
  family). AC/BC/QC/RC 74/70/63/71 pairs py-hex-vs-C-dec
  normalized; _N decls 74/70/63/71 match actual; b4/b5
  in no const set. AC b0-3 e08ad76e NEW vs P260AC
  5d102060 (re-read); BC b0-3 35fda506 single-sig; QC
  b0-3 e08ad76e == PBA sig (single-sig quad); RC b0-3
  06000000 == P252/P253/P256/P259 RC b0-3 (all 4
  re-read py); RC b84-87 22ecf42b ring-wide. RM/RQ
  tails (last 4B) 16/16 distinct each, sets disjoint
  (SPLIT). M-tails 16/16 ALL NEW vs P260T (zero overlap
  vs BOTH P260RM-tail and P260RQ-tail sets); M-full
  also ALL NEW vs P260RQ. Coverage unions exact +
  disjoint (A 8+74+2=84, B 12+70+2=84, Q 8+7+4+63+2=84,
  R 7+8+71+2=88); const-complements exactly lencode+
  mtab (AC-10 [4,5,24-27,76-79]; BC-14
  [4,5,24-31,80-83]; QC-21
  [4,5,21-31,76-83]; RC-17
  [4,5,25-27,35,40-42,76-83] verbatim == GATE). C _b
  legs 7/7 positions == py
  (_b3357/3359/3361/3362/3363/3365/3366). Memo INCL
  PBA 75 / B10 71 / quad 63 / T88 71 (A-624 re-read):
  impl 74/70/63/71 = memo-1 on PBA/B10 (standing),
  identical quad/T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 107565 / S1 107566 / A 107567-582 / B 107583-592 /
  Q 107593-656 / R 107657-912): bounds + paylens (84
  x92 / 88 x256) + lencode both sides + R counter
  b4=(19+2off)&FF b5=73+(off>=119)+(off>=247) both
  sides (C 19/73 = 0x13/0x49) + mtab/qtab/ttab byte
  positions exact (A 8B b24-27,76-79; B 12B b24-31,
  80-83; Q 8/7/4B; R 7/8B) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides. T-mirrors T71565/
  71570/71575/71590/71606/71629 each re-read: hits the
  exact py guard line. Temps _t5520-5537 (base max
  _t5519, no reuse) + _b3357-3366 span (base max _b3355)
  + _i3358/3360/3364/3367 (base max _i3356, no reuse).
  C guards `if ((n) == (107565))` / `(107566)` + 4
  ranges exact. Insert exact both sides: after T10P260R
  close, N-out-of-scope follows. Matches A-624/A-325
  geometry (values re-checked in audit above; NO D
  dips).
- Edges own-loop ownloop369.py over ALL 348 tier Ns
  (fresh oracle bytes via tool-identical -encode -a
  lzraven through ct-cache; seat rgramc each): 348/348
  CLOSED. Paylens 84 x92 + 88 x256. Lencode 92/92;
  ring counter 256/256. S0/S1 5b/48 + 5d/48 match raw
  lencode. A head 5f/48 tail 7d/48 b5set {48}; B head
  7f/48 tail 91/48 b5set {48}; Q head 93/48 tail 11/49,
  carry ff/48->01/49 @107647->107648 single flip
  off54->55; ring 107775 (off118 ff/49) -> 107776
  (off119 01/4a); 107903 (off246 ff/4a) -> 107904
  (off247 01/4b); mid off183 (107840) 81/4a; R head
  13/49 tail 11/4b (off255). Edge pins + tail 107912
  in for-list + PASS py+C. No DISSENT: cut bytes
  verify.
- C diff pure-add: numstat 610/0 (rgramc.c) + 237/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 605 content + 5 bare-blank / 0 del; raw py 237
  content / 0 del. Normalized ([0-9]+ -> N, diff-sign
  strip, trailing-';' strip, python sets, keep-empty/
  no-lead-strip): C del-uniq 0 add-uniq 159, py del-uniq
  0 add-uniq 183, del-subset-add 0 missing - sweep
  family, EXACT. Band-level sole del = for-line churn.
- Wall on band diff added lines (910): vendor/disasm 0,
  depload 0, libcompression/compression_tool/aa/
  nominated/shim/ct-cache 0, shebang 0.
- Tiers: merge-msg +6, code 6 blocks, `# T10P` 1454->
  1460 +6, singletons `if n == ` 554->556 +2,
  range-guards `<= n <=` 496->500 +4, CLOSED T10P prints
  1454->1460 +6, C guards singleton 549->551 +2 / range
  496->500 +4 (5-count C-vs-py offset pre-existing,
  unchanged), seal 1548->1554 +6: all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-624-q773
  verdict CONFIRM (shape 12/12 + quad/ring 11/11 +
  counters 11/11 as sectioned; verdict line 34/34
  as-filed, sections sum 34 exact, no quirk; R7 r0==r2
  EVEN-PAIRED first + tails r0/r2 TRUE-3B programmatic
  re-verify; tier cut SAFE; exact-value corroboration
  incl ring edges + consts re-checked above) + A-325
  (all 3 legs CONFIRM, 348-cell bed + P260T ref + P262
  window, consts 75/71/63/71 INCL). No CONFIRM-P261
  file; A-624 suffices per rule. Agrees with cport
  commit msg (PYID 7649, RGRAM 15298).
- Quiz: no conflicting CLAIM/GATE/FLAG on b369. Newest
  PARENT-* is QNUM-15 (Q-block grants only, read, no
  gate impact); GATE cites QNUM-12: 1 immaterial
  staleness (3 behind, standing pattern). PROSE-01:
  every value above copied from own run output, GATE
  re-read before filing.
- Logs: NVME ws tmp/encode-viewer/r50/ (build369.log,
  pyid369.log, rgram369py/c.log, cmp369.py/.c,
  for369-old/-new.nums, pins369.names/.baseN,
  pass369.names, smoke369.log, tables369.log,
  tabaudit369.py, ownloop369.log/.py, numstat369.txt,
  cdiff369.txt, pydiff369.txt, added369.txt,
  sweepnorm369-c/py-add.txt).

Verdict: PASS. No RED. Code CORRECT; GATE CORRECT on code
(1 immaterial QNUM staleness). Ready for parent PV/merge.
