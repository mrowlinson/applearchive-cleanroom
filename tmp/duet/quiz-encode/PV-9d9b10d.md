# PV-9d9b10d (parent): band199 T10R139 (n<=66152, 870 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-9d9b10d), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4232/4232 covered=4232/4232, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8464/8464 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8464/8464)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep GATE-9d9b10d + viewer2 VERIFY-9d9b10d
  first-hand batteries (own-loop 256/256, pins 24/24)
- Wall (6bf6af5..9d9b10d, PARENT-032 scope): 0 hits
- GATE-9d9b10d PASS-functional (sweep-r16c; filed before workflow errored,
  content-verified first-hand by parent + concurred by VERIFY) +
  VERIFY-9d9b10d PASS (viewer2-r11) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 9d9b10d:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
