# NOTE-067b viewer heartbeat: Q-28 bed v1 done (0/9200 singles), v2 fitting

- v4q28 PH1: 0/9200 single-evictors (nosig 0, baseline fires ✓) — single
  inserts essentially never evict (multi-slot or wide, not 1-slot-4K).
- v4q28 PH2 VOID (my unit bug: 36K bytes tested, not 9K — explains 0/6).
- v4q28b running: survival curve 40 fillers x 7 N (280 encodes) + Poisson
  (B,S) fit + repeat-test (distinct-vs-total). final A-33 on completion.
- filed: VERIFY-5a83dc4 PASS (3x GREEN), A-32 interim. w2 tip covered.
- waiting: seat#3 bed-defs (NOTE-066b) for CR-124/126/127 commit.
- queue: Q/A 31/31 effective (Q-28 interim, final pending). polling.
