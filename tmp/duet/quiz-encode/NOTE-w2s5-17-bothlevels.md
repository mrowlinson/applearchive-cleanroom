# NOTE-w2s5-17 writer2: divergence at BOTH levels (matchfinder + table-g)

- matchfinder: tag0 first-op-div at op25 (lc holds period-8/ff-literals,
  OSS takes period-36 match). greedy-vs-optimal, as predicted.
- table-g: OSS tables ≈ count-DESC (n=96, med Kendall 1.0, 21 EXACT zeros;
  ties-first-seen per w2s3-10). oracle tables med 11-12, 0 zeros. the WRITE
  RULE ITSELF differs (not just downstream of parse). any future rewrite
  must clone BOTH the optimal-parse DP (+tie-breaks) and the oracle table-g
  (still unknown mechanism — tie-lottery describes WHEN, not the WRITE MAP).
- Q-23 open (viewer divergence-proof). claim HELD.
