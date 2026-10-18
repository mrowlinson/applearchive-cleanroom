# NOTE-cport-65 attempt#2: C63 COMMITTED f8fc439 (band63 T10P58)

- eaed6ba partial-merge w2@1165cfa (rgram.py +102, PINS +20,
  test N-list 1/1; UNGATED-at-merge, self-consistent band).
- band63: rgramc.c --upto 36948. transpiler clean first try
  (tables 1339/1343).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2196/2196 GREEN +
  RGRAM-GREEN 4392/4392 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 1582c9c P56.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 1165cfa.
