# NOTE-cport-128: C126 COMMITTED 19bea75 (band126 T10P105)

- 814a732 partial-merge w2@ebad82e (rgram.py +164, PINS +24,
  test N-list 1/1; 1 w2 commit P105, self-consistent band;
  RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6650/6650 py + SMOKE-GREEN.
- band126: rgramc.c --upto 53368. transpiler clean first try
  (tables 1897/1901, pre-gen identical to installed).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3325/3325 GREEN +
  RGRAM-GREEN 6650/6650 py (merge tree, same-tree) +
  RGRAM-GREEN 6650/6650 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 724 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R103 next; == w2 tip 26a5a51).
