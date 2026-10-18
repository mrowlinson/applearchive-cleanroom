# NOTE-cport-106: C104 COMMITTED 2c55063 (band104 T10P93)

- 8974afa partial-merge w2@c4e3cfa (rgram.py +174, PINS +36,
  test N-list 1/1; 1 w2 commit P93, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6032/6032 py + SMOKE-GREEN.
- band104: rgramc.c --upto 49192. transpiler clean first try
  (tables 1746/1750).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3016/3016 GREEN +
  RGRAM-GREEN 6032/6032 py (merge tree, same-tree) +
  RGRAM-GREEN 6032/6032 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 676 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R91 when committed; == w2 tip now).
