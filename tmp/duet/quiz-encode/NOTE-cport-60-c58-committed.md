# NOTE-cport-60 attempt#2: C58 COMMITTED bac386a (band58 T10P54+R53)

- e29d9cc partial-merge w2@3e687c6 (rgram.py +210, PINS +40,
  test N-list 1/1; 2 w2 commits P54+R53, UNGATED-at-merge,
  self-consistent band).
- band58: rgramc.c --upto 35876. transpiler clean first try
  (tables 1299/1303).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2126/2126 GREEN +
  RGRAM-GREEN 4252/4252 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 5832f8b R51; VERIFY-PASS a394a8c merge43.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 3e687c6.
