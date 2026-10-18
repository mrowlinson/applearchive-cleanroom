# NOTE-cport-95: C93 COMMITTED 43b0519 (band93 T10P82+T10R81)

- 235f271 partial-merge w2@b759db1 (rgram.py +215, PINS +46,
  test N-list 1/1; 2 w2 commits P82+R81, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5486/5486 py + SMOKE-GREEN.
- band93: rgramc.c --upto 45620. transpiler clean first try
  (tables 1615/1619).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2743/2743 GREEN +
  RGRAM-GREEN 5486/5486 py (merge tree, same-tree) +
  RGRAM-GREEN 5486/5486 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 634 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P83 bd42dc0 + R82 when committed).
