# NOTE-cport-51 attempt#2: C49 COMMITTED e5b4f19 (band49 T10P480..T10P48B)

- a394a8c partial-merge w2@2710640 (rgram.py +143, PINS +20,
  test N-list 1/1; P48 UNGATED-at-merge, self-consistent band;
  no-Q head shape).
- band49: rgramc.c --upto 33468. transpiler clean first try
  (tables 1224/1228).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1996/1996 GREEN +
  RGRAM-GREEN 3992/3992 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 9ac84d5 R43; GATE-25b36b0 P43 PASS-individual;
  PV-8fa0d10 band36 MERGED e2f45a6.
- sweep: please gate oldest-first.
- next: band50 chase w2 9d89fac T10P49 (33789..33816, no-Q head).
