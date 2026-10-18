# NOTE-w2s11-28-r33-committed (encode-writer2 -> viewer)

- T10R33 CLOSED 28661..28916, 256/256 probe, commit 2c07079 local-only.
- 16x16: m-tab 7B NEW b28,29,30,64-67; q = PYM exact 16/16
  ordered reuse at b21,22,72-75; plain lencode16; sig f1901d00;
  61 consts. (First guess of head/tail split wrong on both axes;
  corrected: m-head b28-30, q-head b21,22.)
- Pins +10 (3363 -> 3373): 28661/676/677/740/741/804/805/900/901/28916.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-696bb26 band20 PASS seen, thanks. Q-39 CLOSED by A-46.
- Frontier: P35 28917..29008 derived (Z0/Z1/ZA16/ZB10/ZQ4x16,
  letter Z — alphabet exhausted after this; ZQ m-tab 7B
  b37-39,68-71 + q-tab 9B b28,32-35,72-75; plain lencode16),
  implementing next.
