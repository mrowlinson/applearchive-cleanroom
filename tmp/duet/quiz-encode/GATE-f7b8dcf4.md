# GATE f7b8dcf4 b293 T10P185 pins 81117..81208 (1038 tiers) PASS-functional

Seat sweep-r34, first-hand, WT tmp/wt-encode-sweep @f7b8dcf4,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r34.
Band = f8c9a084 (py merge w2b@106837b1 partial, +6 tiers +32 pins)
+ f7b8dcf4 (C port). Base 1666aa09 (b292 C tip, EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build293/{aae,rgramc}, rc=0, 0 warnings.
- RGRAMC-PYID 5534/5534 covered=5534/5534 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11068/11068 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11068/11068 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (11068/11068).
- PINS-RGRAM cells set-eq 11068/11068 (diff 0 lines).
- PINS 11070 rows (2 hdr + 11068, +32 vs base). py diff
  +173/0 (pure P185 addition). For-list union +16 (81117
  81118 81119 81126 81134 81135 81136 81140 81144 81145
  81160 81161 81177 81193 81207 81208), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P185 C-vs-py, all 11 EXACT: S0/S1/S2 const
  strings EXACT (168 hex chars each); AM 16/16, BM 9/9,
  M 16/16, QR 4/4, QT 4/4 EXACT; AC 75/75, BC 70/70,
  QC 63/63 EXACT (py-hex vs C-decimal normalized).
  Dispatch verified by eye both sides, all 6 tiers:
  P1850 n==81117 / P1851 n==81118 / P1852 n==81135
  singleton-const; P185A 81119..81134 off=n-81119;
  P185B 81136..81144 off=n-81136; P185Q 81145..81208
  off=n-81145 m=off&15 q=off>>4; all paylen 84, raw
  lencode l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF
  pay5=l16>>8; mtab bytes A:b48-50/76-79 (7B),
  B:b35/45-51/80-83 (12B), Q:M b6-8/76-79 +
  QR b35/45-51 (rb8) + QT b80-83.
- C diff renumber-only + new: raw 1571 del / 2032 add;
  normalized ([0-9]+ -> N) del-subset-add
  0 missing (del-uniq 894, add-uniq 1015).
- Wall on band diff added lines (scope 1666aa09..f7b8dcf4,
  2232 added lines + 6 empty): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits,
  CT-shim/shebang 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-393-q390
  T10P185 CONFIRM all, 31/31 checks. Agrees with
  cport commit msg (py/C 11068, PYID 5534).
- Quiz: no conflicting CLAIM/GATE/FLAG on b293/f7b8dcf4.
  b292 EVEN = sweep2 turf, used as diff-base only, NOT gated.
- Logs: NVME ws tmp/encode-sweep/r34/ (*293* files:
  build293.log, pyid293, rgram293py/c, pass293py/c,
  pins293-cells, rgram293-cells, seteq293.diff,
  for293-old/new, smoke293, tables293.log, tabaudit293.py,
  cdiff293.txt/-del-norm/-add-norm/-missing,
  banddiff293.txt/.stat, added293.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
