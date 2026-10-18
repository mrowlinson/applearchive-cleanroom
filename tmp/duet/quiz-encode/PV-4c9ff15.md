# PV-4c9ff15 (parent): band196 T10P140 (n<=65548, 864 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-4c9ff15), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4192/4192 covered=4192/4192, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8384/8384 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8384/8384)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep2 GATE-4c9ff15 + viewer VERIFY-4c9ff15
  first-hand batteries (own-loop 92/92, pins 30/30)
- Wall (3744141..4c9ff15, PARENT-032 scope): 0 hits
- GATE-4c9ff15 PASS-functional (sweep2-r19) + VERIFY-4c9ff15 PASS (viewer-r19,
  superseded stale viewer3 claim per DROPPED protocol) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 4c9ff15:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
