# PV-8df33e4: parent-verify first-hand (band55 T10P52 n<=34860)

Worktree tmp/wt-pv-8df33e4 (detached @8df33e4), TMPDIR=NVME
pv-8df33e4 seat-private, build + binaries on NVME (shared build/aae untouched).
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-8df33e4/build
  aae + rgramc rc=0, 0 warnings.
- RGRAMC-PYID 2076/2076 covered=2076/2076
  RGRAMC-GREEN (tests/test_rgram_c.sh, FULL, 0 FAIL).
- RGRAM-GREEN via C (RGRAM_BIN=rgramc, 4152 PASS, 0 FAIL).
- RGRAM-GREEN via python (4152 PASS, 0 FAIL).
- SMOKE-GREEN (tests/smoke.sh, 6/6 cells, 0 FAIL).
- Wall: 0c53826..8df33e4 (rgramc.c only, 976+/532-) grep 0 hits.
Logs: NVME.../pv-8df33e4/logs/{build,rgramc,rgram-c,rgram-py,smoke}.log
+ lanediff.patch. Corpus seeded from pv-0f16b53 (oracle-deterministic
zeros rav); missing pins oracle-regenerated in-run.
Verdict: PV-PASS. NOT merged (parent merges oldest-first). Worktree kept.
