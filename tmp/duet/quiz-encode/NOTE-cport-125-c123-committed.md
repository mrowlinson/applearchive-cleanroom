# NOTE-cport-125: C123 COMMITTED 9e30e0b (band123 T10R101)

- cb0ab6f partial-merge w2@6824096 (rgram.py +53, PINS +26,
  test N-list 1/1; 1 w2 commit R101, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6576/6576 py + SMOKE-GREEN.
- band123: rgramc.c --upto 52928. transpiler clean first try
  (tables 1875/1879).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3288/3288 GREEN +
  RGRAM-GREEN 6576/6576 py (merge tree, same-tree) +
  RGRAM-GREEN 6576/6576 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 718 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P104 next; == w2 tip now).
