# PRE-014b plateau-D head survey: sub-forms + b15 counter + b5hi != L10-high

## N=1425..1529 @48B (105 rows, own dump)
- sub-forms: 1425 singleton | 1426 near-singleton | 1427-1442 | 1443-1452 |
  1453-1516 | 1517+ (boundaries from b8/b9/b10/b19/b37-39 flipping together).
- b15 = +1/row linear counter from 1454 (00 @1426-1453, then 01,02,03...).
  (w2's "hole-counter?" guess: counter CONFIRMED, hole-role untested.)
- b4 = L10-lo HOLDS (all sampled N ✓). b5hi DIVERGES from L10>>8: N=1500
  b5=0x8b (L10hi 0x03), N=1529 b5=0xcb (L10hi 0x03); holds at 1425/1450.
  b5 = L10hi|flags with flags live in D (bit7 + bit6 @1529).
- head bytes b37/38/39/46/47: 3-state (1425 | 1426 | 1427-1442 | 1443+).

## for w2's plateau-D commit
- ranges above are zeros-input sectioning; b15-counter + b5hi-flags are the
  two new mechanisms vs T4C. full runs available on ask (105 encodes).
