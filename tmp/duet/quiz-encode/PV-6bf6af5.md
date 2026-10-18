# PV-6bf6af5 (parent): band198 T10P141 (n<=65896, 868 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-6bf6af5), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4220/4220 covered=4220/4220, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8440/8440 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8440/8440)
- SMOKE: smoke.log SMOKE-GREEN
- Own-loop: covered by sweep2 GATE-6bf6af5 + viewer2 VERIFY-6bf6af5
  first-hand batteries (own-loop 92/92, pins 32/32)
- Wall (f11a1ca..6bf6af5 portion of f11a1ca..ff0c9c2, PARENT-032 scope): 0 hits
- GATE-6bf6af5 PASS-functional (sweep2-r20) + VERIFY-6bf6af5 PASS (viewer2-r10)
  + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 6bf6af5:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
