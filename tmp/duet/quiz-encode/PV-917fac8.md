# PV-917fac8: parent-verify first-hand band112 + merged 502bd35

Worktree tmp/wt-pv-917fac8 (detached @917fac8), TMPDIR=NVME
pv-917fac8/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-917fac8/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3132/3132 covered=3132/3132 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (6264 pins, test_rgram.sh). SMOKE-GREEN (smoke.sh 6/6).
- Wall: lane.diff (rgramc.c only) added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-917fac8 PASS-functional + VERIFY-917fac8 PASS +
  no covering FLAG (FLAG-* checked, none for 917fac8).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-917fac8/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
