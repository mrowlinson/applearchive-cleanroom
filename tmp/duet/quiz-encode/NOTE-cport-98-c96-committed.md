# NOTE-cport-98: C96 COMMITTED 0f3f997 (band96 T10P85+T10R84)

- f66b1b7 partial-merge w2@7d215eb (rgram.py +225, PINS +46,
  test N-list 1/1; 2 w2 commits P85+R84, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5624/5624 py + SMOKE-GREEN.
- band96: rgramc.c --upto 46664. transpiler clean first try
  (tables 1650/1654; R84 XOR-b29 construct handled).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2812/2812 GREEN +
  RGRAM-GREEN 5624/5624 py (merge tree, same-tree) +
  RGRAM-GREEN 5624/5624 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 646 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P86 fa795dd + R85 when committed).
