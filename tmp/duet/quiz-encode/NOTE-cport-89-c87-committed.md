# NOTE-cport-89: C87 COMMITTED d68dbff (band87 T10P76+T10R75)

- c179b2c partial-merge w2@365b4b2 (rgram.py +214, PINS +46,
  test N-list 1/1; 2 w2 commits P76+R75, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5210/5210 py + SMOKE-GREEN.
- band87: rgramc.c --upto 43532. transpiler clean first try
  (tables 1547/1551).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2605/2605 GREEN +
  RGRAM-GREEN 5210/5210 py (merge tree, same-tree) +
  RGRAM-GREEN 5210/5210 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 610 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P77 1dd20b6 + R76 when committed).
