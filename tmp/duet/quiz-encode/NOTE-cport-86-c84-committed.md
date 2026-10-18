# NOTE-cport-86 attempt#2: C84 COMMITTED b6151b1 (band84 T10R72+P74)

- bea3fac partial-merge w2@9fb2c01 (rgram.py +214, PINS +46,
  test N-list 1/1; 2 w2 commits R72+P74, UNGATED-at-merge,
  self-consistent band).
- band84: rgramc.c --upto 42516. transpiler clean first try
  (tables 1520/1524). 600-tier milestone.
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2546/2546 GREEN +
  RGRAM-GREEN 5092/5092 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 312aa28 P73.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 9fb2c01.
