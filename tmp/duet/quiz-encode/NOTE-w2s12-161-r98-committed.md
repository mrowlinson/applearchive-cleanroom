# NOTE-w2s12-161: T10R98 COMMITTED @ce895c9

- tier: 51629..51884 (256 cells). 7th 100B zone, NEW sig
  02000000: single 16x16, m-tab 6B b22,23,76-79 (ALL NEW),
  q-tab 7B b8,9,10,72-75 (tail-4 = P100M tails 16/16
  same-pos, 40th; heads NEW), b4 = (0x5b+2off)&FF, b5 =
  0x93+(off>=83)+(off>=211) dbl-carry, 69 consts (of 84B),
  0 dips.
- gates: probe 256/256 CLOSED, storm112 8/8 (fresh regen
  pin-identical), pins +26 pure, bat112 rc=0 RGRAM-GREEN
  6422 PASS 0 FAIL, SMOKE-GREEN.
- matches A-77 (3/3 CONFIRM). Q-72 (P101 head) open.
  frontier n=51884.
- next: T10P101 (census on disk, PRE-1285b: PB1-sig-repeat
  PBB + row0==row2 quad, raw lencode 92/92).
