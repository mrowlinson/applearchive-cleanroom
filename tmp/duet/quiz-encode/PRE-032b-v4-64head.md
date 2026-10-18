# PRE-032b 64-tier head: dip-split regimes + 16-bands + 8825 reframe (w2 map)

## regimes (v5l, 116 rows excl dip)
- pre-dip 8735..8750 vs post-dip 8761..: b5 84->04, b6 55->f5, b12
  fa->03, b9/10/11 87/1d/f0 -> 7f/d8/41. dip SPLITS two regimes.
- 8825 reframe (24 bytes flip): b0 01->14, b9/10/11 -> f1/87/1d,
  b18/19 -> cf/ff, +19 more. 8832: b5 04->05.
- 16-bands under it: flip-N peaks 8777/8793/8809 (+16s, 12-14 flips),
  8841/8857 (+16s). most bytes 1-2 flips (nruns=2/3).

## busy zones (non-tabular — periods=[] ALL bytes)
- b8/13/14/15/16/17: 23-38 runs. b60/61/62/63: 53-83 runs, 19-26
  unique (hash-like tail, unlike 56B tabbed tail).
- b4: L10-lo +2/row runs THROUGH the wide dip (5d@8750 -> 73@8761 ✓).
