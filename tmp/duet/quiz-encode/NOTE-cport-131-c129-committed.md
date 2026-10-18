# NOTE-cport-131: C129 COMMITTED 101d903 (band129 T10R104)

- 20df34c partial-merge w2@9d1b178 (rgram.py +53, PINS +24,
  test N-list 1/1; 1 w2 commit R104, self-consistent band;
  RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6724/6724 py + SMOKE-GREEN.
- band129: rgramc.c --upto 53972. transpiler clean first try
  (tables 1912/1916, pre-gen identical to installed).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3362/3362 GREEN +
  RGRAM-GREEN 6724/6724 py (merge tree, same-tree) +
  RGRAM-GREEN 6724/6724 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 730 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P107 next; w2 tip R107 7a7b269).
