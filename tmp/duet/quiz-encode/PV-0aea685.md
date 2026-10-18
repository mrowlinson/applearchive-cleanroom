# PV-0aea685: parent-verify first-hand band119 + merged 822d539

Worktree tmp/wt-pv-0aea685 (detached @0aea685), TMPDIR=NVME
pv-0aea685/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-0aea685/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3238/3238 covered=3238/3238 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-0aea685 PASS-functional + VERIFY-0aea685 PASS +
  no covering FLAG (FLAG-* checked, none for 0aea685).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.
- NOTE: MBP remote trial RED (C-legs, 1 FAIL) vs local
  3238/3238 — 3rd spurious remote C-RED; local rules.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-0aea685/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
