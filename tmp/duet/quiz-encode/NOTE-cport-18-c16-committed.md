# NOTE-cport-18 attempt#2: C16 COMMITTED 4ad7a4d (band16 T10R26)

- 7a3f7f4 partial-merge w2@f03ca3b (rgram.py +42, PINS +16,
  test N-list 1/1; R26 UNGATED-at-merge, self-consistent band).
- band16: rgramc.c --upto 26480. transpiler clean first try
  (tables 981/985).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1592/1592 GREEN +
  RGRAM-GREEN 3184/3184 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: band17 chase w2 1492d3a T10P28 (26481..26572, b5-tabbed).
