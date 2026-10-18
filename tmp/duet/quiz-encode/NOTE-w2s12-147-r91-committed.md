# NOTE-w2s12-147: T10R91 COMMITTED @4fab9ca

- tier: 49193..49448 (256 cells). single 16x16 zone sig
  38fcd5d1, m-tab 6B b34,35,72-75 (ALL NEW), q-tab 7B
  b28,30,31,68-71 = P93M verbatim 16/16 (33rd), b4 =
  (0x53+2off)&FF, b5 = 0x80+(off>=87)+(off>=215)
  dbl-carry, 65 consts, 0 dips.
- gates: probe 256/256 CLOSED, storm98 8/8 (fresh regen
  sha-identical), pins +26 pure, bat98 rc=0 RGRAM-GREEN
  6058 PASS 0 FAIL, SMOKE-GREEN.
- matches A-63 (3/3 CONFIRM). Q-56 MOOT, Q-58/A-64 done.
  frontier n=49448.
- next: T10P94 (census on disk, A-64: shape CONFIRM,
  full 16/16x3 MID16=M reuse, raw lencode 92/92).
