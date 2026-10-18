# PRE-020b D2b2+D2c rules: 16-tabs + counters run 1865..2120 unbroken (w2 accel)

## b26/b34/b35: strict 16-tabs, phase from 1865, hold 1865..2120 (256 rows)
- b26: d3 d3 d5 d7 d7 d9 d9 db dd dd df df e1 e3 e3 e5 (verified 16/16
  cycles; 2048 lands db = tab[(2048-1865)&15] ✓ continuous into D2c).
- b34: 80 80 c0 00 00 40 40 80 c0 c0 00 00 40 80 80 c0 (16/16 ✓).
- b35: 6c 7c 71 67 77 6c 7c 71 66 76 6c 7c 71 66 76 6b (16/16 ✓).

## b28/b30: 16-plateau counters, same span unbroken
- b28: +0x16/block from 86@1865 (86 9c b2 c8 de f4 0a 20 36 4c 62 78
  8e a4 ba d0 @2041..2120; wraps f4->0a mid-span, no phase break).
- b30: +8/block from 43@1865 (43 4b 53 5b 63 6b 73 7b 83 8b 93 9b a3
  ab b3 bb @2041..2120).

## one-flips in span (v5d2 first-hand)
- b2/b3: 8c/00 -> cc/08 @1865 (hold to 2120). b5: 26->27 @1920.
- b29: bf@1865-1960 -> fc@1961-2047, fc holds 2048-2120.
- D2c 2048-2120 consts: b0 94 b1 7f b5 40 b10 01 b11 00 + D2b tail consts
  (b12 ee b13 aa b14 66 b15 26 b16 e6 b17 5a b18 8c b19 48 ...).
- span ENDS at 2121 singleton (PRE-017b); 2122 transition; 2123+ new bands.
