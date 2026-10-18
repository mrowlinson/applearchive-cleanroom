# NOTE-cport-117: C115 COMMITTED 99355a0 (band115 T10P99)

- 2058487 partial-merge w2@91c502b (rgram.py +174, PINS +30,
  test N-list 1/1; 1 w2 commit P99, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6342/6342 py + SMOKE-GREEN.
- band115: rgramc.c --upto 51280. transpiler clean first try
  (tables 1822/1826).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3171/3171 GREEN +
  RGRAM-GREEN 6342/6342 py (merge tree, same-tree) +
  RGRAM-GREEN 6342/6342 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 700 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R97 next; == w2 tip now).
