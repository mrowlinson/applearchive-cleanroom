# PV-cf2775e: parent-verify first-hand band150 + merged 9596693

Worktree tmp/wt-pv-cf2775e (detached @cf2775e), TMPDIR=NVME
pv-cf2775e/work, binary + build on NVME.
- C-BUILD: cc -O2 -Wall -Wextra -std=c11 -I/opt/homebrew/opt/xz/include
  -o .../pv-cf2775e/build/rgramc rgramc.c rc=0 (build.log first-hand).
- RGRAMC-PYID 3619/3619 covered=3619/3619 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: git diff 56782d2..cf2775e added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-cf2775e PASS-functional + VERIFY-cf2775e PASS +
  no covering FLAG (FLAG-* checked, none for cf2775e).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-cf2775e/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
