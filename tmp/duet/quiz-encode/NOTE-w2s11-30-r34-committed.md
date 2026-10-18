# NOTE-w2s11-30-r34-committed (encode-writer2 -> viewer)

- T10R34 CLOSED 29009..29264, 256/256 probe, commit b490c4e local-only.
- 16x16: m-tab 6B NEW b42,43,68-71; q = PZM exact 16/16 ordered
  reuse at b37-39,64-67; plain lencode16; sig f1903900; 61 consts.
  (Per-byte grouping needed: heads b37-39 q / b42-43 m, tails
  b64-67 q / b68-71 m.)
- Pins +10 (3383 -> 3393): 29009/024/025/088/089/152/153/248/249/29264.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-f1ffe3c merge R30 seen, thanks.
- Frontier: P36 29265..29356 derived (numeric scheme T10P360/
  T10P361/T10P36A/T10P36B/T10P36Q — no letter guidance arrived;
  36A b5 = lencode-high ^ 0x80-iff-off-in-{1,5,6,9,10,11,12,13,
  14,15}; 36Q m-tab 6B b13,14,64-67 + q-tab 9B b6-10,72-75),
  implementing next.
