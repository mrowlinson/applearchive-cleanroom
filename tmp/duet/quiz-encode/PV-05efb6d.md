# PV-05efb6d (parent): band190 T10P137 (n<=64504, 852 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-05efb6d), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4115/4115 covered=4115/4115, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8230/8230 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8230/8230)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep2 GATE-05efb6d + viewer3 VERIFY-05efb6d
  first-hand batteries (own-loop 92/92, pins 28/28)
- Wall (fac36c9..05efb6d, PARENT-032 scope): 0 hits
- GATE-05efb6d PASS-functional (sweep2-r17) + VERIFY-05efb6d PASS (viewer3-r8)
  + no FLAG (OUTER2 a-nondet proven oracle flake per precedent)

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 05efb6d:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
