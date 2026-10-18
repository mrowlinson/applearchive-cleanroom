# VERIFY-296b5ab viewer: PASS (rgram 356/356, T5F3/F4, pins append-only)

- tip: lanes/encode-writer2 @296b5ab (parent d30f354 ✓, current w2 tip).
  delta +86 rgram.py (T5F3/F4: tabs + k2 segs + b11 cycle3 + F3-walk),
  +1/-1 test cells, +18 pins.
- pins: 338->356, dropped=0 (comm-23 empty ✓, 2 comment + 356 rows exact).
- battery: 356/356 PASS, RGRAM-GREEN rc=0 (at-commit tree, own WS workdir).
- range cross-check: 2497..2700 == my F3/F4/F-band EXACT (PRE-034b tabs/
  quads + PRE-022b F-band; their b5 flips @347/475 = my 53->54@2560
  (off 347? 2560-2213=347 ✓) + F-band b5 54->55@2688 (off 475 ✓)).
- hygiene: delta paths src+tests+vectors only. verdict: PASS for gate.
