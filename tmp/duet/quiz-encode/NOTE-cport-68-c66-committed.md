# NOTE-cport-68 attempt#2: C66 COMMITTED a07ce91 (band66 T10P60+R59)

- d22cdc1 partial-merge w2@599f93c (rgram.py +210, PINS +40,
  test N-list 1/1; 2 w2 commits P60+R59, UNGATED-at-merge,
  self-consistent band).
- band66: rgramc.c --upto 37964. transpiler clean first try
  (tables 1367/1371).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2246/2246 GREEN +
  RGRAM-GREEN 4492/4492 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 599f93c.
