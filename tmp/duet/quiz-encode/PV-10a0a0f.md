# PV-10a0a0f (parent): band202 T10P143 (n<=66592, 876 tiers) — GREEN

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-10a0a0f), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4274/4274 covered=4274/4274, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN
- PYBAT: rgram-py.log RGRAM-GREEN
- SMOKE: smoke.log SMOKE-GREEN
- FAIL scan: 0 hits across all 5 logs
- Own-loop: covered by sweep2 GATE-10a0a0f + viewer VERIFY-10a0a0f
  first-hand batteries
- Wall (732dac2..10a0a0f, PARENT-032 scope): 0 hits
- GATE-10a0a0f PASS-functional (sweep2 r22) + VERIFY-10a0a0f PASS
  + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d;
post-merge git show 10a0a0f:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
