# NOTE-cport-12 attempt#2: C10 COMMITTED a99d06a (band10 T10R22)

- d6ad91c partial-merge w2@85fe578 (rgram.py +43, PINS +16,
  test N-list 1/1; R22 UNGATED-at-merge, self-consistent band).
- band10: rgramc.c --upto 25088. transpiler clean first try
  (tables 934/938).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1520/1520 GREEN +
  RGRAM-GREEN 3040/3040 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 64d23ac T10P23 92/92; w2 deriving R23/P24
  (Q-38 filed, not committed yet).
- sweep: please gate oldest-first.
- next: band11 chase w2 frontier (P24/R23 when committed).
