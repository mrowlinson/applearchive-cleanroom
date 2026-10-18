# NOTE-w2s12-159: T10R97 COMMITTED @4b9288f

- tier: 51281..51536 (256 cells). 6th 100B zone: single
  16x16 sig 01000000, m-tab 8B b42,43,50,51,76-79 (ALL
  NEW), q-tab 7B b44,45,46,72-75 = P99M verbatim 16/16
  (39th), b4 = (0xa3+2off)&FF, b5 = 0x90+(off>=47)+
  (off>=175) dbl-carry, 67 consts (of 84B), 0 dips.
- gates: probe 256/256 CLOSED, storm110 8/8 (fresh regen
  pin-identical), pins +26 pure, bat110 rc=0 RGRAM-GREEN
  6368 PASS 0 FAIL, SMOKE-GREEN.
- matches A-75 (3/3 CONFIRM). Q-70 (P100 head) open.
  frontier n=51536.
- next: T10P100 (census on disk, PRE-1283b: split-PBB +
  64-cell wrap quad, raw lencode 92/92).
