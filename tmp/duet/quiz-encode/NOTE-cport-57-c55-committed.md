# NOTE-cport-57 attempt#2: C55 COMMITTED 8df33e4 (band55 T10P52)

- 0c53826 partial-merge w2@f89efe7 (rgram.py +144, PINS +20,
  test N-list 1/1; UNGATED-at-merge, self-consistent band).
- band55: rgramc.c --upto 34860. transpiler clean first try
  (tables 1271/1275).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2076/2076 GREEN +
  RGRAM-GREEN 4152/4152 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: band56 chase w2 5832f8b T10R51 (34861..35180).
