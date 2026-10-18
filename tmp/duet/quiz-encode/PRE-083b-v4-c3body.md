# PRE-083b cluster3-body 7690..7780: banded head + churn tail (T7K)

- 91 rows, 27 var (b1/2/4/36-59). b0 f4 frozen; b5 dc FROZEN
  (no b5 edge in cluster3 — first cluster without one).
- banded head: 7690 lit / 7691..7706 16-row / 7707..7716
  chatter-10 / 7717.. body (b1/2/36-45 16/10/bands; edges
  7691/7707/7710-7720-chatter/7733/7736/7749/7752/7765/7768).
- churn tail b46-59: per-row, NOT period-16 (nruns 11-65;
  hash-like, cf churn regime 073b). b4 ramp.
- model: bands + churn-tail (no tabs). then reframe 7781 (066b).
