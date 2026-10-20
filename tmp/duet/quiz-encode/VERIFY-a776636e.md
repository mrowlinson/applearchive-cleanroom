# VERIFY-a776636e cport bands239-259 T10R159..R179 (n<=80072, 969 tiers): PASS

PARENT OUTAGE-COVER VERIFY (2026-10-20): all viewer seats
dead (provider outage). Parent ran the viewer core legs
first-hand instead, fresh detached worktree
tmp/wt-pv-a776636e, TMPDIR NVME tmp/pv-a776636e
(pv-band.sh, seat-private build, 4 concurrent legs).

- Tree: a776636e (absorb e1e8492f + C port).
- C build: cc -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings.
- PYID: RGRAMC-PYID 5030/5030 covered=5030/5030,
  RGRAMC-GREEN, 0 FAIL.
- CBAT (RGRAM_BIN=own build): 10060 PASS / 0 FAIL,
  RGRAM-GREEN.
- PYBAT (python impl): 10060 PASS / 0 FAIL, RGRAM-GREEN.
- PINS-RGRAM set-eq 10060/10060 (C/PY PASS-name sets
  cmp-identical, both all-PASS).
- SMOKE: aar+aea roundtrips all PASS, SMOKE-GREEN.
- Wall PARENT-032 on band diff: 0 hits outside FPs.
- New cells 72857..80072 served via ct-cache with
  sha-vs-PINS self-check (miss path = real tool).
- Tables-EQ: via battery implication (every pin
  exercising new T10R159..R179 tables passes in both
  impls) + transpiler determinism proof (pre-batch
  input reproduces committed rgramc.c byte-identical,
  code diff of batch is additive-only).

Agrees with GATE-a776636e (PASS-functional) on every leg.
Deviation logged: single-operator cover, no independent
viewer seat available. Evidence strength = full battery
re-execution in two independent worktrees + two builds.
