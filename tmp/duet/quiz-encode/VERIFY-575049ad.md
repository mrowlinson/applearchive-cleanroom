# VERIFY-575049ad b371 T10P263 pins 108261..108608 (1566 tiers) PASS

Seat viewer-r50, first-hand, detached tree-575049ad @575049ad,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r50.
Base a9247512 (b370, 1560 tiers). Band = 6d554cf6 (py merge
w2b@ca2457ad partial, +6 tiers, +62 pins) + 575049ad (C port,
1566 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build371/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 4bfa780f / aae 7d8dd3a2 +
  sha256 rgramc 49f0f8ad / aae d6e27c97 (== GATE all 4;
  aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 7711/7711 covered=7711/7711 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15422/15422 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15422/15422 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15422/15422 sorted).
- PINS 15424 rows (2 hdr + 15422, +62 vs base 15362);
  base-N set-eq 7711/7711 (cmp 0); PASS-names vs
  PINS-names cmp-equal 15422/15422. For-list delta vs
  base +31/-0: 108261 108262 108263 108265 108268 108269
  108270 108278 108279 108281 108283 108284 108285 108286
  108287 108288 108289 108304 108305 108320 108321 108336
  108337 108352 108353 108415 108416 108480 108543 108544
  108608 (2 sing + A6 incl sig2 pair 108269/270 + C8 +
  Q8 + R7 == GATE decomposition; all 3 split sigs
  covered); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit371.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 99 PASS 0
  FAIL first run. Inventory exactly the 15 both sides
  (M19/XA19 b19-tie; CM/CC, no BM/BC). S0/S1 168ch sigs
  02550300/5d45ad06 NEW vs P262 0a550300/35fda506
  (re-read). AM 16x9B / CM 10x16B / M 16x7B / M19 16x1B
  / XA19 4x1B / QR 4x7B / QT 4x4B / RM 16x8B / RQ 16x7B
  all C==py. AM 16/16 distinct; CM 10/10 diverge; M
  16/16 distinct (heads 14-unique, tails disambiguate).
  AM split map b0: 6a x6 offs0-5 + 6c x2 offs6-7 + 50 x8
  offs8-15 (SPLIT6/2/8; full sigs 6a56d46a x6 +
  6c56d46a x2 + 5056d46a x8 via AC b1-3 const 56d46a;
  AC has no b0). CM sandwich b0-3: 6645ad06 x5 offs0-4 +
  b3a25603 x1 off5 + 6645ad06 x4 offs6-9. M19 values
  exact (b0/f0/78/68/b8/d8/40/48/88/38/50/90/f0/38/a0/80,
  14 distinct); XA19 [00,01,01,00] EXACT. b19 ADD staged
  both sides (py `(pay[19]-int(XA19[q],16))&FF vs M19[m];
  C snprintf %02lx same formula; P231/P239 same-formula
  precedent re-read) + XOR tie X=[00,01,01,00] documented
  in Q-block comment both sides. QR r1==r2 MID-PAIRED
  00825f6e963d30 x2; r0 e08e177fd756f2 + r3
  60857f72d1c04a distinct; sig-led b0-3 e08e177f/
  00825f6e/60857f72. QT ea36c61a/c1362ebe/05372ebe/
  ceebb136; r1/r2 share last 2B 2ebe ONLY (last3B
  362ebe/372ebe DIFFER; 2nd bytes 36/37 1B-off);
  last2B 3-unique (c61a/2ebe/2ebe/b136); 4/4 NEW vs
  P262QT (928e9d33/bdc02fdf/e2c02fdf/734a4841 re-read).
  RQ==M tails-only family: b76-79 same-index 16/16 + 1
  full-row coincidence idx5 (fbdcecd7fa71b9) + heads
  last-2B same-index 16/16 (byte0 differs except idx5);
  second tails-only instance after P255 (P261 was FULL).
  AC/CC/QC/RC 73/66/63/71 pairs py-hex-vs-C-dec
  normalized; _N decls 73/66/63/71 match actual; b4/b5
  in no const set. RC b0-3 06000000; RC b84-87 00ad0fa0
  ring-wide. RM/RQ tails (RM b80-83 / RQ b76-79, last
  4B each) 16/16 distinct each, sets disjoint
  (SPLIT-swapped). M-tails 16/16 ALL NEW vs P262T (zero
  overlap vs BOTH P262RM-tail and P262RQ-tail sets; P262
  RM/RQ 6B rows re-read); M-full also ALL NEW vs
  P262RQ. Coverage unions exact + disjoint (A 9+73+2=84,
  C 16+66+2=84, Q 7+1+7+4+63+2=84, R 8+7+71+2=88);
  const-complements exactly lencode+mtab (AC-11
  [0,4,5,9-12,76-79]; CC-18 [0-5,11,13-19,80-83]; QC-21
  [0-5,12-14,16-19,76-83]; RC-17
  [4,5,20-22,28-31,76-83] verbatim == GATE). C _b legs
  7/7 positions == py (_b3379/3381/3383/3384/3385/3387/
  3388; b19 inline both sides). Memo INCL PBA 74 / C10
  66 / quad 64 / T88 71 (A-628 re-read): impl
  73/66/63/71 = memo-1 on PBA/quad (standing),
  identical C10/T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 108261 / S1 108262 / A 108263-278 / C 108279-288 /
  Q 108289-352 / R 108353-608): bounds + paylens (84
  x92 / 88 x256) + lencode both sides + R counter
  b4=(131+2off)&FF b5=78+(off>=63)+(off>=191) both
  sides (C 131/78 = 0x83/0x4E) + mtab/qtab/ttab byte
  positions exact (A 9B b0,9-12,76-79; C 16B
  b0-3,11,13-19,80-83; Q 7/1/7/4B; R 8/7B) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides.
  T-mirrors T72061/72066/72071/72087/72104/72129 each
  re-read: hits the exact py guard line. Temps _t5556-
  5575 (base max _t5555, no reuse) + _b3379-3388 span
  (base max _b3377) + _i3380/3382/3386/3389 (base max
  _i3378, no reuse). C guards
  `if ((n) == (108261))` / `(108262)` + 4 ranges exact.
  Insert exact both sides: after T10P262R close,
  N-out-of-scope follows. Matches A-628/A-327 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop371.py over ALL 348 tier Ns
  (fresh oracle bytes via tool-identical -encode -a
  lzraven through ct-cache; seat rgramc each): 348/348
  CLOSED. Paylens 84 x92 + 88 x256. Lencode 92/92;
  ring counter 256/256. S0/S1 cb/4d + cd/4d match raw
  lencode. A head cf/4d tail ed/4d b5set {4d}; C head
  ef/4d tail 01/4e b5set {4d,4e}, carry ff/4d->01/4e
  @108287->108288 single flip off8->9 LAST-INTERNAL; Q
  head 03/4e tail 81/4e b5set {4e} NO carry; ring
  108415 (off62 ff/4e) -> 108416 (off63 01/4f); 108543
  (off190 ff/4f) -> 108544 (off191 01/50); mid off127
  (108480) 81/4f; R head 83/4e tail 81/50 (off255).
  Edge pins + tail 108608 in for-list + PASS py+C. No
  DISSENT: cut bytes verify.
- C diff pure-add: numstat 640/0 (rgramc.c) + 261/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 635 content + 5 bare-blank / 0 del; raw py 261
  content / 0 del. Normalized ([0-9]+ -> N, diff-sign
  strip, trailing-';' strip, python sets, keep-empty/
  no-lead-strip): C del-uniq 0 add-uniq 183, py del-uniq
  0 add-uniq 204, del-subset-add 0 missing - sweep
  family, EXACT. Band-level sole del = for-line churn.
- Wall on band diff added lines (964): vendor/disasm 0,
  depload 0, libcompression/compression_tool/aa/
  nominated/shim/ct-cache 0, shebang 0.
- Tiers: merge-msg +6, code 6 blocks, `# T10P` 1466->
  1472 +6, singletons `if n == ` 558->560 +2,
  range-guards `<= n <=` 504->508 +4, CLOSED T10P prints
  1466->1472 +6, C guards singleton 553->555 +2 / range
  504->508 +4 (5-count C-vs-py offset pre-existing,
  unchanged), seal 1560->1566 +6: all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-628-q775
  verdict CONFIRM (36/37 + section-F verdict as-filed;
  section heads shape 12/12 + quad/ring 11/12 +
  counters 11/11 quoted verbatim - heads sum 34 of 35,
  verdict line reads 36/37 as-filed: memo arithmetic
  quirk +2/+2, immaterial, same standing class; b19
  ADD/XOR 64/64 tie staged ADD per b19-family precedent;
  r1/r2 tail-share corrected to 2B per §F; tier cut
  SAFE; exact-value corroboration incl split/sandwich
  maps, MID-pair, ring edges + consts re-checked above)
  + A-327 (all 3 legs CONFIRM, 348-cell bed + P262T ref
  + P264 window, consts 74/66/64/71 INCL; its "r1/r2
  share 3B 362ebe" prose line contradicted first-hand -
  values both memos quote show last3B 362ebe/372ebe
  differ, 2B only; section-F stands; code stages full
  4B QT exact + comment states "share 2B" both sides -
  code follows section-F). No CONFIRM-P263 file; A-628
  suffices per rule. Agrees with cport commit msg (PYID
  7711, RGRAM 15422).
- Quiz: no conflicting CLAIM/GATE/FLAG on b371. Newest
  PARENT-* is QNUM-15 (Q-block grants only, read, no
  gate impact); GATE cites QNUM-12: 1 immaterial
  staleness (3 behind, standing pattern). PROSE-01:
  every value above copied from own run output, GATE
  re-read before filing.
- Logs: NVME ws tmp/encode-viewer/r50/ (build371.log,
  pyid371.log, rgram371py/c.log, cmp371.py/.c,
  for371-old/-new.nums, pins371.names/.baseN,
  pass371.names, smoke371.log, tables371.log,
  tabaudit371.py, ownloop371.log/.py, numstat371.txt,
  cdiff371.txt, pydiff371.txt, added371.txt,
  sweepnorm371-c/py-add.txt).

Verdict: PASS. No RED. Code CORRECT; GATE CORRECT on code
(1 immaterial QNUM staleness). Ready for parent PV/merge.
