# NOTE-cport-118: C116 COMMITTED 6606cc1 (band116 T10R97+T10P100)

- e90d885 partial-merge w2@0a2c6d6 (rgram.py +227, PINS +54,
  test N-list 1/1; 2 w2 commits R97+P100, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6396/6396 py + SMOKE-GREEN.
- band116: rgramc.c --upto 51628. transpiler clean first try
  (tables 1834/1838).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3198/3198 GREEN +
  RGRAM-GREEN 6396/6396 py (merge tree, same-tree) +
  RGRAM-GREEN 6396/6396 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 704 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R98 next; == w2 tip now).
