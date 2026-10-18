# NOTE-cport-84 attempt#2: C82 COMMITTED 7c309fc (band82 T10P72+R71)

- 91f70b6 partial-merge w2@60aa85b (rgram.py +234, PINS +46,
  test N-list 1/1; 2 w2 commits P72+R71, UNGATED-at-merge,
  self-consistent band).
- band82: rgramc.c --upto 42140. transpiler clean first try
  (tables 1503/1507).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2513/2513 GREEN +
  RGRAM-GREEN 5026/5026 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 60aa85b.
