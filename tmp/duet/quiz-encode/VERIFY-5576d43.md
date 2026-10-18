# VERIFY-5576d43 w2 T9U1 16x16 12653..12908 PASS

- at-commit tree (git archive 5576d43): test_rgram.sh
  RGRAM-GREEN (PASS g-z12908), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +44 (T9U1 16x16 tab
  b9,10,b17-21 + 5B words b13,b64-67; b5
  62->63->64), PINS +20 (1528 total).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-12908):
  len=84, sha=14095858... == pinned g-z12908 EXACT.
- verdict: PASS. VERIFY 33/33 current.
