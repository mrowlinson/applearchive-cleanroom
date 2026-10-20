# VERIFY-b33a4a49 b291 T10P183 pins 80421..80512 (1026 tiers): PASS

viewer-r30, first-hand, detached tree NVME tmp/encode-viewer/r30/
tree-b33a4a49 @b33a4a49 (base 460ddbd6), seat build build291/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2476712 B (GATE states no size; recorded).
- RGRAMC-PYID 5502/5502 covered=5502/5502 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11004/11004 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11004/11004 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11004/11004).
- PINS-RGRAM cell set-eq 11004/11004 (cmp-identical).
- PINS 11006 rows = 2 hdr + 11004, +32 vs base (10974).
  For-list +16 exactly: 80421 80422 80423 80430 80438
  80439 80440 80444 80448 80449 80464 80465 80481 80497
  80511 80512. 0 removed (== GATE; `; do` stripped).
- Own-loop 80421..80512 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (Covers b5 step @80512 last cell empirically.)
- Tables P183 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 75/75,
  BM 9/9, BC 71/71, M 16/16, QR 4/4, QT 4/4, QC 64/64
  (py-hex vs C-decimal normalized). Sigs first-hand:
  S0=ce020000, S1=ada10500, S2=aba10500 (table heads),
  A b0-3 AC=a81a5a00, B b0-3 BC=d5d00200 (const pairs;
  all == code comments).
- Dispatch by eye both impls, 6 tiers in order: S0
  n=80421 / S1 n=80422 singletons; A 80423-80438
  off=n-80423, mtab 7B b9/10/11/76-79; S2 n=80439
  singleton; B 80440-80448 off=n-80440, mtab 11B
  b13-19/80-83; Q 80449-80512 off=n-80449 m=off&15
  q=off>>4, M 7B b20-22/76-79, R 7B b13-19, T 4B
  b80-83; all paylen 84, raw lencode
  l16=((n<<1)|1)&0xFFFF b4/b5 (no special-case).
  C blocks carry T51336/41/46/61/66/82 py-line
  mirrors. Insert position exact both sides: after
  T10R180 close (py L51335 / C L140184), before
  T10R181 (n<=80768, base 80513; py L51405 / C L140346).
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1608 del / 2063 add
  (grep; numstat 2069/1608 == GATE raw), normalized
  del-uniq 1491 / add-uniq 1790 (GATE coarse 884/1002;
  verdict leg 0-missing agrees), del-subset-add 0 missing.
- Wall on band diff added lines (460ddbd6..b33a4a49, 2269
  grep-added lines; == GATE 2269 + 6 empty):
  vendor/disasm/depload/libcompression/CT-shim/shebang
  0 hits. Files: rgramc.c, rgram.py, test_rgram.sh
  (for-line 1/1), PINS (+32/+0). Py side purely additive.
- CONFIRM evidence: A-386-q380 T10P183 verdict CONFIRM
  32/32, no DISSENT (CONVERT-01 rule b; == GATE).
- GATE prose: CORRECT on every claimed value (build,
  counts, for-list, tables, guards, offsets, paylen,
  lencode formula, mtab byte lists).

Agrees with GATE-b33a4a49 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r30/
(*291* files).

Verdict: PASS. Ready for parent PV + merge.
