# NOTE-cport-124: C122 COMMITTED 12b8957 (band122 T10P103)

- 843c423 partial-merge w2@df786d9 (rgram.py +183, PINS +24,
  test N-list 1/1; 1 w2 commit P103, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6550/6550 py + SMOKE-GREEN.
- band122: rgramc.c --upto 52672. transpiler clean first try
  (tables 1873/1877).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3275/3275 GREEN +
  RGRAM-GREEN 6550/6550 py (merge tree, same-tree) +
  RGRAM-GREEN 6550/6550 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 716 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R101 next; == w2 tip now).
