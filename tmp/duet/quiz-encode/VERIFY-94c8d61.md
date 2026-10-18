# VERIFY-94c8d61 (w1 C-parity test) — PASS

- tree: git archive 94c8d61, EXTRACT-OK. diff vs 34df169:
  tests/test_lz4_c.sh +25 (new file only; no src change).
- batteries: test_lz4_c.sh => LZ4C-GREEN; test_lz4.sh =>
  LZ4-GREEN (re-gated, still green).
- closes VERIFY-34df169 recommendation (committed C
  harness now in tree). w1 tip current.
