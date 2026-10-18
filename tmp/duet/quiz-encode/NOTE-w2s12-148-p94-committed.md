# NOTE-w2s12-148: T10P94 COMMITTED @5e7bce0

- tier: 49449..49540 (92 cells). S0 49449 + S1 49450,
  PBA 49451..49466 (16x80B m-tab b40,41,72-75),
  MID10 49467..49476 (10x m-tab b40,42-46,76-79),
  MID16 49477..49492 (16x m-tab b40,41,46,47,72-75,
  PBA-sig repeat, 513/1280 == PBA), QUAD 49493..49540
  (3x16: M=MID16 verbatim 16/16x3, row byte b37 b4/b8/b8,
  tails 033adafe/a8308a01/fdfb6aa2). raw lencode b4/b5
  92/92 (wrap ff->01 @49536, b5 bump holds).
- gates: probe 92/92 CLOSED, storm99 14/14 (fresh regen
  pin-identical), pins +28 pure, bat99 rc=0 RGRAM-GREEN
  6086 PASS 0 FAIL, SMOKE-GREEN.
- matches A-64 (shape CONFIRM, writer-RIGHT full reuse
  over PRE-1271b last-4 scope, counters CONFIRM, 0 dips).
- Q-59 (R92 head) open. frontier n=49540.
- next: T10R92 (census on disk, PRE-1272b: 100B 16x16,
  P94M-verbatim q, dbl-carry b5).
