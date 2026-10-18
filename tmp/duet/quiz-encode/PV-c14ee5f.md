# PV-c14ee5f: parent-verify first-hand band130 + merged 65d909b

Worktree tmp/wt-pv-c14ee5f (detached @c14ee5f), TMPDIR=NVME
pv-c14ee5f/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-c14ee5f/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3375/3375 covered=3375/3375 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-c14ee5f PASS-functional + VERIFY-c14ee5f PASS +
  no covering FLAG (FLAG-* checked, none for c14ee5f).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-c14ee5f/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
