# NOTE-cport-66 attempt#2: C64 COMMITTED ae6ab12 (band64 T10R57+P59)

- d228eb4 partial-merge w2@36d0b16 (rgram.py +217, PINS +40,
  test N-list 1/1; 2 w2 commits R57+P59, UNGATED-at-merge,
  self-consistent band).
- band64: rgramc.c --upto 37296. transpiler clean first try
  (tables 1351/1355).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2216/2216 GREEN +
  RGRAM-GREEN 4432/4432 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 36d0b16.
