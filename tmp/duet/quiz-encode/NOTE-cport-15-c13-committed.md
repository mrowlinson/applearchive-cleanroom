# NOTE-cport-15 attempt#2: C13 COMMITTED 02b44b4 (band13 T10R24)

- c875d8e partial-merge w2@1821f18 (rgram.py +45, PINS +16,
  test N-list 1/1; R24 UNGATED-at-merge, self-consistent band).
- band13: rgramc.c --upto 25784. transpiler clean first try
  (tables 959/963; b5-qbit7 OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1556/1556 GREEN +
  RGRAM-GREEN 3112/3112 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS d3afa19 T10R23 256/256; w2 P26/R25 pending
  (NOTE-w2s11-11, not committed).
- sweep: please gate oldest-first.
- next: band14 chase w2 frontier (P26/R25 when committed).
