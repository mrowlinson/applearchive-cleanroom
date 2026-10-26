# VERIFY-7ad92845 b372 T10P264 pins 108609..108956 (1572 tiers) PASS

Seat viewer-r51, first-hand, detached tree-7ad92845 @7ad92845,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r51.
Base 575049ad (b371, 1566 tiers). Band = 2bd8f004 (py merge
w2b@b0060063 partial, +6 tiers, +62 pins) + 7ad92845 (C port,
1572 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build372/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc fec1cd75 / aae d6e27c97
  (== GATE; aae pinned, band touches no aae sources per
  numstat) + sha1 rgramc baed201f / aae 7d8dd3a2.
- RGRAMC-PYID 7742/7742 covered=7742/7742 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15484/15484 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15484/15484 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15484/15484 sorted).
- PINS 15486 rows (2 hdr + 15484, +62 vs base 15424);
  PASS-names vs PINS-names cmp-equal 15484/15484; base-N
  vs for-list cmp-equal 7742/7742. For-list delta vs base
  +31/-0: 108609 108610 108611 108612 108616 108621 108625
  108626 108627 108628 108630 108633 108635 108636 108637
  108652 108653 108668 108669 108671 108672 108684 108685
  108700 108701 108799 108800 108864 108927 108928 108956
  (2 sing + A6 + C6 + Q10 + R7 == GATE decomposition;
  7711->7742); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit372.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 110 PASS 0
  FAIL. Inventory exactly the 24 both sides (F6 family:
  M22-34/XA22-34, no QR either side, grep 0/0). S0/S1
  168ch sigs a2560300/bdcfaa06 NEW vs P263 02550300/
  5d45ad06 (re-read). AM 16x8B / CM 10x12B / M 16x7B /
  QT 4x4B / RM 16x9B / RQ 16x7B all C==py. AM 16/16
  distinct; CM 10/10 diverge; M 16/16 distinct. F6
  col-const degenerate 16/16 each (M22 0f / M23 df /
  M30 be / M32 d5 / M33 49 / M34 c0); XA row-vectors
  [00,50,50,80] / [00,2f,2f,79] / [00,70,70,04] /
  [00,a0,a0,a0] / [00,e0,e0,30] / [00,21,21,c3] EXACT
  (== A-629 ADD vectors, r1==r2 x6). QT c37be99d/
  c0fadb1d/e5fadb1d/cb6a97b8; r1/r2 share TRUE 3B
  fadb1d; last2B 3-unique (e99d/db1d/db1d/97b8).
  RQ==M full-row 16/16 (FULL family, 2nd after P261;
  staging per precedent, NOT a finding). AC/CC/QC/RC
  74/70/65/70 py-vs-C normalized; _N decls 74/70/65/70
  match actual; sorted-unique; b4/b5 in no const set.
  CC b0-3 bdcfaa06 == S1 sig (C10-1SIG full-sig-in-
  const). RC b0-3 06000000 == P263T (code-verified vs
  P263RC b0-3); RC b84-87 f36a97b8 ring-wide (P263 had
  00ad0fa0). RM tail b80-83 (chars 10:18) / RQ tail
  b76-79 (chars 6:14) 16/16 distinct each, sets disjoint
  (SPLIT-swapped, UNPAIRED). M-tails 16/16 ALL NEW vs
  P263T (zero overlap vs BOTH P263RM-tail and P263RQ-
  tail sets; P263 RM 16ch / RQ 14ch rows re-read).
  Coverage unions exact + disjoint (A 8+74+2=84, C
  12+70+2=84, Q 17+65+2=84, R 16+70+2=88);
  const-complements exactly mtab+lencode (AC-8
  [21,22,23,31,76-79]; CC-12 [22,23,30-35,80-83]; QC-17
  [22,23,30,32-34,36-38,76-83]; RC-16
  [18,19,39-42,46,47,76-83]). Memo INCL PBA 75 / C10
  71 / quad 65 / T88 70 (A-629 re-read): impl
  74/70/65/70 = memo-1 on PBA/C10 (standing),
  identical quad/T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 108609 / S1 108610 / A 108611-626 / C 108627-636 /
  Q 108637-700 / R 108701-956): bounds + paylens (84
  x92 / 88 x256) + lencode both sides + R counter
  b4=(59+2off)&FF b5=81+(off>=99)+(off>=227) both
  sides (C 59/81 = 0x3B/0x51) + mtab/qtab/ttab byte
  positions exact (A 8B; C 12B; Q 7/1/4B + F6 adds
  (pay-XA[q])&FF==M[m] x6 both sides; R 9/7B) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides.
  T-mirrors T72422/72427/72432/72447/72463/72495 each
  re-read: hits the exact py guard line. Temps _t5576-
  5603 (base max _t5575, no reuse) + _b3390/3392/3394/
  3395/3397/3398 + _i3391/3393/3396/3399 (base max
  _b3388/_i3389, no reuse). C guards
  `if ((n) == (108609))` / `(108610)` + 4 ranges exact.
  Insert exact both sides: after T10P263R close,
  N-out-of-scope follows. Matches A-629/A-328 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop372.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache, 0 misses; seat rgramc each):
  348/348 CLOSED. Census R256/Q64/A16/C10/S0/S1 exact.
  edges372.py: paylens 84 x92 + 88 x256; lencode 92/92;
  ring counter 256/256. S0/S1 83/50 + 85/50 match raw
  lencode. A head 87/50 tail a5/50 b5set {50}; C head
  a7/50 tail b9/50 b5set {50}; Q head bb/50 tail 39/51
  b5set {50,51}, carry ff/50->01/51 @108671->108672
  single flip off34->35 mid-row2; ring 108799 (off98
  ff/51) -> 108800 (off99 01/52); 108927 (off226
  ff/52) -> 108928 (off227 01/53); mid off163 (108864)
  81/52; R head 3b/51 tail 39/53 (off255). Edge pins +
  tail 108956 in for-list + 2 PASS lines each py+C. No
  DISSENT: cut bytes verify.
