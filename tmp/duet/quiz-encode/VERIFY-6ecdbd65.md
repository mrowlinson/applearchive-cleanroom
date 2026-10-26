# VERIFY-6ecdbd65 b373 T10P265 pins 108957..109304 (1578 tiers) PASS

Seat viewer-r51, first-hand, detached tree-6ecdbd65 @6ecdbd65,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r51.
Base 7ad92845 (b372, 1572 tiers). Band = a079ddf3 (py merge
w2b@d55b9220 partial, +6 tiers, +62 pins) + 6ecdbd65 (C port,
1578 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build373/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 71d713b3 / aae 7d8dd3a2 +
  sha256 rgramc cc2beda7 / aae d6e27c97 (== GATE all 4;
  aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 7773/7773 covered=7773/7773 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15546/15546 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15546/15546 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15546/15546 sorted).
- PINS 15548 rows (2 hdr + 15546, +62 vs base 15486);
  PASS-names vs PINS-names cmp-equal 15546/15546; base-N
  vs for-list cmp-equal 7773/7773. For-list delta vs base
  +31/-0: 108957 108958 108959 108960 108964 108969 108973
  108974 108975 108978 108979 108980 108981 108982 108983
  108984 108985 109000 109001 109016 109017 109032 109033
  109048 109049 109052 109055 109056 109183 109184 109304
  (2 sing + A6 offs 0,1,5,10,14,15 + C8 offs 0,3-9, offs
  1,2 unsampled + Q8 offs 0,15/16,31/32,47/48,63 + R7
  offs 0,3,6/7,134/135,255 == GATE decomposition;
  7742->7773); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit373.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 81 PASS 0
  FAIL first run. Inventory exactly the 13 both sides
  (no BM/BC, no M19/XA19, no QB/PT/FM/M42/X42). S0/S1
  168ch sigs a0560300 NEW / bdcfaa06 ==P264S1 (both NEW
  strings, re-read vs base). AM 16x6B / CM 10x13B / M
  16x6B / QR 4x8B / QT 4x4B / RM 16x8B / RQ 16x6B all
  C==py. AM 16/16 distinct; CM 10/10 diverge; M 16/16
  distinct (heads 16-unique, tails 16-unique). 6SIG map
  exact: full-sig bdcfaa06 x4 offs 0-3 + bdcf7a06 +
  bdcffa04 + bdcf1a05 + bdcf3a05 + bdcf7a05 x2 offs 8-9
  (6 distinct; CC b0,b1 const bd,cf). QR r1==r2
  MID-PAIRED 5c52a392917ed792 x2; r0 59d2ffd8b1a56722 +
  r3 5792ce9eb1805f9a distinct; 3 distinct; sig-led
  59/5c/57 + QC b0-2 df/fb/ac (QUADms 3-sig
  dffbac59/5c/57). QT 473b6a01/c2fac80f/756b3610/
  652f4ee8; max pairwise common suffix 0 hex chars
  (last bytes 01/0f/10/e8 all differ) -- no shared
  suffix. RQ==M FULL-STRING 16/16 same-index (THIRD
  FULL instance after P261/P264; staging per precedent,
  NOT a finding). AC/CC/QC/RC 76/69/64/71 py-vs-C
  normalized; _N decls 76/69/64/71 match actual;
  sorted-unique. Missing-sets EXACT: AC-8
  [4,5,48,49,76-79]; CC-15 [2,3,4,5,35,46-51,80-83]
  (sig b2,b3 in tab); QC-20
  [3-7,35,46-51,76-83]; RC-17
  [0,4-7,9-11,20,76-83] (b0 split, b1-3 const 000000).
  RC b84-87 2032bed2 ring-wide. Tails SPLIT (RM b80-83
  by COL / RQ b76-79 by ROW, 16/16 distinct each, 0
  overlap UNPAIRED). M-tails 16/16 ALL NEW vs P264T
  (overlap 0 vs P264 RM/RQ tail union); M-full also ALL
  NEW vs P264RQ; QT 4/4 NEW vs P264QT
  (c37be99d/c0fadb1d/e5fadb1d/cb6a97b8 re-read); RM ALL
  NEW vs P264RM. Memo INCL PBA 77 / C10 70 / quad 65 /
  T88 71 (A-637 re-read): impl 76/69/64/71 = memo-1 on
  PBA/C10/quad (standing), identical T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 108957 / S1 108958 / A 108959-974 / C 108975-984 /
  Q 108985-109048 / R 109049-304): bounds +
  paylens (84 x92 / 88 x256) + lencode both sides + R
  counter b4=(243+2off)&FF b5=83+(off>=7)+(off>=135)
  both sides (C 243/83 = 0xF3/0x53) + b0split
  (0x05 iff c<3 else 0x04; C ternary ((c)<(3))?(5):(4)
  matches py) + mtab/qtab/ttab byte positions exact (A
  6B b48,49,76-79; C 13B b2,3,35,46-51,80-83; Q 6/8/4B;
  R 8/6B) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides. T-mirrors T72668/72673/72678/72693/72709/72732
  each re-read: hits the exact py guard line. Temps
  _t5604-5621 (base max _t5603, no reuse) + _b3400/
  3402/3404/3405/3406/3408/3409 (base max _b3398) +
  _i3401/3403/3407/3410 (base max _i3399, no reuse). C
  guards `if ((n) == (108957))` / `(108958)` + 4 ranges
  exact. Insert exact both sides: after T10P264R close,
  N-out-of-scope follows. Matches A-637/A-329 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop373.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; first run warmed 317 entries, rerun
  0 miss; seat rgramc each): 348/348 CLOSED. Census
  R256/Q64/A16/C10/S0/S1 exact. edges373.py: paylens 84
  x92 + 88 x256; lencode 92/92; ring counter 256/256;
  b0split 48x05+208x04 exact. S0/S1 3b/53 + 3d/53 match
  raw lencode. A head 3f/53 tail 5d/53 b5set {53}; C
  head 5f/53 tail 71/53 b5set {53} NO carry; Q head
  73/53 tail f1/53 b5set {53} NO carry; ring head
  f3/53, 109055 (off6 ff/53) -> 109056 (off7 01/54);
  109183 (off134 ff/54) -> 109184 (off135 01/55); mid
  off127 (109176) f1/54; tail 109304 (off255) f1/55.
  Tail oracle sha 393ae26963053f3e (== GATE prefix).
  Edge pins + tail 109304 in for-list + 2 PASS lines
  each py+C. No DISSENT: cut bytes verify.
