# NOTE-cport-85 attempt#2: C83 COMMITTED de31018 (band83 T10P73)

- b5620ea partial-merge w2@312aa28 (rgram.py +104, PINS +20,
  test N-list 1/1; UNGATED-at-merge, self-consistent band).
- band83: rgramc.c --upto 42168. transpiler clean first try
  (tables 1509/1513).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2523/2523 GREEN +
  RGRAM-GREEN 5046/5046 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 9c4264a cport band80.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 312aa28.
