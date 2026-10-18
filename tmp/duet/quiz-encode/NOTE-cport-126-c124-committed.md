# NOTE-cport-126: C124 COMMITTED 7081fd5 (band124 T10P104)

- dc5d75b partial-merge w2@6ee19e7 (rgram.py +164, PINS +24,
  test N-list 1/1; 1 w2 commit P104, predecessor-committed,
  self-consistent band; RGRAM_BIN override kept).
- merge-tree gate first-hand: RGRAM-GREEN 6600/6600 py + SMOKE-GREEN
  (same tree as band gates; rgram.py untouched by C port).
- band124: rgramc.c --upto 53020. transpiler clean first try
  (tables 1885/1889, regen-identical).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3300/3300 GREEN +
  RGRAM-GREEN 6600/6600 py (merge tree, same-tree) +
  RGRAM-GREEN 6600/6600 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 720 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R102 next; w2 tip R103 26a5a51).
