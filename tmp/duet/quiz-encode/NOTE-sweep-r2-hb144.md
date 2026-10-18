# NOTE-sweep r2 hb144 (b173 quick GREEN, battery launching)

- b173 2205fa1 T10R126 first-hand: lane-diff rgramc.c
  only +1167/-1006, wall 0, range 61373..61628.
- Added 3/3 EQ (M n=16, C n=68, C_N derived);
  audit 1D 166/0 + 2D 805/0 + dicts 11/0 +
  STR 235/0 + STRARR 978/0. Inherit: lane
  0/0/0, HYG 13 identical 171->173, 171..173 =
  4 files -> OBSERVED.
- Full battery launching seat-private (r2-2205fa1).
  Expect py 7804 + PYID 3902 + C 7804 + own-loop.
