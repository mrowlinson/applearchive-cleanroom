# NOTE-cport-114: C112 COMMITTED 917fac8 (band112 T10R95)

- 4313132 partial-merge w2@d882c7c (rgram.py +53, PINS +26,
  test N-list 1/1; 1 w2 commit R95, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6264/6264 py + SMOKE-GREEN.
- band112: rgramc.c --upto 50840. transpiler clean first try
  (tables 1799/1803).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3132/3132 GREEN +
  RGRAM-GREEN 6264/6264 py (merge tree, same-tree) +
  RGRAM-GREEN 6264/6264 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 694 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P98 next; == w2 tip now).