- C diff pure-add: numstat 612/0 (rgramc.c) + 239/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 607 content + 5 bare-blank / 0 del; raw py 239
  content / 0 del. Sweep-family norm ([0-9]+ -> N,
  diff-sign strip, trailing-';' strip, python sets,
  keep-empty/no-lead-strip): C del-uniq 0 add-uniq 156
  EXACT, py del-uniq 0 add-uniq 177 EXACT (== GATE).
- Wall on band diff added lines (scope 7ad92845..
  6ecdbd65, 914 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 612/0, rgram.py 239/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-comments
  `# T10P` 1478->1484 +6, singletons 562->564 +2,
  range-guards 512->516 +4, CLOSED T10P prints
  1478->1484 +6, C guards singleton 557->559 +2 (5-
  count C-vs-py offset pre-existing, unchanged) +
  range 512->516 +4, seal 1572->1578 +6: all agree, no
  slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-637-q777-
  t10p265 verdict CONFIRM 37/37 (12+13+12 sums exact;
  file re-read; exact-value corroboration incl sigs,
  6SIG, QR pairing, QT no-suffix, b0split, ring edges +
  thresholds re-checked above) + A-329 viewer
  corroboration (all 3 legs CONFIRM). No CONFIRM-P265.md
  file; A-637 suffices per rule. Agrees with cport
  commit msg (PYID 7773, RGRAM 15546).
- Quiz: no conflicting CLAIM/GATE/FLAG on b373. Newest
  PARENT-* is QNUM-16 (w2d Q-block grant, read, no gate
  impact); GATE cites QNUM-13 (grants-only staleness,
  immaterial, standing pattern). PROSE-01: all hex/
  counts above copied from own run output.

Verdict: PASS. No RED. GATE CORRECT on code, 1 immaterial
prose staleness (QNUM-13 vs -16).
