# PV-fd438da: parent-verify first-hand band147 + merged 0fc5df4

Worktree tmp/wt-pv-fd438da (detached @fd438da), TMPDIR=NVME
pv-fd438da/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-fd438da/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3583/3583 covered=3583/3583 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-fd438da PASS-functional + VERIFY-fd438da PASS +
  no covering FLAG (FLAG-* checked, none for fd438da).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-fd438da/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
