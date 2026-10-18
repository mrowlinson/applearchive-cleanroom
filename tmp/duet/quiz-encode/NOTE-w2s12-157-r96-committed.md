# NOTE-w2s12-157: T10R96 COMMITTED @ac2e8f5

- tier: 50933..51188 (256 cells). 5th 100B zone: single
  16x16 sig 01000000, m-tab 8B b28,33,34,35,76-79 (ALL
  NEW), q-tab 8B b18,19,26,27,72-75 (tail-4 = P98M tails
  16/16 same-pos, 38th; heads NEW), b4 = (0xeb+2off)&FF,
  b5 = 0x8d+(off>=11)+(off>=139) dbl-carry, 66 consts
  (of 84B), 0 dips.
- gates: probe 256/256 CLOSED, storm108 8/8 (fresh regen
  pin-identical), pins +26 pure, bat108 rc=0 RGRAM-GREEN
  6312 PASS 0 FAIL, SMOKE-GREEN.
- matches A-73 (3/3 CONFIRM). Q-68 (P99 head) open.
  frontier n=51188.
- next: T10P99 (census on disk, PRE-1281b: alternating
  PBB + 64-cell row1-unique quad, raw lencode 92/92).
