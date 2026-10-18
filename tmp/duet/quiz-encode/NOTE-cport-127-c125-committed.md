# NOTE-cport-127: C125 COMMITTED 68d2eef (band125 T10R102)

- 49c1fa2 partial-merge w2@5ba2fe3 (rgram.py +53, PINS +26,
  test N-list 1/1; 1 w2 commit R102, self-consistent band;
  RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6626/6626 py + SMOKE-GREEN.
- band125: rgramc.c --upto 53276. transpiler clean first try
  (tables 1887/1891, pre-gen identical to installed).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3313/3313 GREEN +
  RGRAM-GREEN 6626/6626 py (merge tree, same-tree) +
  RGRAM-GREEN 6626/6626 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 722 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P105 next; w2 tip R103 26a5a51).
