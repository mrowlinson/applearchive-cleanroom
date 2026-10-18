# NOTE-cport-19 attempt#2: C17 COMMITTED 64b7f1a (band17 T10PS0..T10PSQ)

- 20363af partial-merge w2@1492d3a (rgram.py +165, PINS +20,
  test N-list 1/1; P28 UNGATED-at-merge, self-consistent band).
- band17: rgramc.c --upto 26572. transpiler clean first try
  (tables 990/994; b5-tabbed OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1602/1602 GREEN +
  RGRAM-GREEN 3204/3204 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 11cfc70 T10R25 256/256; GATE-9783bf5 P25
  PASS-individual; sweep hb21 queue incl b11..b13.
- sweep: please gate oldest-first.
- next: band18 chase w2 e5fb39a T10R27 (26573..26828, q=PSM reuse).
