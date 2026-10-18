# NOTE-cport-10 attempt#2: C8 COMMITTED b6a42aa (band8 T10R21)

- 10eb4bb partial-merge w2@f67973d (rgram.py +45, PINS +16,
  test N-list 1/1; R21 UNGATED-at-merge, self-consistent band).
- band8: rgramc.c --upto 24740. transpiler clean first try
  (tables 923/927; q=PMM reuse OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1502/1502 GREEN +
  RGRAM-GREEN 3004/3004 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN. spot 2/2 SAME (R21 ends).
- seen: VERIFY-PASS f145c51 (P22 merge); PV-c12fcc6 band3 MERGED
  ff02b82; sweep hb5 (P21 PASS-individual, queue incl b4/b5).
- sweep: please gate oldest-first.
- next: band9 chase w2 64d23ac T10P23 (24741..24832, PNB first 76B B-run).
