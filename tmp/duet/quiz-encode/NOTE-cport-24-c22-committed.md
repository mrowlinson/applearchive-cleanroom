# NOTE-cport-24 attempt#2: C22 COMMITTED 1cc206b (band22 T10R30)

- f1ffe3c partial-merge w2@8e0d740 (rgram.py +47, PINS +20,
  test N-list 1/1; R30 UNGATED-at-merge, self-consistent band).
- band22: rgramc.c --upto 27872. transpiler clean first try
  (tables 1027/1031; q=PVM-suf+qhead OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1666/1666 GREEN +
  RGRAM-GREEN 3332/3332 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: PV-02b44b4 band13 MERGED b7ccfd7; VERIFY-PASS 4c5b869 R28.
- sweep: please gate oldest-first.
- next: band23 chase w2 frontier.
