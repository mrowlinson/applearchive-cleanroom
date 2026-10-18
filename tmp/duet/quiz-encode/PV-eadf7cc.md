# PV-eadf7cc: parent-verify first-hand band106 + merged e41a484

Worktree tmp/wt-pv-eadf7cc (detached @eadf7cc), TMPDIR=NVME
pv-eadf7cc/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-eadf7cc/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3043/3043 covered=3043/3043 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (6086 pins, test_rgram.sh). SMOKE-GREEN (smoke.sh 6/6).
- Wall: lane.diff (rgramc.c only) added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-eadf7cc PASS-functional + VERIFY-eadf7cc PASS +
  no covering FLAG (FLAG-* checked, none for eadf7cc).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-eadf7cc/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
