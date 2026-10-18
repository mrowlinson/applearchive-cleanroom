# NOTE-cport-34 attempt#2: C32 COMMITTED b14a45b (band32 T10R36+P38)

- d605333 partial-merge w2@1b1e2f3 (rgram.py +252, PINS +40,
  test N-list 1/1; 2 w2 commits R36+P38, UNGATED-at-merge,
  self-consistent band).
- band32: rgramc.c --upto 30052. transpiler clean first try
  (tables 1104/1108; b29-rule OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1796/1796 GREEN +
  RGRAM-GREEN 3592/3592 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: GATE-336a303 band23 PASS-functional; VERIFY-PASS c440e04
  (P34 merge); PV-8e4f4f2 P32 MERGED 29b17ce; GATE-b689490 R32
  PASS-individual.
- sweep: please gate oldest-first.
- next: band33 chase w2 b1f4334 T10R37 (30053..30308, b5-mbit).
