# GATE e300bc17 b289 T10P181 pins 79725..79816 (1014 tiers) PASS-functional

Seat sweep-r33, first-hand, WT tmp/wt-encode-sweep @e300bc17,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r33.
Band = 9f491791 (py merge w2b@da529c3c partial, +6 tiers +32 pins)
+ e300bc17 (C port). Base 965f4dd7 (b288 C tip, EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build289/{aae,rgramc}, rc=0, 0 warnings.
- RGRAMC-PYID 5470/5470 covered=5470/5470 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 10940/10940 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 10940/10940 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (10940/10940).
- PINS-RGRAM cells set-eq 10940/10940 (diff 0 lines).
- PINS 10942 rows (2 hdr + 10940, +32 vs base). py diff
  +173/0 (pure P181 addition). For-list union +16 (79725
  79726 79727 79734 79742 79743 79744 79748 79752 79753
  79768 79769 79784 79785 79801 79816), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P181 C-vs-py, all 11 EXACT: S0/S1/S2 const
  strings EXACT (168 hex chars each); AM 16/16, BM 9/9,
  M 16/16, QR 4/4, QT 4/4 EXACT; AC 75/75, BC 69/69,
  QC 62/62 EXACT (py-hex vs C-decimal normalized).
  Dispatch verified by eye both sides, all 6 tiers:
  P1810 n==79725 / P1811 n==79726 / P1812 n==79743
  singleton-const; P181A 79727..79742 off=n-79727;
  P181B 79744..79752 off=n-79744; P181Q 79753..79816
  off=n-79753 m=off&15 q=off>>4; all paylen 84, raw
  lencode l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF
  pay5=l16>>8; mtab bytes A:b20/26/27/76-79,
  B:b11/18/19/25-30/80-83 (13B), Q:M b32-35/76-79 +
  QR b20/21/25-30 + QT b80-83.
- C diff renumber-only + new: raw 2111 del / 2572 add;
  normalized (_t/_i/_b/T numbers, BSD-portable) del-subset-add
  0 missing (del-uniq 872, add-uniq 994).
- Wall on band diff added lines (scope 965f4dd7..e300bc17,
  2772 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule a+b): CONFIRM-P181.md
  PASS 36/36 + A-384-q378 (file present). Agrees with
  cport commit msg (py/C 10940, PYID 5470).
- Quiz: no conflicting CLAIM/GATE/FLAG on b289/e300bc17.
  b288 EVEN = sweep2 turf, used as diff-base only, NOT gated.
- Logs: NVME ws tmp/encode-sweep/r33/ (*289* files:
  build289.log, pyid289, rgram289py/c, pass289py/c,
  pins289-cells, rgram289-cells, seteq289.diff,
  for289-old/new, smoke289, tables289.log, t289-*-py/c,
  cdiff289.txt/-del-norm/-add-norm/-missing,
  banddiff289.txt/.stat, added289.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
