# VERIFY-e300bc17 b289 T10P181 pins 79725..79816 (1014 tiers): PASS

viewer-r29, first-hand, detached tree NVME tmp/encode-viewer/r29/
tree-e300bc17 @e300bc17 (base 965f4dd7), seat build build289/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01). FIRST P tier at verify.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2459640 B (GATE states no size; recorded).
- RGRAMC-PYID 5470/5470 covered=5470/5470 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10940/10940 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10940/10940 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10940/10940).
- PINS-RGRAM cell set-eq 10940/10940 (cmp-identical).
- PINS 10942 rows = 2 hdr + 10940, +32 vs base (10910).
  For-list +16 exactly: 79725 79726 79727 79734 79742
  79743 79744 79748 79752 79753 79768 79769 79784 79785
  79801 79816. 0 removed (== GATE).
- Own-loop 79725..79816 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (6 tiers cover every N contiguously: 0/1/A/2/B/Q.)
- Tables P181 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons; AM 16/16, BM 9/9, M 16/16,
  QR 4/4, QT 4/4; AC 75/75, BC 69/69, QC 62/62
  (py-hex vs C-decimal normalized). Sigs first-hand:
  S0=67010000, S1=68ce0200, S2=274f0400, A b0-3
  AC=2d882d00, B b0-3 BC=dfce0200 (== GATE).
- Dispatch by eye both impls, all 6 tiers: P1810 n==79725
  / P1811 n==79726 / P1812 n==79743 singleton-const;
  P181A 79727..79742 off=n-79727; P181B 79744..79752
  off=n-79744; P181Q 79753..79816 off=n-79753 m=off&15
  q=off>>4; all paylen 84, raw lencode l16=((n<<1)|1)
  &0xFFFF pay4=l16&0xFF pay5=l16>>8; A mtab 7B
  b20/26/27/76-79, B mtab 13B b11/18/19/25-30/80-83,
  Q M 8B b32-35/76-79 + QR 8B b20/21/25-30 + QT 4B
  b80-83. Position: after T10P180Q close, before R160
  catch-all region. C byte arrays/sizes exact.
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 2111 del / 2566 add
  (grep; numstat 2572/2111 == GATE raw; 6 blank-line
  delta), normalized del-uniq 1613 / add-uniq 1880,
  del-subset-add 0 missing. (GATE cites uniq 872/994 —
  coarser normalizer granularity; verdict leg agrees.)
- Wall on band diff added lines (965f4dd7..e300bc17, 2772
  grep-added lines == GATE 2772):
  vendor/disasm/depload/libcompression 0 hits. Files:
  rgramc.c, rgram.py, test_rgram.sh (for-line), PINS.
- CONFIRM evidence: CONFIRM-P181.md PASS 36/36 + A-384-q378
  (CONVERT-01 rule a+b).
- GATE prose: CORRECT on every claimed value (guards, sigs,
  byte lists, lencode, counts).

Agrees with GATE-e300bc17 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r29/
(*289* files).

Verdict: PASS. Ready for parent PV + merge.
