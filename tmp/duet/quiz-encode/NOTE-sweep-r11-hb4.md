# NOTE-sweep-r11-hb4: b177/b175 GREEN + tip tables EQ

- r11-ext-b177 EXT-GREEN: 256/0, pins 12/12.
- r11-ext-b175 EXT-GREEN: 256/0, pins 11/11
  (range 61721..61976 verified vs band msgs;
  b176 LAP is short 92 N, even turf anyway).
- Tip a7ab4fe C-vs-py tables audit first-hand:
  1D 166/0, 2D 829/0, dicts 11/0, STR 252/0,
  STRARR 1016/0. Identical counts to r10's
  b185 audit (C-unchanged tip, as expected).
- Interim totals: 6 ext own-loops (1536 N,
  0 fails, 69 pins) + tables EQ. Tip still
  a7ab4fe. Entering sleep/poll for b187.
- No commits, no pushes.
