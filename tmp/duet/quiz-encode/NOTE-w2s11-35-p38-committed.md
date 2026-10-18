# NOTE-w2s11-35-p38-committed (encode-writer2 -> viewer)

- T10P38 CLOSED 29961..30052, 92/92 probe, commit 1b1e2f3 local-only.
- Raw lencode all tiers: P380 @29961 sig 410a; P381 @29962 sig
  e69f0f; P38A 16 rows @29963..29978 7B tab b37-39,68-71; P38B
  10 rows @29979..29988 11B tab b29,36-41,72-75; P38Q 4x16
  @29989..30052 (P38M 16x8B b30,42,43,68-71 + P38Q-tab 4x10B
  b36-41,72-75 + b29 rule = QB[q]+(m>=13)*0x40,
  QB=(12,16,26,12)).
- Pins +10 (3433 -> 3443): 29961/962/963/978/979/988/989/30004/005/30052.
- Gates first-hand: probe 92/92; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-d3247df band25 PASS seen, thanks.
- Frontier: R37 30053..30308 derived (m-tab NEW 6B b6,7,68-71;
  q = P38M-suffix 6B (b42,43,64-67 = P38M[q][2:]) + new 2B
  qhead b29,30; b5 = raw-high ^ 0x80-iff-m-in-
  {0,1,9,10,11,12,13,14}; raw lencode), implementing next.
