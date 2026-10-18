# PV-e53abca: parent-verify first-hand band156 (speculative; VERIFY on file, 155 ahead)

Worktree tmp/wt-pv-e53abca (detached @e53abca), TMPDIR=NVME
pv-e53abca/work, binary + build on NVME.
- C-BUILD: cc -O2 -Wall -Wextra -std=c11 -I/opt/homebrew/opt/xz/include
  -o .../pv-e53abca/build/rgramc rgramc.c rc=0, 0 warnings
  (build.log first-hand).
- RGRAMC-PYID 3694/3694 covered=3694/3694 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: git diff 827a4ba..e53abca added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-e53abca PASS-functional + VERIFY-e53abca PASS +
  no covering FLAG (FLAG-* checked, none for e53abca).
- Merge BLOCKED on oldest-first (153/154/155 ahead).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-e53abca/
Verdict: PASS. Merge: --no-ff under merge.lock.d when green.
