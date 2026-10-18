# NOTE-w2s12-151: T10R93 COMMITTED @1d55d5b

- tier: 49889..50144 (256 cells). 2nd 100B zone: single
  16x16 sig 01000000, m-tab 7B b28,29,30,72-75 (ALL NEW),
  q-tab 7B b20,21,22,76-79 (tail-4 = P95M tails 16/16,
  35th; prefixes NEW, b21=df/5a b22=02/03 q-split),
  b4 = (0xc3+2off)&FF, b5 = 0x85+(off>=31)+(off>=159)
  dbl-carry, 68 consts (of 84B), 0 dips.
- gates: probe 256/256 CLOSED, storm102 8/8 (fresh regen
  pin-identical), pins +24 pure, bat102 rc=0 RGRAM-GREEN
  6158 PASS 0 FAIL, SMOKE-GREEN.
- matches A-67 (3/3 CONFIRM). Q-62 (P96 head) open.
  frontier n=50144.
- next: T10P96 (census on disk, PRE-1275b: same-family
  head + 64-cell quad 6B new M, raw lencode 92/92).
