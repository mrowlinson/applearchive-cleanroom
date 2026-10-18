# NOTE-cport-107: C105 COMMITTED 8f6c326 (band105 T10R91)

- 79abb83 partial-merge w2@4fab9ca (rgram.py +51, PINS +26,
  test N-list 1/1; 1 w2 commit R91, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6058/6058 py + SMOKE-GREEN.
- band105: rgramc.c --upto 49448. transpiler clean first try
  (tables 1748/1752).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3029/3029 GREEN +
  RGRAM-GREEN 6058/6058 py (merge tree, same-tree) +
  RGRAM-GREEN 6058/6058 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 678 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P94 next; == w2 tip now).
