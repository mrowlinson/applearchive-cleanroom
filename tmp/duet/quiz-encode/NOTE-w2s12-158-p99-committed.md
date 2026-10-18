# NOTE-w2s12-158: T10P99 COMMITTED @91c502b

- tier: 51189..51280 (92 cells). S0 51189 (sig 19870300)
  + S1 51190, PBA 51191..51206 (16x m-tab b34,35,72-75,
  b5 wraps inside @51200), PBB 51207..51216 (10x
  ALTERNATING sigs exact order, 27B m-tab, 28 VPOS),
  QUAD 51217..51280 (4x16 single sig: M 7B b40,41,42,
  72-75, row1 rb unique, rows0,2,3 shared rb, tails
  8656a903/82a174a3/0858a903/8a58a903). raw lencode
  92/92.
- gates: probe 92/92 CLOSED, storm109 15/15 (fresh regen
  pin-identical), pins +30 pure, bat109 rc=0 RGRAM-GREEN
  6342 PASS 0 FAIL, SMOKE-GREEN.
- matches A-74 (3/3 CONFIRM). A-75: R97 3/3 CONFIRM.
  Q-drain 0. frontier n=51280.
- next: T10R97 (census on disk, PRE-1282b: 100B 16x16,
  P99M-verbatim q (39th), dbl-carry b5).
