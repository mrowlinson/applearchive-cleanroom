# PRE-018b E-plateau 2213..2468 @52B (8 fields) + dip re-confirm + F-head (w2 accel)

## E-plateau 2213..2468 @52B: minimal, 8 var (b4/5/6/7/44/45/50/51)
- b4: L10-lo +2/row CONTINUES (4b@2213 = 49@2212 +2, unbroken from D).
- b5: 2-row plateaus cycling 21/41/61/81/a1/c1/e1/01 (period 16).
- b7: 2-row-ish (+8/2rows: 85/8d/95/...); b6 every-row change.
- b44/b50/b51: 16-plateaus (16 runs each over 256 rows); b45: counter
  a2->ab (+1 per 16-32 rows: 2213-2244:a2 ... 2453-2468:ab).
- 44 const bytes (rest of frame fixed). E is as minimal as D-body.

## double-dip 2469/2470 @48B amid 52B: A-35 re-CONFIRMED
- paylen 52->48->52 at 2468/2469/2471 EXACT (A-35 PH1: 48B amid 52B ✓).
- dip frames differ in EXACTLY 17 bytes (nvar=17; A-35 said 17 ✓):
  b0 94/00, b1 7f/e5, b2 38/1f, b3 02/fe, b5 43/83, b6 8a/88,
  b7 0d/cd, b8 f0/16, b9 e2/4d, b10 01/09, b11 00/01, b27 f1/51,
  b38 53/a7, b39 6b/56, b46 33/5b, b47 e5/fb (b4 runs through: 4b/4d).
- L10-lo UNBROKEN through dip (+2/row 2468..2471: 49/4b/4d/4f).

## F-head 2471..2700 @52B: 34 var, 4 bands
- 2471-2486 / 2487-2496 (10-row) / 2497-2560 / 2561-2700 (b28-35 flip
  once @2561: e9/04/9e/51/b0/7d/7f/47 -> 0d/61/e3/19/be/bf/a3/13).
- b10: +8/row ramp 2471-2486 (8b..3d), chaotic 2487-2496, const 80 after.
- b0: 0f/03/3f/eb per band; b4 +2/row continues (4f@2471...).
