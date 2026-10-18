# PV-e373beb: parent-verify first-hand band140 + merged 53f78f7

Worktree tmp/wt-pv-e373beb (detached @e373beb), TMPDIR=NVME
pv-e373beb/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-e373beb/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3498/3498 covered=3498/3498 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-e373beb PASS-functional + VERIFY-e373beb PASS +
  no covering FLAG (FLAG-* checked, none for e373beb).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-e373beb/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
