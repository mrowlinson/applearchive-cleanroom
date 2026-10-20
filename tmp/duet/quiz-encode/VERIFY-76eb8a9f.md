# VERIFY-76eb8a9f b284 T10R185 n<=82160 (1000 tiers): PASS

viewer-r28, first-hand, detached tree NVME tmp/encode-viewer/r28/
tree-76eb8a9f @76eb8a9f (base f8018fbb), seat build build284/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2442504 B (GATE states no size; recorded, no cmp).
- RGRAMC-PYID 5406/5406 covered=5406/5406 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10812/10812 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10812/10812 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10812/10812).
- PINS-RGRAM cell set-eq 10812/10812 (cmp-identical).
  (GATE's "5406/5406" is N-set method = half the cells;
  cell-level set-eq is full 10812. Method note, not FAIL.)
- PINS 10814 rows = 2 hdr + 10812, +24 vs base (10790).
  For-list +12 exactly: 81905 81906 81919 81920 81933
  81997 82047 82048 82061 82145 82159 82160. 0 removed
  (== GATE list).
- Own-loop 81905..82160 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  256 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables R185 C-vs-py mechanical: M 16/16, Q 16/16, C 68/68
  EXACT; M hexlen 12 (6B), Q hexlen 16 (8B) — TAILS-SWAP
  roles confirmed mechanically. Dispatch by eye both impls:
  ceiling 82160, base 81905, paylen 84, pay4=(0xe3+2*off)&
  0xFF, pay5=0x7f+(off>=15)+(off>=143), m 6B b48/b49/
  b72-75, q 8B b34/b35/b42/b43/b76-79. C: 227/127/15/143
  exact. TAILS-SWAP eye-verified per brief.
- py diff pure addition: rgram.py +70/0, test_rgram.sh +1/-1,
  PINS +24/0.
- C diff renumber-only + new: raw 1374 del / 1532 add (grep;
  numstat 1533/1374), normalized del-uniq 1371 / add-uniq
  1520, del-subset-add 0 missing. (GATE cites raw 1533 add,
  uniq 1374/1523 — normalizer/count granularity; verdict
  leg 0-missing agrees.)
- Wall on band diff added lines (f8018fbb..76eb8a9f, 1625
  grep-added lines; GATE cites 1628 = numstat total):
  vendor/disasm/depload/libcompression 0 hits. Files:
  rgramc.c, rgram.py, test_rgram.sh (for-line), PINS.
- CONFIRM evidence: CONFIRM-R185.md PASS 16/16 + A-399-q392r185
  (CONVERT-01 rule a+b; TAILS-SWAP tier per memo + DONE-R log).

OBSERVED (GATE prose error, NOT code FAIL): GATE-76eb8a9f line
23 says "b45 line verified by eye (0xd3=211 both sides)" but
first-hand both impls read pay4 base 0xe3=227 (py 0xe3, C 227)
with pay5 base 0x7f=127 thr 15/143, C-vs-py in exact agreement,
all 10812 cells + 256 own-loop Ns green. The GATE's own line 25
dispatch note (b4 0xe3+2off, b5 0x7f thr 15/143) is CORRECT —
line 23 contradicts it. Third sweep2 b45 eye-error in two rounds
(r32: b280 0x3c, b282 0x9d; r33: this). Code correct; parent may
want GATE correction + a word with sweep2 (eye-checks need
first-hand re-reads, as r27 already flagged).

Agrees with GATE-76eb8a9f (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r28/
(*284* files).

Verdict: PASS. Ready for parent PV + merge.
