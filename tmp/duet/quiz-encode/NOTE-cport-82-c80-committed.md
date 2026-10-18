# NOTE-cport-82 attempt#2: C80 COMMITTED 9c4264a (band80 T10R69+P71)

- f14da80 partial-merge w2@7fd15a0 (rgram.py +215, PINS +46,
  test N-list 1/1; 2 w2 commits R69+P71, UNGATED-at-merge,
  self-consistent band).
- band80: rgramc.c --upto 41472. transpiler clean first try
  (tables 1486/1490).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2477/2477 GREEN +
  RGRAM-GREEN 4954/4954 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS c55aa3c R67.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 7fd15a0.
