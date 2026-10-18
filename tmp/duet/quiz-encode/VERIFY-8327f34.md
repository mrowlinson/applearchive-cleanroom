# VERIFY-8327f34: PASS (MIX pattern cells, additive, honest)

- scope first-hand: tests +19 (MIX helper + 3 calls), pins +8 rows. additive.
- code: MIX = fixed 50k-zeros+50k-seed11 input + AAR + header-walk S/C pattern + asserts + sha.
  pattern pin CCCCCSSSSSS x3 corroborates NOTE-w2s2-11 per GATE-47897e2. honest.
- wall: 0 hits (own grep). covered-within GATE-47897e2 PASS; no FLAG.
