# PV-066fa1c (parent): band183 T10R131 (n<=63368, 838 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-066fa1c), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4024/4024 covered=4024/4024, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8048/8048 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8048/8048)
- SMOKE: smoke.log 6 PASS
- Own-loop: covered by sweep GATE-066fa1c + viewer VERIFY-066fa1c first-hand
  batteries (own-loop 63113..63368 256/0, pins 20/20)
- Wall (d1a3c2d..066fa1c, PARENT-032 scope): 0 hits
- GATE-066fa1c PASS-functional (sweep) + VERIFY-066fa1c PASS (viewer2) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 066fa1c:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
