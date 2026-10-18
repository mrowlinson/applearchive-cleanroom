# FLAG-w1-lzma-b0-hold: 9433954 NOT mergeable until b0 fix + re-gate

- HOLD (sweep, PARENT-008 gate 2): NOTE-RED-9433954 proves a
  deterministic oracle-vs-impl byte divergence (tail-stream
  XZ b0 02-vs-03, +4B cascade) on BOTH backends.
- CLEAR CONDITION: fix commit (b0 rule bedded + py/C) +
  sweep re-gate GREEN (battery 6/6 both + sweep holdout
  12/12 incl m4m bracket). no merge before.
- ALSO OPEN (not sweep-owned): PARENT-008 gate 1 (liblzma
  survey entry — oss-survey lane) + gate 3 (C-link decision
  — parent). those hold independently.
