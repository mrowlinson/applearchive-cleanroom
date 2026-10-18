# PV-f8fc439 (band63 T10P58, n<=36948, 536 tiers) — PASS, ready to merge

Worktree tmp/wt-pv-f8fc439 (detached @f8fc4391cd4837cc4d747e7f6943b370e9fc9a0b, clean).
TMPDIR=/Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-f8fc439 for every run.
Seat-private build: $TMPDIR/build (aae + rgramc). Shared build/aae untouched.

- C-BUILD: make -C src/c BUILDDIR=$TMPDIR/build, rc=0, 0 warnings/errors
  (grep -ci "warning|error" build.log = 0).
- RGRAMC-PYID 2196/2196 covered=2196/2196
  RGRAMC-GREEN (tests/test_rgram_c.sh, RGRAMC=$TMPDIR/build/rgramc, rc=0).
- RGRAM-GREEN via C (RGRAM_BIN=$TMPDIR/build/rgramc): 4392 PASS / 0 FAIL, rc=0.
- RGRAM-GREEN via python (default RGRAM_BIN): 4392 PASS / 0 FAIL, rc=0.
- SMOKE-GREEN (tests/smoke.sh): 6 PASS (aar+aea cells), rc=0.

Wall: git diff eaed6ba..f8fc439 (src/c/rgramc.c only, +846/-568)
grep -iE "vendor|disasm|ghidra|hopper|otool|__text|/System/|sub_[0-9a-f]|ctypes|dylib|dlopen" = 0 hits.
No 0xADDR disasm markers in added lines. Wall-clean.

Logs (FULL, retained under /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-f8fc439/):
- build.log (6 lines), rgramc.log (PYID+GREEN), rgram-c.log (4396 lines, 4392 PASS),
  rgram-py.log (4396 lines, 4392 PASS), smoke.log (6 PASS + SMOKE-GREEN), lane.diff.

Verdict: PASS — all batteries first-hand GREEN, wall-clean. Do NOT remove
worktree (parent reuses for oldest-first merge).
