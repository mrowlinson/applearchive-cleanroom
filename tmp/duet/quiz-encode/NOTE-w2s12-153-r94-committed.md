# NOTE-w2s12-153: T10R94 COMMITTED @043e6d3

- tier: 50237..50492 (256 cells). 3rd 100B zone: single
  16x16 sig 01000000, m-tab 8B b44-47,72-75 (ALL NEW),
  q-tab 6B b38,39,76-79 = P96M verbatim 16/16 (36th),
  b4 = (0x7b+2off)&FF, b5 = 0x88+(off>=67)+(off>=195)
  dbl-carry, 68 consts (of 84B), 0 dips.
- gates: probe 256/256 CLOSED, storm104 8/8 (fresh regen
  pin-identical), pins +26 pure, bat104 rc=0 RGRAM-GREEN
  6210 PASS 0 FAIL, SMOKE-GREEN.
- Q-63 (R94) + Q-64 (P97) open. frontier n=50492.
- next: T10P97 (census on disk, PRE-1277b: split-PBB +
  64-cell 1+3 quad, raw lencode 92/92).
