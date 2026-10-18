# PV-ff0c9c2 (parent): band200 T10P142 (n<=66244, 872 tiers) — GREEN, merge pending b199

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ff0c9c2), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4246/4246 covered=4246/4246, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8492/8492 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8492/8492)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep2 GATE-ff0c9c2 + viewer4 VERIFY-ff0c9c2
  first-hand batteries (own-loop 92/92, pins 28/28)
- Wall (9d9b10d..ff0c9c2, PARENT-032 scope): 0 hits
- GATE-ff0c9c2 PASS-functional (sweep2-r20) + VERIFY-ff0c9c2 PASS (viewer4-r10)
  + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d (after b199);
post-merge git show ff0c9c2:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
