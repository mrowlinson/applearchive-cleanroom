# NOTE-cport-120: C118 COMMITTED 31e41ed (band118 T10P101)

- 25c6f81 partial-merge w2@41af7b2 (rgram.py +174, PINS +28,
  test N-list 1/1; 1 w2 commit P101, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6450/6450 py + SMOKE-GREEN.
- band118: rgramc.c --upto 51976. transpiler clean first try
  (tables 1847/1851).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3225/3225 GREEN +
  RGRAM-GREEN 6450/6450 py (merge tree, same-tree) +
  RGRAM-GREEN 6450/6450 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 708 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R99 next; == w2 tip now).
