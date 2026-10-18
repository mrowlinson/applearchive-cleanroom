# PV-e02b8fe (parent): band178 T10P131 (n<=62416, 828 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-e02b8fe), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 3965/3965 covered=3965/3965, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (7930/7930 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (7930/7930)
- SMOKE: smoke.log 6 PASS
- Own-loop: covered by sweep GATE-e02b8fe + viewer VERIFY-e02b8fe first-hand
  batteries (own-loop 62161..62416 256/0, pins 21/21)
- Wall (fe4c199..e02b8fe, PARENT-032 scope): 0 hits
- GATE-e02b8fe PASS-functional (sweep2) + VERIFY-e02b8fe PASS (viewer4) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show e02b8fe:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
