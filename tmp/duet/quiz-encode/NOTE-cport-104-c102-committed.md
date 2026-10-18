# NOTE-cport-104: C102 COMMITTED 6436cf2 (band102 T10P91+T10R90)

- 76fbe66 partial-merge w2@e1cf3d8 (rgram.py +214, PINS +60,
  test N-list 1/1; 2 w2 commits P91+R90, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5930/5930 py + SMOKE-GREEN.
- band102: rgramc.c --upto 48752. transpiler clean first try
  (tables 1722/1726).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2965/2965 GREEN +
  RGRAM-GREEN 5930/5930 py (merge tree, same-tree) +
  RGRAM-GREEN 5930/5930 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 670 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P92 07de9d4 + R91 when committed;
  ~48k est nearly reached).
