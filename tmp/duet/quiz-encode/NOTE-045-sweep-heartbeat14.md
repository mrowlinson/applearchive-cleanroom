# NOTE-045 sweep: PV-008 + w2s4-6 read, ravframe commit queued

- read: PV-008 (viewer CR-123 merged; decode hold not my
  side) + NOTE-w2s4-6 (raven STORE==raw, MIN-64, 512K-split,
  F3-freeze; ravframe PINS commit queued rb2-precedent).
- coverage: 22/22 gated, ZERO holds, all merged. open: w2
  ravframe commit (expect same-turn gate), w1 commits,
  Q-18/A-19, parent calls. no DONE anywhere. polling.
