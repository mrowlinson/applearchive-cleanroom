# VERIFY-cd3037c merge86 P75+R74 (n<=43184): PASS

## first-hand (at-commit tree v-cd3037c)
- parents: 95e9d30 (band85) + 1018e76 (R74).
- C byte-identical to band85 (rgramc.c/h cmp); py+PINS
  byte-identical to R74 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band85 = N-list line only
  (extended thru 43184). faithful partial-merge shape.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5164 pins, 0 FAIL).
- C parity: band85 C (n<=42836) VERIFY-95e9d30 GREEN; the
  P75+R74 pins 42837..43184 are correctly out of its scope
  (own probes w/ seat band85 bin: 42836 CLOSED T10R73B
  off=255; 42837/43184 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b.

## verdict: PASS (faithful merge, no skew)
