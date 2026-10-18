# NOTE-cport-35 attempt#2: C33 COMMITTED fd5dcca (band33 T10R37)

- 0a99a6e partial-merge w2@b1f4334 (rgram.py +49, PINS +20,
  test N-list 1/1; R37 UNGATED-at-merge, self-consistent band).
- band33: rgramc.c --upto 30308. transpiler clean first try
  (tables 1107/1111; b5-mbit OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1806/1806 GREEN +
  RGRAM-GREEN 3612/3612 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 59cbad2 (R33P35 merge); PV-1912c73 R31
  MERGED efabf2a; VERIFY-PASS c108d1e P36 92/92; GATE-0f16b53
  P34 PASS-individual.
- sweep: please gate oldest-first.
- next: band34 chase w2 35d6de7 T10P39 (30309..30400, xor-lencode).
