# NOTE-cport-52 attempt#2: C50 COMMITTED ac1ec02 (band50 T10R47+P49)

- bc2dbcf partial-merge w2@9d89fac (rgram.py +251, PINS +40,
  test N-list 1/1; 2 w2 commits R47+P49, UNGATED-at-merge,
  self-consistent band; R47 A+B shape OK).
- band50: rgramc.c --upto 33816. transpiler clean first try
  (tables 1235/1239).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2016/2016 GREEN +
  RGRAM-GREEN 4032/4032 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: GATE-cf113e3 R42 PASS-individual; GATE-1b84bca band40
  PASS-functional.
- sweep: please gate oldest-first.
- next: band51 chase w2 838cde4 T10R48 (33817..34136, b8 rule).
