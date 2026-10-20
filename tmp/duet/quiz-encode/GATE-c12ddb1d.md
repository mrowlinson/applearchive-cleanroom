# GATE c12ddb1d b280 T10R181 n<=80768 (992 tiers) PASS-functional

Seat sweep2-r32, first-hand, WT tmp/wt-encode-sweep2 @c12ddb1d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r32.
Band = 44415f62 (py merge w2@8091ee2d partial, +2 tiers +24 pins)
+ c12ddb1d (C port). Base 240aa3dd.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build280/{aae,rgramc}, rc=0, 0 warnings.
- RGRAMC-PYID 5358/5358 covered=5358/5358 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 10716/10716 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 10716/10716 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 10716/10716).
- PINS-RGRAM cells set-eq 5358/5358 (diff 0); PINS 10718
  rows (2 hdr + 10716 = PASS lines). For-list union +12
  (80513 80514 80576 80639 80640 80653 80703 80717 80743
  80753 80767 80768), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit R181 C-vs-py: M 16/16, Q 16/16, C 67/67 EXACT.
  b45 line verified by eye (0x3c=60 both sides).
- C diff renumber-only + new: raw 1370 del / 1529 add;
  normalized (_t/_i/_b/T numbers) del-subset-add 0 missing
  (del-uniq 1367, add-uniq 1516).
- Wall on band diff added lines (scope 240aa3dd..c12ddb1d,
  1625 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh (for-line),
  PINS. Py side purely additive (+71/+1/-1/+24).
- CONFIRM evidence (CONVERT-01 rule a+b): CONFIRM-R181.md
  PASS 16/16 + A-389-q381 CONFIRM all 16/16 (file present,
  counts verified). Agrees with cport NOTE-cport-band280
  (M/Q/C 16/16/67, py/C 10716, PYID 5358).
- Quiz: no conflicting CLAIM/GATE/FLAG on b280 (mentions in
  viewer/sweep/cport NOTEs are coordination-only; PRE-*
  grep hits = substring false positives).
- Logs: NVME ws tmp/encode-sweep2/r32/ (build280.log,
  pyid280, rgram280py/c, cmp280, seteq280, for280-old/new,
  smoke280, tables280.py/.log, cdiff280, del/addnorm280,
  banddiff280, added280, wall280, depload280).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
