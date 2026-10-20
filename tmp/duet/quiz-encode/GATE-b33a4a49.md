# GATE b33a4a49 b291 T10P183 pins 80421..80512 (1026 tiers) PASS-functional

Seat sweep-r34, first-hand, WT tmp/wt-encode-sweep @b33a4a49,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r34.
Band = bde13aba (py merge w2b@939f1a79 partial, +6 tiers +32 pins)
+ b33a4a49 (C port). Base 460ddbd6 (b290 C tip, EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build291/{aae,rgramc}, rc=0, 0 warnings.
- RGRAMC-PYID 5502/5502 covered=5502/5502 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11004/11004 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11004/11004 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (11004/11004).
- PINS-RGRAM cells set-eq 11004/11004 (diff 0 lines).
- PINS 11006 rows (2 hdr + 11004, +32 vs base). py diff
  +173/0 (pure P183 addition). For-list union +16 (80421
  80422 80423 80430 80438 80439 80440 80444 80448 80449
  80464 80465 80481 80497 80511 80512), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P183 C-vs-py, all 11 EXACT: S0/S1/S2 const
  strings EXACT (168 hex chars each); AM 16/16, BM 9/9,
  M 16/16, QR 4/4, QT 4/4 EXACT; AC 75/75, BC 71/71,
  QC 64/64 EXACT (py-hex vs C-decimal normalized).
  Dispatch verified by eye both sides, all 6 tiers:
  P1830 n==80421 / P1831 n==80422 / P1832 n==80439
  singleton-const; P183A 80423..80438 off=n-80423;
  P183B 80440..80448 off=n-80440; P183Q 80449..80512
  off=n-80449 m=off&15 q=off>>4; all paylen 84, raw
  lencode l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF
  pay5=l16>>8; mtab bytes A:b9/10/11/76-79 (7B),
  B:b13-19/80-83 (11B), Q:M b20-22/76-79 +
  QR b13-19 + QT b80-83.
- C diff renumber-only + new: raw 1608 del / 2069 add;
  normalized ([0-9]+ -> N) del-subset-add
  0 missing (del-uniq 884, add-uniq 1002).
- Wall on band diff added lines (scope 460ddbd6..b33a4a49,
  2269 added lines + 6 empty): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  CT-shim/shebang 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-386-q380
  T10P183 CONFIRM all, 32/32 checks. Agrees with
  cport commit msg (py/C 11004, PYID 5502).
- Quiz: no conflicting CLAIM/GATE/FLAG on b291/b33a4a49.
  b290 EVEN = sweep2 turf, used as diff-base only, NOT gated.
- Logs: NVME ws tmp/encode-sweep/r34/ (*291* files:
  build291.log, pyid291, rgram291py/c, pass291py/c,
  pins291-cells, rgram291-cells, seteq291.diff,
  for291-old/new, smoke291, tables291.log, tabaudit291.py,
  cdiff291.txt/-del-norm/-add-norm/-missing, norm.py,
  banddiff291.txt/.stat, added291.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
