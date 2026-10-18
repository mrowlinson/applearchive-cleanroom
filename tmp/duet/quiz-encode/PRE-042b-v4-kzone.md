# PRE-042b K-zone 3769..3952: bands + 3861 singleton + tier-end run (w2 map)

## sectioning (v5s 184 rows @52B, 47 var, consts b6/7/8/9/10 only)
- K1 3769..3860: bands (b24 12/32/16/32; b26 12/16/16/16/16/16; b5
  fd->fe @3840).
- K2 3861: SINGLETON (b0 01 vs 82; b12 00; b20 ab; b21 9f; 34 flips in
  + 34 back @3862 — full-frame deviate-and-return).
- K3 3862..3888: second regime (b13 80, b20 4b, b21 92, b26 45).
- K4 3889..3952: tier-end run (28-flip edge @3889: b12->34, b13->91;
  b44-51 single flips; runs to 52/56 edge 3952/3953).

## busy bytes (non-tabular): b15 (35) / b23 (96) / b30/b31 (91/96) /
  b34/b35 (70/66) / b36-39 (19-32) / b42/43 (64/49). b4 L10-lo ramps.
