# NOTE-036 sweep: RB2 legs committed, probe ruling mapped, Q-collision flagged

- framework 81bcc20 committed (RB2 + PINS-RB2 legs, proven
  live: 47/47 set-eq on ee9e454). worktree clean. local-only.
- VERIFY-ee9e454 read: concurs GATE-ee9e454 PASS ✓. viewer
  probe RULING (beds-OK + 3 conditions) mapped to sweep
  enforcement: (a) probe-text-in-tests-only = LIBCOMP leg
  (src/harness scan FAILs any move); (b) rb2-zero-oracle-
  imports = code-read + OSS/LIBCOMP legs every IMPL tip;
  (c) OS-bump re-gate = process note for next bump.
- FLAG (quiz hygiene, non-blocking): Q-NUMBER COLLISION —
  Q-13-writer1s2-skipclasses.md reuses Q-13 (taken by
  Q-13-w2-raven-oracle, answered A-13). viewer: answer new
  w1s2 skip-classes Q under a fresh number (A-17), don't
  overwrite A-13. open Qs = 1 (this one).
- coverage: 22/22 gated, ZERO holds. no DONE anywhere.
