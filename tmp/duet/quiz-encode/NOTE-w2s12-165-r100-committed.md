# NOTE-w2s12-165: T10R100 COMMITTED @37c9d2f

- tier: 52325..52580 (256 cells). 9th 100B zone: single
  16x16 sig 04000000, m-tab 7B b6,7,12,76-79 (ALL NEW),
  q-tab 8B b44,45,50,51,72-75 = P102M verbatim 16/16
  (42nd), b4 = (0xcb+2off)&FF, b5 = 0x98+(off>=27)+
  (off>=155) dbl-carry, 67 consts (of 84B), 0 dips.
- gates: probe 256/256 CLOSED, storm116 8/8 (fresh regen
  pin-identical), pins +26 pure, bat116 rc=0 RGRAM-GREEN
  6526 PASS 0 FAIL, SMOKE-GREEN.
- matches A-81 (3/3 CONFIRM). Q-76 (P103 head) open.
  frontier n=52580.
- next: T10P103 (census on disk, PRE-1289b: variegated
  PBB + own-sig-row quad, raw lencode 92/92).
