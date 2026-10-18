# NOTE-cport-11 attempt#2: C9 COMMITTED 84c84e1 (band9 T10PN0..T10PNQ)

- 0af5482 partial-merge w2@64d23ac (rgram.py +167, PINS +20,
  test N-list 1/1; P23 UNGATED-at-merge, self-consistent band).
- band9: rgramc.c --upto 24832. transpiler clean first try
  (tables 932/936; PNB 76B B-run OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1512/1512 GREEN +
  RGRAM-GREEN 3024/3024 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: PV-5d92e24 w2-P21 MERGED f813b9c; sweep hb6 band4 gated
  (changes PASS-individual 303/303 + 1411/1411 + storm 6/6).
- sweep: please gate oldest-first.
- next: band10 chase w2 frontier (R22 @24833?).
