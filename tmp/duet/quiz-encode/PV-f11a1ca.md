# PV-f11a1ca (parent): band197 T10R138 (n<=65804, 866 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-f11a1ca), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4204/4204 covered=4204/4204, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8408/8408 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8408/8408)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep GATE-f11a1ca + viewer2 VERIFY-f11a1ca
  first-hand batteries (own-loop 256/256, pins 24/24)
- Wall (4c9ff15..f11a1ca, PARENT-032 scope): 0 hits
- GATE-f11a1ca PASS-functional (sweep-r15) + VERIFY-f11a1ca PASS (viewer2-r10)
  + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show f11a1ca:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
