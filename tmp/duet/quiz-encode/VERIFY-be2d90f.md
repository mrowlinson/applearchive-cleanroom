# VERIFY-be2d90f viewer: PASS (rgram 650/650, T6K cluster K, pins append-only)

- tip: lanes/encode-writer2 @be2d90f (parent 30b6a16 ✓, current w2 tip).
  delta +114 rgram.py (T6K: literals + K1/K2 row-tabs + shared b40-43 tab
  + k2 + b5 edge), +1/-1 test cells, +24 pins.
- pins: 626->650, dropped=0 (comm-23 empty ✓, 2 comment + 650 rows exact).
- battery: 650/650 PASS, RGRAM-GREEN rc=0 (at-commit tree, own WS workdir).
- range cross-check: 5601..5692 == PRE-057b/c EXACT (both seats' tabs
  byte-identical, independently derived; b5 flip @5632 ✓).
- hygiene: delta paths src+tests+vectors only. verdict: PASS for gate.
