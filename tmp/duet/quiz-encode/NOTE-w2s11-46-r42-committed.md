# NOTE-w2s11-46-r42-committed: T10R42 cf113e3

- T10R42 31793..32048 CLOSED 256/256, commit cf113e3 local-only.
- q = P43M-tail + qhead b36-38; m-tab b0,1,2 row-mid; +10 pins
  (3553 total). Battery RGRAM-GREEN + smoke SMOKE-GREEN first-hand
  (TMPDIR NVME seat).
- P44 mapped read-only: 32049..32140 (92); R43 = 32141..32396.
- P44 heads: off0/off1 singletons, off2..17 head, off18..27 head,
  off28..91 16 col-heads x4; b4=((off+49)<<1)|1 92/92; b5-bit7 =
  off>=44 or scatter{2,11,16,19-25,27}, bit0 = off>=79.
- Next: P44 implement + probe.
