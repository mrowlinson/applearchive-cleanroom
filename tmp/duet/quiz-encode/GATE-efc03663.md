# GATE-efc03663 b232 T10P158 n<=71812 (936 tiers) PASS-functional

PARENT OUTAGE-COVER GATE (2026-10-19): sweep seats dead
(provider outage). Parent first-hand, fresh detached
worktree tmp/wt-pv-efc03663, TMPDIR NVME tmp/pv-efc03663.
- Scope vs parent cdc79b92 (b231): rgramc.c ONLY, 1 file changed, 1666 insertions(+), 1205 deletions(-).
- C build 0 warnings; RGRAMC-PYID 4694/4694 GREEN;
  RGRAM py + C GREEN (9388 PASS/0 FAIL each); SMOKE-GREEN.
- Wall PARENT-032: 0 hits outside FPs.
- Other harness suites: GREEN at b231 + untouched since
  (rgramc.c-only diff) => carry over.
VERDICT: PASS-functional (first-hand cover).
