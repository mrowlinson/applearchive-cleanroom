# PV-8ecae82: parent-verify first-hand band132 + merged 01632e3

Worktree tmp/wt-pv-8ecae82 (detached @8ecae82), TMPDIR=NVME
pv-8ecae82/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-8ecae82/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3400/3400 covered=3400/3400 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-8ecae82 PASS-functional + VERIFY-8ecae82 PASS +
  no covering FLAG (FLAG-* checked, none for 8ecae82).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-8ecae82/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
