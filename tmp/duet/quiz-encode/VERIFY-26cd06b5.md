# VERIFY-26cd06b5 b374 T10P266 pins 109305..109652 (1584 tiers) PASS

Seat viewer-r51, first-hand, detached tree-26cd06b5 @26cd06b5,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r51.
Base 6ecdbd65 (b373, 1578 tiers). Band = 5c96a8d2 (py merge
w2b@6d72712a partial, +6 tiers, +62 pins) + 26cd06b5 (C port,
1584 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build374/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ce0d8512 / aae d6e27c97
  (== GATE; aae pinned, band touches no aae sources per
  numstat) + sha1 rgramc c41f5d97 / aae 7d8dd3a2.
- RGRAMC-PYID 7804/7804 covered=7804/7804 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15608/15608 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15608/15608 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15608/15608 sorted).
- PINS 15610 rows (2 hdr + 15608, +62 vs base 15548);
  PASS-names vs PINS-names cmp-equal 15608/15608; base-N
  vs for-list cmp-equal 7804/7804. For-list delta vs base
  +31/-0: 109305 109306 109307 109309 109311 109312 109318
  109322 109323 109325 109327 109328 109329 109330 109331
  109332 109333 109348 109349 109364 109365 109380 109381
  109396 109397 109439 109440 109504 109567 109568 109652
  (2 sing + A6 head/carry-edge-pair/mids/tail + C8
  head/mids/all-sig/tail + Q8 head/row-edge-pairs/tail
  offs 0,15/16,31/32,47/48,63 + R7 head/edge-pairs/mid/
  tail offs 0,42/43,107,170/171,255 == GATE
  decomposition; 7773->7804); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit374.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 77 PASS 0
  FAIL first run. Inventory exactly the 13 both sides.
  S0/S1 168ch sigs a0740300/2a40e906 both NEW (vs P265
  a0560300/bdcfaa06, full-string ne, re-read). AM 16x9B
  / CM 10x15B / M 16x7B / QR 4x8B / QT 4x4B / RM 16x7B /
  RQ 16x7B all C==py. AM/CM/M/RM/RQ all 16/16 or 10/10
  distinct. 5SIG map exact: 958dec06 x5 offs 0-4 +
  e5e87b03 + dd767803 + 6d417603 + 750e7e03 x2 offs 8-9
  (5 distinct in order; full sig in tab, CC has no
  b0-3). QUAD single-sig c0822772 (QC b0-3); NO frags
  (M+QR+QT legs only, eye-verified). QR DOUBLE-PAIRED
  r0==r3 f216dbb97b532400 x2 AND r1==r2 32999dc175931007
  x2 (FIRST; 2 distinct). QT b3327d33/ceb7d61f/f3b7d61f/
  23337d33; r1/r2 share TRUE 3B b7d61f + r0/r3 share 2B
  7d33 (tails echo the R double-pairing). RQ==M full-row
  16/16 (FOURTH FULL instance after P261/P264/P265;
  staging per precedent, NOT a finding). AC/CC/QC/RC
  73/67/63/72 py-vs-C normalized; _N decls 73/67/63/72
  match actual; sorted-unique; b4/b5 in no const set.
  RC b0-3 03000000 NEW vs P265T (P265 b0 split-in-code,
  b1-3 000000, P265R dispatch comment re-read); RC
  b84-87 28ee7163 ring-wide (P265 had 2032bed2).
  STANDARD ring: RM tail b80-83 (chars 6:14) / RQ tail
  b76-79 (chars 6:14) 16/16 distinct each, sets disjoint
  (SPLIT-swapped, UNPAIRED). M-tails 16/16 ALL NEW vs
  P265T (zero overlap vs BOTH P265RM-tail and P265RQ-
  tail sets; P265 RM 16ch / RQ 12ch rows re-read).
  Coverage unions exact every block (A 9+73+2=84, C
  15+67+2=84, Q 19+63+2=84, R 14+72+2=88), 0 overlap.
  PBA sig 8087f776 NEW (P265 PBA e0932f72 per P265A
  dispatch comment re-read). Memo INCL PBA 73 / C10 68 /
  quad 64 / T88 72 (A-638 re-read): impl 73/67/63/72 =
  identical PBA/T88, memo-1 C10/quad (standing;
  b5-const excluded).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 109305 / S1 109306 / A 109307-322 / C 109323-332 /
  Q 109333-396 / R 109397-652): bounds + paylens (84
  x92 / 88 x256) + lencode both sides + R counter
  b4=(171+2off)&FF b5=86+(off>=43)+(off>=171) both
  sides (C 171/86 = 0xAB/0x56) + mtab/qtab/ttab byte
  positions exact (A 9B b12-15,19,76-79; C 15B
  b0-3,11,18-23,80-83; Q 7/8/4B; R 7/7B) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides.
  T-mirrors T72907/72912/72917/72932/72949/72972 each
  re-read: hits the exact py guard line. Temps _t5622-
  5639 (base max _t5621, no reuse) + _b3411/3413/3415/
  3416/3417/3419/3420 (base max _b3409) + _i3412/3414/
  3418/3421 (base max _i3410, no reuse). C guards
  `if ((n) == (109305))` / `(109306)` + 4 ranges exact.
  Insert exact both sides: after T10P265R close,
  N-out-of-scope follows. Matches A-638/A-330 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop374.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache, 317 warmed; seat rgramc each):
  348/348 CLOSED. Census R256/Q64/A16/C10/S0/S1 exact.
  edges374.py: paylens 84 x92 + 88 x256; lencode 92/92;
  ring counter 256/256. S0/S1 f3/55 + f5/55 match raw
  lencode. A head f7/55 tail 15/56 b5set {55,56}, carry
  ff/55->01/56 @109311->109312 single flip off4->5;
  PBA formula == raw lencode 16/16; C head 17/56 tail
  29/56 b5set {56}; Q head 2b/56 tail a9/56 b5set {56}
  NO carry; ring 109439 (off42 ff/56) -> 109440 (off43
  01/57); 109567 (off170 ff/57) -> 109568 (off171
  01/58); mid off107 (109504) 81/57; R head ab/56 tail
  a9/58 (off255). Edge pins + tail 109652 in for-list +
  2 PASS lines each py+C. No DISSENT: cut bytes verify.
