# PV-19bea75: parent-verify first-hand band126 + merged a166753

Worktree tmp/wt-pv-19bea75 (detached @19bea75), TMPDIR=NVME
pv-19bea75/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-19bea75/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3325/3325 covered=3325/3325 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-19bea75 PASS-functional + VERIFY-19bea75 PASS +
  no covering FLAG (FLAG-* checked, none for 19bea75).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-19bea75/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
