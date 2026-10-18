# NOTE-cport-115: C113 COMMITTED 93555bb (band113 T10P98)

- 838e7bf partial-merge w2@f0949f2 (rgram.py +173, PINS +22,
  test N-list 1/1; 1 w2 commit P98, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6286/6286 py + SMOKE-GREEN.
- band113: rgramc.c --upto 50932. transpiler clean first try
  (tables 1809/1813).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3143/3143 GREEN +
  RGRAM-GREEN 6286/6286 py (merge tree, same-tree) +
  RGRAM-GREEN 6286/6286 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 696 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R96 next; == w2 tip now).
