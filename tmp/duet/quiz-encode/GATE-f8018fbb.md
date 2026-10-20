# GATE f8018fbb b283 T10R184 n<=81812 (998 tiers) PASS-functional

Seat sweep-r32, first-hand, WT tmp/wt-encode-sweep @f8018fbb,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r32.
Band = 418a64a4 (py merge w2@ba761356 partial, +2 tiers +24 pins)
+ f8018fbb (C port). Base 9074c987 (b282 C tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build283/{aae,rgramc}, rc=0, 0 warnings.
- RGRAMC-PYID 5394/5394 covered=5394/5394 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 10788/10788 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 10788/10788 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 10788/10788).
- PINS-RGRAM cells set-eq 10788/10788 (diff 0 lines).
- PINS 10790 rows (2 hdr + 10788, +24 vs base). py diff
  +71/0 (pure R184 addition). For-list union +12 (81557
  81558 81663 81664 81677 81741 81791 81792 81797 81805
  81811 81812), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit R184 C-vs-py: M 16/16, Q 16/16, C 68/68 EXACT.
  Dispatch verified by eye both sides: ceiling 81812, base
  81557, paylen 84, b45 0x2b=43/0x7d=125 thr 107/235,
  m bytes 32/33/34/76-79, q bytes 24/25/26/72-75.
- C diff renumber-only + new: raw 1373 del / 1531 add;
  normalized (_t/_i/_b/T numbers) del-subset-add 0 missing
  (del-uniq 1370, add-uniq 1517).
- Wall on band diff added lines (scope 9074c987..f8018fbb,
  1625 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  shebang 0. Files touched: rgramc.c, rgram.py,
  test_rgram.sh (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule a+b): CONFIRM-R184.md
  PASS 16/16 + A-396-q391r184 (file present). Sig f51af502.
  Agrees with cport commit msg (M/Q/C via py/C 10788,
  PYID 5394).
- Quiz: no conflicting CLAIM/GATE/FLAG on b283/f8018fbb
  (FLAG hits all old/unrelated).
- Logs: NVME ws tmp/encode-sweep/r32/ (build283.log,
  pyid283, rgram283py/c, pass283py/c, pins283-cells,
  rgram283-cells, seteq283.diff, for283-old/new, smoke283,
  tables283.log, cdiff283.txt, banddiff283.txt/.stat,
  added283.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
