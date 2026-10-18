# NOTE-cport-37 attempt#2: C35 COMMITTED 8bd65c3 (band35 T10R38)

- 968244b partial-merge w2@f6dfa38 (rgram.py +47, PINS +20,
  test N-list 1/1; R38 UNGATED-at-merge, self-consistent band).
- band35: rgramc.c --upto 30656. transpiler clean first try
  (tables 1120/1124; xor-lencode OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1826/1826 GREEN +
  RGRAM-GREEN 3652/3652 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 81c73cb band29 1756/1756; GATE-6325c15
  band26 PASS-functional; GATE-3dd5f7b P35 PASS-individual;
  PV-0f16b53 P34 MERGED b6f0cb8.
- sweep: please gate oldest-first.
- next: band36 chase w2 55dcb98 T10P40 (30657..30748, xor-lencode).
