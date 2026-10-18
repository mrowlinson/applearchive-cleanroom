# VERIFY-46db216 (w2 T8 64-tier head) — PASS

- tree: git archive 46db216, EXTRACT-OK. diff vs 4b903c7:
  rgram.py +112/-1, test_rgram.sh 1/1, PINS +18.
- battery: tests/test_rgram.sh => RGRAM-GREEN.
- verdict (first-hand ravbed): dip 8751..8760 = 60B (8750
  64B, 8760 60B, 8761 64B) CONFIRMED — 10-row wide dip.
  b60-63 tab varies across 64-tier rows.
- prior: VERIFY-4b903c7 PASS. VERIFY 100% maintained.
