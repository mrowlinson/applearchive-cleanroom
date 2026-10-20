# GATE 240aa3dd b279 T10R180 n<=80420 (990 tiers) PASS-functional

Seat sweep-r31, first-hand, WT tmp/wt-encode-sweep @240aa3dd,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r31.
Band = fcc17a5e (py merge w2@ca1930d6 partial, +2 tiers +24 pins)
+ 240aa3dd (C port). Base f0b9436a.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build279/rgramc, rc=0, 0 warnings.
- RGRAMC-PYID 5346/5346 covered=5346/5346 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 10692/10692 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 10692/10692 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 10692/10692).
- PINS-RGRAM set-eq 10692/10692 (diff 0).
- PINS 10694 rows (2 hdr + 10692, +24 vs base). For-list
  union +12 (80165 80166 80255 80256 80269 80333 80383 80384
  80397 80405 80419 80420), 0 removed.
- SMOKE-GREEN rc=0 (aar+aea roundtrips all PASS).
- Tables audit R180 C-vs-py: M 16/16, Q 16/16, C 66/66 EXACT.
  b45 line verified by eye (0x4b=75, 0x72=114, off>=91/219).
- C diff renumber-only + new: 1369 del / 1527 add; normalized
  (_t/_i/_b/T numbers) del-subset-add 0 missing lines.
- Wall on band diff added lines (PARENT-032 scope
  f0b9436a..240aa3dd): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes) 0 hits. Files touched:
  rgramc.c, rgram.py, test_rgram.sh (for-line), fast-battery
  adds (from master per FASTBAT-01), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-387-q378r180
  (cport-cited, file present).
- Quiz: no conflicting CLAIM/GATE/FLAG on b279 (GATE-f501344
  hit = substring false positive 8b279aa).
- Logs: NVME ws tmp/encode-sweep/r31/ (pyid279, rgram279py/c,
  smoke279, wall279, depload279, tables279, cmp279, seteq,
  for-old/new, del/add-norm, build279/).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
