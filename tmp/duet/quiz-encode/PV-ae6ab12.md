# PV-ae6ab12: parent-verify first-hand (band64 T10R57+T10P59, n<=37296)

Worktree tmp/wt-pv-ae6ab12 (detached @ae6ab12), TMPDIR=NVME
pv-ae6ab12, seat-private build/aae paths (shared build/aae untouched).

- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-ae6ab12/build
  rgramc+aae rc=0, 0 warnings/errors.
- RGRAMC-PYID 2216/2216 covered=2216/2216
  RGRAMC-GREEN (FULL parity, 0 FAIL).
- RGRAM-GREEN via C (test_rgram.sh RGRAM_BIN=rgramc, 4432 PASS / 0 FAIL).
- RGRAM-GREEN via python (test_rgram.sh, 4432 PASS / 0 FAIL).
- SMOKE-GREEN (smoke.sh, 6 PASS).
- Wall: merge-base(42b1e16)..ae6ab12 grep 0 hits
  (pattern: vendor|disasm|ghidra|hopper|otool|objdump|__TEXT|
  /System/|_Private|dylib|ctypes|Binary Ninja|radare; lane.diff 7175 lines).

Logs (FULL, retained):
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ae6ab12/parity.log
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ae6ab12/rgram-c.log
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ae6ab12/rgram-py.log
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ae6ab12/smoke.log
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ae6ab12/build.log
- /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ae6ab12/lane.diff

## verdict: PASS (merge-ready, parent merges oldest-first; worktree kept)
