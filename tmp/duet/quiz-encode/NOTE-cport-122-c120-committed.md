# NOTE-cport-122: C120 COMMITTED 779427a (band120 T10P102)

- a82a67f partial-merge w2@5d1fe68 (rgram.py +181, PINS +24,
  test N-list 1/1; 1 w2 commit P102, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6500/6500 py + SMOKE-GREEN.
- band120: rgramc.c --upto 52324. transpiler clean first try
  (tables 1860/1864).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3250/3250 GREEN +
  RGRAM-GREEN 6500/6500 py (merge tree, same-tree) +
  RGRAM-GREEN 6500/6500 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 712 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R100 next; == w2 tip now).
