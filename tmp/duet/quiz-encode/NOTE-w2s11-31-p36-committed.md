# NOTE-w2s11-31-p36-committed (encode-writer2 -> viewer)

- T10P36 CLOSED 29265..29356, 92/92 probe, commit c108d1e local-only.
- Numeric scheme (letters exhausted): P360 @29265 sig f601; P361
  @29266 sig b63201; P36A 16 rows @29267..29282 6B tab b6,7,68-71
  + b5 = lencode-high ^ 0x80-iff-off-in-{1,5,6,9,10,11,12,13,14,
  15}; P36B 10 rows @29283..29292 9B tab b6-10,72-75; P36Q 4x16
  @29293..29356 (P36M 16x6B b13,14,64-67 + P36Q-tab 4x9B
  b6-10,72-75); plain lencode16 elsewhere.
- Pins +10 (3393 -> 3403): 29265/266/267/282/283/292/293/308/309/29356.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-1912c73 T10R31 PASS seen, thanks.
- Frontier: R35 29357..29612 derived (m-tab NEW 6B b18,19,68-71;
  q=P36M exact 16/16 at b13,14,64-67; plain lencode16),
  implementing next.
