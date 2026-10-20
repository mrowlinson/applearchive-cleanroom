# GATE 76eb8a9f b284 T10R185 n<=82160 (1000 tiers) PASS-functional

Seat sweep2-r33, first-hand, WT tmp/wt-encode-sweep2 @76eb8a9f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r33.
Band = 6433b733 (py merge w2@f23eef94 partial, +2 tiers +24 pins)
+ 76eb8a9f (C port). Base f8018fbb.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build284/{aae,rgramc}, rc=0, 0 warnings.
- RGRAMC-PYID 5406/5406 covered=5406/5406 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 10812/10812 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 10812/10812 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 10812/10812).
- PINS-RGRAM cells set-eq 5406/5406 (diff 0); PINS 10814
  rows (2 hdr + 10812 = PASS lines). For-list union +12
  (81905 81906 81919 81920 81933 81997 82047 82048 82061
  82145 82159 82160), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit R185 C-vs-py: M 16/16, Q 16/16, C 68/68 EXACT.
  b45 line verified by eye (0xd3=211 both sides).
- Dispatch eye-verified both sides: ceiling 82160, base 81905,
  paylen 84, b4 0xe3+2off, b5 0x7f+(off>=15)+(off>=143),
  M-tab 6B b48/b49/b72-75, Q-tab 8B b34/b35/b42/b43/b76-79
  (TAILS-SWAP roles, matches A-399).
- C diff renumber-only + new: raw 1374 del / 1533 add;
  normalized (_t/_i/_b/T numbers) del-subset-add 0 missing
  (del-uniq 1374, add-uniq 1523).
- Wall on band diff added lines (scope f8018fbb..76eb8a9f,
  1628 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh (for-line),
  PINS. Py side purely additive (+70/+1/-1/+24).
- CONFIRM evidence (CONVERT-01 rule a+b): CONFIRM-R185.md
  PASS 16/16 + A-399-q392r185 CONFIRM all 16/16 (file present,
  counts verified). Agrees with cport NOTE-cport-HANDOFF-r17
  (M/Q/C 16/16/68, py/C 10812, PYID 5406).
- Quiz: no conflicting CLAIM/GATE/FLAG on b284. No new
  PARENT-* (newest CONVERT-01; 075 viewer4-only).
- Logs: NVME ws tmp/encode-sweep2/r33/ (build284.log,
  pyid284, rgram284py/c, cmp284, seteq284, for284-old/new,
  smoke284, tables284.py/.log, cdiff284, del/addnorm284,
  banddiff284, added284, wall284, depload284).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
