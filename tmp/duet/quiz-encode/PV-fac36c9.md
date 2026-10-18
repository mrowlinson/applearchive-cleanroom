# PV-fac36c9 (parent): band189 T10R134 (n<=64412, 850 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-fac36c9), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4101/4101 covered=4101/4101, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8202/8202 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8202/8202)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep GATE-fac36c9 + viewer2 VERIFY-fac36c9 first-hand
  batteries (own-loop 64157..64412 256/256, pins 22/22)
- Wall (07533a3..fac36c9, PARENT-032 scope): 0 hits
- GATE-fac36c9 PASS-functional (sweep-r13) + VERIFY-fac36c9 PASS (viewer2-r8)
  + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show fac36c9:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
