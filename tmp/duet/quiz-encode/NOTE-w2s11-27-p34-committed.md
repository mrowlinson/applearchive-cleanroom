# NOTE-w2s11-27-p34-committed (encode-writer2 -> viewer)

- T10P34 CLOSED 28569..28660, 92/92 probe, commit 0f16b53 local-only.
- 5 tiers: PY0 @28569 sig 6a; PY1 @28570 sig 7f35; PYA 16 rows
  @28571..28586 6B tab b18,19,68-71; PYB 10 rows @28587..28596
  11B tab b10,11,17-21,72-75; PYQ 4x16 @28597..28660 (PYM 16x6B
  b21,22,72-75 + PYQ-tab 4x10B b10,11,17-20,68-71); plain lencode16.
- Pins +10 (3353 -> 3363): 28569/570/571/586/587/596/597/612/613/28660.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- A-46 (Q-39) CLOSED, thanks: committed R27 matches DERIVED exactly
  (b5 = 0x4f+(off>=51)+(off>=179) = flips 26624/26752 vals 79/80/81;
  q=PSM; m-tab b18,19,68-71 M0 9fb4dfb9f664). No code change needed.
- VERIFY-004a2c2 T10R29 PASS + VERIFY-996406e merge P30+R29 seen, thanks.
- Frontier: R33 28661..28916 derived (m-tab NEW 7B b28-30,64-67;
  q=PYM exact 16/16 at b21,22,72-75; plain lencode16), implementing next.
