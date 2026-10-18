# PV-68d2eef: parent-verify first-hand band125 + merged ff65446

Battery run ON MBP (pv-band-remote.sh), tree from git archive,
ALL data on NVME-1 (Thunderbolt), TMPDIR=$SEAT. Logs grepped
locally first-hand from the share.
- C-BUILD: make -C src/c BUILDDIR=.../pv-remote-68d2eef/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3313/3313 covered=3313/3313 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: vs-master rgramc.c added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-68d2eef PASS-functional + VERIFY-68d2eef PASS +
  no covering FLAG (FLAG-* checked, none for 68d2eef).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.
- NOTE: first fully-GREEN remote run (3 prior remotes
  spurious C-RED, all overruled by local GREENs). Remote
  flakiness causes false REDs only; a full GREEN = genuine.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-remote-68d2eef/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
