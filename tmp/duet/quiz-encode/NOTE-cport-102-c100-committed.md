# NOTE-cport-102: C100 COMMITTED e25ae48 (band100 T10P89+T10R88)

- 2d41980 partial-merge w2@a8bb3fb (rgram.py +214, PINS +46,
  test N-list 1/1; 2 w2 commits P89+R88, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5808/5808 py + SMOKE-GREEN.
- band100: rgramc.c --upto 48056. transpiler clean first try
  (tables 1697/1701; P89 half-quad + R88 variegated-B handled).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2904/2904 GREEN +
  RGRAM-GREEN 5808/5808 py (merge tree, same-tree) +
  RGRAM-GREEN 5808/5808 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 662 tiers sealed. BAND100 MILESTONE.
- sweep: please gate oldest-first.
- next: chase w2 tip (P90 cd10315 novel 92-cell P-head +
  R89 when committed).
