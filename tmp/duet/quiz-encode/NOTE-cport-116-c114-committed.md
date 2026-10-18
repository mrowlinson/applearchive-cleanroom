# NOTE-cport-116: C114 COMMITTED c343ea0 (band114 T10R96)

- 6df65ce partial-merge w2@ac2e8f5 (rgram.py +71, PINS +26,
  test N-list 1/1; 1 w2 commit R96, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6312/6312 py + SMOKE-GREEN.
- band114: rgramc.c --upto 51188. transpiler clean first try
  (tables 1812/1816).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3156/3156 GREEN +
  RGRAM-GREEN 6312/6312 py (merge tree, same-tree) +
  RGRAM-GREEN 6312/6312 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 698 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P99 next; == w2 tip now).
