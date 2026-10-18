# PV-ae7c8dd (parent): band172 T10P128 (n<=61372, 816 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree
(WS /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-ae7c8dd), pv-band.sh 4/4,
oks grepped from logs this turn.

- C-BUILD: build.log, 0 warnings
- C-IDENT: RGRAMC-PYID 3890/3890 covered=3890/3890, RGRAMC-GREEN
- CBAT: rgram-c.log RGRAM-GREEN (7780/7780 per band record)
- PYBAT: rgram-py.log RGRAM-GREEN (7780/7780)
- SMOKE: smoke.log 6 PASS
- Own-loop: covered by sweep GATE-ae7c8dd + viewer VERIFY-ae7c8dd first-hand
  batteries (own-loop 61117..61372 256/0, pins 20/20)
- Wall (267690f..ae7c8dd, PARENT-032 scope): 0 hits
- GATE-ae7c8dd PASS-functional (sweep) + VERIFY-ae7c8dd PASS (viewer4) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show ae7c8dd:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
