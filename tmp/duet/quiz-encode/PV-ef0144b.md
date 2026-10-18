# PV-ef0144b (parent): band193 T10R136 (n<=65108, 858 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ef0144b), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4152/4152 covered=4152/4152, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8304/8304 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8304/8304)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep GATE-ef0144b + viewer VERIFY-ef0144b
  first-hand batteries (own-loop 256/0, pins 24/24)
- Wall (bd1ca6d..ef0144b, PARENT-032 scope): 0 hits
- GATE-ef0144b PASS-functional (sweep-r14) + VERIFY-ef0144b PASS (viewer-r16)
  + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show ef0144b:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
