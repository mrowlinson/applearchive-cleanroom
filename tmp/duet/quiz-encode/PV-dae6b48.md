# PV-dae6b48: parent-verify first-hand band152 + merged 216b6c6

Worktree tmp/wt-pv-dae6b48 (detached @dae6b48), TMPDIR=NVME
pv-dae6b48/work, binary + build on NVME.
- C-BUILD: cc -O2 -Wall -Wextra -std=c11 -I/opt/homebrew/opt/xz/include
  -o .../pv-dae6b48/build/rgramc rgramc.c rc=0, 0 warnings
  (build.log first-hand).
- RGRAMC-PYID 3644/3644 covered=3644/3644 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: git diff d497e00..dae6b48 added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-dae6b48 PASS-functional + VERIFY-dae6b48 PASS +
  no covering FLAG (FLAG-* checked, none for dae6b48).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-dae6b48/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
