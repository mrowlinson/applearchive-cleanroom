# VERIFY-e59e5d25 b375 T10P267 pins 109653..110000 (1590 tiers) PASS

Seat viewer-r51, first-hand, detached tree-e59e5d25 @e59e5d25,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r51.
Base 26cd06b5 (b374, 1584 tiers). Band = 444de119 (py merge
w2b@aa2a6a60 partial, +6 tiers, +62 pins) + e59e5d25 (C port,
1590 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build375/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 1ea26863 / aae 7d8dd3a2 +
  sha256 rgramc cc943172 / aae d6e27c97 (== GATE all 4;
  aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 7835/7835 covered=7835/7835 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15670/15670 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15670/15670 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15670/15670 sorted).
- PINS 15672 rows (2 hdr + 15670, +62 vs base 15610);
  PASS-names vs PINS-names cmp-equal 15670/15670; base-N
  vs for-list cmp-equal 7835/7835. For-list delta vs base
  +31/-0: 109653 109654 109655 109656 109660 109665 109669
  109670 109671 109672 109674 109677 109679 109680 109681
  109688 109695 109696 109697 109712 109713 109728 109729
  109744 109745 109823 109824 109888 109951 109952 110000
  (2 sing + A6 offs 0,1,5,10,14,15 + C6 offs 0,1,3,6,8,9,
  offs 2,4,5,7 unsampled + Q10 head/row0-mid/step-triple/
  row-edge-pairs/tail offs 0,7,14/15/16,31/32,47/48,63 +
  R7 head/edge-pairs/mid/tail offs 0,78/79,143,206/207,
  255 == GATE decomposition; 7804->7835); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit375.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 84 PASS 0
  FAIL first run. Inventory exactly the 15 both sides
  (M42/X42 b42-family; no BM/BC, no M19, no QB/PT/FM).
  S0/S1 168ch sigs a0740300 ==P266PB0 REPEAT / 1d18e406
  NEW (both NEW strings, re-read vs base). AM 16x6B / CM
  10x11B / M 16x7B / M42 16x1B / X42 4x1B / QR 4x6B / QT
  4x4B / RM 16x8B / RQ 16x8B all C==py. AM/CM/M/RM/RQ
  all 16/16 or 10/10 distinct. 1SIG: CC b0-3 const
  1d18e406 (full sig const, == S1 sig); CM 10/10
  diverge. M42 values exact (66/e6/66/e6/66/66/66/e6/
  66/66/26/e6/66/e6/66/26, 3 distinct); X42
  [00,0f,0f,0f] EXACT. b42 XOR staged both sides (py
  pay[42]^int(X42[q]) vs M42[m]; C snprintf %02lx of
  pay[42]^hexval(X42[q]) vs M42[m]); ADD tie A=[0,3,3,3]
  flagged in Q-block comment both sides; memo A-644 +
  viewer A-331 both first-hand confirm XOR/ADD 64/64
  TIE (re-read). QR r1==r2==r3 LAST3-PAIRED
  bfdd8c6dd153 x3 (FIRST; r0 24dfb205518e distinct; 2
  distinct). QT 9e2c5289/71bf4a51/96bf4a51/bbbf4a51;
  r1/r2/r3 share TRUE 3B bf4a51 (first bytes 71/96/bb
  differ, exactly 3B); r0 last3B 2c5289 differs. RQ==M
  tails-only family: b76-79 same-index 16/16 + set-eq
  (M 7B vs RQ 8B widths differ; THIRD tails-only
  instance after P255/P263). AC/CC/QC/RC 76/71/64/70
  py-vs-C normalized; _N decls 76/71/64/70 match
  actual; sorted-unique. Missing-sets EXACT: AC-8
  [4,5,36,37,76-79]; CC-13 [4,5,36-42,80-83]; QC-20
  [4,5,34-43,76-83]; RC-18 [4,5,38,39,46,47,52-55,
  76-83]. RC b0-3 06000000; RC b84-87 de93eef2
  ring-wide. Tails SPLIT (RM b80-83 by COL / RQ b76-79
  by ROW, 16/16 distinct each, 0 overlap UNPAIRED).
  M-tails 16/16 ALL NEW vs P266T (overlap 0 vs P266
  RM/RQ tail union); M-full also ALL NEW vs P266RQ; QT
  4/4 NEW vs P266QT (b3327d33/ceb7d61f/f3b7d61f/23337d33
  re-read); RM ALL NEW vs P266RM. Memo INCL PBA 77 /
  C10 72 / quad 64 / T88 70 (A-644 re-read): impl
  76/71/64/70 = memo-1 on PBA/C10 (standing), identical
  quad/T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 109653 / S1 109654 / A 109655-670 / C 109671-680 /
  Q 109681-744 / R 109745-110000): bounds + paylens (84
  x92 / 88 x256) + lencode both sides (Q b5-step emerges
  from raw lencode) + R counter b4=(99+2off)&FF
  b5=89+(off>=79)+(off>=207) both sides (C 99/89 =
  0x63/0x59) + mtab/qtab/ttab byte positions exact (A
  6B b36,37,76-79; C 11B b36-42,80-83; Q 7/1/6/4B; R
  8/8B) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides. T-mirrors T73166/73171/73176/73191/73207/73232
  each re-read: hits the exact py guard line. Temps
  _t5640-5659 (base max _t5639, no reuse) + _b3422/
  3424/3426/3427/3428/3430/3431 (base max _b3420) +
  _i3423/3425/3429/3432 (base max _i3421, no reuse). C
  guards `if ((n) == (109653))` / `(109654)` + 4 ranges
  exact. Insert exact both sides: after T10P266R close,
  N-out-of-scope follows. Matches A-644/A-331 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop375.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache, 317 warmed; seat rgramc each):
  348/348 CLOSED. Census R256/Q64/A16/C10/S0/S1 exact.
  edges375.py: paylens 84 x92 + 88 x256; lencode 92/92
  (quad formula == raw-lencode 64/64 within); ring
  counter 256/256. S0/S1 ab/58 + ad/58 match raw
  lencode. A head af/58 tail cd/58 b5set {58}; C head
  cf/58 tail e1/58 b5set {58} NO carry; Q head e3/58,
  step 109695 (off14 ff/58) -> 109696 (off15 01/59) +
  109697 (off16 03/59), tail 61/59 (109744); ring head
  63/59, 109823 (off78 ff/59) -> 109824 (off79 01/5a);
  109951 (off206 ff/5a) -> 109952 (off207 01/5b); mid
  off143 (109888) 81/5a; tail 110000 (off255) 61/5b.
  Tail oracle sha c740e727a2eeba6c (== GATE prefix).
  Edge pins + tail 110000 in for-list + 2 PASS lines
  each py+C. No DISSENT: cut bytes verify.
