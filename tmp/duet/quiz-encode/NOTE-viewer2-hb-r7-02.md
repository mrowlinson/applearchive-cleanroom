# NOTE-viewer2-hb-r7-02 (statics GREEN, big legs in flight)

- Build first-hand: cc -O2 -Wall -Wextra
  -std=c11 rc=0, 0 warnings, 1929512B
  (matches staged size).
- C-leg DONE: RGRAM-GREEN 8152 PASS /
  0 FAIL rc=0 (own bin).
- Own-loop DONE: 63809..64064 pass=256
  fail=0, pins 12 cells 24/24,
  OWNLOOP-GREEN rc=0.
- Tables-EQ DONE: M 16/16 + C 70/70 EQ,
  C_N=70 row-consistent, 2/2 GREEN.
- Wall-grep lane-diff (rgramc.c-only
  +1195/-1054, PARENT-032 scope): 0 hits.
  PINS 8154 lines = 8152+2 header.
- In flight: PYID (corpus seeded 4038
  own-seat .rav, new-pin oracle regen)
  + py-leg (1736 PASS / 0 FAIL and
  climbing). Set-eq + VERIFY after.
- Field: CLAIM-viewer2-5bfc21a uncont-
  ested (CLAIM-sweep-5bfc21a = gate
  track, independent); no GATE yet —
  VERIFY waits on sweep GATE per
  oldest-gated-first. viewer-r12 b186
  VERIFY in flight (yield stands). Q
  max 361, 0 owed. No commits, no push.
