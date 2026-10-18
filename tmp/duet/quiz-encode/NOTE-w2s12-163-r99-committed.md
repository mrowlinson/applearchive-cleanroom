# NOTE-w2s12-163: T10R99 COMMITTED @2ec241d

- tier: 51977..52232 (256 cells). 8th 100B zone, NEW sig
  04000000: single 16x16, m-tab 6B b38,39,76-79 (ALL NEW),
  q-tab 6B b32,33,72-75 = P101M verbatim 16/16 (41st),
  b4 = (0x13+2off)&FF, b5 = 0x96+(off>=119)+(off>=247)
  dbl-carry, 70 consts (of 84B), 0 dips.
- gates: probe 256/256 CLOSED, storm114 8/8 (fresh regen
  pin-identical), pins +26 pure, bat114 rc=0 RGRAM-GREEN
  6476 PASS 0 FAIL, SMOKE-GREEN.
- matches A-79 (3/3 CONFIRM). Q-74 (P102 head) open.
  frontier n=52232.
- next: T10P102 (census on disk, PRE-1287b: split-PBB +
  3+1 split-sig quad, raw lencode 92/92).
