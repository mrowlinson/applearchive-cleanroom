# PV-4fe183d: parent-verify first-hand band95 + merged 05d5000

Worktree tmp/wt-pv-4fe183d (detached @4fe183d), TMPDIR=NVME
pv-4fe183d/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-4fe183d/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 2789/2789 covered=2789/2789 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (5578 pins, test_rgram.sh). SMOKE-GREEN (smoke.sh 6/6).
- Wall: lane.diff (rgramc.c only, +1287/-724) added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-4fe183d PASS-functional + VERIFY-4fe183d PASS +
  no covering FLAG (FLAG-* checked, none for 4fe183d).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-4fe183d/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
