# PV-7c2e8d4 (parent): band185 T10R132 (n<=63716, 842 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-7c2e8d4), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4050/4050 covered=4050/4050, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8100/8100 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8100/8100)
- SMOKE: smoke.log 6 PASS
- Own-loop: covered by sweep GATE-7c2e8d4 + viewer VERIFY-7c2e8d4 first-hand
  batteries (own-loop 63461..63716 256/0, pins 24/24)
- Wall (a31520e..7c2e8d4, PARENT-032 scope): 0 hits
- GATE-7c2e8d4 PASS-functional (sweep) + VERIFY-7c2e8d4 PASS (viewer3) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 7c2e8d4:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
