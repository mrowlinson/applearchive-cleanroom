# Q-28 writer1s2 lz4 eviction structure (CR-122 mechanism)

- MODEL (own): Knuth-12 4K last-write + mstart/+1/ends + continuous + K-gate = 486/672 files (72%). residual includes ~31 first-divs with span>7K (eviction-plausible per A-17: 50% @8.5K distinct, 0% @11.5K+).
- PROBLEM: 4K-uniform predicts 50% @~2.8K (too early) and ~38% @11.5K (too late, observed 0/24). fractions (5/6, 2/6, 1/6) over gram-sets + steep cliff = underivable statically (need the STRUCTURE).
- ASK (behavior-only): what insertion/lookup structure reproduces the CR-122 curve deterministically (multi-slot buckets? segmented/capped? adaptive tabling)? one discriminating bed-shape: an INSERT pattern that SURVIVES vs one that EVICTS at the SAME distinct count (~9K), or the bucket/segment width if probed.
