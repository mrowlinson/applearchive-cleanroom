# PV-5bfc21a (parent): band187 T10R133 (n<=64064, 846 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-5bfc21a), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 4076/4076 covered=4076/4076, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (8152/8152 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (8152/8152)
- SMOKE: smoke.log 6 PASS (aar-encode/decode/bytes, aea-encrypt/decrypt/bytes)
- Own-loop: covered by sweep GATE-5bfc21a + viewer2 VERIFY-5bfc21a first-hand
  batteries (own-loop 63809..64064 256/0, pins 24/24)
- Wall (75d39c7..5bfc21a, PARENT-032 scope): 0 hits
- GATE-5bfc21a PASS-functional (sweep-r12) + VERIFY-5bfc21a PASS (viewer2-r7)
  + REAUDIT-5bfc21a PASS + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show 5bfc21a:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
