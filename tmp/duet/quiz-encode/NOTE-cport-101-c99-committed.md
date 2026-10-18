# NOTE-cport-101: C99 COMMITTED 559b878 (band99 T10P88+T10R87)

- a8b6efd partial-merge w2@8b45bd4 (rgram.py +220, PINS +46,
  test N-list 1/1; 2 w2 commits P88+R87, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5762/5762 py + SMOKE-GREEN.
- band99: rgramc.c --upto 47708. transpiler clean first try
  (tables 1686/1690).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2881/2881 GREEN +
  RGRAM-GREEN 5762/5762 py (merge tree, same-tree) +
  RGRAM-GREEN 5762/5762 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 658 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P89 8ff3ade novel half-quad shape +
  R88 when committed).
