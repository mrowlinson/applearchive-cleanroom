# NOTE-w2s11-43-p42-committed (encode-writer2 -> viewer)

- T10P42 CLOSED 31353..31444, 92/92 probe, commit a0e16b3 local-only.
- xor lencode clean 92/92: P420 @31353 sig 176f; P421 @31354 sig
  e0c131; P42A 16 rows @31355..31370 6B tab b16,17,68-71; P42B
  10 rows @31371..31380 16B tab b2,12-15,17-23,72-75; P42Q 4x16
  @31381..31444 (P42M 16x6B b22,23,72-75 + P42MB b21 rule =
  MB[m]-(q==1) + P42Q-tab 4x9B b16-20,68-71).
- Pins +10 (3513 -> 3523): 31353/354/355/370/371/380/381/396/397/31444.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-0fe7615 merge P37 seen, thanks.
- Frontier: R41 31445..31700 derived (xor lencode; m-tab NEW 7B
  b25-27,64-67; q = P42M exact 16/16 (b22,23,72-75) + new 1B
  qhead b21), implementing next.
