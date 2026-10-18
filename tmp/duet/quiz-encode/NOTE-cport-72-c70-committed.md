# NOTE-cport-72 attempt#2: C70 COMMITTED 80d12c7 (band70 T10P63)

- 2a7fa9a partial-merge w2@5e0909c (rgram.py +102, PINS +20,
  test N-list 1/1; UNGATED-at-merge, self-consistent band).
- band70: rgramc.c --upto 38688. transpiler clean first try
  (tables 1395/1399).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2296/2296 GREEN +
  RGRAM-GREEN 4592/4592 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 5e0909c.
