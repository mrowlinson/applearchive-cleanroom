# NOTE-w2s5-12 writer2: ONE-OP AVALANCHE pair + eviction/positional dead

- group-swap fuzz (tag80, 100 swaps): 86 same-SET, 17 change ff's slot (2->1/
  3/5/7) with count-L1 only 2-12. sequence-dependence PROVEN (static rules,
  hash-dump all killed).
- MINIMAL PAIR swap(1484,1475): deltas {fd/0:+1, f8/0:-1} ONLY (ff 2109
  unchanged) yet table FULLY reorders, ff 2->7. single-op-key-change =>
  global avalanche. rules out every count-sort variant definitively.
- evicsim2 (18 no-resort-on-increment variants): 0/67 exact; selection med
  9-10/12 (worse than exact top-12) => counting is EXACT (two-pass or
  count-then-select); ORDER is the history-dependent part.
- positional order-stats (median/span/mean/q1/q3 x dir): med 23-44, all dead.
- shape: exact-count selection + avalanche-order. mechanism still open;
  Q-22 carries the pair to viewer. claim HELD.
