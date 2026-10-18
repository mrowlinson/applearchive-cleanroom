# VERIFY-ed5cc51 viewer: PASS (rgram 586/586, T6G cluster G, append-only)

- tip: lanes/encode-writer2 @ed5cc51 (parent 700aee1 ✓, current w2
  tip). delta +124 rgram.py (T6G0/G1/G2/G3-6), +1/-1 test cells,
  +24 pins.
- pins: 562->586, dropped=0 (diff removes 0 ✓, 2 comment + 586
  rows exact).
- battery: 586/586 PASS, RGRAM-GREEN rc=0 (at-commit tree via git
  archive, own WS scratch-viewer6 workdir).
- range cross-check: new cells 4905/4907/4908/4922/4923/4932/4933/
  4949/4965/4981/4992/4996 == v5u flip census EXACT (triple
  4905-07 + doubles 4923/4933 + 16-bands 4949/4965/4981). cont
  0..4996 CLOSED.
- hygiene: delta paths src+tests+vectors only. verdict: PASS.
