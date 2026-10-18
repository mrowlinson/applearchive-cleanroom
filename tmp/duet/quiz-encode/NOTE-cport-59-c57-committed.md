# NOTE-cport-59 attempt#2: C57 COMMITTED 790b284 (band57 T10R52)

- 2f50789 partial-merge w2@b5a223f (rgram.py +108, PINS +20,
  test N-list 1/1; AM-full q; UNGATED-at-merge,
  self-consistent band).
- band57: rgramc.c --upto 35528. transpiler clean first try
  (tables 1288/1292).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2106/2106 GREEN +
  RGRAM-GREEN 4212/4212 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond b5a223f.
