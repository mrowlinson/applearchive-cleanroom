# PV-9afecce (parent): band174 T10P129 (n<=61720, 820 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-9afecce), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 3915/3915 covered=3915/3915, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (7830/7830 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (7830/7830)
- SMOKE: smoke.log 6 PASS
- Own-loop: covered by sweep GATE-9afecce + viewer VERIFY-9afecce first-hand
  batteries (own-loop 61629..61720 92/0, pins 26/26)
- Wall (ae7c8dd..9afecce, PARENT-032 scope): 0 hits
- GATE-9afecce PASS-functional (sweep2) + VERIFY-9afecce PASS (viewer2) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 9afecce:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
