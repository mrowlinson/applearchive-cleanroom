# PV-bd1ca6d (parent): band192 T10P138 (n<=64852, 856 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-bd1ca6d), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4140/4140 covered=4140/4140, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8280/8280 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8280/8280)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep2 GATE-bd1ca6d + viewer2 VERIFY-bd1ca6d
  first-hand batteries (own-loop 92/92, pins 26/26)
- Wall (94a0e0b..bd1ca6d, PARENT-032 scope): 0 hits
- GATE-bd1ca6d PASS-functional (sweep2-r19) + VERIFY-bd1ca6d PASS (viewer2)
  + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show bd1ca6d:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
