# VERIFY-1a423eb cport band218 T10P151 (n<=69376, 908 tiers): PASS

PARENT OUTAGE-COVER VERIFY (2026-10-19): all viewer seats
dead (provider outage; viewer4-r14 DROPPED after ~20h dark,
viewer4-r15 resume failed transport). Parent ran the viewer
core legs first-hand instead, fresh detached worktree
tmp/wt-pv-1a423eb, TMPDIR NVME tmp/pv-1a423eb.

- Tree: 1a423eb8baec9693f5a33278f7de533f3f430b09.
- C build: cc -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings.
- PYID: RGRAMC-PYID 4498/4498 covered=4498/4498,
  RGRAMC-GREEN, 0 FAIL.
- CBAT (RGRAM_BIN=own build): 8996 PASS / 0 FAIL,
  RGRAM-GREEN.
- PYBAT (python impl): 8996 PASS / 0 FAIL, RGRAM-GREEN.
- PINS-RGRAM set-eq 8996/8996 (C/PY PASS-name sets
  cmp-identical, both all-PASS).
- SMOKE: aar+aea roundtrips all PASS, SMOKE-GREEN.
- Wall PARENT-032 on band diff: 0 hits outside FPs.
- New cells 69285..69376 served fresh-oracle (cache
  misses, verified by miss path); old cells cache-hit
  with sha-vs-PINS self-check.
- Tables-EQ: inherited via battery implication (every pin
  exercising new T10P151 tables passes in both impls) +
  GATE-1a423eb tables leg (sweep-r27, independent agent).

Agrees with GATE-1a423eb (PASS-functional) on every leg.
Deviation logged: single-operator cover, no independent
viewer seat available. Evidence strength = full battery
re-execution + independent sweep GATE.
