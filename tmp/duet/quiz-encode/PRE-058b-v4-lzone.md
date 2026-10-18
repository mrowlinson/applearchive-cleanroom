# PRE-058b L-zone 5693..5948: run-256, 16-tabs + 16-bands + b5-128s

## census (v5ag, 256 rows all 56B, 14 var)
- 16-quiet head 5693..5708, then 14 edges>=8 @5709..5933
  (16-step + one 32-gap 5757-5789). no triple/chatter/dips.
- 16-tabs from 5693 (period-16 EXACT whole zone): b40=(d1 11
  31 71 91 d1 f1 31 51 91 d1 f1 11 51 91 b1), b41=(58 61 95
  95 c9 d1 a4 a5 d9 e1 e1 15 20 f1 f1 25), b42=(ff c1x4 c3
  c4x3 c6 c6 c7 c9x3 ca), b46=(06 2c ae ae 30 56 0c 0c 8e
  b4 b4 36 6c 12 12 94), b47=(f9 f8 f8 f8 f9 f8 f9 f9 f9
  f8 f8 f9 f8 f9 f9 f9), b48=(b3 d3x15).
- b4: ramp +2/row. b5: 128-plateaus 6c/6d/6e @5693/5760/5888.
  b15: bf->cf @5709 (single edge).
- bands from 5709: b30 strict 98/18 alternation; b22/b23/b31/
  b39 16-bands (+32-runs over the 5757-5789 gap).
- one commit 5693..5948 (or split at 5789/5821 gap edges).
