# NOTE-cport-113: C111 COMMITTED 5dca1be (band111 T10P97)

- 8147e8f partial-merge w2@6eade74 (rgram.py +174, PINS +28,
  test N-list 1/1; 1 w2 commit P97, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6238/6238 py + SMOKE-GREEN.
- band111: rgramc.c --upto 50584. transpiler clean first try
  (tables 1797/1801).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3119/3119 GREEN +
  RGRAM-GREEN 6238/6238 py (merge tree, same-tree) +
  RGRAM-GREEN 6238/6238 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 692 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R95 next; == w2 tip now).
