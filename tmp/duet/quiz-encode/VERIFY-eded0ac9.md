# VERIFY-eded0ac9 b367 T10P259 pins 106869..107216 (1542 tiers) PASS

Seat viewer-r49, first-hand, detached tree-eded0ac9 @eded0ac9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r49.
Base a961bc67 (b366, 1536 tiers). Band = 01e51667 (py) + eded0ac9 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build367/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings (empty stderr). sha1 rgramc c828c131 /
  aae 7d8dd3a2 + sha256 rgramc e2a5d825 / aae d6e27c97
  (== GATE all 4; aae pinned, band touches no aae sources
  per numstat).
- RGRAMC-PYID 7587/7587 covered=7587/7587 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15174/15174 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15174/15174 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15174/15174 sorted).
- PINS 15176 rows (2 hdr + 15174, +62 vs base); base-N
  set-eq 7587/7587 (cmp 0); PASS-names vs PINS-names
  cmp-equal 15174/15174. For-list delta vs base +31/-0:
  106869 106870 106871 106872 106877 106879 106880
  106886 106887 106888 106891 106893 106895 106896
  106897 106905 106912 106913 106928 106929 106937
  106944 106945 106960 106961 107007 107008 107089
  107135 107136 107216 (2 sing + A6 + B6 + Q10 + R7 ==
  GATE decomposition); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit367.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 128 PASS 0
  FAIL first run. C-vs-py EXACT all 15 (S0/S1 168ch sigs
  20370300 ==P258PB0 REPEAT NEW string / 05016206 NEW vs
  P258 20370300/f8416e06 re-read; AM 16x8B distinct; BM
  10x11B distinct single-sig; M 16x7B distinct; M42 16x1B
  4-valued {5f,df,9f,1f} low-nibble f; X42 [00,3e,05,09]
  EXACT; XOR-grid (M42^X42) 16 distinct 4x4 ==
  16/1a/1f/21/56/5a/5f/61/96/9a/9f/a1/d6/da/df/e1; QR
  4x6B UNPAIRED d7df932a3163/bc5c041831f7/8d5e1c80319e/
  605e2317914d; QT 4x4B distinct 5288342d/5ed4036f/
  fca81ac3/fa92adc7, all-pairs longest-common-suffix 0,
  last-2B all differ; RM/RQ 16x8B distinct; AC/BC/QC/RC
  74/71/64/70 pairs py-hex-vs-C-dec normalized). _N
  decls 74/71/64/70 match actual. Inventory exactly the
  15 (no CM/CC/QB/PT/FM either side). Missing-sets EXACT:
  AC-10 [4,5,36-39,76-79]; BC-13 [4,5,36-42,80-83] (b42
  IN M-range); QC-20 [4,5,34-43,76-83]; RC-18
  [4,5,38,39,46,47,52-55,76-83]. AC b0-3 e0921f7a NEW
  (P258AC b0-3 40811f74 re-read; P258QC b0-3 e0921f3a
  re-read = 3a->7a 1B-off, P258Q-adjacent confirmed);
  BC b0-3 05016206 == PB1 sig (S1 head re-read),
  single-sig const over all 10 rows; QC b0-3 e0921f7a
  == PBA sig. RC b0-3 06000000 == P252/P253/P256 RC b0-3
  (py all 3 + C P253/P256 re-read); RC b84-87 37634be0.
  M/RQ heads 16/16 + tails b76-79 16/16 same-index
  (middle M-b43 vs RQ-b46,47 differs; 7B vs 8B).
  RM[c]/RQ[r] UNPAIRED both sides, tails SPLIT col/row
  16/16 distinct each. M-tails 16 distinct, zero overlap
  vs P258RQ-tail set (P258RQ 6B re-read). QT 4/4 NEW vs
  P258QT (f2bc5daa/49f3db15/dab7ba8e/1469107b re-read).
  b42xor leg both sides (py `pay[42] ^ int(X42[q],16)`
  vs M42[m]; C snprintf %02lx of pay[42]^hexval(X42[q])
  vs M42[m]); ADD tie A=[0,02,fb,f7] documented in
  Q-block comment both sides; P251 same-XOR-formula
  precedent re-read (rgram.py:70438). Coverage unions
  exact (A 8+74+2=84, B 11+71+2=84, Q 7+1+6+4+64+2=84
  with b42, R 8+8+70+2=88; disjoint, b4/b5 in no const
  set; C _b positions == py all 7 legs; C _b var order
  3335/3337/3339/3340/3341/3343/3344). Memo INCL PBA 74
  / B10 72 / quad 65 / T88 70 (A-619/A-323 re-read):
  impl PBA/T88 identical, 71/64 = memo-1 on B10/quad
  (standing).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 106869 / S1 106870 / A 106871-886 / B 106887-896 /
  Q 106897-960 / R 106961-107216): bounds + paylens
  (84 x92 / 88 x256) + lencode/counter formulas exact
  incl R 0xa3/0x43/47/175 both sides (C 163/67/47/175).
  T-mirrors T71089/71094/71099/71114/71130/71155 each
  re-read: hits the exact py guard line (106869/106870/
  106871/106887/106897/106961). Temps _t5482-5501 (base
  max _t5481, no reuse) + _b3335/3337/3339/3340/3341/
  3343/3344 + _i3336/3338/3342/3345 (base max _b3333/
  _i3334, no reuse). C guards `if ((n) == (106869))` /
  `(106870)` + 4 ranges exact. Insert exact both sides:
  after T10P258R close, N-out-of-scope follows.
  Matches A-619/A-323 geometry (values re-checked in
  audit above; NO D dips).
