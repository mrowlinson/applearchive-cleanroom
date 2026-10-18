# VERIFY-cb301db viewer: PASS (rgram 254/254, T4G=D2b1, pins append-only)

- tip: lanes/encode-writer2 @cb301db (parent bdf1372 ✓, current w2 tip).
  delta +43 rgram.py (T4G: L10 + b5=26 + band-consts + b24 4-cycle +
  b29/30/31 tabs + 36 consts), +1/-1 test cells, +16 pins.
- pins: 238->254, dropped=0 (comm-23 empty ✓, 2 comment + 254 rows exact).
- battery: 254/254 PASS, RGRAM-GREEN rc=0 (at-commit tree, own WS workdir).
- range cross-check: T4G 1801..1864 == my D2b1 EXACT (PRE-017b); their b24
  4-cycle + 4x16 band-consts reproduce my v5d2 rows (b24 4b/6b/8b/ab ✓).
- hygiene: delta paths src+tests+vectors only. verdict: PASS for gate.
