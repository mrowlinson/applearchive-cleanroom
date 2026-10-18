# PV-eeb1ee5: parent-verify first-hand band110 + merged 0fa8d24

Worktree tmp/wt-pv-eeb1ee5 (detached @eeb1ee5), TMPDIR=NVME
pv-eeb1ee5/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-eeb1ee5/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3105/3105 covered=3105/3105 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (6210 pins, test_rgram.sh). SMOKE-GREEN (smoke.sh 6/6).
- Wall: lane.diff (rgramc.c only) added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-eeb1ee5 PASS-functional + VERIFY-eeb1ee5 PASS +
  no covering FLAG (FLAG-* checked, none for eeb1ee5).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-eeb1ee5/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