- C diff pure-add: numstat 610/0 (rgramc.c) + 238/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 605 content + 5 bare-blank (`+$`, verified bare, no
  whitespace) / 0 del; raw py 238 content / 0 del.
  Fine-norm temp-norm-only (_tN/_iN/_bN, empty-
  excluding): C del-uniq 0 add-uniq 397 EXACT (== GATE),
  py del-uniq 0 add-uniq 188. Sweep2 family.
- Wall on band diff added lines (scope 6ecdbd65..
  26cd06b5, 911 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 610/0, rgram.py 238/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 564->566 +2 / ranges 516->520 +4 (stated
  method py; C ranges 516->520 +4; C singletons broad
  `(n) == (` 564->566 +2 == GATE, dispatch-guard-only
  559->561 +2, delta agrees both), CLOSED T10P prints
  1484->1490 +6, seal 1578->1584 +6: all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-638-q778-
  t10p266 verdict CONFIRM 39/39 (13+12+14 sums exact;
  file present, counts verified; exact-value
  corroboration incl 5SIG map, QR double-pair, QT
  tails, single-sig, M-tails NEW, ring edges + consts
  re-checked above) + A-330 viewer corroboration (all 3
  legs CONFIRM, no correction). No CONFIRM-P266.md file;
  A-638 suffices per rule. Agrees with cport commit msg
  (PYID 7804, RGRAM 15608).
- Quiz: no conflicting CLAIM/GATE/FLAG on b374. Newest
  PARENT-* is QNUM-16 (w2d Q-block grant, read, no gate
  impact); GATE cites QNUM-13 (grants-only staleness,
  immaterial, standing pattern). PROSE-01: all hex/
  counts above copied from own run output.

Verdict: PASS. No RED. GATE CORRECT on code, 1 immaterial
prose staleness (QNUM-13 vs -16).
