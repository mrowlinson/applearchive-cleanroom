# PV-9e30e0b: parent-verify first-hand band123 + merged b2f23a4

Worktree tmp/wt-pv-9e30e0b (detached @9e30e0b), TMPDIR=NVME
pv-9e30e0b/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-9e30e0b/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3288/3288 covered=3288/3288 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-9e30e0b PASS-functional + VERIFY-9e30e0b PASS +
  no covering FLAG (FLAG-* checked, none for 9e30e0b).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-9e30e0b/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
