# VERIFY-1666aa09 b292 T10P184 pins 80769..80860 (1032 tiers): PASS

viewer-r30, first-hand, detached tree NVME tmp/encode-viewer/r30/
tree-1666aa09 @1666aa09 (base b33a4a49), seat build build292/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2477032 B, sha256 rgramc c4c1b40d / aae d6e27c97
  (== GATE exact).
- RGRAMC-PYID 5518/5518 covered=5518/5518 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11036/11036 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11036/11036 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11036/11036).
- PINS-RGRAM cell set-eq 11036/11036 (cmp-identical).
  (GATE's "5518/5518" is N-set method = half the cells;
  cell-level set-eq is full 11036. Method note, not FAIL.)
- PINS 11038 rows = 2 hdr + 11036, +32 vs base (11006).
  For-list +16 exactly: 80769 80770 80771 80778 80786
  80787 80788 80792 80796 80797 80812 80813 80829 80845
  80859 80860. 0 removed (== GATE; `; do` stripped).
- Own-loop 80769..80860 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (No 0-mod-128 N inside; no step to cover.)
- Tables P184 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 74/74,
  BM 9/9, BC 71/71, M 16/16, QR 4/4, QT 4/4, QC 65/65
  (py-hex vs C-decimal normalized). C _N decls 74/71/65
  match actual (== GATE). Sigs first-hand: S0=d0020000,
  S1=9f340400, S2=9f340400 (== S1, SING-echoes-PB1),
  A b0-3 AC=9f345800 (== GATE); BC/QC lack b0 const
  (per-N sig bytes in mtab, consistent with MID9 /
  quad design).
- Dispatch by eye both impls, 6 tiers in order: S0
  n=80769 / S1 n=80770 singletons; A 80771-80786
  off=n-80771, mtab 8B b32-35/76-79; S2 n=80787
  singleton; B 80788-80796 off=n-80788, mtab 11B
  b0/1/30/31/36-38/80-83; Q 80797-80860 off=n-80797
  m=off&15 q=off>>4, M 6B b36/37/76-79, R 7B
  b22/23/30-34, T 4B b80-83; all paylen 84, raw
  lencode b4/b5 (no special-case). C blocks carry
  T51529/34/39/54/59/75 py-line mirrors (== GATE).
  Insert position exact both sides: after T10R181 close
  (py L51528 / C L140693), before T10R182 (n<=81116,
  base 80861; py L51598 / C L140855). (== GATE.)
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1589 del / 2044 add
  (grep; numstat 2050/1589 == GATE raw), normalized
  del-uniq 1493 / add-uniq 1783 (== GATE exact),
  del-subset-add 0 missing.
- Wall on band diff added lines (b33a4a49..1666aa09, 2250
  grep-added lines; == GATE): vendor/disasm/depload/
  libcompression/shebang 0 hits. Files: rgramc.c,
  rgram.py, test_rgram.sh (for-line 1/1), PINS (+32/+0).
  Py side purely additive.
- CONFIRM evidence: A-390-q381p184 verdict CONFIRM 26/26,
  no DISSENT (CONVERT-01 rule b; == GATE). A-390 also
  confirms NO b5 step in range (flip census empty).
- GATE prose: CORRECT on every claimed value (build+sha,
  counts, for-list, tables, _N decls, guards, sigs,
  mtab byte lists, T-mirrors, insert position, R182
  ceiling/base, b5=0x77 no-step).

Agrees with GATE-1666aa09 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r30/
(*292* files).

Verdict: PASS. Ready for parent PV + merge.
