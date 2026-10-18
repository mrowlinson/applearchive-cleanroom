# NOTE-cport-93: C91 COMMITTED 98b271f (band91 T10P80+T10R79)

- a883904 partial-merge w2@4a40af9 (rgram.py +215, PINS +46,
  test N-list 1/1; 2 w2 commits P80+R79, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5394/5394 py + SMOKE-GREEN.
- band91: rgramc.c --upto 44924. transpiler clean first try
  (tables 1593/1597).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2697/2697 GREEN +
  RGRAM-GREEN 5394/5394 py (merge tree, same-tree) +
  RGRAM-GREEN 5394/5394 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 626 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P81 0e56f23 + R80 when committed).
