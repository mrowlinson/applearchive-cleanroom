# VERIFY-015711bc b294 T10P186 pins 81465..81556 (1044 tiers): PASS

viewer-r30, first-hand, detached tree NVME tmp/encode-viewer/r30/
tree-015711bc @015711bc (base f7b8dcf4), seat build build294/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2494120 B, sha256 rgramc 420006a2 / aae d6e27c97
  (== GATE exact).
- RGRAMC-PYID 5550/5550 covered=5550/5550 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11100/11100 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11100/11100 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11100/11100).
- PINS-RGRAM cell set-eq 11100/11100 (cmp-identical).
  (GATE's "5550/5550" is N-set method = half the cells;
  for-list count 5550 confirmed; cell-level set-eq is
  full 11100. Method note, not FAIL.)
- PINS 11102 rows = 2 hdr + 11100, +32 vs base (11070).
  For-list +16 exactly: 81465 81466 81467 81474 81482
  81483 81484 81488 81492 81493 81509 81525 81535 81536
  81541 81556. 0 removed (== GATE; `; do` stripped).
- Own-loop 81465..81556 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (Covers b5 step @81536 empirically mid-range.)
- Tables P186 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 75/75,
  BM 9/9, BC 71/71, M 16/16, QR 4/4, QT 4/4, QC 63/63
  (py-hex vs C-decimal normalized). C _N decls 75/71/63
  match actual (== GATE). Sigs first-hand: S0=f6020000,
  S1=04f60200, S2=7d940500 (own, NEW), A b0-3
  AC=4d602f00, B b0-3 BC=04f60200 (== S1,
  PBB-echoes-PB1); QC lacks b0 const (multi-sig quad,
  sig bytes in rtab — consistent).
- Dispatch by eye both impls, 6 tiers in order: S0
  n=81465 / S1 n=81466 singletons; A 81467-81482
  off=n-81467, mtab 7B b20-22/76-79; S2 n=81483
  singleton; B 81484-81492 off=n-81484, mtab 11B
  b20-26/80-83; Q 81493-81556 off=n-81493 m=off&15
  q=off>>4, M 8B b20/21/26/27/76-79, R 7B
  b0/1/2/11/19/24/25, T 4B b80-83; all paylen 84, raw
  lencode b4/b5 (no special-case; step @81536 emergent,
  own-loop green through it). C blocks carry
  T51915/20/25/40/45/61 py-line mirrors (== GATE).
  Insert position exact both sides: after T10R183 close
  (py L51914 / C L141708), before T10R184 (n<=81812,
  base 81557; py L51984 / C L141871). (== GATE.)
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1553 del / 2008 add
  (grep; numstat 2014/1553 == GATE raw), normalized
  del-uniq 1491 / add-uniq 1756 (== GATE exact),
  del-subset-add 0 missing.
- Wall on band diff added lines (f7b8dcf4..015711bc, 2214
  grep-added lines; == GATE): vendor/disasm/depload/
  libcompression/shebang 0 hits. Files: rgramc.c,
  rgram.py, test_rgram.sh (for-line 1/1), PINS (+32/+0).
  Py side purely additive.
- CONFIRM evidence: A-395-q391p186 verdict CONFIRM 29/29,
  no DISSENT (CONVERT-01 rule b; == GATE).
- GATE prose: CORRECT on every claimed value (build+sha,
  counts, for-list, tables, _N decls, guards, sigs,
  mtab byte lists, T-mirrors, insert position, R184
  ceiling/base, flip [81536]).

Agrees with GATE-015711bc (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r30/
(*294* files).

Verdict: PASS. Ready for parent PV + merge.
