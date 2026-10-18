# PRE-019b E-plateau field rules: 16-tabs + b5-lo=L10>>8 (w2 accel)

## b6: strict 16-tab x16 (v5e2, 256/256 rows)
- tab (i=(N-2213)&15): b9 f9 c0 87 c7 8e ce 95 d5 9c dc a3 e3 ab eb b2.
  no drift, no exception.

## b5: 16-tab duty (3,1,2,2,2,2,2,2) + lo-nibble = L10>>8
- values cycle +0x20: 21 41 61 81 a1 c1 e1 01; 41 singleton @i==2,
  21 triple @i==15,0,1, rest pairs. repeats every 16 EXACT (16/16 cycles).
- lo-nibble drifts: x1 @2213..2303, x2 @2304..2431, x3 @2432..2468 =
  L10>>8 (L10=(N<<1|1)&0x3FF: 331->513->769 cross 512/768 at 2304/2432 ✓).
  same L10>>8-lo shape as w2 T4F b5 formula.

## b7: 16-tab duty (2,1,2,2,2,2,2,2,1), no drift
- values: 85(x2) 8d(x1 @i==2) 95 9d a5 ad b5 bd (x2 each) c5(x1 @i==15).
  16/16 cycles EXACT.

## b4: L10-lo +2/row (PRE-018b, unbroken 1517..2471+)
