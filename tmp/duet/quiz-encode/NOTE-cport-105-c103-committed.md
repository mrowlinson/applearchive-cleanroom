# NOTE-cport-105: C103 COMMITTED 19ab457 (band103 T10P92+T10B91)

- 73df8f0 partial-merge w2@5ff15f1 (rgram.py +243, PINS +66,
  test N-list 1/1; 2 w2 commits P92+B91, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5996/5996 py + SMOKE-GREEN.
- band103: rgramc.c --upto 49100. transpiler clean first try
  (tables 1735/1739; B91 BLOCK-regime handled).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2998/2998 GREEN +
  RGRAM-GREEN 5996/5996 py (merge tree, same-tree) +
  RGRAM-GREEN 5996/5996 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 674 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P93 c4e3cfa + B92 when committed).
