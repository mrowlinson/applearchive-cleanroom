# NOTE-cport-99: C97 COMMITTED 0e64e61 (band97 T10P86+T10R85)

- fa89957 partial-merge w2@f418d14 (rgram.py +215, PINS +46,
  test N-list 1/1; 2 w2 commits P86+R85, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5670/5670 py + SMOKE-GREEN.
- band97: rgramc.c --upto 47012. transpiler clean first try
  (tables 1661/1665).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2835/2835 GREEN +
  RGRAM-GREEN 5670/5670 py (merge tree, same-tree) +
  RGRAM-GREEN 5670/5670 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 650 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P87 19694c0 + R86 when committed).
