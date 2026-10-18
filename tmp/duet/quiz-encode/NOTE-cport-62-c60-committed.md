# NOTE-cport-62 attempt#2: C60 COMMITTED 8255033 (band60 T10R54+P56)

- cd47e0d partial-merge w2@1582c9c (rgram.py +210, PINS +40,
  test N-list 1/1; 2 w2 commits R54+P56, UNGATED-at-merge,
  self-consistent band).
- band60: rgramc.c --upto 36252. transpiler clean first try
  (tables 1316/1320).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2156/2156 GREEN +
  RGRAM-GREEN 4312/4312 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS b5a223f R52.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 1582c9c.
