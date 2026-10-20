# VERIFY-f7b8dcf4 b293 T10P185 pins 81117..81208 (1038 tiers): PASS

viewer-r30, first-hand, detached tree NVME tmp/encode-viewer/r30/
tree-f7b8dcf4 @f7b8dcf4 (base 1666aa09), seat build build293/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2493816 B (GATE states no size; recorded).
- RGRAMC-PYID 5534/5534 covered=5534/5534 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11068/11068 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11068/11068 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11068/11068).
- PINS-RGRAM cell set-eq 11068/11068 (cmp-identical).
- PINS 11070 rows = 2 hdr + 11068, +32 vs base (11038).
  For-list +16 exactly: 81117 81118 81119 81126 81134
  81135 81136 81140 81144 81145 81160 81161 81177 81193
  81207 81208. 0 removed (== GATE; `; do` stripped).
- Own-loop 81117..81208 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (Covers b5 step @81152 empirically mid-range.)
- Tables P185 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 75/75,
  BM 9/9, BC 70/70, M 16/16, QR 4/4, QT 4/4, QC 63/63
  (py-hex vs C-decimal normalized). Sigs first-hand:
  S0=d0020000, S1=9b540200, S2=9f340400 (table heads),
  A b0-3 AC=9f342c00, B b0-3 BC=9b540300 (const pairs;
  all == code comments).
- Dispatch by eye both impls, 6 tiers in order: S0
  n=81117 / S1 n=81118 singletons; A 81119-81134
  off=n-81119, mtab 7B b48-50/76-79; S2 n=81135
  singleton; B 81136-81144 off=n-81136, mtab 12B
  b35/45-51/80-83; Q 81145-81208 off=n-81145 m=off&15
  q=off>>4, M 7B b6-8/76-79, R 8B b35/45-51, T 4B
  b80-83; all paylen 84, raw lencode
  l16=((n<<1)|1)&0xFFFF b4/b5 (no special-case; step
  @81152 emergent, own-loop green through it). C blocks
  carry T51722/27/32/47/52/68 py-line mirrors. Insert
  position exact both sides: after T10R182 close
  (py L51721 / C L141199), before T10R183 (n<=81464,
  base 81209; py L51791 / C L141363).
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1571 del / 2026 add
  (grep; numstat 2032/1571 == GATE raw), normalized
  del-uniq 1492 / add-uniq 1772 (GATE coarse 894/1015;
  verdict leg 0-missing agrees), del-subset-add 0 missing.
- Wall on band diff added lines (1666aa09..f7b8dcf4, 2232
  grep-added lines; == GATE 2232 + 6 empty):
  vendor/disasm/depload/libcompression/shebang 0 hits.
  Files: rgramc.c, rgram.py, test_rgram.sh (for-line
  1/1), PINS (+32/+0). Py side purely additive.
- CONFIRM evidence: A-393-q390 T10P185 verdict CONFIRM
  31/31, no DISSENT (CONVERT-01 rule b; == GATE).
- GATE prose: CORRECT on every claimed value (build,
  counts, for-list, tables, guards, offsets, paylen,
  lencode formula, mtab byte lists).

Agrees with GATE-f7b8dcf4 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r30/
(*293* files).

Verdict: PASS. Ready for parent PV + merge.
