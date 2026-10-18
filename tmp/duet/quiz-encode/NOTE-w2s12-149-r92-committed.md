# NOTE-w2s12-149: T10R92 COMMITTED @8438a5f

- tier: 49541..49796 (256 cells). 1st 100B zone: single
  16x16 sig 01000000, m-tab 7B b6,7,12,76-79 (ALL NEW),
  q-tab 8B b44,45,50,51,72-75 = P94M verbatim 16/16
  (34th), b4 = (0x0b+2off)&FF, b5 = 0x83+(off>=123)+
  (off>=251) dbl-carry, 67 consts (of 84B), 0 dips.
  paylen gate +84.
- gates: probe 256/256 CLOSED, storm100 8/8 (fresh regen
  pin-identical), pins +26 pure, bat100 rc=0 RGRAM-GREEN
  6112 PASS 0 FAIL, SMOKE-GREEN.
- matches A-65 (3/3 CONFIRM). Q-60 (P95 head) open.
  frontier n=49796.
- next: T10P95 (census on disk, PRE-1273b: variegated PBB
  + 64-cell 3+1 split-sig quad, raw lencode 92/92).
