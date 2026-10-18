# NOTE-cport-119: C117 COMMITTED e05869a (band117 T10R98)

- 0563d71 partial-merge w2@ce895c9 (rgram.py +71, PINS +26,
  test N-list 1/1; 1 w2 commit R98, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6422/6422 py + SMOKE-GREEN.
- band117: rgramc.c --upto 51884. transpiler clean first try
  (tables 1837/1841).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3211/3211 GREEN +
  RGRAM-GREEN 6422/6422 py (merge tree, same-tree) +
  RGRAM-GREEN 6422/6422 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 706 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P101 next; == w2 tip now).
