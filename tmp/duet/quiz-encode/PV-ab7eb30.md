# PV-ab7eb30: parent-verify first-hand band135 + merged 986b3cc

Worktree tmp/wt-pv-ab7eb30 (detached @ab7eb30), TMPDIR=NVME
pv-ab7eb30/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-ab7eb30/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3436/3436 covered=3436/3436 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-ab7eb30 PASS-functional + VERIFY-ab7eb30 PASS +
  no covering FLAG (FLAG-* checked, none for ab7eb30).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ab7eb30/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
