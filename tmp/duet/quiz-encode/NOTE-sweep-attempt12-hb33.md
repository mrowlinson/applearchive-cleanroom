# NOTE-sweep-attempt12-hb33: order self-correction + 2 gates filed

- CAUGHT own oldest-first violation: ran R27 battery (16:02:42)
  before noticing band16 4ad7a4d (16:00:58) older. Repaired: band16
  fully gated + FILED FIRST (PASS-functional), R27 filed after.
  Lesson: pull BOTH lane dates BEFORE launching each gate.
- Filed: GATE-4ad7a4d (band16: bounds 363/363, tables 982/982,
  parity 1592/1592 FULL, C-side 3184/3184, storm 6/6) +
  GATE-e5fb39a (R27 PASS-individual 3220/3220, "3221" 16th off-by-one).
- Rebuilding full queue with dates below; next oldest-first.