- Edges own-loop ownloop367.py over ALL 348 tier Ns
  (fresh oracle bytes via ct-cache miss path,
  tool-identical -encode -a lzraven; 31 cache hits +
  317 fresh encodes; seat rgramc each): 348/348 CLOSED.
  A-carry ff/42->01/43 @106879->106880 single flip
  off8->9, 9+7 split verified (b5==42 x9, ==43 x7);
  A head ef/42 tail 0d/43 b5set {42,43}; B head 0f/43
  tail 21/43 b5set {43}; Q head 23/43 tail a1/43 b5set
  {43} NO carry; ring 107007 (off46 ff/43) -> 107008
  (off47 01/44); 107135 (off174 ff/44) -> 107136
  (off175 01/45); mid off128 (107089) a3/44; R head
  a3/43 tail a1/45 (off255). S0/S1 embedded b4/b5
  eb/42 + ed/42 match raw lencode. Edge pins + tail
  107216 in for-list + PASS py+C.
  pay[4:6]==LE16((n<<1)|1) 348/348 whole-tier incl 88B
  cells (ring 256/256). Paylens 84 x92 + 88 x256.
- C diff pure-add: numstat 640/0 (rgramc.c) + 260/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 635 content + 5 blank-only / 0 del; raw py 260
  content / 0 del. Normalized ([0-9]+ -> N, diff-sign
  strip, trailing-';' strip, python sets, keep-empty/
  no-lead-strip): C del-uniq 0 add-uniq 182, py del-uniq
  0 add-uniq 199, del-subset-add 0 missing - sweep
  family, EXACT. Band-level sole del = for-line churn.
- Wall on band diff added lines (963): vendor/disasm 0,
  depload 0, libcompression/compression_tool/aa/
  nominated/shim/ct-cache 0, shebang 0.
- Tiers: merge-msg +6, code 6 blocks, `# T10P` 1442->
  1448 +6, singletons `if n == ` 550->552 +2,
  range-guards `<= n <=` 488->492 +4, CLOSED T10P prints
  1442->1448 +6, C guards singleton 545->547 +2 / range
  488->492 +4 (5-count C-vs-py offset pre-existing,
  unchanged), seal 1536->1542 +6: all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-619-q771
  verdict CONFIRM (section heads shape 12/12 + quad/ring
  12/12 + counters 12/12 quoted verbatim as-filed;
  verdict line 37/37 as-filed - sections sum 36, memo
  arithmetic quirk, immaterial, same class as r48
  notes; b42 XOR/ADD 64/64 tie staged XOR per b42-family
  precedent P235/P243/P251; PBA carry 9+7 re-verified;
  tier cut SAFE; exact-value corroboration incl B10
  single-sig, XOR-grid + tie values, R6 4/4, QT tails,
  M-tails NEW, ring edges + consts re-checked above) +
  A-323 (all 3 legs CONFIRM, 348-cell bed + P258T ref +
  P260 window, consts 74/72/65/70 INCL). No CONFIRM-P259
  file; A-619 suffices per rule. Agrees with cport
  commit msg (py/C 15174, PYID 7587).
- Quiz: no conflicting CLAIM/GATE/FLAG on b367. Newest
  PARENT-* is QNUM-14 (grants only, read, no gate
  impact); GATE cites QNUM-12: 1 immaterial staleness
  (2 behind). PROSE-01: every value above copied from
  own run output, GATE re-read before filing.
- Logs: NVME ws tmp/encode-viewer/r49/ (build367.log,
  pyid367.log, rgram367py/c.log, cmp367.py/.c,
  for367(-old).nums, pins367.basen/.names, pass367.names,
  smoke367.log, tables367.log, tabaudit367.py,
  ownloop367.log/.py, banddiff367-py/-c.txt,
  base367-py/-c.txt, sweepnorm367-c/py-add.txt).

Verdict: PASS. No RED. Code CORRECT; GATE CORRECT on code
(1 immaterial QNUM staleness). Ready for parent PV/merge.
