# VERIFY-460ddbd6 b290 T10P182 pins 80073..80164 (1020 tiers): PASS

viewer-r29, first-hand, detached tree NVME tmp/encode-viewer/r29/
tree-460ddbd6 @460ddbd6 (base e300bc17), seat build build290/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2459928 B (GATE states sha256 only; recorded).
- RGRAMC-PYID 5486/5486 covered=5486/5486 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10972/10972 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10972/10972 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10972/10972).
- PINS-RGRAM cell set-eq 10972/10972 (cmp-identical).
  (GATE's "5486/5486" is N-set method = half the cells;
  cell-level set-eq is full 10972. Method note, not FAIL.)
- PINS 10974 rows = 2 hdr + 10972, +32 vs base (10942).
  For-list +16 exactly: 80073 80074 80075 80082 80090
  80091 80092 80096 80100 80101 80117 80127 80128 80133
  80149 80164. 0 removed (== GATE; `; do` stripped).
- Own-loop 80073..80164 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (Covers b5 step @80128 empirically; 6 tiers contiguous.)
- Tables P182 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 74/74,
  BM 9/9, BC 70/70, M 16/16, QR 4/4, QT 4/4, QC 62/62
  (py-hex vs C-decimal normalized). Sigs first-hand:
  S0=ce020000, S1=274f0400, S2=274f0400 (== S1,
  sig-echoes-PB1 ✓), A b0-3 AC=274f4c00, B b0-3
  BC=bf5b0200 (== GATE).
- Dispatch by eye both impls, 6 tiers in order: S0
  n=80073 / S1 n=80074 singletons; A 80075-80090
  off=n-80075, mtab 8B b34/35/42/43/76-79; S2 n=80091
  singleton; B 80092-80100 off=n-80092, mtab 12B
  b34/35/41-46/80-83; Q 80101-80164 off=n-80101
  m=off&15 q=off>>4, M 8B b48-51/76-79, R 8B
  b34/35/41-46, T 4B b80-83; all paylen 84, raw
  lencode b4/b5 (no special-case; step @80128 emergent,
  own-loop green through it). C arrays/sizes exact.
  Insert position exact both sides: after T10R179 close
  (py L51140 / C L139667), before T10R180 (n<=80420,
  base 80165; py L51212 / C L139837).
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1628 del / 2083 add
  (grep; numstat 2089/1628 == GATE raw), normalized
  del-uniq 1495 / add-uniq 1778 (GATE 1495/1779, +1 =
  blank line), del-subset-add 0 missing.
- Wall on band diff added lines (e300bc17..460ddbd6, 2289
  grep-added lines; GATE cites 2295 = numstat total):
  vendor/disasm/depload/libcompression 0 hits. Files:
  rgramc.c (+173/+0), rgram.py, test_rgram.sh (for-line
  1/1), PINS (+32/+0). Py side purely additive.
- CONFIRM evidence: CONFIRM-P182.md PASS 28/28 +
  A-388-q379p182 verdict CONFIRM 28/28 (CONVERT-01 a+b).
- GATE prose: CORRECT on every claimed value (guards,
  sigs, widths, byte lists, insert position, R180
  ceiling/base).

Agrees with GATE-460ddbd6 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r29/
(*290* files).

Verdict: PASS. Ready for parent PV + merge.
