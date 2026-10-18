# NOTE-w2s12-160: T10P100 COMMITTED @0a2c6d6

- tier: 51537..51628 (92 cells). S0 51537 (sig 19df0300)
  + S1 51538, PBA 51539..51554 (16x m-tab b6,7,8,72-75),
  split-PBB 51555..51564 (10x: single 51555 sig a619df04
  + 9x sig d38c6f02, m-tab b0-3,6-11,76-79), QUAD
  51565..51628 (4x16 single sig: M 6B b13,14,72-75,
  row0/row1 differ b6 only, row2==row1, row3 unique,
  tails fde69467/818c0f42/018d0f42/534edea2). raw lencode
  92/92 (wrap row1m2->m3 51583/51584).
- gates: probe 92/92 CLOSED, storm111 14/14 (fresh regen
  pin-identical), pins +28 pure, bat111 rc=0 RGRAM-GREEN
  6396 PASS 0 FAIL, SMOKE-GREEN.
- matches A-76 (3/3 CONFIRM). Q-71 (R98 head) open.
  frontier n=51628.
- next: T10R98 (census on disk, PRE-1284b: 100B 16x16 NEW
  sig 02000000, P100M-tail4 same-pos q (40th), dbl-carry).
