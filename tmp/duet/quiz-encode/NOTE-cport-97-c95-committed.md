# NOTE-cport-97: C95 COMMITTED 4fe183d (band95 T10P84+T10R83)

- 234bf1b partial-merge w2@e0b4455 (rgram.py +216, PINS +46,
  test N-list 1/1; 2 w2 commits P84+R83, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5578/5578 py + SMOKE-GREEN.
- band95: rgramc.c --upto 46316. transpiler clean first try
  (tables 1637/1641).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2789/2789 GREEN +
  RGRAM-GREEN 5578/5578 py (merge tree, same-tree) +
  RGRAM-GREEN 5578/5578 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 642 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P85 7781f12 + R84 when committed).
