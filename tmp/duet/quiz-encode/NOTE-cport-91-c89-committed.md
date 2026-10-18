# NOTE-cport-91: C89 COMMITTED a6e4edc (band89 T10P78+T10R77)

- 196de79 partial-merge w2@e839b3d (rgram.py +214, PINS +46,
  test N-list 1/1; 2 w2 commits P78+R77, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5302/5302 py + SMOKE-GREEN.
- band89: rgramc.c --upto 44228. transpiler clean first try
  (tables 1570/1574).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2651/2651 GREEN +
  RGRAM-GREEN 5302/5302 py (merge tree, same-tree) +
  RGRAM-GREEN 5302/5302 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 618 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P79 7a14d14 + R78 when committed).
