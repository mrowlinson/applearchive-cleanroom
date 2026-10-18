# NOTE-cport-75 attempt#2: C73 COMMITTED d0484b7 (band73 T10P65+R64)

- b4de394 partial-merge w2@012efda (rgram.py +215, PINS +46,
  test N-list 1/1; 2 w2 commits P65+R64, UNGATED-at-merge,
  self-consistent band).
- band73: rgramc.c --upto 39704. transpiler clean first try
  (tables 1424/1428).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2352/2352 GREEN +
  RGRAM-GREEN 4704/4704 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 012efda.
