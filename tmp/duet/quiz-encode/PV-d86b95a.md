# PV-d86b95a: parent-verify first-hand band141 + merged 4873497

Worktree tmp/wt-pv-d86b95a (detached @d86b95a), TMPDIR=NVME
pv-d86b95a/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-d86b95a/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3510/3510 covered=3510/3510 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-d86b95a PASS-functional + VERIFY-d86b95a PASS +
  no covering FLAG (FLAG-* checked, none for d86b95a).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-d86b95a/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
