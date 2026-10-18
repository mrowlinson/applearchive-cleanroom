# NOTE-sweep2-r5-hb3 (RGRAM py leg 40% green)

- Gate-tip legs so far: C-BUILD PASS w=0, RAWENC 13,
  PBZE 10, LZMA 6, LZ4 4, SMOKE 6, OUTER2 284,
  RB2 47, RAVFRAME 181 — all PASS, zero FAIL.
- RGRAM py battery in flight: 3014 PASS / 0 FAIL
  (~40% of 7536). HYGIENE/CONTAM raw FAIL expected
  (inherit legs, compare-after vs b159 like r4).
- Pins csv at ef51ec3: 7538 lines (=7536 + header
  + trailing, matches commit claim).
