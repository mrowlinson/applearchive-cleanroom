# NOTE-cport-96: C94 COMMITTED fecaa3d (band94 T10P83+T10R82)

- 8233b06 partial-merge w2@fd558ad (rgram.py +215, PINS +46,
  test N-list 1/1; 2 w2 commits P83+R82, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5532/5532 py + SMOKE-GREEN.
- band94: rgramc.c --upto 45968. transpiler clean first try
  (tables 1626/1630).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2766/2766 GREEN +
  RGRAM-GREEN 5532/5532 py (merge tree, same-tree) +
  RGRAM-GREEN 5532/5532 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 638 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P84 ed8d830 + R83 e0b4455 ready).
