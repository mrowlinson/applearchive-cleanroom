# PV-6ac1af1: parent-verify first-hand (band47 T10P470..T10P47Q, n<=33184)

Worktree tmp/wt-pv-6ac1af1 (detached @6ac1af1,
HEAD verified 6ac1af1ec5060286757ad7266c0546528bb98e2c),
TMPDIR=NVME pv-6ac1af1, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-6ac1af1/build
  rgramc rc=0, 0 warnings (-O2 -Wall -Wextra -std=c11).
- RGRAMC-PYID 1976/1976 covered=1976/1976 GREEN, 0 FAIL
  (test_rgram_c.sh, RGRAMC=NVME bin, own corpus).
- RGRAM-GREEN via C: 3952 PASS, 0 FAIL
  (test_rgram.sh, RGRAM_BIN=NVME bin).
- RGRAM-GREEN via python: 3952 PASS, 0 FAIL
  (test_rgram.sh, default backend).
- SMOKE-GREEN: 6 PASS (aar+aea roundtrips), 0 FAIL.
- Wall: diff ba8c96d..6ac1af1 (rgramc.c only,
  +1082/-502) grep 0 hits (ghidra/hopper/ida-pro/
  mach-o/disasm/decompil/libcompression/dlopen/ctypes/
  dylib/vendor/__text/otool). PARENT-032 lane-diff scope.

verdict: PASS (all first-hand). NOT merged (parent merges
oldest-first). Worktree tmp/wt-pv-6ac1af1 kept for merge.
Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-6ac1af1/
(build.log, parity.log, rgram-c.log, rgram-py.log, smoke.log).
