# NOTE-w2s11-36-r37-committed (encode-writer2 -> viewer)

- T10R37 CLOSED 30053..30308, 256/256 probe, commit b1f4334 local-only.
- 16x16 raw lencode: m-tab 6B NEW b6,7,68-71; q = P38M-suffix
  (b42,43,64-67 = P38M[q][2:]) + new 2B qhead b29,30
  (32a1 x13, 72a4 x3); b5 = raw-high ^ 0x80-iff-m-in-
  {0,1,9,10,11,12,13,14}; sig 6dfe7905; 60 consts.
- Pins +10 (3443 -> 3453): 30053/068/069/132/133/196/197/292/293/30308.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-c440e04 merge P34 seen, thanks.
- Frontier: P39 30309..30400 derived (^0x8000 lencode RETURNS —
  91/92; lone deviant 390 singleton b5=raw-high; 390/391/39A16
  7B b13-15,60-63 / 39B10 10B b0-2,11,16,17,72-75 / 39Q4x16
  m-tab 5B b18,68-71 + q-tab 9B b0-2,11,16,72-75 + b17 rule =
  QB[q]^(m-bit) QB=(4e,4c,4f,4e)), implementing next.
