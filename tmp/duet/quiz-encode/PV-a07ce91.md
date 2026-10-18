# PV-a07ce91: parent-verify first-hand (band66 T10P60+T10R59, n<=37964)

Worktree tmp/wt-pv-a07ce91 (detached @a07ce91), TMPDIR=NVME pv-a07ce91,
seat-private BUILDDIR pv-a07ce91/build. Shared build/aae untouched.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-a07ce91/build rgramc
  rc=0, 0 warnings/errors. Log: NVME.../pv-a07ce91/build.log
- RGRAMC-PYID 2246/2246 covered=2246/2246
  RGRAMC-GREEN, 0 FAIL, rc=0. Log: NVME.../pv-a07ce91/rgramc.log (full, 2 lines: no per-N PASS by script design)
- RGRAM-GREEN via C (RGRAM_BIN=rgramc): 4492 PASS / 0 FAIL, rc=0.
  Log: NVME.../pv-a07ce91/rgram-c.log (full 4496 lines)
- RGRAM-GREEN via python: 4492 PASS / 0 FAIL, rc=0.
  Log: NVME.../pv-a07ce91/rgram-py.log (full 4496 lines)
- SMOKE-GREEN (6 PASS), rc=0. Log: NVME.../pv-a07ce91/smoke.log
- Wall: d22cdc1..a07ce91 (src/c/rgramc.c only, 5805 diff lines)
  vendor/disasm grep 0 hits; added-line abspath/sub_XXX grep 0 hits.
  Diff: NVME.../pv-a07ce91/lane.diff
- VERDICT: PV-PASS. Worktree kept for parent merge (oldest-first).
