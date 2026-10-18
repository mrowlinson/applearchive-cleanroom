# NOTE-cport-50 attempt#2: C48 COMMITTED 528b83c (band48 T10R46)

- 75d3b00 partial-merge w2@804eb41 (rgram.py +53, PINS +20,
  test N-list 1/1; R46 UNGATED-at-merge, self-consistent band).
- band48: rgramc.c --upto 33440. transpiler clean first try
  (tables 1218/1222; 80B pay OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1986/1986 GREEN +
  RGRAM-GREEN 3972/3972 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 25b36b0 P43; PV-745afe2 band34 MERGED
  f6fa86e; GATE-0c7b7fe R41 PASS-individual.
- sweep: please gate oldest-first.
- next: band49 chase w2 2710640 T10P48 (33441..33468, no-Q head).