- C diff pure-add: numstat 640/0 (rgramc.c) + 260/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 635 content + 5 bare-blank / 0 del; raw py 260
  content / 0 del. Sweep-family norm ([0-9]+ -> N,
  diff-sign strip, trailing-';' strip, python sets,
  keep-empty/no-lead-strip): C del-uniq 0 add-uniq 169
  EXACT, py del-uniq 0 add-uniq 187 EXACT (== GATE).
- Wall on band diff added lines (scope 26cd06b5..
  e59e5d25, 963 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 640/0, rgram.py 260/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-comments
  `# T10P` 1490->1496 +6, singletons 566->568 +2,
  range-guards 520->524 +4, CLOSED T10P prints
  1490->1496 +6, C guards singleton 561->563 +2 (5-
  count C-vs-py offset pre-existing, unchanged) +
  range 520->524 +4, seal 1584->1590 +6: all agree, no
  slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-644-q779-
  t10p267 verdict CONFIRM 39/39 (13+12+14 sums exact;
  file re-read; exact-value corroboration incl sigs,
  1SIG, M42/X42, QR last3, QT 3B-share, ring edges +
  thresholds re-checked above) + A-331 viewer
  corroboration (all 3 legs CONFIRM, consts 77/72/64/70
  INCL). No CONFIRM-P267.md file; A-644 suffices per
  rule. Agrees with cport commit msg (PYID 7835, RGRAM
  15670).
- Quiz: no conflicting CLAIM/GATE/FLAG on b375. Newest
  PARENT-* is QNUM-16 (w2d Q-block grant, read, no gate
  impact); GATE cites QNUM-13 (grants-only staleness,
  immaterial, standing pattern). PROSE-01: all hex/
  counts above copied from own run output.

Verdict: PASS. No RED. GATE CORRECT on code, 1 immaterial
prose staleness (QNUM-13 vs -16).
