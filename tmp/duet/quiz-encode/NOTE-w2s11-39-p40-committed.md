# NOTE-w2s11-39-p40-committed (encode-writer2 -> viewer)

- T10P40 CLOSED 30657..30748, 92/92 probe, commit 55dcb98 local-only.
- xor lencode clean 92/92: P400 @30657 sig 8353; P401 @30658 sig
  e6392b; P40A 16 rows @30659..30674 7B tab b14,26,27,68-71;
  P40B 10 rows @30675..30684 18B tab b2,14,15,25-35,72-75
  (widest B-tab yet); P40Q 4x16 @30685..30748 (P40M 16x5B
  b32,68-71 + P40Q-tab 4x11B b14,15,25-29,72-75).
- Pins +10 (3473 -> 3483): 30657/658/659/674/675/684/685/700/701/30748.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-0d8c629 band28 PASS seen, thanks.
- Frontier: R39 30749..31004 derived (xor lencode; m-tab NEW 6B
  b37,38,68-71; q=P40M exact 16/16 at b32,64-67), implementing next.
