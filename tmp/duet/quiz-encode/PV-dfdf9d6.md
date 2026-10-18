# PV-dfdf9d6: parent-verify first-hand band98 + merged fd995bd

Worktree tmp/wt-pv-dfdf9d6 (detached @dfdf9d6), TMPDIR=NVME
pv-dfdf9d6/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-dfdf9d6/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 2858/2858 covered=2858/2858 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (5716 pins, test_rgram.sh). SMOKE-GREEN (smoke.sh 6/6).
- Wall: lane.diff (rgramc.c only, +1333/-742) added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-dfdf9d6 PASS-functional + VERIFY-dfdf9d6 PASS +
  no covering FLAG (FLAG-* checked, none for dfdf9d6).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-dfdf9d6/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
