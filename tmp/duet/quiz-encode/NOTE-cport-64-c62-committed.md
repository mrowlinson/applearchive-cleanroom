# NOTE-cport-64 attempt#2: C62 COMMITTED 6a04351 (band62 T10P57+R56)

- 6b8939e partial-merge w2@3dfc862 (rgram.py +210, PINS +40,
  test N-list 1/1; 2 w2 commits P57+R56, UNGATED-at-merge,
  self-consistent band).
- band62: rgramc.c --upto 36920. transpiler clean first try
  (tables 1333/1337).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2186/2186 GREEN +
  RGRAM-GREEN 4372/4372 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 3dfc862.
