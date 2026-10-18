# PV-fe4c199 (parent): band177 T10R128 (n<=62324, 826 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-fe4c199), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 3950/3950 covered=3950/3950, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (7900/7900 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (7900/7900)
- SMOKE: smoke.log 6 PASS
- Own-loop: covered by sweep GATE-fe4c199 + viewer VERIFY-fe4c199 first-hand
  batteries (own-loop 62069..62324 256/0, pins 24/24)
- Wall (2551219..fe4c199, PARENT-032 scope): 0 hits
- GATE-fe4c199 PASS-functional (sweep) + VERIFY-fe4c199 PASS (viewer2) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show fe4c199:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