- C diff pure-add: numstat 776/0 (rgramc.c) + 366/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 771 content + 5 bare-blank (`+$`, verified bare, no
  whitespace) / 0 del; raw py 366 content / 0 del.
  Fine-norm temp-norm-only (_tN/_iN/_bN, empty-
  excluding): C del-uniq 0 add-uniq 443 EXACT (== GATE),
  py del-uniq 0 add-uniq 220. Sweep2 family.
- Wall on band diff added lines (scope 575049ad..
  7ad92845, 1205 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 776/0, rgram.py 366/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 560->562 +2 / ranges 508->512 +4 (stated
  method py; C ranges 508->512 +4; C singletons broad
  `(n) == (` 560->562 +2 == GATE, dispatch-guard-only
  555->557 +2, delta agrees both), CLOSED T10P prints
  1472->1478 +6, seal 1566->1572 +6: all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-629-q776-
  t10p264 verdict CONFIRM 49/49 (12+21+16 sums exact;
  file re-read in full; exact-value corroboration incl
  ADD vectors, QT tails, single-sig, M-tails NEW, ring
  edges + consts re-checked above) + A-328 viewer
  corroboration (all 3 legs CONFIRM + 1 correction
  quad-65, matching impl QC 65). No CONFIRM-P264.md
  file; A-629 suffices per rule. Agrees with cport
  commit msg (PYID 7742, RGRAM 15484).
- Quiz: no conflicting CLAIM/GATE/FLAG on b372. Newest
  PARENT-* is QNUM-16 (w2d Q-block grant, read, no gate
  impact); GATE cites QNUM-13 (grants-only staleness,
  immaterial, standing pattern). PROSE-01: all hex/
  counts above copied from own run output.

Verdict: PASS. No RED. GATE CORRECT on code, 1 immaterial
prose staleness (QNUM-13 vs -16).
