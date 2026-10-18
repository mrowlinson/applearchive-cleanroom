# PV-c56c1e6: parent-verify first-hand band139 + merged 71afeb0

Worktree tmp/wt-pv-c56c1e6 (detached @c56c1e6), TMPDIR=NVME
pv-c56c1e6/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-c56c1e6/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3486/3486 covered=3486/3486 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-c56c1e6 PASS-functional + VERIFY-c56c1e6 PASS +
  no covering FLAG (FLAG-* checked, none for c56c1e6).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-c56c1e6/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
