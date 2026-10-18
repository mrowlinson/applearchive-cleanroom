# PV-d840c7b: parent-verify first-hand (band52 T10P500..T10P50B, n<=34164)

Worktree tmp/wt-pv-d840c7b (detached @d840c7b), TMPDIR=NVME/.../tmp/pv-d840c7b, build seat-private.
- C-BUILD: make -C src/c BUILDDIR=$TMPDIR/build rc=0, 0 warnings (log build.log).
- RGRAMC-PYID 2036/2036 covered=2036/2036 (log rgramc.log):
  RGRAMC-PYID 2036/2036 covered=2036/2036
  RGRAMC-GREEN
- RGRAM-GREEN via C: 4072 PASS, 0 FAIL (log rgram-c.log, RGRAM_BIN=seat rgramc).
- RGRAM-GREEN via python: 4072 PASS, 0 FAIL (log rgram-py.log).
- SMOKE-GREEN (log smoke.log, 6 PASS).
- Wall: d840c7b^1..d840c7b (src/c/rgramc.c only, 960+/520-) grep vendor/disasm markers 0 genuine hits
  (1 FP: "r2 " matched T8R2 tier-label comments, not radare2).
- Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-d840c7b/{build,rgramc,rgram-c,rgram-py,smoke}.log
- Verdict: PV-PASS. Ready for parent oldest-first merge. Worktree left in place.
