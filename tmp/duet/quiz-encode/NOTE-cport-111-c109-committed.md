# NOTE-cport-111: C109 COMMITTED b718d47 (band109 T10R93)

- 8dd89c2 partial-merge w2@1d55d5b (rgram.py +71, PINS +24,
  test N-list 1/1; 1 w2 commit R93, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6158/6158 py + SMOKE-GREEN.
- band109: rgramc.c --upto 50144. transpiler clean first try
  (tables 1775/1779).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3079/3079 GREEN +
  RGRAM-GREEN 6158/6158 py (merge tree, same-tree) +
  RGRAM-GREEN 6158/6158 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 686 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P96 next; == w2 tip now).
