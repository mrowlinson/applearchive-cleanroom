# PRE-016b plateau-D body = 7-field minimal form (1517..1772, w2 accel)

## N=1517..1772 @48B: 7 varying bytes, 41 const
- b4: +2/row (L10-lo continues ✓). b5: cb@1517-1535, cc@1536-1663,
  cd@1664+ (19-row + 128-plateaus).
- b15: (N-1517)>>4 (16-row plateaus 00..0f ✓ PRE-015b holds to 1772).
- b0: 17 x11 / 18 x5 alternating (period 16).
- b11: ramp +8/row-ish, 1-2-row plateaus, period 16 (c5..0d, repeats @1533).
- b19: ramp +0x19/row-ish, plateaus, period 16 (51.., repeats @1533).
- b10: e2/c2/a2 period-3 cycling + phase slip (double-e2 @1526-1527,
  pattern resumes; slip period OPEN — needs longer run or w2's dump).
- consts (41): 1:8d,2:08,3:00,6:bd,7:4a,8:f0,9:06,12:00,13:00,14:3c,16:12,
  17:00,18:00,20:08,21:cc,22:3d,23:f8,24:00,25:3c,26:04,27:1f,28:86,29:ef,
  30:f8,31:bd,32:69,33:01,34:4c,35:d7,36:24,37:a7,38:d6,39:3e,40:83,41:c6,
  42:43,43:4d,44:06,45:5f,46:a6,47:fc.

## for w2
- D-body is nearly as minimal as B5 (7 vs 3 fields). b10-slip + b0-duty
  are the only non-trivial bits. zeros-input sectioning; dev mapping theirs.
