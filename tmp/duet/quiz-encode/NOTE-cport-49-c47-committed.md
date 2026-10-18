# NOTE-cport-49 attempt#2: C47 COMMITTED 6ac1af1 (band47 T10P470..T10P47Q)

- ba8c96d partial-merge w2@0fb3ec8 (rgram.py +198, PINS +20,
  test N-list 1/1; P47 UNGATED-at-merge, self-consistent band).
- band47: rgramc.c --upto 33184. transpiler clean first try
  (tables 1216/1220; 80B A16 + row-heads OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1976/1976 GREEN +
  RGRAM-GREEN 3952/3952 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: GATE-a0e16b3 P42 PASS-individual.
- sweep: please gate oldest-first.
- next: band48 chase w2 804eb41 T10R46 (33185..33440, 80B pay).
