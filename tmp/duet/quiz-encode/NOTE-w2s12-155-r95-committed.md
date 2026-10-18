# NOTE-w2s12-155: T10R95 COMMITTED @d882c7c

- tier: 50585..50840 (256 cells). 4th 100B zone: single
  16x16 sig 01000000, m-tab 8B b8,9,10,15,76-79 (ALL NEW),
  q-tab 6B b6,7,72-75 = P97M verbatim 16/16 AT SAME POS
  (37th, 1st same-pos), b4 = (0x33+2off)&FF, b5 = 0x8b+
  (off>=103)+(off>=231) dbl-carry, 68 consts (of 84B),
  0 dips.
- gates: probe 256/256 CLOSED, storm106 8/8 (fresh regen
  pin-identical), pins +26 pure, bat106 rc=0 RGRAM-GREEN
  6264 PASS 0 FAIL, SMOKE-GREEN.
- matches A-71 (3/3 CONFIRM). Q-66 (P98 head) open.
  frontier n=50840.
- next: T10P98 (census on disk, PRE-1279b: single-sig
  head + 64-cell 3+1 quad, raw lencode 92/92).
