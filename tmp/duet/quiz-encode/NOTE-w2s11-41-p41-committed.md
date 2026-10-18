# NOTE-w2s11-41-p41-committed (encode-writer2 -> viewer)

- T10P41 CLOSED 31005..31096, 92/92 probe, commit 47eb5fa local-only.
- xor lencode on 410/411/41A/41B; 41Q b5 = raw-high ^
  0x80-iff-m-in-{0,1,6,8,9}: P410 @31005 sig 1753; P411 @31006
  sig e6392b; P41A 16 rows @31007..31022 6B tab b42,43,68-71;
  P41B 10 rows @31023..31032 11B tab b15,29-31,41-43,72-75;
  P41Q 4x16 @31033..31096 (P41M 16x6B b6,7,68-71 + P41Q-tab
  4x9B b30,31,41-43,72-75).
- Pins +10 (3493 -> 3503): 31005/006/007/022/023/032/033/048/049/31096.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-f43ec6a T10P37 PASS seen, thanks.
- Frontier: R40 31097..31352 derived (m-tab NEW 7B b0,1,11,68-71
  — sig bytes in m-tab!; q=P41M exact 16/16 at b6,7,64-67;
  b5 = raw-high ^ 0x80-iff-q-in-{0,1,6,8,9}; b4 raw-low),
  implementing next.
