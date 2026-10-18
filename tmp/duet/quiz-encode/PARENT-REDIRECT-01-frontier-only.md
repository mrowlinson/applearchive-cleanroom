# PARENT-REDIRECT-01 (2026-10-18): viewers FRONTIER-ONLY until drain

- Effective immediately, all viewer seats (viewer, viewer2,
  viewer3, viewer4): Step-1 frontier VERIFYs ONLY.
- No NEW down-series REAUDIT claims until the parent lifts
  this redirect (lift condition: merge queue from master tip
  to newest GATE <= 2 bands). Any new old-band CLAIM filed
  after this note is REJECTED at filing — do not start the
  battery.
- Live REAUDIT batteries (claim filed before this note) may
  finish and file. Then frontier-only.
- Rounds with no unclaimed GATE: poll + heartbeat (do not
  invent REAUDIT work to fill the cap); 2 consecutive empty
  rounds = report to parent for reassignment, not SPINNING.
- Reason: owner-ordered finish drive. Every viewer hour goes
  to unblocking merges. Old-band REAUDIT backlog resumes
  after the drain.
