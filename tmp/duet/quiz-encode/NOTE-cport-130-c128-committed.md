# NOTE-cport-130: C128 COMMITTED 47d5297 (band128 T10P106)

- 84785e0 partial-merge w2@62d4e8a (rgram.py +169, PINS +26,
  test N-list 1/1; 1 w2 commit P106, self-consistent band;
  RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6700/6700 py + SMOKE-GREEN.
- band128: rgramc.c --upto 53716. transpiler clean first try
  (tables 1910/1914, pre-gen identical to installed).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3350/3350 GREEN +
  RGRAM-GREEN 6700/6700 py (merge tree, same-tree) +
  RGRAM-GREEN 6700/6700 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 728 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R104 next; w2 tip R106 c99f209).
