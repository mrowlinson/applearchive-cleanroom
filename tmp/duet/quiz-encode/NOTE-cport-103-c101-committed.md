# NOTE-cport-103: C101 COMMITTED 4798cde (band101 T10P90+T10R89)

- 174f8a4 partial-merge w2@0022950 (rgram.py +243, PINS +62,
  test N-list 1/1; 2 w2 commits P90+R89, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5870/5870 py + SMOKE-GREEN.
- band101: rgramc.c --upto 48404. transpiler clean first try
  (tables 1711/1715; P90 92-cell P-head handled).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2935/2935 GREEN +
  RGRAM-GREEN 5870/5870 py (merge tree, same-tree) +
  RGRAM-GREEN 5870/5870 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 666 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P91 182438b + R90 when committed).
