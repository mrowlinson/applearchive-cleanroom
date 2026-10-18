# NOTE-cport-121: C119 COMMITTED 0aea685 (band119 T10R99)

- 0323580 partial-merge w2@2ec241d (rgram.py +53, PINS +26,
  test N-list 1/1; 1 w2 commit R99, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6476/6476 py + SMOKE-GREEN.
- band119: rgramc.c --upto 52232. transpiler clean first try
  (tables 1849/1853).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3238/3238 GREEN +
  RGRAM-GREEN 6476/6476 py (merge tree, same-tree) +
  RGRAM-GREEN 6476/6476 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 710 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P102 next; == w2 tip now).
