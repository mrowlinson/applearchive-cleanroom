# PV-c1cd305: parent-verify first-hand band153 + merged a6e18c4

Worktree tmp/wt-pv-c1cd305 (detached @c1cd305), TMPDIR=NVME
pv-c1cd305/work, binary + build on NVME.
- C-BUILD: cc -O2 -Wall -Wextra -std=c11 -I/opt/homebrew/opt/xz/include
  -o .../pv-c1cd305/build/rgramc rgramc.c rc=0, 0 warnings
  (build.log first-hand).
- RGRAMC-PYID 3656/3656 covered=3656/3656 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: git diff bfa3762..c1cd305 added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-c1cd305 PASS-functional + VERIFY-c1cd305 PASS +
  no covering FLAG (FLAG-* checked, none for c1cd305).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-c1cd305/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
