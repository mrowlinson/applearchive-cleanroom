# NOTE-094 sweep heartbeat: polling, tips current, RED-hold open

1. state @this-NOTE: lanes tips 94c8d61 (w1 DONE-side) / 6c69085 (w2
   T10E-to-17144). ALL 151 tips gated-mine-current: 150/151 PASS + 1
   RED-held (48ebfe0). partners active (viewer beats NOTE-485b..488b
   inside the window).
2. hold: FLAG-48ebfe0-hold UNCHANGED — 15752 restoration outstanding
   across 9 descendant tips (48ebfe0..6c69085). each descendant verified
   individually-closed on fresh bytes; range BLOCKED pending restore.
3. gaps: none new. w1 hash parked-STUCK per A-42/individual verdicts. no
   joint DONE (w2 active, no viewer DONE-writer2).
4. turn: sweeping NOW. next poll covers any tip after 6c69085.
