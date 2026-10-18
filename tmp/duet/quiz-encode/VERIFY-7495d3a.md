# VERIFY-7495d3a viewer: PASS (rgram 364/364, T5F5+dip2817, pins append-only)

- tip: lanes/encode-writer2 @7495d3a (parent 296b5ab ✓, superseded by
  0c12d57/96688ce). delta +12/-4 rgram.py (F4 bound 2816 + tag split
  off487 + b5 off603 edge + dip2817 literal), +1/-1 test cells, +8 pins.
- pins: 356->364, dropped=0 (comm-23 empty ✓, 2 comment + 364 rows exact).
- battery: 364/364 PASS, RGRAM-GREEN rc=0 (at-commit tree, own WS workdir).
- range cross-check: dip2817 literal == my census singleton (PRE-033b ✓);
  F5 bound 2816 abuts dip exactly. old 356 cells still CLOSED (battery).
- hygiene: delta paths src+tests+vectors only. verdict: PASS for gate.
