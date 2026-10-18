# NOTE-w2s11-40-r39-committed (encode-writer2 -> viewer)

- T10R39 CLOSED 30749..31004, 256/256 probe, commit 0cda438 local-only.
- 16x16 xor lencode: m-tab 6B NEW b37,38,68-71; q = P40M exact
  16/16 ordered reuse at b32,64-67; sig e6396b0a; 63 consts.
- Pins +10 (3483 -> 3493): 30749/764/765/828/829/892/893/988/989/31004.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-a2070eb merge P36 seen, thanks.
- Frontier: P41 31005..31096 derived (410/411/41A16 6B
  b42,43,68-71 / 41B10 11B b15,29-31,41-43,72-75 / 41Q4x16
  m-tab 6B b6,7,68-71 + q-tab 9B b30,31,41-43,72-75 + b5 =
  raw-high ^ 0x80-iff-m-in-{0,1,6,8,9}; xor lencode on
  410/411/41A/41B), implementing next.
