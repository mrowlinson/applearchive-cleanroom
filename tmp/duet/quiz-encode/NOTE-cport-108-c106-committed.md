# NOTE-cport-108: C106 COMMITTED eadf7cc (band106 T10P94)

- 9507514 partial-merge w2@5e7bce0 (rgram.py +203, PINS +28,
  test N-list 1/1; 1 w2 commit P94, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6086/6086 py + SMOKE-GREEN.
- band106: rgramc.c --upto 49540. transpiler clean first try
  (tables 1759/1763).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3043/3043 GREEN +
  RGRAM-GREEN 6086/6086 py (merge tree, same-tree) +
  RGRAM-GREEN 6086/6086 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 680 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R92 next; == w2 tip now).
