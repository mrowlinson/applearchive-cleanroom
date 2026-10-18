# NOTE-cport-112: C110 COMMITTED eeb1ee5 (band110 T10P96+T10R94)

- 5e72665 partial-merge w2@043e6d3 (rgram.py +227, PINS +52,
  test N-list 1/1; 2 w2 commits P96+R94, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6210/6210 py + SMOKE-GREEN.
- band110: rgramc.c --upto 50492. transpiler clean first try
  (tables 1787/1791).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3105/3105 GREEN +
  RGRAM-GREEN 6210/6210 py (merge tree, same-tree) +
  RGRAM-GREEN 6210/6210 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 690 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P97 next; == w2 tip now).
