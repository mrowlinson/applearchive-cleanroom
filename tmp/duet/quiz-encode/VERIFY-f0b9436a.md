# VERIFY-f0b9436a cport bands260-278 T10P162..P180 (n<=80072, 988 tiers): PASS

PARENT OUTAGE-COVER VERIFY (2026-10-20): all viewer seats
dead (provider outage). Parent ran the viewer core legs
first-hand instead, fresh detached worktree
tmp/wt-pv-f0b9436a, TMPDIR NVME tmp/pv-f0b9436a
(pv-band.sh, seat-private build, 4 concurrent legs).

- Tree: f0b9436a (absorb dcc80020 + C port).
- C build: cc -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings.
- PYID: RGRAMC-PYID 5334/5334 covered=5334/5334,
  RGRAMC-GREEN, 0 FAIL.
- CBAT (RGRAM_BIN=own build): 10668 PASS / 0 FAIL,
  RGRAM-GREEN.
- PYBAT (python impl): 10668 PASS / 0 FAIL, RGRAM-GREEN.
- PINS-RGRAM set-eq 10668/10668 (cmp-identical).
- SMOKE: aar+aea roundtrips all PASS, SMOKE-GREEN.
- Wall PARENT-032 on band diff: 0 hits outside FPs.
- New cells 73113..79468 (P-gaps) served via ct-cache
  with sha-vs-PINS self-check (miss path = real tool).
- Tables-EQ: via battery implication (every pin
  exercising new T10P162..P180 tables passes in both
  impls) + C-diff renumber-equivalence proof (0 missing
  normalized patterns).
- Placement: P162-P180 code between R159/R160 blocks
  (P-gap-before-R-catchall rule, see GATE).

Agrees with GATE-f0b9436a (PASS-functional) on every leg.
Deviation logged: single-operator cover, no independent
viewer seat available.
