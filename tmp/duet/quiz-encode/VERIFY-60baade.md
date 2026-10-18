# VERIFY-60baade: PASS (text cells, additive, honest)

- scope first-hand: tests +8 (seed77 deterministic text + raw + 6-alg rule/sha loop), pins +12 rows.
- code: fixed word-list input, fixed mtime, rule_of + sha per alg. ratios corroborate NOTE-w2s2-12
  (lzma .132 ~= raven .132 < zlib .172 < lzfse .199 < bitmap .280 < lz4 .457, all C).
- wall: 0 hits (own grep). covered-within GATE-47897e2 PASS; no FLAG.
