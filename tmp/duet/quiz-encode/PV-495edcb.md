# PV-495edcb (parent): band181 T10R130 (n<=63020, 834 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-495edcb), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4002/4002 covered=4002/4002, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8004/8004 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8004/8004)
- SMOKE: smoke.log 6 PASS
- Own-loop: covered by sweep GATE-495edcb + viewer VERIFY-495edcb first-hand
  batteries (own-loop 62765..63020 256/0, pins 12/12)
- Wall (e5ed337..495edcb, PARENT-032 scope): 0 hits
- GATE-495edcb PASS-functional (sweep) + VERIFY-495edcb PASS (viewer4) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 495edcb:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
