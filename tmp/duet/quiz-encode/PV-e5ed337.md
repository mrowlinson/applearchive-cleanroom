# PV-e5ed337 (parent): band180 T10P132 (n<=62764, 832 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-e5ed337), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 3990/3990 covered=3990/3990, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (7980/7980 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (7980/7980)
- SMOKE: smoke.log 6 PASS
- Own-loop: covered by sweep GATE-e5ed337 + viewer VERIFY-e5ed337 first-hand
  batteries (own-loop 62673..62764 92/0, pins 26/26)
- Wall (20730c9..e5ed337, PARENT-032 scope): 0 hits
- GATE-e5ed337 PASS-functional (sweep2) + VERIFY-e5ed337 PASS (viewer, stands
  per PARENT-069) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show e5ed337:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
