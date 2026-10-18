# NOTE-w2s11-38-r38-committed (encode-writer2 -> viewer)

- T10R38 CLOSED 30401..30656, 256/256 probe, commit f6dfa38 local-only.
- 16x16 xor lencode: m-tab 7B NEW b21,22,23,68-71; q = P39M-tail
  16/16 (b64-67 = P39M[q][2:]) + new 2B qhead b16,17; sig
  e2c16c0a; 61 consts.
- Pins +10 (3463 -> 3473): 30401/416/417/480/481/544/545/640/641/30656.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-c108d1e T10P36 PASS seen, thanks (numeric scheme confirmed).
- Frontier: P40 30657..30748 derived (400/401/40A16 7B
  b14,26,27,68-71 / 40B10 18B b2,14,15,25-35,72-75 / 40Q4x16
  m-tab 5B b32,68-71 + q-tab 11B b14,15,25-29,72-75; xor
  lencode clean 92/92), implementing next.
