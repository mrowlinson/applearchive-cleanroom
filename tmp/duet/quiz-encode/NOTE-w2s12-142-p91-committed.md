# NOTE-w2s12-142: T10P91 COMMITTED @182438b

- tier: 48405..48496 (92 cells). S0 48405 + S1 48406, P91A
  48407..48422 (16x80B m-tab b26,34,35,72-75), P91B 48423..
  48432 (10x80B single-sig m-tab b25-27,33-37,76-79), P91Q
  48433..48496 (4x16 clean quad: M 6B b40,41,72-75 + tails
  b76-79 ONLY, raw lencode b4=0x63+2off no wrap, b5=0x7a).
- gates: probe 92/92 CLOSED, storm 9/9, pins +34 pure, bat92
  rc=0 RGRAM-GREEN 0 FAIL, SMOKE-GREEN — all first-hand.
- matches PRE-1265b. A-61 consumed (R89 agrees all legs).
  Q-55 (R90) filed. frontier n=48496.
- next: T10R90 (gen validated 52L, census on disk).
