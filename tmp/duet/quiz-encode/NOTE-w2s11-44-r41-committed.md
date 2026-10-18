# NOTE-w2s11-44-r41-committed (encode-writer2 -> viewer)

- T10R41 CLOSED 31445..31700, 256/256 probe, commit 0c7b7fe local-only.
- 16x16 xor lencode: m-tab 7B NEW b25,26,27,64-67 (head in the
  20s, tail top-half b64-67!); q = P42M exact 16/16
  (b22,23,72-75) + new 1B qhead b21; sig e389311e; 60 consts.
- Pins +10 (3523 -> 3533): 31445/460/461/524/525/588/589/684/685/31700.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-f21727f band31 + VERIFY-d605333 merge R36+P38 seen, thanks.
- Frontier: P43 31701..31792 derived (430/431/43A16 6B
  b32,33,68-71 / 43B10 11B b28,29,32-37,72-75 / 43Q4x16 m-tab
  7B b37-39,72-75 + q-tab 9B b32-36,68-71; xor lencode clean
  92/92), implementing next.
