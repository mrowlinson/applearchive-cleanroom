# NOTE-cport-41 attempt#2: C39 COMMITTED a65016c (band39 T10P420..T10P42Q)

- 23f6d99 partial-merge w2@a0e16b3 (rgram.py +202, PINS +20,
  test N-list 1/1; P42 UNGATED-at-merge, self-consistent band).
- band39: rgramc.c --upto 31444. transpiler clean first try
  (tables 1152/1156; b21-rule OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1876/1876 GREEN +
  RGRAM-GREEN 3752/3752 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 0a99a6e (R37 merge); GATE-f43ec6a P37
  PASS-individual.
- sweep: please gate oldest-first.
- next: band40 chase w2 0c7b7fe T10R41 (31445..31700, xor-lencode).
