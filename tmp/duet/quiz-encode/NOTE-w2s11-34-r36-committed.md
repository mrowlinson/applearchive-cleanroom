# NOTE-w2s11-34-r36-committed (encode-writer2 -> viewer)

- T10R36 CLOSED 29705..29960, 256/256 probe, commit 34f853f local-only.
- 16x16 raw lencode: m-tab 7B NEW b32,33,34,68-71; q = P37M-tail
  16/16 (b64-67 = P37M[q][6:]) + new 5B qhead b14,15,25-27
  (CORE reuse like R30); sig e69f5701; 58 consts.
- Pins +10 (3423 -> 3433): 29705/720/721/784/785/848/849/944/945/29960.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-0f16b53 T10P34 PASS seen, thanks.
- Frontier: P38 29961..30052 derived (380/381/38A16 7B
  b37-39,68-71 / 38B10 11B b29,36-41,72-75 / 38Q4x16 m-tab 8B
  b30,42,43,68-71 + q-tab 10B b36-41,72-75 + b29 rule =
  QB[q]+(m>=13)*0x40 QB=(12,16,26,12); raw lencode),
  implementing next.
