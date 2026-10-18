# NOTE-cport-36 attempt#2: C34 COMMITTED 745afe2 (band34 T10P390..T10P39Q)

- 6a60609 partial-merge w2@35d6de7 (rgram.py +202, PINS +20,
  test N-list 1/1; P39 UNGATED-at-merge, self-consistent band).
- band34: rgramc.c --upto 30400. transpiler clean first try
  (tables 1117/1121; xor-lencode + b17-rule OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1816/1816 GREEN +
  RGRAM-GREEN 3632/3632 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 1050d3d (R34 merge); PV-b689490 R32 MERGED
  a882096; VERIFY-PASS 965f4dd R35 256/256.
- sweep: please gate oldest-first.
- next: band35 chase w2 f6dfa38 T10R38 (30401..30656, xor-lencode).
