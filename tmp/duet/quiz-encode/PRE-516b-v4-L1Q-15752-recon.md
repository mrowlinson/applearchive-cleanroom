# PRE-516b L1Q-15752 recon (derived vendor bytes only)

## breaking cell
- N=15752 (L1Q off=31, m=15, q=1). vendor
  payload 68B:
  68d6e301113bc3f92503945ea249efb11af510
  edbe3ce60001e4ff5c80f111b48a5ca24a789a
  94575be05d1898aa5e71597e748b5d5ddd9d5
  abc92bb0ad282b155bccdfa

## divergence within q=1 row (15737 m=0 vs 15752 m=15)
- payload bytes 18..23 identical
  (`edbe3ce60001`); byte 24 diverges: m=0
  has cd, m=15 has e4. rest of middle
  (`ff5c80f1...`) identical.
- byte 4 walks with N as usual
  (0f@15751 / 11@15752 / 13@15753).

## m=15 column (all q)
- tail `55bccdfa` constant at 15736 (q=0),
  15752 (q=1), 15768 (q=2), 15784 (q=3).
- middle per-q signatures differ
  (a03cdd0301 / be3ce60001 / 6c3cdc0401 /
  ...), as in passing rows.

## verdict aid
- neighbors 15737/15753 rc=0; only (m=15,
  q=1) breaks. single-bytepayload
  divergence at byte 24 is the observable
  fact; table/model fix is writer-side.
