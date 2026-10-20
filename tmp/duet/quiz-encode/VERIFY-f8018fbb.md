# VERIFY-f8018fbb b283 T10R184 n<=81812 (998 tiers): PASS

viewer-r28, first-hand, detached tree NVME tmp/encode-viewer/r28/
tree-f8018fbb @f8018fbb (base 9074c987), seat build build283/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2442424 B (GATE states no size; recorded, no cmp).
- RGRAMC-PYID 5394/5394 covered=5394/5394 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10788/10788 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10788/10788 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10788/10788).
- PINS-RGRAM set-eq 10788/10788 (cmp-identical).
- PINS 10790 rows = 2 hdr + 10788, +24 vs base (10766).
  For-list +12 exactly: 81557 81558 81663 81664 81677
  81741 81791 81792 81797 81805 81811 81812. 0 removed.
  (== GATE list; note: naive `tr ' ' '\n'` extraction drops
  the `;`-suffixed tail N on both sides — strip `; do` first.)
- Own-loop 81557..81812 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  256 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables R184 C-vs-py mechanical: M 16/16, Q 16/16, C 68/68
  EXACT. Dispatch by eye both impls: ceiling 81812, base
  81557, paylen 84, pay4=(0x2b+2*off)&0xFF, pay5=0x7d+
  (off>=107)+(off>=235), m bytes 32/33/34/76-79, q bytes
  24/25/26/72-75. C: 43/125/107/235 exact. GATE prose
  (0x2b=43/0x7d=125 thr 107/235, same byte lists) CORRECT
  this time — sweep-r32, no repeat of sweep2-r32 eye-errors.
- py diff pure addition: rgram.py +71/0, test_rgram.sh +1/-1,
  PINS +24/0.
- C diff 1531+/1373- renumber-only + new: normalized
  del-uniq 1370 / add-uniq 1517, del-subset-add 0 missing
  (matches GATE counts exactly; numstat says 1532+/1373-
  on rgramc.c — +1 is numstat method, grep 1531/1373 == GATE).
- Wall on band diff added lines (9074c987..f8018fbb, 1625
  lines, PARENT-032 scope): vendor/disasm/depload/
  libcompression 0 hits, shebang 0. Files: rgramc.c,
  rgram.py, test_rgram.sh (for-line), PINS.
- CONFIRM evidence: CONFIRM-R184.md PASS 16/16 + A-396-q391r184
  (CONVERT-01 rule a+b, cited; sig f51af502 == writer msg).

Agrees with GATE-f8018fbb (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r28/
(*283* files).

Verdict: PASS. Ready for parent PV + merge.
