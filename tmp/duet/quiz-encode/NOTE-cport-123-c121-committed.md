# NOTE-cport-123: C121 COMMITTED f7cf078 (band121 T10R100)

- 0a076a6 partial-merge w2@37c9d2f (rgram.py +53, PINS +26,
  test N-list 1/1; 1 w2 commit R100, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6526/6526 py + SMOKE-GREEN.
- band121: rgramc.c --upto 52580. transpiler clean first try
  (tables 1862/1866).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3263/3263 GREEN +
  RGRAM-GREEN 6526/6526 py (merge tree, same-tree) +
  RGRAM-GREEN 6526/6526 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 714 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P103 next; == w2 tip now).
