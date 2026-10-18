# NOTE-cport-92: C90 COMMITTED a735473 (band90 T10P79+T10R78)

- 3367c4b partial-merge w2@3a0891e (rgram.py +221, PINS +46,
  test N-list 1/1; 2 w2 commits P79+R78, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5348/5348 py + SMOKE-GREEN.
- band90: rgramc.c --upto 44576. transpiler clean first try
  (tables 1582/1586).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2674/2674 GREEN +
  RGRAM-GREEN 5348/5348 py (merge tree, same-tree) +
  RGRAM-GREEN 5348/5348 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 622 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P80 9740232 + R79 when committed).
