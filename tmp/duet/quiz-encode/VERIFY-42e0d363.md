# VERIFY-42e0d363 b281 T10R182 n<=81116 (994 tiers): PASS

viewer-r27, first-hand, detached tree NVME tmp/encode-viewer/r27/
tree-42e0d363 @42e0d363 (base c12ddb1d = b280 C tip, ungated),
seat build build281/rgramc, env CT shim + CT_CACHE_DIR
(CT-CACHE-01), fast batteries (FASTBAT-01). Self-contained tip
battery ahead of ungated b280 (b219-precedent).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2425752 B (GATE states no size; recorded, no cmp).
- RGRAMC-PYID 5370/5370 covered=5370/5370 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10740/10740 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10740/10740 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10740/10740).
- PINS-RGRAM set-eq 10740/10740 (cmp-identical).
- PINS 10742 rows = 2 hdr + 10740, +24 vs base (10718).
  For-list tail +12 exactly: 80861 80862 80895 80896 80909
  80973 81023 81024 81037 81101 81115 81116. 0 removed.
- Own-loop 80861..81116 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  256 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (First run used stale b279 binary path by script bug: all
  crc=2 scope-gated as expected; rerun with seat binary green.)
- Tables R182 C-vs-py mechanical: M 16/16, Q 16/16, C 68/68
  EXACT. Dispatch by eye both impls: ceiling 81116, base
  80861, pay4=(0xbb+2*off)&0xFF, pay5=0x77+(off>=35)+
  (off>=163), m bytes 23/35/42/43/76-79, q bytes 36/37/72-75.
- py diff pure R182 addition: 71 added / 0 removed (69
  non-blank + 2 separator blanks; GATE cites +69 non-blank).
- C diff 1530+/1371- renumber-only + new: normalized
  (_t/_i/_b/T numbers) del-subset-add 0 missing lines.
- Wall on band diff added lines (c12ddb1d..42e0d363, 1626
  lines, PARENT-032 scope): vendor/disasm/depload/
  libcompression 0 hits. Files: rgramc.c, rgram.py,
  test_rgram.sh (for-line), PINS.
- CONFIRM evidence: A-391-q382 (CONVERT-01 rule b, cited).

Agrees with GATE-42e0d363 (PASS-functional) on every leg.
Logs: NVME ws tmp/encode-viewer/r27/ (*281* files).

Verdict: PASS. Ready for parent PV + merge (behind b280 when
sweep2 gates it).
