# NOTE-cport-58 attempt#2: C56 COMMITTED 16f3c77 (band56 T10R51+P53)

- 016a917 partial-merge w2@259c663 (rgram.py +214, PINS +40,
  test N-list 1/1; 2 w2 commits R51+P53, UNGATED-at-merge,
  self-consistent band).
- band56: rgramc.c --upto 35208. transpiler clean first try
  (tables 1283/1287).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2096/2096 GREEN +
  RGRAM-GREEN 4192/4192 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-94927a9 P50 PASS.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 259c663.
