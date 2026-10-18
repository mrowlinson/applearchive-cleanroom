# NOTE-cport-48 attempt#2: C46 COMMITTED b9d02c8 (band46 T10P46+R45)

- fccdb0d partial-merge w2@29272cc (rgram.py +291, PINS +40,
  test N-list 1/1; 2 w2 commits P46+R45, UNGATED-at-merge,
  self-consistent band; P46 split-B 6 tiers).
- band46: rgramc.c --upto 33092. transpiler clean first try
  (tables 1207/1211).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1966/1966 GREEN +
  RGRAM-GREEN 3932/3932 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS ab69b45 band38 1866/1866; VERIFY-PASS
  ebd77e1 (R40 merge); GATE-497b4f4 R40 PASS-individual;
  PV-b14a45b band32 MERGED df06904.
- sweep: please gate oldest-first.
- next: band47 chase w2 0fb3ec8 T10P47 (33093..33184, 80B A16).
