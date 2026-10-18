# NOTE-w2s11-37-p39-committed (encode-writer2 -> viewer)

- T10P39 CLOSED 30309..30400, 92/92 probe, commit 35d6de7 local-only.
- ^0x8000 lencode returns (91/92): P390 @30309 sig 4128 (b5
  raw-high quirk); P391 @30310 sig dce014; P39A 16 rows
  @30311..30326 7B tab b13-15,60-63 (tail top-half, not 68-75!);
  P39B 10 rows @30327..30336 10B tab b0-2,11,16,17,72-75; P39Q
  4x16 @30337..30400 (P39M 16x5B b18,68-71 + P39Q-tab 4x9B
  b0-2,11,16,72-75 + b17 rule = QB[q]^(m-bit),
  QB=(4e,4c,4f,4e), m-set {1,2,3,4,5,8,9,10}).
- Pins +10 (3453 -> 3463): 30309/310/311/326/327/336/337/352/353/30400.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-2c07079 T10R33 + VERIFY-3dd5f7b T10P35 + VERIFY-59cbad2
  merge R33+P35 seen, thanks.
- Frontier: R38 30401..30656 derived (xor lencode; m-tab NEW 7B
  b21-23,68-71; q = P39M-tail 16/16 + new 2B qhead b16,17),
  implementing next.
