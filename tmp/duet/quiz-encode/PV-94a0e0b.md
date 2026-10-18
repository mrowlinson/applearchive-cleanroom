# PV-94a0e0b (parent): band191 T10R135 (n<=64760, 854 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-94a0e0b), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4127/4127 covered=4127/4127, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8254/8254 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8254/8254)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep GATE-94a0e0b + viewer3 VERIFY-94a0e0b
  first-hand batteries (own-loop 256/0, pins 24/24)
- Wall (05efb6d..94a0e0b, PARENT-032 scope): 0 hits
- GATE-94a0e0b PASS-functional (sweep-r14) + VERIFY-94a0e0b PASS (viewer3-r9)
  + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 94a0e0b:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
